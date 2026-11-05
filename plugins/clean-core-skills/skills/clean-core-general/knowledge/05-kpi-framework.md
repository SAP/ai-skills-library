# Clean Core Measurement Framework — KPIs

**Source:** Clean Core Measurement Framework – KPIs (external)  
**Document ID:** SAP1240359 | Public download: https://dam.sap.com/mac/app/p/pdf/asset/preview/XbqgDc4?ltr=a&rc=10&doi=SAP1240359  
**File:** Measurement_Criteria_for_Clean_Core_KPIs_Ext_Final_v1.3  
**Version:** v1.3 Final  
**Ingested:** 2026-09-13  
**Audience:** Installed base customers, Enterprise Architects, TQMs  
**Purpose:** The KPI deck builds on the L2 and Governance & Maturity decks by introducing what the recommended KPIs are for each clean core principle and how to assess them.

> **Scope of this file:** Cross-principle approach, glossary, KPI overview per principle, and guiding principles for use. The per-KPI calculation details for **Extensibility** are already in `knowledge/06-kpi-extensibility.md` (in the `clean-core-extensibility` skill). Per-KPI detail for the other four dimensions will be added to their respective expert skills when those are ingested.

---

## What is the Clean Core Measurement Framework?

> *"The clean core measurement framework enables customers to successfully advance toward a clean core by assessing their governance and maturity, defining concrete actions, and continuously tracking their success using clean core KPIs."*

The framework covers all five principles: Processes, Extensibility, Data, Integration, Operations.

**Measurement framework evolution roadmap:**

| Stage | What exists |
|---|---|
| **Past** | Clean core definition |
| **Now** | RISE with SAP Methodology framework (Success Plan & Quality Gates) + Governance & Maturity Assessment + KPIs |
| **Vision** | Benchmarking *(SAP Lab Preview — subject to change)* |

---

## Glossary of Terms

| Term | Definition |
|---|---|
| **Metric** | A quantifiable measure used to track and assess the status of a specific process or activity. Not always tied to strategic goals. Example: "Number of custom objects", "Custom software lines of code (SLOC)" |
| **KPI (Key Performance Indicator)** | A specific type of metric directly linked to strategic objectives. Used to evaluate performance against defined goals. Example: Fit-to-Standard (%) as a KPI for a >90% standardization target |
| **Value driver** | An activity or capability that contributes measurable value across one or more of four categories: business value, IT spend effectiveness (TCO), risk mitigation, strategy enablement |

> All KPIs are metrics, but not all metrics are KPIs. Metrics cover a wide range of data points; KPIs focus on the most important indicators of success aligned with strategic objectives.

---

## Guiding Principles for Clean Core KPIs

1. **Foundational reference** — the KPIs presented are SAP's recommended selection for measuring progress across the five principles. They serve as a foundational reference, especially for executive stakeholder conversations (CIO, COO).

2. **Context-dependent** — depending on a customer's specific context and strategic goals, additional KPIs may be considered.

3. **Automation maturity varies** — KPIs and metrics vary in terms of automation maturity and feasibility. SAP is progressively integrating automated collection into the RISE with SAP Methodology dashboard based on technical feasibility.

4. **Four value driver categories** — for each principle, SAP has defined value drivers across:
   - Strategy enablement
   - Risk mitigation
   - Business value
   - IT spend effectiveness (TCO)
   Benefits are classified as either **quantifiable (Q)** or **not quantifiable (NQ)**.

5. **KPI categories** — KPIs are grouped into categories according to their attributes and purpose. Each KPI/category is presented with: objective, calculation details, supporting tools, cadence, prerequisites, and measurement guidance.

6. **Integral part of the measurement framework** — governance and maturity adoption are expected to drive continuous improvement in KPI performance. The two components are designed to work together.

---

## RISE with SAP Methodology Dashboard

The dashboard is the central tool for KPI tracking:
- Comprehensive set of dashboards to track and monitor status
- Gathers insights and provides recommendations for transformation projects
- SAP is progressively integrating automated KPI collection into the dashboard

Current state: many KPIs require semi-automatic or manual measurement; automation roadmap is ongoing.

---

## KPI Overview by Principle

### Business Processes — 4 KPIs

| KPI | KPI Category | What it measures | Tool |
|---|---|---|---|
| **Process fit-to-standard alignment** | Process standardization | % of processes fit to standard | SAP Signavio + SAP Cloud ALM |
| **Process fit-to-standard alignment – gaps** | Process adaptation | % of processes with G-EP or G-EC gap deviations | SAP Signavio + SAP Cloud ALM |
| **Alignment to clean core** | Process adaptation | % of delta requirements aligned with clean core extensibility and integration guidelines | SAP Cloud ALM |
| **Alignment to SAP S/4HANA target architecture** | Process standardization | # of adoption backlog simplification items from SAP Readiness Check | SAP Readiness Check |

Measurement type: Semi-automatic. Cadence: Each process governance cycle.

> *Full per-KPI detail with formulas, measurement guidance, and G&M linkage: `clean-core-processes` skill → `knowledge/02-kpi-processes.md`*

