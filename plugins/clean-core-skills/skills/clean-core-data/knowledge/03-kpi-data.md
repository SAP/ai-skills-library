# Clean Core Data — KPI Detail

**Source:** Clean Core KPI Measurement Deck (SAP1240359 v1.3) — Data section (Slides 42–50)  
**Ingested:** 2026-09-13  
**Purpose:** Full per-KPI detail for the two data KPI categories: Data Volume Efficiency and Data Quality. Covers calculation details, measurement guidance, tools, cadence, and governance & maturity relevance.

---

## Data KPI Context (Slide 42)

### Why Data KPIs Matter — Expected Customer Benefits

| Benefit type | Specific benefit | Quantified? |
|---|---|---|
| Strategy enablement | Improve decision-making with higher-quality data | NQ |
| Business value | Enable greater value from business AI with relevant and reliable data | Q |
| Risk mitigation | Reduce costs to address data quality issues | NQ |
| Risk mitigation | Reduce risks associated with poor data quality | NQ |
| IT spend effectiveness (TCO) | Reduce (cloud) infrastructure costs | Q |

**What clean core data achieves (Why):**
- Drive process efficiency by ensuring consistent, high-quality data
- Ensure trusted, reliable data as the foundation for accurate AI and analytics
- Optimized IT spend through reduced infrastructure and upgrade demands
- Lower operational risk by eliminating poor data quality issues
- Unify your data landscape by governing SAP and non-SAP systems under one framework
- Ensure semantic connectivity of data for consistent interpretation
- Harmonize data by aligning it with the latest standards
- Manage data volumes to support scalability
- Maintain compliant data through continuous quality controls
- Govern data under a defined framework to ensure integrity and accountability

---

## Data KPI Categories at a Glance (Slide 43)

| KPI Category | KPI Name | What It Measures |
|---|---|---|
| **Data volume efficiency** | Data volume improvement potential | Efficiency of data volume management based on SAP data volume management best practices |
| **Data quality** | Data quality index | Consistency and quality of data in chosen areas |

Both KPIs are accessible within the RISE with SAP Methodology Clean Core Q-gates and the RISE with SAP Methodology Dashboard.

---

## KPI Category 1: Data Volume Efficiency

### Overview (Slide 45)

Five KPI metrics within data volume efficiency:

| Metric | Description |
|---|---|
| **% of data older than SAP Best Practice** | Outdated data |
| **% of data for which NSE can be activated** | Unused data (memory/disk data never accessed) |
| **% of indexes that can be removed** | Redundant data |
| **Total disk & total memory** | Optimized SAP HANA usage |
| **% of custom tables** | Custom table footprint |

**Current measurement tools:** Data Volume Management chapter in the Early Watch Alert report, Data Volume Management app in SAP Readiness Check, DVM Workcenter, Data Volume Management self-service, Data capacity excellence dashboard in AI assistance from SAP MaxAttention.

**Future:** RISE with SAP Methodology dashboard.

### Data Volume Efficiency KPI — Full Detail (Slides 46–47)

**Context:** SAP data volume efficiency is a core element of the clean data framework, enabling organizations to efficiently manage data throughout its lifecycle — from creation to archiving and deletion — to ensure compliance, system agility, and performance.

**Value proposition:** Enables continuous right-sizing of system landscapes, helping avoid both storage bottlenecks and over-provisioned infrastructure. With proactive monitoring of data volume efficiency KPIs, organizations can:
- Control data growth
- Ensure timely archiving and deletion
- Minimize additional infrastructure investments
- Maintain a scalable, future-ready system landscape

**Measurement framework:** Within the RISE with SAP Methodology, data volume efficiency is evaluated through two complementary approaches:
1. Governance and operational maturity assessment: reviews data management policies and practices
2. Automated system analysis: monitors KPIs to provide actionable insights

**Calculation Details:**

| Metric | Formula |
|---|---|
| **Outdated data** | Total sum of data in memory and disk (GB) where creation date is older than SAP Best Practice residence time (depending on document type) |
| **Unused data** | Total sum of table data in memory and disk (GB) that is never accessed |
| **Redundant data** | Total sum of table indexes in memory and disk (GB) that are not used (redundant) and can be dropped without impact |
| **Optimized SAP HANA usage** | Current memory and disk usage of the system compared against total system sizes of memory and disk (independent of system size) |
| **Custom table footprint** | Total sum of custom tables in memory and disk (GB) |

**Key results:** Active and regular monitoring of data volume efficiency KPIs ensures:
- Controlled data growth
- Timely archiving and deletion
- Cost savings by reducing additional infrastructure needs
- Scalable infrastructure

