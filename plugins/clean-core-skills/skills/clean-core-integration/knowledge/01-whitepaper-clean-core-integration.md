# Clean Core Integration — Whitepaper

**Source:** Clean Core Integration Whitepaper  
**Document ID:** SAP1327955 | Link: https://dam.sap.com/mac/u/a/x9YTRSn?rc=10&doi=SAP1327955  
**Published:** 2026  
**Ingested:** 2026-09-13  
**Audience:** Enterprise Architects, Integration Architects, TQMs  
**Purpose:** Strategic reference and authoritative guidance on clean core integration — architectural patterns, governance, stay-clean/get-clean journeys, KPI framework. Most authoritative and up-to-date source for integration.

---

## Preface: Autonomous Enterprise and Clean Core

Enterprises are entering a new era in which AI can facilitate collaboration among people, processes, and systems with greater speed, precision, and resilience. The **Autonomous Enterprise** embodies this vision — a business that can sense change, recommend actions, automate routine decisions, and continuously improve outcomes, all while keeping people in control of strategy, governance, and exceptions.

For established SAP customers, RISE with SAP provides a guided path toward that future by connecting trusted ERP processes, business data, and industry expertise to modern cloud capabilities and embedded agentic AI. Clean core principles are essential in this context: by reducing unnecessary complexity, standardizing non-differentiating processes, managing extensions in a modern, upgrade-stable manner, and improving data and process quality, customers create a foundation for faster innovation and lower operational risk.

---

## Executive Summary

As enterprises accelerate their transformation toward cloud-centric SAP landscapes, effective integration has become critical to long-term success. The design, governance, and operation of integrations ultimately determine stability, agility, and the amount of technical debt associated with upgrades.

This whitepaper presents the **clean core integration strategy**: architectural principles, design guidelines, governance models, and operational practices that enable organizations to efficiently integrate systems while protecting the integrity of the SAP core.

**Five key topics:**
1. The clean core integration classification defined in SAP Note 3690029
2. Three architectural patterns (central middleware, API-managed, event-driven)
3. Governance using SAP Integration Solution Advisory Methodology (ISAM)
4. "Stay clean" and "get clean" transformation journeys
5. The clean core measurement framework (KPIs)

**Benefits of clean core integration:**
- Reduce integration-related technical debt
- Improve upgrade stability and reduce regression risk
- Simplify integration maintenance and operations
- Increase resilience and transparency across end-to-end processes

---

## 1. Introduction

Enterprise landscapes are undergoing a fundamental shift. SAP customers are moving toward cloud-centric architectures, adopting continuous delivery models, and integrating an ever-growing ecosystem of SAP and non-SAP applications. Integration is not just a technical issue; it is a **strategic capability** that directly affects business resilience, the speed of innovation, and long-term sustainability.

Historically, integration in SAP landscapes has evolved in a fragmented way: point-to-point connections, custom-built interfaces, and tightly coupled logic embedded in the ERP core. While initially effective, these approaches accumulate technical debt, resulting in fragile landscapes that are difficult to upgrade, operate, and adapt.

The clean core approach provides a guiding framework: maintaining a stable, standard, and upgradeable ERP core while enabling flexibility and innovation at the edges. Clean core integration promotes loose coupling, standardized and versioned integration interfaces, platform-based orchestration, and end-to-end transparency.

### 1.1 Important Clarifications

#### 1.1.1 Contracts in the Context of Clean Core Integration

A **contract** refers to released, stable interfaces that define how systems interact — typically APIs or business events representing the only supported way to access or exchange data with the SAP core.

Contracts define:
- The structure and semantics of exchanged data
- The allowed operations or event types
- The stability guarantees across upgrades

SAP categorizes APIs based on release status (the C0–C2 classification):
- **C0:** Not released — internal use only, no stability guarantees
- **C1:** Released for local (in-system) consumption
- **C2:** Released for remote consumption — intended for external integration scenarios

From a clean core integration perspective, **C2 APIs are the primary contract** for system-to-system integration. They are designed to remain stable across upgrades and form the foundation for API-managed connectivity.

#### 1.1.2 Integration Levels in the Context of Clean Core

SAP Note 3690029 defines four integration levels classifying technologies and patterns based on clean core compliance, upgrade stability, and architectural characteristics:

