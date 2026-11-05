"""
ATC Clean Core Assessment Dashboard Generator
==============================================
Parses an ATC findings ZIP export and generates a self-contained HTML dashboard
in SAP Horizon look & feel, covering:

  - Run metadata header
  - KPI summary: total score, potential score, level distribution
  - Top packages by technical debt score (bar chart)
  - Top objects by technical debt score
  - Top objects by Level D (Priority 1) findings
  - Top referenced SAP objects by impact
  - Per top-package: top 3 referenced SAP objects
  - Potential score analysis (successor-available findings)

Usage:
  python scripts/generate_dashboard.py <path-to-atc-zip> [--out <output.html>] [--top <N>]

In-scope check classes (per KPI definition):
  CL_YCM_CC_CHECK_API_USAGE        Usage of APIs
  CL_CI_TEST_CRITICAL_STATEMENTS   Critical statements
  CL_CI_TEST_ADMISSIBLE_ENHANCM    Allowed SAP enhancement technologies
"""

import argparse
import json
import sys
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

IN_SCOPE_CHECKS = {
    "CL_YCM_CC_CHECK_API_USAGE",
    "CL_CI_TEST_CRITICAL_STATEMENTS",
    "CL_CI_TEST_ADMISSIBLE_ENHANCM",
}

PRIO_WEIGHT = {"1": 10, "2": 5, "3": 1}
PRIO_LABEL  = {"1": "Error (P1)", "2": "Warning (P2)", "3": "Info (P3)"}
LEVEL_LABEL = {"1": "Level D", "2": "Level C", "3": "Level B"}
LEVEL_COLOR = {"1": "#bb0000", "2": "#e76500", "3": "#0070f2"}

# Object types that can be set to ABAP Cloud Language Version (Level A capable).
# These are repository object types that the ABAP development environment allows
# to run under the restricted "ABAP for Cloud Development" language version.
# All other types (PROG, SSFO, SFPF, VIEW, WAPA, ENHO, FUGS, FUGX, …) are capped
# at Level B* — their technical debt score can reach 0 but they cannot be placed
# under ABAP Cloud Language Version technically.
LEVEL_A_CAPABLE_TYPES = {
    "BDEF",  # behavior definition (RAP-native, designed for ABAP Cloud Development)
    "CLAS",  # ABAP class
    "INTF",  # ABAP interface
    "FUNC",  # function module (when counted individually, see FUGR/FUNC logic)
    "FUGR",  # function group (only when all sub-objects are FUNC; kept for pkg-level)
    "DDLS",  # CDS view / data definition
    "DTEL",  # data element (not a focus type but can carry ABAP Cloud Language Version)
    # Note: TABL is not a focus type (excluded from KPIs per RISE Dashboard).
    # Note: DOMA is a non-focus type (excluded from KPIs) — not listed here
}

# "Focus object types" — the curated set of logic-bearing object types used for all
# KPI calculations (Technical Debt Score, Clean Core Level distribution, etc.).
# Defined by SAP Note 3761018 (Version 3, released 02.09.2026) as the 10 official
# focus object types for the RISE with SAP Methodology Dashboard.
# Non-logic-bearing types (DTEL, DOMA, TABL, TTYP, …) are tracked but excluded from KPIs.
FOCUS_OBJECT_TYPES = {
    "BDEF",  # behavior definition (added per SAP Note 3761018)
    "CLAS",  # ABAP class
    "INTF",  # ABAP interface
    "FUNC",  # function module (individually counted, see FUGR/FUNC logic)
    "FUGR",  # function group
    "FUGX",  # function group with customer include (customer part)
    "PROG",  # program / include
    "DDLS",  # CDS view / data definition
    "ENHO",  # enhancement implementation
    "SXCI",  # business add-in implementation (added per SAP Note 3761018)
}

DATA_DIR = Path(__file__).parent / "data"


# ---------------------------------------------------------------------------
# Cloudification Repository loader
# ---------------------------------------------------------------------------

def load_cr_lookup() -> tuple[dict, dict, dict]:
    """
    Returns:
      released_lookup  keyed by (obj_type, obj_name) -> True
      classic_lookup   keyed by (obj_type, obj_name) -> True
      cr_detail        keyed by (obj_type, obj_name) -> full CR entry dict
    """
    released_lookup = {}
    classic_lookup  = {}
    cr_detail       = {}

    release_file = DATA_DIR / "objectReleaseInfo_PCELatest.json"
    class_file   = DATA_DIR / "objectClassifications_SAP.json"

    if release_file.exists():
        data = json.loads(release_file.read_text(encoding="utf-8"))
        for item in data.get("objectReleaseInfo", []):
            key = (item.get("objectType", ""), item.get("objectKey", ""))
            cr_detail[key] = item
            if item.get("state") == "released":
                released_lookup[key] = True

    if class_file.exists():
        data = json.loads(class_file.read_text(encoding="utf-8"))
        for item in data.get("objectClassifications", []):
            key = (item.get("objectType", ""), item.get("objectKey", ""))
            if key not in cr_detail:
                cr_detail[key] = item
            if item.get("state") == "classicAPI":
                classic_lookup[key] = True

    return released_lookup, classic_lookup, cr_detail


def load_cr_metadata() -> dict:
    meta_file = DATA_DIR / "cr_metadata.json"
    if meta_file.exists():
        return json.loads(meta_file.read_text(encoding="utf-8"))
    return {}


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def parse_zip(zip_path: str):
    """
    Returns:
      settings  - dict of run metadata from atc_settings.xml
      findings  - list of dicts, one per in-scope finding
      excluded  - count of out-of-scope findings
    """
    settings = {}
    findings = []
    excluded = 0

    with zipfile.ZipFile(zip_path) as zf:
        names = zf.namelist()

        # settings
        if "atc_settings.xml" in names:
            root = ET.fromstring(zf.read("atc_settings.xml").decode("utf-8"))
            s = root.find("atc_settings")
            if s is not None:
                for child in s:
                    settings[child.tag] = child.text or ""

        # findings files
        finding_files = sorted(n for n in names if n.startswith("atc_findings_") and n.endswith(".xml"))
        for fname in finding_files:
            root = ET.fromstring(zf.read(fname).decode("utf-8"))
            for f in root.findall(".//finding"):
                check = (f.findtext("check_class") or "").upper()
                if check not in IN_SCOPE_CHECKS:
                    excluded += 1
                    continue
                findings.append({
                    "priority":    f.findtext("priority") or "",
                    "obj_type":    f.findtext("obj_type") or "",
                    "obj_name":    f.findtext("obj_name") or "",
                    "sub_type":    f.findtext("sub_type") or "",
                    "sub_name":    f.findtext("sub_name") or "",
                    "package":     f.findtext("package_name") or "",
                    "ref_type":    f.findtext("ref_obj_type") or "",
                    "ref_name":    f.findtext("ref_obj_name") or "",
                    "check_class": check,
                    "msg_code":    f.findtext("message_code") or "",
                    "has_successor": (f.findtext("message_code") or "").endswith("_SUC"),
                })

    return settings, findings, excluded


# ---------------------------------------------------------------------------
# Scoring & aggregation
# ---------------------------------------------------------------------------

def weighted_score(p1: int, p2: int, p3: int) -> int:
    return p1 * 10 + p2 * 5 + p3 * 1


def aggregate(findings: list, released_lookup: dict, classic_lookup: dict, cr_detail: dict):
    """
    Returns a big dict with all aggregated data needed for the dashboard.
    Only findings for FOCUS_OBJECT_TYPES are counted in KPIs (score, level distribution).
    Non-focus objects are tracked separately and reported in the run bar but not in any KPI.
    """
    # Message codes that indicate table write access (P1 Error)
    TABL_WRITE_CODES = {"UPDATE", "UPDATE_SUC"}
    # Message codes that indicate table read access (P2 Warning)
    TABL_READ_CODES  = {"SELECT", "SELECT_SUC", "DB_TAB_CDS", "DB_TAB_SUC"}

    # per-object counters (focus types only)
    obj_prio      = defaultdict(lambda: {"1": 0, "2": 0, "3": 0})
    obj_pkg       = {}
    obj_type      = {}
    obj_suc       = defaultdict(lambda: {"1": 0, "2": 0, "3": 0})  # _SUC findings per obj
    obj_pot_score = defaultdict(int)  # accumulates residual score after successor migration

    # non-focus objects: tracked for the run bar, excluded from all KPIs
    non_focus_objs  = {}   # (obj_name, eff_type) -> {"package": ..., "score": ..., "level": ...}
    non_focus_prio  = defaultdict(lambda: {"1": 0, "2": 0, "3": 0})

    # per-object successor detail: list of (ref_type, ref_name, access_mode, prio, cr_entry)
    obj_suc_detail = defaultdict(list)

    # per-package counters
    pkg_prio   = defaultdict(lambda: {"1": 0, "2": 0, "3": 0})
    pkg_suc    = defaultdict(lambda: {"1": 0, "2": 0, "3": 0})

    # referenced SAP objects (global) — keyed by (ref_name, access_mode) for TABL
    ref_impact  = defaultdict(int)
    ref_custom  = defaultdict(set)
    ref_type_map = {}               # display_ref_name -> ref_obj_type

    # referenced SAP objects that have a known successor (_SUC findings only)
    ref_suc_impact   = defaultdict(int)
    ref_suc_custom   = defaultdict(set)   # display_ref -> set of obj_names
    ref_suc_packages = defaultdict(set)   # display_ref -> set of package names
    ref_suc_count    = defaultdict(int)   # display_ref -> number of _SUC findings

    # per-package: ref_name -> score within package
    pkg_ref_impact = defaultdict(lambda: defaultdict(int))
    pkg_pot_score  = defaultdict(int)  # accumulates residual score per package

    # successor potential score
    suc_potential_released = 0  # score reduction if successor is released (-> 0 pts)
    suc_potential_classic  = 0  # score reduction if successor is classic (-> 1 pt)
    suc_unknown_score      = 0  # score from _SUC findings where CR lookup gives no info

    for f in findings:
        raw_obj_type = f["obj_type"]
        raw_obj_name = f["obj_name"]
        sub_type     = f.get("sub_type", "")
        sub_name     = f.get("sub_name", "")

        # FUGR/FUNC remapping: when the ATC finding is on a function module
        # (sub_type == FUNC) inside a function group (obj_type == FUGR), count
        # it under the individual function module (sub_name) rather than the
        # function group. This matches the RISE Dashboard logic.
        # For other FUGR sub-objects (INCL, etc.) and exotic types (FUGX, FUGS),
        # keep the original function group as the object key.
        if raw_obj_type == "FUGR" and sub_type == "FUNC" and sub_name:
            obj_name  = sub_name
            eff_type  = "FUNC"
        else:
            obj_name  = raw_obj_name
            eff_type  = raw_obj_type

        # Use (name, type) as the composite key — same object name with different
        # obj_types in the ATC export are distinct objects (matches RISE Dashboard logic).
        obj = (obj_name, eff_type)

        pkg  = f["package"] or "UNKNOWN"
        prio  = f["priority"]
        ref   = f["ref_name"]
        rtype = f["ref_type"]
        msg   = f["msg_code"]

        # Object Type Harmonization: only "focus" (logic-bearing) object types count
        # toward KPIs. Non-focus types (VIEW, SSFO, SFPF, FUGS, DOMA, WAPA, …) are
        # tracked in a separate counter and shown in the run bar but excluded from all
        # score and level calculations. Aligns with RISE Dashboard (September 2026).
        if eff_type not in FOCUS_OBJECT_TYPES:
            if msg != "DPRCTD_SUC":
                non_focus_prio[obj][prio] += 1
            non_focus_objs[obj] = {"package": pkg, "type": eff_type}
            continue

        obj_pkg[obj]  = pkg
        obj_type[obj] = eff_type

        # DPRCTD_SUC findings are not counted in the Technical Debt Score — they
        # carry a known successor and are only tracked for potential score calculation.
        # All other findings (including other _SUC codes like SELECT_SUC, TC_CLA_SUC)
        # are counted normally. This matches RISE Dashboard behaviour.
        if msg != "DPRCTD_SUC":
            obj_prio[obj][prio] += 1
            pkg_prio[pkg][prio] += 1

        pts = PRIO_WEIGHT.get(prio, 0)

        # Determine access mode for TABL references
        if rtype == "TABL":
            if msg in TABL_WRITE_CODES or (f["has_successor"] and msg.replace("_SUC","") in {"UPDATE"}):
                access_mode = "Write"
            elif msg in TABL_READ_CODES or (f["has_successor"] and msg.replace("_SUC","") in {"SELECT","DB_TAB"}):
                access_mode = "Read"
            else:
                access_mode = "Read"  # default for TABL
            display_ref = f"{ref} (TABL, {access_mode})"
        else:
            access_mode = ""
            display_ref = ref

        if ref:
            ref_impact[display_ref] += pts
            ref_custom[display_ref].add(obj)
            pkg_ref_impact[pkg][display_ref] += pts
            if display_ref not in ref_type_map:
                ref_type_map[display_ref] = rtype
            if f["has_successor"]:
                ref_suc_impact[display_ref] += pts
                ref_suc_custom[display_ref].add(obj)
                ref_suc_packages[display_ref].add(pkg)
                ref_suc_count[display_ref] += 1

        if f["has_successor"]:
            obj_suc[obj][prio] += 1
            pkg_suc[pkg][prio] += 1
            cr_key = (rtype, ref)
            cr_entry = cr_detail.get(cr_key, {})
            if cr_key in released_lookup:
                suc_potential_released += pts
                residual = 0
            elif cr_key in classic_lookup:
                suc_potential_classic += max(0, pts - 1)
                residual = 1
            else:
                suc_potential_classic += max(0, pts - 1)
                residual = 1

            # TABL write with CDS successor → flag as insufficient for write operations
            is_tabl_write = (rtype == "TABL" and access_mode == "Write")
            suc_class = cr_entry.get("successorClassification", "")
            successors = cr_entry.get("successors", [])
            suc_concept = cr_entry.get("successorConceptName", "")
            # CDS successors cover read but not write
            suc_is_cds_only = any(
                s.get("objectType", "") in ("CDS_STOB", "DDLS") for s in successors
            ) and not any(
                s.get("objectType", "") not in ("CDS_STOB", "DDLS") for s in successors
            )
            write_warning = is_tabl_write and (suc_is_cds_only or suc_class == "concept")

            obj_pot_score[obj] += residual
            pkg_pot_score[pkg] += residual

            # Store detail for show-more panel
            obj_suc_detail[obj].append({
                "ref_type":    rtype,
                "ref_name":    ref,
                "access_mode": access_mode,
                "display_ref": display_ref,
                "prio":        prio,
                "msg":         msg,
                "suc_class":   suc_class,
                "successors":  successors,
                "suc_concept": suc_concept,
                "write_warning": write_warning,
                "cr_state":    cr_entry.get("state", ""),
            })
        else:
            obj_pot_score[obj] += pts
            pkg_pot_score[pkg] += pts

    # totals
    total_p1 = sum(c["1"] for c in obj_prio.values())
    total_p2 = sum(c["2"] for c in obj_prio.values())
    total_p3 = sum(c["3"] for c in obj_prio.values())
    total_score = weighted_score(total_p1, total_p2, total_p3)

    potential_reduction = suc_potential_released + suc_potential_classic
    potential_score = total_score - potential_reduction

    # object-level derived data
    objects = []
    for obj, prios in obj_prio.items():
        obj_name, otype = obj
        p1, p2, p3 = int(prios["1"]), int(prios["2"]), int(prios["3"])
        sc  = weighted_score(p1, p2, p3)
        pot = obj_pot_score[obj]
        worst = "1" if p1 > 0 else ("2" if p2 > 0 else "3")
        objects.append({
            "name":        obj_name,
            "type":        otype,
            "package":     obj_pkg.get(obj, ""),
            "p1": p1, "p2": p2, "p3": p3,
            "score":       sc,
            "pot_score":   pot,
            "reduction":   sc - pot,
            "red_pct":     round((sc - pot) / sc * 100, 1) if sc else 0.0,
            "level":       worst,
            "can_reach_a": otype in LEVEL_A_CAPABLE_TYPES,
            "suc_p1": int(obj_suc[obj]["1"]),
            "suc_p2": int(obj_suc[obj]["2"]),
            "suc_p3": int(obj_suc[obj]["3"]),
        })

    # package-level derived data
    packages = []
    for pkg, prios in pkg_prio.items():
        p1, p2, p3 = int(prios["1"]), int(prios["2"]), int(prios["3"])
        sc  = weighted_score(p1, p2, p3)
        pot = pkg_pot_score[pkg]
        worst = "1" if p1 > 0 else ("2" if p2 > 0 else "3")
        # keep ALL refs per package; the dashboard reveals N of them via a dropdown (incl. "Max")
        top3_refs = sorted(pkg_ref_impact[pkg].items(), key=lambda x: x[1], reverse=True)
        suc = pkg_suc[pkg]
        packages.append({
            "name":      pkg,
            "p1": p1, "p2": p2, "p3": p3,
            "suc_p1": int(suc["1"]), "suc_p2": int(suc["2"]), "suc_p3": int(suc["3"]),
            "score":     sc,
            "pot_score": pot,
            "reduction": sc - pot,
            "red_pct":   round((sc - pot) / sc * 100, 1) if sc else 0.0,
            "level":     worst,
            "obj_count": sum(1 for o in objects if o["package"] == pkg),
            "top3_refs": top3_refs,
        })

    # level distribution (object-level, worst-finding logic)
    level_dist = Counter(o["level"] for o in objects)

    def _dedup_suc_detail(dets: list) -> list:
        """Collapse multiple findings for the same (ref_name, access_mode) into one entry,
        keeping the highest-priority finding and merging occurrence counts."""
        seen = {}
        for d in dets:
            key = (d["ref_name"], d["access_mode"])
            if key not in seen:
                seen[key] = {**d, "count": 1}
            else:
                seen[key]["count"] += 1
                if int(d["prio"]) < int(seen[key]["prio"]):
                    seen[key]["prio"] = d["prio"]
                    seen[key]["msg"]  = d["msg"]
        return sorted(seen.values(), key=lambda x: int(x["prio"]))

    # level-upgrade objects: objects that can improve their clean core level
    # by migrating successor-available findings
    def _worst(p1, p2, p3):
        if p1 > 0: return "1"
        if p2 > 0: return "2"
        if p3 > 0: return "3"
        return None  # fully clean

    level_upgrades = []
    for o in objects:
        rem_p1 = o["p1"] - o["suc_p1"]
        rem_p2 = o["p2"] - o["suc_p2"]
        rem_p3 = o["p3"] - o["suc_p3"]
        pot_level = _worst(rem_p1, rem_p2, rem_p3)
        cur_level = o["level"]
        # improvement = pot_level is better (higher key value = better) or fully clean
        cur_rank = {"1": 3, "2": 2, "3": 1}[cur_level]
        pot_rank = {"1": 3, "2": 2, "3": 1}.get(pot_level, 0)  # None -> 0 (clean)
        if pot_rank < cur_rank:
            level_upgrades.append({**o,
                "pot_level": pot_level,
                "rem_p1": rem_p1, "rem_p2": rem_p2, "rem_p3": rem_p3,
            })

    # sort: biggest level jump first, then by current score descending
    level_upgrades.sort(key=lambda x: (
        {"1":3,"2":2,"3":1}[x["level"]] - {"1":3,"2":2,"3":1}.get(x["pot_level"], 0),
        -x["score"]
    ), reverse=True)

    # package-level upgrade candidates: packages whose level could improve
    # if all successor-available findings across all their objects were migrated
    pkg_level_upgrades = []
    for p in packages:
        rem_p1 = p["p1"] - p["suc_p1"]
        rem_p2 = p["p2"] - p["suc_p2"]
        rem_p3 = p["p3"] - p["suc_p3"]
        pot_level = _worst(rem_p1, rem_p2, rem_p3)
        cur_level = p["level"]
        cur_rank = {"1": 3, "2": 2, "3": 1}[cur_level]
        pot_rank = {"1": 3, "2": 2, "3": 1}.get(pot_level, 0)
        if pot_rank < cur_rank:
            pkg_level_upgrades.append({**p,
                "pot_level": pot_level,
                "rem_p1": rem_p1, "rem_p2": rem_p2, "rem_p3": rem_p3,
            })
    pkg_level_upgrades.sort(key=lambda x: (
        {"1":3,"2":2,"3":1}[x["level"]] - {"1":3,"2":2,"3":1}.get(x["pot_level"], 0),
        -x["score"]
    ), reverse=True)

    return {
        "total_findings":      len(findings),
        "total_p1": total_p1, "total_p2": total_p2, "total_p3": total_p3,
        "total_score":         total_score,
        "potential_score":     potential_score,
        "potential_reduction": potential_reduction,
        "suc_findings":        sum(1 for f in findings if f["has_successor"]),
        "level_dist":          level_dist,
        "objects":             sorted(objects, key=lambda x: x["score"], reverse=True),
        "packages":            sorted(packages, key=lambda x: x["score"], reverse=True),
        "ref_impact":          sorted(ref_impact.items(), key=lambda x: x[1], reverse=True),
        "ref_custom_count":    {r: len(s) for r, s in ref_custom.items()},
        "ref_type_map":        ref_type_map,
        "ref_suc_impact":      sorted(ref_suc_impact.items(), key=lambda x: x[1], reverse=True),
        "ref_suc_custom_count":  {r: len(s) for r, s in ref_suc_custom.items()},
        "ref_suc_pkg_count":     {r: len(s) for r, s in ref_suc_packages.items()},
        "ref_suc_finding_count": dict(ref_suc_count),
        "level_upgrades":      level_upgrades,
        "pkg_level_upgrades":  pkg_level_upgrades,
        # key: (obj_name, obj_type) — HTML lookup uses both name and type
        "obj_suc_detail":      {obj: _dedup_suc_detail(dets) for obj, dets in obj_suc_detail.items()},
        # non-focus objects: tracked but excluded from all KPIs (Object Type Harmonization)
        "non_focus_obj_count": len(non_focus_objs),
        "non_focus_type_counts": dict(Counter(v["type"] for v in non_focus_objs.values())),
        "non_focus_score":     sum(
            int(non_focus_prio[k]["1"]) * 10 +
            int(non_focus_prio[k]["2"]) * 5 +
            int(non_focus_prio[k]["3"]) * 1
            for k in non_focus_objs
        ),
    }


