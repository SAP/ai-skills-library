# RISE with SAP Methodology Dashboard — Full Reference

**Source:** SAP Help Portal — "SAP Cloud ALM and RISE with SAP Methodology" tree (exported 2026-09-13)  
**Ingested:** 2026-09-14  
**Purpose:** Comprehensive reference for the RISE with SAP Methodology Dashboard hosted in SAP Cloud ALM, which is the primary tool for measuring KPI compliance across all five clean core principles.

---

## Overview

The **RISE with SAP Methodology Dashboard** is available in the SAP Cloud ALM launchpad. It is the central tool for measuring a customer's SAP S/4HANA system's compliance with the five clean core principles (Extensibility, Data, Integration, Operations, and Business Processes).

**Access requirements:**
- Valid RISE with SAP contract
- SAP Cloud ALM tenant
- Supported systems: **SAP S/4HANA** and **SAP S/4HANA Cloud Private Edition** (production, test, and development)
- SAP S/4HANA Foundation systems are NOT supported
- Demo systems are NOT supported

**Key principle:** The dashboard is not a real-time monitoring tool — it provides periodic reports on clean core progress.

---

## Dashboard Views

The dashboard has two primary views:

| View | Purpose | Data Frequency |
|---|---|---|
| **System View** | Measures software stack, extensibility, data, and integration KPIs | Once per week (up to 1.5 weeks for initial data) |
| **Operations View** | Measures security, system health, and operations setup | Daily (initial data within 24 hours) |

Three drill-down views:
- **Customer Objects** deep dive (extensibility detail)
- **Business Modifications** deep dive (extensibility detail)
- **Data Volume Efficiency** deep dive (data detail)

---

## Setup and Configuration

The dashboard uses a **three-phase setup**:

| Phase | Description |
|---|---|
| **Phase 1** | Connect systems to SAP Cloud ALM (Landscape Management) |
| **Phase 2** | Activate data collection tools for each principle |
| **Phase 3** | Import ATC check results for extensibility KPIs (manual step) |

### Data Collection Tools by Principle

| Principle | Required Tool(s) |
|---|---|
| **Extensibility** | ABAP Test Cockpit (ATC) — manual import; ABAP Call Monitor (SAP Note 2679723); Aggregated Usage Data / SUSG transaction (SAP Note 2701371) |
| **Data** | ST-PI 7.40 SP31+ add-on + SAP Note 3703380; batch user with roles `SAP_SDF_ALM_METRIC_PUSH_FND` and `SAP_SDF_ALM_METRIC_PUSH_DVM` |
| **Integration** | SAP Readiness Check (SAP Note 3690029) — manual trigger via "New Analysis" button |
| **Operations** | ST-PI 7.40 SP28+; SAP Cloud ALM integration; Health Monitoring and Integration & Exception Monitoring apps configured |

---

## System View — Software Stack

The Software Stack section shows the currency of the customer's SAP software stack.

**Status values:**
| Status | Meaning |
|---|---|
| **Current Release** | On the latest available release |
| **Upgrade Recommended** | Behind the latest release but within support |
| **Upgrade Overdue** | Behind threshold, action required |
| **Out of Maintenance** | No longer receiving updates |

**Currency designations:**
| Designation | Condition |
|---|---|
| **Innovation-Ready** | On initial shipment or FPS; stack < 24 months old |
| **Security-Compliant** | Any stack released < 24 months ago |

---

## System View — Extensibility KPIs

The Extensibility section measures the customer's compliance with the Clean Core Level Concept using data from the ABAP Test Cockpit.

**Focus Object Types (Object Type Harmonization, August 2026):** KPI calculations use only 10 logic-bearing ABAP object types (BDEF, CLAS, DDLS, FUNC, FUGR, FUGX, INTF, PROG, ENHO, SXCI). Other types are shown as supporting objects but excluded from KPI scores and level counts. This means object counts and KPI values may differ significantly from values displayed before August 2026.

**ATC Level mapping in the dashboard:**

| ATC Priority | Dashboard Level | Type |
|---|---|---|
| No finding / info message (Priority 3) | Level A / Level B | Best practice |
| Warning (Priority 2) | Level C | Needs attention |
| Error (Priority 1) | Level D | Non-compliant |

### Extensibility KPI Cards

