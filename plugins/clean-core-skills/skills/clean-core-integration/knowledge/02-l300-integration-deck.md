# Clean Core Integration — L3 Deck

**Source:** Clean Core Integration L3 Deck  
**Document ID:** SAP1280564 | Link: https://dam.sap.com/mac/app/p/pdf/asset/preview/JhcAkZf?ltr=a&rc=10&doi=SAP1280564  
**File:** Clean_Core_Integration_L3_Deck (1).pptx  
**Published:** 2025 (complementary to the 2026 whitepaper)  
**Ingested:** 2026-09-13  
**Audience:** Enterprise Architects, Integration Architects, TQMs  
**Purpose:** Practical, implementation-level detail on how to achieve clean core integration — guidelines, toolchain, assessment methodology, migration, upskilling. The 2026 whitepaper supersedes on strategic framing; this deck remains valid and complementary for implementation guidance.

---

## Agenda (Slide 2)

1. Why does clean core integration matter?
2. What is clean core integration?
3. What are the key guidelines for clean core integration?
   - Best practices for process integration
   - Integration design guidelines
   - Integration flow extensions
   - Center of Excellence strategy
   - End-to-end monitoring
4. How to achieve clean core integration
   - Stay Clean I: Defining an integration strategy
   - Stay Clean II: Conducting an integration assessment
   - Get Clean
5. Measure clean core
6. Upskill your integration experts
7. How others achieved clean core integration

---

## Section 1: Why Does Clean Core Integration Matter?

### Slide 4 — Key Business Challenge

SAP brings all components together to lead the way into the next era of enterprise management. Staying competitive requires a core that is ready for the accelerating pace of innovation.

### Slide 5 — Overcoming Obstacles and Unlocking Innovation

The accelerating pace of innovation creates opportunity — if your core is ready. Clean core integration breaks the patterns of fragile, tightly coupled landscapes.

### Slide 6 — Why Is Clean Core Beneficial in Integration?

Four key benefits:
1. **Upgrade stability** — Boost integration stability during upgrades by leveraging SAP standard interfaces in SAP S/4HANA, while reducing custom development to lower TCD and TCO
2. **Agility** — Increase agility and enable faster adoption of SAP innovations, while lowering costs
3. **Operational risk reduction** — Reduce operational risk and minimize business disruptions through robust integration monitoring, build confidence in end-to-end processes
4. **Innovation adoption** — Accelerate time-to-value by adopting modern integration architecture

### Slides 8-9 — What Is a Clean Core?

> *"Clean core refers to a set of guiding principles that support continuous business transformation by fostering agile, innovative, and efficient ERP systems. The principles focus on building resilient business processes and extensions, supported by seamless integration, efficient operations, and high data quality."*

Five guiding principles: Extensibility (decouple extensions from standard core), Business Processes (keep competitiveness while reducing complexity), Integration (keep the system landscape reliable and flexible), Data (control data according to the latest standards), Operations (keep the operations effective and efficient).

---

## Section 2: What Is Clean Core Integration?

### Slide 10 — Understanding the Need

Clean core integration: what it is and why it matters — keeping the landscape reliable and flexible while enabling continuous business transformation.

---

## Section 3: Key Guidelines for Clean Core Integration

### Slide 13 — Six Principles and Best Practices

1. **Standard-first** — Aim for standard integration content and released interfaces available on the SAP Business Accelerator Hub, deviating only when the standard cannot meet validated requirements

2. **Modern integration strategies** — Adopt event-driven architecture and API-led connectivity; establish a Developer Hub to expose APIs in a catalog

3. **Minimize traditional interfaces** — Minimize the use of traditional interfaces (IDocs, BAPIs). If a modern alternative exists, using a traditional interface is not considered clean. If no modern option is available and the traditional interface is not deprecated or listed in the simplification item catalog, it is acceptable to use.

4. **Extension governance** — When modifying standard interfaces or building custom ones, use released SAP extension points and leverage the level concept for extensibility; document the approach and decisions

5. **Centralized governance** — Leverage expert monitoring tools for SAP S/4HANA and SAP Integration Suite, and end-to-end process monitoring through SAP Cloud ALM for real-time monitoring, alerting, and analytics of interfaces, ensuring proactive issue resolution

6. **Continuous innovation cycle** — Establish a continuous innovation and optimization cycle via an Integration Governance Board; regularly review traditional integrations using the SAP Integration Solution Advisory Methodology