# ---------------------------------------------------------------------------
# HTML generation
# ---------------------------------------------------------------------------

def pct(part: int, total: int) -> str:
    if total == 0:
        return "0.0"
    return f"{part / total * 100:.1f}"


def fmt_score(n: int) -> str:
    return f"{n:,}"


def level_badge(level_key: str) -> str:
    color = LEVEL_COLOR.get(level_key, "#888")
    label = LEVEL_LABEL.get(level_key, "?")
    return f'<span class="badge" style="background:{color}">{label}</span>'


def info_page_html(agg: dict, cr_meta: dict) -> str:
    """Build the methodology / help page content (custom CSS style, no UI5 web components)."""
    cr_files  = cr_meta.get("files", {})
    cr_ri     = cr_files.get("objectReleaseInfo_PCELatest.json", {})
    cr_date   = cr_ri.get("commit_date", "unknown")
    cr_msg    = cr_ri.get("commit_message", "")

    ex_obj   = "ZCL_IM_PP_MB_DOCUMENT_BADI"
    ex_p1, ex_p2, ex_p3 = 2, 3, 3
    ex_score = ex_p1*10 + ex_p2*5 + ex_p3*1
    ex_pot_reduction = 4
    ex_pot_score = ex_score - ex_pot_reduction

    total_objs  = len(agg["objects"])
    total_score = agg["total_score"]
    non_focus_obj_count = agg.get("non_focus_obj_count", 0)
    non_focus_score     = agg.get("non_focus_score", 0)

    return f"""
  <div id="page-info" class="tab-page" style="display:none;">
  <main class="page">

    <div class="section-title">About This Dashboard</div>
    <div class="card">
      <p style="margin-bottom:0.75rem;">
        This dashboard analyses the results of an <strong>SAP ABAP Test Cockpit (ATC)</strong>
        clean core check run. It calculates the Clean Core KPIs defined in the
        <em>SAP Clean Core Measurement Framework</em> — specifically the
        <strong>Technical Debt Score</strong> and <strong>Clean Core Level Distribution</strong>
        — and shows how they break down by object, package, and referenced SAP object.
      </p>
      <p style="color:var(--sap-text-secondary); font-size:0.8125rem;">
        Reference: <em>Clean Core Measurement Framework: KPIs (2025)</em>,
        SAP Digital Asset Management.
      </p>
    </div>

    <div class="section-title">1 · What Is Included in This Analysis</div>
    <div class="card">
      <p style="margin-bottom:0.75rem;">
        Only findings from the following three ATC check classes are included in all
        score and level calculations. These are the checks defined as relevant for
        the Technical Debt Score KPI:
      </p>
      <table style="max-width:700px; margin-bottom:1rem;">
        <thead><tr><th>Check Class</th><th>Check Name</th></tr></thead>
        <tbody>
          <tr><td class="mono">CL_YCM_CC_CHECK_API_USAGE</td><td>Usage of APIs</td></tr>
          <tr><td class="mono">CL_CI_TEST_CRITICAL_STATEMENTS</td><td>Critical Statements</td></tr>
          <tr><td class="mono">CL_CI_TEST_ADMISSIBLE_ENHANCM</td><td>Allowed SAP Enhancement Technologies</td></tr>
        </tbody>
      </table>

      <p style="font-weight:700; margin-bottom:0.5rem;">Object Type Harmonization — Focus Object Types</p>
      <p style="margin-bottom:0.75rem;">
        In addition to the check class filter, this dashboard applies an
        <strong>Object Type Harmonization</strong> that restricts KPI calculations
        to a curated set of <strong>logic-bearing ("focus") object types</strong>.
        This aligns with the SAP RISE with SAP Methodology Dashboard as of September 2026,
        which introduced this concept to ensure consistent object counts across data sources
        (ATC and CCA) and to exclude purely declarative or non-executable types from clean
        core debt scoring.
        See also:
        <a href="https://me.sap.com/notes/3761018" target="_blank">SAP Note 3761018</a>.
      </p>
      <table style="max-width:700px; margin-bottom:1rem;">
        <thead><tr><th>Focus Object Types (included in KPIs)</th><th>Non-Focus Types (tracked, excluded from KPIs)</th></tr></thead>
        <tbody>
          <tr>
            <td style="vertical-align:top;">
              <code>BDEF</code> Behavior Definition · <code>CLAS</code> Class · <code>INTF</code> Interface ·
              <code>FUNC</code> Function Module · <code>FUGR</code> Function Group · <code>FUGX</code> Function Group Ext. ·
              <code>PROG</code> Program · <code>DDLS</code> CDS View ·
              <code>ENHO</code> Enhancement Implementation · <code>SXCI</code> BAdI Implementation
            </td>
            <td style="vertical-align:top;">
              <code>TABL</code> Table/Structure · <code>VIEW</code> Database/Help View ·
              <code>SSFO</code> Smart Form · <code>SFPF</code> PDF Form ·
              <code>FUGS</code> Function Group Shared Part ·
              <code>DOMA</code> Domain · <code>WAPA</code> Web Dynpro App · and others
            </td>
          </tr>
        </tbody>
      </table>
      <div class="notice" style="margin:0 0 0.75rem 0;">
        <span class="notice-icon">⚠</span>
        <span>
          <strong>Only objects with at least one in-scope finding of a focus object type appear in KPIs.</strong>
          Non-focus objects with findings are shown in the run bar (count and score) but do not
          contribute to the Technical Debt Score, level distribution, or any other KPI tile.
          This run has <strong>{non_focus_obj_count:,} non-focus objects</strong>
          with a combined score of <strong>{fmt_score(non_focus_score)}</strong> (not counted).
        </span>
      </div>
      <div class="notice" style="margin:0;">
        <span class="notice-icon">⚠</span>
        <span>
          <strong>Only focus-type objects with at least one in-scope finding appear in this analysis.</strong>
          Focus objects with no findings are not present in the ATC export and therefore cannot be
          assessed here. They are <em>not</em> labelled "Level A" — that classification requires
          a confirmed absence of findings from a complete ATC run. This analysis covers
          <strong>{total_objs:,} focus objects</strong> with findings.
        </span>
      </div>
    </div>

    <div class="section-title">2 · Technical Debt Score — Formula &amp; Calculation</div>
    <div class="card">
      <p style="margin-bottom:1rem;">
        The Technical Debt Score translates the number and severity of ATC findings into
        a single numeric value. ATC reports three priority levels, each mapped to a weight:
      </p>
      <table style="max-width:500px; margin-bottom:1.25rem;">
        <thead>
          <tr><th>ATC Priority</th><th>Severity</th><th>Weight</th><th>Clean Core Level</th></tr>
        </thead>
        <tbody>
          <tr>
            <td><span class="badge" style="background:var(--sap-error)">P1 Error</span></td>
            <td>Error — must not be used</td>
            <td class="num bold" style="color:var(--sap-error)">× 10</td>
            <td><span class="badge" style="background:var(--sap-error)">Level D</span></td>
          </tr>
          <tr>
            <td><span class="badge" style="background:var(--sap-warning)">P2 Warning</span></td>
            <td>Warning — should be avoided</td>
            <td class="num bold" style="color:var(--sap-warning)">× 5</td>
            <td><span class="badge" style="background:var(--sap-warning)">Level C</span></td>
          </tr>
          <tr>
            <td><span class="badge" style="background:var(--sap-info)">P3 Info</span></td>
            <td>Information — classic / acceptable</td>
            <td class="num bold" style="color:var(--sap-info)">× 1</td>
            <td><span class="badge" style="background:var(--sap-info)">Level B</span></td>
          </tr>
        </tbody>
      </table>
      <div class="notice" style="background:#f0f8ff; border-color:#b0cce8; color:#1a3a5a; margin-bottom:1rem;">
        <span class="notice-icon">𝑓</span>
        <span><strong>Score = (P1 × 10) + (P2 × 5) + (P3 × 1)</strong></span>
      </div>
      <div class="notice" style="background:#f5f5f5; border-color:#ccc; margin-bottom:1rem;">
        <span class="notice-icon">ℹ</span>
        <span>
          <strong><code>DPRCTD_SUC</code> findings are excluded from the Technical Debt Score.</strong>
          These findings carry the message code <code>DPRCTD_SUC</code> (deprecated object with a
          known successor) and are <em>not</em> counted as P1/P2/P3 in the score — they are tracked
          separately and feed only into the <strong>Potential Score</strong> calculation (Section 7).
          All other <code>_SUC</code> message codes (<code>SELECT_SUC</code>, <code>TC_CLA_SUC</code>,
          etc.) <em>are</em> counted normally. This matches the RISE Dashboard counting logic.
        </span>
      </div>
      <p style="margin-bottom:0.75rem; font-weight:700;">Real example: <code>{ex_obj}</code></p>
      <table style="max-width:450px; margin-bottom:0.75rem;">
        <thead><tr><th>Priority</th><th class="num">Findings</th><th class="num">Weight</th><th class="num">Points</th></tr></thead>
        <tbody>
          <tr>
            <td><span class="badge" style="background:var(--sap-error)">P1 Error</span></td>
            <td class="num">{ex_p1}</td><td class="num">× 10</td>
            <td class="num bold" style="color:var(--sap-error)">{ex_p1*10}</td>
          </tr>
          <tr>
            <td><span class="badge" style="background:var(--sap-warning)">P2 Warning</span></td>
            <td class="num">{ex_p2}</td><td class="num">× 5</td>
            <td class="num bold" style="color:var(--sap-warning)">{ex_p2*5}</td>
          </tr>
          <tr>
            <td><span class="badge" style="background:var(--sap-info)">P3 Info</span></td>
            <td class="num">{ex_p3}</td><td class="num">× 1</td>
            <td class="num bold" style="color:var(--sap-info)">{ex_p3*1}</td>
          </tr>
          <tr style="border-top:2px solid var(--sap-accent);">
            <td colspan="3" class="bold">Technical Debt Score</td>
            <td class="num bold">{ex_score}</td>
          </tr>
        </tbody>
      </table>
      <p style="font-size:0.8125rem; color:var(--sap-text-secondary);">
        Total for this run: <strong>{fmt_score(total_score)} points</strong> across all {total_objs:,} objects with findings.
      </p>
    </div>

    <div class="section-title">3 · Clean Core Level — Worst-Finding Logic</div>
    <div class="card">
      <p style="margin-bottom:0.75rem;">
        Each custom code object is assigned a single Clean Core Level based on its
        <strong>worst (highest-priority) finding</strong>. One P1 Error finding is enough to
        classify the entire object as Level D.
      </p>
      <table style="max-width:480px; margin-bottom:1rem;">
        <thead><tr><th>Worst Finding</th><th>Object Level</th></tr></thead>
        <tbody>
          <tr><td>At least one P1 Error</td><td><span class="badge" style="background:var(--sap-error)">Level D</span></td></tr>
          <tr><td>No P1, but at least one P2 Warning</td><td><span class="badge" style="background:var(--sap-warning)">Level C</span></td></tr>
          <tr><td>Only P3 Info findings</td><td><span class="badge" style="background:var(--sap-info)">Level B</span></td></tr>
          <tr><td>No in-scope findings (not in export)</td><td style="color:var(--sap-text-secondary); font-style:italic;">Not assessed here — may be Level A</td></tr>
        </tbody>
      </table>
    </div>

    <div class="section-title">4 · Table Access Mode — Read vs. Write</div>
    <div class="card">
      <p style="margin-bottom:0.75rem;">
        When the referenced SAP object is a database table (<code>TABL</code>), the dashboard
        distinguishes between <strong>read</strong> and <strong>write</strong> access based on the ATC message code:
      </p>
      <table style="max-width:620px; margin-bottom:1rem;">
        <thead><tr><th>Message codes</th><th>Access mode</th><th>Priority</th><th>Displayed as</th></tr></thead>
        <tbody>
          <tr>
            <td><code>SELECT</code>, <code>SELECT_SUC</code>, <code>DB_TAB_CDS</code></td>
            <td>Read (SELECT)</td>
            <td><span class="badge" style="background:var(--sap-warning)">P2 Warning</span></td>
            <td><code>MARA (TABL, Read)</code></td>
          </tr>
          <tr>
            <td><code>UPDATE</code>, <code>UPDATE_SUC</code></td>
            <td>Write (INSERT/UPDATE/DELETE)</td>
            <td><span class="badge" style="background:var(--sap-error)">P1 Error</span></td>
            <td><code>MARA (TABL, Write)</code></td>
          </tr>
        </tbody>
      </table>
      <div class="notice">
        <span class="notice-icon">⚠</span>
        <span>In the <strong>Pkg Upgrades</strong> and <strong>Obj Upgrades</strong> tabs, write-access findings with a CDS successor
        are flagged with a warning. These findings may overstate the potential score reduction —
        verify whether an actual write successor exists before planning the migration.</span>
      </div>
    </div>

    <div class="section-title">5 · Package-Level Aggregation</div>
    <div class="card">
      <p style="margin-bottom:0.75rem;">
        Package scores are the <strong>sum of all object scores within the package</strong>.
        The package level follows the same worst-finding logic.
      </p>
      <p style="font-size:0.8125rem; color:var(--sap-text-secondary);">
        The "Top Referenced SAP objects" column shows which SAP objects generate the
        most technical debt score <em>within that package</em>. Use the "Refs/pkg" dropdown
        above the table to show between 3 and 25 objects per package.
      </p>
    </div>

    <div class="section-title">6 · Referenced SAP Object Impact</div>
    <div class="card">
      <p style="margin-bottom:0.75rem;">
        The <strong>impact score</strong> of a referenced SAP object is the sum of weighted
        points from all findings that reference it, across all custom objects:
      </p>
      <div class="notice" style="background:#f0f8ff; border-color:#b0cce8; color:#1a3a5a; margin-bottom:0.75rem;">
        <span class="notice-icon">𝑓</span>
        <span><code>Impact(ref) = Σ weight(priority) for every finding referencing ref</code></span>
      </div>
      <p style="font-size:0.8125rem; color:var(--sap-text-secondary); margin-bottom:1rem;">
        A high-impact referenced object is one where many custom objects use it heavily (P1/P2 findings).
      </p>

      <p style="font-weight:700; margin-bottom:0.5rem;">Top Referenced SAP Objects with Successor</p>
      <p style="margin-bottom:0.75rem;">
        A second view filters to only the findings that carry a <code>_SUC</code> message code —
        i.e. findings where the ATC check has identified a potential successor in the Cloudification
        Repository. The <strong>successor impact score</strong> is computed the same way as the
        overall impact score, but restricted to those <code>_SUC</code> findings only.
      </p>
      <p style="margin-bottom:0.75rem;">
        The purpose of this view is to answer: <em>for which SAP objects does a known successor
        exist, and how much technical debt could be eliminated if that successor turns out to be
        applicable?</em> It is a <strong>migration prioritisation tool</strong>: the objects ranked
        highest here are the ones worth investigating first — if the successor covers your use cases,
        migrating that one SAP object could remove the most debt across the widest set of custom objects.
      </p>
      <p style="margin-bottom:0.5rem;">
        The <strong>spread</strong> column shows how many custom objects and packages are affected
        by the successor-flagged findings for each SAP object. This is key for assessing migration
        effort: 100 findings in 4 objects within one package is far easier to coordinate than 100
        findings spread across 50 objects in 10 packages. The column is colour-coded:
      </p>
      <table style="max-width:580px; margin-bottom:1rem;">
        <thead><tr><th>Colour</th><th>Condition</th><th>Meaning</th></tr></thead>
        <tbody>
          <tr>
            <td><span class="badge" style="background:var(--sap-success)">Green</span></td>
            <td>≤ 5 objects, 1 package</td>
            <td>Highly concentrated — easy to scope and coordinate</td>
          </tr>
          <tr>
            <td><span class="badge" style="background:var(--sap-warning)">Amber</span></td>
            <td>≤ 10 objects, ≤ 2 packages</td>
            <td>Moderately concentrated</td>
          </tr>
          <tr>
            <td><span style="color:var(--sap-text-secondary);font-weight:700;">Grey</span></td>
            <td>More than 10 objects or 2+ packages</td>
            <td>Spread across many objects / packages — higher coordination effort</td>
          </tr>
        </tbody>
      </table>
      <div class="notice">
        <span class="notice-icon">⚠</span>
        <span>
          <strong>A <code>_SUC</code> finding is not a confirmed replacement.</strong>
          The successor must be verified per use case — especially for table write access where
          CDS successors are read-only. See sections 4 and 8 for details on the write-access
          warning and level upgrade logic.
        </span>
      </div>
    </div>

    <div class="section-title">7 · Potential Score — Successor-Available Findings</div>
    <div class="card">
      <div class="notice" style="background:#fff8e1; border-color:#f0c040; margin-bottom:1rem;">
        <span class="notice-icon">⚠</span>
        <span>
          <strong>The Potential Score is indicative — one option, not a must-do.</strong>
          It represents a theoretical minimum if all successor findings were migrated, but:
          <ul style="margin:0.4rem 0 0 1rem; padding:0;">
            <li>Successor migration is only one of several ways to reduce technical debt.</li>
            <li>It may not be the right starting point for every object or package.</li>
            <li><strong>Not every successor is a functional drop-in replacement</strong> — field coverage,
            write access, and business logic must be validated individually per use case.</li>
          </ul>
          Always consult the
          <a href="https://sap.github.io/abap-atc-cr-cv-s4hc" target="_blank">Cloudification Repository</a>
          for the specific successor object and verify scope before planning any migration.
        </span>
      </div>
      <p style="margin-bottom:0.75rem;">
        Findings with a <code>_SUC</code> suffix indicate the referenced SAP object has a known
        successor in the
        <a href="https://sap.github.io/abap-atc-cr-cv-s4hc" target="_blank">Cloudification Repository</a>.
        Successor classification determines the residual score after migration:
      </p>
      <table style="max-width:560px; margin-bottom:1.25rem;">
        <thead><tr><th>Successor classification</th><th class="num">Residual score</th><th>Reasoning</th></tr></thead>
        <tbody>
          <tr>
            <td><strong>Released</strong> (officially released API)</td>
            <td class="num bold" style="color:var(--sap-success)">0 pts</td>
            <td>Fully clean — no debt after migration</td>
          </tr>
          <tr>
            <td><strong>Classic API</strong> (nominated, not yet released)</td>
            <td class="num bold" style="color:var(--sap-info)">1 pt</td>
            <td>Level B — still some debt, but acceptable</td>
          </tr>
          <tr>
            <td><strong>Unknown</strong> (not in CR data)</td>
            <td class="num bold" style="color:var(--sap-warning)">1 pt</td>
            <td>Conservative assumption: treated as Classic API</td>
          </tr>
        </tbody>
      </table>
      <p style="font-size:0.8125rem; color:var(--sap-text-secondary);">
        Example: <code>{ex_obj}</code> has 1 P2 successor finding (5 pts).
        After migration to Classic API: {ex_pot_score} pts (−{ex_pot_reduction} pts).
      </p>
    </div>

    <div class="section-title">8 · Level Upgrade Candidates</div>
    <div class="card">
      <p style="margin-bottom:0.75rem;">
        An object is a <strong>level upgrade candidate</strong> if migrating its
        successor-available findings would eliminate all findings of the worst priority level.
      </p>
      <table style="max-width:560px; margin-bottom:1rem;">
        <thead><tr><th>Transition</th><th>Condition</th></tr></thead>
        <tbody>
          <tr><td>Level D → Level C</td><td>All P1 findings have a <code>_SUC</code> code; P2/P3 remain</td></tr>
          <tr><td>Level D → Level B</td><td>All P1 and P2 findings have <code>_SUC</code>; only P3 remain</td></tr>
          <tr><td>Level D → Level A</td><td>All findings have <code>_SUC</code>; potentially none remain — <em>only for Level-A-capable types</em></td></tr>
          <tr><td>Level D → Level B*</td><td>All findings have <code>_SUC</code> but object type cannot use ABAP Cloud Language Version</td></tr>
        </tbody>
      </table>
      <div class="notice" style="background:#fff8e1; border-color:#f0c040; margin-bottom:0.75rem;">
        <span class="notice-icon">⚠</span>
        <span>
          <strong>Not all object types can reach Level A.</strong>
          Level A requires the ABAP Cloud Language Version (<code>S_ABPLNGVS</code>), which is
          only supported for specific repository object types.
          <strong>Object types such as PROG (reports/includes) and ENHO</strong>
          and others <strong>cannot be placed under ABAP Cloud Language
          Version</strong> — their maximum achievable clean core level is <strong>Level B</strong>.
          Note: types such as SSFO, SFPF, VIEW, DOMA, and WAPA are excluded from KPIs entirely
          (non-focus types) and do not appear in upgrade candidate lists.
          <br/>
          <strong>Level B* in this dashboard</strong> means: successor migration could bring the
          technical debt score to 0 (no more P1/P2/P3 findings), but the object type still prevents
          Level A. The "B*" marker is informational — the Clean Core level framework only has A/B/C/D.
          <br/>
          Object types that <em>do</em> support ABAP Cloud Language Version include:
          BDEF, CLAS, INTF, FUNC, DDLS, DTEL. For these, Level A is technically achievable
          after full successor migration — but always verify functional scope per use case.
        </span>
      </div>
      <div class="notice">
        <span class="notice-icon">⚠</span>
        <span>
          <strong>Conservative interpretation required.</strong>
          A <code>_SUC</code> finding does not confirm the successor is a drop-in replacement.
          Always verify functional scope — especially for table write access where CDS successors are read-only.
        </span>
      </div>
    </div>

    <div class="section-title">9 · Cloudification Repository Data</div>
    <div class="card">
      <p style="margin-bottom:0.75rem;">
        SAP maintains a public <strong>Cloudification Repository (CR)</strong> at
        <a href="https://github.com/SAP/abap-atc-cr-cv-s4hc" target="_blank">github.com/SAP/abap-atc-cr-cv-s4hc</a>.
        This dashboard uses a bundled snapshot of two files:
      </p>
      <table style="max-width:680px; margin-bottom:1rem;">
        <thead><tr><th>File</th><th>Contents</th></tr></thead>
        <tbody>
          <tr>
            <td class="mono">objectReleaseInfo_PCELatest.json</td>
            <td>All <strong>released</strong> and deprecated SAP objects (~44,000)</td>
          </tr>
          <tr>
            <td class="mono">objectClassifications_SAP.json</td>
            <td>Objects classified as <strong>Classic API</strong> or noAPI (~8,500)</td>
          </tr>
        </tbody>
      </table>
      <div class="notice" style="background:#f0f8ff; border-color:#b0cce8; color:#1a3a5a;">
        <span class="notice-icon">ℹ</span>
        <span>
          <strong>Bundled CR version:</strong> commit date <strong>{cr_date}</strong> ({cr_msg}).<br/>
          To check for updates: <code>python scripts/update_cr_data.py --check</code><br/>
          See <code>references/HOW-TO-UPDATE-CR-DATA.md</code> for full instructions.
        </span>
      </div>
    </div>

  </main>
  </div>
"""


