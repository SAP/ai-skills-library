# Clean Core Operations — KPI Measurement Framework

**Source:** Clean Core Measurement Framework – KPIs (external)  
**Document ID:** SAP1240359 | Public download: https://dam.sap.com/mac/app/p/pdf/asset/preview/XbqgDc4?ltr=a&rc=10&doi=SAP1240359  
**File:** Measurement_Criteria_for_Clean_Core_KPIs_Ext_Final_v1.3 (1).pptx  
**Version:** v1.3 Final  
**Slides:** 65–89 (Operations section)  
**Ingested:** 2026-09-13  
**Audience:** Installed base customers, Enterprise Architects, TQMs  
**Purpose:** Full per-KPI calculation detail, measurement guidance, tooling, and cadence for the six Operations KPI categories.

> **Scope note:** The cross-principle KPI framework overview (glossary, guiding principles, all five principles at a glance) is in the `clean-core-general` skill → `knowledge/05-kpi-framework.md`. This file covers Operations-specific content only.

---

## Operations Context (Slide 66)

### Expected Benefits — Four Value Driver Categories

| Value driver | Benefit | Q/NQ |
|---|---|---|
| **Strategy enablement** | Increased business agility | NQ |
| **Business value** | Improve value from adopting latest capabilities | Q |
| | Reduce production defects | NQ |
| | Accelerate time-to-release for latest capabilities (by reducing testing scope and increasing test automation) | Q |
| | Improve quality of delivery | NQ |
| | Improve collaboration between stakeholders | NQ |
| **Risk mitigation** | Reduce cybersecurity risk | Q |
| | Reduce operational risk | NQ |
| | Reduce change fatigue | NQ |
| **IT spend effectiveness (TCO)** | Reduce SAP application testing cost | Q |
| | Reduce SAP application testing scope | NQ |
| | Reduce tool TCO across the delivery pipeline | Q |

*Q = Quantified, NQ = Not Quantified*

### What Operations KPIs Track

This set of KPI categories tracks how operational excellence enables transformation and best practices across all dimensions:
- **Software stack** — ensure systems stay current to support business innovation and security
- **Toolchain adoption** — measure integration of tools that unify business, IT, and architecture
- **Clean core requirements** — monitor alignment to standards, minimizing complexity and technical debt
- **Agile delivery** — gauge speed and quality of delivering business value through iterative delivery
- **Operational efficiency** — track stable operations and process performance for business continuity
- **Secure operations** — confirm compliance to security standards, protecting transformation

---

## Operations KPI Categories at a Glance (Slide 67)

| KPI Category | Description | Persona |
|---|---|---|
| **Software stack** | Measures adherence to keeping SAP systems current with the latest releases to enable innovation and reduce security and operational risks | CIO/CTO (platform currency) |
| **Enable agility through integrated toolchain adoption** | Indicates adoption of the integrated toolchain streamlining collaboration and innovation, ensuring continuous transformation and clean core integrity | CIO |
| **Adopt clean core requirements** | Tracks how requirements validation is embedded as a practice to ensure ongoing alignment with clean core principles | CIO (SSB governance) |
| **Continuously improve agile delivery and operational excellence** | An integrated toolchain streamlines collaboration and innovation, ensuring continuous transformation and clean core integrity throughout the SAP lifecycle | CIO/COO |
| **Enduring operational efficiency** | Assesses enduring operational efficiency of SAP operations, focusing on minimizing disruptions and driving continuous improvement | COO |
| **Embed secure operations** | Confirms compliance with security standards and adoption of SAP baseline practices to reduce risk, prevent technical debt, and ensure long-term protection | CISO/CSO |

---

## KPI 1: Software Stack

### Overview (Slide 69)

| | |
|---|---|
| **KPI category** | Software stack |
| **KPIs** | Age of Feature Pack Stack (months) / Age of Support Package Stack (months) |
| **Sub-categories** | Innovation readiness / Security compliance |
| **Measurement tools** | SAP Cloud ALM (configuration and security analysis), SAP EarlyWatch Alert, SAP for Me, SAP S/4HANA directly |

### Context (Slide 70)

