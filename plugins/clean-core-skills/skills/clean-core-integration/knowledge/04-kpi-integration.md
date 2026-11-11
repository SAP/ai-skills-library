# Clean Core Integration — KPI Detail

**Source:** Clean Core KPI Measurement Deck (SAP1240359 v1.3) — Integration section (Slides 51–64)  
**Ingested:** 2026-09-13  
**Purpose:** Full per-KPI calculation detail, measurement guidance, prerequisites, cadence, and governance & maturity relevance for all Integration KPI categories.

---

## Integration KPI Context (Slides 52–53)

### Why Integration KPIs Matter — Expected Customer Benefits

| Benefit type | Specific benefit | Quantified? |
|---|---|---|
| Strategy enablement | Enable incremental revenue opportunities through faster integration | NQ |
| Strategy enablement | Increase business agility through easier, faster, and lower-cost upgrades | NQ |
| Strategy enablement | Improve readiness for M&A and divestitures | NQ |
| Business value | Improve adoption of future innovations | NQ |
| Risk mitigation | Improve regulatory compliance | NQ |
| Risk mitigation | Reduce cybersecurity risks | Q |
| Risk mitigation | Reduce operational risks | Q |
| IT spend effectiveness (TCO) | Reduce cost to build integrations | Q |
| IT spend effectiveness (TCO) | Reduce cycle time to build integrations | NQ |
| IT spend effectiveness (TCO) | Reduce cost to maintain integrations | Q |
| IT spend effectiveness (TCO) | Reduce cost of upgrades | Q |

**What clean core integration achieves:**
- Boost integration stability during upgrades by leveraging SAP standard interfaces in SAP S/4HANA, while reducing custom development to lower TCD and TCO
- Increase agility and enable faster adoption of SAP innovations, while lowering costs
- Reduce operational risk and minimize business disruptions through robust integration monitoring, and build confidence in end-to-end processes
- Accelerate time-to-value by adopting modern integration architecture
- Gain real-time visibility with an integrated toolchain, accelerating decision-making speed and accuracy

### Integration KPIs at a Glance (Slide 53)

| KPI Category | KPI / Metric |
|---|---|
| **Upgrade stability** | % of standard, traditional, and custom interfaces — measures ratio of active interface technologies adhering to clean core principles vs. those that do not |
| **Operational risk** | % of centrally monitored interfaces — measures interfaces automatically and centrally monitored with SAP Application Interface Framework (AIF) and SAP Cloud ALM |
| **Innovation adoption** | Usage of modern integration technologies — assesses the extent to which modern SAP integration tools and technologies are being used |
| **Agile decision-making and operational risk** | % of tools used for the integration requirement process — assesses whether the integrated toolchain is used to enable agile and transparent decision-making |

*Note: SAP-managed integration content is excluded from upgrade stability calculations. Data integration for SAP to non-SAP scenarios must be evaluated based on defined metrics.*

---

## KPI 1: Upgrade Stability

**Context:** KPI drives innovation adoption. Measures the ratio of integration APIs that adhere to clean core principles — specifically, standard APIs released and supported on the SAP Business Accelerator Hub — versus those that do not, compared to the total amount of active interfaces.

**Basis:** Uses SAP ISA-M and integration styles to separate calculations for data and process integration.

**Scope:** Tracks use of SAP-managed content across SAP S/4HANA and standard assets from the SAP Business Accelerator Hub (e.g., integration flows for SAP Integration Suite).

**Impact:** Drives the KPI for innovation adoption, as updates/new features released on cloud cycles are automatically incorporated by SAP.

### What This KPI Provides

- Clear visibility into all actively used interfaces (as-is analysis)
- Identification of interfaces that do not adhere to clean core principles or are inactive
- Actionable insights to guide transformation efforts towards a cleaner core
- Alignment with SAP's recommended best practices for stable, upgrade-ready integrations
- A quantifiable measure of progress when calculated annually

### Calculation Details

**Formula:**

```
Usage of interface technology from type X* (in %) = 
  # of activated interfaces from type X*
  ──────────────────────────────────────────────────
  Total # of activated interfaces
```