| Level | Name | Description | Status |
|---|---|---|---|
| **A** | Strategic, clean-core-compliant | Released APIs (C2), business events, modern integration technologies (API management, EDA). Integration logic decoupled from the SAP core and handled via platform services. | Target state for all integrations |
| **B** | Acceptable with limitations | Supported but with constraints in upgrade stability or flexibility. Older patterns still valid but not fully aligned with strategic direction. | Transitional state, acceptable where no better option exists |
| **C** | Limited clean core alignment | Technologies not aligned with modern integration practices. Introduce tighter coupling, reduced transparency, or increased lifecycle effort. | Candidates for modernization |
| **D** | Non-compliant / partially supported | Do not align with clean core principles. Often rely on direct access to internal artifacts or obsolete technologies. Not supported in modern SAP landscapes, especially cloud. | Should be avoided or replaced |

All recommended architectures, patterns, and practices in this whitepaper align with **Level A** integrations. Levels B–D are treated as transitional or legacy states that require governance and modernization.

---

## 2. Why a Clean Core Is Important for Integration

### 2.1 Overcoming Obstacles and Unlocking Innovation

Many organizations pursuing frequent innovation cycles encounter recurring integration challenges:
- **Excessive point-to-point connectivity** — difficult to govern, hard to reuse, costly to maintain
- **Tight coupling between integrations and ERP internals** — custom logic like user exits and unreleased interfaces create hidden dependencies that significantly increase upgrade effort and risk
- **Unclear interface ownership, limited versioning strategies, weak lifecycle management** — overreliance on legacy interfaces or outdated prebuilt content
- **Limited operational visibility** — without centralized monitoring, alerting, and traceability, integration issues are detected late; operations teams forced into reactive firefighting

### 2.2 Why Clean Integration Is Beneficial

| Benefit | Detail |
|---|---|
| **Upgrade stability** | Decoupling integrations from the ERP core and relying on SAP-released APIs minimizes in-core changes during upgrades. Orchestration and transformation logic handled on the integration platform. |
| **Transparency** | Interfaces are cataloged, architectural decisions recorded through structured integration assessments, custom or legacy integrations clearly identified. Speeds up error resolution, makes technical debt visible and actionable. |
| **Flexibility** | API-first and event-driven patterns enable composability and reuse across business scenarios. New consumers or processes added without destabilizing the ERP core. |
| **Technical versatility** | Platform integration capabilities (managed runtimes, eventing, API management, centralized monitoring) protect ERP performance, reduce TCO, enable scalable operations. |

---

## 3. What a Clean Core Means for Integration

### 3.1 Integration as Part of the Five Guiding Principles of Clean Core

The five guiding principles:
1. **Business processes** — Maintain competitiveness while reducing complexity
2. **Extensibility** — Decouple extensions from the standard core
3. **Data** — Control data according to the latest standards
4. **Integration** — Keep the landscape reliable and flexible
5. **Operations** — Maintain effective and efficient operations

Integration acts as a **connective layer across all other principles**:
- **Business processes:** Enables end-to-end process execution across systems without fragmenting logic
- **Extensibility:** Relies on stable, well-documented APIs; extensions delivered side-by-side or on-stack consuming reliable APIs; orchestration on dedicated integration platforms
- **Data:** Standardized interfaces and event-based communication improve data consistency, reduce redundancy, ensure clear data ownership
- **Operations:** Centralized monitoring, error alerting/handling, security enforcement, and lifecycle management are required to ensure transparency, auditability, and compliance

### 3.2 What Is "Clean Integration"?

Clean integration is defined by these characteristics:

- **Released and stable interfaces** — APIs and events explicitly intended for integration use, supported across upgrades, treated as formal contracts
- **Orchestration and transformation logic on the platform layer** — SAP S/4HANA Cloud Private Edition focuses on executing business processes; integration platforms handle routing, mapping, enrichment, and sequencing
- **Standard content-first approach** — Prepackaged integration content used wherever possible; "copy-and-extend" pattern preferred over rebuilding from scratch; enterprise-specific integration patterns and templates for consistency and reuse
- **Secure-by-design connectivity** — Authentication, authorization, and data protection centrally enforced
- **Centralized monitoring** — Errors detectable, diagnosable, and resolvable through centralized monitoring without requiring deep technical intervention in the SAP core (e.g., SAP Cloud ALM)
- **Defined integration strategy** — Establishes how integrations are designed, governed, and evolved across the enterprise. Structured approaches like SAP ISAM define integration domains, styles, patterns, and guiding principles
- **Structured integration assessment process** — Each requirement evaluated using standardized criteria to determine the most appropriate integration style, interface type, and architectural pattern

### 3.3 Integration Architecture: Central Middleware, API-Managed, and Event-Driven

A clean integration architecture combines three complementary approaches:

#### 3.3.1 Central Middleware Approach — SAP Integration Suite

SAP Integration Suite is an enterprise-grade integration platform as a service on SAP BTP. It serves as the **recommended central middleware** for A2A, B2B, B2G, and master data integration scenarios.

Key capabilities:
- **Cloud Integration** — end-to-end process integration
- **API Management** — secures and governs APIs
- **Trading Partner Management + Integration Advisor** — B2B scenarios
- **Advanced event mesh** — event-driven architectures
- **Open Connectors** — third-party connectivity
- **SAP Business Accelerator Hub** — library of pre-built integration content
- **Edge Integration Cell** — runs integration content in customer-managed private landscapes for deployment or data residency requirements
- **Migration Assessment capability** — estimates migration effort from SAP Process Integration/Process Orchestration, with semi-automated migration tooling

**When to use central middleware:** When many systems require standardized connectivity and protocol translation; when point-to-point integrations have proliferated and governance is weak; when centralized security, auditing, and monitoring are required across a broad integration landscape.

#### 3.3.2 API-Managed Connectivity

API-managed connectivity structures integrations into reusable, governed building blocks that separate concerns such as exposure, mediation, and consumption. Core is **SAP API Management within SAP Integration Suite** acting as a central API gateway.

API Management enforces:
- Security (authentication and authorization)
- Traffic management (throttling, quotas)
- Protocol mediation and lightweight transformations
- Monitoring, analytics, and policy enforcement

This protects backend systems (SAP S/4HANA) from direct access and keeps them decoupled from consumers.

Additional capabilities:
- **Cloud Integration** — complex message transformations, routing, and orchestration beyond simple API mediation
- **SAP Business Accelerator Hub** — predefined APIs and integration content, policy templates, discoverable and reusable assets
- **Graph capability** — exposes business data as a semantically connected API across multiple underlying data sources
- **SAP Connectivity services** — cloud connector and destination service for hybrid connectivity (cloud-to-cloud, cloud-to-on-premises, on-premises-to-on-premises)
- **Developer Hub** — primary access point for API consumers; approved APIs are documented, versioned, secured, and discoverable
- **Application Interface Framework (AIF)** — monitoring, error handling, and operational transparency for backend integration with SAP S/4HANA or SAP ECC

**How to use:** (1) Expose backend capabilities via API Management using API proxies with centralized policies; (2) Separate simple API exposure from complex integration logic — use API Management for lightweight mediation, Cloud Integration for advanced transformations; (3) Start with standard content and predefined APIs from SAP Business Accelerator Hub; (4) Enable secure hybrid connectivity via SAP Connectivity services; (5) Provide centralized API governance and discoverability; (6) Combine APIs with event-driven patterns for asynchronous scenarios; (7) Ensure operational monitoring and control across API Management, Cloud Integration, and backend systems.

**When to use:** Backend systems must be protected from direct access; strong governance, security, and policy enforcement required; APIs need to be reusable across multiple consumers; partner and third-party integrations require standardized interfaces.

#### 3.3.3 Event-Driven Integration

Event-driven integration focuses on reacting to business events rather than invoking systems synchronously. Producers publish events when something relevant occurs; consumers subscribe independently.

Benefits:
- **Loose coupling** — producers do not need to know who consumes the event
- **Scalability and resilience** — decoupling senders and receivers, processing asynchronously absorbs peak loads, reduces cascading failure risk
- **Business semantics** — events represent business facts rather than technical calls

**When to use:** Real-time or near-real-time notifications required; multiple receivers need to react independently; tight coupling must be avoided; peak-load buffering and elastic consumption important; resilient asynchronous integration designs preferred.

**How to use (standard-first):**
1. Discover available SAP standard business events via SAP Business Accelerator Hub (prefer released events before designing custom ones)
2. Select broker capability: SAP Event Mesh (standard publish/subscribe) or Advanced Event Mesh (large distributed landscapes requiring streaming + lifecycle governance)
3. Enable event publication from SAP S/4HANA using Enterprise Event Enablement
4. Design topics and schemas for long-term stability — define topic taxonomy (domain/object/action/version), apply schema versioning
5. Set up reliable consumption — queues, subscriptions, retry patterns, idempotency, dead-letter handling
6. Make it operable — govern events like APIs: assign owners, define lifecycle states, document purpose and consumers

**Custom events:** Only when no suitable SAP standard business event exists. Treat as contracts: define topic taxonomy, ownership, lifecycle state, and schema/versioning. To extend payload without breaking consumers, use derived RAP business events.