---

### Extensibility — 4 KPIs

| KPI | KPI Category | What it measures | Tool |
|---|---|---|---|
| **Clean core share** | Upgrade stability | % of custom code objects per clean core level (A/B/C/D) | ATC + custom dashboard |
| **Technical debt score** | Upgrade stability | Weighted score: P1×10 + P2×5 + P3×1 per object | ATC + custom dashboard |
| **Unused code share** | Operational risks | % of unused custom code objects | SCMON + SUSG |
| **Business modifications** | Operational risks | # of business modifications to SAP standard objects | RISE dashboard / SMODILOG |

Measurement type: Semi-automatic (clean core share, technical debt, unused code), Automatic (business modifications). Cadence: Weekly recommended.

> *Full per-KPI calculation detail: `clean-core-extensibility` skill → `knowledge/06-kpi-extensibility.md`*

---

### Data — 2 KPI Categories

| KPI Category | What it measures | Key metrics | Tool |
|---|---|---|---|
| **Data volume efficiency** | Efficiency of data volume management based on SAP Best Practices (DVM) | Outdated data, unused data, redundant data, optimized SAP HANA usage, custom table footprint | Early Watch Alert, SAP Readiness Check, DVM Workcenter |
| **Data quality** | Consistency and quality of data in chosen areas | Accuracy, completeness, consistency, timeliness, uniqueness, validity (weighted composite score) | Financial Data Quality app in SAP Readiness Check |

Measurement type: Semi-automatic. Cadence: Quarterly during transformation; twice per year at stable state.

> *Full per-KPI calculation detail: to be added to `clean-core-data` skill when ingested.*

---

### Integration — 4 KPIs

| KPI | KPI Category | What it measures | Tool |
|---|---|---|---|
| **Upgrade stability** | Upgrade stability | % of standard vs. traditional vs. custom interfaces in SAP S/4HANA | SAP Readiness Check |
| **Operational risk (expert tool monitoring)** | Operational risk | % of interfaces centrally monitored via SAP Application Interface Framework | SAP S/4HANA + SAP Readiness Check |
| **End-to-end integration monitoring** | Operational risk | Coverage of SAP Cloud ALM integration monitoring and alert notifications | SAP Cloud ALM |
| **Innovation adoption** | Innovation adoption | % of activated and used modern SAP integration technologies (7 technologies measured) | SAP BTP tools |
| **Agile decision-making (toolchain coverage)** | Agile decision-making | % of integration requirements managed through the integrated toolchain (Signavio, LeanIX, Integration Suite, Cloud ALM) | SAP Signavio + SAP LeanIX + SAP Integration Suite + SAP Cloud ALM |

Measurement type: Semi-automatic to Manual. Cadence: Quarterly to once per year depending on KPI.

> *Full per-KPI calculation detail: to be added to `clean-core-integration` skill when ingested.*

---

### Operations — 6 KPI Categories

| KPI Category | What it measures |
|---|---|
| **Software stack** | Age of FPS/SPS in months; compliance threshold = 24 months. Covers both innovation compliance and security compliance. |
| **Enable agility through integrated toolchain adoption** | % of integrated toolchain capabilities adopted across the full project lifecycle |
| **Adopt clean core requirements** | Aggregate score from all four dimension KPIs (40% weight on technical debt ratio; 15% each for Processes, Integration, Data, Extensibility) |
| **Continuously improve agile delivery and operational excellence** | Four sub-KPIs: Velocity (delivery speed/throughput), Quality (code/test health), Efficiency (lead time, deployment frequency), Reliability (MTTR, incident volume, system performance) |
| **Enduring operational efficiency** | Operations excellence (alert flooding, event management, business process performance) + System health (connectivity, exceptions, background processing, performance) |
| **Embed secure operations** | FPS/SPS lifecycle compliance (≤24 months) + % compliance with SAP secure baseline |

Measurement type: Automatic (software stack, operational efficiency) to Manual (toolchain adoption). Cadence: Daily to monthly.

> *Full per-KPI calculation detail: to be added to `clean-core-operations` skill when ingested.*

---

## Connection to Governance & Maturity

Every KPI includes a **"Governance & maturity relevance"** field pointing to the specific practice(s) from the Governance & Maturity Assessment most directly linked to that KPI's performance. This creates a closed feedback loop:

> Improve governance practice → better processes/tools/skills → measurable KPI improvement

The KPI deck is an integral part of the clean core measurement framework — it does not stand alone. Governance and maturity adoption are expected to drive continuous improvement in KPI performance over time.

---

## Key Reference Links

- Full KPI deck (external): https://dam.sap.com/mac/app/p/pdf/asset/preview/XbqgDc4?ltr=a&rc=10&doi=SAP1240359
- Governance & Maturity deck: https://dam.sap.com/mac/app/p/pdf/asset/preview/a5A7qyM?ltr=a&rc=10&doi=SAP1222195
- RISE with SAP Methodology dashboard: https://www.sap.com/products/erp/rise/methodology/clean-core.html
