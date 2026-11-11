# Clean Core Extensibility — Governance & Maturity Assessment

> Source: Clean Core Measurement Framework — Governance and Maturity deck (2025)
> Scope: Extensibility dimension only (slides 25–52)

---

## Sources

When citing content from this file, link to the primary source. This is a publicly available SAP document hosted on the SAP Digital Asset Management (DAM) portal.

| Topic | Source | URL |
|-------|--------|-----|
| All content in this file | Clean Core Measurement Framework: Governance & Maturity (2025) | https://dam.sap.com/mac/app/p/pdf/asset/preview/a5A7qyM?ltr=a&rc=10&doi=SAP1222195 |
| Clean Core Extensibility context | SAP White Paper: Clean Core Extensibility (2025) | https://www.sap.com/documents/2024/09/20aece06-d87e-0010-bca6-c68f7e60039b.html |

---

## Overview

The Governance & Maturity assessment for **Extensibility** consists of **11 practices** split into two categories:

| Category | Practices |
|----------|-----------|
| **Governance Maturity** (EXT-GOV) | 6 practices scored 0–5 |
| **System Setup** (EXT-SYS) | 5 practices scored 0–5 |

The overall Extensibility score is derived from the individual practice scores. Assessment can be done at any point — before, during, or after a transformation.

### Result Structure (Slide 30)

| Category | Practices | Importance |
|----------|-----------|-----------|
| EXT-GOV-01 | Maturity of Governance Process for Extensions | High |
| EXT-GOV-02 | Maturity of Extension Architecture Guidelines | High |
| EXT-GOV-03 | Maturity of Development Guidelines | High |
| EXT-GOV-04 | Maturity of Developer Skills & Enablement | High |
| EXT-GOV-05 | Maturity of Measurements & KPIs | High |
| EXT-GOV-06 | Maturity of Housekeeping Practice | Medium |
| EXT-SYS-01 | Setup of Automated Code Checks | High |
| EXT-SYS-02 | Setup of Exemption Process | High |
| EXT-SYS-03 | Setup of ABAP Cloud Software Component | High |
| EXT-SYS-04 | Setup of Usage Data Collection | High |
| EXT-SYS-05 | Setup of SAP BTP Account | High |

---

## EXT-GOV-01: Governance Process for Extensions

**Why:** To ensure continuous governance throughout the extension process, it is important that the governance process is well-defined and starts already with the functional request, and is consistent through architectural design, implementation and deployment.

**Practice Summary:** This practice ensures robust governance of process deviations by documenting and managing extension requests throughout their lifecycle, validates business necessity, enforces architecture and approval standards, accommodates changes, and thoroughly records decisions and technical debt, all under expert review.

**Key dimensions assessed:**
- **Continuity**: Existence and completeness of a documented, end-to-end governance process for extension lifecycle (from request to deployment)
- **Guidance**: Availability of structured guidance for selecting appropriate extension architecture and models (incl. SAP Extension Methodology)
- **Standardization**: Use of standardized criteria and documented reasoning (decision assets for justification of architectural choices)
- **Approval Process**: Presence of formal, board-linked approval processes for extensions (incl. handling exceptions like modifications)
- **Documentation**: Consistency in recording decisions, approvals, justifications, and technical debt

**Evaluation Criteria:**
1. Is there a continuous governance process (incl. documentation) defined through the complete extension process, from functional request over designing the extension architecture, implementation until deployment?
2. Is there a governance process (e.g., based on a Solution Standardization Board (SSB)) in place that ensures extensions are only created aligned with a business case and process mapping?
3. In this governance process, are there different approval levels considered based on the target architecture (e.g., for an extension planned with a technical modification, you need to have the buy-in from the CTO)?
4. Is there a well-defined process in place in case of changes to the initial plan during development? Is there reiteration included in the process (or at least documentation of deviation, e.g., a missing field in an API leads to demotion from "clean" to "unclean")?
5. Is there a documentation of decisions on technical architecture (and technical debt) after decision in the SSB?
6. Is there a peer review process in place, especially to ensure that the extension domain is chosen based on the use case — and not based on a single biased architect?

**Maturity Rating Guidance:**

