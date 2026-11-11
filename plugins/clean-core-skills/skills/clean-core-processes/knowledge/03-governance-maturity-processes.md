# Governance & Maturity Assessment – Business Processes

**Source:** SAP Clean Core Governance & Operational Practices Maturity Assessment (SAP1222195, v2.0, May 2026), Business Processes section

---

## Sources

| Topic | Source |
|---|---|
| All content in this file | SAP1222195 — Clean Core Governance & Operational Practices Maturity Assessment v2.0 (May 2026), PRO-01 through PRO-05 |
| Cross-principle framework overview | `clean-core-general` skill → `knowledge/04-governance-maturity-framework.md` |

---

## Overview

The Business Processes dimension has **5 practices (PRO-01–05)**, organized around the end-to-end toolchain (Enterprise Architecture → Business Process Management → Application Lifecycle Management) and the governance structures that keep process decisions clean.

The overall maturity scale is **0–5** across all practices:

| Rating | Short label |
|---|---|
| 0 | Not Started / Not Considered |
| 1 | Beginner |
| 2 | Intermediate |
| 3 | Proficient |
| 4 | Advanced |
| 5 | Expert |

**Running the assessment:** A governance maturity assessment — even with just the 19 questions across PRO-01–05 — is a practical first engagement step with a customer. It creates a structured conversation about where the customer wants to be in 12 months given their resource constraints, and identifies 2–3 priority focus areas.

---

## PRO-01: Enterprise Architecture Management

**Core rationale:** The clean core business process principle recommends setting up an end-to-end toolchain connecting Enterprise Architecture Management (EAM) with Business Process Management (BPM) and Application Lifecycle Management (ALM).

**Evaluation criteria questions:**
1. Has Enterprise Architecture Management been set up as a separate practice?
2. Have you defined a target (North Star) architecture for your enterprise which includes business capabilities, data, applications, and technology architecture?
3. Have you set up a transition roadmap to this target architecture?
4. Are you using software tools to support Enterprise Architecture?
5. Have you integrated EAM tools with Business Process Management (BPM) and Application Lifecycle Management (ALM) tools?

**Maturity levels:**

| Rating | Short Description | Full Description |
|---|---|---|
| **0 — Not Started / Not Considered** | Ad hoc or informal EAM activity | No EAM practice, target architecture, or supporting tools are in place or considered. |
| **1 — Beginner** | Initial EAM structure with basic architecture defined | EAM activities are sporadic or informal; limited architecture documentation and no clear transition roadmap. |
| **2 — Intermediate** | Standard EAM with defined architecture and tools | EAM basics exist; a target architecture and initial roadmap may be defined, but integration and tool use are limited. |
| **3 — Proficient** | Integrated EAM with BPM/ALM and strategic roadmap | EAM is established, a target architecture and roadmap are in place, and supporting tools are used consistently. |
| **4 — Advanced** | Fully optimized, enterprise-wide EAM | EAM is mature with tool integration across BPM/ALM and a well-defined, regularly updated transition roadmap. |
| **5 — Expert** | Continuously evolving, fully integrated EAM | EAM is fully integrated, tools are seamlessly connected to BPM/ALM, and the architecture continually evolves with business needs. |

**Recommended tool:** SAP LeanIX (Application Portfolio Management, Architecture and Road Map Planning)

---

## PRO-02: Business Process Management

**Core rationale:** The clean core business process principle recommends setting up an end-to-end toolchain connecting Enterprise Architecture Management (EAM) with Business Process Management (BPM) and Application Lifecycle Management (ALM).

**Evaluation criteria questions:**
1. Has Business Process Management (BPM) been set up as a separate practice?
2. Have you defined your functional processes based on SAP best practices (sub-process level)?
3. Have you defined your end-to-end processes based on the functional processes (sub-process level) and linked the processes to your end-to-end processes?
4. Have you defined KPIs for measuring process efficiency and track those on a regular basis?
5. Are you regularly executing either SAP Readiness Check for S/4HANA or SAP Readiness Check for SAP S/4HANA upgrades to verify which simplification items and compatibility scope items you can take action on?
6. Are you using software tools to support BPM?