| KPI | Description |
|---|---|
| **Technical Debt Score** | Weighted sum: 10 pts/error (Level D finding) + 5 pts/warning (Level C finding) + 1 pt/info (Level B finding). Higher score = more technical debt. |
| **Execution of Customer Objects** | % of customer objects executed within the last 6 months (from ABAP Call Monitor) |
| **Business Modifications** | Count of customer-initiated modifications to SAP standard objects (from SMODILOG table); subset of all technical modifications |
| **Unused Customer Objects** | % of customer objects not executed in last 6 months (complement of Execution KPI) |
| **Clean Core Share** | Bar chart showing % of objects at each level (A/B/C/D) |
| **Level A/B/C/D Objects** | Absolute counts at each clean core level |

### Clean Core Level Overview

Objects are assigned to the highest-criticality level found in their ATC check result:
- If a customer object has error messages → **Level D**
- If a customer object has warning messages (no errors) → **Level C**
- If a customer object has only information messages → **Level B**
- If a customer object has no findings → **Level A**

**Note:** Data update for ATC-based cards requires manual import of ATC check results. Recommend weekly import; results older than 4 weeks are flagged as "Outdated."

---

## System View — Data KPIs

The Data section measures data volume efficiency using the **Data Volume Efficiency score**.

**Formula:**
```
Data Volume Efficiency score (%) =
  (Overall memory size − Unused data − Redundant data − Outdated data − Custom table footprint)
  ÷ Overall memory size × 100
```

Higher = better (closer to 100% means data is efficiently managed).

### Data KPI Cards

| KPI | Description |
|---|---|
| **Data Volume Efficiency score** | Composite efficiency percentage (see formula above) |
| **SAP HANA Memory (%)** | Current HANA memory utilization as % of total capacity |
| **SAP HANA Disk (%)** | Current HANA disk utilization as % of total capacity |
| **Unused Data (GB)** | Table data in memory + disk not accessed in the last 30 days, where Native Storage Extension (NSE) has not yet been applied |
| **Redundant Data (GB)** | Unused table indexes in memory + disk that can be dropped without impact |
| **Outdated Data (GB)** | Data in memory + disk older than SAP Best Practice residence time (document-type dependent) |
| **Custom Table Footprint (GB)** | Total volume of custom tables in memory + disk (excludes ZARIX archiving tables) |

**Prerequisites:** ST-PI 7.40 SP31+ and SAP Note 3703380. Data runs only for **productive systems**. Initial data takes up to 1.5 weeks after activation.

---

## System View — Integration KPI

The Integration section shows the Clean Core Compliance of Interfaces based on the SAP Readiness Check.

| KPI | Description |
|---|---|
| **Clean Core Compliance of Interfaces** | Average of (standard + traditionally-compliant interfaces) / total interfaces; per SAP Note 3690029 |

The card is not auto-updated — requires a new SAP Readiness Check analysis. To improve compliance, follow SAP Business Accelerator Hub recommendations for interfaces categorized as "Conditionally Compliant" or "Not Compliant."

---

## Operations View — Overview

The Operations View provides daily compliance reporting for the **Operations principle**. It measures the operational security, quality, efficiency, and setup of productive SAP S/4HANA systems.

**Key constraint:** Operations View shows only **productive clients** of productive systems. Development and quality systems are excluded.

**Data basis:** UTC time zone; most recent values from the previous day (yesterday).

### Score Architecture

The **Operations Score** is a weighted average of three area scores:

| Area Score | Weight |
|---|---|
| **Security** | 40% |
| **System Health** | 30% |
| **Operations Setup** | 30% |

**Rating thresholds (all scores):**

| Color | Threshold |
|---|---|
| Good (Green) | > 85% |
| Warning (Orange) | 70–85% |
| Critical (Red) | < 70% |

**Calculation example:**
```
Operations Score = Security (82%) × 40% + System Health (86.4%) × 30% + Operations Setup (89%) × 30% = 80.62%
```

---

## Operations View — Security Score

**Security score** = weighted average of three KPIs:

| KPI | Weight | Description |
|---|---|---|
| **System Hardening** | 40% | Security settings of relevant system parameters and configurations |
| **Vulnerability & Lifecycle** | 40% | Whether system components are up to date and within maintenance thresholds |
| **Identity & Access Control** | 20% | Effectiveness of access-related risk controls |

**Security is driven by the Configuration & Security Analysis (CSA) use case** in SAP Cloud ALM. Each metric compares against the SAP Security Baseline (SAP Note 2253549).

### System Hardening — Metrics (all weighted ~5.9%, except Gateway Security Settings at 5.6%)