| Rating | Short Description | Long Description |
|--------|------------------|-----------------|
| 0 – Not Started | No governance process | No formal process exists for managing or documenting process deviations or extensions. |
| 1 – Beginner | Ad hoc and undocumented | Sporadic, inconsistent handling of extensions with minimal or undocumented governance, justification, and technical oversight. |
| 2 – Intermediate | Basic documented process | Some documentation and defined steps exist, but business case validation and architectural review are partial or not consistently applied. |
| 3 – Proficient | Consistent and documented governance | End-to-end extension process governance is documented and repeatable, with approval processes and architectural review applied in most cases. |
| 4 – Advanced | Proactive with differentiated review | Extensions are only approved with clear business justification; approval levels, architectural reviews, and technical debt are actively managed and documented. |
| 5 – Expert | Comprehensive and adaptive governance | Fully integrated, adaptive process with continuous improvement; all decisions are reviewed, documented, and updated with changes, involving expert oversight. |

---

## EXT-GOV-02: Extension Architecture Guidelines

**Why:** In order to evaluate the best technical architecture, you ideally have architecture guidelines in place that recommend "cleaner" options over "uncleaner" ones and facilitate a suitable choice between on-stack or side-by-side extensions.

**Practice Summary:** This practice ensures consistent and high-quality extension architecture by establishing comprehensive guidelines, favouring cleaner options (like Level A on-stack or side-by-side extensions), and basing extension domain choices on documented, objective criteria. It links guidance to governance processes, enforces the use of released APIs, and mandates thorough documentation and control over architectural decisions and exceptions.

**What good guidelines include:**
- Standardized guidelines prioritizing side-by-side extensions via SAP BTP and ABAP Cloud for on-stack developments
- Ensures use of released APIs and defines processes for exceptions
- Incorporates automated code checks and supports modern development technologies
- Documents code review and exemption processes for unreleased SAP objects
- Outlines procedures for managing deviations and mitigating missing APIs

**Evaluation Criteria:**
1. Is there guidance implemented that ensures consistency, e.g., based on the SAP Application Extension Methodology?
2. Is there a structured guidance in place to guide architects into the best extension architecture for a given use case, e.g., based on the SAP Application Extension Methodology?
3. Is the clean core level concept considered and the cleanest option set as a target whenever possible?
4. Is the extension domain (on-stack or side-by-side) chosen based on your extension use case? Is there a general decision asset available, pointing out reasons to use either extension domain?
5. Is there guidance for architects into selecting released APIs (local or remote) wherever possible? Does it include mandatory steps for documentation in case of missing APIs (e.g., Influence Request to SAP)?
6. Is there an extension approval process established in your governance board that is linked to your guidelines (e.g., choosing a modification needs approval from central architecture board; classic user exit only from local architect)?
7. Is there a standardized documentation approach of the approvals, justifications and technical debt in the planning process?

**Maturity Rating Guidance:**

| Rating | Short Description | Long Description |
|--------|------------------|-----------------|
| 0 – Not Started | No guidance or process | No extension architecture guidelines are in place; no standardized process for extension decisions or documentation exists. |
| 1 – Beginner | Ad hoc, basic awareness | Some informal or ad hoc practices; partial awareness of SAP extension models and clean core principles, but not institutionalized. |
| 2 – Intermediate | Basic guidance, partially applied | Guideline drafts exist; some considerations of Level A extensions and released API usage, but inconsistent application and lacking robust governance. |
| 3 – Proficient | Consistent, documented guidelines | Documented guidance in place; adherence to Level A extensions and released APIs; governance and documentation processes exist but have some gaps or exceptions. |
| 4 – Advanced | Comprehensive, enforced governance | Guidelines are comprehensive, consistently followed, and enforced; strict governance and exception processes; thorough documentation of decisions. |
| 5 – Expert | Fully optimized, integrated best practices | Guideline usage is fully embedded in processes; objective domain choice, stringent API use, proactive governance, continuous improvements and best-in-class. |

---

## EXT-GOV-03: Development Guidelines

**Why:** It is important to ensure and guide developers to stick with the architecture as planned — and to offer a documented process in case of deviations from the architectural plan. This way, unnecessary technical debt can be avoided.