**Note:** Guidance is not applicable for criterion 5 (SAP Readiness Check execution).

**Maturity levels:**

| Rating | Short Description | Full Description |
|---|---|---|
| **0 — Not Started / Not Considered** | No BPM practice or processes defined | No BPM practice, process definitions, KPIs, or supporting tools in place or considered. |
| **1 — Beginner** | Informal BPM activities and basic awareness | BPM activities are ad hoc or informal, with limited or no consistent process or KPI definitions. |
| **2 — Intermediate** | Basic BPM structure with some process documentation | Initial BPM practices are established; some processes and KPIs are defined but not fully comprehensive. |
| **3 — Proficient** | Standard BPM and KPIs tracked for key processes | BPM is established with clear SAP-aligned processes, regular KPI tracking, and some use of supporting tools. |
| **4 — Advanced** | Integrated BPM supported by tools and regular reviews | BPM and KPI measurement are fully integrated with software tools, covering most processes with regular reviews. |
| **5 — Expert** | Optimized, holistic BPM with continuous improvement | Comprehensive BPM with end-to-end integration, automated tracking, and ongoing process optimization. |

**KPI linkage:** Alignment to SAP S/4HANA Target Architecture (PRO-02 → KPI 4 in `knowledge/02-kpi-processes.md`)

**Recommended tools:** SAP Signavio Process Manager, SAP Signavio Process Navigator, SAP Cloud ALM

---

## PRO-03: Application Lifecycle Management

**Core rationale:** The clean core business process principle recommends setting up an end-to-end toolchain connecting Enterprise Architecture Management (EAM) with Business Process Management (BPM) and Application Lifecycle Management (ALM).

**Evaluation criteria questions:**
1. Has Application Lifecycle Management (ALM) been set up as a separate practice?
2. Are new technical requirements documented in ALM tools to support management of solution changes?
3. Are business requirements linked to technical requirements in ALM tools, describing how the approved business requirements will be realized?
4. Have you linked business requirements to a business process master list (BPML)?
5. Have you set up test management methods and tools based on end-to-end processes?

**Maturity levels:**

| Rating | Short Description | Full Description |
|---|---|---|
| **0 — Not Started / Not Considered** | No ALM practice or linkage established | No ALM practice; requirements, changes, or processes are not documented or managed in a structured manner. |
| **1 — Beginner** | Informal or inconsistent ALM usage | ALM processes and tools are used inconsistently; limited documentation and no systematic traceability. |
| **2 — Intermediate** | Basic ALM setup and partial requirement tracking | ALM set up for technical requirements, but business-process links and end-to-end test management are limited or manual. |
| **3 — Proficient** | Standardized ALM with business-technical traceability | Requirements routinely documented in ALM, with some linkage to business processes and organized test management. |
| **4 — Advanced** | Integrated ALM and process/test management | Robust ALM with systematic linkage between business/process and technical requirements, plus comprehensive test management. |
| **5 — Expert** | Fully connected, optimized ALM and process governance | Mature ALM practice with end-to-end traceability, full linkage to BPML, and optimized process/test governance. |

**Recommended tools:** SAP Cloud ALM (requirements management, delta requirements triage, testing), Tricentis

---

## PRO-04: Process Deviations Management

**Core rationale:** The clean core business process principle recommends establishing guidelines for governing process enhancements and improvements.

**Evaluation criteria questions:**
1. Do you have a standardized way to record process deviations via delta requirements describing who needs it, what is needed, and why it is needed (describe the value gain)?
2. Do you perform an impact analysis to minimize deviation from SAP standard processes, with documented business justifications for deviations and impact on other clean core principles?
3. Have you set up a steering and governance process as part of a Solution Standardization Board for process deviations with stakeholders from architecture, business, and solutioning teams?
4. Do you set up a back-to-standard plan in case the process gap is addressed by a future product roadmap item, as part of the overall enterprise architecture to reduce technical debt from interim and workaround solutions?

**Maturity levels:**