def generate_html(settings: dict, agg: dict, cr_meta: dict,
                  excluded: int, top_n: int, zip_name: str) -> str:

    run_title   = settings.get("run_title", zip_name)
    system      = settings.get("scheduled_sys", "—")
    run_ts_raw  = settings.get("scheduled_on_ts", "")
    check_var   = settings.get("check_variant", "—")
    run_series  = settings.get("run_series", "—")

    if len(run_ts_raw) >= 8:
        run_date = f"{run_ts_raw[:4]}-{run_ts_raw[4:6]}-{run_ts_raw[6:8]}"
        if len(run_ts_raw) >= 14:
            run_date += f" {run_ts_raw[8:10]}:{run_ts_raw[10:12]}:{run_ts_raw[12:14]}"
    else:
        run_date = run_ts_raw or "—"

    cr_files  = cr_meta.get("files", {})
    cr_ri     = cr_files.get("objectReleaseInfo_PCELatest.json", {})
    cr_date   = cr_ri.get("commit_date", "unknown")
    cr_msg    = cr_ri.get("commit_message", "")
    cr_bundled = cr_meta.get("bundled_on", "unknown")

    total_score     = agg["total_score"]
    potential_score = agg["potential_score"]
    reduction       = agg["potential_reduction"]
    reduction_pct   = pct(reduction, total_score)
    suc_count       = agg["suc_findings"]
    total_findings  = agg["total_findings"]

    non_focus_obj_count   = agg.get("non_focus_obj_count", 0)
    non_focus_type_counts = agg.get("non_focus_type_counts", {})
    non_focus_score       = agg.get("non_focus_score", 0)
    # Build a compact label like "106 (VIEW×60, SSFO×32, …)"
    _nf_parts = ", ".join(f"{t}×{c}" for t, c in sorted(non_focus_type_counts.items(), key=lambda x: -x[1]))
    non_focus_label = f"{non_focus_obj_count:,} ({_nf_parts})" if _nf_parts else str(non_focus_obj_count)

    level_dist = agg["level_dist"]
    total_objs = len(agg["objects"])

    # ── Auto-scaling by data size ─────────────────────────────────────────
    # The HTML size is driven by two things that grow with the customer:
    #   1. dashboard table rows (bounded by DASH_MAX)
    #   2. referenced-object "chips" per package row = packages × refs (multiplicative)
    # We pick caps from the actual export size so a huge customer still gets an
    # openable file. All Data *row* tables stay complete (that's the full view);
    # only the per-package chip rendering and the dashboard top-N are bounded.
    n_findings = agg["total_findings"]
    n_objects  = len(agg["objects"])
    max_pkg_refs = max((len(p["top3_refs"]) for p in agg["packages"]), default=0)

    if n_findings <= 80_000 and n_objects <= 8_000:
        SIZE_TIER = "standard"
        DASH_MAX, CHART_MAX, CHIP_CAP = 500, 100, 500
    elif n_findings <= 200_000 and n_objects <= 15_000:
        SIZE_TIER = "large"
        DASH_MAX, CHART_MAX, CHIP_CAP = 500, 100, 300
    elif n_findings <= 400_000 and n_objects <= 30_000:
        SIZE_TIER = "very large"
        DASH_MAX, CHART_MAX, CHIP_CAP = 300, 75, 150
    else:
        SIZE_TIER = "huge"
        DASH_MAX, CHART_MAX, CHIP_CAP = 250, 50, 100

    # Never cap below what the data actually has (avoids a pointless "500 of 30").
    CHIP_CAP = min(CHIP_CAP, max_pkg_refs) if max_pkg_refs else CHIP_CAP

    print(f"  Size tier         : {SIZE_TIER} "
          f"(findings={n_findings:,}, objects={n_objects:,}, max refs/pkg={max_pkg_refs:,})",
          file=sys.stderr)
    print(f"  Render caps       : dashboard rows={DASH_MAX}, chart bars={CHART_MAX}, "
          f"refs/pkg={CHIP_CAP}", file=sys.stderr)

    # Dashboard tables render up to DASH_MAX rows into the HTML; a per-table
    # dropdown reveals a subset client-side (full lists live in All Data).
    top_pkgs = agg["packages"][:DASH_MAX]
    top_objs_score = agg["objects"][:DASH_MAX]
    top_objs_d = sorted(agg["objects"], key=lambda x: x["p1"], reverse=True)[:DASH_MAX]
    top_refs = agg["ref_impact"][:DASH_MAX]
    top_refs_suc = agg["ref_suc_impact"][:DASH_MAX]

    # Row-count dropdown steps adapt to DASH_MAX (only offer steps we actually render).
    _ALL_STEPS = (10, 25, 50, 100, 250, 500, 1000)
    ROW_STEPS = tuple(n for n in _ALL_STEPS if n <= DASH_MAX)

    # "Save to Excel" button — exports the currently-visible rows of one table.
    def export_button(table_id: str) -> str:
        fname = table_id.replace("uptbl-", "upgrade-").replace("tbl-", "") + ".xlsx"
        return (
            f'<button type="button" class="excel-btn" '
            f"onclick=\"exportTableToExcel('{table_id}', '{fname}')\" "
            f'title="Save the currently shown rows to Excel">'
            f'⬇ Excel</button>'
        )

    # Dropdown control that lets the user grow a dashboard list client-side.
    def rowcount_control(table_id: str, total: int, steps=None) -> str:
        steps = steps if steps is not None else ROW_STEPS
        opts = []
        for n in steps:
            if n <= total:
                sel = " selected" if n == 10 else ""
                opts.append(f'<option value="{n}"{sel}>{n}</option>')
        # always offer the exact total if it isn't already an option and is within the render cap
        if total <= DASH_MAX and total not in steps:
            sel = " selected" if total <= 10 else ""
            opts.append(f'<option value="{total}"{sel}>All {total}</option>')
        opts_html = "".join(opts)
        return (
            f'<span class="rowcount-ctl">Show '
            f'<select class="rowcount-select" data-table="{table_id}" '
            f'onchange="applyRowCount(this.value, this.dataset.table)">{opts_html}</select>'
            f' of {total:,}</span>{export_button(table_id)}'
        )

    # --- Build table rows ---

    def upgrade_count_control(target_id: str, total: int, apply_fn: str, exportable: bool = True) -> str:
        """Dropdown for the upgrade tabs: steps of 10 up to 1000, capped at total,
        defaulting to 'All' so the true count is visible (nothing looks truncated)."""
        opts = []
        for n in range(10, 1001, 10):
            if n < total:
                opts.append(f'<option value="{n}">{n}</option>')
        opts.append(f'<option value="{total}" selected>All {total:,}</option>')
        opts_html = "".join(opts)
        return (
            f'<span class="rowcount-ctl">Show '
            f'<select class="rowcount-select" data-target="{target_id}" '
            f'onchange="{apply_fn}(this.value, this.dataset.target)">{opts_html}</select>'
            f'</span>{export_button(target_id) if exportable else ""}'
        )

    def obj_rows(obj_list: list, sort_col: str) -> str:
        rows = []
        for i, o in enumerate(obj_list, 1):
            sc = fmt_score(o["score"])
            badge = level_badge(o["level"])
            rows.append(
                f'<tr data-rowidx="{i}">'
                f'<td class="rank">{i}</td>'
                f'<td class="mono">{o["name"]}</td>'
                f'<td>{o["type"]}</td>'
                f'<td class="mono">{o["package"]}</td>'
                f'<td class="num red">{o["p1"]}</td>'
                f'<td class="num orange">{o["p2"]}</td>'
                f'<td class="num blue">{o["p3"]}</td>'
                f'<td class="num bold">{sc}</td>'
                f'<td>{badge}</td>'
                f'</tr>'
            )
        return "\n".join(rows)

    def obj_rows_full(obj_list: list) -> str:
        """All Data objects table — includes potential/reduction columns so this
        table is a complete superset of the (capped) Cleanup Potential tables."""
        rows = []
        for i, o in enumerate(obj_list, 1):
            badge = level_badge(o["level"])
            rows.append(
                f'<tr data-rowidx="{i}">'
                f'<td class="rank">{i}</td>'
                f'<td class="mono">{o["name"]}</td>'
                f'<td>{o["type"]}</td>'
                f'<td class="mono">{o["package"]}</td>'
                f'<td class="num red">{o["p1"]}</td>'
                f'<td class="num orange">{o["p2"]}</td>'
                f'<td class="num blue">{o["p3"]}</td>'
                f'<td class="num bold">{fmt_score(o["score"])}</td>'
                f'<td class="num">{fmt_score(o["pot_score"])}</td>'
                f'<td class="num" style="color:var(--sap-success);font-weight:700;">{fmt_score(o["reduction"])}</td>'
                f'<td class="num">{o["red_pct"]:.1f}%</td>'
                f'<td>{badge}</td>'
                f'</tr>'
            )
        return "\n".join(rows)

    def pkg_rows(pkg_list: list, chip_cap: int = None, more_hint: str = "see All Data") -> str:
        cap = chip_cap if chip_cap is not None else CHIP_CAP
        rows = []
        for i, p in enumerate(pkg_list, 1):
            sc = fmt_score(p["score"])
            badge = level_badge(p["level"])
            refs_parts = []
            # `cap` bounds how many chips we render per row (packages × refs is the
            # fastest-growing part of the file). On the Dashboard tab this points the
            # overflow to the complete All Data table; on All Data itself it's uncapped.
            all_refs = p["top3_refs"]
            for ri, (r, s) in enumerate(all_refs[:cap]):
                # data-refidx lets the "SAP Objects" dropdown reveal/hide chips
                refs_parts.append(
                    f'<span class="ref-chip" data-refidx="{ri}">{r} <em>({fmt_score(s)})</em></span>'
                )
            if len(all_refs) > cap and more_hint:
                refs_parts.append(
                    f'<span class="ref-more" title="{more_hint}">'
                    f'+{len(all_refs) - cap:,} more — {more_hint}</span>'
                )
            refs_html = "".join(refs_parts) if refs_parts else "—"
            rows.append(
                f'<tr data-rowidx="{i}">'
                f'<td class="rank">{i}</td>'
                f'<td class="mono bold">{p["name"]}</td>'
                f'<td class="num">{p["obj_count"]}</td>'
                f'<td class="num red">{p["p1"]}</td>'
                f'<td class="num orange">{p["p2"]}</td>'
                f'<td class="num blue">{p["p3"]}</td>'
                f'<td class="num bold">{sc}</td>'
                f'<td>{badge}</td>'
                f'<td class="refs">{refs_html}</td>'
                f'</tr>'
            )
        return "\n".join(rows)

    def ref_rows(ref_list: list) -> str:
        rows = []
        max_score = ref_list[0][1] if ref_list else 1
        for i, (ref, sc) in enumerate(ref_list, 1):
            bar_w = int(sc / max_score * 100)
            custom_cnt = agg["ref_custom_count"].get(ref, 0)
            rows.append(
                f'<tr data-rowidx="{i}">'
                f'<td class="rank">{i}</td>'
                f'<td class="mono">{ref}</td>'
                f'<td class="num">{custom_cnt}</td>'
                f'<td class="num bold">{fmt_score(sc)}</td>'
                f'<td><div class="mini-bar"><div class="mini-bar-fill" style="width:{bar_w}%"></div></div></td>'
                f'</tr>'
            )
        return "\n".join(rows)

    def ref_suc_rows(ref_list: list) -> str:
        rows = []
        max_score = ref_list[0][1] if ref_list else 1
        for i, (ref, sc) in enumerate(ref_list, 1):
            bar_w       = int(sc / max_score * 100)
            obj_cnt     = agg["ref_suc_custom_count"].get(ref, 0)
            pkg_cnt     = agg["ref_suc_pkg_count"].get(ref, 0)
            finding_cnt = agg["ref_suc_finding_count"].get(ref, 0)
            # colour-code concentration: green = very concentrated, amber = moderate, grey = spread
            if obj_cnt <= 5 and pkg_cnt == 1:
                conc_color = "var(--sap-success)"
                conc_title = "Highly concentrated — few objects, single package"
            elif obj_cnt <= 10 and pkg_cnt <= 2:
                conc_color = "var(--sap-warning)"
                conc_title = "Moderately concentrated"
            else:
                conc_color = "var(--sap-text-secondary)"
                conc_title = "Spread across many objects / packages"
            conc_html = (
                f'<span title="{conc_title}" style="color:{conc_color};font-weight:700;">'
                f'{obj_cnt} obj / {pkg_cnt} pkg</span>'
            )
            rows.append(
                f'<tr data-rowidx="{i}">'
                f'<td class="rank">{i}</td>'
                f'<td class="mono">{ref}</td>'
                f'<td class="num">{finding_cnt}</td>'
                f'<td class="num bold">{fmt_score(sc)}</td>'
                f'<td style="text-align:right;">{conc_html}</td>'
                f'<td><div class="mini-bar"><div class="mini-bar-fill" style="width:{bar_w}%;background:var(--sap-success)"></div></div></td>'
                f'</tr>'
            )
        return "\n".join(rows)

    def successor_by_object_rows() -> str:
        """One row per (custom object, referenced SAP object that has a successor).
        Sorted by referenced object name so every caller of the same SAP object —
        e.g. one BAPI used across many packages — groups together. Shows the
        object's current Clean Core level and the level it would reach if ALL its
        successor-available findings were migrated (worst-finding logic)."""
        LEVEL_KEY = {"1": "D", "2": "C", "3": "B", None: "A"}

        # index object metadata (level + potential level after migrating successors)
        obj_meta = {}
        for o in agg["objects"]:
            rem_p1 = o["p1"] - o["suc_p1"]
            rem_p2 = o["p2"] - o["suc_p2"]
            rem_p3 = o["p3"] - o["suc_p3"]
            pot = "1" if rem_p1 > 0 else ("2" if rem_p2 > 0 else ("3" if rem_p3 > 0 else None))
            obj_meta[o["name"]] = {
                "type": o["type"], "package": o["package"],
                "level": o["level"], "pot_level": pot, "score": o["score"],
            }

        # flatten obj_suc_detail into rows
        flat = []
        for obj_name, dets in agg["obj_suc_detail"].items():
            meta = obj_meta.get(obj_name, {})
            for d in dets:
                # successor target string
                if d["successors"]:
                    suc_str = ", ".join(
                        f'{s.get("objectType","")} {s.get("objectKey","")}'.strip()
                        for s in d["successors"]
                    )
                elif d["suc_concept"]:
                    suc_str = f'(concept) {d["suc_concept"]}'
                else:
                    suc_str = "— (successor flagged by ATC, not detailed in CR)"
                flat.append({
                    "ref": d["display_ref"],
                    "ref_sort": d["ref_name"],
                    "successor": suc_str,
                    "cr_state": d["cr_state"] or "—",
                    "prio": d["prio"],
                    "obj": obj_name,
                    "type": meta.get("type", ""),
                    "package": meta.get("package", ""),
                    "level": meta.get("level"),
                    "pot_level": meta.get("pot_level"),
                    "write_warning": d["write_warning"],
                })

        # sort: referenced object name, then object level (worst first), then object name
        rank = {"1": 3, "2": 2, "3": 1, None: 0}
        flat.sort(key=lambda r: (r["ref_sort"], -rank.get(r["level"], 0), r["obj"]))

        rows = []
        for i, r in enumerate(flat, 1):
            cur = LEVEL_KEY.get(r["level"], "?")
            pot = LEVEL_KEY.get(r["pot_level"], "?")
            cur_badge = level_badge(r["level"]) if r["level"] else '<span class="badge" style="background:#107e3e">Level A</span>'
            if r["pot_level"] == r["level"]:
                # this particular object can't change level (other findings hold it)
                transition = f'{cur_badge} <span style="color:var(--sap-text-secondary);font-size:0.75rem;">(no level change — other findings remain)</span>'
            else:
                pot_badge = (level_badge(r["pot_level"]) if r["pot_level"]
                             else '<span class="badge" style="background:#107e3e">Level A</span>')
                transition = f'{cur_badge} <span class="level-arrow">→</span> {pot_badge}'
            warn = ' <span class="write-warn">⚠ write</span>' if r["write_warning"] else ""
            prio_color = "var(--sap-error)" if r["prio"] == "1" else "var(--sap-warning)" if r["prio"] == "2" else "var(--sap-info)"
            rows.append(
                f'<tr data-rowidx="{i}">'
                f'<td class="rank">{i}</td>'
                f'<td class="mono">{r["ref"]}</td>'
                f'<td class="mono" style="color:var(--sap-success);">{r["successor"]}{warn}</td>'
                f'<td style="font-size:0.75rem;">{r["cr_state"]}</td>'
                f'<td><span class="badge" style="background:{prio_color};font-size:0.65rem;">P{r["prio"]}</span></td>'
                f'<td class="mono">{r["obj"]}</td>'
                f'<td>{r["type"]}</td>'
                f'<td class="mono">{r["package"]}</td>'
                f'<td>{transition}</td>'
                f'</tr>'
            )
        return "\n".join(rows)

    # level distribution cards
    def level_cards() -> str:
        cards = []
        for key, label in [
            ("1", "Level D — Error"),
            ("2", "Level C — Warning"),
            ("3", "Level B — Info"),
        ]:
            color = LEVEL_COLOR[key]
            cnt   = level_dist.get(key, 0)
            p     = pct(cnt, total_objs)
            note  = "P1 Error" if key == "1" else "P2 Warning" if key == "2" else "P3 Info"
            cards.append(
                f'<div class="level-card" style="border-top: 4px solid {color}">'
                f'<div class="level-label" style="color:{color}">{label}</div>'
                f'<div class="level-count">{cnt}</div>'
                f'<div class="level-pct">objects ({p}%)</div>'
                f'<div class="level-note">worst finding = {note}</div>'
                f'</div>'
            )
        cards.append(
            f'<div class="level-card info-card">'
            f'<div class="level-label" style="color:#5a5a5a">Objects in analysis</div>'
            f'<div class="level-count">{total_objs}</div>'
            f'<div class="level-pct">with at least one finding</div>'
            f'<div class="level-note">Level A = no finding — not in ATC export</div>'
            f'</div>'
        )
        return "\n".join(cards)


    def cleanup_bar(red_pct: float, score: int) -> str:
        if red_pct >= 40:
            color = "#107e3e"
            cls   = "high"
        elif red_pct >= 15:
            color = "#e76500"
            cls   = "medium"
        else:
            color = "#9e9e9e"
            cls   = "low"
        w = int(red_pct)
        return (
            f'<div class="cleanup-bar-wrap">'
            f'<div class="cleanup-bar-bg">'
            f'<div class="cleanup-bar-fill" style="width:{w}%;background:{color}"></div>'
            f'</div>'
            f'<span class="cleanup-pct {cls}">{red_pct:.1f}%</span>'
            f'</div>'
        )

    def size_tag(score: int) -> str:
        if score >= 10000:
            label, bg = "XL", "#ffe0b2"
        elif score >= 1000:
            label, bg = "L",  "#fff9c4"
        elif score >= 200:
            label, bg = "M",  "#e8f5e9"
        else:
            label, bg = "S",  "#f5f5f5"
        return f'<span class="size-tag" style="background:{bg}">{label}</span>'

    def pkg_cleanup_rows(pkg_list: list) -> str:
        max_score = max((p["score"] for p in pkg_list), default=1)
        rows = []
        for i, p in enumerate(pkg_list, 1):
            bar  = cleanup_bar(p["red_pct"], p["score"])
            sc_w = int(p["score"] / max_score * 100)
            sc_bar = (
                f'<div style="display:flex;align-items:center;gap:0.4rem;">'
                f'<div style="flex:1;height:6px;background:#e8edf5;border-radius:3px;min-width:60px;">'
                f'<div style="width:{sc_w}%;height:6px;background:#0070f2;border-radius:3px;"></div>'
                f'</div>'
                f'<span style="font-size:0.8rem;font-variant-numeric:tabular-nums;min-width:4rem;text-align:right;">{fmt_score(p["score"])}</span>'
                f'</div>'
            )
            rows.append(
                f'<tr data-rowidx="{i}">'
                f'<td class="rank">{i}</td>'
                f'<td class="mono bold">{p["name"]}</td>'
                f'<td>{sc_bar}</td>'
                f'<td class="num">{fmt_score(p["pot_score"])}</td>'
                f'<td class="num" style="color:var(--sap-success);font-weight:700;">{fmt_score(p["reduction"])}</td>'
                f'<td>{bar}</td>'
                f'</tr>'
            )
        return "\n".join(rows)

    def obj_cleanup_rows(obj_list: list) -> str:
        rows = []
        for i, o in enumerate(obj_list, 1):
            bar = cleanup_bar(o["red_pct"], o["score"])
            tag = size_tag(o["score"])
            rows.append(
                f'<tr data-rowidx="{i}">'
                f'<td class="rank">{i}</td>'
                f'<td class="mono">{o["name"]}</td>'
                f'<td class="mono">{o["package"]}</td>'
                f'<td>{tag} {fmt_score(o["score"])}</td>'
                f'<td class="num">{fmt_score(o["pot_score"])}</td>'
                f'<td class="num" style="color:var(--sap-success);font-weight:700;">−{fmt_score(o["reduction"])}</td>'
                f'<td>{bar}</td>'
                f'</tr>'
            )
        return "\n".join(rows)

    def level_upgrade_groups_html(upgrades: list) -> str:
        """Render upgrade objects grouped by transition type, sorted best-jump first."""
        LEVEL_NAME  = {"1": "Level D", "2": "Level C", "3": "Level B", None: "Level A (fully clean)"}
        LEVEL_COLOR_UP = {"1": "#bb0000", "2": "#e76500", "3": "#0070f2", None: "#107e3e"}
        SUC_CLASS_LABEL = {
            "oneObject":       "one successor object",
            "multipleObjects": "multiple successor objects",
            "concept":         "successor concept (no specific object yet)",
            "":                "no successor details in CR",
        }
        TRANSITION_ORDER = [("1",None),("1","2"),("1","3"),("2",None),("2","3"),("3",None)]

        from collections import defaultdict
        groups = defaultdict(list)
        for u in upgrades:
            groups[(u["level"], u["pot_level"])].append(u)

        uid_counter = [0]

        def make_detail_panel(obj_name: str, obj_type_str: str) -> str:
            details = agg["obj_suc_detail"].get((obj_name, obj_type_str), [])
            if not details:
                return ""
            uid_counter[0] += 1
            panel_id = f"suc-detail-{uid_counter[0]}"
            rows_html = []
            has_any_warning = False
            for d in details:
                if d["successors"]:
                    suc_targets = ", ".join(
                        f'<code>{s.get("objectType","")} {s.get("objectKey","")}</code>'
                        for s in d["successors"]
                    )
                    suc_desc = f'{SUC_CLASS_LABEL.get(d["suc_class"], d["suc_class"])}: {suc_targets}'
                elif d["suc_concept"]:
                    suc_desc = f'Successor concept: <em>{d["suc_concept"]}</em> (no specific object listed in CR yet)'
                else:
                    suc_desc = "Successor identified in ATC but not detailed in Cloudification Repository"

                prio_color = "var(--sap-error)" if d["prio"] == "1" else "var(--sap-warning)" if d["prio"] == "2" else "var(--sap-info)"
                prio_badge = f'<span class="badge" style="background:{prio_color};font-size:0.65rem;">P{d["prio"]}</span>'
                count_str  = f' ({d["count"]}×)' if d.get("count", 1) > 1 else ""

                warn_html = ""
                if d["write_warning"]:
                    has_any_warning = True
                    warn_html = '<span class="write-warn">⚠ Write access — CDS successor covers reads only. Verify whether a write successor exists before migrating.</span>'

                rows_html.append(
                    f'<div class="suc-row">'
                    f'<span class="suc-arrow">→</span>'
                    f'<div>'
                    f'<span class="suc-ref">{d["display_ref"]}</span>{count_str} {prio_badge}'
                    f'<div class="suc-meta">{suc_desc}{warn_html}</div>'
                    f'</div>'
                    f'</div>'
                )

            toggle_label = "Show successor details"
            if has_any_warning:
                toggle_label += ' ⚠'

            return (
                f'<button class="detail-toggle" onclick="toggleDetail(\'{panel_id}\')" id="btn-{panel_id}">{toggle_label}</button>'
                f'<div class="detail-panel" id="{panel_id}">'
                f'<strong style="font-size:0.75rem;color:var(--sap-text-secondary);">'
                f'Referenced objects with potential successor — verify scope before migrating</strong>'
                + "".join(rows_html)
                + f'</div>'
            )

        html_parts = []
        for cur, pot in TRANSITION_ORDER:
            objs = groups.get((cur, pot), [])
            if not objs:
                continue
            cur_badge = f'<span class="badge" style="background:{LEVEL_COLOR_UP[cur]}">{LEVEL_NAME[cur]}</span>'

            # For "→ Level A" transitions, split by whether the object type can
            # technically be placed under ABAP Cloud Language Version.
            # Types that cannot (PROG, SSFO, VIEW, …) are capped at Level B* —
            # their technical debt score can reach 0 but Level A is not achievable.
            if pot is None:
                capable   = [o for o in objs if o.get("can_reach_a", True)]
                b_star    = [o for o in objs if not o.get("can_reach_a", True)]
                sublists  = []
                if capable:
                    sublists.append((None, capable, False))   # (pot_level, list, is_b_star)
                if b_star:
                    sublists.append(("3", b_star, True))      # pot_level "3" = Level B
            else:
                sublists = [(pot, objs, False)]

            for pot_level, subobjs, is_b_star in sublists:
                if is_b_star:
                    pot_badge  = (
                        f'<span class="badge" style="background:#0070f2">Level B</span>'
                        f'<sup style="font-size:0.6rem;color:var(--sap-text-secondary);margin-left:2px;" '
                        f'title="Score can reach 0, but ABAP Cloud Language Version is not technically applicable for this object type">*</sup>'
                    )
                    group_note = (
                        "— all findings reference objects with a potential successor. "
                        "<strong>These object types cannot use ABAP Cloud Language Version</strong> "
                        "(e.g. PROG, SSFO, VIEW) — the technical debt score can reach 0 but "
                        "the highest achievable clean core level is <strong>Level B</strong>."
                    )
                    tab_suffix = f"up-{cur}-bstar"
                else:
                    pot_badge  = f'<span class="badge" style="background:{LEVEL_COLOR_UP[pot_level]}">{LEVEL_NAME[pot_level]}</span>'
                    if pot_level is None:
                        group_note = (
                            "— all findings reference objects with a potential successor in the "
                            "Cloudification Repository. These object types support ABAP Cloud "
                            "Language Version — Level A is technically achievable after migration "
                            "(subject to functional verification)."
                        )
                    else:
                        group_note = "— all worst-priority findings reference objects with a potential successor"
                    tab_suffix = f"up-{cur}-{'none' if pot_level is None else pot_level}"

                rows = []
                for _row_i, o in enumerate(sorted(subobjs, key=lambda x: -x["score"]), 1):
                    suc_parts = []
                    if o["suc_p1"]: suc_parts.append(f'<span style="color:var(--sap-error)">{o["suc_p1"]} P1</span>')
                    if o["suc_p2"]: suc_parts.append(f'<span style="color:var(--sap-warning)">{o["suc_p2"]} P2</span>')
                    if o["suc_p3"]: suc_parts.append(f'<span style="color:var(--sap-info)">{o["suc_p3"]} P3</span>')
                    suc_str = " + ".join(suc_parts) + " with potential successor"

                    rem_parts = []
                    if o["rem_p1"]: rem_parts.append(f'<span style="color:var(--sap-error)">{o["rem_p1"]} P1</span>')
                    if o["rem_p2"]: rem_parts.append(f'<span style="color:var(--sap-warning)">{o["rem_p2"]} P2</span>')
                    if o["rem_p3"]: rem_parts.append(f'<span style="color:var(--sap-info)">{o["rem_p3"]} P3</span>')
                    rem_str = (", ".join(rem_parts) + " remaining") if rem_parts else \
                        '<span style="color:var(--sap-success);font-weight:700;">none — potentially fully clean</span>'

                    tag = size_tag(o["score"])
                    detail_html = make_detail_panel(o["name"], o["type"])
                    rows.append(
                        f'<tr data-rowidx="{_row_i}">'
                        f'<td class="mono">{o["name"]}</td>'
                        f'<td>{o["type"]}</td>'
                        f'<td class="mono">{o["package"]}</td>'
                        f'<td>{tag} {fmt_score(o["score"])}</td>'
                        f'<td style="font-size:0.8rem;">{suc_str}<br/>{detail_html}</td>'
                        f'<td style="font-size:0.8rem;">{rem_str}</td>'
                        f'</tr>'
                    )

                html_parts.append((tab_suffix, cur_badge, pot_badge, len(subobjs), group_note, rows))

        return html_parts

    def upgrade_subtabs_html(groups: list) -> str:
        """Render transition groups as plain-JS sub-tabs — no anchoring needed."""
        if not groups:
            return '<p style="color:var(--sap-text-secondary);">No upgrade candidates found.</p>'

        tab_bar_items = []
        tab_panels    = []
        for i, (tab_key, cur_badge, pot_badge, count, group_note, rows) in enumerate(groups):
            active_cls = " active" if i == 0 else ""
            tab_bar_items.append(
                f'<button class="subtab-btn{active_cls}" id="btn-{tab_key}" '
                f'onclick="showUpgradeTab(\'{tab_key}\')">'
                f'{cur_badge} <span class="subtab-arrow">→</span> {pot_badge}'
                f'<span class="upgrade-count-badge">{count}</span>'
                f'</button>'
            )
            display = '' if i == 0 else 'display:none;'
            tbl_id = f"uptbl-{tab_key}"
            tab_panels.append(
                f'<div class="upgrade-subtab-panel" id="panel-{tab_key}" style="{display}">'
                f'<p style="font-size:0.8rem;color:var(--sap-text-secondary);margin-bottom:0.75rem;">{group_note}'
                f'<span style="float:right;">{upgrade_count_control(tbl_id, count, "applyUpgradeRowCount")}</span></p>'
                f'<div class="table-wrap"><table id="{tbl_id}" style="table-layout:fixed;width:100%;">'
                f'<colgroup>'
                f'<col style="width:24%"/>'
                f'<col style="width:6%"/>'
                f'<col style="width:16%"/>'
                f'<col style="width:8%"/>'
                f'<col style="width:24%"/>'
                f'<col style="width:22%"/>'
                f'</colgroup>'
                f'<thead><tr>'
                f'<th>Object</th><th>Type</th><th>Package</th>'
                f'<th>Score</th><th>Potential successor findings</th><th>Remaining after migration</th>'
                f'</tr></thead>'
                f'<tbody>{"".join(rows)}</tbody>'
                f'</table></div>'
                f'</div>'
            )

        all_keys = [tab_key for tab_key, *_ in groups]
        keys_js  = json.dumps(all_keys)
        return f"""
    <div class="subtab-label">Select a transition type:</div>
    <div class="subtab-bar">{"".join(tab_bar_items)}</div>
    {"".join(tab_panels)}
    <script>
    var _upgradeTabKeys = {keys_js};
    function showUpgradeTab(key) {{
      _upgradeTabKeys.forEach(function(k) {{
        var panel = document.getElementById('panel-' + k);
        var btn   = document.getElementById('btn-' + k);
        if (panel) panel.style.display = (k === key) ? '' : 'none';
        if (btn) btn.classList.toggle('active', k === key);
      }});
    }}
    </script>"""

    def upgrade_summary_html(upgrades: list) -> str:
        """Compact summary table: one row per transition, switches to that sub-tab on click."""
        LEVEL_NAME  = {"1": "Level D", "2": "Level C", "3": "Level B", None: "Level A"}
        LEVEL_COLOR_UP = {"1": "#bb0000", "2": "#e76500", "3": "#0070f2", None: "#107e3e"}
        TRANSITION_ORDER = [("1",None),("1","2"),("1","3"),("2",None),("2","3"),("3",None)]

        from collections import defaultdict
        groups = defaultdict(list)
        for u in upgrades:
            groups[(u["level"], u["pot_level"])].append(u)

        rows = []
        for cur, pot in TRANSITION_ORDER:
            objs = groups.get((cur, pot), [])
            if not objs:
                continue
            cur_badge = f'<span class="badge" style="background:{LEVEL_COLOR_UP[cur]}">{LEVEL_NAME[cur]}</span>'

            if pot is None:
                # split by Level-A capability
                capable = [o for o in objs if o.get("can_reach_a", True)]
                b_star  = [o for o in objs if not o.get("can_reach_a", True)]
                sublists = []
                if capable:
                    sublists.append((None, capable, False))
                if b_star:
                    sublists.append(("3", b_star, True))
            else:
                sublists = [(pot, objs, False)]

            for pot_level, subobjs, is_b_star in sublists:
                if is_b_star:
                    tab_key  = f"up-{cur}-bstar"
                    pot_badge = (
                        f'<span class="badge" style="background:#0070f2">Level B</span>'
                        f'<sup style="font-size:0.6rem;color:var(--sap-text-secondary);margin-left:2px;" '
                        f'title="Score can reach 0, but Level A is not technically applicable for these object types">*</sup>'
                    )
                else:
                    tab_key  = f"up-{cur}-{'none' if pot_level is None else pot_level}"
                    pot_badge = f'<span class="badge" style="background:{LEVEL_COLOR_UP[pot_level]}">{LEVEL_NAME[pot_level]}</span>'

                total_score_sum = sum(o["score"] for o in subobjs)
                rows.append(
                    f'<tr class="clickable-row" data-rowidx="{len(rows)+1}" onclick="goToTab(\'obj-upgrades\');setTimeout(function(){{showUpgradeTab(\'{tab_key}\')}},80);">'
                    f'<td><span class="level-transition">{cur_badge} <span class="level-arrow">→</span> {pot_badge}</span></td>'
                    f'<td class="num bold">{len(subobjs)}</td>'
                    f'<td class="num">{fmt_score(total_score_sum)}</td>'
                    f'<td style="color:var(--sap-accent);font-size:0.8rem;white-space:nowrap;">View details →</td>'
                    f'</tr>'
                )

        return f"""
    <div class="table-wrap">
      <table id="tbl-obj-upgrade-summary">
        <thead>
          <tr>
            <th>Transition</th>
            <th class="num">Objects</th>
            <th class="num">Combined Score</th>
            <th></th>
          </tr>
        </thead>
        <tbody>{"".join(rows)}</tbody>
      </table>
    </div>"""

    def pkg_level_upgrade_html(upgrades: list) -> str:
        LEVEL_NAME     = {"1": "Level D", "2": "Level C", "3": "Level B", None: "Level A (fully clean)"}
        LEVEL_COLOR_UP = {"1": "#bb0000", "2": "#e76500", "3": "#0070f2", None: "#107e3e"}

        if not upgrades:
            return """
  <div class="section-title" style="border-bottom-color: var(--sap-success); font-size:0.9rem; margin-top:0.25rem;">
    Level Upgrade Candidates — Packages
  </div>
  <div class="card">
    <div class="notice" style="background:#f0faf0; border-color:#a0d8a0; margin-bottom:0;">
      <span class="notice-icon" style="color:var(--sap-success);">✓</span>
      <span>No package can improve its Clean Core Level based on available successors alone.
      Individual objects within packages may still be upgradeable — see the <strong>Obj Upgrades</strong> tab.</span>
    </div>
  </div>"""

        rows = []
        for p in upgrades:
            cur_badge = f'<span class="badge" style="background:{LEVEL_COLOR_UP[p["level"]]}">{LEVEL_NAME[p["level"]]}</span>'
            pot_badge = f'<span class="badge" style="background:{LEVEL_COLOR_UP[p["pot_level"]]}">{LEVEL_NAME[p["pot_level"]]}</span>'

            suc_parts = []
            if p["suc_p1"]: suc_parts.append(f'<span style="color:var(--sap-error)">{p["suc_p1"]} P1</span>')
            if p["suc_p2"]: suc_parts.append(f'<span style="color:var(--sap-warning)">{p["suc_p2"]} P2</span>')
            if p["suc_p3"]: suc_parts.append(f'<span style="color:var(--sap-info)">{p["suc_p3"]} P3</span>')
            suc_str = " + ".join(suc_parts)

            rem_parts = []
            if p["rem_p1"]: rem_parts.append(f'<span style="color:var(--sap-error)">{p["rem_p1"]} P1</span>')
            if p["rem_p2"]: rem_parts.append(f'<span style="color:var(--sap-warning)">{p["rem_p2"]} P2</span>')
            if p["rem_p3"]: rem_parts.append(f'<span style="color:var(--sap-info)">{p["rem_p3"]} P3</span>')
            rem_str = (", ".join(rem_parts) + " remaining") if rem_parts else \
                '<span style="color:var(--sap-success);font-weight:700;">none — potentially fully clean</span>'

            pkg_panel_id = f"pkg-panel-{p['name'].replace(' ', '_')}"
            rows.append(
                f'<tr class="clickable-row" data-rowidx="{len(rows)+1}" onclick="goToTab(\'pkg-upgrades\');setTimeout(function(){{showPkgPanel(\'{pkg_panel_id}\')}},80);">'
                f'<td class="mono bold">{p["name"]}</td>'
                f'<td class="num">{p["obj_count"]}</td>'
                f'<td><span class="level-transition">{cur_badge} <span class="level-arrow">→</span> {pot_badge}</span></td>'
                f'<td class="num bold">{fmt_score(p["score"])}</td>'
                f'<td style="font-size:0.8rem;">{suc_str}</td>'
                f'<td style="font-size:0.8rem;">{rem_str}</td>'
                f'<td style="color:var(--sap-accent);font-size:0.8rem;white-space:nowrap;">View details →</td>'
                f'</tr>'
            )

        return f"""
  <div class="section-title" style="border-bottom-color: var(--sap-success); font-size:0.9rem; margin-top:0.25rem;">
    Level Upgrade Candidates — Packages
    <span class="count-tag" style="background:var(--sap-success);">{len(upgrades)} packages</span>
    {upgrade_count_control("tbl-pkg-upgrade-summary", len(upgrades), "applyUpgradeRowCount")}
  </div>
  <div class="card">
    <div class="notice" style="margin-bottom:1rem; background:#f0faf0; border-color:#a0d8a0;">
      <span class="notice-icon" style="color:var(--sap-success);">✓</span>
      <span>
        These packages could improve their overall Clean Core Level if all successor-available
        findings across their objects were migrated. The package level is determined by its
        worst-level object — so a package is upgradeable only when <em>all</em> objects
        driving the worst priority level have successor-available findings.
        As always, verify each successor before planning the migration.
      </span>
    </div>
    <div class="table-wrap">
      <table id="tbl-pkg-upgrade-summary">
        <thead>
          <tr>
            <th>Package</th>
            <th class="num">Objects</th>
            <th>Potential Transition</th>
            <th class="num">Score</th>
            <th>Findings with Successor</th>
            <th>Remaining after Migration</th>
            <th></th>
          </tr>
        </thead>
        <tbody>{"".join(rows)}</tbody>
      </table>
    </div>
  </div>"""

    def pkg_upgrade_detail_html(pkg_upgrades: list, agg: dict) -> str:
        """For each upgradeable package, list all its objects with upgrade info."""
        LEVEL_NAME     = {"1": "Level D", "2": "Level C", "3": "Level B", None: "Level A (fully clean)"}
        LEVEL_COLOR_UP = {"1": "#bb0000", "2": "#e76500", "3": "#0070f2", None: "#107e3e"}
        SUC_CLASS_LABEL = {
            "oneObject":       "one successor object",
            "multipleObjects": "multiple successor objects",
            "concept":         "successor concept (no specific object yet)",
            "":                "no successor details in CR",
        }

        if not pkg_upgrades:
            return '<p style="color:var(--sap-text-secondary);font-size:0.875rem;">No packages qualify for a level upgrade based on available successors.</p>'

        uid_counter = [0]

        def make_detail_panel(obj_name: str, obj_type_str: str) -> str:
            details = agg["obj_suc_detail"].get((obj_name, obj_type_str), [])
            if not details:
                return ""
            uid_counter[0] += 1
            panel_id = f"pkgd-{uid_counter[0]}"
            rows_html = []
            has_any_warning = False
            for d in details:
                if d["successors"]:
                    suc_targets = ", ".join(
                        f'<code>{s.get("objectType","")} {s.get("objectKey","")}</code>'
                        for s in d["successors"]
                    )
                    suc_desc = f'{SUC_CLASS_LABEL.get(d["suc_class"], d["suc_class"])}: {suc_targets}'
                elif d["suc_concept"]:
                    suc_desc = f'Successor concept: <em>{d["suc_concept"]}</em>'
                else:
                    suc_desc = "Successor identified in ATC but not detailed in CR"
                prio_color = "var(--sap-error)" if d["prio"] == "1" else "var(--sap-warning)" if d["prio"] == "2" else "var(--sap-info)"
                prio_badge = f'<span class="badge" style="background:{prio_color};font-size:0.65rem;">P{d["prio"]}</span>'
                count_str  = f' ({d["count"]}×)' if d.get("count", 1) > 1 else ""
                warn_html = ""
                if d["write_warning"]:
                    has_any_warning = True
                    warn_html = '<span class="write-warn">⚠ Write access — CDS successor covers reads only.</span>'
                rows_html.append(
                    f'<div class="suc-row">'
                    f'<span class="suc-arrow">→</span>'
                    f'<div><span class="suc-ref">{d["display_ref"]}</span>{count_str} {prio_badge}'
                    f'<div class="suc-meta">{suc_desc}{warn_html}</div></div></div>'
                )
            toggle_label = "Show successor details" + (" ⚠" if has_any_warning else "")
            return (
                f'<button class="detail-toggle" onclick="toggleDetail(\'{panel_id}\')" id="btn-{panel_id}">{toggle_label}</button>'
                f'<div class="detail-panel" id="{panel_id}">{"".join(rows_html)}</div>'
            )

        parts = []
        obj_by_pkg = defaultdict(list)
        for o in agg["objects"]:
            obj_by_pkg[o["package"]].append(o)

        for _pkg_idx, p in enumerate(pkg_upgrades, 1):
            cur_badge = f'<span class="badge" style="background:{LEVEL_COLOR_UP[p["level"]]}">{LEVEL_NAME[p["level"]]}</span>'
            pot_badge = f'<span class="badge" style="background:{LEVEL_COLOR_UP[p["pot_level"]]}">{LEVEL_NAME[p["pot_level"]]}</span>'
            all_pkg_objs = sorted(obj_by_pkg.get(p["name"], []), key=lambda x: x["score"], reverse=True)

            # Only show objects that are themselves upgrade candidates
            def _worst(a, b, c): return "1" if a > 0 else ("2" if b > 0 else ("3" if c > 0 else None))
            def _is_candidate(o):
                rem_p1 = o["p1"] - o["suc_p1"]
                rem_p2 = o["p2"] - o["suc_p2"]
                rem_p3 = o["p3"] - o["suc_p3"]
                return _worst(rem_p1, rem_p2, rem_p3) != o["level"]
            pkg_objs = [o for o in all_pkg_objs if _is_candidate(o)]

            obj_rows_html = []
            for o in pkg_objs:
                o_cur_badge = f'<span class="badge" style="background:{LEVEL_COLOR_UP[o["level"]]}">{LEVEL_NAME[o["level"]]}</span>'
                rem_p1 = o["p1"] - o["suc_p1"]
                rem_p2 = o["p2"] - o["suc_p2"]
                rem_p3 = o["p3"] - o["suc_p3"]
                pot_lv = _worst(rem_p1, rem_p2, rem_p3)
                if pot_lv != o["level"]:
                    o_pot_badge = f'<span class="badge" style="background:{LEVEL_COLOR_UP[pot_lv]}">{LEVEL_NAME[pot_lv]}</span>'
                    transition  = f'<span class="level-transition">{o_cur_badge} <span class="level-arrow">→</span> {o_pot_badge}</span>'
                else:
                    transition = o_cur_badge
                detail = make_detail_panel(o["name"], o["type"])
                obj_rows_html.append(
                    f'<tr>'
                    f'<td class="mono">{o["name"]}</td>'
                    f'<td>{o["type"]}</td>'
                    f'<td class="num bold">{fmt_score(o["score"])}</td>'
                    f'<td>{transition}</td>'
                    f'<td style="font-size:0.8rem;">{detail}</td>'
                    f'</tr>'
                )

            pkg_panel_id = f"pkg-panel-{p['name'].replace(' ', '_')}"
            parts.append(f"""
    <div class="transition-group upgrade-pkg-panel" data-pkgidx="{_pkg_idx}" id="{pkg_panel_id}" style="margin-bottom:1.5rem;">
      <div class="transition-group-header">
        <span class="mono bold" style="font-size:0.85rem;">{p["name"]}</span>
        <span class="level-transition">{cur_badge} <span class="level-arrow">→</span> {pot_badge}</span>
        <span class="upgrade-count-badge">{p["obj_count"]} objects</span>
        <span style="color:var(--sap-text-secondary);font-size:0.75rem;">score: {fmt_score(p["score"])}</span>
      </div>
      <div class="table-wrap">
        <table style="table-layout:fixed;width:100%;">
          <colgroup>
            <col style="width:28%"/>
            <col style="width:6%"/>
            <col style="width:8%"/>
            <col style="width:20%"/>
            <col style="width:38%"/>
          </colgroup>
          <thead><tr>
            <th>Object</th><th>Type</th><th class="num">Score</th>
            <th>Level / Potential Transition</th><th>Successor Details</th>
          </tr></thead>
          <tbody>{"".join(obj_rows_html)}</tbody>
        </table>
      </div>
    </div>""")

        all_pkg_ids = json.dumps([f"pkg-panel-{p['name'].replace(' ', '_')}" for p in pkg_upgrades])
        show_fn = f"""<script>
    var _pkgPanelIds = {all_pkg_ids};
    function showPkgPanel(panelId) {{
      _pkgPanelIds.forEach(function(id) {{
        var el = document.getElementById(id);
        if (el) el.style.display = (id === panelId) ? '' : 'none';
      }});
      var backEl = document.getElementById('pkg-panel-back');
      if (backEl) backEl.style.display = '';
    }}
    function showAllPkgPanels() {{
      _pkgPanelIds.forEach(function(id) {{
        var el = document.getElementById(id);
        if (el) el.style.display = '';
      }});
      var backEl = document.getElementById('pkg-panel-back');
      if (backEl) backEl.style.display = 'none';
    }}
    </script>"""
        back_btn = '<div id="pkg-panel-back" style="display:none;margin-bottom:0.75rem;"><button class="back-btn" onclick="showAllPkgPanels()">← Show all packages</button></div>'
        return back_btn + "\n".join(parts) + show_fn

    level_upgrades = agg["level_upgrades"]
    # number of distinct transition rows in the Objects upgrade-summary table
    _obj_upgrade_transition_count = len({(u["level"], u["pot_level"]) for u in level_upgrades})

    # cleanup data: rendered up to DASH_MAX, revealed via dropdown (full escape = All Data).
    # These sorted/filtered views exist nowhere else, so they must not silently truncate.
    cleanup_pkgs_all = sorted(agg["packages"], key=lambda x: x["red_pct"], reverse=True)
    cleanup_pkgs = cleanup_pkgs_all[:DASH_MAX]
    pkg_level_upgrades = agg["pkg_level_upgrades"]

    # objects by absolute reduction (min score 50 to filter noise)
    cleanup_objs_abs_all = sorted(
        [o for o in agg["objects"] if o["score"] >= 50],
        key=lambda x: x["reduction"], reverse=True
    )
    cleanup_objs_abs = cleanup_objs_abs_all[:DASH_MAX]

    # objects by % reduction (min score 100 for meaningful % comparison)
    cleanup_objs_pct_all = sorted(
        [o for o in agg["objects"] if o["score"] >= 100],
        key=lambda x: x["red_pct"], reverse=True
    )
    cleanup_objs_pct = cleanup_objs_pct_all[:DASH_MAX]

    # Chart data: keep up to CHART_MAX packages (size-adaptive); a dropdown reslices client-side.
    chart_pkgs  = agg["packages"][:CHART_MAX]
    pkg_labels  = json.dumps([p["name"] for p in chart_pkgs])
    pkg_scores  = json.dumps([p["score"] for p in chart_pkgs])
    pkg_p1      = json.dumps([p["p1"] * 10 for p in chart_pkgs])
    pkg_p2      = json.dumps([p["p2"] * 5  for p in chart_pkgs])
    pkg_p3      = json.dumps([p["p3"] * 1  for p in chart_pkgs])

    # Chart dropdown options adapt to CHART_MAX (only steps we actually plotted).
    _chart_cap = min(CHART_MAX, len(agg["packages"]))
    _chart_opts = []
    for n in (10, 25, 50, 75, 100):
        if n < _chart_cap:
            sel = " selected" if n == 10 else ""
            _chart_opts.append(f'<option value="{n}"{sel}>{n}</option>')
    _sel_all = " selected" if _chart_cap <= 10 else ""
    _chart_opts.append(f'<option value="{_chart_cap}"{_sel_all}>{_chart_cap}</option>')
    chart_count_options = "".join(_chart_opts)

    # Refs/pkg dropdown options adapt to CHIP_CAP (how many chips we render per row).
    _refpkg_opts = ['<option value="5" selected>5</option>']
    for n in (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500):
        if n < CHIP_CAP:
            _refpkg_opts.append(f'<option value="{n}">{n}</option>')
    # "Max" reveals every rendered chip (CHIP_CAP); label shows the number.
    _refpkg_opts.append(f'<option value="{CHIP_CAP}">Max ({CHIP_CAP:,})</option>')
    refpkg_options = "".join(_refpkg_opts)

    # All Data → All Packages "SAP Objects" dropdown. This table renders ALL chips
    # (uncapped), so Max reaches the true maximum refs in any package.
    _adref_opts = ['<option value="5" selected>5</option>']
    for n in (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 750, 1000):
        if n < max_pkg_refs:
            _adref_opts.append(f'<option value="{n}">{n}</option>')
    _adref_opts.append(f'<option value="{max_pkg_refs}">Max ({max_pkg_refs:,})</option>')
    alldata_refpkg_options = "".join(_adref_opts)

    # All Data "Show N" dropdowns. Default to "Max" (all rows) so these complete-view
    # tables stay fully visible for Ctrl+F; the user can shrink them for a quick look.
    def alldata_control(table_id: str, total: int) -> str:
        opts = []
        for n in (10, 20, 50, 100, 200, 500, 1000):
            if n < total:
                opts.append(f'<option value="{n}">{n}</option>')
        opts.append(f'<option value="{total}" selected>Max ({total:,})</option>')
        return (
            '<span class="rowcount-ctl">Show '
            f'<select class="rowcount-select" data-table="{table_id}" '
            'onchange="applyRowCount(this.value, this.dataset.table)">'
            + "".join(opts) +
            f'</select></span>{export_button(table_id)}'
        )

    alldata_pkg_control = alldata_control("tbl-alldata-pkg", len(agg["packages"]))
    alldata_obj_control = alldata_control("tbl-alldata-obj", len(agg["objects"]))
    alldata_ref_control = alldata_control("tbl-alldata-ref", len(agg["ref_impact"]))
    alldata_suc_control = alldata_control(
        "tbl-suc-by-obj", sum(len(v) for v in agg["obj_suc_detail"].values())
    )

    # Full search index of every referenced SAP object (all of them, not just the
    # rendered top-N) so the Tab-1 search box can locate items past the render cap.
    _suc_names = {r for r, _ in agg["ref_suc_impact"]}
    ref_search_index = json.dumps([
        {"n": r, "rank": i + 1, "score": s, "suc": (r in _suc_names)}
        for i, (r, s) in enumerate(agg["ref_impact"])
    ])

    generated_on = date.today().isoformat()

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>ATC Clean Core Assessment — {run_title}</title>
<style>
/* SAP Horizon Design System — core tokens */
:root {{
  --sap-font: "72", "72full", Arial, Helvetica, sans-serif;
  --sap-shell-bg:       #1d2d3e;
  --sap-shell-text:     #ffffff;
  --sap-page-bg:        #f5f6f7;
  --sap-card-bg:        #ffffff;
  --sap-border:         #d9d9d9;
  --sap-accent:         #0070f2;
  --sap-accent-dark:    #0064d9;
  --sap-error:          #bb0000;
  --sap-warning:        #e76500;
  --sap-info:           #0070f2;
  --sap-success:        #107e3e;
  --sap-text:           #1d2d3e;
  --sap-text-secondary: #6a6d70;
  --sap-radius:         0.5rem;
  --sap-shadow:         0 2px 8px rgba(0,0,0,0.10);
}}

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  font-family: var(--sap-font);
  font-size: 14px;
  background: var(--sap-page-bg);
  color: var(--sap-text);
  line-height: 1.5;
}}
.tab-page {{ display: block; }}

