# Object Types Considered by the RISE with SAP Methodology Dashboard — Extensibility KPI Calculation

**Source:** SAP Note 3761018, Version 3, Released 02.09.2026  
Component: SV-CLM-RMD-SYS (Service > SAP Cloud ALM > RISE Methodology Dashboards > RISE Methodology Dashboards System View)

Also informed by: SAP Community Blog — "SAP Cloud ALM's Clean Core Extensibility Assessment Is Getting More Precise!" (September 2026)  
URL: https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/sap-cloud-alm-s-clean-core-extensibility-assessment-is-getting-more/ba-p/14463584

---

## Overview

The RISE with SAP Methodology Dashboard measures extensibility KPIs by focusing specifically on **"focus object types"** — a curated subset of logic-bearing, code-based ABAP object types. This approach was harmonized and made effective from approximately **August 2026** onwards.

**Key consequence:** Clean Core Level assignments (A/B/C/D), Technical Debt Score, and Level counts in the dashboard are based exclusively on these focus object types. Objects outside this set (e.g. data elements, domains, tables) are scanned by underlying data collection tools but classified as **supporting objects** — displayed in the dashboard but excluded from KPI calculations.

> **Important:** If you compare dashboard numbers from before August 2026 with current values, the object counts and KPI scores may differ significantly. This is expected behavior caused by the harmonization, not a data issue.

---

## Focus Object Types (Clean Core Relevant)

The following 10 ABAP object types are the "focus object types" used for all extensibility KPI calculations:

| Object Type | Description |
|---|---|
| **BDEF** | Behavior Definition |
| **CLAS** | Class |
| **DDLS** | Data Definition Language Source |
| **FUNC** | Function Module |
| **FUGR** | Function Group |
| **FUGX** | Function Group with Customer Include (Customer Part) |
| **INTF** | Interface |
| **PROG** | Program |
| **ENHO** | Enhancement Implementation |
| **SXCI** | Business Add-Ins — Implementations |

These are code-based, logic-bearing types. Purely structural types like data elements (DTEL), domains (DOMA), tables (TABL), and table types (TTYP) are not in this set.

---

## Level A Objects

### Definition

Level A customer objects are identified as objects with one of the following **ABAP Language Versions**:

| Language Version | Description |
|---|---|
| **Language Version 5 (LV5)** | "ABAP for Cloud Development" — the primary ABAP Cloud target |
| **Language Version 2 (LV2)** | "ABAP for Key Users" — newly included as of August 2026 harmonization |
| **Language Version K (LVK)** | "Generated - ABAP for Key Users" — objects with Language Version "Standard ABAP" that were generated as part of Key User extensibility; newly included as of August 2026 harmonization |

LV2 and LVK were added to Level A in the harmonization. These objects are already compliant with the ABAP Cloud development model and represent the target state for clean core.

**General limitation for Level A:** Per-object information (such as individual object names) is not available at Level A in the dashboard.

### Data Source

Level A objects are determined using **SAP EarlyWatch Alert (EWA)** together with **Online Collectors (Custom Code Analytics / CCA)**.

### Supported Object Types by SAP Basis Release

Custom Code Analytics (CCA) supports the following object types for Level A identification, organized by the minimum SAP Basis release required:

**SAP Basis Release 753:**
- BDEF — Behavior Definition
- CLAS — Class
- DCLS — ABAP Data Control Language Sources
- DDLS — Data Definition Language Source
- DOMA — Domain
- DTEL — Data Element
- FUNC — Function Module
- FUGR — Function Group (including FUGS and FUGX for Function Groups with Customer Include)
- INTF — Interface
- PROG — Program
- TABL — Table
- TTYP — Table Type

**SAP Basis Release 754:**
- AUTH — Authorization Check Fields
- DEVC — Package

**SAP Basis Release 755:**
- DDLX — CDS Metadata Extension
- ENHO — Enhancement Implementation

**SAP Basis Release 757:**
- EVTB — Event Binding
- WAPA — BSP Application

**Note:** Some of these types (DOMA, DTEL, TABL, TTYP, etc.) are supported by CCA for Level A detection but are not "focus object types" — they appear in the dashboard but are not used for KPI calculations.

---

## Level B, C, and D Objects

### Definition

Levels B, C, and D include customer objects of the focus object types (listed above) with **Language Version "Classic ABAP"** that have findings from the following three ATC clean core checks:

1. **Allowed SAP Enhancement Technologies**
2. **Usage of APIs**
3. **Critical Statements**

Objects are classified based on the severity of ATC findings:

| Level | ATC Finding Severity |
|---|---|
| **Level B** | Info message (Priority 3) |
| **Level C** | Warning message (Priority 2) |
| **Level D** | Error message (Priority 1) |