*\* X being the different interface technologies for process (e.g., OData, SOAP, IDoc, etc.) and data integration (e.g., ABAP core data services, SAP Business Warehouse Extractors, etc.)*

**Example:** SAP Readiness Check integration results show 38 active and used IDocs in the productive environment. IDocs are considered traditional interfaces. Total number of all interfaces = 157.
→ Usage of IDoc = 38/157 = 24.2% traditional interfaces (IDocs) used

**Calculation scope by integration type:**
- **Process integration:** SAP standard content for SAP Integration Suite is managed by SAP and should be **excluded** from calculation
- **Data integration — SAP to SAP:** SAP Datasphere and SAP Business Data Cloud standard content is managed by SAP and should be **excluded**; content relies on upgrade-stable and cloud-ready assets
- **Data integration — SAP to non-SAP:** Must be evaluated based on defined metrics (standard, traditional, or customized data extractors)

*Note: This KPI is not relevant for SAP-managed integration content.*

### Objectives (Key Results)

- Ensure the integration landscape is documented and understood
- Flag technical debt related to integration, especially customizations and obsolete interfaces
- Provide clear visibility of activated and used interface technology in SAP S/4HANA, showing share adhering to clean core principles and those that do not
- Enable transformation road map planning towards a cleaner core to reduce core modifications and adopt standardized, upgrade-safe models
- Guide organization towards future-proof, modern integration technologies leveraging SAP BTP

### Measurement Details

| Field | Value |
|---|---|
| **Recommended tools — Now** | SAP S/4HANA; SAP Readiness Check (limited functionality) |
| **Recommended tools — Future** | RISE with SAP Methodology dashboard |
| **Prerequisites** | Run SAP Readiness Check on the productive environment and trace the data for several weeks |
| **Cadence** | Quarterly (during transformation journey); Twice a year (after reaching a stable state) |
| **Type** | Semi-automatic |

**Measurement guidance:** SAP Readiness Check — Integration Analysis. Deep dive into each available interface technology on SAP Readiness Check, identify the number of active interfaces per type, and determine the number of extensions.

### Governance & Maturity Relevance

- Maturity of Integration Landscape (INT-03)
- Maturity of SAP S/4HANA Integration Readiness (INT-05)

---

## KPI 2: Operational Risk — Expert Tool Monitoring Coverage

**Context:** Using central monitoring governance reduces operational risk. SAP recommends SAP Application Interface Framework (AIF) as the expert monitoring tool to oversee a variety of interface types (standard, traditional, and custom) within the SAP S/4HANA landscape. Business users benefit from intuitive error analysis tools, enabling rapid access and resolution of issues.

### Calculation Details

**Formula:**

```
% of monitored interfaces via expert tool =
  # of centrally monitored interfaces in expert tool
  ─────────────────────────────────────────────────────
  Total # of active interfaces identified by SAP Readiness Check
```

**Numerator:** Count of interfaces actively monitored using SAP Application Interface Framework in SAP S/4HANA  
**Denominator:** Sum of all active and used interfaces in SAP S/4HANA identified by SAP Readiness Check

### Objectives (Key Results)

- Streamlined error resolution
- Smarter workload and resource allocation
- Reduced operational risk via alert notifications
- Improved integration robustness through error analysis
- Enhanced system scalability and performance

### Measurement Details

| Field | Value |
|---|---|
| **Recommended tools — Now** | SAP S/4HANA (productive environment) — SAP Application Interface report, SAP Readiness Check |
| **Recommended tools — Future** | RISE with SAP Methodology dashboard |
| **Prerequisites** | Currently requires semi-manual effort |
| **Cadence** | Twice per year (during transformation journey); Once a year (after reaching a stable state) |
| **Type** | Semi-automatic |

**Measurement guidance:**
1. Use SAP Readiness Check to identify all activated interfaces
2. Go to transaction SA38 and run the report `/AIF/IDX_TBL_OVERVIEW`
3. Count interfaces that do not have an entry
4. Manual check: Go to customizing via transaction `/AIF/CUST` → Check interface definition (namespace/name) in Define Interfaces
5. Use transaction `/AIF/NOTIF_SETUP` to check whether an alert notification has been set up
6. Calculate the percentage of interfaces with active monitoring