.run-bar {{
  background: #fff;
  border-bottom: 1px solid var(--sap-border);
  padding: 0.75rem 2rem;
}}
.run-bar h1 {{
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--sap-text);
}}
.run-meta {{
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  margin-top: 0.4rem;
}}
.run-meta-item {{
  font-size: 0.8125rem;
  color: var(--sap-text-secondary);
}}
.run-meta-item strong {{
  color: var(--sap-text);
  font-weight: 600;
}}

.page {{
  max-width: 1400px;
  margin: 0 auto;
  padding: 1.5rem 2rem;
}}

.section-title {{
  font-size: 1rem;
  font-weight: 700;
  color: var(--sap-text);
  margin-bottom: 1rem;
  padding-bottom: 0.4rem;
  border-bottom: 2px solid var(--sap-accent);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}}
.section-title .count-tag {{
  font-size: 0.75rem;
  font-weight: 600;
  background: var(--sap-accent);
  color: #fff;
  border-radius: 999px;
  padding: 0.1rem 0.5rem;
}}
.rowcount-ctl {{
  font-size: 0.75rem;
  font-weight: 500;
  color: var(--sap-text-secondary);
  margin-left: auto;
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
}}
.section-title .rowcount-ctl + .rowcount-ctl {{ margin-left: 1rem; }}
.rowcount-select {{
  font-family: inherit;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--sap-text);
  background: #fff;
  border: 1px solid var(--sap-border);
  border-radius: 4px;
  padding: 0.1rem 0.3rem;
  cursor: pointer;
}}
.excel-btn {{
  font-family: inherit;
  font-size: 0.75rem;
  font-weight: 600;
  color: #fff;
  background: #217346;  /* Excel green */
  border: 1px solid #1a5c37;
  border-radius: 4px;
  padding: 0.15rem 0.55rem;
  margin-left: 0.5rem;
  cursor: pointer;
  white-space: nowrap;
  transition: background 0.15s;
}}
.excel-btn:hover {{ background: #1a5c37; }}
.excel-btn:active {{ background: #14472a; }}
  display: flex;
  gap: 0.5rem;
  align-items: center;
}}
.ref-search-input {{
  flex: 1;
  font-family: inherit;
  font-size: 0.9rem;
  color: var(--sap-text);
  background: #fff;
  border: 1px solid var(--sap-border);
  border-radius: 6px;
  padding: 0.5rem 0.75rem;
}}
.ref-search-input:focus {{
  outline: none;
  border-color: var(--sap-accent);
  box-shadow: 0 0 0 2px rgba(0,112,242,0.15);
}}
.ref-search-clear {{
  font-family: inherit;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--sap-text-secondary);
  background: #f5f6f7;
  border: 1px solid var(--sap-border);
  border-radius: 6px;
  padding: 0.5rem 0.9rem;
  cursor: pointer;
}}
.ref-search-clear:hover {{ background: #ebedee; }}
.ref-search-status {{
  font-size: 0.8rem;
  color: var(--sap-text-secondary);
  margin-top: 0.6rem;
  min-height: 1.1rem;
}}
.ref-search-status b {{ color: var(--sap-text); }}
tr.ref-search-hit td {{ background: #fff6d6 !important; }}

.card {{
  background: var(--sap-card-bg);
  border: 1px solid var(--sap-border);
  border-radius: var(--sap-radius);
  box-shadow: var(--sap-shadow);
  padding: 1.25rem 1.5rem;
  margin-bottom: 1.5rem;
}}

.kpi-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
}}
.kpi-card {{
  background: var(--sap-card-bg);
  border: 1px solid var(--sap-border);
  border-radius: var(--sap-radius);
  box-shadow: var(--sap-shadow);
  padding: 1.25rem 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}}
.kpi-card.accent {{ border-top: 4px solid var(--sap-accent); }}
.kpi-card.success {{ border-top: 4px solid var(--sap-success); }}
.kpi-card.warning {{ border-top: 4px solid var(--sap-warning); }}
.kpi-label {{
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--sap-text-secondary);
}}
.kpi-value {{
  font-size: 2rem;
  font-weight: 700;
  color: var(--sap-text);
  line-height: 1.1;
}}
.kpi-sub {{
  font-size: 0.8125rem;
  color: var(--sap-text-secondary);
}}
.kpi-sub em {{ font-style: normal; color: var(--sap-success); font-weight: 600; }}
.kpi-info {{
  display: inline-block;
  margin-left: 0.35rem;
  font-size: 0.75rem;
  color: var(--sap-text-secondary);
  cursor: help;
  vertical-align: middle;
}}

.level-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
}}
.level-card {{
  background: var(--sap-card-bg);
  border: 1px solid var(--sap-border);
  border-radius: var(--sap-radius);
  box-shadow: var(--sap-shadow);
  padding: 1rem 1.25rem;
}}
.info-card {{ border-top: 4px solid #5a5a5a !important; }}
.level-label {{ font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 0.4rem; }}
.level-count {{ font-size: 1.75rem; font-weight: 700; color: var(--sap-text); }}
.level-pct {{ font-size: 0.8125rem; color: var(--sap-text-secondary); }}
.level-note {{ font-size: 0.75rem; color: var(--sap-text-secondary); margin-top: 0.4rem; font-style: italic; }}

.notice {{
  background: #fff8e5;
  border: 1px solid #f0c050;
  border-radius: var(--sap-radius);
  padding: 0.75rem 1rem;
  font-size: 0.8125rem;
  color: #5a4000;
  margin-bottom: 1.25rem;
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
}}
.notice-icon {{ font-size: 1rem; flex-shrink: 0; margin-top: 1px; }}

.table-wrap {{ overflow-x: auto; }}
table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 0.8125rem;
}}
thead tr {{
  background: #f0f4ff;
  border-bottom: 2px solid var(--sap-accent);
}}
th {{
  padding: 0.55rem 0.75rem;
  text-align: left;
  font-weight: 700;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--sap-text-secondary);
  white-space: nowrap;
}}
td {{
  padding: 0.5rem 0.75rem;
  border-bottom: 1px solid #ececec;
  vertical-align: middle;
}}
tr:last-child td {{ border-bottom: none; }}
tr:hover td {{ background: #f8f9ff; }}
.clickable-row {{ cursor: pointer; }}
.clickable-row:hover td {{ background: #e8f0ff; }}
.rank {{ color: var(--sap-text-secondary); font-size: 0.75rem; font-weight: 600; width: 2rem; }}
.mono {{ font-family: "Courier New", monospace; font-size: 0.8rem; word-break: break-word; }}
.bold {{ font-weight: 700; }}
.num {{ text-align: right; font-variant-numeric: tabular-nums; }}
.red {{ color: var(--sap-error); font-weight: 700; }}
.orange {{ color: var(--sap-warning); font-weight: 700; }}
.blue {{ color: var(--sap-info); font-weight: 600; }}

.badge {{
  display: inline-block;
  color: #fff;
  font-size: 0.7rem;
  font-weight: 700;
  padding: 0.15rem 0.5rem;
  border-radius: 999px;
  white-space: nowrap;
}}

.mini-bar {{
  height: 8px;
  background: #e8edf5;
  border-radius: 4px;
  min-width: 60px;
  max-width: 160px;
}}
.mini-bar-fill {{
  height: 8px;
  background: var(--sap-accent);
  border-radius: 4px;
}}

.refs {{ font-size: 0.75rem; }}
.ref-chip {{
  display: inline-block;
  background: #f0f4ff;
  border: 1px solid #c8d8f8;
  border-radius: 4px;
  padding: 0.1rem 0.4rem;
  margin: 1px;
  font-family: "Courier New", monospace;
  font-size: 0.75rem;
  white-space: nowrap;
}}
.ref-chip em {{ color: var(--sap-text-secondary); }}
.ref-more {{
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--sap-text-secondary);
  background: #eef0f2;
  border: 1px dashed var(--sap-border);
  border-radius: 4px;
  padding: 0.1rem 0.4rem;
  margin: 1px;
  white-space: nowrap;
}}

.chart-container {{
  position: relative;
  height: 300px;
  margin: 0.5rem 0;
}}

.potential-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1rem;
  margin-bottom: 1rem;
}}
.potential-item {{
  background: #f5fbf5;
  border: 1px solid #b0e0b0;
  border-radius: var(--sap-radius);
  padding: 1rem 1.25rem;
}}
.potential-label {{ font-size: 0.75rem; font-weight: 700; text-transform: uppercase; color: var(--sap-success); margin-bottom: 0.25rem; }}
.potential-value {{ font-size: 1.5rem; font-weight: 700; color: var(--sap-success); }}
.potential-sub {{ font-size: 0.8125rem; color: var(--sap-text-secondary); margin-top: 0.2rem; }}

.footer {{
  border-top: 1px solid var(--sap-border);
  margin-top: 2rem;
  padding: 1rem 2rem;
  font-size: 0.75rem;
  color: var(--sap-text-secondary);
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: space-between;
}}

.detail-toggle {{
  cursor: pointer;
  color: var(--sap-accent);
  font-size: 0.75rem;
  font-weight: 600;
  border: none;
  background: none;
  padding: 0;
  font-family: var(--sap-font);
  text-decoration: underline;
  white-space: nowrap;
}}
.detail-toggle:hover {{ color: var(--sap-accent-dark); }}
.detail-panel {{
  display: none;
  background: #f8f9ff;
  border: 1px solid #d0daf5;
  border-radius: 4px;
  padding: 0.6rem 0.75rem;
  margin-top: 0.4rem;
  font-size: 0.8rem;
}}
.detail-panel.open {{ display: block; }}
.suc-row {{
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
  padding: 0.25rem 0;
  border-bottom: 1px solid #e5eaf5;
}}
.suc-row:last-child {{ border-bottom: none; }}
.suc-arrow {{
  color: var(--sap-success);
  font-weight: 700;
  flex-shrink: 0;
  margin-top: 1px;
}}
.suc-ref {{
  font-family: monospace;
  font-size: 0.8rem;
  flex-shrink: 0;
}}
.suc-meta {{
  font-size: 0.75rem;
  color: var(--sap-text-secondary);
  flex: 1;
}}
.write-warn {{
  display: inline-block;
  background: #fff3cd;
  border: 1px solid #f0c040;
  border-radius: 3px;
  padding: 0.1rem 0.4rem;
  font-size: 0.7rem;
  font-weight: 700;
  color: #7a5000;
  margin-left: 0.4rem;
}}

.level-transition {{
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  white-space: nowrap;
}}
.level-arrow {{
  font-size: 0.9rem;
  color: var(--sap-success);
  font-weight: 700;
}}
.transition-group {{
  margin-bottom: 1.25rem;
}}
.transition-group-header {{
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--sap-text-secondary);
  padding: 0.4rem 0.75rem;
  background: #f7f7f7;
  border-radius: 4px;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}}