**Note:** ABAP Classic customer objects that have no findings from any of the three ATC checks (for example, because they do not reference any SAP objects) technically belong to Level B.

### Function Module Change

**Function modules (FUNC) are now counted as separate main objects (object class R3TR)**, not as sub-objects (LIMU) of their function group (FUGR). This increases the visible object count in the dashboard but improves precision — each function module is now individually assessed and classified.

### Data Source

Level B, C, and D objects are identified using the **ABAP Test Cockpit (ATC)**. ATC check results must be manually imported into the RISE with SAP Methodology Dashboard.

Level B/C/D objects include additional per-object information such as object names and package assignments.

**Critical alignment requirement:** ATC must be configured to analyze the same packages and namespaces as those analyzed by Custom Code Analytics (i.e., namespaces set to "producer"). Otherwise, Level A and Level B/C/D results will not be comparable.

### Current Limitations for Level B/C/D

- Customer objects of types beyond those supported by the ATC checks are not included
- Objects with syntax errors are excluded (ATC cannot analyze objects with syntax errors)
- If ATC is not configured to analyze all packages in customer namespaces (Z\*, Y\*, /MYNAMESPACE/), those packages will not receive Level B/C/D analysis

---

## General Namespace Limitation

Objects in customer namespaces (Z\*, Y\*, /MYNAMESPACE/) that are **not set to role "producer"** in the analyzed system might not be detected, counted, or classified correctly. This applies to both Level A (CCA) and Level B/C/D (ATC) identification.

---

## ATC Configurations NOT Reflected in the Dashboard

The following ATC configurations are ignored when the dashboard calculates KPIs and levels:

| ATC Configuration | What it means | Dashboard behavior |
|---|---|---|
| **ATC Baseline** | Excludes well-known findings from the result list | Baselined findings are still counted in the dashboard |
| **ATC Exemptions** | Marks findings as false positives or currently unresolvable | Exempted findings are still counted in the dashboard |
| **Customer-specific priority changes** | Changes to the default priority of findings | Original priorities are used; customer changes are ignored |

**Implication:** The dashboard always shows the "raw" state of technical debt, independent of any customer decisions to defer or exempt findings.

---

## Objects That May Be Incorrectly Included

In certain configurations, objects may be incorrectly included in clean core KPIs:

1. **Partner namespace objects:** If ATC is configured to analyze packages in namespaces outside of customer namespaces (e.g. partner namespaces), objects from those packages will be incorrectly included in clean core KPIs.

2. **Key User extensibility objects misclassified as Level B/C/D:** If **SAP Note 3593439** ("Exclude Key User Items from ATC Check") and its dependent notes have not been implemented before running ATC, customer objects with Language Version "Classic ABAP" that were generated as part of Key User extensibility may be incorrectly classified as Level B/C/D objects (instead of being recognized as Level A).

> **Action required:** Implement SAP Note 3593439 (and its dependencies, as outlined based on software release) before running the ATC clean core checks. This prevents Key User extensibility objects from appearing in Level B/C/D.

---

## Understanding Discrepancies with Other Tools

When comparing object counts from the RISE with SAP Methodology Dashboard with numbers from other tools (such as the ATC results view or iCCM), discrepancies are expected and explained by the following factors:

| Factor | Explanation |
|---|---|
| **ATC analyzes more object types** | ATC may show a higher total number of analyzed objects because non-clean-core checks may also be active, and those checks often consider additional types (e.g. DDIC elements such as data elements, domains, tables, and table types) |
| **Clean core checks focus on code-based objects** | Clean core checks intentionally examine only code-based objects (FUGR, FUNC, CLAS, PROG, etc.). A single program may have dozens of associated DDIC objects that other ATC checks analyze — those are excluded from the clean core KPI calculation |
| **iCCM has a different scope and purpose** | iCCM (Intelligent Custom Code Management) does not solely focus on clean core compliance. It aims to provide full transparency on all objects in customer namespaces, without excluding any ABAP object types. It clusters customer objects to provide recommendations on decommissioning or redesign, and therefore considers more object types than the RISE Dashboard. Additionally, iCCM is a **service offering** (included in SAP's Max Success Plan), not a standalone tool |

---

## Impact on KPI Values

Due to the Object Type Harmonization effective August 2026:

- **Technical Debt Score** values may differ significantly from pre-August 2026 values
- **Clean Core Share** percentages (Level A/B/C/D distribution) may shift
- **Level A/B/C/D object counts** will change — for example, function modules now count as individual R3TR objects (previously sub-objects of FUGR), and LV2/LVK objects move into Level A
- These changes reflect a more precise measurement, not a deterioration of clean core status

When presenting dashboard results to customers or stakeholders, acknowledge that numbers may have changed since August 2026 and explain the harmonization context.