| Metric | Check (Configuration & Security Analysis) |
|---|---|
| Global Change Options | Global Change Options (SE06) — ABAP-CHANGE-00011 |
| Client Settings | Client Settings (SCC4) — VM_ABAP-CHANGE0002_1 |
| Changes to Global Change Options | Global Change Options (SE06) — ABAP-CHANGE-00012 |
| Changes to Client Settings | Client Settings (SCC4) — Changes (Last Day) — ABAP-CHANGE-00022 |
| Password Length | Minimum password length ≥ 12 — ABAP-PWDPOL-00011 |
| Password Expiration | Validity of Initial Passwords ≤ 14 Days — ABAP-PWDPOL-0002-1 |
| Downward Compatible Passwords | Enablement of Downward Compatible Passwords — ABAP-PWDPOL-0004-1 |
| Password Length (Security Policy) | Usergroup-specific minimum password length — ABAP-PWDPOL-0001-2 |
| Password Expiration (Security Policy) | Usergroup-specific max validity period — ABAP-PWDPOL-0003-3 |
| Encryption of Internal Server Communication | Dedicated internal port for message server — ABAP-MSGSRV-0001-1 |
| Unauthorized Monitoring of Message Servers | Blocking of unauthenticated monitoring — ABAP-MSGSRV-0006-1 |
| Gateway ACL File Evaluation | RFC Gateway behavior when no ACL file exists — ABAP-RFCGW-0004-1 |
| Gateway Monitoring Set to Local | RFC Gateway communication configuration — ABAP-RFCGW-0005-1 |
| Gateway Simulation Mode Off | Simulation mode for reg_info and sec_info — ABAP-RFCGW-0006-1 |
| Message Server ACL Path | ACL file path for message server — ABAP-MSGSRV-0004-1 |
| Security Method of Trust Relationships | Security method of trust relationships — ABAP-TRUST-0003-1 |
| Gateway Security Settings | Activation status of RFC Gateway security — ABAP-RFCGW-0003-1 |

### Vulnerability & Lifecycle — Metrics (each 25%)

| Metric | Check |
|---|---|
| Support Package Updates | Last Update of Software Components (Support Packages) — ABAP-SECUPD-0001-1 |
| Age of SAP Cryptolib Assembly | Age of SAP Cryptolib Assembly Date — ABAP-SECUPD-00012 |
| Age of SAP Kernel Compile | Age of SAP Kernel Compile Date — ABAP-SECUPD-00013 |
| Age of Support Packages | Age of Support Packages — ABAP-SECUPD-00031 |

### Identity & Access Control — Metrics (each ~14.2–14.3%)

| Metric | Check |
|---|---|
| Default Password of SAP* | Default Password of User SAP* in Client 000 — ABAP-STDUSR-0001-4-2 |
| Existence of SAP* | Existence of User SAP* in Client Other than 000 — ABAP-STDUSR-00012-1 |
| Lock Status of SAP* | Lock of User SAP* in Client 000 — ABAP-STDUSR-00013-2 |
| SAPCPIC User | Existence of User SAPCPIC — ABAP-STDUSR-00031 |
| Default Password of TMSADM | Default Password of User TMSADM — ABAP-STDUSR-00041 |
| TMSADM in Production Client | Existence of User TMSADM in Client other than 000 — ABAP-STDUSR-00043 |
| EARLYWATCH in Obsolete Client | Existence of User EARLYWATCH in Obsolete Client 066 — ABAP-STDUSR-0005-1 |

---

## Operations View — System Health Score

**System Health score** = weighted average of four KPIs:

| KPI | Weight | Description | SLA |
|---|---|---|---|
| **Connectivity** | 50% | Quality of connection between system and SAP Cloud ALM | Critical System Heartbeat: 10%; Critical Instance Heartbeat: 10% |
| **Exceptions** | 25% | Number of Runtime Errors, System Logs, Application Logs | Runtime Errors: 400; System Logs: 9000; Application Logs: 2500 |
| **Background Processing** | 15% | Number of batch jobs with status "Canceled" | Batch Jobs Aborted per client per 5 min: 2.24 |
| **Performance** | 10% | Average and maximum daily response times | Avg: 4000 ms; Max: 200,000 ms |

**Prerequisites:** ST-PI 7.40 SP28+; Health Monitoring and Integration & Exception Monitoring apps activated in SAP Cloud ALM; ABAP Runtime, ABAP System Log, and ABAP Application Log metrics manually enabled.

**Calculation example:**
```
System Health = Connectivity (87%) × 50% + Exceptions (90%) × 25% + Background Processing (70%) × 15% + Performance (99%) × 10% = 86.4%
```

### Connectivity Metrics

| Metric | Weight | Description |
|---|---|---|
| Critical System Heartbeat | 90% | ABAP system sends heartbeat to SAP Cloud ALM every minute; >0 = connection issue |
| Critical Instance Heartbeat | 10% | ABAP instance heartbeat; >0 = instance unavailability |