.upgrade-count-badge {{
  background: var(--sap-success);
  color: #fff;
  font-size: 0.7rem;
  font-weight: 700;
  border-radius: 999px;
  padding: 0.1rem 0.45rem;
}}

.cleanup-bar-wrap {{
  display: flex;
  align-items: center;
  gap: 0.5rem;
  min-width: 160px;
}}
.cleanup-bar-bg {{
  flex: 1;
  height: 10px;
  background: #e8edf5;
  border-radius: 5px;
  overflow: hidden;
  min-width: 80px;
}}
.cleanup-bar-fill {{
  height: 10px;
  border-radius: 5px;
  transition: width 0.3s;
}}
.cleanup-pct {{
  font-size: 0.8125rem;
  font-weight: 700;
  min-width: 3rem;
  text-align: right;
}}
.cleanup-pct.high   {{ color: var(--sap-success); }}
.cleanup-pct.medium {{ color: var(--sap-warning); }}
.cleanup-pct.low    {{ color: var(--sap-text-secondary); }}
.size-tag {{
  display: inline-block;
  font-size: 0.7rem;
  font-weight: 600;
  padding: 0.1rem 0.4rem;
  border-radius: 999px;
  background: #f0f0f0;
  color: #555;
  white-space: nowrap;
}}

.subtab-bar {{
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.25rem;
  padding-bottom: 0.25rem;
}}
.subtab-label {{
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--sap-text-secondary);
  margin-bottom: 0.5rem;
}}
.subtab-btn {{
  background: #fff;
  border: 1px solid var(--sap-border);
  border-radius: 8px;
  padding: 0.5rem 0.85rem;
  font-family: var(--sap-font);
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--sap-text-secondary);
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.35rem;
  white-space: nowrap;
  box-shadow: 0 1px 2px rgba(0,0,0,0.04);
  transition: all 0.12s ease;
}}
.subtab-btn:hover {{
  background: #f0faf0;
  border-color: var(--sap-success);
}}
.subtab-btn.active {{
  background: var(--sap-success);
  border-color: var(--sap-success);
  color: #fff;
  box-shadow: 0 2px 6px rgba(16,126,62,0.35);
}}
.subtab-btn .subtab-arrow {{ opacity: 0.7; font-weight: 700; }}
.subtab-btn.active .upgrade-count-badge {{
  background: rgba(255,255,255,0.25);
  color: #fff;
}}
.subtab-btn.active .badge {{
  box-shadow: 0 0 0 1.5px rgba(255,255,255,0.6);
}}

