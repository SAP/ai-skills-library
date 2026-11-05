# Clean Core Extensibility — Whitepaper (2026)

> Source: SAP White Paper "Clean core extensibility — Creating scalable, upgrade-ready extensions for the Autonomous Enterprise" (August 2026, document 243569_232950enUS)

---

## Sources

When citing content from this file, link to the relevant source below:

| Topic | Source | URL |
|-------|--------|-----|
| All content in this file | SAP White Paper: Clean Core Extensibility (August 2026) | https://www.sap.com/documents/2024/09/20aece06-d87e-0010-bca6-c68f7e60039b.html |
| ABAP Extensibility Guide (public companion document, chapter 5: ATC) | SAP Help Portal – ABAP Extensibility Guide | https://www.sap.com/documents/2022/10/52e0cd9b-497e-0010-bca6-c68f7e60039b.html |
| Cloudification Repository (released APIs, classic APIs, noAPIs) | Cloudification Repository Viewer | https://sap.github.io/abap-atc-cr-cv-s4hc |

---

## Preface: Autonomous Enterprise and Clean Core

*(New in 2026 edition — not in 2025)*

Enterprises are entering a new era in which AI facilitates collaboration among people, processes, and systems with greater speed, precision, and resilience. The **Autonomous Enterprise** embodies this vision: a business that can sense change, recommend actions, automate routine decisions, and continuously improve outcomes — while keeping people in control of strategy, governance, and exceptions.

Clean core principles are **essential prerequisites** for the Autonomous Enterprise:
- AI agents, intelligent applications, and automated workflows need clean, governed, and upgrade-stable foundations
- Excessive customization and tightly coupled extensions slow innovation, increase risk, and make it harder to adopt new capabilities
- A clean core makes it easier to adopt new SAP capabilities, integrate AI responsibly, and maintain an ERP landscape that adapts to continuous change

RISE with SAP provides a guided path toward the Autonomous Enterprise by connecting trusted ERP processes, business data, and industry expertise to modern cloud capabilities and embedded agentic AI. The **RISE with SAP Methodology** is now described as an **agent-led toolchain** that simplifies migration, modernization, and continuous innovation — including migration and modernization assistants that reduce complexity and cost.

> SAP publishes a series of white papers on clean core covering all five principles: Business Processes, Data, Integration, Operations, and Extensibility (this document).

---

## Executive Summary

### Why Clean Core Matters

Over time, ERP landscapes become weighed down by custom code, undocumented changes, and hard-to-maintain integrations. This limits flexibility, slows upgrades, and makes it harder to adopt AI-enabled capabilities at scale.

Clean core addresses these challenges by promoting standard, best-practice-aligned processes and enabling strategic extensions for differentiation. It is essential for the **Autonomous Enterprise**: a business where applications, data, and AI work together so that trusted signals become business context, agents can take action, and people stay in control of direction, judgment, and exceptions.

Benefits include:

- Accelerate innovation cycles
- Minimize technical debt
- Simplify system maintenance and upgrades

Rather than limiting agility, clean core ensures extensions are done the right way — with long-term stability, scalability, and innovation readiness.

### What Is New: The Clean Core Level Concept

SAP evolved from the previous **3-tier extensibility model** to the **clean core level concept** — a new model with four distinct levels (A, B, C, D) based on:
- Architectural integrity
- Upgrade safety
- Alignment with clean core principles

The **"SAP Business AI Platform first"** strategy is the core recommendation (Level A as ideal), but the model acknowledges the realities of complex legacy landscapes and provides a pragmatic path forward.

**Fundamental principle (unchanged):** Decouple extensions from standard SAP code to ensure upgrade stability.

---

## Chapter 1: Introduction

SAP software delivers broad and deep functionality across lines of business and industries. In the age of AI, this foundation becomes more powerful: applications generate business signals, data provides trusted context, and agents turn that context into action. This is the foundation of the **Autonomous Enterprise** — a business that responds as one connected system, with people setting direction and AI helping execute routine work, coordinate workflows, and improve outcomes.

The **SAP Autonomous Suite** brings this vision to life through autonomous domains (finance, supply chain, spend, HCM, customer experience). **SAP Business AI Platform** is SAP's AI platform — combining deep process context, unified business data, purpose-built models, and governance so AI can operate in business context at scale. SAP BTP capabilities are a core part of SAP Business AI Platform.

