# Clean Core KPI Measurement Framework – Business Processes

**Source:** SAP Clean Core Measurement Framework: KPIs (SAP1240359, v1.3 Final), Business Processes section

---

## Sources

| Topic | Source |
|---|---|
| All content in this file | Clean Core Measurement Framework: KPIs (SAP1240359, v1.3) — Business Processes section |
| Fit/gap classification | See also `knowledge/01-whitepaper-clean-core-processes.md` (whitepaper chapter on fit/gap) |
| Simplification Items context | SAP Readiness Check for SAP S/4HANA (OSS Note 2913617); SAP Readiness Check for SAP S/4HANA Upgrades (OSS Note 3059197) |

---

## Overview

The KPI framework for the Business Processes dimension focuses on measuring how well an organization follows SAP standard processes and the extent to which deviations are controlled and justified.

**Why Business Processes KPIs matter:**
- Achieve business agility by enabling adaptation of processes to business needs
- Reduce TCO by lowering customization, development, and maintenance costs, while also reducing system implementation time
- Increase business value by adopting innovations via frequent and less time-consuming upgrades
- Ensure process efficiency by leveraging standard SAP solution capabilities and limiting deviations to differentiating processes
- Minimize process deviations by aligning the target-state enterprise architecture with the SAP reference solution architecture

**Expected benefits:**
- Strategy enablement: Improve public cloud readiness (NQ)
- Business value: Improve process efficiency (Q); Ease of adoption of future innovations (NQ); Business value through frequent upgrades (Q)
- Risk mitigation: Reduce cybersecurity risk (NQ)
- IT spend effectiveness (TCO): Reduce system implementation and upgrade time (NQ); Reduce cost to develop and maintain customizations (Q); Reduce cost of upgrades (Q)

---

## Business Processes KPI Overview

| KPI Category | KPI | Metric | Tool |
|---|---|---|---|
| Process standardization | Process fit-to-standard alignment | % of processes fit to standard | SAP Signavio + SAP Cloud ALM |
| Process standardization | Process fit-to-standard alignment – gaps | % of processes with G-EP or G-EC gap deviations | SAP Signavio + SAP Cloud ALM |
| Process adaptation | Alignment to clean core | % of delta requirements aligned with clean core extensibility and integration guidelines | SAP Cloud ALM |
| Process adaptation | Alignment to SAP S/4HANA target architecture | # of adoption backlog simplification items from SAP Readiness Check | SAP Readiness Check |

**Measurement type:** Semi-automatic  
**Cadence:** Each process governance cycle (influenced by project phase)

---

## Requirement Classification (Fit/Gap Codes)

Delta requirements are classified using the following codes. These codes directly drive downstream treatment in the SSB and feed the KPI calculations.

| Type | Code | Classification | Definition |
|---|---|---|---|
| Fit | F-SC | SAP Content | SAP Best Practices, EML, or SAP Standard Content identified as a fit |
| Fit | F-VS | Software Vendor SaaS Applications | Software vendor applications as a fit outside of core (e.g. SAP Industry Cloud, SAP Ariba, SAP BTP apps, third-party SaaS) |
| Fit | F-EC | Extended configuration aligned to SAP Standard | Additional configuration settings or latest innovations (e.g. embedded AI, new modules) — aligned to standard |
| Gap | G-EC | Extended configuration not aligned to SAP Standard | Complex system maintenance / lack of system optimization leading to non-conformance to fit to standard (e.g. compatibility packs, over-configuration) |
| Gap | G-RP | Roadmap path to standard | Temporary gap where a SAP roadmap item will fulfill the requirement in the future |
| Gap | G-EP | Extensions: Process Deviation | Requirement to extend to meet specific process deviation from standard system behavior — requires business justification |
| Gap | G-EN | Extensions: Non-Process | Requirement to extend for project/business need not tied to process execution (e.g. conversion program, business report, output form) |
| Gap | G-AN | Machine Learning, RPA, Custom Innovation | Requirement to consume custom AI capabilities or build a solution/application as part of an innovation project |

**Note:** G-ET (Extensions: Temporary) also exists — a requirement temporary in nature, to be purged at a later point in the transformation journey.

---

## KPI Detail: Process Fit-to-Standard Alignment

**Objective:** Drive standardization of processes across the organization; reduce time and cost of deploying processes by reducing complexities; provide harmonized data as a foundation for decision-making.

**Key results:**
- Measure fit-to-standard processes in new implementation or transition to SAP Business Suite
- For system conversion and selective data transition, consider the KPI for all new capability scope deployed as part of pre-, during, and post-conversion activities

**Formula:**
```
% of processes fit to standard =
  1 – (# of processes with delta requirements / total # of processes in scope)
```

**Calculation details:**
- **Numerator:** Total number of processes with deviations that do not align with established SAP standard processes (SAP Best Practice / SAP Standard Content / partner process content built on SAP Best Practices)
- **Denominator:** Total number of processes in scope, as identified using the process scope definition for the customer

**Recommended tools:**
- Now: SAP Signavio Process Manager + SAP Cloud ALM
- Future: RISE with SAP Methodology Dashboard

**Prerequisites:** Usage of SAP Best Practices, standard content, or partner content built on SAP Best Practices

**Cadence:** Each process governance cycle (influenced by project phase)

**Measurement guidance:**
1. Set up SAP Signavio and SAP Cloud ALM and integrate them to replicate the BPMN master list
2. Import process decomposition
3. Assign each delta requirement to a process