.back-btn {{
  cursor: pointer;
  background: none;
  border: 1px solid var(--sap-accent);
  color: var(--sap-accent);
  font-family: var(--sap-font);
  font-size: 0.8125rem;
  font-weight: 600;
  padding: 0.35rem 0.9rem;
  border-radius: var(--sap-radius);
}}
.back-btn:hover {{ background: #f0f4ff; }}

@media (max-width: 700px) {{
  .page {{ padding: 1rem; }}
}}

/* ── Native tab bar (no external dependencies) ── */
.shell-bar {{
  background: var(--sap-shell-bg);
  color: var(--sap-shell-text);
  padding: 0.6rem 2rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}}
.shell-bar-title {{
  font-size: 0.9rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  opacity: 0.95;
}}
.shell-bar-sep {{
  opacity: 0.4;
}}
.shell-bar-sub {{
  font-size: 0.8rem;
  opacity: 0.75;
}}
.main-tab-bar {{
  background: #fff;
  border-bottom: 1px solid var(--sap-border);
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
}}
.main-tab-btn {{
  background: #fff;
  border: 1px solid var(--sap-border);
  border-radius: 8px;
  padding: 0.5rem 1.1rem;
  font-family: var(--sap-font);
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--sap-text-secondary);
  cursor: pointer;
  white-space: nowrap;
  box-shadow: 0 1px 2px rgba(0,0,0,0.04);
  transition: all 0.12s ease;
}}
.main-tab-btn:hover {{
  color: var(--sap-accent);
  background: #f0f4ff;
  border-color: var(--sap-accent);
}}
.main-tab-btn.active {{
  color: #fff;
  background: var(--sap-accent);
  border-color: var(--sap-accent);
  box-shadow: 0 2px 6px rgba(0,112,242,0.35);
}}
.tab-count {{
  display: inline-block;
  background: #e8edf5;
  color: var(--sap-text-secondary);
  font-size: 0.7rem;
  font-weight: 700;
  border-radius: 999px;
  padding: 0.05rem 0.45rem;
  margin-left: 0.3rem;
  vertical-align: middle;
}}
.main-tab-btn.active .tab-count {{
  background: rgba(255,255,255,0.25);
  color: #fff;
}}
</style>
<!-- Chart.js CDN — replace with local bundle for fully offline use -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<!-- SheetJS CDN — used by the "Save to Excel" buttons to write real .xlsx files -->
<script src="https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js"></script>
</head>
<body>

<div class="shell-bar">
  <span class="shell-bar-title">SAP</span>
  <span class="shell-bar-sep">|</span>
  <span class="shell-bar-sub">Clean Core Assessment · ATC Findings Dashboard</span>
</div>

<nav class="main-tab-bar" id="main-tabs">
  <button class="main-tab-btn active" data-tab="dashboard" onclick="goToTab('dashboard')">Dashboard</button>
  <button class="main-tab-btn" data-tab="pkg-upgrades" onclick="goToTab('pkg-upgrades')">Pkg Upgrades <span class="tab-count">{len(pkg_level_upgrades)}</span></button>
  <button class="main-tab-btn" data-tab="obj-upgrades" onclick="goToTab('obj-upgrades')">Obj Upgrades <span class="tab-count">{len(level_upgrades)}</span></button>
  <button class="main-tab-btn" data-tab="alldata" onclick="goToTab('alldata')">All Data</button>
  <button class="main-tab-btn" data-tab="info" onclick="goToTab('info')">Methodology &amp; Help</button>
</nav>

<!-- Run info bar -->
<div class="run-bar">
  <h1>{run_title}</h1>
  <div class="run-meta">
    <span class="run-meta-item"><strong>System:</strong> {system}</span>
    <span class="run-meta-item"><strong>Run date:</strong> {run_date}</span>
    <span class="run-meta-item"><strong>Check variant:</strong> {check_var}</span>
    <span class="run-meta-item"><strong>Run series:</strong> {run_series}</span>
    <span class="run-meta-item"><strong>In-scope findings:</strong> {total_findings:,}</span>
    <span class="run-meta-item"><strong>Excluded (out-of-scope checks):</strong> {excluded:,}</span>
    <span class="run-meta-item" title="Non-logic-bearing object types (VIEW, SSFO, SFPF, FUGS, DOMA, WAPA, …) are excluded from all KPIs per Object Type Harmonization. Score shown is what they would contribute if counted."><strong>Non-focus objects (excluded from KPIs):</strong> {non_focus_label} · score {fmt_score(non_focus_score)} not counted</span>
  </div>
</div>

<!-- ── DASHBOARD PAGE ─────────────────────────────────────────────────── -->
<div id="page-dashboard" class="tab-page">
<main class="page">

  <!-- Notice -->
  <div class="notice">
    <span class="notice-icon">⚠</span>
    <span>
      This analysis covers only custom code objects with at least one in-scope ATC finding
      <strong>and</strong> of a <strong>logic-bearing ("focus") object type</strong>
      (BDEF, CLAS, INTF, FUNC, FUGR, FUGX, PROG, DDLS, ENHO, SXCI).
      Objects without findings are <strong>not included</strong> — they cannot be classified as
      "Level A" based on this export alone.
      Non-logic-bearing types (VIEW, SSFO, SFPF, FUGS, DOMA, WAPA, …) are tracked but
      <strong>excluded from all KPIs</strong> — see the run bar above for their count.
      Aligns with the SAP RISE Dashboard Object Type Harmonization (September 2026).
      In-scope checks: <em>Usage of APIs</em>, <em>Critical Statements</em>,
      <em>Allowed Enhancement Technologies</em>.
    </span>
  </div>

  <!-- ── Section 1: KPI Summary ──────────────────────────────────────────── -->
  <div class="section-title">Technical Debt KPIs</div>

  <div class="kpi-grid">
    <div class="kpi-card accent">
      <div class="kpi-label">Total Technical Debt Score</div>
      <div class="kpi-value">{fmt_score(total_score)}</div>
      <div class="kpi-sub">{fmt_score(agg["total_p1"])} × 10 + {fmt_score(agg["total_p2"])} × 5 + {fmt_score(agg["total_p3"])} × 1</div>
    </div>
    <div class="kpi-card success">
      <div class="kpi-label">Potential Score
        <span class="kpi-info" title="One possible scenario: if all findings with a known successor were migrated. This is not a target or commitment — successor coverage must be verified per use case (not all fields/functionality may be available in the successor). See Methodology → Section 7 for details.">ⓘ</span>
      </div>
      <div class="kpi-value">{fmt_score(potential_score)}</div>
      <div class="kpi-sub"><em>−{fmt_score(reduction)} pts ({reduction_pct}%)</em> if {suc_count:,} successor findings resolved
        <br/><span style="font-size:0.7rem; color:var(--sap-text-secondary);">Indicative only — verify successor scope</span>
      </div>
    </div>
    <div class="kpi-card warning">
      <div class="kpi-label">Objects with Findings</div>
      <div class="kpi-value">{total_objs:,}</div>
      <div class="kpi-sub">Across {len(agg["packages"]):,} packages · {total_findings:,} total findings</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-label">Priority Breakdown</div>
      <div class="kpi-value" style="font-size:1.2rem; display:flex; gap:1rem; align-items:baseline;">
        <span style="color:var(--sap-error)">{agg["total_p1"]:,}<small style="font-size:0.65rem;font-weight:400"> P1</small></span>
        <span style="color:var(--sap-warning)">{agg["total_p2"]:,}<small style="font-size:0.65rem;font-weight:400"> P2</small></span>
        <span style="color:var(--sap-info)">{agg["total_p3"]:,}<small style="font-size:0.65rem;font-weight:400"> P3</small></span>
      </div>
      <div class="kpi-sub">Error · Warning · Info</div>
    </div>
  </div>

  <!-- ── Section 2: Clean Core Level Distribution ─────────────────────────── -->
  <div class="section-title">Clean Core Level Distribution
    <span class="count-tag">per object, worst-finding logic</span>
  </div>

  <div class="level-grid">
    {level_cards()}
  </div>

  <!-- ── Section 3: Technical Debt by Package (chart) ──────────────────── -->
  <div class="section-title">Technical Debt Score by Package
    <span class="rowcount-ctl">Show
      <select class="rowcount-select" id="pkgChartCount"
              onchange="applyChartCount(this.value)">
        {chart_count_options}
      </select>
      of {min(CHART_MAX, len(agg["packages"])):,} shown
    </span>
  </div>

  <div class="card">
    <div class="chart-container">
      <canvas id="pkgChart"></canvas>
    </div>
  </div>

  <!-- ── Section 4: Package detail table ───────────────────────────────── -->
  <div class="section-title">Package Detail — Score, Level &amp; Top Referenced SAP Objects
    {rowcount_control("tbl-pkg", len(agg["packages"]))}
    <span class="rowcount-ctl">Refs/pkg
      <select class="rowcount-select" data-table="tbl-pkg"
              onchange="applyRefCount(this.value, this.dataset.table)">
        {refpkg_options}
      </select>
    </span>
  </div>

  <div class="card">
    <div class="table-wrap">
      <table id="tbl-pkg" data-refcount="5">
        <thead>
          <tr>
            <th>#</th>
            <th>Package</th>
            <th class="num">Objects</th>
            <th class="num" style="color:var(--sap-error)">P1 ×10</th>
            <th class="num" style="color:var(--sap-warning)">P2 ×5</th>
            <th class="num" style="color:var(--sap-info)">P3 ×1</th>
            <th class="num">Score</th>
            <th>Level</th>
            <th>Top Referenced SAP Objects (score within pkg)</th>
          </tr>
        </thead>
        <tbody>
          {pkg_rows(top_pkgs)}
        </tbody>
      </table>
    </div>
  </div>

  <!-- ── Section 5: Top objects by score ───────────────────────────────── -->
  <div class="section-title">Top Custom Code Objects by Technical Debt Score
    {rowcount_control("tbl-obj-score", len(agg["objects"]))}
  </div>

  <div class="card">
    <div class="table-wrap">
      <table id="tbl-obj-score">
        <thead>
          <tr>
            <th>#</th>
            <th>Object</th>
            <th>Type</th>
            <th>Package</th>
            <th class="num" style="color:var(--sap-error)">P1</th>
            <th class="num" style="color:var(--sap-warning)">P2</th>
            <th class="num" style="color:var(--sap-info)">P3</th>
            <th class="num">Score</th>
            <th>Level</th>
          </tr>
        </thead>
        <tbody>
          {obj_rows(top_objs_score, "score")}
        </tbody>
      </table>
    </div>
  </div>

  <!-- ── Section 6: Top objects by Level D (P1) ────────────────────────── -->
  <div class="section-title">Top Custom Code Objects by Level D Findings (P1 Errors)
    {rowcount_control("tbl-obj-d", sum(1 for o in agg["objects"] if o["p1"] > 0))}
  </div>

  <div class="card">
    <div class="table-wrap">
      <table id="tbl-obj-d">
        <thead>
          <tr>
            <th>#</th>
            <th>Object</th>
            <th>Type</th>
            <th>Package</th>
            <th class="num" style="color:var(--sap-error)">P1</th>
            <th class="num" style="color:var(--sap-warning)">P2</th>
            <th class="num" style="color:var(--sap-info)">P3</th>
            <th class="num">Score</th>
            <th>Level</th>
          </tr>
        </thead>
        <tbody>
          {obj_rows([o for o in top_objs_d if o["p1"] > 0], "p1")}
        </tbody>
      </table>
    </div>
  </div>

  <!-- ── Section 7: Top referenced SAP objects ─────────────────────────── -->
  <div class="section-title">Search Referenced SAP Objects</div>
  <div class="card">
    <div class="ref-search-wrap">
      <input type="text" id="refSearch" class="ref-search-input"
             placeholder="Search referenced SAP object (e.g. BAPI_PO_GETDETAIL)…"
             oninput="applyRefSearch(this.value)" autocomplete="off"/>
      <button class="ref-search-clear" onclick="clearRefSearch()">Clear</button>
    </div>
    <div id="refSearchStatus" class="ref-search-status"></div>
  </div>

  <div class="section-title">Top Referenced SAP Objects by Impact
    {rowcount_control("tbl-ref", len(agg["ref_impact"]))}
  </div>

  <div class="card">
    <div class="notice" style="margin-bottom:0.75rem;">
      <span class="notice-icon">ℹ</span>
      <span>Impact score = sum of weighted findings across all custom objects referencing this SAP object.
      "Custom objects" = number of distinct custom code objects that reference it.</span>
    </div>
    <div class="table-wrap">
      <table id="tbl-ref">
        <thead>
          <tr>
            <th>#</th>
            <th>Referenced SAP Object</th>
            <th class="num">Custom Objects</th>
            <th class="num">Impact Score</th>
            <th>Relative Impact</th>
          </tr>
        </thead>
        <tbody>
          {ref_rows(top_refs)}
        </tbody>
      </table>
    </div>
  </div>

  <!-- ── Section 7b: Top referenced SAP objects with successor ─────────── -->
  <div class="section-title">Top Referenced SAP Objects with Successor
    {rowcount_control("tbl-ref-suc", len(agg["ref_suc_impact"]))}
  </div>

  <div class="card">
    <div class="notice" style="background:#f0faf0; border-color:#a0d8a0; margin-bottom:0.75rem;">
      <span class="notice-icon" style="color:var(--sap-success);">✓</span>
      <span>
        These SAP objects are referenced by findings with a <code>_SUC</code> message code —
        meaning ATC has identified a potential successor. Use this list to prioritise:
        <em>where should we verify whether the successor is legitimately applicable in our scenarios?</em>
        A high score means migrating this one SAP object could eliminate the most technical debt.
        The <strong>spread</strong> column shows how many custom objects and packages are affected:
        fewer objects concentrated in fewer packages means the migration effort is easier to scope
        and coordinate. Colour coding:
        <strong style="color:var(--sap-success);">green</strong> = highly concentrated (≤5 objects, 1 package),
        <strong style="color:var(--sap-warning);">amber</strong> = moderate (≤10 objects, ≤2 packages),
        <span style="color:var(--sap-text-secondary);">grey</span> = spread across many objects/packages.
      </span>
    </div>
    <div class="table-wrap">
      <table id="tbl-ref-suc">
        <thead>
          <tr>
            <th>#</th>
            <th>Referenced SAP Object</th>
            <th class="num">Findings (_SUC)</th>
            <th class="num">Successor Impact Score</th>
            <th class="num">Spread (objects / packages)</th>
            <th>Relative successor impact</th>
          </tr>
        </thead>
        <tbody>
          {ref_suc_rows(top_refs_suc)}
        </tbody>
      </table>
    </div>
  </div>

  <!-- ── Section 8: Cleanup Potential ─────────────────────────────────── -->
  <div class="section-title">Cleanup Potential — Where Successor Migration Has Real Impact</div>

  <!-- ── Section 8a: Potential Score detail ────────────────────────────── -->
  <div class="section-title" style="font-size:0.9rem; margin-top:0.25rem;">
    Potential Score — Successor-Available Findings
  </div>

  <div class="card">
    <div class="notice" style="margin-bottom:1rem; background:#fff8e1; border-color:#f0c040;">
      <span class="notice-icon">⚠</span>
      <span>
        <strong>The Potential Score is one indicative scenario — not a target or forecast.</strong>
        It answers: <em>"What would the score be if every finding with a known successor were migrated?"</em>
        In practice, successor migration is just one of several options for reducing technical debt,
        and it may not always be the right starting point.
        <strong>Always verify successor scope before planning any migration:</strong> not all
        fields and functionality may be available in the successor object. In particular,
        CDS-based successors typically cover read access only — write scenarios require separate
        validation. See the
        <a href="https://sap.github.io/abap-atc-cr-cv-s4hc" target="_blank">Cloudification Repository</a>
        for successor details per object.
      </span>
    </div>
    <div class="notice" style="margin-bottom:1rem;">
      <span class="notice-icon">ℹ</span>
      <span>
        Findings with a <code>_SUC</code> message code indicate the referenced SAP object
        has a known successor. Successor classification is looked up in the bundled
        <a href="https://sap.github.io/abap-atc-cr-cv-s4hc" target="_blank">Cloudification Repository (CR)</a>
        data: <strong>Released</strong> successor → 0 pts; <strong>Classic API</strong>
        successor → 1 pt. Where no CR entry is found, Classic API is assumed (conservative).
      </span>
    </div>
    <div class="potential-grid">
      <div class="potential-item">
        <div class="potential-label">Findings with Successor</div>
        <div class="potential-value">{suc_count:,}</div>
        <div class="potential-sub">of {total_findings:,} in-scope findings ({pct(suc_count, total_findings)}%)</div>
      </div>
      <div class="potential-item">
        <div class="potential-label">Score Reduction Possible</div>
        <div class="potential-value">−{fmt_score(reduction)}</div>
        <div class="potential-sub">{reduction_pct}% of current total score</div>
      </div>
      <div class="potential-item">
        <div class="potential-label">Potential Score</div>
        <div class="potential-value">{fmt_score(potential_score)}</div>
        <div class="potential-sub">after full successor migration</div>
      </div>
    </div>
  </div>

  <!-- ── Section 8b: Package Level Upgrade Candidates ────────────────── -->
  {pkg_level_upgrade_html(pkg_level_upgrades)}

  <!-- ── Section 8c: Level Upgrade Candidates — Objects (summary) ─────── -->
  <div class="section-title" style="border-bottom-color: var(--sap-success); font-size:0.9rem; margin-top:0.25rem;">
    Level Upgrade Candidates — Objects
    <span class="count-tag" style="background:var(--sap-success);">{len(level_upgrades)} objects</span>
    {upgrade_count_control("tbl-obj-upgrade-summary", _obj_upgrade_transition_count, "applyUpgradeRowCount")}
  </div>

  <div class="card">
    <div class="notice" style="margin-bottom:1rem; background:#f0faf0; border-color:#a0d8a0;">
      <span class="notice-icon" style="color:var(--sap-success);">✓</span>
      <span>
        Objects that can potentially improve their Clean Core Level by migrating
        successor-available findings. Click a transition row to open the full detail.
      </span>
    </div>
    {upgrade_summary_html(level_upgrades)}
  </div>

  <!-- ── Section 8d: Score reduction tables ───────────────────────────── -->
  <div class="card">
    <div class="notice" style="margin-bottom:1rem;">
      <span class="notice-icon">ℹ</span>
      <span>
        A high reduction % is only meaningful if the object or package also has significant
        technical debt to begin with. Size tags (XL / L / M / S) indicate the current score
        tier so you can spot high-impact targets vs. small wins.
        Color coding: <strong style="color:#107e3e">≥ 40% reduction</strong> (green),
        <strong style="color:#e76500">15–39%</strong> (amber),
        <span style="color:#9e9e9e">below 15%</span> (grey — low successor coverage).
        <br/>These lists render up to the dashboard row cap; use the dropdowns to grow them,
        or see <strong>All Data → All Objects</strong> (Potential / Reduction / Reduction % columns)
        for the complete, unfiltered ranking.
      </span>
    </div>

    <div class="section-title" style="font-size:0.875rem; margin-top:0.5rem;">
      By Package — Reduction % &amp; Absolute Gain
      {rowcount_control("tbl-cleanup-pkg", len(cleanup_pkgs_all))}
    </div>
    <div class="table-wrap" style="margin-bottom:1.5rem;">
      <table id="tbl-cleanup-pkg">
        <thead>
          <tr>
            <th>#</th>
            <th>Package</th>
            <th>Current Score</th>
            <th class="num">Potential Score</th>
            <th class="num">Absolute Reduction</th>
            <th>Reduction %</th>
          </tr>
        </thead>
        <tbody>
          {pkg_cleanup_rows(cleanup_pkgs)}
        </tbody>
      </table>
    </div>

    <div class="section-title" style="font-size:0.875rem; margin-top:0.5rem;">
      Top Objects by Absolute Score Reduction
      <span class="count-tag">min score 50</span>
      {rowcount_control("tbl-cleanup-abs", len(cleanup_objs_abs_all))}
    </div>
    <div class="table-wrap" style="margin-bottom:1.5rem;">
      <table id="tbl-cleanup-abs">
        <thead>
          <tr>
            <th>#</th>
            <th>Object</th>
            <th>Package</th>
            <th>Current Score</th>
            <th class="num">Potential Score</th>
            <th class="num">Reduction</th>
            <th>Reduction %</th>
          </tr>
        </thead>
        <tbody>
          {obj_cleanup_rows(cleanup_objs_abs)}
        </tbody>
      </table>
    </div>

    <div class="section-title" style="font-size:0.875rem; margin-top:0.5rem;">
      Top Objects by Relative Reduction %
      <span class="count-tag">min score 100</span>
      {rowcount_control("tbl-cleanup-pct", len(cleanup_objs_pct_all))}
    </div>
    <p style="font-size:0.8125rem; color:var(--sap-text-secondary); margin-bottom:0.75rem;">
      Objects where successor migration addresses the biggest <em>relative</em> share of debt.
      Minimum score of 100 applied to exclude objects too small to matter.
    </p>
    <div class="table-wrap">
      <table id="tbl-cleanup-pct">
        <thead>
          <tr>
            <th>#</th>
            <th>Object</th>
            <th>Package</th>
            <th>Current Score</th>
            <th class="num">Potential Score</th>
            <th class="num">Reduction</th>
            <th>Reduction %</th>
          </tr>
        </thead>
        <tbody>
          {obj_cleanup_rows(cleanup_objs_pct)}
        </tbody>
      </table>
    </div>
  </div>

</main>
</div>

<!-- ── PKG UPGRADES PAGE ──────────────────────────────────────────────── -->
<div id="page-pkg-upgrades" class="tab-page" style="display:none;">
<main class="page">

  <div style="margin-bottom:1rem;">
    <button class="back-btn" onclick="goToTab('dashboard')">← Back to Dashboard</button>
  </div>

  <div class="section-title" style="border-bottom-color: var(--sap-success);">
    Level Upgrade Candidates — By Package
    <span class="count-tag" style="background:var(--sap-success);">{len(pkg_level_upgrades)} packages</span>
    {upgrade_count_control("upgrade-pkg", len(pkg_level_upgrades), "applyUpgradePkgCount", exportable=False)}
  </div>
  <div class="card">
    <div class="notice" style="margin-bottom:1rem; background:#f0faf0; border-color:#a0d8a0;">
      <span class="notice-icon" style="color:var(--sap-success);">✓</span>
      <span>
        Packages whose overall Clean Core Level could improve. Only the objects within each
        package that are themselves upgrade candidates are shown. Expand successor details
        per object to see what the Cloudification Repository says about each referenced SAP object.
      </span>
    </div>
    {pkg_upgrade_detail_html(pkg_level_upgrades, agg)}
  </div>

</main>
</div>

<!-- ── OBJ UPGRADES PAGE ──────────────────────────────────────────────── -->
<div id="page-obj-upgrades" class="tab-page" style="display:none;">
<main class="page">

  <div style="margin-bottom:1rem;">
    <button class="back-btn" onclick="goToTab('dashboard')">← Back to Dashboard</button>
  </div>

  <div class="section-title" style="border-bottom-color: var(--sap-success);">
    Level Upgrade Candidates — By Transition Type
    <span class="count-tag" style="background:var(--sap-success);">{len(level_upgrades)} objects</span>
  </div>
  <div class="card">
    <div class="notice" style="margin-bottom:1rem; background:#f0faf0; border-color:#a0d8a0;">
      <span class="notice-icon" style="color:var(--sap-success);">✓</span>
      <span>
        Select a transition type to see all objects of that type, across all packages.
        Expand "Show successor details" to see the Cloudification Repository information
        for each referenced SAP object.
        <strong>Important:</strong> always verify that the successor covers the same functional
        scope, especially for table write access where CDS successors are read-only.
        <br/><br/>
        <strong>Level B* transitions</strong> appear for object types that cannot use ABAP Cloud
        Language Version (e.g. PROG, SSFO, VIEW). For these, successor migration could eliminate
        all findings (score → 0) but the achievable clean core level is <strong>Level B</strong>,
        not Level A. See Methodology → Section 8 for the full list of object type constraints.
        <br/><br/>
        <strong>Why an object with a fixable P1 may still only reach Level C (not B):</strong>
        the Clean Core level follows <em>worst-finding</em> logic. Removing a P1 (Error) finding
        that has a successor drops an object out of Level D, but if it still has P2 (Warning)
        findings <em>without</em> a successor, those hold it at Level C. An object only reaches
        Level B when every P1 and P2 finding is resolved. See
        <strong>All Data → Successors by Object</strong> for the full per-object list of every
        successor and the level each migration would achieve.
      </span>
    </div>
    {upgrade_subtabs_html(level_upgrade_groups_html(level_upgrades))}
  </div>

</main>
</div>

<!-- ── ALL DATA PAGE ──────────────────────────────────────────────────── -->
<div id="page-alldata" class="tab-page" style="display:none;">
<main class="page">

  <div style="margin-bottom:1rem;">
    <button class="back-btn" onclick="goToTab('dashboard')">← Back to Dashboard</button>
  </div>

  <div class="notice">
    <span class="notice-icon">ℹ</span>
    <span>Full untruncated data for all {len(agg["objects"]):,} objects and {len(agg["packages"]):,} packages with in-scope findings.
    Use your browser's Ctrl+F to search within each table.</span>
  </div>

  <div class="section-title">All Packages — Full List
    <span class="count-tag">{len(agg["packages"]):,} packages</span>
    {alldata_pkg_control}
    <span class="rowcount-ctl">SAP Objects
      <select class="rowcount-select" data-table="tbl-alldata-pkg"
              onchange="applyRefCount(this.value, this.dataset.table)">
        {alldata_refpkg_options}
      </select>
    </span>
  </div>
  <div class="card">
    <div class="table-wrap">
      <table id="tbl-alldata-pkg">
        <thead>
          <tr>
            <th>#</th><th>Package</th><th class="num">Objects</th>
            <th class="num" style="color:var(--sap-error)">P1 ×10</th>
            <th class="num" style="color:var(--sap-warning)">P2 ×5</th>
            <th class="num" style="color:var(--sap-info)">P3 ×1</th>
            <th class="num">Score</th><th>Level</th>
            <th>Top Referenced SAP Objects (score within pkg)</th>
          </tr>
        </thead>
        <tbody>{pkg_rows(agg["packages"], chip_cap=max_pkg_refs, more_hint="")}</tbody>
      </table>
    </div>
  </div>

  <div class="section-title">All Objects — Full List
    <span class="count-tag">{len(agg["objects"]):,} objects</span>
    {alldata_obj_control}
  </div>
  <div class="card">
    <div class="table-wrap">
      <table id="tbl-alldata-obj">
        <thead>
          <tr>
            <th>#</th><th>Object</th><th>Type</th><th>Package</th>
            <th class="num" style="color:var(--sap-error)">P1</th>
            <th class="num" style="color:var(--sap-warning)">P2</th>
            <th class="num" style="color:var(--sap-info)">P3</th>
            <th class="num">Score</th>
            <th class="num">Potential</th>
            <th class="num">Reduction</th>
            <th class="num">Reduction %</th>
            <th>Level</th>
          </tr>
        </thead>
        <tbody>{obj_rows_full(agg["objects"])}</tbody>
      </table>
    </div>
  </div>

  <div class="section-title">All Referenced SAP Objects — Full List
    <span class="count-tag">{len(agg["ref_impact"]):,} objects</span>
    {alldata_ref_control}
  </div>
  <div class="card">
    <div class="table-wrap">
      <table id="tbl-alldata-ref">
        <thead>
          <tr>
            <th>#</th><th>Referenced SAP Object</th>
            <th class="num">Custom Objects</th>
            <th class="num">Impact Score</th>
            <th>Relative Impact</th>
          </tr>
        </thead>
        <tbody>{ref_rows(agg["ref_impact"])}</tbody>
      </table>
    </div>
  </div>

  <div class="section-title">Successors by Object — What Each Migration Would Move
    <span class="count-tag">{sum(len(v) for v in agg["obj_suc_detail"].values()):,} rows</span>
    {alldata_suc_control}
  </div>
  <div class="card">
    <div class="notice" style="margin-bottom:0.75rem;">
      <span class="notice-icon">ℹ</span>
      <span>
        One row per <strong>custom object × referenced SAP object that has a successor</strong>,
        sorted by the referenced SAP object so every caller of the same object groups together
        — useful when one API (e.g. a BAPI) is used across several packages. The
        <strong>Object Level</strong> column shows each object's current Clean Core level and the
        level it would reach if <em>all</em> its successor-available findings were migrated.
        A "no level change" note means that object keeps other findings (often P2s without a
        successor) that hold its level even after this migration — the level follows worst-finding
        logic. Use Ctrl+F or the search on the Dashboard tab to jump to a specific object.
      </span>
    </div>
    <div class="table-wrap">
      <table id="tbl-suc-by-obj">
        <thead>
          <tr>
            <th>#</th>
            <th>Referenced SAP Object</th>
            <th>Successor (per CR)</th>
            <th>CR State</th>
            <th>Prio</th>
            <th>Custom Object</th>
            <th>Type</th>
            <th>Package</th>
            <th>Object Level (current → potential)</th>
          </tr>
        </thead>
        <tbody>{successor_by_object_rows()}</tbody>
      </table>
    </div>
  </div>

</main>
</div>

{info_page_html(agg, cr_meta)}

<div class="footer">
  <span>Generated: {generated_on} · Source: {zip_name}</span>
  <span>In-scope checks: Usage of APIs · Critical Statements · Allowed Enhancement Technologies</span>
  <span>Cloudification Repository: {cr_date} ({cr_msg}) · bundled {cr_bundled}</span>
</div>

<script>
// ── Tab management ────────────────────────────────────────────────────────
var TABS = ['dashboard', 'pkg-upgrades', 'obj-upgrades', 'alldata', 'info'];

function showTab(tabName) {{
  TABS.forEach(function(t) {{
    var el = document.getElementById('page-' + t);
    if (el) el.style.display = (t === tabName) ? '' : 'none';
  }});
}}

function goToTab(tabName) {{
  showTab(tabName);
  // Update active state on native tab buttons
  document.querySelectorAll('.main-tab-btn').forEach(function(btn) {{
    var isActive = btn.dataset.tab === tabName;
    btn.classList.toggle('active', isActive);
  }});
}}

// Default: show only dashboard on load
document.addEventListener('DOMContentLoaded', function() {{
  showTab('dashboard');
  // apply the default (10 rows) to every dashboard list
  document.querySelectorAll('.rowcount-select[data-table]').forEach(function(sel) {{
    if (sel.getAttribute('onchange').indexOf('applyRefCount') !== -1) {{
      applyRefCount(sel.value, sel.dataset.table);
    }} else {{
      applyRowCount(sel.value, sel.dataset.table);
    }}
  }});
}});

// Show only the first N rows of a dashboard table, hide the rest.
function applyRowCount(n, tableId) {{
  n = parseInt(n, 10);
  var tbl = document.getElementById(tableId);
  if (!tbl) return;
  tbl.querySelectorAll('tbody tr[data-rowidx]').forEach(function(tr) {{
    var idx = parseInt(tr.dataset.rowidx, 10);
    tr.style.display = (idx <= n) ? '' : 'none';
  }});
}}

// Save the currently-VISIBLE rows of a table to a real Excel (.xlsx) file.
// Uses the SheetJS (XLSX) library loaded from CDN — needs internet at open time.
function _visibleCellText(cell) {{
  // Text of a cell, skipping any child elements hidden by a dropdown (display:none).
  var parts = [];
  cell.childNodes.forEach(function(node) {{
    if (node.nodeType === 3) {{                    // text node
      parts.push(node.textContent);
    }} else if (node.nodeType === 1) {{             // element
      if (node.offsetParent === null && node.style.display === 'none') return;
      parts.push(node.textContent);
    }}
  }});
  var txt = parts.join(' ').replace(/\\s+/g, ' ').trim();
  // Turn "1,234" style numbers back into real numbers for Excel.
  if (/^-?[\\d,]+(\\.\\d+)?%?$/.test(txt) && /\\d/.test(txt)) {{
    var num = parseFloat(txt.replace(/,/g, '').replace('%', ''));
    if (!isNaN(num) && txt.indexOf('%') === -1) return num;
  }}
  return txt;
}}

function exportTableToExcel(tableId, filename) {{
  var tbl = document.getElementById(tableId);
  if (!tbl) {{ alert('Table not found: ' + tableId); return; }}
  if (typeof XLSX === 'undefined') {{
    alert('The Excel library could not be loaded (no internet connection?). '
        + 'Please connect to the internet and reload the dashboard.');
    return;
  }}
  var aoa = [];
  // Header row.
  var head = [];
  tbl.querySelectorAll('thead th').forEach(function(th) {{
    head.push(th.textContent.replace(/\\s+/g, ' ').trim());
  }});
  aoa.push(head);
  // Only rows currently visible on screen (respects the Show-N dropdown).
  tbl.querySelectorAll('tbody tr').forEach(function(tr) {{
    if (tr.offsetParent === null || tr.style.display === 'none') return;
    var row = [];
    tr.querySelectorAll('td').forEach(function(td) {{ row.push(_visibleCellText(td)); }});
    if (row.length) aoa.push(row);
  }});

  var ws = XLSX.utils.aoa_to_sheet(aoa);
  var wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, 'Export');

  // Build the .xlsx bytes, then let the user choose where to save.
  var wbout = XLSX.write(wb, {{bookType: 'xlsx', type: 'array'}});
  var blob = new Blob([wbout], {{
    type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
  }});
  saveBlob(blob, filename);
}}