**Practice Summary:** Comprehensive development guidelines ensure that ABAP Cloud is prioritized, mandate the use of released APIs, and support modern SAP technologies. They provide documented processes for exceptions, code reviews, and the use of unreleased objects to minimize technical debt and enforce architectural standards. Automated checks are aligned with these guidelines, ensuring consistent adherence and process transparency.

**Evaluation Criteria:**
1. Is ABAP Cloud set as default for on-stack developments?
2. Is the usage of released APIs prioritized in the guidelines (both on-stack and side-by-side)?
3. Is a process in place on how to mitigate missing APIs or what exceptional cases allow the usage of classic extensibility?
4. Do the guidelines refer to automated code checks based on ABAP Cloud? Is the check described in there aligned with the guidelines' content?
5. Is an exemption process described in case of usage of unreleased SAP objects?
6. Is there a code review process established?
7. Is the development guideline covering modern development technologies, e.g., RAP, UI5, Fiori (Elements), CAP, etc.?

**Maturity Rating Guidance:**

| Rating | Short Description | Long Description |
|--------|------------------|-----------------|
| 0 – Not Started | No guidelines or processes | No documented development guidelines exist, nor are processes or reviews in place relating to ABAP Cloud or architecture compliance. |
| 1 – Beginner | Basic, ad hoc guidelines | Guidelines are informal or incomplete; little focus on ABAP Cloud or modern tech; exception and review processes are missing or not enforced. |
| 2 – Intermediate | Partial guidelines established | Some guidelines reference ABAP Cloud and API usage; processes for exceptions exist but are inconsistent or lack automation and coverage of modern tech. |
| 3 – Proficient | Comprehensive, mostly aligned | Development guidelines comprehensively cover ABAP Cloud, API usage, exemptions, reviews, and some modern tech; automated checks are described but not fully enforced. |
| 4 – Advanced | Fully documented and enforced | Guidelines are fully documented, aligned with architecture, cover all modern tech, enforced with automated checks and formal processes, including regular code reviews. |
| 5 – Expert | Continual improvement and leading | Guidelines are continuously improved; all processes are automated and optimized, aligned with best practices; proactive management of deviations and easy adaptation to change. |

---

## EXT-GOV-04: Developer Skills & Enablement

**Why:** Developers need to be enabled in modern extension technologies to achieve the cleanest implementations possible. Certification can act as an indicator to ensure developers do not create technical debt because of missing knowledge.

**Practice Summary:** This practice measures how well developer teams are equipped and enabled for clean core development using SAP BTP and ABAP Cloud. It covers team experience, formal certifications, ongoing enablement plans, and hiring criteria, ensuring that both internal and external developers possess the modern skills needed to minimize technical debt and implement clean extensions.

**Evaluation Criteria:**
1. Do your (lead) developers have experience in SAP BTP based development?
2. Do your (lead) developers have experience with ABAP Cloud — especially for on-stack developments?
3. What is the share of certified developers and technical architects in your project?
4. Is there an enablement plan set up to enable developers on ABAP Cloud and SAP BTP development accordingly?
5. If external developers are considered, is the qualification on ABAP Cloud or even the certification considered as a factor to choose the best developers? Is it set up as a requirement for lead developers?

**Maturity Rating Guidance:**

| Rating | Short Description | Long Description |
|--------|------------------|-----------------|
| 0 – Not Started | No enablement or skills present | No SAP BTP/ABAP Cloud skills, certifications, or enablement plans exist among any developers. |
| 1 – Beginner | Minimal skills, ad hoc experience | Few developers have basic experience or exposure; no formal enablement or certification in place. |
| 2 – Intermediate | Some skills, limited enablement | Several developers have hands-on experience; enablement is informal, few certifications available. |
| 3 – Proficient | Defined enablement, growing skills | Enablement plan exists, regular upskilling; noticeable share of certified staff and skills coverage. |
| 4 – Advanced | Advanced, integrated enablement | Most developers are skilled and certified, enablement is proactive and structured, hiring is skills-based. |
| 5 – Expert | Expert, certification-driven team | Team is fully certified and highly experienced; enablement is continuous, and certification is mandatory for key roles. |

---

## EXT-GOV-05: KPIs & Measuring

**Why:** System KPIs need to be defined and measured regularly to match the system reality with the expectation of technical debt based on the target architecture for extensions. At the same time, KPIs can help identify areas of improvement.