### The Clean Core Approach

Clean core encourages organizations to:
- Adopt **standardized, upgrade-stable functionality** for non-differentiating processes
- Use **flexible extensibility options** for capabilities that deliver unique business value

This means maintaining a stable digital foundation — reducing complexity, technical debt, and upgrade effort — so innovation can happen where it delivers the most value.

### Scope of the Whitepaper

This whitepaper focuses exclusively on the **extensibility principle** of clean core. It covers:
- Extension options for **SAP Cloud ERP Private** (the package including SAP S/4HANA Cloud Private Edition)
- Architectural considerations
- Governance recommendations
- Implementation guidance

Journeys covered: **RISE with SAP** (existing SAP ERP customers) and **GROW with SAP** (net new customers).

---

## Chapter 2: Why a Clean Core Is Important

### Overcoming Obstacles and Unlocking Innovation

Common challenges in legacy on-premise systems:
- Lack of standardization
- Excessive customization
- Poor data quality

These increase complexity and reduce agility, making it difficult to capitalize on emerging technologies (especially business AI).

### Value of Clean Core

| Pillar | Benefits |
|--------|----------|
| **Driving enterprise agility** | Reduce time to value; focus extensions on differentiating processes; faster decisions with clean data |
| **Unlocking new innovations** | Continuous improvement; adopt AI; frequent low-effort upgrades |
| **Enabling efficient operations** | Lower maintenance costs; reduce cybersecurity risks; minimize customizations |

Clean core shifts IT spend from managing technical debt to driving innovation.

---

## Chapter 3: What Clean Core Means for Extensibility

### 3.1 Extensibility as Part of the 5 Guiding Principles

The 5 clean core guiding principles:

1. **Business Processes** — Streamline and standardize; stay competitive while reducing complexity
2. **Extensibility** — Decouple extensions from the standard; use SAP Build and Joule Studio for on-stack and side-by-side; ensure easier upgrades and better maintainability
3. **Data** — Control data per latest standards; ensure governed, compliant data
4. **Integration** — Use released APIs and event-based integration; no dependencies that compromise flexibility
5. **Operations** — Keep operations effective and efficient; automate wherever possible

> Extensions should only be made where processes are clearly differentiating and deliver measurable value.

### 3.2 Extensibility Options: On-Stack and Side-by-Side

Two architectural approaches for **SAP Cloud ERP Private** (SAP S/4HANA Cloud Private Edition):

| Approach | Description |
|----------|-------------|
| **On-stack** | Tightly coupled with ERP core; runs on the same stack (SAP Cloud ERP Private) |
| **Side-by-side** | Loosely coupled; runs on **SAP Business AI Platform** |

Often a combination of both is needed.

#### When to Use On-Stack Extensions

Use on-stack when the extension must operate in close proximity to S/4HANA, interacting directly with core data, transactions, or applications.

**Common on-stack patterns:**
- Adapt and extend standard applications (UI adaptations, custom fields, extend data model, custom logic in LUW)
- Create custom full-stack applications (UI service, application logic, persistence using local APIs)
- Create and enable integration (released local APIs, events)

**Typical characteristics requiring on-stack:**
- Transactional consistency required (updating SAP standard + custom tables together)
- Reading high data volumes with complex SQL/joins
- Frequent access/changes to SAP standard tables
- Extension of existing S/4HANA core applications

> On-stack extensions on S/4HANA Cloud Private Edition **must** use the ABAP Cloud development model. On-premise environments also recommend ABAP Cloud for highest clean core standards.

#### 3.2.1 ABAP Cloud (on-stack via SAP Build)

ABAP Cloud is the standard development model for cloud-ready business applications, services, and extensions.

**Key benefits:**
- **Unified model**: Single model for on-stack and side-by-side; same model SAP uses for core development
- **Cloud readiness by default**: Compiler and syntax checks enforce cloud and clean core rules — cannot be bypassed
- **Model-driven architecture**: Supports OLTP (ABAP RAP), OLAP, and new integrations/APIs
- **Rich prebuilt services**: Logging, change documents, number ranges, jobs, factory calendar, currency conversion, etc. — no extra license
- **Built-in cloud qualities**: Scalability, elasticity, testability, supportability
- **Tailored tools**: ABAP development tools for pro-code developers; no-code/low-code for key users
- **AI-powered development**: Joule for developer productivity; AI SDK for consuming AI services from SAP's generative AI hub; custom code migration enhanced by generative AI

