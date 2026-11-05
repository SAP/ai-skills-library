# Clean Core Measurement Framework — Governance & Maturity

**Source:** Clean Core Measurement Framework – Governance and Maturity (external)  
**Document ID:** SAP1222195 | Public download: https://dam.sap.com/mac/app/p/pdf/asset/preview/a5A7qyM?ltr=a&rc=10&doi=SAP1222195  
**File:** Clean_Core_Governance_and_Operational_Practices_Maturity_v2.0_2605  
**Version:** v2.0, May 2026  
**Ingested:** 2026-09-13  
**Audience:** Installed base customers, Enterprise Architects, TQMs  
**Purpose:** How to assess the clean core governance and maturity for each principle and calculate the associated score. Together with the KPI deck, establishes the Clean Core Measurement Framework.

> **Scope of this file:** Cross-principle approach, structure, and practice overview per principle. The per-practice evaluation criteria and 0–5 maturity rating guidance tables for the **Extensibility** dimension are in `knowledge/05-governance-maturity-extensibility.md` (in the `clean-core-extensibility` skill). Per-practice detail for the other four dimensions will be added to their respective expert skills when those are ingested.

---

## What is the Clean Core Measurement Framework?

> *"The clean core measurement framework enables customers to successfully advance toward a clean core by assessing their governance and maturity, defining concrete actions, and continuously tracking their success using clean core KPIs."*

The framework has two complementary components:

| Component | Purpose |
|---|---|
| **Governance & Maturity Assessment** | Assess how well the organization is structurally set up to achieve and sustain a clean core — practices, processes, tools, and people |
| **KPI Measurement** | Track quantitative progress across the five principles using defined metrics and calculation rules |

**Evolution roadmap:**

| Stage | What exists |
|---|---|
| **Past** | Clean core definition |
| **Now** | RISE with SAP Methodology framework (Success Plan & Quality Gates) + Governance & Maturity Assessment + KPIs |
| **Vision** | Benchmarking *(SAP Lab Preview — subject to change)* |

---

## Guiding Principles for the Governance & Maturity Score

The score assesses organizational maturity across a set of **practices** per principle. Each practice is evaluated on a **0–5 scale**:

| Score | Meaning |
|---|---|
| 0 | Not in place |
| 1 | Initial / ad hoc |
| 2 | Developing |
| 3 | Defined |
| 4 | Managed |
| 5 | Optimizing |

Each practice score is derived from a set of **evaluation criteria questions** with explicit guidance on what each maturity level looks like. Scores are aggregated to a principle-level result, split by sub-dimension (e.g., Governance vs. System Setup for Extensibility).

The assessment is designed to:
1. Understand the current maturity baseline
2. Identify the most impactful areas for improvement
3. Define concrete actions and an improvement roadmap
4. Track progress over time as part of the RISE with SAP Methodology

---

## Practice Overview by Principle

### Business Processes — 5 Practices

| Practice ID | Practice Name | Core question |
|---|---|---|
| PRO-01 | Enterprise Architecture Management | Is EAM established as a practice, with tools integrated into BPM and ALM? |
| PRO-02 | Business Process Management | Is BPM established, with processes defined based on SAP reference content and KPIs measuring process efficiency? |
| PRO-03 | Application Lifecycle Management | Is ALM established, with requirements captured, traced to processes, and test management integrated? |
| PRO-04 | Process Deviations Management | Are process deviations standardized, justified, and governed through a Solution Standardization Board? |
| PRO-05 | Organization Transformation Readiness | Is a transformation office (or equivalent) formalized, with OCM integrated early into transformation programs? |

**Sub-dimensions:** The L2 deck positions all five as part of an end-to-end toolchain: EAM → BPM → ALM.

---

### Extensibility — 11 Practices (6 Governance + 5 System Setup)

**Governance practices:**

| Practice ID | Practice Name |
|---|---|
| EXT-GOV-01 | Governance Process for Extensions |
| EXT-GOV-02 | Extension Architecture Guidelines |
| EXT-GOV-03 | Development Guidelines |
| EXT-GOV-04 | Development Skills & Enablement |
| EXT-GOV-05 | KPIs & Measuring |
| EXT-GOV-06 | Housekeeping |

**System Setup practices:**

| Practice ID | Practice Name |
|---|---|
| EXT-SYS-01 | Automated Code Checks (ATC) |
| EXT-SYS-02 | Exemption Process |
| EXT-SYS-03 | Setup of ABAP Cloud Software Component |
| EXT-SYS-04 | Usage Data Collection |
| EXT-SYS-05 | Setup of SAP Business Technology Platform |