// Save a Blob with the native file picker (Save-As dialog) where supported,
// otherwise fall back to a normal download.
function saveBlob(blob, filename) {{
  if (window.showSaveFilePicker) {{
    window.showSaveFilePicker({{
      suggestedName: filename,
      types: [{{
        description: 'Excel workbook',
        accept: {{'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ['.xlsx']}}
      }}]
    }}).then(function(handle) {{
      return handle.createWritable().then(function(w) {{
        return w.write(blob).then(function() {{ return w.close(); }});
      }});
    }}).catch(function(err) {{
      if (err && err.name !== 'AbortError') downloadBlob(blob, filename);
    }});
  }} else {{
    downloadBlob(blob, filename);
  }}
}}

function downloadBlob(blob, filename) {{
  var url = URL.createObjectURL(blob);
  var a = document.createElement('a');
  a.href = url; a.download = filename;
  document.body.appendChild(a); a.click();
  document.body.removeChild(a);
  setTimeout(function() {{ URL.revokeObjectURL(url); }}, 1000);
}}

// Show only the first N reference chips per package row.
function applyRefCount(n, tableId) {{
  n = parseInt(n, 10);
  var tbl = document.getElementById(tableId);
  if (!tbl) return;
  tbl.setAttribute('data-refcount', n);
  tbl.querySelectorAll('tbody .ref-chip[data-refidx]').forEach(function(chip) {{
    var idx = parseInt(chip.dataset.refidx, 10);
    chip.style.display = (idx < n) ? '' : 'none';
  }});
}}

// Reslice the Package chart to the first N packages.
// (applyChartCount is defined alongside the chart itself, near the bottom.)

// Upgrade tab — By Transition Type: show first N rows of one sub-tab table.
function applyUpgradeRowCount(n, tableId) {{
  n = parseInt(n, 10);
  var tbl = document.getElementById(tableId);
  if (!tbl) return;
  tbl.querySelectorAll('tbody tr[data-rowidx]').forEach(function(tr) {{
    var idx = parseInt(tr.dataset.rowidx, 10);
    tr.style.display = (idx <= n) ? '' : 'none';
  }});
}}

// Upgrade tab — By Package: show first N package panels.
function applyUpgradePkgCount(n, _ignored) {{
  n = parseInt(n, 10);
  document.querySelectorAll('.upgrade-pkg-panel[data-pkgidx]').forEach(function(panel) {{
    var idx = parseInt(panel.dataset.pkgidx, 10);
    panel.style.display = (idx <= n) ? '' : 'none';
  }});
}}

// ── Referenced-object search (Tab 1) ──────────────────────────────────────
// Full index of every referenced SAP object, including those past the render cap.
var REF_INDEX = {ref_search_index};
var REF_RENDER_CAP = {DASH_MAX};

function _refSearchTable(tableId, q) {{
  // Reveal + highlight matching rows in one table; returns count of visible matches.
  var tbl = document.getElementById(tableId);
  if (!tbl) return 0;
  var hits = 0;
  tbl.querySelectorAll('tbody tr[data-rowidx]').forEach(function(tr) {{
    var cell = tr.querySelector('td.mono');
    var name = cell ? cell.textContent.trim().toUpperCase() : '';
    var match = q && name.indexOf(q) !== -1;
    if (!q) {{
      tr.classList.remove('ref-search-hit');
      // restore the Show-dropdown limit
      var sel = document.querySelector('.rowcount-select[data-table="' + tableId + '"]');
      var lim = sel ? parseInt(sel.value, 10) : 10;
      tr.style.display = (parseInt(tr.dataset.rowidx, 10) <= lim) ? '' : 'none';
    }} else if (match) {{
      tr.style.display = '';            // reveal even if past the Show cap
      tr.classList.add('ref-search-hit');
      hits++;
    }} else {{
      tr.style.display = 'none';
      tr.classList.remove('ref-search-hit');
    }}
  }});
  return hits;
}}

function applyRefSearch(raw) {{
  var q = (raw || '').trim().toUpperCase();
  var status = document.getElementById('refSearchStatus');
  if (!q) {{ clearRefSearch(); return; }}

  var visImpact = _refSearchTable('tbl-ref', q);
  var visSuc    = _refSearchTable('tbl-ref-suc', q);

  // Consult the full index for anything matching (covers rows past the render cap).
  var idxHits = REF_INDEX.filter(function(r) {{ return r.n.toUpperCase().indexOf(q) !== -1; }});
  idxHits.sort(function(a, b) {{ return a.rank - b.rank; }});

  if (idxHits.length === 0) {{
    status.innerHTML = 'No referenced SAP object matches “<b>' + raw + '</b>”.';
    return;
  }}
  var lines = [];
  lines.push('Found <b>' + idxHits.length + '</b> matching referenced object' + (idxHits.length > 1 ? 's' : '') + ':');
  idxHits.slice(0, 8).forEach(function(r) {{
    var where = r.suc ? ' — also in “with Successor” list' : '';
    var shown = (r.rank <= REF_RENDER_CAP) ? 'shown below (impact rank #' + r.rank + ')'
                                           : 'rank #' + r.rank + ' — beyond the on-page limit, see the <b>All Data</b> tab';
    lines.push('• <b>' + r.n + '</b> — impact ' + r.score.toLocaleString() + ', ' + shown + where);
  }});
  if (idxHits.length > 8) lines.push('…and ' + (idxHits.length - 8) + ' more.');
  if (visImpact + visSuc > 0) {{
    lines.push('<span style="color:var(--sap-success);">' + (visImpact + visSuc) + ' matching row(s) highlighted below.</span>');
  }}
  status.innerHTML = lines.join('<br/>');
}}

function clearRefSearch() {{
  var box = document.getElementById('refSearch');
  if (box) box.value = '';
  _refSearchTable('tbl-ref', '');
  _refSearchTable('tbl-ref-suc', '');
  var status = document.getElementById('refSearchStatus');
  if (status) status.innerHTML = '';
}}

function toggleDetail(id) {{
  var panel = document.getElementById(id);
  panel.classList.toggle('open');
  var btn = document.getElementById('btn-' + id);
  if (btn) {{
    btn.textContent = panel.classList.contains('open')
      ? btn.textContent.replace('Show', 'Hide')
      : btn.textContent.replace('Hide', 'Show');
  }}
}}
</script>

<script>
var _pkgChart = null;
var _pkgAll = {{
  labels: {pkg_labels},
  p1: {pkg_p1},
  p2: {pkg_p2},
  p3: {pkg_p3}
}};

function applyChartCount(n) {{
  n = parseInt(n, 10);
  if (!_pkgChart) return;
  _pkgChart.data.labels = _pkgAll.labels.slice(0, n);
  _pkgChart.data.datasets[0].data = _pkgAll.p1.slice(0, n);
  _pkgChart.data.datasets[1].data = _pkgAll.p2.slice(0, n);
  _pkgChart.data.datasets[2].data = _pkgAll.p3.slice(0, n);
  _pkgChart.update();
}}

(function() {{
  const N = 10;  // default number of packages shown
  const labels  = _pkgAll.labels.slice(0, N);
  const p1Data  = _pkgAll.p1.slice(0, N);
  const p2Data  = _pkgAll.p2.slice(0, N);
  const p3Data  = _pkgAll.p3.slice(0, N);

  const ctx = document.getElementById('pkgChart').getContext('2d');
  _pkgChart = new Chart(ctx, {{
    type: 'bar',
    data: {{
      labels: labels,
      datasets: [
        {{ label: 'P1 Error (×10)', data: p1Data, backgroundColor: '#bb0000', stack: 'stack' }},
        {{ label: 'P2 Warning (×5)', data: p2Data, backgroundColor: '#e76500', stack: 'stack' }},
        {{ label: 'P3 Info (×1)',    data: p3Data, backgroundColor: '#0070f2', stack: 'stack' }},
      ]
    }},
    options: {{
      responsive: true,
      maintainAspectRatio: false,
      plugins: {{
        legend: {{ position: 'top', labels: {{ font: {{ family: '"72", Arial, sans-serif', size: 12 }} }} }},
        tooltip: {{
          callbacks: {{
            footer: function(items) {{
              return 'Total score: ' + items.reduce((s, i) => s + i.raw, 0).toLocaleString();
            }}
          }}
        }}
      }},
      scales: {{
        x: {{ stacked: true, grid: {{ display: false }}, ticks: {{ font: {{ family: '"72", Arial, sans-serif', size: 11 }} }} }},
        y: {{
          stacked: true,
          ticks: {{ font: {{ family: '"72", Arial, sans-serif', size: 11 }}, callback: v => v.toLocaleString() }},
          title: {{ display: true, text: 'Technical Debt Score', font: {{ family: '"72", Arial, sans-serif', size: 12 }} }}
        }}
      }}
    }}
  }});
}})();
</script>
</body>
</html>"""

    return html


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate a Clean Core ATC assessment HTML dashboard from an ATC findings ZIP."
    )
    parser.add_argument("zip_path", help="Path to the ATC findings ZIP file.")
    parser.add_argument("--out", default="atc_dashboard.html",
                        help="Output HTML file path (default: atc_dashboard.html).")
    parser.add_argument("--top", type=int, default=10,
                        help="Reserved for future use (default: 10). The HTML dashboard lists "
                             "are fully rendered and controlled by in-page dropdowns.")
    args = parser.parse_args()

    zip_path = Path(args.zip_path)
    if not zip_path.exists():
        print(f"Error: file not found: {zip_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Parsing {zip_path.name}...")
    settings, findings, excluded = parse_zip(str(zip_path))
    print(f"  In-scope findings : {len(findings):,}")
    print(f"  Excluded findings : {excluded:,}")

    print("Loading Cloudification Repository data...")
    released_lookup, classic_lookup, cr_detail = load_cr_lookup()
    print(f"  Released objects  : {len(released_lookup):,}")
    print(f"  Classic API objects: {len(classic_lookup):,}")
    cr_meta = load_cr_metadata()

    print("Calculating scores...")
    agg = aggregate(findings, released_lookup, classic_lookup, cr_detail)
    print(f"  Total score       : {agg['total_score']:,}")
    print(f"  Potential score   : {agg['potential_score']:,}")
    print(f"  Objects           : {len(agg['objects']):,}")
    print(f"  Packages          : {len(agg['packages']):,}")

    print("Generating HTML dashboard...")
    html = generate_html(settings, agg, cr_meta, excluded, args.top, zip_path.name)
    out_path = Path(args.out)
    out_path.write_text(html, encoding="utf-8")
    print(f"  HTML written to: {out_path.resolve()}")

    print(f"\nDone.")


if __name__ == "__main__":
    main()