#### When to Use Side-by-Side Extensions

Use side-by-side for loosely coupled extensions running on **SAP Business AI Platform**.

**Common side-by-side patterns:**
- Full-stack single-tenant applications (customers and partners on SAP Business AI Platform)
- Full-stack multitenant SaaS (ISVs)
- Hub scenario (central hub collecting/distributing data from multiple systems)
- Custom mobile applications
- Automate tasks and processes across multiple systems (low-code/no-code)

**Typical characteristics for side-by-side:**
- Stand-alone apps; data managed independently (no transactional consistency needed)
- Demand for broad language choice (Java, JavaScript, ABAP, Python, open-source)
- Applications for external users without SAP Cloud ERP Private accounts
- Independent scalability, lifecycle management, continuous delivery

#### 3.2.2 Side-by-Side with SAP Build and Joule Studio

**SAP Business AI Platform** brings together SAP's AI, data, process, and AI governance capabilities, enabling organizations to create and integrate agents, applications, and automations grounded in business context. SAP BTP capabilities are evolving into SAP Business AI Platform.

SAP Business AI Platform supports two programming models:
- **SAP Cloud Application Programming Model (CAP)** — JavaScript (Node.js), TypeScript, Java; runs on Cloud Foundry and Kyma runtime
- **ABAP RESTful Application Programming Model (ABAP RAP)** — part of ABAP Cloud; used in SAP BTP ABAP environment

Both are based on **Core Data Services (CDS)** and integrate with SAPUI5/SAP Fiori.

**SAP Build** — low-code and pro-code, established use cases:
- Combines AI-powered pro-code (ABAP, Java, JavaScript) and low-code tools
- Accelerate ERP modernization; foster innovation; automate processes
- Fusion team development (developers + key users)
- SAP Build lobby as central entry point
- Continued availability and support; customer-managed runtime environment

**Joule Studio** — AI-first development *(new in 2026)*:
- Build and deploy enterprise-ready AI agents, apps, and agentic workflows with intent-based development
- "Vibe coding" for content-based AI agents
- Modern AI developer tools and frameworks for building agentic solutions
- No-code, low-code, and pro-code tooling
- SAP-managed runtime supports mission-critical workloads with SAP standards for security, compliance, and governance
- Deep integration with **SAP Signavio** and **SAP LeanIX** for business context and enterprise architecture insights in agentic AI use cases

> SAP Build and Joule Studio together provide the tools for clean core extension development with agentic AI — SAP Build for established use cases, Joule Studio for AI-first development.

#### 3.2.3 The Best of Both Worlds

On-stack and side-by-side complement each other:
- **Hybrid deployment**: Components remain on-premise while others run in cloud; SAP Business AI Platform supports this
- **Hybrid development**: Microservices architecture and DevOps; back-end tightly coupled on-stack (ABAP Cloud), front-end on SAP Business AI Platform
- **Integration**: ABAP Cloud integrates with SAP Business AI Platform's integration services for complex scenarios

**Two-layer IT architecture:**
- **Layer 1 (Stable clean core)**: Essential core processes; process automation to reduce costs
- **Layer 2 (Innovation layer)**: Fast-paced innovations with flexibility; differentiating processes (sales-order automation, just-in-time production, customer loyalty management)

SAP Business AI Platform is the innovation layer — deeply integrated with core ERP, sharing underlying metadata and business model.

---

### 3.3 SAP's Clean Core Level Concept

#### 3.3.1 The Four Levels

Extensions are labelled A (best) to D (worst):

| Level | Name | Description |
|-------|------|-------------|
| **A** | Extend with SAP Build and Joule Studio | Only released interfaces and extension points with stability contracts. On-stack via ABAP Cloud; side-by-side via SAP Build (CAP/ABAP Cloud/low-code) or Joule Studio (AI-first agentic development) |
| **B** | Leverage classic APIs | Classic APIs/frameworks — upgrade-stable, well-defined, documented. Not formally contracted but nominated by SAP product experts. |
| **C** | Access internal objects | SAP internal objects not declared released/recommended/cloud-ready. Conditionally clean when applying changelog for SAP objects. |
| **D** | Not recommended | Objects marked as "noAPI", modifications to SAP objects, direct write access to SAP tables, implicit enhancements. Highest risk, significant technical debt. |