**Practice Summary:** This practice evaluates whether system KPIs are systematically defined, measured, and used to set and monitor objectives related to technical debt and extensibility. It assesses the alignment of KPIs with management goals, their integration into individual targets, and their coverage of critical extensibility metrics, ensuring that KPIs drive continuous improvement.

**Evaluation Criteria:**
1. Are system KPIs defined and measured regularly to identify the current state of your system?
2. Are goals actively defined based on the KPIs (e.g., reduction of technical debt score of 10% in the next year)? Are these goals aligned with the management level?
3. Is there a clear link between KPIs and the success in achieving goals on KPIs with developers'/architects' targets and goals?
4. Are the KPIs considering different aspects around extensibility, e.g., amount of business modifications or technical debt score?

**Maturity Rating Guidance:**

| Rating | Short Description | Long Description |
|--------|------------------|-----------------|
| 0 – Not Started | No KPIs defined or tracked | System KPIs are not defined, measured, or used; no link to goals or improvement. |
| 1 – Beginner | KPIs considered, not consistently tracked | Some KPIs are informally discussed or tracked, but not regularly measured or connected to goals. |
| 2 – Intermediate | KPIs defined, basic tracking | Key KPIs are defined and measured; goals may exist but lack alignment with management or teams. |
| 3 – Proficient | Regular measurement, partially aligned | KPIs are measured regularly and used for setting goals partially aligned with management and teams. |
| 4 – Advanced | KPIs linked to goals and targets | KPIs are central to improvement; goals are fully aligned with management and individual targets. |
| 5 – Expert | Integrated and full coverage of extensibility | KPIs comprehensively cover extensibility, are managed systematically, and drive continuous improvement. |

---

## EXT-GOV-06: Housekeeping

**Why:** It is important to regularly do housekeeping (e.g., retirement of unused code) to avoid security risks and technical debt in your system which is no longer needed. Additionally, general code checks and continuous quality improvement are recommended.

**Practice Summary:** This practice ensures systematic housekeeping by regularly reviewing code usage and conducting code checks to identify and remove unused or faulty code. Timely actions and continuous improvement are implemented to minimize technical debt, helping maintain a healthy, sustainable, and high-quality codebase.

**Evaluation Criteria:**
1. Do you consider usage data regularly to retire unused code?
2. Do you run regular code checks and create actions out of the results (e.g., to tackle all errors over a given timeframe)?

**Maturity Rating Guidance:**

| Rating | Short Description | Long Description |
|--------|------------------|-----------------|
| 0 – Not Started | No housekeeping activities | No practice exists for code housekeeping or code checks; unused code remains unaddressed. |
| 1 – Beginner | Ad hoc housekeeping, no regular checks | Housekeeping or code checks happen sporadically and only in reaction to issues, not proactively. |
| 2 – Intermediate | Irregular checks, limited action | Some code checks and usage reviews are performed, but actions are inconsistently tracked/taken. |
| 3 – Proficient | Regular checks, actions tracked | Code checks and usage analyses occur regularly; most issues and unused code are actioned. |
| 4 – Advanced | Systematic housekeeping, improvement plans | Housekeeping is systematic; corrective actions are tracked and planned in a timely, consistent way. |
| 5 – Expert | Proactive and continuous improvement | Housekeeping is fully integrated, with continuous improvement and proactive retirement of unused code. |

---

## EXT-SYS-01: Automated Code Checks

**Why:** To live up to your guidelines it is crucial to also follow up on an operational level. Automated checks (SAP recommends ABAP Test Cockpit — ATC) are the recommended way to ensure the code is following your guidelines.

**Practice Summary:** Automated code checks with ATC are established to enforce coding and architecture guidelines, supporting clean core and ABAP Cloud principles. This includes defining and aligning default check variants, performing regular checks, and mandating checks during transport releases to ensure compliance and code quality across the development lifecycle.

**Evaluation Criteria:**
1. Is there a default ATC check variant set up? Does it align with your development and architecture guidelines?
2. Is the default ATC check variant considering clean core and ABAP Cloud?
3. Are regular checks with ATC set up in your system?
4. Is ATC set up as mandatory check upon transport release (as information or error)?