**Notification vs. data events:** SAP standard events are typically notification events (signal that "something happened"). Notification events minimize payload size and coupling; data events carry full business context. Choice driven by specific use case.

#### 3.3.4 Choosing Between the Three Patterns

The three patterns are **not mutually exclusive** — they serve different purposes and are often used together:

- **Central middleware** → when many systems need standardized connectivity, governance and lifecycle control are weak, centralized security and auditing required
- **API-managed** → for direct synchronous interactions, posting data, triggering follow-up actions, retrieving information where immediate confirmation is required; if no transformation/routing needed, APIs can be consumed directly without middleware (provided governance requirements are met)
- **Event-driven** → when decoupling and asynchronous processing are priorities; events signal that something has happened, allowing consumers to react independently without tight dependencies

### 3.4 Best Practices in Clean Core Process Integration

Clean core integration starts with intentional design decisions. Rather than treating every integration requirement as custom development, clean core integration prioritizes **standardization, reuse, and architectural consistency**.

#### 3.4.1 Standard Content and Released Interfaces

**Standard-first decision path:**

1. **Standard integration scenario, released API, or event available and sufficient** → use as-is (cleanest and most upgrade-stable option)
2. **Standard scenario exists but requires local changes** → use standard extension points per the cloudification repository; if no extension points, adopt standard content with minimal adjustments per SAP Note 3578329
3. **No SAP standard content exists** → if adoption with minor changes possible: follow SAP Note 3578329; if not possible: build a custom interface strictly adhering to clean core extensibility guidelines

Always consult SAP Note 3690029 to understand the impact on clean core integration and cloud readiness of the chosen technology or protocol.

Key building blocks:
- **SAP Business Accelerator Hub** — prepackaged integration content, integration content catalog, SAP-recommended integration logic, mappings, and connectivity patterns
- **Released APIs and business events** — stable technical contracts between systems, maintained with backward compatibility, explicitly intended for integration use

#### 3.4.2 Use of Traditional Interfaces

Prefer modern alternatives (released APIs and business events) whenever available. They deliver stronger governance, better security, improved scalability, and higher upgrade stability.

If no modern alternative exists and a traditional interface has not been deprecated, its **temporary use may be acceptable**, provided:
- The interface is clearly documented
- Ownership is defined
- The integration is explicitly identified as a candidate for future modernization

Traditional interfaces are treated as **transitional solutions, not permanent architectural choices**. A clean-core-aligned organization maintains a clear modernization plan for these scenarios.

#### 3.4.3 SAP API Policy

On April 27, 2026, SAP introduced a formalized **API policy** published on the SAP Help Portal. The policy distinguishes three interface categories:

- **Published interfaces** (listed on SAP Business Accelerator Hub, SAP Help Portal, or dedicated portals) — supported and may be used within their documented API controls
- **Other SAP-internal interfaces** — neither published nor explicitly prohibited; may still be used where authorized by SAP; may be changed or removed without notice
- **Prohibited interfaces** — designated confidential and proprietary by SAP, or flagged as not permitted by tools like the ABAP Test Cockpit (currently: ODP-RFC interface, as specified in SAP Note 3255746)

**Four common misunderstandings:**

| Myth | Reality |
|---|---|
| "The API policy is Level E of clean core." | The API policy is a separate governance framework, not an extension of the clean core extensibility level concept. |
| "If I follow clean core, I'm automatically API policy compliant." | Clean core guides you toward stable APIs but does not cover API use compliance. These are separate concerns. |
| "If I'm API policy compliant, I don't need to care about clean core." | API policy compliance does not protect you from upgrade costs caused by using unstable APIs. |
| "Most customers are at risk of API policy violations." | SAP does not expect existing integrations using APIs for documented purposes to be impacted. |

#### 3.4.4 Clean Core and API Policy Scope

Clean core and the API policy are **two independent, orthogonal governance dimensions**:
- **Clean core** (Level A–D) describes how customer extensions are built and maintained — architectural quality and upgrade stability
- **API policy** governs how SAP-provided interfaces are used — documented purposes, use cases, controls, usage limits, security requirements

Together they form a coordinate system. Clean core level does not determine API policy compliance. Prohibited usage patterns apply across all levels A–D, including: systematic/large-scale data extraction outside SAP-endorsed architectures, unendorsed agentic or AI access, and circumventing API controls.

### 3.5 Integration Design Guidelines

#### 3.5.1 SAP Integration Suite: Core Qualities of Enterprise-Grade Integration Flows