> **Key rule**: Each extension is classified by its **lowest-ranked** technology. If one technology is Level C in a mixed extension, the whole extension is Level C.

> **Recommendation**: Always extend at the **highest applicable level**. SAP Business AI Platform first strategy. Focus first on eliminating Level D.

#### ABAP Test Cockpit Behavior

| Level | SAP Objects | ATC Finding |
|-------|-------------|-------------|
| A | [Released] remote APIs, local APIs, extension points | No finding |
| B | [Classic] SAP extension points and APIs | Priority 3 (information) |
| C | [Internal] SAP objects | Priority 2 (warning) |
| D | [Not recommended] objects and techniques | Priority 1 (error) |

#### 3.3.2 Evolution from 3-Tier Model

**Why SAP evolved the model:**
- Previous 3-tier model was too stringent for the reality of legacy landscapes
- Some classic patterns (e.g., ABAP List Viewer) pose minimal upgrade risk but were classified as "unclean"
- Need for more differentiated, transparent assessment

**What changed:**
- [Classic APIs]: Selected classic APIs recognized as upgrade-stable without requiring code rewrites
- [Not recommended objects]: SAP now clearly flags high-risk objects
- [Internal SAP objects]: Changelog-based approach for proactive upgrade risk assessment

**What has NOT changed:**
- Level A (ABAP Cloud + SAP Build and Joule Studio) remains the gold standard
- SAP Business AI Platform first strategy is still the recommendation
- Goal: always strive for the highest level of extensibility available

#### 3.3.3 Level A — Extend with SAP Build and Joule Studio

**What to expect:**
- Maximum upgrade stability
- Officially released, well-documented in SAP Business Accelerator Hub
- Governed by transparent lifecycle

**Important**: Level A coverage does not extend to the complete scope of S/4HANA Cloud Private Edition.

**Qualifying criteria:**
- Side-by-side on SAP Business AI Platform: exclusively released APIs
- On-stack: key user or developer extensibility tools using ABAP Cloud language version

**SAP side includes:**
- Released interfaces and extension points with stability contracts
- Discoverable via SAP Business Accelerator Hub, Cloudification Repository, and directly in the system

**Private vs. Public cloud portability:**
- On-stack Level A extensions are generally NOT portable to S/4HANA Public Edition without adaptations
- Side-by-side (SAP Business AI Platform) extensions are more portable — inherent decoupling from core

#### 3.3.4 Level B — Classic APIs

**What to expect:**
- Requirements not fulfillable with released APIs only
- Classic APIs: well-established, broadly recommended, thoroughly documented
- Not governed by formal stability contracts but have longstanding history of reliable use
- Broader scope than Level A; still follows SAP best practices

**Qualifying criteria:**
- Wrappers around classic APIs (e.g., BAPI_PO_CREATE1)
- Classic ABAP extensions (e.g., ALV grid, CL_GUI_ALV_GRID)
- Custom objects using ABAP "Standard" language version not referencing restricted objects

**SAP side includes:**
- Legacy APIs, user exits, BAdIs, SAP GUI, ABAP List Viewer grid
- Available in Cloudification Repository and SAP Note 3578329

#### 3.3.5 Level C — Internal Objects

**What to expect:**
- SAP internal objects not intended for customer use
- No official support scope, incomplete/absent documentation
- Risk of future incompatibility
- Conditionally clean via changelog for SAP objects

**Qualifying criteria:**
- Direct use of internal function modules, classes
- Read access to SAP tables not endorsed for external consumption

**Changelog for SAP objects** (planned with SAP S/4HANA 2025):
- Automated ATC checks to detect incompatible changes to referenced SAP objects
- Early access to future incompatible change information
- Increased planning reliability
- SAP may reclassify internal objects as classic APIs (→ Level B) or not recommended (→ Level D)

> Note: Changelog findings do not automatically demote objects to "not recommended." They encourage refactoring toward released or classic APIs.

#### 3.3.6 Level D — Not Recommended

**What to expect:**
- Highest degree of technical debt
- May compromise system stability, data integrity, and business agility
- **Immediate remediation strongly recommended**

**Qualifying criteria:**
- Objects labeled "noAPI" in Cloudification Repository
- Modifications to SAP objects
- Direct write access to SAP core tables
- Implicit enhancements

