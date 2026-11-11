# Clean Core Integration — Governance & Maturity

**Source:** Governance & Maturity Assessment Deck (SAP1222195 v2.0) — Integration section (Slides 65–80)  
**Ingested:** 2026-09-13  
**Purpose:** Full per-practice evaluation criteria and 0–5 maturity rating guidance for all 6 Integration G&M practices (INT-01 through INT-06).

---

## Practices Overview

### Result Table (Slide 68)

| Practice | Practice ID | Importance | Current Score | Target Score |
|---|---|---|---|---|
| Maturity of Integration Strategy | INT-01 | Medium | \<0–5\> | \<0–5\> |
| Maturity of Integration Governance Process | INT-02 | High | \<0–5\> | \<0–5\> |
| Maturity of Integration Landscape | INT-03 | High | \<0–5\> | \<0–5\> |
| Maturity of Tool Chain | INT-04 | Medium | \<0–5\> | \<0–5\> |
| Maturity of SAP S/4HANA Integration Readiness | INT-05 | High | \<0–5\> | \<0–5\> |
| Maturity of Operational Framework | INT-06 | High | \<0–5\> | \<0–5\> |

---

## Practices Overview — Why and What

### INT-01/02: Strategy and Governance (Slide 66)

**Maturity of Integration Strategy — Why:**
To remain agile, cloud-ready, and future-proof, customers must align their integration architecture with evolving technologies and SAP's product roadmap. This means modernizing legacy systems, embracing new integration paradigms, and designing for the future enterprise landscape. Defining a clear target architecture and multi-year roadmap (5–10 years) is essential to guide this transformation effectively.

**Maturity of Integration Governance — Why:**
With Clean Core principles and guidelines in place, a mature integration governance framework is essential to ensure they are consistently applied and traceable. Structured governance enforces architectural standards, enables informed decision-making, and ensures long-term compliance. Leveraging methodologies like SAP ISA-M supports a systematic assessment and implementation of integration strategies across the organization.

**What these practices evaluate:**
- Awareness of product availability and future-ready technology by defining an integration strategy following SAP ISAM
- Whether a transformation journey has been established to reach the target architecture
- Whether a formal integration governance framework is established, ensuring Clean Core principles are consistently applied through defined organizations (e.g., CoE), guidelines, and oversight (e.g., Governance Board)
- Systematic processes and methodologies (such as SAP ISA-M) to evaluate and guide integration strategies, handle new integration requests, and maintain architectural standards for long-term compliance

### INT-03: Integration Landscape (Slide 66 continued)

**Why:**
Adopting modern integration technologies is key to ensuring scalability, flexibility, and innovation readiness. A mature integration landscape empowers enterprises to respond quickly to evolving business needs.

**What it evaluates:**
- Whether the integration landscape leverages modern middleware technologies, centralized B2B integration layers, and API-led strategies to ensure scalability, flexibility, and reuse
- Whether the architecture incorporates real-time, event-driven processing and clearly defined integration patterns to create a resilient and future-ready integration environment
- Whether hybrid and multi-cloud integration strategies are in place to enable seamless connectivity across on-premise and cloud environments

### INT-04/05/06: Toolchain, S/4HANA Readiness, Operational Framework (Slide 67)

**Maturity of Tool Chain — Why:**
Without comprehensive tools to document, govern, and oversee integrations, organizations risk losing transparency over their integration landscape, resulting in unmanaged technical debt, inconsistent data flows, and costly manual troubleshooting. Strong visibility empowers informed decision-making, reusability, and lowers risk throughout the transformation journey.

**Maturity of SAP S/4HANA Integration Readiness — Why:**
Ensuring integration readiness for SAP S/4HANA is essential to gain insights into transformation efforts towards a cleaner core. This readiness assessment mitigates risk by reducing technical debt and helps avoid disruptions during transformation. By leveraging standardized content, organizations can accelerate innovation adoption while lowering TCO and TCD.

**Maturity of Operational Framework — Why:**
A mature operational framework ensures that integrations are consistently monitored, managed, and maintained. This ensures operational stability and accelerates issue resolution enabling integrations to run reliably while supporting continuous innovation and agility.

---

## INT-01: Integration Strategy

**Why:** To remain agile, cloud-ready, and future-proof, customers must align their integration architecture with evolving technologies and SAP's product roadmap. Defining a clear target architecture and multi-year roadmap (5–10 years) is essential.

### Evaluation Criteria