### Slides 15-16 — SAP Business Accelerator Hub: Best Practices

- Discover process blueprints, identify relevant integration points, and trace to the required APIs/events and integration packages
- Discover and consume released SAP APIs, events, data models, and integration packages — stable, upgrade-safe contracts
- Copy and deploy standard integration content to accelerate time-to-value; parameterize instead of customizing
- Standardized domain models (SAP One Domain Model) reduce mapping effort and risk

---

## Section 4a: Best Practices for Process Integration — Detailed Guidance

### Slides 17-18 — When to Use API-Led vs. Event-Driven

**API-led integration** is best for:
- Synchronous scenarios where immediate confirmation is required
- Backend systems that must be protected from direct access
- Strong governance, security, and policy enforcement requirements
- APIs that need to be reusable across multiple consumers
- Partner and third-party integrations requiring standardized interfaces

**Event-driven integration** is best for:
- Real-time or near-real-time notifications
- Multiple independent receivers reacting to the same business event
- Avoiding tight coupling between sender and receiver
- Peak-load buffering and elastic consumption
- Resilient, asynchronous integration designs

### Slide 19 — API Management: Developer Hub

Developer Hub provides a clean, developer-facing view of available APIs and integration assets. Primary access point for API consumers. APIs should be documented, versioned, secured, and discoverable.

### Slide 20 — Upgrade Stability: Risk Areas

Upgrade stability risks are linked to the use of non-standard, tightly coupled integration approaches. SAP Labs preview guidance on risk identification.

### Slide 21 — When and How to Extend Integrations

Decision trees for integration requirement decisions provide general guidance. Each integration requirement should be reviewed based on its specific use case.

### Slide 22 — Impact of Building Custom Integration in SAP ERP

Building custom integration in SAP ERP (as opposed to using the integration platform layer) increases upgrade risk and maintenance cost — core reason to externalize orchestration and transformation to SAP Integration Suite.

### Slides 23-24 — Best Practice: Technology Mapping and Interface Technology Decision Tree

**Technology mapping (runtime profiles):**

| Integration Pattern | SAP Integration Suite Runtime Profile |
|---|---|
| Cloud to cloud | SAP Integration Suite |
| Cloud to on-premises | SAP Integration Suite — cloud runtime |
| On-premises to on-premises | SAP Integration Suite — Edge Integration Cell |

*Edge Integration Cell is a runtime environment designed to support private integration scenarios. There is no separate decision path to determine whether the setup should run in a private or public environment.*

### Slides 25-26 — Example: How to Replace IDoc Usage

> *"There is no simple how-to guide SAP can provide for replacing IDocs. Since it is an outdated technology, it should be replaced where meaningful and possible. If no adequate API or events are available yet from SAP, it can be reasonable to keep the IDoc scenario until such an API or event becomes available. Inform SAP and request APIs or events through the SAP Influencer Portal."*

**IDoc replacement process:**
- Involved people: Enterprise Architect, Business Process Owner, Solution Architect, Integration Architect
- Step 1: Clarify actual integration requirement and linkage to the business process — why is the integration required? what needs to be integrated? (identify sender, receiver, business object)
- Step 2: Conduct integration assessment following SAP ISAM — identify integration style and pattern, synchronous vs. asynchronous, transformation/routing logic required, message volume, additional requirements
- Step 3: Identify integration approach via SAP Integration Suite, API-led, or event-driven
- Step 4: Check for relevant SAP standard integrations and interfaces in SAP Business Accelerator Hub
- Step 5: Check the simplification item catalog for the specific IDoc — is it blocked or deprecated?
- Step 6: Assess the advantage the replacement would bring — identify benefits and costs
- Step 7: Within the Integration Governance Board, decide which integration approach to pursue

### Slide 27 — Example: How to Work with XI

Guidance on working with XI (XI ABAP proxy) — modernize with standard web service/event-driven architecture.

---

## Section 4b: Integration Design Guidelines

### Slide 30-31 — Core Qualities of Enterprise-Grade Integration Flows

Enterprise-grade integration flows in a clean core landscape must exhibit:
- Loose coupling and API-first design (avoid direct DB access, internal tables, in-core modifications)
- High availability and resilience (retries, idempotency, timeout handling, failure isolation)
- Graceful error handling (failures do not disrupt core operations; errors handled asynchronously, logged centrally)
- Readability and maintainability (modular, consistently structured, easy to understand)
- Efficient resource usage (optimize payloads, call frequency, processing logic)