**Two objectives:**
1. **Increase business value by staying up to date with SAP innovations:** Running on a recent SAP S/4HANA release, or at least a recent Feature Pack Stack (FPS), is crucial to adopt new innovations in time.
2. **Reduce operational and cybersecurity risk with up-to-date SPS:** Running on a recent Support Package Stack (SPS) is crucial for system security — SAP guarantees security notes only for SPS shipped within the last 24 months.

**SAP S/4HANA release cadence:**
- Each release ships with an initial shipment stack
- Three Feature Pack Stacks (FPS) delivered ~6 months apart, each containing smaller features and new innovations
- Support Package Stacks (SPS) delivered on a regular basis until end of maintenance

**Compliance thresholds:**
- Innovation compliance: system stack must not be older than **24 months**. Compliance is capped at the delivery of the last FPS (FPS3) of the release + 24 months.
- Security compliance: system stack must not be older than **24 months**
- Innovation compliance always implies security compliance, but not the other way around

**Governance & maturity relevance:** Maturity of release management / Maturity of secure operations

### Calculation and Measurement (Slide 71)

| | Detail |
|---|---|
| **Key results** | 100% of production SAP S/4HANA systems run on an SPS/FPS delivered within the last 24 months. All production systems upgraded at least once every two years; 75% upgraded annually. All critical security patches (SAP HotNews/priority 1 notes) applied within 30 days of release. Organization has adopted at least one major new SAP S/4HANA innovation within 12 months of its release. |
| **Recommended tool** | RISE with SAP Methodology dashboard (now); SAP for Me, SAP EarlyWatch Alert (alternative) |
| **Prerequisites** | RISE with SAP Methodology dashboard access for automatic collection; SAP Cloud ALM |
| **Cadence** | Monthly monitoring; minimum technical upgrade target: once per year (Release/FPS/SPS as appropriate) |
| **Measurement guidance** | SAP Cloud ALM Application Help → Software Stack |
| **Measurement type** | **Automatic** |

---

## KPI 2: Enable Agility Through Integrated Toolchain Adoption

### Overview (Slide 72)

| | |
|---|---|
| **KPI category** | Enable agility through integrated toolchain adoption |
| **Measurement tools** | SAP Cloud ALM for implementation, Focused Build for SAP Solution Manager, SAP BTP/SAP Cloud Transportation Management, SAP Continuous Integration and Delivery |

### Context (Slide 73)

This KPI is vital for clean core adoption — it ensures streamlined processes and improved collaboration. The comprehensive business transformation suite accelerates innovation and value realization.

**Important distinction (KPI relationship):** This KPI is a technical measure used to understand the current status of tool adoption. It does **not** measure the effectiveness of tool adoption.

*Example: The sub-KPI "Test management and automation readiness" measures tool usage, while the KPI "Quality" in the category "Continuously improve agile delivery and operational excellence" measures whether practices and tools enable greater automation and improve delivery quality.*

**Measurement approach:**
- Toolchain usage measured through licenses and customer usage metrics
- Each measure is % based on capability adoption
- Capabilities not included in the RISE with SAP Methodology are not rated individually but still support greater toolchain adoption
- Usage metrics related to actual usage per capability within the past month, specific to project phases

**Governance & maturity relevance:** Maturity of business transformation toolchain / Maturity of clean core governance

### Calculation and Measurement (Slide 74)

| | Detail |
|---|---|
| **Objective** | Ensure adoption of an integrated toolchain, streamlining handover and reuse of artefacts across the lifecycle of the landscape. Improve related KPIs enabled by the toolchain. Enable agility in software delivery. |
| **Calculation** | Numerator: Sum of all KPIs in the KPI tree, each with equal weight. Denominator: Total number of KPIs. Result: Mean value for the metrics (since the number of metrics per KPI can vary, all KPIs are aggregated to the mean value of related metrics). |
| **Key results** | Toolchain adopted across entire project lifecycle, including Run operations and ongoing/future transformations and innovation cycles. All key project and Run activities (as per SAP Activate) orchestrated through end-to-end toolchain. |
| **Recommended tool** | Manual validation (now); RISE with SAP Methodology dashboard (alternative) |
| **Prerequisites** | RISE with SAP Methodology dashboard access; SAP Cloud ALM Project Management phase timeboxes configured |
| **Cadence** | Weekly during relevant project phases; monthly otherwise |
| **Measurement type** | **Automatic** |