### Governance & Maturity Relevance

- Maturity of Operational Framework (INT-06)

---

## KPI 3: Operational Risk — End-to-End Integration Monitoring Using SAP Cloud ALM

**Context:** For SAP Integration Suite, SAP recommends SAP Cloud ALM for monitoring integration. The main focus is to ensure that Integration & Exception Monitoring is activated in SAP Cloud ALM and that alert notifications are properly set up. Connecting surrounding systems (SAP S/4HANA and other LoB solutions) to SAP Cloud ALM monitoring enables centralized end-to-end monitoring.

### Calculation Details

**Score-based (not a percentage):**

| Score | Condition |
|---|---|
| **3** | If end-to-end monitoring (including SAP S/4HANA & LoB solutions) is configured |
| **2** | If integration monitoring AND alert notification via SAP Cloud ALM are set up |
| **1** | If only integration monitoring is set up |
| **0** | If neither integration monitoring nor alert notification is set up for SAP Integration Suite |

### Objectives (Key Results)

- Streamlined error resolution
- Smarter workload and resource allocation
- Reduced operational risk via alert notifications
- Improved integration robustness through error analysis
- Enhanced system scalability and performance

### Measurement Details

| Field | Value |
|---|---|
| **Recommended tools — Now** | SAP Integration Suite (productive environment), SAP Cloud ALM |
| **Recommended tools — Future** | RISE with SAP Methodology dashboard |
| **Prerequisites** | SAP Cloud ALM must be connected to SAP Integration Suite; integration flows must fail to enable active monitoring (manual step) |
| **Cadence** | Twice per year (during transformation journey); Once a year (after reaching a stable state) |
| **Type** | Manual |

**Measurement guidance:**
1. Within the Operations area of SAP Cloud ALM, set up Integration & Exception Monitoring for SAP Integration Suite and SAP S/4HANA (also end-to-end monitoring)
2. In SAP Cloud ALM, verify whether integration flows are monitored (e.g., connection to message monitoring) and whether an alert notification has been configured

### Governance & Maturity Relevance

- Maturity of Operational Framework (INT-06)

---

## KPI 4: Innovation Adoption — Adapting Modern Integration Technologies

**Context:** Adopting modern integration technologies enables agility and drives innovation. This KPI assesses the extent to which modern SAP integration tools and technologies are being used. Specifically, it evaluates whether recommended SAP services have been activated and are in active use.

**Key focus areas:**
- SAP Integration Suite usage (standard integration content from SAP Business Accelerator Hub)
- API-led strategy via API Management capability in SAP Integration Suite
- B2B integrations via Trading Partner Management (TPM) in SAP Integration Suite
- Event-driven architecture via SAP Integration Suite Advanced Event Mesh (or SAP Event Mesh)
- Master data integration via SAP Master Data Integration
- Data integration via SAP Datasphere and/or SAP Business Data Cloud

### Calculation Details

**Formula:**

```
% of activated and used SAP integration technologies =
  # of actively used modern SAP integration technologies
  ─────────────────────────────────────────────────────────
  Total # of modern SAP integration technologies (= 7)
```

**Numerator — check activation and active usage of:**
1. SAP Integration Suite
2. SAP Integration Suite, API Management capability
3. SAP Integration Suite, Trading Partner Management capability
4. SAP Integration Suite, Advanced Event Mesh (or SAP Event Mesh)
5. SAP Master Data Integration
6. SAP Datasphere
7. SAP Business Data Cloud

**Denominator:** 7 (total number of SAP integration technologies)

### Objectives (Key Results)

- Speed up innovation cycles by reducing reliance on legacy middleware
- Measure adoption and active usage of SAP's modern integration technologies
- Assess road map and features of available SAP integration solutions
- Explore SAP integration functionalities for business fit
- Prioritize transformation initiatives based on modernization needs

### Measurement Details