| Question | Current Score | Target Score |
|---|---|---|
| Have you defined a target (North Star) integration architecture considering future product availability and future roadmaps? | \<0–5\> | \<0–5\> |
| Is there a transformation roadmap guiding the evolution towards your target architecture? | \<0–5\> | \<0–5\> |
| Within your target integration architecture are you considering replacing legacy integration tools with modern integration approaches, e.g. Event-Driven Architecture? | \<0–5\> | \<0–5\> |

### Maturity Rating Guidance

| Rating | Short Description | Long Description |
|---|---|---|
| **0 — Not Started / Not Considered** | No target architecture or roadmap defined | No consideration or definition of a target integration architecture; no roadmap or modernization plans exist. |
| **1 — Beginner** | Initial awareness; informal ideas | Early-stage awareness of need for modernization, initial conversations have started, but no formal documentation or planning has taken place. |
| **2 — Intermediate** | Draft target architecture defined with limited detail and scope | A target (North Star) integration architecture is drafted but lacks detail, completeness, or broad alignment. |
| **3 — Proficient** | Defined target architecture and initial roadmap planning | Target architecture and a high-level transformation roadmap are formally defined and communicated. |
| **4 — Advanced** | Comprehensive target; detailed, phased roadmap | Target architecture is clear, comprehensive, and supported by a detailed, staged transformation roadmap addressing legacy. |
| **5 — Expert** | Future-ready, evolving, fully aligned vision | Target architecture is fully defined, broadly aligned, regularly updated, and acts as a continuous guide for modernization. |

---

## INT-02: Integration Governance Process

**Why:** With Clean Core principles and guidelines in place, a mature integration governance framework is essential to ensure they are consistently applied and traceable. Leveraging methodologies like SAP ISA-M supports a systematic assessment and implementation of integration strategies across the organization.

### Evaluation Criteria

| Question | Current Score | Target Score |
|---|---|---|
| Have you set up an Integration Governance Board including the roles for different persona such as integration architects, developers, and business experts? | \<0–5\> | \<0–5\> |
| Is there an Integration Assessment Methodology (e.g., SAP Integration Solution Advisory Methodology (ISA-M)) in place to determine the most suitable integration approach and technology? | \<0–5\> | \<0–5\> |
| Have you defined Integration Principles and Guidelines to enforce integration modernization (e.g., EDA, API-led, minimizing point-to-Point, RFC, Flat File)? | \<0–5\> | \<0–5\> |
| Is there a template available to capture all relevant requirements for Integration (Business and technical requirements)? | \<0–5\> | \<0–5\> |
| Is there a documented governance process for evaluating new integration requirements (Stay Clean)? | \<0–5\> | \<0–5\> |
| Are you on a regular basis reviewing your existing integration implementations to use modern integration technologies (Get Clean)? | \<0–5\> | \<0–5\> |

### Maturity Rating Guidance

| Rating | Short Description | Long Description |
|---|---|---|
| **0 — Not Started / Not Considered** | No governance or principles considered | No integration governance organization, guidelines, board, or assessment methodology exists or considered. Integration requirements addressed ad hoc or not at all. |
| **1 — Beginner** | Informal, unstructured approach | Some initial discussions or informal ideas exist, but nothing documented or structured; no formal ownership. Integration requirements handled reactively by different teams, often individually and without consistency. |
| **2 — Intermediate** | Governance partially defined | Principles, guidelines, or methodologies have been drafted, and some governance processes or boards are in place; however, enforcement remains limited. Integration requirements are reviewed inconsistently, often lacking standardized procedures or clear guidance. |
| **3 — Proficient** | Structured and established governance | The governance organization and processes are defined, documented, and generally adhered to for new integrations. Integration requirements are evaluated through a formalized process, though the approach may not yet be fully comprehensive or uniformly applied across all scenarios. |
| **4 — Advanced** | Comprehensive, consistent governance | Governance is formalized with well-documented, methodical guidance that is consistently applied across the organization. Integration requirements are systematically assessed and approved through standardized processes, ensuring alignment with architectural best practices and compliance standards. |
| **5 — Expert** | Optimized, evolving governance | Governance is fully institutionalized, reviewed, and continuously improved. Integration requirements are handled proactively and strategically, supporting innovation and business goals. |

---

## INT-03: Integration Landscape

**Why:** Adopting modern integration technologies is key to ensuring scalability, flexibility, and innovation readiness. Defining and applying clear integration patterns aligned with these tools is essential for building a resilient, future-proof architecture.

### Evaluation Criteria