---

## KPI 3: Adopt Clean Core Requirements

### Overview (Slide 76)

| | |
|---|---|
| **KPI category** | Adopt clean core requirements |
| **Sub-KPIs** | Clean core process index, Clean core extensibility index, Clean core data index, Clean core integration index, Tracking technical debt and improvements |
| **Measurement tools** | RISE with SAP Methodology dashboard (aggregate scores from all four dimension KPIs), SAP Cloud ALM for implementation requirements, Focused Build for SAP Solution Manager |
| **Status** | Vision — SAP Lab Preview based on KPI automatization in RISE with SAP Methodology dashboard, subject to change |

### Context (Slide 77)

Aligning to the clean core principles measures how organizations adopt their business requirements to the capabilities of SAP software. Measuring overall alignment to clean core as a technical KPI provides feedback on adherence to SAP best practices across all dimensions, while also tracking potential technical debt arising from capability gaps.

Clean core requirements promote the use of standard SAP functionalities and best practices, helping to minimize technical debt and complexity.

As requirements and operations are a cross-dimension measure, this KPI uses:
- The overall % score from each dimension KPI
- Those project requirements marked as non-clean core compliant

**Governance & maturity relevance:** Maturity of continuous improvement for an enduring clean core / Maturity of clean core governance

### Calculation and Measurement (Slide 78)

| | Detail |
|---|---|
| **Objective** | Maximize adoption of clean core requirements across all dimensions. Reduce technical debt and non-compliant requirements. Strengthen governance and continuous improvement practices. |
| **Calculation** | Technical debt ratio weighted at **40%** (emphasizes continuous improvement as an ongoing initiative). Remaining 60% distributed across dimension ratings — business processes, integrations, data, and extensibility each weighted at **15%**. Ensures both governance focus and measurable progress across dimensions. |
| **Key results** | All new projects and business requirements assessed for clean core compliance. Improve clean core KPI scores across all other dimensions. Minimize non-clean core compliant requirements. Continuously remediate significant portion of identified technical debt items. Achieve ongoing improvement in overall clean requirements KPI score. |
| **Recommended tool** | Manual validation requiring requirement categorization in SAP Cloud ALM (now); RISE with SAP Methodology dashboard (alternative) |
| **Prerequisites** | SAP Cloud ALM |
| **Cadence** | Weekly during relevant project phases; according to release strategy |
| **Measurement guidance** | All requirements should be categorized as compliant with clean core principles. Documentation in SAP Cloud ALM ensures technical debt is understood, tracked, and remediated in future projects. |
| **Measurement type** | **Manual; automatic in the future** |

---

## KPI 4: Continuously Improve Agile Delivery and Operational Excellence

### Overview (Slide 79)

| Sub-KPI | Metrics | Measurement tools |
|---|---|---|
| **Velocity** | Change frequency, Change volume, Deployment speed, Innovation rate, Clean core share | SAP Cloud ALM deployment management, Focused Build for SAP Solution Manager, SAP Cloud Transportation Management, SAP Continuous Integration and Delivery |
| **Quality** | Test coverage and execution, Test automation rate, Security and compliance tests | SAP Cloud ALM/SAP Solution Manager test management & process management, ABAP Test Cockpit, SAP Code Vulnerability Analyzer, SAP Test Automation by Tricentis |
| **Efficiency** | Lead time for changes, Deployment frequency, Number of emergency changes | SAP Cloud ALM for implementation requirements/features/deployment management, SAP Cloud ALM for operations event management, Focused Build for SAP Solution Manager/SAP Focused Run |
| **Reliability** | Mean time to recovery, Incident and alert volume, System performance (operations health), Integration exceptions | Alert management, RISE with SAP operations dashboard |

### Context (Slide 80)