**Type:** Semi-automatic (list of total processes gathered from SAP Signavio Process Manager; associated delta requirements from SAP Cloud ALM)

**Governance & maturity relevance:** Maturity of process deviation management (PRO-04)

---

## KPI Detail: Process Fit-to-Standard Alignment – Gaps

**Objective:** Same as above — drive process standardization and reduce complexity — but focused specifically on the more significant gap types (G-EP and G-EC).

**Context:** Delta requirements recorded in SAP Cloud ALM are classified. This KPI is based on the total number of processes with deviations classified as G-EP or G-EC, which indicate a **greater deviation from standard** than other gap types.

**Formula:**
```
% of processes fit to standard (gaps) =
  1 – (# of processes with delta requirements classified as G-EP or G-EC
       / total # of processes in scope)
```

**Calculation details:**
- **Numerator:** Total number of processes with deviations classified as G-EP (process deviation extension) or G-EC (extended configuration not aligned to SAP standard)
- **Denominator:** Total number of processes in scope

**Recommended tools:** SAP Signavio Process Manager + SAP Cloud ALM (same as above)

**Cadence:** Each process governance cycle

**Measurement guidance:** Same setup as Process Fit-to-Standard Alignment — Signavio + CALM integration required

**Type:** Semi-automatic

**Governance & maturity relevance:** Maturity of process deviation management (PRO-04)

---

## KPI Detail: Alignment to Clean Core

**Objective:** Measure how well the organization is aligned to clean core principles in its process design decisions.

**Context:** Delta requirements classified as G-EP are evaluated against the clean core extensibility and integration dimensions to determine whether the implementation is compliant. Delta requirements that are not clean core-compliant should be challenged to confirm whether they genuinely add business value. This KPI can be measured once the initial analysis of the extensibility solution design has been completed.

**Formula:**
```
% alignment to clean core =
  1 – (# of gaps not aligned with clean core
       / total # of delta requirements)
```

**Calculation details:**
- **Numerator:** Total number of gaps identified as either:
  - Selective G-EP extensions: process deviations not intended to be solved in a clean core manner (based on extensibility and integration guidelines)
  - G-EC: all configurations in relation to compatibility scope items
- **Denominator:** Total number of delta requirements

**Recommended tools:**
- Now: SAP Cloud ALM
- Future: RISE with SAP Methodology Dashboard

**Prerequisites:**
- Delta requirements must be captured and dispositioned into SAP-recommended fit/gap classification
- Initial disposition of G-EP required to identify Level C and D types of extensibility and integration compliance (e.g. non-allow-listed APIs)

**Cadence:** Each process governance cycle

**Measurement guidance:**
1. Set up SAP Signavio and SAP Cloud ALM and integrate them
2. Import process decomposition
3. Assign each delta requirement to a process; apply fit/gap classification
4. Identify G-EP items and assess their clean core compliance

**Type:** Semi-automatic

**Governance & maturity relevance:** Maturity of process deviation management (PRO-04)

---

## KPI Detail: Alignment to SAP S/4HANA Target Architecture

**Objective:** Achieve compliance with the SAP S/4HANA target architecture by resolving relevant simplification items.

**Context:** Simplification items document changes from older SAP ERP systems to SAP S/4HANA — functions changed, removed, or replaced. They explain what changed, why, and how to adapt or migrate. They are crucial for planning system conversions or upgrades, identifying necessary adaptations in custom code, configuration, and processes.

**Formula:**
```
% alignment to target architecture =
  1 – (# of adoption backlog simplification items
       / total # of simplification items in scope)
```

**Calculation details:**
- **Numerator (Backlog):** The subset of simplification items that can be resolved based on the current SAP S/4HANA release, or that can only be resolved after an upgrade to a higher release
- **Denominator:** Total number of simplification items in scope

**Recommended tools:**
- SAP Readiness Check for SAP S/4HANA (system conversions) — OSS Note 2913617
- SAP Readiness Check for SAP S/4HANA Upgrades — OSS Note 3059197

**Prerequisites:** Technical prerequisites described in OSS Notes 2913617 and 3059197

**Cadence:**
- **Regular:** Execute Readiness Check upon availability of a new SAP S/4HANA release or Feature Pack
- **Event-based:** For system conversions, new implementations, selective data transitions, system upgrades

**Measurement guidance:**
1. Fulfill technical prerequisites to execute SAP Readiness Check
2. Execute SAP Readiness Check
3. Verify findings, eliminating false positives
4. Analyze suggested solution options

**Type:** Semi-automatic (execution of SAP Readiness Check is automatic; interpretation of results is manual)

**Governance & maturity relevance:** Maturity of process management (PRO-02)

---

## Connection to Other Clean Core Principles

The Alignment to Clean Core KPI explicitly links the Business Processes and Extensibility/Integration dimensions:
- G-EP gaps (process deviations requiring extensions) are evaluated against clean core extensibility and integration guidelines
- A non-clean-core G-EP means the process deviation is being addressed via a Level C or D extension — driving extensibility KPI debt
- The SSB should govern both the process deviation decision and the extensibility/integration design decision together (see `knowledge/01-whitepaper-clean-core-processes.md` — SSB section)

In the RISE Dashboard clean core score, Business Processes KPIs carry a **15% weight** alongside Extensibility (40%), Integration (15%), and Data (15%) in the "Adopt clean core requirements" aggregate score.