### 3.4 Partner Add-Ons and Clean Core

- Partner add-ons use SAP-endorsed technologies, aligning with clean core principles
- **SAP Integration and Certification Center (SAP ICC)**: Open certification program — partners can obtain "SAP-certified for clean core with SAP S/4HANA Cloud"
- **SAP Solution Extensions**: Validated by SAP in collaboration with partners; confirmed clean core compliance
- **Clean core APIs from partners**: Level A via extension; Level B (classic APIs) in partner responsibility via Cloudification Repository

---

## Chapter 4: How to Achieve a Clean Core for Extensibility

### 4.1 RISE with SAP Methodology

A proven approach bundling elements to support digital transformation:
- Structured guidance based on SAP Activate methodology
- Integrated toolchain for streamlined collaboration
- Quality gate checkpoints
- Clean core success plan (roadmap with clear tasks and activities)
- RISE with SAP Methodology dashboard in SAP Cloud ALM

The methodology enables customers to progress toward clean core by integrating:
1. Governance and maturity assessments
2. KPI-based performance tracking

### 4.1.1 Governance and Maturity Assessment

- Framework to assess and strengthen governance processes
- Built around **12 key practices** for Extensibility:
  - 7 practices evaluate **governance maturity**
  - 5 address **system setup** for clean core goals
- Each practice scored on a **maturity scale 0–5** (0 = not started, 5 = expert)
- Gap analysis → targeted actions → prioritized roadmap
- Templates available (referenced in whitepaper)

### 4.1.2 Clean Core Measurement Framework

Two pillars:

| Pillar | Description |
|--------|-------------|
| **Governance & Maturity** | Qualitative assessment; recommendations on tools, governance structures (e.g., SSB), expertise |
| **KPIs** | Quantitative measurement of clean core adherence; derived from system data |

Both integrate with RISE with SAP Methodology: quality gates + dashboard.

> Analogy: Governance and maturity = healthy habits (nutrition, exercise). KPIs = measurable outcomes (hydration, workout frequency). Together = continuous progress.

### 4.1.3 Extensibility KPIs

| KPI | Description | Key Benefit |
|-----|-------------|-------------|
| **Clean core share** | Distribution of custom code objects across levels A–D (based on worst reference) | Visualize distribution; identify areas needing attention; track progress |
| **Technical debt score** | Weighted score per object (10 pts/error, 5 pts/warning, 1 pt/info in ATC) | Objective measure of maintainability factors; highlight where most debt resides |
| **Unused code share** | Portion of custom objects not utilized | Maintain lean, efficient system; identify cleanup candidates |
| **Business modifications** | Count of modifications in SMODILOG table | Identify non-upgrade-stable modifications; highlight need for cleaner practices |

**Measuring clean core share:**
- Each object classified by its worst/lowest reference level
- Example: Level A: 10% (100 objects), Level B: 50%, Level C: 35%, Level D: 5%

**Measuring technical debt score:**
- 10 pts per ATC error + 5 pts per warning + 1 pt per info message
- Can be aggregated by development packages

**Measuring unused code share:**
- Activate ABAP Call Monitor (SCMON) + transaction SUSG

**Measuring business modifications:**
- Extract from SAP table SMODILOG; available in RISE with SAP Methodology dashboard

### 4.2 "Stay Clean" and "Get Clean" Patterns

Two complementary governance patterns:

**Stay Clean** (prevent new debt):
1. Functional requirement assessment (clear business case, cannot be covered by standard)
2. Extension architecture (structured framework, e.g., SAP Application Extension Methodology)
3. Extension implementation (guidelines, authorization checks, automated ATC checks)
4. Extension deployment (transport governance, exemption process)

**Get Clean** (address existing debt):
- Measure KPIs to pinpoint improvement areas
- "Boy scout principle": leave code cleaner than you found it
- Realistic but ambitious goals for technical debt reduction (e.g., 10% per year)

**AI agents and SAP AI Agent Hub** *(new in 2026)*:
For AI agents, the governance scope should also include **SAP AI Agent Hub**. Acting as a command center for enterprise-wide data and AI governance, SAP AI Agent Hub provides visibility and control over SAP and non-SAP AI agents across the IT landscape, helping organizations manage them across their lifecycle — from planning through decommissioning. Just as custom ABAP extensions are governed through the Stay Clean pattern, AI agents deployed as extensions require the same lifecycle governance.

