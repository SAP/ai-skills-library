---
name: clean-core-extensibility-atc-assessment
description: >
  Generates a Clean Core ATC Assessment Dashboard from an SAP ATC findings ZIP export.
  Produces a self-contained HTML report in SAP Horizon look & feel covering:
  Technical Debt Score, Potential Score (successor-aware), Clean Core Level Distribution
  (Level B/C/D per object using worst-finding logic), top objects and packages by debt score,
  top objects by Level D (P1 error) findings, top referenced SAP objects by impact,
  and per-package top-3 referenced SAP objects.

  Use this skill whenever the user provides or mentions an ATC findings ZIP file,
  wants to analyse their clean core technical debt, asks for a clean core dashboard,
  wants to understand their Level D / Level C distribution, or asks about technical
  debt score, potential score, or successor-available findings.
allowed-tools: [Bash, Read, Write]
---

## What this skill does

Parses an SAP ATC findings ZIP export (typically named `atc_findings_*.zip`) and generates
a self-contained **HTML dashboard** the user can open in a browser or share.

---

## How to invoke

The user typically says something like:
- "Analyse this ATC export: `path/to/atc_findings_BC1.zip`"
- "Generate a clean core dashboard from my ATC results"
- "What's our technical debt score?" (then ask for the ZIP if not provided)

---

## Workflow

### Step 1 — Locate the ZIP file

If the user has given a path, use it directly. If not, ask:
> "Please provide the path to your ATC findings ZIP file (e.g. `sources/atc_findings.zip`)."

Resolve the path relative to the current working directory or the skill directory.

### Step 2 — Generate the dashboard

From the skill directory (`skills/clean-core-atc-assessment/`), run:

```bash
python3 scripts/generate_dashboard.py <path-to-zip> --out <output-path.html>
```

- `--out` defaults to `atc_dashboard.html`. Suggest a descriptive name based on the
  run title or system (e.g. `atc_dashboard_BC1_CW16.html`).
- `--top` is accepted but has no effect on the HTML output (lists are dropdown-driven).


### Step 3 — Deliver the result

Tell the user:
- Where the HTML file was saved
- Key headline numbers (total score, potential score, number of objects/packages)
- Any notable observations (e.g. one package dominates the score, high % of successor findings)

Offer to open the file or copy the path for them to open in a browser.

---

## Output file

The HTML dashboard is fully self-contained except for Chart.js and SheetJS (loaded from
CDN for the bar chart and Excel export). For a fully offline file, replace the CDN
`<script>` tags with local copies — or simply view it while connected.

The file has five tabs:
1. **Dashboard** — all KPIs, charts, and tables; package and object upgrade summary with clickable rows
2. **Pkg Upgrades** — upgrade-candidate objects per package (only objects that can improve a level)
3. **Obj Upgrades** — upgrade-candidate objects by transition type (D→A, D→C, D→B, C→A, C→B, B→A)
4. **All Data** — full untruncated object, package, and referenced SAP object tables
5. **Methodology & Help** — explains every calculation with real examples from the data

All dashboard lists are dropdown-driven (adjustable row counts) and the caps auto-scale
to the export size so large customers never lose data. Every table with a dropdown also has
a **⬇ Excel** button that exports the visible rows as a real `.xlsx` file. See
`references/DASHBOARD-ENHANCEMENTS.md` for the full list of dashboard enhancements.

---

## Calculation rules (summary — full detail in the help tab)

| KPI | Rule |
|---|---|
| **In-scope checks** | `CL_YCM_CC_CHECK_API_USAGE`, `CL_CI_TEST_CRITICAL_STATEMENTS`, `CL_CI_TEST_ADMISSIBLE_ENHANCM` |
| **Technical Debt Score** | P1 × 10 + P2 × 5 + P3 × 1 (per object; summed for packages/total) |
| **DPRCTD_SUC excluded from score** | Findings with message code `DPRCTD_SUC` (deprecated with successor) are **not** counted in P1/P2/P3 — they feed only the Potential Score. All other `_SUC` codes (`SELECT_SUC`, `TC_CLA_SUC`, etc.) are counted normally. Matches RISE Dashboard logic. |
| **Clean Core Level (object)** | Worst finding: P1 → Level D, P2 → Level C, P3 → Level B |
| **Objects without findings** | Not in export; labelled "not assessed here" — not Level A |
| **Potential Score** | Score minus reduction from `_SUC` findings (including `DPRCTD_SUC`): Released successor → 0 pts; Classic API or unknown → 1 pt |
| **FUGR/FUNC counting** | Findings on a function module sub-object (`sub_type=FUNC`) are counted under the individual function module (`sub_name`), not the function group. Other FUGR sub-objects (INCL, etc.) stay under the function group. Matches RISE Dashboard logic. |
| **Composite object key** | Objects are identified by `(obj_name, obj_type)` — same name with different types are counted as distinct objects. Matches RISE Dashboard logic. |
| **Referenced SAP object impact** | Sum of weighted finding points across all custom objects referencing it |

---

## Cloudification Repository data (for potential score)

The successor classification lookup uses bundled JSON files in `scripts/data/`:
- `objectReleaseInfo_PCELatest.json` — released SAP objects
- `objectClassifications_SAP.json` — classic API / noAPI objects
- `cr_metadata.json` — version record with commit SHA and date

To check for updates (requires internet access, run from laptop):
```bash
python3 scripts/update_cr_data.py --check
```

To download updates:
```bash
python3 scripts/update_cr_data.py
```

See `references/HOW-TO-UPDATE-CR-DATA.md` for the full guide.

---

## Notes

- All score and level values reflect only objects with at least one in-scope ATC finding.
  Make clear to the user that this is a partial view of the landscape — objects without
  findings could be Level A but are not confirmed here.
- Out-of-scope findings (`CL_CI_TEST_PROGRAM`, `CL_CI_TEST_CUST_MODIFICATIONS`) are counted
  but excluded from calculations; the dashboard shows the excluded count in the run bar.