| Quality | Description |
|---|---|
| **Loose coupling and API-first design** | Avoid direct database access, internal tables, in-core modifications. Systems interact through released APIs and business events. SAP provides checks through the Cloudification Repository Viewer to enforce compliance. |
| **High availability and resilience** | Integration flows gracefully handle failures through retries, idempotency, timeout handling, and failure isolation. |
| **Graceful error handling** | Failures do not disrupt core operations. Errors handled asynchronously where possible, logged centrally, surfaced through monitoring. |
| **Readability and maintainability** | Integration flows are modular, consistently structured, easy to understand. Standard naming, documentation, and reusable patterns. |
| **Efficient resource usage** | Optimize payloads, call frequency, and processing logic. Ensures predictable performance and lower TCO. |

**What implementation guidelines should cover:**
- Scenario design standards — patterns, naming conventions, documentation, interface classification
- Integration qualities — security, resilience, performance, error handling
- Connectivity configuration — secure and standardized system connectivity
- Lifecycle management — transport, testing, versioning, release, and deprecation
- Monitoring strategy — expert and end-to-end monitoring, including ownership and alerting

#### 3.5.2 SAP Cloud ERP Private ABAP Integration Design Guidelines

Integration governed by **ABAP Cloud principles**, supporting:
- **Process integration** — end-to-end business processes with coordinated communication across applications
- **Data integration** — data exchange between systems without tight process coupling
- **Event-driven integration** — propagates significant business events (state changes) to trigger follow-up actions

Key design requirements:
- **Clear provider/consumer model** — Inbound: SAP S/4HANA exposes services for external consumption; Outbound: SAP S/4HANA consumes services or sends data/events to other systems
- **Standard protocols** — HTTP-based services (OData or SOAP); RFC for compatibility scenarios only
- **ABAP cloud compliance** — only released objects, APIs, and extension points used; ensures upgrade safety

### 3.6 Integration Extensions

#### 3.6.1 Extensions for SAP Cloud ERP Private

Integration extensions must be designed in alignment with clean core principles:
- Use released objects and APIs only; avoid access to internal tables or unreleased artifacts
- Leverage SAP-supported extensibility options: key user extensibility, developer extensibility, released extension points
- Extensions clearly separated from standard code, transparently documented
- Use the ABAP Cloud model and related checks via the Cloudification Repository Viewer

Detailed guidance: SAP Note 3578329 and the broader SAP S/4HANA extensibility framework.

#### 3.6.2 Integration Flow Extensions

**Key principle:** Never modify standard integration artifacts directly. Implement customer-specific extension logic only through **explicitly defined extension points** (pre-exit or post-exit extension steps).

Layered approach:
- **Standard integration flow** — SAP-owned and maintained; defines canonical message structures, process logic, and interaction patterns; stable across releases
- **Customer-specific extension content** — added only at defined extension points; allows enrichment, conditional processing, custom field handling

Benefits: Standard content remains fully upgradeable; customer-specific logic is isolated and explicit; clear ownership boundaries between SAP-delivered content and customer extensions.

### 3.7 Governance: Integration Center of Excellence (ICoE) and SSB

#### 3.7.1 Integration Center of Excellence (ICoE)

The ICoE acts as the **centralized responsibility and coordination function** for integration. Its purpose is not to become a delivery bottleneck but to provide structure, guidance, and reuse at scale.

ICoE responsibilities:
- **Defining and curating best practices** — integration principles, design standards, reference architectures
- **Maintaining reusable assets** — shared patterns, templates, mappings, APIs, event definitions
- **Coaching and enabling delivery teams** — guidance, reviews, enablement
- **Providing cross-technology oversight** — architectural coherence across integration approaches and deployment models
- **Enabling self-service** — centralized access to integration catalogs, documentation, decision records, guidelines

#### 3.7.2 Solution Standardization Board (SSB)

The SSB provides **formal governance over deviations from standard processes and architectures**. It sits above the ICoE and handles decision-making outside the ICoE's authority.

SSB responsibilities:
- Evaluating deviations from standard processes
- Assessing proposed designs against clean core principles and architectural "golden rules"
- Ensuring documentation, risk transparency, and awareness of long-term impacts (including upgrade implications)
- Driving cross-team alignment across programs and system landscapes

The SSB reinforces a **fit-to-standard mindset** by acting as the decision-making body for requirements that cannot be fulfilled using standard capabilities.

#### 3.7.3 Decision Logging and Integration Assessment

Clean core integration relies on structured decision logging supported by formal integration assessments.