### 4.3 Stay Clean: Creating Clean Extensions

#### 4.3.1 Functional Requirements

- Identified during **fit-to-standard workshops**, managed in **SAP Cloud ALM**
- Requirement gathering: business context first; break down into user stories
- Extension must provide **tangible business value** — even technically sound extensions are "unclean" if they don't address a differentiating need

**Governance — decision process:**
```
New business requirement/gap
    → Is it necessary/beneficial/differentiating?
        → No: Do not implement
        → Yes: Can it be covered with SAP standard/add-on?
            → Yes: Implement as standard functionality
            → No: Is it beneficial to create extension?
                → Yes: Continue with extension architecture
                → No: Do not implement
```

**Solution Standardization Board (SSB):**
- Central authority to oversee design and implementation of business processes
- Validates necessity of extensions
- Ensures SAP standard options are considered first
- Documents and approves all deviations in standardized manner

**SAP Cloud ALM for governance:**
- Tags ("clean" / "not clean") on processes, requirements, user stories, features
- Solution Process Traceability analytical page for compliance overview
- Integrates with RISE with SAP Methodology quality gates

#### 4.3.2 Extension Architecture: SAP Application Extension Methodology

A structured, technology-agnostic approach with three phases:

| Phase | Focus |
|-------|-------|
| **Phase 1: Assess extension use case** | Business & system context; application extension use case definition |
| **Phase 2: Assess extension technology** | Extension styles, tasks, and technology mapping to building blocks |
| **Phase 3: Define extension target solution** | Decision guidance; extension target solution definition |

**Key output per phase:**
- Phase 1: Application extension use case description
- Phase 3: Decision on technical building blocks + extension target solution (used as input for SAP Cloud ALM user stories)

**Decision guidance resources:** Extension Architecture Guide, SAP Discovery Center, SAP Architecture Center

#### 4.3.3 Extension Implementation

**Clean core mindset:**
- Code is strategic — consider clean architecture, system stability, long-term maintainability
- Reuse > rushing into implementation
- Upskilling is part of the work

**Development guidelines:**
- Right APIs, avoid certain enhancements, naming conventions and coding standards
- Key references: "Extend SAP S/4HANA in cloud and on premise with ABAP-based extensions", Clean ABAP Guide & Cheat Sheet, ABAP Cheat Sheets

**Skill development:**
- SAP Learning free journeys: Acquiring Core ABAP Skills, Managing Clean Core, Practicing Clean Core
- Certification: SAP Certified Associate — Back-End Developer — ABAP Cloud
- For architects: Becoming an SAP BTP Solution Architect

**Development approach (top-down, Level A first):**
1. Identify all touchpoints: UIs, integrations, business logic, APIs, persistence
2. Start with SAP S/4HANA Key User Extensibility (Level A) — search released extension points
3. For developer extensibility on-stack: check SAP Fiori Apps Reference Library, transaction SCFD_REGISTRY
4. For side-by-side: explore remote public APIs on SAP Business Accelerator Hub (OData, REST, events)
5. For on-stack developer extensibility: use ABAP Development Tools for Eclipse to find released APIs (CDS views, BOIs, BAdIs)

**When stepping outside Level A:**
- Monitor changelog for SAP objects for early warnings
- Create and run ABAP unit tests after each upgrade (especially for Level C/D objects)
- Encapsulate classic/internal/not-recommended objects in **wrappers** released via API contract (ABAP Cloud API Enablement Guidelines)

#### 4.3.4 Extension Deployment

**Governance controls:**

| Control | Description |
|---------|-------------|
| **Authorizations** | Restrict ABAP language version to ABAP Cloud via S_ABPLNGVS and dedicated software components |
| **ABAP Cloud Readiness check** | ATC variant to promote ABAP Cloud development; optional but strongly recommended |
| **Cloud API enablement** | Wrappers to release non-released objects for ABAP Cloud use |
| **Unit testing** | ABAP unit tests to verify stability of access to non-released objects |
| **Changelog for SAP objects** | Monitor for incompatible changes to non-released objects |

**Transport governance:**
- ABAP test cockpit checks integrated into transport release process
- Pre-delivered ATC variants as baseline; customizable to internal policies
- High-priority findings (priority 1/2) should block transport until addressed or exempted