For SAP customers, adoption of the integrated toolchain (SAP LeanIX, SAP Signavio, SAP Cloud ALM, SAP Cloud Transportation Management, SAP Continuous Integration and Delivery, Tricentis solutions, WalkMe) is essential for clean core. Yet, true value comes when these tools improve how teams deliver and operate SAP systems.

**Four KPIs within this category:**
- **Velocity** — speed and throughput of SAP change and feature delivery
- **Quality** — functional integrity and code/test health of the SAP solution
- **Efficiency** — ability to deliver quickly and cost-effectively, minimizing rework or delays
- **Reliability** — operational performance and stability of the delivered SAP solution

**Business benefits:**
- Accelerated innovation: improved delivery velocity means features reach users faster
- Higher quality: monitoring code and test health reduces defects
- Greater efficiency: metrics identify bottlenecks and minimize rework
- Stronger reliability: consistent tracking of performance and stability minimizes downtime

**Governance & maturity relevance:** Maturity of software delivery efficiency / Maturity of test management and execution / Maturity of release management / Maturity of IT operations excellence

### Calculation and Measurement (Slide 81)

| | Detail |
|---|---|
| **Calculation** | Numerator: Sum of all KPIs in the KPI tree, each weighted equally. Denominator: Number of KPIs. Result: Mean value of the metrics. Details of metric and KPI relationship calculation provided in the deck. |
| **Key results** | Toolchain adopted across full project lifecycle including Run operations, ongoing transformations, and innovation cycles. All key project and Run activities orchestrated through end-to-end toolchain. |
| **Recommended tool** | Manual validation (now); RISE with SAP Methodology dashboard (alternative) |
| **Prerequisites** | RISE with SAP Methodology dashboard access; SAP Cloud ALM analytics |
| **Cadence** | Weekly during relevant project phases; monthly otherwise |
| **Measurement guidance** | All measurements taken from SAP Cloud ALM analytics |
| **Measurement type** | **Manual; automatic in the future** |

---

## KPI 5: Enduring Operational Efficiency

### Overview (Slide 83)

| Sub-KPI | Metrics | Tools |
|---|---|---|
| **Alert flooding** | Number of very high alerts, Alert processing time, New alerts raised, Current number of alerts | SAP Cloud ALM for operations, SAP Focused Run |
| **Event management efficiency** | Alerts older than 3 days (high) / 3 hours (very high) | SAP Cloud ALM for operations |
| **Business process performance** | Number of process disruptions/exceptions, Number of real user monitoring alerts | SAP Cloud ALM for operations, SAP Signavio Process Insights |
| **Connectivity** | Critical system heartbeat, Critical instance heartbeat | SAP Cloud ALM for operations |
| **Exceptions** | Runtime errors, System log errors, Application log errors | SAP Cloud ALM for operations |
| **Performance** | Maximum response time, Average response time | SAP Cloud ALM |
| **Background processing** | Batch jobs aborted | SAP Cloud ALM, SAP Focused Run |

### Context (Slide 84)

SAP landscapes are dynamic and complex, requiring continuous operational oversight to ensure stability, reliability, and responsiveness.

**Enduring operational efficiency** is measured by two main KPIs, each with aggregated sub-KPIs:

**Operations excellence:**
- Alert flooding (number of alerts)
- Event management efficiency (handling speed, severity)
- Business process performance (process disruptions, user monitoring alerts)

**System health:**
- Connectivity (system/instance heartbeat)
- Exceptions (runtime, system, application errors)
- Background processing (batch jobs aborted)
- Performance (maximum/average response times)

This value driver reflects a shift from reactive management to **predictive and preventative governance**.

**Governance & maturity relevance:** Maturity of IT operations excellence

### Calculation and Measurement (Slide 85)

