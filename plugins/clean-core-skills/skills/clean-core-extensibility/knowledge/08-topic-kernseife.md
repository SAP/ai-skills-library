# Project Kernseife — Custom ATC Check for Clean Core Measurement

> Synthesized from SAP Community blog posts and the official GitHub repository (https://github.com/SAP/project-kernseife).
> See `sources/kernseife-blogs.md` for source registry and refresh instructions.
> Last sync: 2026-05-28 | Current version: 1.5.x

---

## Sources

When citing content from this file, link to the relevant source below:

| Topic | Source | URL |
|-------|--------|-----|
| What Kernseife is, motivation, custom classification concept, Kernseife Score | Project Kernseife – Improving the Measurement of Clean Core in ABAP | https://community.sap.com/t5/technology-blog-posts-by-sap/project-kernseife-improving-the-measurement-of-clean-core-in-abap/ba-p/14099819 |
| When to use Kernseife vs. standard approach, 4 advantages, decision guide | Taking Control of Clean Core: When to Use Project Kernseife | https://community.sap.com/t5/technology-blog-posts-by-sap/taking-control-of-clean-core-when-to-use-project-kernseife-in-addition-to/ba-p/14258229 |
| Project overview, links to all guides | GitHub Repository – Project Kernseife | https://github.com/SAP/project-kernseife |
| Full rating code table (all codes, scores, levels, examples) | Wiki – Ratings & Classification | https://github.com/SAP/project-kernseife/wiki/Ratings-&-Classification |
| ABAP installation steps (abapGit, SCI, check variant, classification upload) | Wiki – ABAP Installation Guide | https://github.com/SAP/project-kernseife/wiki/ABAP-Installation-Guide |
| Scoring mode, level concept, BTP app integration, missing classifications | Wiki – Scoring & Development Object Guide | https://github.com/SAP/project-kernseife/wiki/Scoring-&-Development-Object-Guide |
| Classification lifecycle: initial setup, export, import, BTP connector sync | Wiki – Classification Setup and Management Guide | https://github.com/SAP/project-kernseife/wiki/Classification-Setup-and-Management-Guide |
| Differences vs. standard check, checked object types, known issues | Wiki – FAQ | https://github.com/SAP/project-kernseife/wiki/FAQ |
| BTP App installation prerequisites | Wiki – BTP Installation Guide | https://github.com/SAP/project-kernseife/wiki/BTP-Installation-Guide |
| Latest releases and version history | GitHub Releases | https://github.com/SAP/project-kernseife/releases |

---

## What is Project Kernseife?

Project Kernseife is an **open-source custom ABAP Test Cockpit (ATC) check** that extends the standard "Usage of APIs" check (SAP Note 3565942) with a **custom, adjustable classification system**. It allows organizations to define their own rating for SAP objects — overriding or supplementing SAP's official classification — to produce more accurate and actionable clean core measurements.

It consists of two components:

1. **Custom ATC Check (`ZKNSF_CL_API_USAGE`)** — installed in your ABAP system, checks custom code against a custom classification JSON file
2. **BTP CAP Application** — manages the classification, analyzes results, and provides dashboards (scoring, development objects, findings)

Repository: https://github.com/SAP/project-kernseife  
License: Apache 2.0 (open source)

> **Important:** Kernseife is not an official SAP product. It is an open-source project with active development, but **no product roadmap**. It is used in production projects but requires the adopting team to own, maintain, and update the custom classification.

---

## Why Kernseife Exists — The Problem It Solves

The standard ATC "Usage of APIs" check (from SAP Note 3565942) classifies SAP objects as released, classic API, internal, or no-API based on SAP's official Cloudification Repository. This works well for a general view but has two gaps in practice:

**1. SAP cannot classify everything perfectly for every project.**
Some SAP objects are not officially classified (reported as "internal object" = Level C warning) even when their use is well-established or explicitly documented for a given scenario (e.g., `/SCWM/CL_RF*` for EWM RF framework, `/SCWM/IF_API_WHR_OUTBOUND` for EWM Outbound Delivery). Without Kernseife, developers must individually request exemptions for every such finding — flooding approvers with "false positives" and creating autopilot approval behavior.

**2. Standard checks have a fixed scoring model.**
The technical debt score from the standard check maps directly to ATC priority (P1/P2/P3), which may not reflect your organization's actual risk profile. Kernseife introduces a configurable numeric score (0–10) per classification code, enabling custom technical debt calculations per object, package, or system.

---

## When to Use Kernseife vs. the Standard Approach

### Standard approach (RISE with SAP Methodology Dashboard) is better when:
- Primary goal is alignment with SAP's out-of-the-box reporting (RISE dashboard comparability)
- No capacity to own and maintain custom classification rules
- Comparability across systems matters more than precision (same classification baseline for all)
- Simple, low-effort clean core overview is sufficient

### Kernseife is the right choice when:
- The standard check produces too many "false positive" findings for your specific project scope (e.g., EWM, IS-specific frameworks)
- Exemption approvers are overwhelmed and governance quality is suffering
- You need a **custom technical debt score** with configurable weights per object type
- You want to define and enforce **custom successors** for objects (including custom wrappers)
- You need **prioritized cleanup guidance** (Score vs. Potential Score gap analysis)
- You want detailed dashboards **before** SAP's official Extensibility Deep Dive dashboard is generally available

### Both can co-exist:
Kernseife is a supplement, not a replacement. Organizations can run both: the standard check for RISE dashboard uploads and Kernseife for internal governance and detailed scoring.

---

## The Custom Classification System

### What a Classification Does

Each entry in the classification JSON maps an SAP object (or wildcard pattern) to a **rating code**. The rating code determines:
- **ATC finding severity** (Success / Info / Warning / Error)
- **Kernseife Score** (0–10 numeric debt score)
- **Clean Core Level** (A / B / C / D)

### Rating Codes Reference

| Code | Title | Criticality | Score | Level | Description | Example |
|------|--------|------------|-------|-------|-------------|---------|
| BF0 | Business Function - Released | S (Success) | 0 | A | Released SAP API | Released CDS views like I_Product |
| FW0 | Framework - Released | S | 0 | A | Released technical framework object | CL_ABAP_FORMAT |
| EF0 | Enhancement Framework - Released | S | 0 | A | Released enhancement framework object | — |
| BF1 | Business Function - Recommended | I (Info) | 1 | B | Classic API nominated in Cloudification Repository | BAPI_PO_CREATE1 |
| FW1 | Framework - Recommended | I | 1 | B | Classic API technical framework (e.g. ALV) | CL_SALV* |
| EF1 | Enhancement Framework - Recommended | I | 1 | B | Enhancement framework classic API | — |
| MSG | Message Class | I | 1 | B | Message classes used to share SAP messages | Any MSAG object |
| DDS | DDIC - Simple | I | 1 | B | Simple DDIC (data elements, domains) | DTEL SYUCOMM |
| DDA | DDIC - Avoid | I | 2 | B | DDIC objects with successor | — |
| BF3 | Business Function - Utility | I | 3 | B | Not released but considered good practice (BADI example impls, exemption classes) | /SCWM/CX_RESOURCE_MGMT |
| FW3 | Framework - Utility | I | 3 | B | Technical framework utility objects | /BOPF/CX_FRW |
| EF3 | Enhancement Framework - Utility | I | 3 | B | Enhancement framework utility | — |
| DDC | DDIC - Complex | I | 3 | B/C | Table types, structures with some dependency risk | SFPDOCPARAMS |
| BF5 | Business Function - Internal | W (Warning) | 5 | C | Unreleased SAP business object — not recommended but distinguishable from no-API | CL_MM_PUR_CNTRL_CTR_MA_MPC |
| FW5 | Framework - Internal | W | 5 | C | Unreleased technical framework | CL_WDY_MD_VIEW_ELEMENT_DEF |
| EF5 | Enhancement Framework - Internal | W | 5 | C | Unreleased enhancement framework | — |
| TBLSEL | Reading SAP DB table/view | W | 5 | C | SELECT from SAP table | SELECT * FROM MARA |
| TBLTYP | Table as type definition | I | 1 | B | `DATA ls TYPE mara.` usage | — |
| TBLCDS | SAP table in CDS view | W | 5 | C | CDS view referencing SAP DB table | — |
| BF9 | Business Function - Avoid | E (Error) | 9 | D | noAPI in Cloudification Repository | BAPI_BUPA_ROLE_ADD |
| FW9 | Framework - Avoid | E | 9 | D | Technical framework marked as noAPI | SX_INTERNET_ADDRESS_TO_NORMAL |
| EF9 | Enhancement Framework - Avoid | E | 10 | D | Enhancement framework to avoid | — |
| TBL | Database Table (write) | E | 10 | D | UPDATE/INSERT/DELETE on SAP table | UPDATE MARA |
| TBLUPD | Updating SAP DB table/view | E | 10 | D | Write access to SAP table/view | — |
| MIG | Migration required | E | 0 | D | Object requires migration | — |
| NOC | Missing Classification | E | 0 | C | Object not yet in classification — requires attention | — |
| ENH | BADI | I | 0 | B | BADI usage not released for ABAP Cloud — considered upgrade stable | — |

`_SUC` variants (e.g. `BF1_SUC`) exist for all codes where a successor is defined — same score and level but includes a successor hint in the finding. These are system-generated and not usable in manual classification entries.

### Key Difference: NOC (Missing Classification)
Unlike the standard check (which reports unclassified objects as "internal API" = warning), Kernseife reports them as `NOC` = **Error (Priority 1)**. This forces teams to consciously classify every SAP object used in custom code. It requires more upfront effort but results in complete visibility.

### Custom Classification Use Cases

**Make stricter:** Classify a direct SELECT on MARA as `TBL` (Error, score 10) instead of the default `TBLSEL` (Warning, score 5) to push developers toward the CDS view `I_Product`.

**Make more permissive:** Classify `/SCWM/CL_RF*` as `FW1` (Info, score 1, Level B) because EWM RF framework usage is accepted project-wide — eliminating mass exemption requests.

**Define custom successors:** Add a custom wrapper `Z_WRAPPER_ABC` as the successor for an SAP function module — developers are guided to use the central wrapper rather than re-implementing it.

**Partner APIs:** Classification can include objects from SAP partner namespaces.

---

## Score and Potential Score

Kernseife introduces two key metrics per custom code object:

| Metric | Definition |
|--------|-----------|
| **Score** | Current technical debt score of the object (sum of finding scores based on current classification) |
| **Potential Score** | Score the object would have if all findings with defined successors were refactored to use the successor |

The **gap between Score and Potential Score** identifies cleanup priority:
- Large gap (e.g., Score 10, Potential 0) = high-impact refactoring opportunity ("low-hanging fruit")
- Small gap (e.g., Score 2, Potential 2) = no successor defined or successor is also non-ideal = lower priority

This allows data-driven prioritization of cleanup efforts beyond simple level counts.

---

## ABAP Installation Guide

### Prerequisites

| Requirement | Details |
|-------------|---------|
| SAP S/4HANA 2023 or higher | ATC with clean core check support required |
| SAP Note 3565942 | **Mandatory** — base clean core ATC check |
| SAP Note 3630552 | **Mandatory** — partner classic API support (also needed for Kernseife upload report) |
| SAP Note 3710789 | **Mandatory** — required due to breaking changes |
| SAP Note 3627152 | Recommended — identifies all clean core related notes for your system |
| Authorizations | Standard role `SAP_SATC_QE` + authorization object `SYCM_API` |
| abapGit | Required for import (transaction `ZABAPGIT` or report `ZABAPGIT_STANDALONE`) |
| Transport request | Workbench transport needed for check activation; the code itself can be in a local `$` package |

**Note:** Kernseife cannot be used in ABAP Cloud (BTP ABAP environment) — it requires a classic ABAP system.

### Installation Steps

**Step 1 — Import via abapGit:**
1. Run transaction `ZABAPGIT` or report `ZABAPGIT_STANDALONE`
2. Click *New Offline* → enter name `KERNSEIFE` → create package `$KERNSEIFE` → *Create Offline Repository*
3. Click *Import zip* → upload `import.zip` from the [latest release](https://github.com/SAP/project-kernseife/releases/latest)
4. Press *Pull* → confirm objects → activate (local package = no transport needed)

**Step 2 — Enable checks in Code Inspector (SCI):**
1. Transaction `SCI` → Utilities → *Import Check Variants*
2. Confirm successful import: Code Inspector → Management of → Checks
3. Select category `ZKNSF_CL_CI_CATEGORY` → Save
4. Select check `ZKNSF_CL_API_USAGE` → Save (requires workbench transport, can be deleted after)

**Step 3 — Upload classification JSON:**
1. Execute report `ZKNSF_CLASSIFICATION_MANAGR`
2. Click *Upload Classic API File* → select your classification JSON

Starting point: use the [default classification](https://raw.githubusercontent.com/SAP/project-kernseife/refs/heads/main/defaultClassification_System.json) — based on the Cloudification Repository as of 2025-05-21. This is a starting point, not a finished classification.

**Step 4 — Create ATC check variant:**
1. Transaction `SCI` → create new check variant
2. Recommended base: copy `ABAP_CLOUD_DEVELOPMENT_3TIER`
   - Disable: *Usage of Released APIs* check
   - Enable: *Check for Enhancement Technology*
3. **Mandatory in all cases:** enable *Kernseife: Usage of APIs* check
4. Make the variant public (not personal)

---

## Scoring Mode and BTP App Integration

For level calculation (Level A/B/C/D per object), Kernseife needs the ABAP language version — create a **separate check variant for scoring** (proposed name: `ZKNSF_SCORING`) with:
- Only the Kernseife check enabled
- **Track Language Version** option activated

After running the ATC check:
1. Export results using CDS view `ZKNSF_I_EXPORT` via SE16N (filter by Run ID)
2. In the Kernseife BTP Jobs App: Import via *Findings Import (CSV)*

Alternatively, call function module `ZKNSF_CREATE_PROJECT` in SE37 to auto-create a Custom Code Migration App project and trigger a full ATC run (note: triggers full system ATC run).

### BTP Application Components

| App tile | Purpose |
|----------|---------|
| Manage Classifications | View and edit the classification — adjust rating codes per object |
| Analyze Overview | High-level scoring overview per system |
| Analyze Score | Detailed score drill-down per package / object |
| Manage Development Objects | Browse custom code objects with scoring |
| Manage Extensions | Manage extension-level information |
| Configure Settings | System connections, BTP connector setup |
| Monitor Jobs | Track import/export jobs |

**Key CDS views for direct data access (without BTP app):**

| View | Purpose |
|------|---------|
| `ZKNSF_I_SCORING` | Combines ATC findings with Kernseife score — use for custom dashboards (e.g., SAP Analytics Cloud) |
| `ZKNSF_I_DEVELOPMENT_OBJECTS` | Aggregated list by object |
| `ZKNSF_I_MISSING` | Objects not yet in classification — starting point for classification work |

---

## Classification Lifecycle

### Initial Setup
1. Download [default classification JSON](https://raw.githubusercontent.com/SAP/project-kernseife/refs/heads/main/defaultClassification_System.json)
2. Run report `ZKNSF_CLASSIFICATION_MANAGR` → *Upload API File* → confirm overwrite → select file
3. Run full system ATC check → review `NOC` (Missing Classification) findings

### Handling Missing Classifications (NOC)
NOC findings appear for SAP objects used in custom code that are not yet in the classification. Process:
1. Export unclassified objects: SE16N → table `ZKNSF_I_MISSING` → Export as CSV
   - Required columns: `objectType`, `objectName`, `applicationComponent`, `subType`, `softwareComponent`, `tadirObjectType`, `tadirObjectName`
2. Import to BTP app: Jobs App → Import → *Missing Classification Import* (leave Default Rating empty to apply default logic)
3. Review and adjust ratings in BTP Manage Classifications app
4. Export updated classification: Jobs App → Export → *Classification (System Upload Format)* → download ZIP
5. Upload to ABAP system: `ZKNSF_CLASSIFICATION_MANAGR` → *Upload API File* → select ZIP
6. Rerun ATC check

For Kernseife BTP version ≥ 1.4.x: export via Jobs App (not the Manage Classifications app).

**Alternative — BTP Connector sync:** Settings App → select system → *Sync Classification* (pushes updated classification directly without manual file transfer).

> Note: updating the classification does **not** retroactively change previous ATC run results — a new ATC run is needed.

---

## Differences vs. Standard "Usage of APIs" Check

| Aspect | Standard Check (Note 3565942) | Kernseife |
|--------|------------------------------|-----------|
| Classification source | SAP Cloudification Repository only | SAP repo + custom overrides |
| Unclassified objects | Reported as "internal API" (Warning) | Reported as `NOC` — Error (configurable) |
| Scoring | Fixed to ATC priority (P1/P2/P3) | Custom numeric score 0–10 per rating code |
| Checked object types | ~8 types (INTF, CLAS, FUNC, DDLS, TABL, VIEW, PROG, BDEF) | ~28 types — adds TRAN, AUTH, SUSO, MSAG, ACID, DTEL, DOMA, TTYP, ENHS, ENHO, SXSD, and more |
| DDIC type references | Not tracked | Tracked (`TBLTYP`) |
| Released object tracking | Not tracked in results | Tracked in Scoring Mode (for full picture) |
| Key-user objects | System dependent | Filtered out (local ATC only) |
| RISE dashboard upload | Yes (official) | No (custom data — use `ZKNSF_I_SCORING` for custom dashboards) |
| BTP ABAP environment | Yes | No — classic ABAP only |
| Maintenance | SAP-maintained | Community/open-source — self-maintained |

---

## Known Issues

| Issue | Resolution |
|-------|-----------|
| Dump: *Function module "RS_ABAP_GET_INTFS_INCL_INFT_E" not found* | Run report `RS_ABAP_SETUP_ANALYSIS` (manual step from SAP Note 3373034) |
| Dump: *LOAD_PROGRAM_CLASS_MISMATCH* after running RS_ABAP_SETUP_ANALYSIS | Run report `RSGENDUMP` for affected users; check SAP Note 2296826 |
| "A PROCESS statement is missing" during abapGit import | Update abapGit to latest version |
| ITAB_DUPLICATE_KEYS dumps | See GitHub Issue #19 |
| Cannot select/delete uploaded classification in ALV | Fixed in Kernseife 1.3.0+ |
| Cannot navigate to finding object (no navigation info) | Apply SAP Note 3623342 or use ADT instead of SAP GUI |
| Exemptions not working for Kernseife findings (sometimes) | See GitHub Issue #60 |

---

## BTP App — Installation Prerequisites

For teams wanting the full Kernseife experience with the CAP application:

| Resource | Requirement |
|----------|------------|
| BTP subaccount | Cloud Foundry enabled |
| Application runtime | Min. 2 GB |
| HANA Cloud | Instance for HDI container |
| SAP Build Work Zone | Standard edition subscription |
| Services needed | hana (hdi-shared), xsuaa (application), html5-apps-repo (app-host), destination (lite), autoscaler (standard), cloud-logging (dev/standard) |

Post-deployment: assign user to role `kernseife-admin-${space}`.

> The BTP app is a CAP/TypeScript application built and deployed via MBT build + CF deployment. A GitHub Actions workflow is provided for automated CI/CD. Detailed deployment steps are in the [BTP Installation Guide](https://github.com/SAP/project-kernseife/wiki/BTP-Installation-Guide).