**Exemption process:**
- Designated Quality Manager (senior developer or architect) approves/rejects
- Every exemption: clear justification, specific finding reference, list of objects
- Temporal limits for each exemption; avoid broad/generic exemptions
- Periodic reviews of 10–20% of existing exemptions

**Language version restriction:**
- Assign S_ABPLNGVS authorization object and/or create dedicated software component for ABAP Cloud only
- Separates standard ABAP Cloud developers from trusted developers with elevated privileges

### 4.4 Get Clean: Measuring Current State

#### 4.4.1 RISE with SAP Methodology Dashboard

Available in SAP Cloud ALM → RISE with SAP tab → System View.

**System View tabs:**
- **Software Stack**: Overview of system stack + SAP Readiness Check results
- **Clean Core Tool Status**: Status of tools needed for clean core data collection
- **Extensibility KPIs** (current):
  - Setup for ABAP Cloud Development (recommended software components created?)
  - Unused Customer Objects
  - Execution of Customer Objects (vs. total executable objects)
  - ABAP Cloud: Level A Customer Objects (limited clean core share view)
  - ABAP Classic: Business Modifications

> Note: Full clean core level visualization (A–D) in the dashboard is planned for a future release. Levels are currently measurable via ABAP test cockpit.

#### 4.4.2 Individual KPI Assessment

For granular insights beyond the standard dashboard:
- Apply individual filter/analysis criteria (e.g., map packages/namespaces to business units)
- Extract KPI data manually using ABAP test cockpit check results
- **Project Kernseife** (open-source): Custom classification model for SAP objects → tailored technical debt score

### 4.5 The Clean Core Journey

#### A) Stay Clean (for all new developments)
- Strict adherence to clean core principles from day one
- Robust governance + up-to-date guidelines + developer training
- Applicable even on SAP ECC today (e.g., build SAP BTP extensions now)

#### B) Get Clean (for existing landscape)
- Measure technical debt baseline (RISE dashboard or ABAP test cockpit)
- Identify unused/obsolete code
- Prioritize lighthouse extensions (rebuild when reworking anyway)
- Set realistic goals (e.g., 10% reduction per year)
- Apply "boy scout principle" continuously

**Clean core is an ongoing journey — not a one-time effort.**

### 4.5.1 Key Steps and Recommendations

1. **Establish clear governance**: Define clean extension guidelines covering all S/4HANA Cloud Private Edition developments
2. **Empower governance**: Involve business + technical teams; get top management commitment
3. **Assess starting point**: Measure current technical debt; create transparency with tools
4. **Upskill developers**: Regular training on clean core principles and ABAP Cloud
5. **Adjust for conversion**: Align with S/4HANA functional changes; reduce scope where feasible
6. **Set incremental goals**: Ambitious yet realistic targets (e.g., 10% technical debt reduction per year)
7. **Prioritize business value**: Focus remediation on code with tangible business impact
8. **Monitor continuously**: Incorporate clean core measurement into development cycles
9. **Adopt boy scout principle**: Leave code cleaner with every change
10. **Prepare for the future**: Leverage SAP Business AI Platform now; lay groundwork for AI agent adoption with SAP AI Agent Hub

### 4.5.2 How the RISE with SAP Methodology Can Help

The **RISE with SAP Methodology** is an agent-led transformation approach that actively supports customers throughout their clean core journey:

- **Standardized framework**: Provides a proven transformation framework with integrated toolchain
- **KPI setup**: Establishes clean core KPIs and tracks them in the RISE with SAP Methodology dashboard
- **Success plan in SAP Cloud ALM**: Creates a structured success plan with quality gates and milestone checkpoints
- **Periodic checkpoint reports**: Generates regular reports with recommendations to guide the customer's transformation
- **Enterprise Architect review**: SAP Enterprise Architects periodically assess the customer's clean core progress using quality gates and a governance/maturity approach, then work with the customer on an action plan

> SAP Enterprise Architects bring an outside-in perspective — they can identify patterns across hundreds of customer engagements and benchmark a customer's clean core maturity against comparable organizations.

---

## Chapter 5: FAQ

> The whitepaper references a separate FAQ document for detailed questions on the level concept. This content is fully ingested in `knowledge/02-faq-level-concept.md`. Topics covered: object classification criteria (QA), classification change rules (QB), ABAP language version mapping (QC), framework/technology classification (QD), measurement in RISE dashboard (QE), and relation to Simplification Item Database / Blocklist Monitor / deprecation (QG).