**Maturity Rating Guidance:**

| Rating | Short Description | Long Description |
|--------|------------------|-----------------|
| 0 – Not Started | No automated checks | No ATC check variants are defined or used; code is not systematically checked for guideline compliance. |
| 1 – Beginner | Basic ATC setup | Some ATC checks are run manually or ad-hoc, but default variants are missing or not aligned to guidelines. |
| 2 – Intermediate | ATC variants defined, partial alignment | Default ATC check variants exist and are occasionally used; partial alignment with guidelines; not fully mandatory. |
| 3 – Proficient | Regular ATC checks, guideline alignment | Default ATC check variants are well-defined, aligned with guidelines, and regular checks are performed. |
| 4 – Advanced | Mandatory ATC checks, clean core included | ATC checks (including clean core and ABAP Cloud) are mandatory on transport release, enforced as informational warnings. |
| 5 – Expert | Fully enforced, error-level, continuous review | ATC checks strictly enforced on transport release as errors, including continuous updates and full guideline coverage. |

---

## EXT-SYS-02: Exemption Process

**Why:** The quality of the exemption process is important as lead developers should be able to review exemptions. This is only possible if the number of exemptions is manageable. Exemptions should only be granted in unavoidable cases.

**Practice Summary:** A robust exemption process for ABAP Test Cockpit ensures manageable quality control by assigning appropriate approvers, enforcing timely limitations, and discouraging broad, package-wide exemptions. This approach keeps technical debt under control and aligns with Clean Core governance by making finding-level exemptions the default and regularly reviewing all granted exemptions.

**Evaluation Criteria:**
1. Are exemptions in place in general?
2. Are the approvers for exemptions configured according to the governance process?
3. Are timely limitations (e.g., until a standard API is released) regularly or mandatorily used in the exemption process?
4. Are there rules on object- or package-wide exemptions in place? Are exemptions on finding level the default?

**Maturity Rating Guidance:**

| Rating | Short Description | Long Description |
|--------|------------------|-----------------|
| 0 – Not Started | No exemption process | No exemption process in place; exemptions are unmanaged and approvals or limitations are not defined. |
| 1 – Beginner | Basic setup, ad-hoc approaches | Exemptions are set up for basic use; ad-hoc approvals without clear governance or time limitations; package-wide exemptions common. |
| 2 – Intermediate | Process defined, limited governance | Exemptions exist with some guidelines; approvers are partially defined/transparent, but time limits and scope rules are inconsistently applied. |
| 3 – Proficient | Standard process, governance mostly followed | Well-defined exemption process; approvers assigned, time limits commonly used, and finding-level exemptions are standard practice. |
| 4 – Advanced | Proactive governance, limited generic use | Exemptions strictly governed; time limits regularly enforced, package-wide exemptions rare and well-documented; processes regularly reviewed. |
| 5 – Expert | Optimized, fully controlled with continuous improvement | Exemption process fully controlled, optimized, and continuously improved; finding-level only, strict governance, and transparent oversight. |

---

## EXT-SYS-03: Setup of ABAP Cloud Software Component

**Why:** The utilization of ABAP Cloud objects in your system can be enforced by creating a separate software component that only and exclusively allows the usage of language version "ABAP for Cloud development".

**Practice Summary:** This practice aims to enforce the ABAP Cloud development paradigm by setting up a dedicated software component, establishing a transparent package structure. Through strict authorization measures and clear separation of responsibilities, it supports clean core principles and sustainable management of technical debt and legacy code.

**Evaluation Criteria:**
1. Is a separate software component set up to enforce the usage of "ABAP Cloud" in new developments?
2. Has a clear package structure been set up to identify "wrapper" objects and to distinguish between approved technical debt and legacy code?
3. Is the clean core level concept enforced by the usage of separate authorization for developers (e.g., only senior developers or internals are allowed to use classic APIs or internal objects)?

**Maturity Rating Guidance:**

