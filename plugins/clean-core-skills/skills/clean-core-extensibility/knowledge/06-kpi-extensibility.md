# Clean Core KPI Measurement Framework – Extensibility

Source: SAP Clean Core Measurement Framework – KPIs (2025_KPI.pptx), Extensibility section (slides 28–40)

---

## Sources

When citing content from this file, link to the primary source. This is a publicly available SAP document hosted on the SAP Digital Asset Management (DAM) portal.

| Topic | Source | URL |
|-------|--------|-----|
| All content in this file | Clean Core Measurement Framework: KPIs (2025) | https://dam.sap.com/mac/u/a/XbqgDc4?rc=10&doi=SAP1240359 |
| Clean Core Extensibility context | SAP White Paper: Clean Core Extensibility (2025) | https://www.sap.com/documents/2024/09/20aece06-d87e-0010-bca6-c68f7e60039b.html |
| RISE with SAP Methodology Dashboard (KPI tracking) | RISE with SAP Methodology | https://support.sap.com/en/alm/rise-with-sap-methodology.html |
| ATC check for technical debt score | SAP Note 3565942 (clean core checks) | https://me.sap.com/notes/3565942 |

---

## Overview

The KPI deck is part of the clean core measurement framework. The two components are:
1. **Governance & Maturity** – Recommendations on tools, governance structures (e.g., SSB), and expertise required to get and stay clean.
2. **KPIs** – Measure clean core adherence both during a project and in ongoing operations, based on analysis of system data and collected metrics.

KPIs are presented per clean core principle. This file covers the **Extensibility** principle only.

---

## Why Clean Core Extensibility Matters

**Expected benefits:**
- **Strategy enablement:** Improve agility and innovation readiness to allow for flexible business strategy adjustments (NQ)
- **Business value:** Increase upgrade stability (NQ); Differentiate extensions only while adhering to SAP standard and best practices (NQ)
- **Risk mitigation:** Lower the risk of extended downtime or broken extensions during upgrade events (NQ); Reduce security risks associated with unused and unmaintained coding (NQ)
- **IT spend effectiveness (TCO):** Reduce maintenance and adjustment efforts during upgrade events to free up resources

**How to achieve clean extensions:**
- Create decoupled extensions to ensure upgrade stability — leverage released APIs from SAP
- Use modern extensibility technologies with SAP Build and the clean core extensibility model
- Rely on released APIs wherever possible to avoid breaking upgrades
- Choose between on-stack and side-by-side extensibility based on use case, applying an SAP BTP first strategy
- Ensure continuous governance from requirement → design → implementation → deployment:
  - Requirement: Only allow extensions that add clear business value
  - Design: Define guidelines to ensure the cleanest option is used
  - Implementation: Encourage developers to follow the clean core approach and document technical debt transparently
  - Deployment: Introduce mandatory code checks and a structured exemption process
- Ensure technical debt is always an informed decision — manage it professionally
- Measure technical debt, set ambitious but realistic goals to reduce it; acknowledge that legacy code will not vanish overnight

---

## Extensibility KPIs at a Glance

| Stakeholder | KPI Category | KPI |
|---|---|---|
| CTO – "I need to understand the degree of technical debt in the extensions of my organization" | Technical debt score | Score of technical debt per custom object |
| CIO – "I need to understand that my transformation team is following a clean core mindset with regard to extensibility" | Clean core share | % of code objects per clean core level |
| CSO – "I need to understand the excess of unused coding to assess associated risks" | Unused code share | % of unused custom code |
| Upgrade Project Manager – "I need to estimate the adjustment effort caused by modified SAP standard objects during upgrade events" | Business modifications | # of business modifications to SAP standard objects |

**RISE with SAP Methodology touchpoints:** RISE with SAP Methodology Clean Core Q-gates | RISE with SAP Methodology Dashboard

---

## Extensibility KPIs Overview Table

| KPI Category | KPI | Metric | Measurement Tool |
|---|---|---|---|
| Clean core share | % of code objects per clean core level | Identify all Level A objects; Identify all Level B/C/D objects | ABAP test cockpit clean core checks; Online Collectors SAP Note 2947886 |
| Technical debt score | Score of technical debt per custom object | Weighted score by amount and priority of ABAP test cockpit findings | ABAP test cockpit clean core checks |
| Unused code share | % of unused custom code | Usage information of all ABAP Call Monitor-compatible objects | ABAP Call Monitor (SCMON and SUSG) |
| Business modifications | # of business modifications to SAP standard objects | Overview of modifications and their impact on the system | Online Collectors SAP Note 2947886 |