### Exceptions SLAs

| Metric | Weight | SLA (daily count) | Transaction |
|---|---|---|---|
| Runtime Errors (ABAP dumps) | 70% | 400 | ST22 |
| System Logs | 25% | 9,000 | SM21 |
| Application Logs | 5% | 2,500 | SLG1 |

### Performance SLAs

| Metric | Weight | SLA |
|---|---|---|
| Average Response Time | 90% | 4,000 ms |
| Maximum Response Time | 10% | 200,000 ms |

---

## Operations View — Operations Setup Score

**Operations Setup score** = weighted average of eight KPIs. All KPIs measure whether the SAP Cloud ALM use case is configured and actively delivering data.

| KPI | Weight | Description |
|---|---|---|
| **Health Monitoring** | 20% | System connected to Health Monitoring app; Configuration Status (50%) + Runtime Status (50%) |
| **Exception Monitoring** | 20% | Connected to Integration & Exception Monitoring; 6 sub-metrics covering Config Status, Runtime Status, and the Runtime Errors / System Logs / Application Logs monitoring categories |
| **Integration Monitoring** | 15% | Connected to Integration & Exception Monitoring (integration messages via SAP AIF); Config Status + Runtime Status + AIF Config Status + AIF Runtime Status (25% each) |
| **Job & Automation Monitoring** | 15% | Connected to Job & Automation Monitoring app; Config Status (50%) + Runtime Status (50%) |
| **Configuration & Security Analysis** | 15% | Connected to Configuration & Security Analysis app; Config Status (50%) + Runtime Status (50%) |
| **Real User Monitoring** | 5% | Connected to Real User Monitoring app; Config Status (50%) + Runtime Status (50%) |
| **Business Service Management** | 5% | System added to a business service in Business Service Management app; Config Status (100%) |
| **Business Process Monitoring** | 5% | Connected to Business Process Monitoring app; Config Status (50%) + Runtime Status (50%) |

**Calculation example:**
```
Operations Setup = Health Monitoring (100%) × 20% + Exception Monitoring (100%) × 20%
  + Integration Monitoring (75%) × 15% + Job & Automation Monitoring (50%) × 15%
  + Configuration & Security Analysis (100%) × 15% + Real User Monitoring (100%) × 5%
  + Business Service Management (100%) × 5% + Business Process Monitoring (100%) × 5% = 89%
```

---

## AI-Assisted Analysis (Operations View)

The Operations View includes an optional **AI-assisted analysis** feature ("AI-Assisted Operations Score Optimization" in SAP for Me) that:
- Identifies the top 3 KPIs and metrics driving the score
- Provides a score breakdown with recommendations
- Estimates the impact of each fix

Must be activated via SAP for Me → Portfolio & Products → Business AI. Not available in the China (North 3) – cn20 region.

---

## Deep-Dive Views

### Customer Objects (Extensibility Deep Dive)

Provides object-level detail on extensibility compliance. Requires ATC check result import.

**Object Type Harmonization (effective August 2026):** The dashboard uses a "focus object types" concept — only 10 logic-bearing, code-based ABAP types are used for KPI calculations and level assignments: BDEF, CLAS, DDLS, FUNC, FUGR, FUGX, INTF, PROG, ENHO, SXCI. Other types (data elements, domains, tables, etc.) are scanned but classified as supporting objects and excluded from KPIs. This is a significant change from pre-August 2026 behavior — object counts and scores may differ substantially. See `clean-core-extensibility` skill, knowledge file 10, for full details.

**Three table views:**
- **All** — all customer objects (focus object types + supporting/non-relevant objects)
- **Clean Core Relevant** — only focus object types with a level assignment (A/B/C/D)
- **With ATC Findings** — objects that have ATC findings from clean core checks

**Level A definition (as of August 2026 harmonization):** Objects with any of these three ABAP Language Versions:
- Language Version 5 (LV5) — "ABAP for Cloud Development"
- Language Version 2 (LV2) — "ABAP for Key Users" *(newly included in August 2026)*
- Language Version K (LVK) — "Generated - ABAP for Key Users" *(newly included in August 2026)*

Level A data source: SAP EarlyWatch Alert (EWA) + Online Collectors (Custom Code Analytics / CCA). Per-object names are not available at Level A.

**Level B/C/D definition:** Focus object types with Language Version "Classic ABAP" that have findings from three ATC clean core checks (Allowed SAP Enhancement Technologies, Usage of APIs, Critical Statements).

**Key columns:**