| Rating | Short Description | Long Description |
|--------|------------------|-----------------|
| 0 – Not Started | Not started | No separation or enforcement; all developments done in classic ABAP environment. |
| 1 – Beginner | Initial awareness | Some awareness; ad-hoc efforts but no structural changes or enforcement. |
| 2 – Intermediate | Basic structure | Separate component/package exists, but enforcement is inconsistent or incomplete. |
| 3 – Proficient | Defined and enforced | Structured separation and partial enforcement; some controls and authorization. |
| 4 – Advanced | Managed and measurable | Strict separation, well-defined authorization, and enforced package structure. |
| 5 – Expert | Optimized & institutionalized | Full enforcement by using authorizations, separate software components and a well-aligned package structure. |

---

## EXT-SYS-04: Usage Data Collection

**Why:** Setting up usage data collection is crucial to identify unused extensions and custom objects as well as heavily used ones. The usage logging tools leverage the full power of the RISE with SAP Methodology Dashboard.

**Practice Summary:** Implementation of comprehensive usage data collection and dashboarding ensures effective identification and management of custom code usage, leveraging SAP tools like SCMON, SUSG, and the RISE with SAP Methodology Dashboard in Cloud ALM. This setup lays the foundation for clean core initiatives by providing reliable insights and actionable metrics on custom extension utilization.

**Evaluation Criteria:**
1. Is usage data collection with SCMON (or UPL) activated?
2. Is the aggregation of the usage data active (either in CCLM with Solution Manager or — preferably — with transaction SUSG in production)?
3. Are the custom-code related online collectors of SAP Early Watch Alert activated and running?
4. Is the RISE with SAP Methodology Dashboard used in SAP Cloud ALM? Is it technically running and are the relevant users assigned to access the dashboard?

**Maturity Rating Guidance:**

| Rating | Short Description | Long Description |
|--------|------------------|-----------------|
| 0 – Not Started | No setup | No usage data collection or dashboards are set up or in use. |
| 1 – Beginner | Initial activation | Some tools are known; limited or no activation of SCMON/UPL and dashboards. |
| 2 – Intermediate | Partial setup | Some components (e.g., SCMON/UPL or aggregation) are activated, but not all collectors/dashboards are active. |
| 3 – Proficient | Basic operational setup | Most collectors and dashboards are running; some gaps in user access or automation remain. |
| 4 – Advanced | Nearly complete data & dashboarding | All usage data collection and dashboards are set up and running; minor improvements possible. |
| 5 – Expert | Fully integrated & utilized | Complete, automated setup with all collectors, aggregations, and dashboards; data is regularly reviewed and acted upon. |

---

## EXT-SYS-05: Setup of SAP BTP Account

**Why:** Side-by-side extensions decouple by design, therefore the general availability of a side-by-side enabled setup indicates a "cleaner" landscape. While not every extension needs to run side-by-side, a missing setup might indicate that SAP BTP is not yet considered as a serious option for extensions.

**Practice Summary:** The practice assesses whether SAP Business Technology Platform (BTP) is established and integrated as a core part of the extension landscape. Evaluation covers the platform's setup, operational governance, backend integration, enablement of multiple development environments (low-code/no-code, pro-code), and actual use in extension projects. A higher maturity rating reflects not only foundational setup but also operational adoption and development activity on BTP.

**Evaluation Criteria:**
1. Is SAP BTP generally set up and available in the extension landscape?
2. Has an operational model (e.g., sub-account structure and clear responsibility) for SAP BTP been set up?
3. Is there a concept for connection between SAP BTP and the backend systems?
4. Have the low-code/no-code and pro-code environments already been provisioned and used in prototypes, pilots or productive extensions?
5. Are developments already happening on SAP BTP?

**Maturity Rating Guidance:**

| Rating | Short Description | Long Description |
|--------|------------------|-----------------|
| 0 – Not Started | BTP not set up | SAP BTP is not set up or available for any extension use; not considered in the extension landscape. |
| 1 – Beginner | Initial setup only | SAP BTP is minimally set up but lacks operational model, integration, and active usage. |
| 2 – Intermediate | Basic setup and planning | BTP is set up with some governance or integration concepts, but limited enablement or development usage. |
| 3 – Proficient | Setup and partial operation | BTP operational model is in place; some connections and environments established; development initiated. |
| 4 – Advanced | Operational and in use | BTP is fully set up, connected to backend, environments provisioned, and multiple projects utilize it. |
| 5 – Expert | Fully integrated and adopted | BTP is deeply integrated, operational, and widely adopted; significant solutions are developed and live. |