### Slide 32 — Implementation Guideline Topics

| Topic | Examples |
|---|---|
| Design of integration scenarios | Reusable building blocks (enterprise integration patterns), naming conventions, documentation, sample integration flows |
| Integration qualities | Reliable, resilient, secure, well-performing — authentication, retries, logging, validation |
| Backend configuration | Communication arrangements and scenarios in SAP S/4HANA |
| Lifecycle management | Releasing, updating, deprecating; testing (unit tests, end-to-end tests); transporting across multi-tier landscapes |
| Monitoring | For technical experts, for business users, end-to-end integration monitoring |

---

## Section 4c: Integration Flow Extensions

### Slides 34-36 — How to Extend SAP Integration Suite Flows

**Concept:** Standard content plus extension content (layered approach):
- Standard integration flow provides baseline orchestration and mapping — defines canonical message structures, process logic, interaction patterns; SAP owns and maintains
- Customer-specific extension content added only at explicitly defined extension points (pre-exit or post-exit steps)

Extension steps: Mapping Extension (pre-exit / post-exit). See SAP Influence for Customer Influence requests when custom extension is not available.

**Key sections:**
- Integration Flow Extension - Concepts: overview of concept and involved components
- Mapping Extension Step by Step (Demo Example): creating standard integration flow with post-exit step; creating custom integration flow with post-exit mapping
- Mapping Extension Step by Step (Example from SAP Hybris C4C): real-life use case covering pre-exit and post-exit mappings

---

## Section 4d: Center of Excellence Strategy

### Slide 38 — Set Up a Customer Centre of Expertise (cCOE)

Establish the governance and capabilities needed to support the delivery and management of the SAP Business Suite. The cCOE provides overarching governance for integration practices.

### Slide 39 — Establish a Solution Standardization Board (SSB)

The SSB ensures that deviations from standard processes are formally evaluated and governed. Resources:
- "Establish a Solution Standardization Board"
- "Implementing SAP Cloud ERP Private with a Cloud mindset"
- "Clean Core related enhancements in the SSB for RISE with SAP"
- "The value of a Solution Standardization Board as part of implementing SAP S/4HANA Cloud"

### Slide 40 — Integration Center of Excellence (ICoE) Strategy

Establish robust governance to enforce the integration strategy by using the Integration Center of Excellence strategy. Centralizes best practices, reusable assets, coaching of delivery teams, cross-technology oversight.

### Slide 41 — SAP BTP Center of Excellence Maturity Model

By centralizing essential SAP BTP expertise in the Center of Excellence — while empowering separate agile teams to deliver solutions — organizations can:
- Adopt SAP BTP capabilities faster
- Work in mixed (business/IT) teams more effectively
- Drive their transformation journey to the cloud with SAP

---

## Section 4e: End-to-End Monitoring

### Slide 43 — Adopt End-to-End Integration Monitoring Tools

Increase process visibility by adopting end-to-end integration monitoring tools.

### Slide 44 — SAP Integration Suite: Built-in Monitoring

| Capability | Why | 
|---|---|
| Cloud integration | Monitor Integrations and APIs |
| API management | Monitor APIs |
| Event mesh | Monitor Event Mesh |
| Trading partner management | Monitor B2B Scenarios |

### Slides 45-46 — SAP Application Interface Framework: Expert Monitoring Tool for SAP S/4HANA

SAP Application Interface Framework (AIF) is the **expert monitoring tool for SAP S/4HANA interfaces**:
- Enables monitoring of a variety of interface types (standard, traditional, and custom) within the SAP S/4HANA landscape
- Business users benefit from intuitive error analysis tools
- Custom namespace transactions count toward license; SAP-delivered interfaces (e.g., SAP S/4HANA for central finance, SAP Document Compliance, standard SAP S/4HANA interfaces) are free

### Slide 47-48 — SAP Cloud ALM for End-to-End Monitoring

SAP Cloud ALM provides centralized monitoring of integration scenarios and service health state — central view for operations teams:
- End-to-end monitoring of integration scenarios, bringing the technical message flow closer to the business context
- Correlation of messages to an end-to-end message path
- Reporting of failed messages and deployment exceptions
- Tracking messages based on business attributes
- Technical health tracking of cloud integration tenants (JMS resource exhaustion, validity of certificates and key pairs)
- Embedded alerting with possibility to collaborate during issue resolution
- Configurable actions toward email-, chat-based, and ticketing-based services

