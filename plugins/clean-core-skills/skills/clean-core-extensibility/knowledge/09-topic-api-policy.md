# SAP API Policy – Implications for Clean Core

---

## Sources

| Topic | Source | URL |
|---|---|---|
| Official policy text | SAP API Policy v4.2026a | https://help.sap.com/doc/sap-api-policy/latest/en-US/API_Policy_latest.pdf |
| Clean core impact overview (slide 6) | SAP API Policy – Sapphire 2026 Presentation | https://www.sap.com/documents/2026/04/e2a0665e-4c7f-0010-bca6-c68f7e60039b.html |
| FAQ document (v1.2, May 2026) | SAP API Policy FAQ | https://www.sap.com/documents/2026/04/e2a0665e-4c7f-0010-bca6-c68f7e60039b.html |
| Endorsed agentic AI architecture | SAP Architecture Center – AI Golden Path | https://architecture.learning.sap.com/docs/aigp |

---

## The Core Message: The API Policy Does Not Impact Clean Core

**Slide 6 of the SAP Sapphire 2026 presentation states directly:**

> "SAP's API Policy does not impact clean core.
> Custom APIs that customers build in their own namespace for integration and extensibility remain unaffected."

These are **complementary, not competing** frameworks. The API Policy governs *access to SAP-owned interfaces*. Clean Core governs *how customers build and structure their own extensions*.

---

## What the API Policy Restricts (and Does Not Restrict)

### What the Policy Targets

The API Policy restricts access to **SAP-internal, non-published APIs** — those in SAP's own namespace that are not listed on the SAP Business Accelerator Hub or in product documentation. The policy's key categories:

| Category | Status | Examples |
|---|---|---|
| **Published APIs** | Permitted (within documented controls) | APIs on SAP Business Accelerator Hub, SAP Help Portal |
| **Customer-owned code (Z/Y namespace)** | Permitted — not restricted | Custom RFCs, BAPIs, OData services, CDS views, function modules in customer namespace |
| **Undocumented SAP-internal APIs** | "At own risk" — always was | SAP-internal interfaces not on Business Accelerator Hub; used without SAP stability guarantee |
| **Explicitly prohibited APIs** | Not permitted | APIs designated "Confidential/Proprietary", flagged by SAP Note or ATC as "not permitted" (e.g. ODP-RFC) |

**FAQ Q26 states explicitly:** The policy's restriction on non-published APIs "leaves custom APIs built by customers in their own namespace for their own extensibility, integration, and migration purposes unaffected." The policy "does not reach into the Z namespace and condemn two decades of legitimate ABAP engineering."

---

## What This Means for Clean Core Customers

### Custom Extensions in Customer Namespace: No Change

Custom code that customers have built in their own SAP-system namespace — including customer-namespace ABAP interfaces, OData services via SAP Gateway, CDS views, and custom RFC modules — are considered "custom-developed" interfaces under the API Policy.

- **The policy's restriction is not per se applied to this code.**
- Compliance of custom code is determined by the **underlying SAP components it calls** — any calls from custom code to SAP's own APIs must adhere to the API Policy.
- It is not permitted to create custom APIs as a workaround to circumvent API controls (e.g., proxying prohibited interfaces like ODP-RFC).

### Clean Core Classification Still Applies to Custom APIs

Even though customer-namespace custom APIs are not prohibited by the policy, **clean core classification still governs how they are built**. FAQ Q28 specifies what "documented and governed" means for custom APIs:

1. **Internal API inventory**: Registry of custom APIs per system (namespace, interface type, purpose, owning team, and — critically — the Clean Core dependency level)
2. **Clean Core classification**: Each custom API classified by the level of its underlying SAP objects, using the ABAP Test Cockpit Cloud Readiness Check and the Cloudification Repository Viewer
3. **Standard development governance**: ATC checks, code review, test automation, transport management

This directly links clean core tooling to API Policy compliance management for custom code.

---

## ATC Extension for API Policy Compliance

One concrete technical implication of the API Policy for clean core tooling:

**FAQ Q10 states:** SAP will extend the Cloudification Repository with additional tags for explicitly prohibited APIs, so that calls to those objects are automatically flagged in ATC and Cloud Readiness runs.

- SAP's Cloudification Repository-based ATC checks already distinguish released from non-released objects using JSON classification
- The extension will add tags for **explicitly prohibited APIs**
- ATC and Cloud Readiness Check runs will automatically surface these as findings
- The S/4HANA Simplification Item Catalog and `/SDF/RC_START_CHECK` report will also flag prohibited interface usage

**FAQ Q30 confirms** the tools to assess exposure:
- **ABAP Test Cockpit (ATC) with Cloud Readiness Check**: Identifies dependencies on non-published SAP interfaces in custom code
- **SAP Integration Assessment**: Discovers and analyzes the integration landscape for high-risk patterns

This means that existing ATC clean core check setups (see `knowledge/05-topic-atc-setup.md`) will automatically pick up API Policy-relevant findings when SAP extends the Cloudification Repository — no separate tooling required.

---

## RISE with SAP Transformation: No Retroactive Impact

FAQ Q26 addresses the RISE journey specifically:

- SAP honors the investment customers have made in integrating their existing SAP ERP systems, including custom data services, custom RFCs, and ABAP interfaces
- Private Cloud customers "retain the ability to build and extend in their own namespace; this freedom is not being revoked"
- SAP's Private Cloud customers are in "a distinctly privileged position" because they have long been able to build in their own namespace