| Field | Value |
|---|---|
**Recommended tools — Now:** Data Volume Management chapter in the Early Watch Alert report; Data Volume Management app in SAP Readiness Check; data volume management self-service; data capacity excellence dashboard in AI assistance from SAP MaxAttention
**Recommended tools — Future/Dashboard:** RISE with SAP Methodology Dashboard in SAP Cloud ALM — Data section of the System View shows: **Data Volume Efficiency score** (composite), **SAP HANA Memory (%)**, **SAP HANA Disk (%)**, **Unused Data (GB)**, **Redundant Data (GB)**, **Outdated Data (GB)**, **Custom Table Footprint (GB)**. Plus a **Data Volume Efficiency deep dive** with per-table breakdowns for each KPI. See `clean-core-general` knowledge file `06-rise-dashboard.md` for full KPI definitions and setup requirements (ST-PI 7.40 SP31+, SAP Note 3703380, batch user authorizations).
**Prerequisites — Now:** Setup of the data capacity AI assistance dashboard
**Prerequisites — Future/Dashboard:** ST-PI 7.40 SP31+ add-on + SAP Note 3703380 on productive systems; batch user with roles `SAP_SDF_ALM_METRIC_PUSH_FND` and `SAP_SDF_ALM_METRIC_PUSH_DVM` in the PUSH Data Provider; data runs for productive systems only
| **Cadence** | Quarterly (during transformation journey); Twice per year (after reaching a stable state) |
| **Type** | Semi-automatic |
| **Value** | Quantifiable |
| **Effort** | Medium |

**Measurement guidance — Now:**
- SAP Note 1257308 to set up Early Watch Alert report
- SAP Note 3404904 to set up SAP Readiness Check
- SAP Note 1487247 for the data volume management self-service
- Subscription to the data capacity excellence dashboard in AI assistance from SAP MaxAttention

**Measurement guidance — Future:** Leverage the RISE with SAP Methodology dashboard.

**Governance & maturity relevance:** Maturity of data volume efficiency management (DAT-04)

---

## KPI Category 2: Data Quality

### Overview (Slide 48)

Data quality KPIs measure the consistency and quality of data in chosen areas via a **Data Quality Index**.

### Data Quality KPI — Full Detail (Slides 49–50)

**Context:** SAP recommends leveraging data quality assessment tools and services to achieve transparency and to perform regular data cleansing and quality assurance activities, ensuring high-quality data.

**Value proposition:** Regular data quality assessments are essential for maintaining consistent, reliable, and trustworthy data that supports informed decision-making and efficient operations. Effective data cleansing processes ensure that organizations can rely on accurate and complete information. A dedicated governance board enforces robust data strategies and promotes data harmonization across the enterprise.

**Six data quality dimensions and their KPIs:**

| Dimension | Weight | KPI |
|---|---|---|
| **Accuracy** | 10% | % of correct records |
| **Completeness** | 10% | % of non-missing values |
| **Consistency** | 40% | % of fields without conflicts across datasets |
| **Timeliness** | 5% | % of records updated within a defined timeframe |
| **Uniqueness** | 30% | % of unique records |
| **Validity** | 5% | % of fields adhering to defined rules |

**Composite Score Calculation:**

```
Data Quality Index = Σ (Dimension score × Weight)
```

Each metric is assigned a weight based on the relevance and importance of the respective area (weights shown above are a proposal). The collected dataset must be evaluated against the defined metrics, then multiplied by their respective weights and summed for the composite Data Quality Index.

*Note: Consistency (40%) and Uniqueness (30%) together account for 70% of the total score, reflecting their outsized impact on data reliability.*

**Key results:** Active and regular monitoring of data quality ensures:
- Transparency
- Timely identification of data mismatches and inconsistencies that impact system performance
- Clean, reliable data

| Field | Value |
|---|---|
| **Recommended tools — Now** | Financial Data Quality app in SAP Readiness Check; Financial Data Quality chapter in the Early Watch Alert report |
| **Recommended tools — Future/Dashboard** | RISE with SAP Methodology dashboard (Data Volume Efficiency section in System View); data quality dashboard in AI assistance from SAP MaxAttention |
| **Prerequisites — Future/Dashboard** | Setup of data collectors for RISE with SAP Methodology dashboard (ST-PI 7.40 SP31+ + SAP Note 3703380); setup of the data quality AI assistance dashboard |
| **Cadence** | Quarterly (during transformation journey); Twice per year (after reaching a stable state) |
| **Type** | Low / Medium |
| **Value** | Non-quantifiable |
| **Effort** | Medium |

**Measurement guidance — Now:**
- Implement SAP Note 3404904 to leverage SAP Readiness Check
- Implement SAP Note 1257308 to set up Early Watch Alert report

**Measurement guidance — Future:** Leverage the RISE with SAP Methodology dashboard.

**Governance & maturity relevance:** Maturity of data quality management (DAT-03)

---

## KPI Measurement Type Summary

| KPI Category | KPI Name | Type | Cadence | Effort |
|---|---|---|---|---|
| Data volume efficiency | Data volume improvement potential | Semi-automatic | Quarterly (transformation); Twice/year (stable) | Medium |
| Data quality | Data quality index | Low/Medium | Quarterly (transformation); Twice/year (stable) | Medium |