### Slide 49 — SAP Operations Control Center (OCC)

The OCC provides centralized transparency to manage operational, tactical, and strategic IT decisions across the integration landscape. Additional information available in SAP Help Portal.

---

## Section 5: How to Achieve Clean Core Integration

### Slides 52-54 — How to Achieve Clean Core Integrations

The clean core integration journey provides a structured path from the current state to a clean integration architecture. Two complementary tracks:
- **Get Clean** — decrease technical debt for existing integrations
- **Stay Clean** — avoid any "unnecessary" technical debt

### Stay Clean I: Defining an Integration Strategy (Slides 55-61)

**Integrated toolchain for stay clean (core solutions):**
- SAP LeanIX — visualize, assess, and manage transitions toward target IT architecture; Interface Repository
- SAP Signavio — managing and optimizing business processes; integration requirements linked to business process models
- SAP Cloud ALM — digital backbone for project management, solution operation, ALM/DevOps

**Integrated toolchain extended view:**
- SAP Integration Suite — integration assessment capability (ISAM-based)
- SAP Business Accelerator Hub — standard content, APIs, events

**Setting up a future-state integration architecture (high-level steps):**

Stage 1 (Discovery):
- Task: Understand current integration landscape
- Activity: Execute SAP Readiness Check, analyze integration technologies
- Output: Current state baseline, identified technical debt
- Tool: SAP Readiness Check, SAP LeanIX

Stage 2 (Architecture design):
- Task: Define target (North Star) integration architecture
- Activity: Apply SAP ISAM, select integration styles and patterns, define integration domains
- Output: Target architecture, integration strategy document
- Tool: SAP LeanIX, SAP Signavio

### Stay Clean II: Conducting an Integration Assessment (Slides 62-67)

**SAP Integration Solution Advisory Methodology (ISAM):**

SAP ISAM is the structured approach for consistently assessing and guiding integration decisions across the organization. Supported by:
- SAP BTP Guidance Framework
- Integration Assessment capability within SAP Integration Suite

**Three-step assessment process:**

**Step 1: Customize your integration strategy** (done once, or when strategy evolves)
- Adapt ISAM settings to customer needs: integration domains, styles, patterns, questionnaires
- Configure landscape information
- Customize integration strategy

**Step 2: Create a Business Solution Request** (per new integration requirement)
- Define high-level requirements from a business perspective: source and target application instances, business process context
- Submit to an integration architect
- *Role:* Business domain expert

**Step 3: Process Interface Request** (translation to technical requirements)
- Translate business solution request into technical interface request
- Specify integration requirements via customizable questionnaire
- Get a proposal of the integration technology with the best fit
- Decide on the integration technology
- *Role:* Integration architect

### Integration Transformation Road Map Prioritization (Slide 68)

**Priority criteria framework:**

| Dimension | Criteria |
|---|---|
| Business value & impact | Criticality to business processes, regulatory/compliance needs, customer impact |
| Technical obsolescence & risk | Legacy technology, security exposure, support/maintainability cost |
| Complexity & feasibility | Dependencies on other systems, data complexity, migration effort |
| Readiness & resource availability | Team capacity, partner/system readiness |
| Reuse & standardization potential | Reuse opportunity, alignment to integration patterns (APIs, event-driven) |
| Cost & benefit | TCO for redesign/migration/ongoing support, ROI (cost savings, speed, agility, risk reduction) |
| Time sensitivity | Upcoming system changes, strategic initiatives alignment |

### Get Clean (Slides 69-73)

**How to get clean in terms of integration:**

Integrated toolchain for get clean:
- SAP Readiness Check — identify all activated interfaces, understand migration effort
- SAP LeanIX — Interface Repository, impact analysis, modernization planning
- SAP Integration Suite Migration Assessment capability — estimates effort and semi-automated migration tooling for SAP Process Integration/Process Orchestration scenarios

**SAP Integration Suite Migration Assessment capability:**
- Data extraction directly connecting to SAP Process Orchestration systems
- Evaluation based on flexible rules framework
- Migration effort expressed in T-shirt sizes and person-days
- Assessment categories:
  - **Ready to migrate** — can be moved to SAP Integration Suite manually or semi-automatically
  - **Adjustment required** — can be moved but further adjustments to end-to-end integration process based on best practices are required
  - **Evaluation required** — no match or match not known; some items require further evaluation