FAQ Q24 clarifies: SAP does **not retroactively invalidate** existing integrations using undocumented APIs as a policy enforcement action. For the vast majority of such usage, the situation is unchanged: "at own risk" usage meaning they can continue but without SAP stability or support guarantees.

**Important scoping note for RISE customers (FAQ Q29):** Remediation of customer-built integrations that rely on non-published SAP APIs is **not automatically included** in standard RISE scope — customers should explicitly discuss integration remediation scope, timeline, and commercial provisions during contract negotiation.

---

## ADT-Based Developer Access (Clarification for Clean Core Tooling)

FAQ Q33 clarifies the scope of ADT-based access:

- ADT (ABAP Developer Tools) APIs are SAP-internal APIs **endorsed for development tooling only**
- Endorsed channels: SAP-published Eclipse ADT (primary supported client), abapGit, SAP-provided developer tools, CI/CD pipelines using SAP-published tooling, custom utilities built on the documented Eclipse Java SDK
- ADT APIs **may not** be used for: programmatic reading of application tables, SQL execution against SAP backend, business data integration, runtime orchestration, agentic AI workflows on business data, or substitution for business APIs

This is relevant for clean core tooling teams using ADT-based automation for ATC pipeline integration — the use case of CI/CD-based code checks using SAP-published tooling is explicitly endorsed.

---

## Endorsed Architectures for AI and Data (Context for Customers Asking "What Instead?")

The API Policy prohibits two categories of non-endorsed access patterns (Section 2.2.2 of the policy):
1. Interaction/integration with autonomous or generative AI systems that plan, select, or execute sequences of API calls
2. Scraping, harvesting, or systematic large-scale data extraction — except through SAP-endorsed architectures

The endorsed alternatives are:

### Agentic AI Access
- **MCP Gateway on SAP Integration Suite**: Governed, controlled access for AI agents with proper authentication, authorization, rate limiting, and audit logging
- **Agent2Agent (A2A) Protocol**: Multi-agent collaboration scenarios; open standard under the Linux Foundation
- Reference: [AI Golden Path](https://architecture.learning.sap.com/docs/aigp), [A2A and MCP Reference Architecture](https://architecture.learning.sap.com/docs/ref-arch/ca1d2a3e/1)

### Large-Scale Data Access
- **SAP Business Data Cloud (BDC)** with Delta Sharing open protocol — supports Databricks, Snowflake, Microsoft Fabric, Google BigQuery, AWS
- **SAP Landscape Transformation Replication Server (SLT)** — real-time replication; existing SLT use cases remain permitted under the API Policy with no new limits
- **Analytical CDS Views** — OData V4 analytical services for analytical consumption below full-dataset replication granularity

---

## How Clean Core and API Policy Work Together: Summary

| Aspect | Clean Core | API Policy |
|---|---|---|
| **Purpose** | Architectural discipline for upgrade-safe, cloud-ready extensions | Governance framework for API access, security, and fair use |
| **Scope** | Customer's own code and extension practices | SAP-owned interfaces and how they are consumed |
| **Applies to customer namespace code** | Yes — recommends Level A/B, discourages Level C/D | No — customer namespace code is not restricted by the policy |
| **Key tool** | ABAP Test Cockpit (ATC) clean core checks | ATC Cloud Readiness Check (being extended for prohibited API flags) |
| **Complementary?** | Yes — clean core Level A/B approach automatically aligns with the API Policy | Yes — following clean core guidance leads to API Policy-compliant extensions |
| **Primary concern** | Upgrade stability, maintainability, technical debt | Security, platform stability, fair access, agentic AI governance |

**The key insight:** A fully clean core Level A extension uses only released ABAP Cloud APIs — these are by definition published APIs on the SAP Business Accelerator Hub, making them automatically API Policy-compliant. Clean core is both an architectural discipline and the practical path to API Policy compliance for custom extension code.

---

## FAQ Reference: Top Clean-Core-Relevant Questions

| Q# | Question | Short Answer |
|---|---|---|
| Q1 | What is the API Policy? | Harmonized framework for API availability, controls, monitoring across SAP portfolio |
| Q2 | Does it change customer entitlements? | No — APIs remain available as documented |
| Q10 | Will existing integrations break? | No — SAP will extend ATC with prohibited API flags; existing compliant integrations unaffected |
| Q23 | How to determine which APIs are allowed? | Published APIs on API Hub/Help Portal; customer namespace custom code is permitted; undocumented APIs "at own risk"; prohibited APIs flagged by SAP Note/ATC |
| Q26 | How does the policy affect the RISE journey? | Customer namespace custom code unaffected; freedom to build in own namespace preserved |
| Q27 | How are custom-developed APIs affected? | Not prohibited per se; compliance determined by underlying SAP components called |
| Q28 | What does "governed" mean for custom APIs? | Maintain internal API inventory with clean core classification; use ATC Cloud Readiness Check |
| Q30 | Tools to assess non-compliance exposure? | ABAP Test Cockpit with Cloud Readiness Check; SAP Integration Assessment |
| Q33 | How does the policy apply to ADT-based access? | Endorsed for development tooling only (ADT, abapGit, CI/CD checks) — not for business data access |