> Full evaluation criteria and 0–5 rating guidance for all 11 practices: see `clean-core-extensibility` skill → `knowledge/05-governance-maturity-extensibility.md`

---

### Data — 5 Practices

| Practice ID | Practice Name | Core question |
|---|---|---|
| DAT-01 | Data Strategy Setup | Are clear data roles, organizational alignment, and a governance framework in place? |
| DAT-02 | Data Governance Setup | Is a governance framework established, with Data Mesh/Data Product principles and a data catalog? |
| DAT-03 | Data Quality Management | Are regular data quality assessments performed, supported by cleansing tools and a governance board? |
| DAT-04 | Data Volume Efficiency Management | Is a scalable data infrastructure with well-managed retention policies in place? |
| DAT-05 | Data Protection Setup | Are data protection procedures, breach response, and compliance audits (e.g., GDPR) established? |

---

### Integration — 6 Practices

| Practice ID | Practice Name | Core question |
|---|---|---|
| INT-01 | Integration Strategy | Is a clear target architecture and multi-year roadmap (5–10 years) defined, aligned with SAP ISA-M? |
| INT-02 | Integration Governance Process | Is a formal governance framework established, with a CoE and defined oversight? |
| INT-03 | Integration Landscape | Does the landscape leverage modern middleware, API-led strategies, and event-driven architecture? |
| INT-04 | Tool Chain | Are BPM, EAM, assessment, ALM, and interface repository tools used for end-to-end integration visibility? |
| INT-05 | SAP S/4HANA Integration Readiness | Is there clear visibility of all integration technologies and a migration plan toward clean core? |
| INT-06 | Operational Framework | Is a robust operational framework with central monitoring, alerting, and a CoE in place? |

---

### Operations — 8 Practices

| Practice ID | Practice Name | Core question |
|---|---|---|
| OPS-01 | Clean Core Governance | Is organizational governance established to achieve the new operating model and manage innovation cycles? |
| OPS-02 | Business Transformation Toolchain | Is the integrated toolchain adopted to streamline implementation and operations? |
| OPS-03 | Continuous Improvement for an Enduring Clean Core | Are requirements continuously revisited in future cycles to improve clean core adoption? |
| OPS-04 | Test Management and Execution | Are early agile-based testing approaches and test automation in place? |
| OPS-05 | Software Delivery Efficiency | Is software delivery speed increasing while maintaining quality and reliability? |
| OPS-06 | Secure Operations | Are secure operations embedded: baseline adoption, lifecycle compliance, breach response? |
| OPS-07 | Release Management | Is a controlled, predictable release process in place, keeping the system current with SAP innovations? |
| OPS-08 | IT Operations Excellence | Is comprehensive monitoring, alerting, and event management established across the SAP landscape? |

---

## How to Use the Assessment

1. **Conduct the assessment** — work through each practice's evaluation criteria questions with the customer (typically 1–4 hours depending on number of principles in scope)
2. **Score each practice** on the 0–5 scale using the maturity rating guidance
3. **Aggregate to a principle score** — each principle produces a summary score (split by sub-dimension where applicable)
4. **Identify improvement areas** — practices with lower scores indicate where governance investment will have the most impact
5. **Connect to KPIs** — each practice has a "Governance & maturity relevance" link to specific KPIs; improving governance maturity is expected to drive measurable KPI improvement over time
6. **Revisit regularly** — the assessment is designed for periodic re-evaluation as part of the RISE with SAP Methodology engagement cadence

---

## Connection to KPIs

Every KPI in the KPI deck includes a **"Governance & maturity relevance"** field naming the specific practice(s) most directly linked to that KPI's performance. This creates a closed loop:

> Governance maturity improvement → better practices → better KPI scores → measurable clean core progress

Example linkages:
- Extensibility: *Maturity of governance process* → Clean core share, Technical debt score
- Extensibility: *Maturity of housekeeping practice* → Unused code share
- Business Processes: *Maturity of process deviation management* → Process fit-to-standard alignment
- Operations: *Maturity of release management* → Software stack currency KPI

---

## Key Reference Links

- Full deck (external): https://dam.sap.com/mac/app/p/pdf/asset/preview/a5A7qyM?ltr=a&rc=10&doi=SAP1222195
- RISE with SAP Methodology: https://www.sap.com/products/erp/rise/methodology/clean-core.html