---

## Chapter 6: Appendix — Key Resources

| Resource | Purpose |
|----------|---------|
| ABAP Cloud (SAP Help Portal) | Deep dive into ABAP Cloud development model |
| Clean core strategy website | Overview of ERP clean core strategy |
| Guide: Extend SAP S/4HANA (ABAP-based extensions) | Extensibility options; guidelines for PMs, key users, ABAP developers |
| Extension Architecture Guide | Which SAP technology to use in a given scenario |
| Extension use case patterns | On-stack vs. side-by-side decision guidance |
| From Classic ABAP to ABAP Cloud | Certification options for ABAP Cloud add-ons |
| SAP Application Extension Methodology (SAP Help Portal) | Structured approach for defining extension strategy |
| SAP Architecture Center | Solution reference architectures |
| SAP BTP Developer's Guide | Building business applications on SAP BTP |
| SAP BTP Guidance Framework | Central access for architects, developers, administrators on SAP BTP |
| SAP Build website | Unified application development and process automation |
| SAP Business Accelerator Hub | APIs, events, CDS views, pre-built automation content |
| SAP Cloud Application Programming Model (CAP) | Cloud-native applications with best practices |
| SAP Discovery Center | Step-by-step use case implementation missions |
| Joule Studio getting started | Building Joule skills and AI agents tailored to business needs — https://help.sap.com/docs/joule-studio |
| Project Kernseife (GitHub) | Open-source custom ATC classification model |
| Cloudification Repository | Classic APIs, internal objects, not-recommended objects classification |
| SAP Note 3578329 | Classification of ABAP frameworks into clean core levels |
| SAP Note 3565942 | New clean core ATC checks; technical debt score base data |

---

## Key Terminology

| Term | Definition |
|------|-----------|
| **Clean core** | Set of guiding principles for agile, innovative, efficient ERP systems; decoupled extensions, upgrade stability |
| **SAP Cloud ERP Private** | Umbrella product name for SAP's on-premise and private cloud ERP portfolio (includes SAP S/4HANA Cloud Private Edition) |
| **SAP Business AI Platform** | SAP's AI, data, process, and AI governance platform — successor branding to SAP BTP in strategic positioning; enables creating and integrating agents, applications, and automations grounded in business context |
| **Joule Studio** | AI-first development environment for building and deploying enterprise-ready AI agents, apps, and agentic workflows; SAP-managed runtime; complements SAP Build |
| **SAP AI Agent Hub** | Command center for enterprise-wide AI agent governance; provides visibility and control over SAP and non-SAP AI agents across their lifecycle |
| **Level A** | Extensions using only released APIs/extension points; ABAP Cloud on-stack or SAP Build / Joule Studio side-by-side |
| **Level B** | Classic APIs — upgrade-stable, documented, nominated by SAP experts but no formal stability contract |
| **Level C** | Internal SAP objects — conditionally clean via changelog for SAP objects |
| **Level D** | Not recommended — noAPI objects, modifications, write access to SAP tables, implicit enhancements |
| **ABAP Cloud** | SAP's development model for cloud-ready extensions; enforces clean core rules via compiler |
| **SAP Build** | Unified suite: ABAP Cloud (pro-code on-stack) + CAP/low-code (side-by-side); established use cases; customer-managed runtime |
| **Stay Clean** | Governance pattern preventing new technical debt |
| **Get Clean** | Pattern for reducing existing technical debt |
| **Boy scout principle** | Always leave code cleaner than you found it |
| **Technical debt score** | Weighted ATC findings: 10 pts/error, 5 pts/warning, 1 pt/info |
| **Clean core share** | Distribution of custom objects across levels A–D |
| **Changelog for SAP objects** | SAP tool proactively identifying internal objects with incompatible changes in upcoming releases |
| **Cloudification Repository** | SAP tool listing classic APIs, internal objects, and not-recommended objects with their classifications |
| **SAP Application Extension Methodology** | 3-phase structured approach: assess use case → assess technology → define target solution |
| **Solution Standardization Board (SSB)** | Central governance authority for extension approval in organizations |
| **RISE with SAP Methodology** | Agent-led transformation framework; includes quality gates, dashboard, clean core success plan, and SAP Enterprise Architect periodic review |