| Rating | Short Description | Full Description |
|---|---|---|
| **0 — Not Started / Not Considered** | No process deviation strategy | No standardized way to record, analyze, justify, or manage process deviations; no governance or decision-making process established. |
| **1 — Beginner** | Basic recording of deviations | Basic recording of process deviations without systematic impact analysis or comprehensive business justification; limited governance process. |
| **2 — Intermediate** | Initial impact analysis and documentation | Initial implementation of impact analysis and documentation for deviations; basic consideration of integration and technical implications; limited steering governance. |
| **3 — Proficient** | Comprehensive deviation management | Comprehensive analysis and documentation of deviations, including market, legal, and compliance needs; established governance process; consideration of clean core and integration impacts. |
| **4 — Advanced** | Integrated governance and strategic alignment | Integrated steering governance; strategic alignment on SAP standard processes with documented back-to-standard plans; decision-making at business level considering architecture principles. |
| **5 — Expert** | Full adherence and proactive management | Full adherence to Solution Standardization Board guidelines; proactive management; robust justification and clean core principles; actively mitigates technical debt and plans for future product inclusion. |

**KPI linkage:** Process Fit-to-Standard Alignment, Process Fit-to-Standard Alignment – Gaps, Alignment to Clean Core (all three KPIs in `knowledge/02-kpi-processes.md` link to PRO-04)

**Recommended tools:** SAP Cloud ALM (delta requirements), SAP Signavio Process Manager

---

## PRO-05: Organization Transformation Readiness

**Core rationale:** The clean core business process principle recommends defining roles and responsibilities as part of a process transformation office (or similar instance driving the success of business process transformation).

**Evaluation criteria questions:**
1. Is organizational change management (OCM) on projects centrally organized, applied in a standard structured way with continuous improvement, and does it have a mandate and resources to execute?
2. Is the business structurally involved in the creation and execution of the target enterprise architecture (EA) and transition roadmap?

**Maturity levels:**

| Rating | Short Description | Full Description |
|---|---|---|
| **0 — Not Started / Not Considered** | Profound disconnect between IT and the business | Business is not involved in defining a target EA. IT projects happen on an ad-hoc basis without consideration of architectural principles. The business believes IT should own projects, which often fail since OCM is limited to training and basic communication. |
| **1 — Beginner** | Business participates in planning but does not commit to execution | The business participates in defining the target EA, but architectural principles are often ignored in practice. Business does not commit to a roadmap; project priorities change regularly. Ownership of projects by the business is almost non-existent. |
| **2 — Intermediate** | Business participates and largely commits, but architectural principles are sometimes overruled | The business participates in defining the target EA and accepts IT's role in defining architectural principles, but overrules them when in disagreement. Aligned on roadmap but ad-hoc projects still happen. Ownership of key projects is pro-forma; OCM regularly struggles to get the business on board. |
| **3 — Proficient** | Business collaborates with IT and owns project execution; accepts IT's role to safeguard the EA | The business and IT collaborate on the target EA and are aligned on the roadmap. Architectural principles are in place, but exceptions happen. The business generally feels ownership of key projects; OCM deals effectively with stakeholders. |
| **4 — Advanced** | Business and IT co-own planning; business leads execution; EA is future-proof based on mutually agreed principles | The business participates in defining architectural principles and commits to them. They co-own the target EA and are fully aligned on the roadmap at all hierarchical levels. The business owns all key projects; OCM is very effective. |
| **5 — Expert** | Business sees IT as a partner for innovation; drives planning and execution of projects | The business sees IT as a key enabler for innovation and understands the need for architectural principles to manage complexity. They drive the definition of the target EA and roadmap in full collaboration with IT. OCM is largely needed only for training and communication. |

---

## Connections Between Practices

The five PRO practices form an integrated chain:
- **PRO-01 (EAM)** defines the target architecture and roadmap that frames all process decisions
- **PRO-02 (BPM)** establishes the ongoing practice of process management, measurement, and improvement
- **PRO-03 (ALM)** ensures requirements and test management are systematically linked to processes
- **PRO-04 (Process Deviations)** governs what deviations are allowed and ensures they are justified and tracked
- **PRO-05 (Org Readiness)** ensures the organization is actually set up to drive and own the transformation

**Without PRO-05**, even perfect toolchain setup (PRO-01–03) and governance design (PRO-04) will fail — executive ownership and OCM are prerequisites for any of the other practices to function sustainably.