| Question | Current Score | Target Score |
|---|---|---|
| Are you using a middleware technology for your integration requirements? | \<0–5\> | \<0–5\> |
| Do you have a centralized B2B integration layer to efficiently manage your B2B transactions? | \<0–5\> | \<0–5\> |
| Have you established an API-led integration strategy to enhance reusability and standardization? | \<0–5\> | \<0–5\> |
| Is your architecture designed to support real-time processing through an event-driven approach? | \<0–5\> | \<0–5\> |

### Maturity Rating Guidance

| Rating | Short Description | Long Description |
|---|---|---|
| **0 — Not Started / Not Considered** | No modern integration tools or patterns | No middleware, API management, or EDI/B2B solutions are in place. Integration is handled manually or through ad-hoc, point-to-point connections with no standardization or governance. |
| **1 — Beginner** | Ad-hoc, basic integration solutions | Limited use of integration technologies (e.g., some middleware or custom scripts). Integration requirements handled inconsistently, with low standardization or reusability. |
| **2 — Intermediate** | Foundational middleware in place | Some middleware or B2B layers implemented, but strategy is fragmented; APIs or event-driven designs may be piloted. Integration requirements are partially supported by technology selection but lack clear patterns. |
| **3 — Proficient** | Centralized, strategic integration layer | Standard middleware and/or B2B integration layers in use; initial API-led or event-driven approaches established. Integration requirements are processed using recognized patterns and central platforms. |
| **4 — Advanced** | Comprehensive, modern integration stack | Robust middleware, centralized B2B, mature API management, and event-driven architecture widely adopted. Integration requirements are systematically addressed using reusable, standardized patterns and tools. |
| **5 — Expert** | Adaptive, innovative integration landscape | Integration landscape is optimized, leveraging future-proofed, evolving technologies and patterns (API, B2B, real-time, event-driven). Integration requirements are proactively anticipated, rapidly and flexibly supported. |

---

## INT-04: Tool Chain

**Why:** Without comprehensive tools to document, govern, and oversee integrations, organizations risk losing transparency over their integration landscape, resulting in unmanaged technical debt, inconsistent data flows, and costly manual troubleshooting.

### Evaluation Criteria

| Question | Current Score | Target Score |
|---|---|---|
| Are your Business Process Management tools covering integration requirements to provide end-to-end visibility of the business processes? | \<0–5\> | \<0–5\> |
| Are Enterprise Architecture tools being used to document and govern integrations? | \<0–5\> | \<0–5\> |
| Are you using an integration assessment tool to document your integration requirements and decision rationale? | \<0–5\> | \<0–5\> |
| Have you established an Interface Repository for visibility over the Integration architecture? | \<0–5\> | \<0–5\> |

### Maturity Rating Guidance

| Rating | Short Description | Long Description |
|---|---|---|
| **0 — Not Started / Not Considered** | No integration toolchain or visibility | No formal tools are used to document or govern integration requirements; minimal or no visibility; manual/ad-hoc processes, if any. There is no organizational overview or understanding of such tools. |
| **1 — Beginner** | Unstructured, informal documentation | Isolated or manual efforts exist to document integrations, but no consistent tool usage; minimal governance or end-to-end visibility. |
| **2 — Intermediate** | Siloed and partial tool usage | Some tools (BPM, EA integration) are selectively used to document integration needs, but coverage and linkage across business processes is inconsistent. Integration requirements and decisions are partially documented, but visibility and control are fragmented. |
| **3 — Proficient** | Centralized integration toolchain | A centralized toolchain is in place and consistently used to document and govern integrations. Integration requirements are traceable, and partial end-to-end visibility is achieved across teams and systems. |
| **4 — Advanced** | Comprehensive, integrated toolchain | Integrated tools support EA and decision-making processes. Integration requirements and decisions are documented, governed, and shared across the organization. End-to-end visibility is strong, and processes are broadly adopted and standardized. |
| **5 — Expert** | Optimized, automated, insight-driven tools | A fully integrated and automated toolchain supports the entire integration lifecycle — from strategy to operations. All integration requirements are documented in a governed environment, with advanced analytics providing insights for continuous improvement and strategic alignment. |

---

## INT-05: SAP S/4HANA Integration Readiness

**Why:** Ensuring integration readiness for SAP S/4HANA is essential to gain insights into transformation efforts towards a cleaner core. This readiness assessment mitigates risk by reducing technical debt and helps avoid disruptions during transformation. By leveraging standardized content, organizations can accelerate innovation adoption while lowering TCO and TCD.

### Evaluation Criteria