| | Detail |
|---|---|
| **Calculation** | Sub-KPIs normalized into % values and aggregated at the operations health and system health level. Details on the following slide. |
| **Key results** | Reduce unnecessary alert noise and handle critical alerts quickly and effectively. Minimize business process disruptions and improve end-user experience. Strengthen system health by improving connectivity, reducing errors, and ensuring stable background processing. Maintain performance standards for critical transactions and processes. Increase automation and proactive monitoring. |
| **Recommended tool** | System health via RISE with SAP Methodology dashboard; additional metrics require SAP Cloud ALM standard capabilities |
| **Prerequisites** | RISE with SAP Methodology dashboard access; SAP Cloud ALM |
| **Cadence** | **Daily**; metrics calculated at 15-minute intervals |
| **Measurement guidance** | Operations health – Business process performance: Monitoring \| SAP Help Portal; SAP Signavio Process Insights. Operations health – Alert flooding, event management efficiency: Intelligent Event Processing \| SAP Help Portal. System health: SAP Cloud ALM Application Help → Operations view. |
| **Measurement type** | **Automatic** |

---

## KPI 6: Embed Secure Operations

### Overview (Slide 87)

| Sub-KPI | Metrics | Tools |
|---|---|---|
| **Software stack security compliance** | Age of FPS (months), Age of SPS (months) | SAP Cloud ALM (configuration and security analysis), SAP EarlyWatch Alert, SAP for Me, SAP S/4HANA directly |
| **Adoption of secure baseline** | % checks compliant with SAP secure baseline | SAP Cloud ALM (configuration and security analysis), SAP EarlyWatch Alert, Security optimization service |

### Context (Slide 88)

Security and lifecycle compliance are foundational to maintaining clean core operations. Keeping FPS and SPS updated ensures that security patches, performance improvements, and SAP road map innovations are regularly integrated without disrupting the core.

**Two key areas:**

1. **Lifecycle compliance — FPS or SPS no older than 24 months:** Tracks how up to date the system is. Regular updates reduce security risks, maintain performance, and ensure compatibility with SAP's road map.
   - FPS and SPS versions extracted from the system landscape and compared to current date to determine age in months
   - Evaluated against threshold of 24 months, aligning with SAP's recommended update cycle

2. **Adoption of secure baseline:** Measures adherence to SAP's secure operations baseline, identifying configuration gaps that could expose systems to vulnerabilities.
   - SAP's secure operations map or security baseline template serves as the reference model
   - Compliance checks run via SAP Cloud ALM security validation or SAP Focused Run configuration analytics
   - % of failed checks relative to total baseline checks = KPI

**Governance & maturity relevance:** Maturity of secure operations

### Calculation and Measurement (Slide 89)

| | Detail |
|---|---|
| **Calculation** | FPS or SPS no older than 24 months: defined in the software stack KPI (binary measure, 0 or 100, **weighted 50%**). Adoption of secure baseline: determined by % of monitored landscapes in non-compliant status. Each managed landscape shall adopt at least the standard content from the SAP security baseline as per guidance for SAP Cloud ALM "Configuration and Security Analysis". |
| **Key results** | Keep SAP systems consistently updated with the latest recommended software stacks. Regularly assess and promptly remediate security configuration gaps. Apply secure-by-default and clean core principles to all system changes and upgrades. Automate monitoring and reporting of system lifecycle and security compliance status. |
| **Recommended tool** | System health via RISE with SAP Methodology dashboard; additional metrics require SAP Cloud ALM standard capabilities |
| **Prerequisites** | RISE with SAP Methodology dashboard access; SAP Cloud ALM configuration and security analysis |
| **Cadence** | **Daily** |
| **Measurement guidance** | FPS or SPS no older than 24 months: SAP Cloud ALM Application Help → Software Stack. Adoption of secure baseline: SAP Cloud ALM for Operations Expert Portal → Configuration and Security Analysis. Where trend metrics not yet available in SAP Cloud ALM, measure manually via SAP EarlyWatch Alert, SAP Security Optimization services, and SAP Focused Run/Solution Manager capabilities. |
| **Measurement type** | **Automatic** |

---

## Connection to Governance & Maturity Practices (Slides 91-95)

Each KPI category is directly linked to specific governance & maturity practices:

| KPI Category | Linked Governance & Maturity Practice(s) |
|---|---|
| Software stack | Maturity of release management / Maturity of secure operations |
| Integrated toolchain adoption | Maturity of business transformation toolchain / Maturity of clean core governance |
| Adopt clean core requirements | Maturity of continuous improvement / Maturity of clean core governance |
| Agile delivery and operational excellence | Maturity of software delivery efficiency / Maturity of test management / Maturity of release management / Maturity of IT operations excellence |
| Enduring operational efficiency | Maturity of IT operations excellence |
| Embed secure operations | Maturity of secure operations |