A standardized assessment approach (ISAM-based) supports:
- Consistent decision-making — uniform criteria and evaluation logic across all integration scenarios
- Standardized questionnaires and evaluation criteria — covering architecture selection, interface choice, coupling level, security, resilience, operational impact
- Traceable rationale — documenting why a specific architecture, technology, or interface was chosen, including alternatives considered and rejected

Together, the ICoE, SSB, and structured decision logging form a **governance framework that enables clean core integration at scale**.

### 3.8 End-to-End Monitoring and Operational Excellence

Operational excellence means full transparency across technical components and end-to-end business processes while maintaining lean operational costs. This requires embedding operational efficiency considerations into the assessment and design phases — monitoring and support requirements must be architected from the beginning, not added later.

#### 3.8.1 ICoE-Driven Operational Framework

The ICoE establishes a structured error resolution process:
- **Error recognition and proactive monitoring** — automated alerting across all monitoring layers; cost-optimized alerting strategies that prevent alert fatigue
- **Analytics-driven resilience** — historical monitoring data and trend analysis identify systemic weaknesses and drive continuous improvement
- **Reactive response framework** — structured access to expert and end-to-end monitoring; clear technical and functional ownership for efficient escalation and resolution
- **CI/CD-enabled resolution** — error resolution leverages established pipelines to deploy fixes consistently across environments

#### 3.8.2 Monitoring Layers

**Expert monitoring tools (in-depth, component-level visibility for root cause analysis):**
- **SAP Application Interface Framework (AIF)** — detailed monitoring without embedding logic into core business processes; supports business users with self-service capabilities for resolving common issues
- **SAP Integration Suite built-in monitoring** — across runtime components: cloud integration, API management, event mesh, B2B integration

Expert monitoring tools empower business users with self-service capabilities, enabling functional experts to identify and resolve routine issues independently (data validation errors, missing master data, processing status inquiries) without escalating to technical teams.

**End-to-end monitoring (connects technical message flows with business context):**
- **SAP Cloud ALM** — central end-to-end monitoring view of SAP Integration Suite, SAP Cloud ERP Private, and connected cloud services; enables tracking of business context, correlation of message paths, alerting, and analytics across integration scenarios

#### 3.8.3 Common Monitoring Capabilities

| Capability | Description |
|---|---|
| **Monitoring** | Visibility into status of interfaces and message flows — success/failure states, processing times, availability indicators |
| **Alerting** | Automated notifications to clearly defined integration owners when thresholds or error conditions are met; integrated with email, collaboration, or ticketing systems |
| **Analytics** | Historical and trend-based analysis of message volumes, failure rates, performance metrics to identify systemic issues and optimization opportunities |
| **Tracking** | Search and trace capabilities based on business-relevant attributes with correlation across systems |

#### 3.8.4 Guiding Principle

ICoE-governed operational excellence is a **foundational pillar of clean core integration, not an afterthought**. Without structured, cost-conscious operational processes, transparency is reduced, issues are detected later, and operational risk increases. Efficient ICoE-driven monitoring and resolution processes enable predictable operations, reduce downtime, and significantly lower the total cost of ownership.

---

## 4. How to Achieve a Clean Core for Integration

Achieving a clean core requires understanding two distinct yet complementary processes: **"stay clean"** and **"get clean"**.

Both processes are typically structured as follows:
- Unlock agility and innovation with a future-ready integration strategy
- Accelerate productivity and efficiency with best practices and modern technologies
- Embed operational excellence to ensure reliability and adaptability
- Institutionalize continuous optimization to enable ongoing innovation

### 4.1 Stay Clean: How to Create and Sustain Clean Integrations

"Stay clean" incorporates clean core principles into demand intake, architecture, delivery, and operations. It:
- Prevents the accumulation of new technical debt
- Protects the target architecture from gradual architecture drift
- Sustains a clean core and stable business outcomes

**Implementation steps:**
1. Define governance and guidelines based on SAP ISAM characteristics — establish decision criteria, document decision rationale, starting with a comprehensive integration strategy
2. Model business requirements (e.g., SAP Signavio) and create the corresponding integration architecture (e.g., SAP LeanIX)
3. Capture integration requirements in dedicated requirements management tools
4. Conduct an integration assessment using SAP ISAM via the SAP Integration Suite integration assessment capability
5. Implement using SAP Cloud ALM and SAP Integration best practices
6. Document all interfaces comprehensively in SAP LeanIX

#### 4.1.2 Integration Assessment

Every new integration requirement should follow a formal assessment process. An effective integration assessment captures:
- Business context: what business process triggers the requirement, which systems act as sender and receiver, which business objects are exchanged
- Technical characteristics: message volume, business criticality, synchronous vs. asynchronous, transformation and routing requirements, security and compliance constraints, reuse potential