| Question | Current Score | Target Score |
|---|---|---|
| Do you have a clear visibility (e.g., by executing the SAP Readiness Check) on currently used Integration technologies on the SAP backend? | \<0–5\> | \<0–5\> |
| Have you assessed the effort to modernize existing integrations (e.g., Interface technology) in your SAP S/4HANA (e.g., based on the SAP Readiness Check)? | \<0–5\> | \<0–5\> |
| Are your integration-related extensions built according to the clean core principles for extensibility? | \<0–5\> | \<0–5\> |
| Are you using SAP Business Accelerator Hub to verify on existing SAP Standard APIs and SAP Standard Integration Packages? | \<0–5\> | \<0–5\> |
| In cases of missing SAP standard content on the SAP Business Accelerator Hub, are you using the SAP Customer Influence Program? | \<0–5\> | \<0–5\> |

### Maturity Rating Guidance

| Rating | Short Description | Long Description |
|---|---|---|
| **0 — Not Started / Not Considered** | No visibility or planning | No visibility into existing SAP backend integrations. No assessment or planning for S/4HANA migration. Integration technologies are unmanaged and not aligned with clean core principles. |
| **1 — Beginner** | Limited visibility, ad-hoc actions | Some knowledge of integration technologies, but no formal assessment or planning activities started. |
| **2 — Intermediate** | Partial visibility, some planning | SAP Readiness Check or similar tools have been used to get initial visibility and rough estimates for migration. Some integrations are being reviewed or refactored; clean core principles are considered but not consistently enforced. |
| **3 — Proficient** | Structured approach, basic adherence | Clear, documented view of SAP backend integration landscape. Migration efforts are assessed, and there is a plan to address non-compliant integrations. SAP Business Accelerator Hub is routinely consulted for standard APIs/content. |
| **4 — Advanced** | Proactive standardized practices, risk mitigation | Comprehensive visibility of SAP S/4HANA readiness achieved: all existing integrations are reviewed, documented, and aligned or in transition to clean core. Regular use of SAP Business Accelerator Hub and SAP Customer Influence Program for missing standard content. |
| **5 — Expert** | Optimized visibility of SAP S/4HANA readiness and migration effort | Full transparency and control over all SAP integrations. Migration plans are complete, risks are minimal. Organization actively replaces non-compliant APIs and leverages SAP's standard content and influence programs for continuous improvement. |

---

## INT-06: Operational Framework

**Why:** A mature operational framework ensures that integrations are consistently monitored, managed, and maintained. This ensures operational stability and accelerates issue resolution enabling integrations to run reliably while supporting continuous innovation and agility.

### Evaluation Criteria

| Question | Current Score | Target Score |
|---|---|---|
| Have you established an Integration Center of Excellence (ICoE) within your integration organization to oversee the operation, maintenance, and continuous improvement of productive integrations? | \<0–5\> | \<0–5\> |
| Have you implemented an automatic alert notification to proactively monitor errors in productive integrations? | \<0–5\> | \<0–5\> |
| Have you defined a structured error resolution process for each of your integrations to ensure timely and consistent issue handling? | \<0–5\> | \<0–5\> |
| Have you defined an Enablement Journey (continuous learning path) for your integration experts to ensure they are always up-to-date? | \<0–5\> | \<0–5\> |

### Maturity Rating Guidance

| Rating | Short Description | Long Description |
|---|---|---|
| **0 — Not Started / Not Considered** | No operational structure or monitoring | No Center of Excellence (CoE) or operational framework established. Integrations operate without systematic monitoring, proactive alerting, or structured error resolution processes. |
| **1 — Beginner** | Some ad-hoc operations and practices | Basic, informal operational oversight and manual error handling for integrations. Monitoring and alerting are sporadic. There is no formal structure for continuous improvement or support. |
| **2 — Intermediate** | Initial framework, partial monitoring | Some operational processes documented; initial team structure (CoE or similar) may exist. Select integrations have automated monitoring or alerting, and basic error handling processes. |
| **3 — Proficient** | Defined CoE, standard monitoring, processes | A CoE is established with clear responsibility for integration operations. Automated monitoring and alerting are implemented for most integrations. Error resolution processes are standardized and consistently applied. |
| **4 — Advanced** | Proactive, automated, process-driven | The operational framework is holistic and mature: the CoE provides governance, monitoring is automated across all productive integrations, and error resolution is proactive and efficient. |
| **5 — Expert** | Integrated, optimized, self-improving | The operational framework is fully integrated, automated, and continuously optimized. The CoE leverages analytics and continuous feedback for self-healing, rapid resolution, and innovation. |