*Note: The assessment category is an indication of the ease of "migratability" and not an indication of what the migration tool can automate.*

**Modernization recommendations (Slide 73-74):**

| From | To |
|---|---|
| SAP Process Integration / SAP Process Orchestration | SAP Integration Suite using the Migration Guide for SAP Process Orchestration |
| Decentralized point-to-point integration | Centralized middleware approach using SAP Integration Suite; API-led strategy via API Management; event-driven architecture via Advanced Event Mesh |
| Decentralized legacy B2B integration / SAP PI/PO B2B add-on | Trading Partner Management in SAP Integration Suite and Integration Advisor leveraging the B2B Integration Factory |
| IDocs | SOAP/OData APIs or business events on SAP Business Accelerator Hub |
| XI ABAP proxy | Standard web service / event-driven architecture |

---

## Section 6: Measure Clean Core

### Slide 76 — How to Measure Clean Core: KPI Framework

The clean core measurement framework covers four dimensions for integration:

| KPI Category | Metric | Key Question |
|---|---|---|
| **Upgrade stability** | % of standard, traditional, and custom interfaces | Measures the ratio of active interface technologies that adhere to clean core principles vs. those that do not, compared to total active interfaces |
| **Operational risk — expert tool monitoring** | % of centrally monitored interfaces (AIF) | Measures interfaces automatically and centrally monitored with SAP Application Interface Framework |
| **Operational risk — end-to-end monitoring** | SAP Cloud ALM monitoring coverage | Measures whether integration monitoring and alert notification via SAP Cloud ALM are set up |
| **Innovation adoption** | Usage of modern integration technologies | Assesses the extent to which modern SAP integration tools and technologies are being used (SAP Integration Suite and its capabilities, SAP Master Data Integration, SAP Datasphere, SAP Business Data Cloud) |
| **Agile decision-making and operational risks** | % of tools used for the integration requirement process | Assesses whether the integrated toolchain is used to enable agile and transparent decision-making for integration projects |

Stakeholder framing:
- **COO perspective:** *"As the COO, I am responsible for ensuring that end-to-end business processes run seamlessly and without disruption."* → Upgrade stability, operational risk KPIs
- **CIO perspective:** *"As the CIO, I need a comprehensive overview of our integration architecture."* → All KPI categories
- **CTO perspective:** *"As the CTO, I am responsible for ensuring that our integration architecture remains agile and resilient to future changes."* → Innovation adoption, agile decision-making KPIs

---

## Section 7: Upskill Your Integration Experts

### Slide 79 — Launching an Enablement Journey

Key steps:
1. **Assess current skills** — conduct assessments to identify gaps in integration knowledge, focusing on AI-driven integrations, event-driven architecture, and hybrid strategies
2. **Design a tailored journey** — align with SAP's integration strategy
3. **Incorporate continuous learning** — structured paths with bite-sized modules, certifications, and community forums
4. **Define target audience** — integration developers, architects, and experts aiming for certifications like SAP Certified Associate - Integration Developer
5. **Roll out key modules** — distributed architecture, iPaaS, API management, integration flows, modern capabilities like event-driven architecture using SAP Integration Suite
6. **Focus on innovation enablement** — AI-assisted features (e.g., integration advisor for B2B mappings), migration tools (migration accelerator for SAP PI/PO to SAP Integration Suite), hybrid integration for scalability
7. **Include practical elements** — demos, proofs of concept, tools like SAP Discovery Center
8. **Promote collaboration** — SAP Learning Groups and expert-moderated forums
9. **Join SAP-provided bootcamps** — SAP Integration Modernization Info Days
10. **Track and certify** — digital badges, certifications (Records of Achievement, SAP Certified Associate status)
11. **Evaluate ROI** — review how enablement reduces TCO, accelerates adoption of SAP innovations, supports business transformation

---

## Key Reference Links

- L3 Integration Deck: https://dam.sap.com/mac/app/p/pdf/asset/preview/JhcAkZf?ltr=a&rc=10&doi=SAP1280564
- Clean Core Integration Whitepaper (most authoritative): https://dam.sap.com/mac/u/a/x9YTRSn?rc=10&doi=SAP1327955
- SAP Business Accelerator Hub: https://hub.sap.com
- SAP Note 3690029 (integration technologies): https://me.sap.com/notes/3690029