Outputs of an integration assessment:
- The selected integration style and pattern
- A technology recommendation (e.g., API-managed or event-driven, including appropriate runtime profile)
- A documented architectural rationale
- Clearly defined ownership and lifecycle responsibility

#### 4.1.3 Architecture Selection and Technology Mapping

Based on SAP Note 3690029 and chapters 3.3 and 3.4. Custom integrations must maintain transparency — due to their impact on upgrade stability and long-term maintainability, custom-built interfaces are classified and monitored.

#### 4.1.4 Implementation Guardrails

- Enforce consistent naming, documentation, and artifact standards across all integration flows
- Require explicit versioning and defined ownership for every interface
- Centralize security policy enforcement at the API layer
- Prefer asynchronous interaction patterns where feasible
- Avoid point-to-point proliferation by standardizing shared patterns, reusable building blocks, and centralized orchestration
- Use released interfaces and standard integration content as the default implementation baseline
- Ensure monitoring coverage for both expert-level and end-to-end visibility

#### 4.1.5 Deployment, Lifecycle, and Continuous Review

- Define clear release and transport practices across development, testing, and production environments
- Implement comprehensive testing strategy covering unit testing and end-to-end process validation
- Define versioning and deprecation policies to prevent outdated interfaces from becoming permanent legacy artifacts
- Lifecycle management linked to clean core measurement KPIs (upgrade stability, operational risk, innovation adoption)

### 4.2 Get Clean: How to Modernize Existing Integrations

"Get clean" addresses the existing integration landscape — a structured effort to modernize and reduce accumulated technical debt, transitioning from fragmented, tightly coupled integrations to standardized, upgrade-safe, and governable integration patterns.

#### 4.2.1 Discover and Document the Current State

Organizations must create a comprehensive view of existing integrations by:
- Establishing or completing an interface repository
- Linking interfaces to business processes and responsible ownership
- Capturing integration technologies used, business criticality and usage patterns, lifecycle status

#### 4.2.2 SAP LeanIX as the Integration Repository

SAP LeanIX acts as the **central Integration Repository and system of record** for integration architecture documentation. Interface fact sheets capture: sender, receiver, middleware, integration pattern, business object, ownership, lifecycle status, criticality, links to applications and business processes. Creates a governed view enabling impact analysis, modernization planning, and clean-core compliance tracking.

#### 4.2.3 Assess and Prioritize Modernization

Typical prioritization criteria:
- Business criticality and customer impact
- Technical obsolescence and security exposure
- Complexity and dependency across systems
- Feasibility and resource readiness
- Reuse potential and alignment with target architecture
- Cost-benefit and time sensitivity

#### 4.2.4 Migration Assessment and Modernization Recommendations

Each integration is evaluated to determine its future state:
- **Ready for modernization** — can be transitioned directly to modern patterns
- **Requires adjustment** — can be modernized with moderate changes (protocol upgrades, mapping simplification, improved decoupling)
- **Requires further evaluation** — complex dependencies or constraints require deeper analysis

Based on this classification, modernization recommendations are defined:
- Adoption of released APIs or business events
- Replacement of legacy protocols with modern, HTTP-based interfaces
- Simplification or redesign of transformation and routing logic
- Decoupling of tightly integrated systems

#### 4.2.5 Road Map Execution Model

Typical execution principles:
- **Focus on quick wins first** — replace high-risk, low-effort integrations to demonstrate early value
- **Prioritize high-value domains** — revenue generation, supply chain, financial operations
- **Establish foundations early** — monitoring, interface transparency, governance standards
- **Execute in controlled waves** — align with business road maps, release cycles, and upgrade windows
- **Embed continuous "stay clean" controls** — prevent reintroduction of technical debt

#### 4.2.6 Typical "Get Clean" Use Cases

**Clean core recommendations (replacing proprietary SAP interfaces):**
- Replace RFCs/BAPIs with SOAP or OData APIs (documented on SAP Business Accelerator Hub, managed by SAP throughout lifecycle)
- Replace custom interfaces with SAP pre-delivered packages
- Replace IDocs with SOAP/OData APIs or Business Events (real-time integration, reduced latency, better scalability)

**Integration style recommendations:**
- Multiple receivers async Business Event — replaces point-to-multipoint routing
- IDoc → Business Event — where message size and complexity should be minimized
- Polling → Push — for near-real-time and alert notification scenarios

**Mapping modernization:** Java and ABAP mappings → Graphical, XSLT, or Groovy Script mapping in SAP Cloud Integration