> *Full per-practice evaluation criteria and 0–5 rating guidance: `knowledge/04-governance-maturity-operations.md`*

---

## RISE with SAP Methodology Dashboard — Operations View

The RISE with SAP Methodology Dashboard in SAP Cloud ALM includes an **Operations View** that maps directly to the Operations KPIs. This view provides daily automated compliance data and is the primary measurement tool for the Enduring Operational Efficiency and Embed Secure Operations KPI categories.

> Full reference (setup, all KPI/metric definitions, calculation examples, rating thresholds, FAQ): `clean-core-general` → `knowledge/06-rise-dashboard.md`

### How Operations View Maps to Operations KPI Categories

| Operations View Score/KPI | Maps to KPI Category |
|---|---|
| **Operations Score** (overall) | Enduring operational efficiency |
| **Security score** → System Hardening, Vulnerability & Lifecycle, Identity & Access Control | Embed secure operations |
| **System Health score** → Connectivity, Exceptions, Background Processing, Performance | Enduring operational efficiency |
| **Operations Setup score** → 8 use-case KPIs | Enduring operational efficiency (toolchain setup aspect) |

### Score Architecture

**Operations Score** = Security (40%) + System Health (30%) + Operations Setup (30%)

**Rating thresholds:** Good (Green) > 85%; Warning (Orange) 70–85%; Critical (Red) < 70%

### Security Score Sub-KPIs

| KPI | Weight | What it measures |
|---|---|---|
| System Hardening | 40% | 17 security metrics (password policies, gateway settings, message server, change options) |
| Vulnerability & Lifecycle | 40% | Age of support packages, SAP Kernel, SAP Cryptolib (SLA: Compliant; each metric 25%) |
| Identity & Access Control | 20% | Standard user accounts (SAP*, TMSADM, SAPCPIC, EARLYWATCH) in correct state |

### System Health Score Sub-KPIs

| KPI | Weight | SLA |
|---|---|---|
| Connectivity | 50% | Critical System Heartbeat: 10%; Critical Instance Heartbeat: 10% |
| Exceptions | 25% | Runtime Errors (ABAP dumps): 400/day; System Logs: 9,000/day; Application Logs: 2,500/day |
| Background Processing | 15% | Batch Jobs Aborted per client/5 min: 2.24 |
| Performance | 10% | Avg Response Time: 4,000 ms; Max Response Time: 200,000 ms |

### Operations Setup Score Sub-KPIs

| KPI | Weight | Measures |
|---|---|---|
| Health Monitoring | 20% | SAP Cloud ALM Health Monitoring app configured + active |
| Exception Monitoring | 20% | Integration & Exception Monitoring configured + active for runtime errors/logs |
| Integration Monitoring | 15% | Integration & Exception Monitoring configured for SAP AIF messages |
| Job & Automation Monitoring | 15% | Job & Automation Monitoring app configured + active |
| Configuration & Security Analysis | 15% | Configuration & Security Analysis use case active |
| Real User Monitoring | 5% | Real User Monitoring app configured + active |
| Business Service Management | 5% | System added to a business service with SLOs and event actions |
| Business Process Monitoring | 5% | Business Process Monitoring app configured + active |

**Prerequisites for Operations View:** ST-PI 7.40 SP28+; SAP Cloud ALM integration; ABAP Runtime/System Log/Application Log metrics manually enabled; productive systems only.

**Key reference links:**
- Full KPI deck (external): https://dam.sap.com/mac/app/p/pdf/asset/preview/XbqgDc4?ltr=a&rc=10&doi=SAP1240359
- Governance & Maturity deck: https://dam.sap.com/mac/app/p/pdf/asset/preview/a5A7qyM?ltr=a&rc=10&doi=SAP1222195
- RISE with SAP Methodology dashboard: https://www.sap.com/products/erp/rise/methodology/clean-core.html