| Field | Value |
|---|---|
| **Recommended tools — Now** | Different SAP tools using SAP Business Technology Platform |
| **Recommended tools — Future** | RISE with SAP Methodology dashboard |
| **Prerequisites** | Requires purchase of SAP BTP services |
| **Cadence** | Once a year, and as part of evaluating new integration requirements |
| **Type** | Manual |

**Measurement guidance:**
1. Log into SAP BTP Global and Sub accounts
2. Check activation status of each tool
3. Use Usage Analysis in SAP BTP to confirm active usage

### Governance & Maturity Relevance

- Maturity of Integration Landscape (INT-03)

---

## KPI 5: Agile Decision-Making and Operational Risks — Interface Documentation Lifecycle

**Context:** The integrated toolchain enables transparency and agility. This KPI assesses whether the organization is leveraging the integrated toolchain to support agile and transparent decision-making for integration projects.

**Toolchain lifecycle flow:**
1. Business process requirements defined in SAP Signavio — integration requirements linked to business process models
2. Requirements defined, tracked, and managed within SAP Cloud ALM throughout the project lifecycle
3. Integration architecture connected via SAP LeanIX Interface Repository — clear visibility into the integration architecture
4. Integration assessments conducted via SAP Integration Suite integration assessment app (ISAM-based)
5. Project delivery managed within SAP Cloud ALM — end-to-end project management and transparency
6. Integration documentation consolidated in SAP LeanIX Interface Repository — comprehensive lifecycle visibility

*Note: This KPI is measured based on SAP products, but also applies when using non-SAP products.*

### Calculation Details

**Formula:**

```
% of integration requirements covered by the toolchain (per tool Y) =
  # of maintained integration requirements in tool Y
  ──────────────────────────────────────────────────────────────────
  Total # of integration requirements in the organization's landscape
```

**Numerator — per tool:**
- **SAP Signavio:** Each integration requirement linked to a business process, captured in the BPM tool
- **SAP LeanIX:** Detailed view of the integration requirement maintained in the enterprise architecture management tool, resulting in an integration architecture
- **SAP Integration Suite integration assessment:** Tool-based assessment performed and documented consistently (e.g., using SAP ISAM)
- **SAP Cloud ALM:** Status of the integration requirement implementation tracked in a project management tool

**Denominator:** Total number of integration requirements in the organization's landscape

### Objectives (Key Results)

- Gain an overview of all integration requirements and their links to business processes
- Understand how each integration requirement is described, managed, and visualized
- Enable step-by-step assessment of integration requirements and documentation of technology choices
- Identify missing or incomplete data or documentation to support continuous improvement

### Measurement Details

| Field | Value |
|---|---|
| **Recommended tools — Now** | SAP Signavio, SAP LeanIX, SAP Integration Suite, SAP Cloud ALM |
| **Recommended tools — Future** | RISE with SAP Methodology dashboard |
| **Prerequisites** | Currently a manual step |
| **Cadence** | Once a year, and as part of evaluating new integration requirements |
| **Type** | Manual |

**Measurement guidance:** Check within the integration requirement process whether your organization is leveraging the integrated toolchain for each of the four tools.

**Key results:**
- Increase decision speed and accuracy: real-time visibility across business processes, integration architecture, and project progress
- Break down silos: seamless data flow and transparency across tools ensuring business, IT, and project teams are aligned
- Drive continuous improvement: insights from integrated tools reveal bottlenecks, integration gaps, and optimization opportunities
- Accelerate value realization: faster, better-informed decisions enable organizations to deliver innovation more rapidly

### Governance & Maturity Relevance

- Maturity of Integrated Toolchain (INT-04)

---

## KPI Measurement Type Summary

| KPI | Type | Cadence |
|---|---|---|
| Upgrade stability | Semi-automatic | Quarterly (transformation); Twice/year (stable) |
| Operational risk — AIF expert tool | Semi-automatic | Twice/year (transformation); Once/year (stable) |
| Operational risk — SAP Cloud ALM end-to-end | Manual | Twice/year (transformation); Once/year (stable) |
| Innovation adoption | Manual | Once/year |
| Agile decision-making / toolchain | Manual | Once/year |
