# Clean Core Data — Governance & Maturity

**Source:** Clean Core Governance & Maturity Deck (SAP1222195 v2.0) — Data section (Slides 51–64)  
**Ingested:** 2026-09-13  
**Purpose:** Full per-practice evaluation criteria and 0–5 maturity rating guidance for all five data governance & maturity practices. Used during RISE with SAP Methodology assessments to score current state and define target state.

---

## Data G&M Context (Slide 51–54)

The G&M assessment evaluates five data practices, each scored 0–5 for both Current State and Target State:

| Practice | ID | Importance |
|---|---|---|
| Maturity of Data Strategy Setup | DAT-01 | High |
| Maturity of Data Governance Setup | DAT-02 | High |
| Maturity of Data Quality Management | DAT-03 | Medium |
| Maturity of Data Volume Efficiency Management | DAT-04 | Medium |
| Maturity of Data Protection Setup | DAT-05 | High |

**Why this matters:**
- Clear data roles, organizational alignment, and a strong governance framework are key to informed decisions, scalable and compliant data use, and successful clean core data implementation (DAT-01)
- Without governance, data becomes fragmented and unreliable, slowing innovation — while Data Mesh/Fabric roles enable trusted, data-driven decisions during and after upgrades (DAT-02)
- Regular data quality assessments, supported by cleansing tools and overseen by a governance board, ensure consistent, reliable data (DAT-03)
- A scalable data infrastructure paired with well-managed retention policies ensures seamless growth, performance, compliance, and cost efficiency (DAT-04)
- Data protection, supported by clear procedures and audit practices, builds stakeholder trust, ensures regulatory compliance, and safeguards data confidentiality and integrity (DAT-05)

**What needs to be in place:**
- Implement data policies, assign clear data roles, build necessary skills, set up a governance board, apply Data Mesh/Data Product principles, use a Data Catalog (DAT-01/02)
- Use data quality tools to gain transparency, perform regular data quality cleansing, establish continuous data monitoring for integrity and efficiency (DAT-03)
- Establish a continuous process for effective data management; define validation, approval, and distribution frameworks using SAP Master Data Integration / SAP Master Data Governance; implement archiving, deletion, or data tiering via SAP ILM / Data Privacy Integration (DAT-04)
- Enforce access controls and encrypt sensitive data; define breach response procedures; run regular compliance audits (e.g., GDPR) (DAT-05)

---

## DAT-01: Maturity of Data Strategy Setup

**Why:** Clear data roles, organizational alignment, and a strong governance framework are key to informed decisions, scalable and compliant data use, and successful clean core data implementation.

### Evaluation Criteria

| Question | Current Score | Target Score |
|---|---|---|
| Are there clear policies on data access, sharing, and compliance? | 0–5 | 0–5 |
| Are data roles assigned: compliance officer, data protection officer, steward, owner, etc.? | 0–5 | 0–5 |
| Is there an enablement plan related to data skills necessary for implementing clean core? | 0–5 | 0–5 |
| Is regular audit to ensure governance to policies conducted? | 0–5 | 0–5 |
| Is there a strategy for managing the lifecycle of non-SAP data products? | 0–5 | 0–5 |
| Is there a governance board to take decisions around data strategy? | 0–5 | 0–5 |
| Is there a data governance framework in place? | 0–5 | 0–5 |
| Is there an overview/catalogue of your data, e.g., data domain map? | 0–5 | 0–5 |

### Maturity Rating Guidance

| Rating | Short Description | Long Description |
|---|---|---|
| **0 – Not Started / Not Considered** | Not started | Not started |
| **1 – Beginner** | Ad hoc, informal, rarely practiced | Policies and roles are ad hoc with no formal controls or governance. |
| **2 – Intermediate** | Some elements defined, inconsistent | Basic data roles or frameworks exist but are implemented inconsistently and lack organization-wide coverage. |
| **3 – Proficient** | Standardized, somewhat integrated | Data policies and roles are standardized in some areas, but not fully integrated or consistently applied. |
| **4 – Advanced** | Integrated, regularly audited | Data roles, frameworks, and policies are widely adopted, integrated, and routinely reviewed across functions. |
| **5 – Expert** | Fully optimized, proactive, strategic | Policies and roles are automated and best-in-class, proactively managed organization-wide, championed by leadership, and continually improved. |

---

## DAT-02: Maturity of Data Governance Setup

**Why:** Without governance, data becomes fragmented and unreliable, slowing innovation. Data Mesh/Fabric roles enable trusted, data-driven decisions during and after upgrades.

### Evaluation Criteria (Sub-Practices)

| Question | Current Score | Target Score |
|---|---|---|
| Is there a data governance organization setup? | 0–5 | 0–5 |
| Is there a development guideline to handle custom data objects by considering the clean core level concept? | 0–5 | 0–5 |
| Is the extension or creation of new data models with custom data objects evaluated? | 0–5 | 0–5 |
| Are there data mesh / data fabric and data product-related roles in your organization? | 0–5 | 0–5 |
| Is there a system / tool to centrally manage the consistency of data across systems? | 0–5 | 0–5 |

### Maturity Rating Guidance