---

## KPI Detail: Clean Core Share

**Objective:** Provide transparency on the distribution of custom code objects across clean core levels.

**Key results:** Clean core share provides transparency into how custom code objects (including SAP BTP side-by-side extensions) are distributed across clean core levels. Essential for driving system efficiency and guiding optimization efforts. Supports strategic decision-making and ensures long-term maintainability.

**How it works:**
- Clean core share is determined by evaluating each custom code object based on its "worst" reference (the most non-compliant dependency defines the object's classification)
- ABAP cloud objects and side-by-side extensions with SAP BTP → Level A
- Objects referring to internal objects → Level C
- Example distribution for 1,000 objects:
  - Level A: 10% (100 objects)
  - Level B: 50% (500 objects)
  - Level C: 35% (350 objects)
  - Level D: 5% (50 objects)
- Actionable insight: Reducing Level C/D share indicates stronger adherence to clean core principles

**Calculation details:** Each custom code object is classified based on its "worst" reference level, according to the clean core level concept and the ABAP language version used.

**Recommended tools:**
- Now: ABAP test cockpit and custom dashboard
- Future: RISE with SAP Methodology dashboard

**Prerequisites & limitations:**
- Now: ABAP test cockpit clean core checks (SAP Note 3565942) configured, or Project Kernseife
- Future: Setup of data collectors for RISE with SAP Methodology dashboard

**Cadence:** Regular basis (e.g., weekly)

**Measurement guidance:**
1. Implement the latest version of SAP Note 3565942 to leverage ABAP test cockpit clean core check findings
2. Extract data regularly into a custom dashboard, or — in the future — use the RISE with SAP Methodology dashboard

**Type:** Semi-automatic

**Governance & maturity relevance:** Maturity of governance process | Value: Non-quantifiable | Effort: Medium

---

## KPI Detail: Technical Debt Score

**Objective:** Create a virtual score to assess the technical debt of individual objects and enable higher-level aggregation (e.g., development packages, namespaces).

**Key results:**
- Identify objects with higher technical debt
- Measure overall technical debt in the system over time
- Set goals, track progress, and compare results across periods

**How it works:**
- The technical debt score is a weighted measure based on the severity of references to SAP objects
- Weighting factors for ABAP test cockpit findings:
  - Error (Priority 1): 10 points
  - Warning (Priority 2): 5 points
  - Information (Priority 3): 1 point
- Score = sum of weighted findings
- Example: 5 errors + 20 warnings + 10 informational = 5×10 + 20×5 + 10×1 = 160 points
- While clean core share gives a general overview, the technical debt score is more actionable — it represents the technical debt within a given object

**Formula:**
```
Technical debt score (per object) =
  (# of Priority 1 findings × 10) +
  (# of Priority 2 findings × 5) +
  (# of Priority 3 findings × 1)
```

**Calculation details:** Based on priority assessment of ABAP test cockpit findings from the clean core check variant (SAP Note 3565942).
- Relevant checks: "Usage of APIs", "Allowed enhancement technologies", "Search customer modifications", "Critical statements"

**Recommended tools:**
- Now: ABAP test cockpit and custom dashboard
- Future: RISE with SAP Methodology dashboard

**Prerequisites & limitations:**
- Now: ABAP test cockpit clean core checks (SAP Note 3565942) configured, or Project Kernseife
- Future: Setup of data collectors for RISE with SAP Methodology dashboard

**Cadence:** ABAP test cockpit clean core checks should run on a regular basis (e.g., weekly) to update scores.

**Measurement guidance:**
1. Implement the latest version of SAP Note 3565942 to leverage ABAP test cockpit clean core check findings
2. Extract data regularly into a custom dashboard, or — in the future — use the RISE with SAP Methodology dashboard

**Type:** Semi-automatic

**Governance & maturity relevance:** Maturity of governance process | Value: Non-quantifiable | Effort: Medium

---

## KPI Detail: Unused Code Share

**Objective:** Identify the share of unused custom code in the system.

**Key results:** Highlights the portion of custom objects not utilized, helping identify areas for potential cleanup and optimization.

**How it works:**
- Requires activating usage data measurements
- SAP recommends using ABAP Call Monitor (SCMON) for usage data collection + transaction SUSG for aggregation
- Steps:
  1. Activate ABAP Call Monitor (SCMON) to collect usage data
  2. Aggregate SCMON data using transaction SUSG
  3. Compare list of used objects with all custom code objects (from tables such as TADIR)
  4. This comparison identifies unused objects for potential cleanup
- Every unused custom code object represents potential technical debt

**Formula:**
```
Unused code share (%) = (# unused custom code objects / # total custom code objects) × 100
```

**Recommended tools:** ABAP Call Monitor (SCMON) and SUSG

**Prerequisites & limitations:**
- Activation of usage logging via ABAP Call Monitor (SCMON) and SUSG for aggregation in productive system
- Ideally covers a time frame of 12 months or more

**Cadence:** Usage logging should be active permanently in production systems.

**Measurement guidance:**
- Activate usage logging directly via transaction SUSG in production
- See SAP Notes 2643357 and 2701371 for more details

**Type:** Automatic

**Governance & maturity relevance:** Maturity of housekeeping practice | Value: Non-quantifiable | Effort: Medium

---

## KPI Detail: Business Modifications

**Objective:** Provide transparency on the number of business modifications in the system.

**Key results:** Business modifications generally pose risks during upgrades, as they involve changes to SAP standard code outside of extension points, potentially leading to additional maintenance efforts. Tracking supports proper risk assessment during upgrades and highlights the need for cleaner extension practices.

**How it works:**
- Business modifications are a subset of all logged changes to SAP standard objects in table SMODILOG
- They represent intentional changes by the customer, distinguished from technical modifications (unintended changes, e.g., from SAP Note implementations)
- Can be identified using the custom code analytics dashboard or the RISE with SAP Methodology dashboard
- The Modification Analysis guide explains how to extract data using patterns to identify technical modifications not created intentionally as business modifications

**Recommended tools:** RISE with SAP Methodology dashboard

**Prerequisites & limitations:** Setup of data collectors for RISE with SAP Methodology dashboard

**Cadence:** Business modifications should be tracked on a regular basis (e.g., weekly).

**Measurement guidance:** The calculation logic for business modifications is explained in the document "Modification Analysis". Results can be reviewed directly in the dashboards.

**Type:** Automatic

**Governance & maturity relevance:** Maturity of extension architecture guidelines | Value: Non-quantifiable | Effort: Medium

---

## Connection to Other Clean Core Principles

The KPI deck also covers Business Processes, Data, Integration, and Operations KPIs. The extensibility KPIs listed here connect to:

- **Business Processes – Alignment to clean core KPI:** Delta requirements (G-EP gaps) are evaluated against clean core extensibility and integration dimensions to determine if extensions are compliant
- **Governance & Maturity Assessment:** Each extensibility KPI maps to a specific governance practice:
  - Clean core share → Maturity of governance process (EXT-GOV-01 to EXT-GOV-03)
  - Technical debt score → Maturity of governance process
  - Unused code share → Maturity of housekeeping practice (EXT-SYS-04)
  - Business modifications → Maturity of extension architecture guidelines (EXT-EXT-02)

---

## Glossary of Key Terms

| Term | Definition |
|---|---|
| Metric | A quantifiable measure used to track and assess the status of a specific process or activity. Not always tied to strategic goals. Example: "Number of custom objects", "Custom software lines of code (SLOC)" |
| KPI (Key Performance Indicator) | A specific metric directly linked to strategic objectives. Used to evaluate performance against defined goals. Example: Fit-to-Standard (%) with a target of >90% |
| Value driver | An activity or capability that contributes measurable value across: business value, IT spend effectiveness (TCO), risk mitigation, and strategy enablement |
| Q (Quantified) | Benefit that can be measured in concrete numbers (cost savings, time reduction, etc.) |
| NQ (Not Quantified) | Benefit that is real but harder to express in precise numbers (agility, innovation readiness, etc.) |
| Technical debt score | Weighted sum of ABAP test cockpit findings per object: P1×10 + P2×5 + P3×1 |
| Clean core share | Distribution of custom code objects across Level A/B/C/D, based on worst-case reference |
| Business modifications | Intentional customer changes to SAP standard code objects (table SMODILOG), outside of extension points |