**Monitoring modernization:** Alert rules from SAP Process Orchestration → alert notification service on SAP Cloud ALM

**Protocol and security modernization:**
- File-based protocols (NFS, FTP, SFTP) → API-managed protocols (SOAP, OData, REST)
- IDoc → API-managed protocols
- RFC → API-managed protocols
- HTTP → HTTPS
- Basic Authentication → Client Certificate or OAuth 2.0

### 4.3 How to Measure Clean Core Integration (KPIs)

Clean core integration must be measurable and continuously monitored. Without clear metrics, organizations cannot track progress, identify risks, or prioritize modernization efforts.

**Four KPI categories:**

| Category | Description |
|---|---|
| **Upgrade stability** | Measures the distribution of active interface technologies in SAP Cloud ERP Private across integration levels (SAP Note 3690029), separately for process and data integration. A clean core target state maximizes the share of standard, upgrade-safe and modern interfaces. |
| **Operational risk** | Measures monitoring coverage across the integration landscape using SAP Application Interface Framework (expert tool monitoring) and SAP Cloud ALM (end-to-end integration monitoring across SAP Integration Suite and connected systems). |
| **Innovation adoption** | Measures the activation and active usage of modern SAP BTP integration technologies including SAP Integration Suite and its capabilities, SAP Master Data Integration, SAP Datasphere, and SAP Business Data Cloud. |
| **Agile decision-making and operational risks** | Measures the adoption of the agent-led toolchain — SAP Signavio, SAP LeanIX, SAP Integration Suite, and SAP Cloud ALM — across the full integration requirement lifecycle, from business process linkage to architecture, assessment, and delivery tracking. |

### 4.4 Upskill and Enable Integration Experts

Sustainable adoption of clean core principles requires equipping integration teams to design, implement, and operate integrations in line with SAP-recommended approaches.

Enablement approach:
- **Assess current capabilities and identify gaps** — evaluate skills across API design, event-driven architecture, resilience patterns, security, and lifecycle management
- **Define role-based learning paths** — tailored for integration developers, integration architects, and operations teams
- **Promote hands-on learning** — practical exercises, reusable templates, structured code or design reviews
- **Leverage reusable assets and best practices** — standard content, reference architectures, reusable patterns
- **Track progress and capability maturity** — formal indicators (certifications, learning milestones) and practical outcomes (adherence to design guidelines, successful delivery of clean integrations)

### 4.5 Patterns of Success: Lessons Learned and Customer Outcomes

**Standard content-first mindset** — Successful organizations consistently prioritize standard integration content and released interfaces. They treat custom integrations as exceptions, justifying them through structured assessment and governing them accordingly.

**Balanced governance with empowered delivery teams** — Governance centralized through ICoE and SSB. Delivery teams empowered through clear guidelines, reusable assets, and self-service access to integration knowledge.

**Operational ownership and transparency** — All integrations have clearly defined ownership, lifecycle status, and monitoring coverage. No "orphaned" interfaces.

**Continuous modernization mindset** — Clean core treated as an operating model, not a one-time initiative. Regular assessment, prioritization, and improvement through structured "get clean" initiatives while "stay clean" practices prevent new technical debt.

**Customer outcomes:**
- Increased upgrade stability and reduced regression risk
- Lower operational effort due to improved monitoring and governance
- Faster delivery through reuse of standard content and integration patterns
- Greater architectural consistency and reduced complexity
- Improved ability to adopt new SAP innovations without disruption

---

## 5. Conclusion and Outlook

Clean core integration is not achieved through isolated technical decisions, but through a combination of architecture, governance, operations, and enablement. Organizations that incorporate these principles into their operating model develop integration landscapes that are resilient, scalable, and future-ready.

Future releases of this whitepaper will incorporate coverage of data integration and AI capabilities (e.g., AI on SAP Integration Suite) as the corresponding content becomes publicly available.

---

## Key Reference Links

- Integration whitepaper (most authoritative): https://dam.sap.com/mac/u/a/x9YTRSn?rc=10&doi=SAP1327955
- SAP Note 3690029 (integration levels): https://me.sap.com/notes/3690029
- SAP Note 3578329 (extensibility guidance): https://me.sap.com/notes/3578329
- SAP Business Accelerator Hub: https://hub.sap.com
- SAP API Policy: https://help.sap.com/doc/sap-api-policy/latest/en-US/API_Policy_latest.pdf
- Cloudification Repository: https://sap.github.io/abap-atc-cr-cv-s4hc