| Column | Description |
|---|---|
| **Clean Core Level** | Assigned based on most critical finding: Priority 1 (error) = Level D; Priority 2 (warning) = Level C; Priority 3 (info) = Level B |
| **Technical Debt Score** | 10 pts/error + 5 pts/warning + 1 pt/info; higher = more debt |
| **Technical Debt Share (%)** | Object's debt ÷ system total debt × 100 |
| **ABAP Language Version** | ABAP for Cloud Development (LV5) / ABAP for Key Users (LV2) / Standard ABAP / Generated — ABAP for Key Users (LVK) |
| **Level B/C/D Findings** | Count by finding severity |
| **Level B/C/D References** | Count of references to Classic APIs (B), Internal SAP Objects (C), Not Recommended SAP Objects (D) |
| **Level B/C/D Behaviors** | Write access to SAP tables → Level D; Read access → Level C; CALL TRANSACTION / ROLLBACK WORK → Level B |

**Finding types:**
- **Reference-based:** The customer object calls or references an SAP object/API
- **Behavior-based:** The customer object produces a behavior (read/write SAP tables, CALL TRANSACTION, etc.) independent of a specific SAP object

**Important — ATC configurations not reflected:** ATC Baseline, ATC Exemptions, and customer-specific priority changes are all ignored by the dashboard. It always uses the raw, unexempted ATC findings.

**Important — Key User objects prerequisite:** SAP Note 3593439 ("Exclude Key User Items from ATC Check") must be implemented before running ATC, or Key User extensibility objects (LV2/LVK) may be incorrectly classified as Level B/C/D instead of Level A.

**Note:** Function modules (FUNC) are counted as independent main objects (R3TR), not sub-objects of their function group (FUGR). This increases visible object counts but improves precision — each function module is assessed and classified individually.

### Business Modifications (Extensibility Deep Dive)

Shows potential business modifications (customer-initiated changes to SAP standard objects) from the SMODILOG table.

**Types of modifications in SMODILOG:**
1. **Unavoidable** — automatically generated by standard tools; uncritical, overwritten during upgrade
2. **SAP Note / Legacy enhancements** — corrections and user exits; minimal upgrade effort
3. **Business Modifications** — customer decisions, not foreseen by SAP; require significant upgrade adaptation → **this is what the dashboard focuses on**

**Note:** Some SAP Notes requiring manual pre/post steps may be incorrectly classified as business modifications. Verify by searching SAP for Me → Services & Support → Knowledge Search.

**Data source:** SAP EarlyWatch Alert Online Collectors (listed in System View Data Collection Tools).

### Data Volume Efficiency (Data Deep Dive)

Provides table-level detail for each data KPI card.

| Tab | Content |
|---|---|
| **SAP HANA Memory** | Current memory usage broken down by top-consuming tables; shows memory pressure and growth rate |
| **SAP HANA Disk** | Current disk usage broken down by top-consuming tables; record counts and growth trends |
| **Unused Data** | Tables not accessed in last 30 days; read/write counts; NSE potential |
| **Redundant Data** | Obsolete table indexes; identifies candidates for deletion |
| **Outdated Data** | Data older than SAP Best Practice residence time; archiving object suggestions per document type |
| **Custom Table Footprint** | Total volume of custom tables; excludes ZARIX archiving tables; helps identify custom development impact |

---

## FAQ Highlights

### System View
- Changes take **up to 10 days** to be reflected (not 1.5 weeks — that is only for initial setup)
- If no data appears in Extensibility cards: ATC check result has not been manually imported
- ABAP Call Monitor and SUSG tool activation: SAP Note 2679723 (ABAP Call Monitor) and SAP Note 2701371 (Aggregated Usage Data); SAP Note 3100194 for storage impact
- SAP recommends keeping ABAP Call Monitor active **at all times**
- Business Modifications may include SAP Note changes (false positives) — further investigation in SAP for Me required
- Data Volume Efficiency KPIs run on **productive systems only** (not development/QA); CALM DVM COLLECTOR job retries automatically on failure

### Operations View
- Operations View is **not a monitoring tool** — daily report on clean core progress
- Non-compliant security metric = check not compliant, not yet configured, or data collection not on
- System Health goal is not 100% — aim for "green" (>85%); use it to identify anomalies
- System Health shows 0% if Health Monitoring and Integration & Exception Monitoring apps are not configured
- Business Service Management KPI specifically measures whether a business service is configured with SLOs and event actions (not just connectivity)
- SLAs are fixed for all RISE with SAP customers (cannot be customized)
- SLA thresholds for System Health metrics were determined by statistical analysis on real productive SAP S/4HANA systems
- For incidents: System View → SV-CLM-RMD-SYS; Operations View → SV-CLM-RMD-OPS