| Rating | Short Description | Long Description |
|---|---|---|
| **0 – Not Started / Not Considered** | Not started | Not started |
| **1 – Beginner** | No structure, ad hoc, minimal awareness | No formal organization or guidelines exist; practices are informal or handled individually with little coordination. |
| **2 – Intermediate** | Basic setup, partial coverage | Some guidelines or organizational elements exist, but only address limited areas; implementation is inconsistent. |
| **3 – Proficient** | Standardized, moderate integration | Standard processes, roles, and guidelines are established and followed in most cases, with some integration efforts. |
| **4 – Advanced** | Integrated, organization-wide, monitored | Governance organization, roles, and development guidelines are fully deployed, integrated, and regularly monitored. |
| **5 – Expert** | Optimized, strategic, continuously improved | Organization is best-in-class; all elements are optimized, proactively managed, and continuously advanced. |

---

## DAT-03: Maturity of Data Quality Management

**Why:** Regular data quality assessments, supported by cleansing tools and overseen by a governance board, ensure consistent and reliable data, enabling informed decision-making, efficient operations, and effective strategies such as data harmonization.

### Evaluation Criteria

| Question | Current Score | Target Score |
|---|---|---|
| Is there a system / tool to centrally manage the consistency of data across systems? | 0–5 | 0–5 |
| Is there a regular check to cleanse data? | 0–5 | 0–5 |
| Is there a process to identify inconsistent data? | 0–5 | 0–5 |
| Is there a tool to profile your data and identify errors? | 0–5 | 0–5 |

### Maturity Rating Guidance

| Rating | Short Description | Long Description |
|---|---|---|
| **0 – Not Started / Not Considered** | Not started | Not started |
| **1 – Beginner** | Ad hoc, minimal, informal | No regular data cleansing; governance board/processes/tools are lacking or rarely used and not standardized. |
| **2 – Intermediate** | Basic, limited, partially applied | Occasional data checks or inconsistent use of processes/tools; some standardization, but not organization-wide. |
| **3 – Proficient** | Defined, regular, standardized | Regular data quality checks and standardization are practiced; processes and basic tools are defined and used. |
| **4 – Advanced** | Integrated, proactive, monitored | Data cleansing, governance, identification, and error profiling are systematic, integrated, and proactively managed. |
| **5 – Expert** | Optimized, automated, strategic | Data quality and governance are fully automated, strategically managed, and continuously improved organization-wide. |

---

## DAT-04: Maturity of Data Volume Efficiency Management

**Why:** A scalable data infrastructure paired with well-managed retention policies ensures seamless growth, performance, compliance, and cost efficiency. It handles growing data volumes while optimizing storage, enhancing security, and supporting responsible data lifecycle management.

### Evaluation Criteria

| Question | Current Score | Target Score |
|---|---|---|
| Is there a data infrastructure that can scale efficiently as data volume increases? | 0–5 | 0–5 |
| Is there a policy to identify and archive unused data? | 0–5 | 0–5 |
| Is there a policy about retention and deletion of various kinds of data? | 0–5 | 0–5 |
| Are compression / archiving / hot-cold storage techniques being leveraged? | 0–5 | 0–5 |

### Maturity Rating Guidance

| Rating | Short Description | Long Description |
|---|---|---|
| **0 – Not Started / Not Considered** | Not started | Not started |
| **1 – Beginner** | Ad hoc, unstructured | No scalable infrastructure or formal policies; archiving and storage practices are reactive and not standardized. |
| **2 – Intermediate** | Basic, partially in place | Some infrastructure, archiving, or retention practices exist, but are informal, limited, or inconsistently applied. |
| **3 – Proficient** | Standardized, documented | Infrastructure and policies are documented, defined, and commonly followed; standard storage techniques in use. |
| **4 – Advanced** | Integrated, proactively managed | Scalable infrastructure and data lifecycle policies are integrated, regularly reviewed, and techniques are optimized. |
| **5 – Expert** | Automated, strategic, best-in-class | Fully automated, highly scalable infrastructure and advanced data lifecycle management with continuous improvement. |

---

## DAT-05: Maturity of Data Protection Setup

**Why:** Data protection, supported by clear procedures and audit practices, builds stakeholder trust, ensures regulatory compliance, and safeguards data confidentiality and integrity, while preparing for unexpected incidents.

### Evaluation Criteria

| Question | Current Score | Target Score |
|---|---|---|
| If data lakes are used, are access controls enforced for sensitive data (e.g., personal data)? | 0–5 | 0–5 |
| If data lakes or external databases are used, is sensitive data encrypted? | 0–5 | 0–5 |
| Is there a standard procedure for handling data breach or security incident? | 0–5 | 0–5 |
| Is there a regular planned Compliance Audit? | 0–5 | 0–5 |

### Maturity Rating Guidance

| Rating | Short Description | Long Description |
|---|---|---|
| **0 – Not Started / Not Considered** | Not started | Not started |
| **1 – Beginner** | Ad hoc, no controls | No formal security controls or compliance processes for sensitive data in data lakes or external databases. |
| **2 – Intermediate** | Basic, inconsistent | Some access controls or encryption exist, and compliance practices are in place, but they are applied inconsistently. |
| **3 – Proficient** | Standardized, enforced | Standard security measures (access controls, encryption, breach handling) and planned audits are established and used. |
| **4 – Advanced** | Integrated, proactively managed | Security, compliance, and incident procedures are fully integrated, regularly reviewed, and proactively managed. |
| **5 – Expert** | Automated, best-in-class | Security and compliance practices are automated, continuously monitored, benchmarked as industry leading, and aligned with global regulations. |
