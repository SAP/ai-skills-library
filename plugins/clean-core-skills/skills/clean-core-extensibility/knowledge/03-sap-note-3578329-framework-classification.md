<!-- Source: SAP Note 3578329 v21 (05.08.2026) — requires S-User to access -->

# Source: SAP Note 3578329 — Frameworks, Technologies and Development Patterns in Context of Clean Core Extensibility

**Note number:** 3578329
**Component:** BC (Basis Components)
**Version:** 21 — Released 05.08.2026
**Access:** Requires S-User login at https://me.sap.com/notes/3578329

---

## Purpose

This note answers: *"I plan to use a specific framework, technology or ABAP development pattern — is this considered clean core?"*

It provides the official SAP classification of frameworks, technologies, and development patterns by clean core level (A–D), upgrade stability, and public cloud readiness.

---

## How to Read the Classification Table

**Conditional / multiple levels** — some entries carry multiple levels (e.g., A/B) because:
- The framework can be used via differently classified APIs (released C1 → Level A; classic API → Level B)
- Cloud readiness depends on which specific APIs are used

Unless explicitly stated as "Usage of individual SAP …", the classification refers to **general usage** of the framework or technology.

**Scope** — the level concept applies **only to clean core extensibility**, not to other clean core dimensions (integration, data, processes). Specifically it covers:
- Calling a framework's API from custom/partner code
- Extending SAP standard objects or implementing SAP enhancements in the context of a framework
- Creating own objects in customer/partner namespace related to a framework

It does **not** apply to: calling a standard SAP remote API from another system, or using SAP standard functionality without customer extension involvement.

**Single-implementation extension techniques** — some techniques (Customer Exits, Single-Use BAdIs) support only one concurrent active implementation. If two implementations exist (e.g., customer + 3rd-party add-on), conflicts can occur. This does not negatively affect the clean core level — managing conflicts is the customer's responsibility.

---

## Classification Table

API classification reference: https://github.com/SAP/abap-atc-cr-cv-s4hc

### Application-Specific

| Framework / Technology | Component | Level | Upgrade Stable | Public Cloud Ready | Notes |
|---|---|---|---|---|---|
| Organizational Management | BC-BMT-OM | **B** | yes | no | |
| Radio Frequency Framework (SAP EWM) | SCM-EWM-RF | **B** | yes | no | |
| Transportation Management (SAP TM) Extensibility | TM-* | — | — | — | No single rating — derived from underlying frameworks (BOBF, BAdIs, Webdynpro etc.) listed separately |
| Business Data Toolset (BDT) | CA-GTF-BDT | **B** | yes | no | |

### Automation-Related

| Framework / Technology | Component | Level | Upgrade Stable | Public Cloud Ready | Notes |
|---|---|---|---|---|---|
| Application Jobs | BC-SRV-APS-APJ | **A/B** | yes | conditional | Cloud readiness depends on usage of released framework APIs |
| Classical Batch Jobs (SM37) | BC-CCM-BTC | **B** | yes | no | |
| Technical Job Repository | BC-CCM-BTC-JR | **B** | yes | no | |
| Manage Substitution and Validation Rules (Fiori) | FI-SL-VSR | **A** | yes | yes | |
| Classic Substitution and Validation (GGB0/GGB1) | FI-SL-VSR | **B** | yes | no | Successor: Manage Substitution and Validation Rules (Fiori) |
| Batch Input / Batch Data Communication (BDC) | BC-ABA-SC | **B/C** | conditional | no | BDC Framework / APIs (BDC_* FMs) = Level B; individual batch input sessions on SAP transactions = Level C |
| FI-CA Mass Activities | FI-CA | **B** | yes | no | SAP Note 144461 |
| Post-Processing-Framework (PPF) | BC-SRV-GBT-PPF | **B** | yes | no | |

### Customizing

| Framework / Technology | Component | Level | Upgrade Stable | Public Cloud Ready | Notes |
|---|---|---|---|---|---|
| Factory Calendar | BC-SRV-ASF-CAL | **A/B** | yes | conditional | Cloud readiness depends on usage of released framework APIs |
| Units of Measurement | BC-SRV-ASF-UOM | **A/B** | yes | conditional | Cloud readiness depends on usage of released framework APIs |
| Currency Handling | BC-SRV-BSF-CUR | **A/B** | yes | conditional | |
| Date Rules | BC-SRV-TIM-TR | **B** | yes | no | |

### Data Management

| Framework / Technology | Component | Level | Upgrade Stable | Public Cloud Ready | Notes |
|---|---|---|---|---|---|
| Archive Development Kit | BC-CCM-ADK | **A/B** | yes | conditional | Cloud readiness depends on released framework APIs; successor: Data Archiving |
| Information Lifecycle Management (ILM) | BC-ILM | **A/B** | yes | conditional | Cloud readiness depends on released framework APIs; successor: Data Destruction |
| Document Relationship Browser | BC-SRV-GBT-DRB | **B** | yes | no | |
| Table Analysis TAANA | BC-CCM-TAN | **B** | yes | no | |
| Archive Information System | BC-CCM-ADK-AS | **B** | yes | no | |
| Notes for Application Objects | BC-SRV-GBT-NTE | **B** | yes | no | |
| Generic Object Services (GOS) | BC-SRV-GBT-GOS | **B** | yes | no | |
| Online Text Repository (OTR) | BC-SRV-OTR | **B** | yes | no | |
| Business Document Service | BC-SRV-BDS | **B** | yes | no | |
| Archive Link | BC-SRV-ARL* | **B** | yes | no | Successor: BTP Document Management Service |
| Knowledge Provider (KPro) | BC-SRV-KPR* | **B** | yes | no | |

### Enhancement-Related

| Framework / Technology | Component | Level | Upgrade Stable | Public Cloud Ready | Notes |
|---|---|---|---|---|---|
| **BAdI (Kernel-based)** | BC-DWB-CEX | **A** | yes | yes | Gold standard for enhancement |
| **BAdI (classic)** | BC-DWB-CEX | **B** | yes | no | Successor: BAdI (Kernel-based) |
| Customer Exits (SMOD/CMOD) | BC-DWB-CEX | **B** | yes | no | Check table MODSAP to verify exit type |
| **Explicit Enhancement Options excl. BAdIs** (Enhancement Points & Sections) | BC-DWB-CEX | **D** | no | no | Successor: BAdI (Kernel-based) |
| **Implicit Enhancement Options** | BC-DWB-CEX | **D** | no | no | Includes: implicit enhancements in ABAP source code, enhancing FM parameter interfaces, enhancing global class/interface components. Successor: BAdI (Kernel-based) |
| Extension Components Library (XCO) | BC-SRV-APS-EXT-XCO | **A** | yes | yes | |
| DDIC Field Extensions (e.g. Appends) | BC-DWB-DIC | **A/B/C/D** | conditional | conditional | Depends on usage — see SAP Note 3632977 |
| SD/LE User Exits (Form Routines) & VOFM Routines | SD/LE | **B/D** | conditional | no | See SAP Note 3589866 |
| Business Transaction Events (BTE) | CA-GTF-TS-BRHF | **B** | yes | no | See SAP Note 3641991 |
| FI-CA Events / FQEVENTS | FI-CA | **B** | yes | no | |

### Integration-Related

| Framework / Technology | Component | Level | Upgrade Stable | Public Cloud Ready | Notes |
|---|---|---|---|---|---|
| **OData Services via Service Definition/Binding (RAP)** | BC-ESI-RAP-SRV | **A** | yes | yes | Modern approach |
| AIF (Application Interface Framework) | BC-SRV-AIF | **A/B** | yes | conditional | See SAP Note 3622023 |
| SOAP-based Web Service Framework — Proxy Generation | BC-DWB-PRX / BC-ESI-WS-ABA | **A/B** | yes | conditional | See SAP Note 3594071 |
| Application Link Enabling (ALE) & IDoc | BC-MID-ALE | **B** | yes | no | Successor: Process Integration Technologies |
| BAPI Framework — Technology | BC-MID-API | **B** | yes | no | Successor: RAP |
| OData Services via SAP Gateway Service Builder (SEGW) | OPU-BSE-SB | **B** | yes | no | Successor: RAP. Note: unsupported software components in S/4HANA |
| **Usage of individual SAP BAPIs** | See individual BAPI | **B/C/D** | conditional | no | Level depends on classification of individual BAPI |
| **ODP Framework RFC APIs** | BC-BW-ODP | **D** | no | no | See SAP Note 3255746 |

### Other Frameworks

| Framework / Technology | Component | Level | Upgrade Stable | Public Cloud Ready | Notes |
|---|---|---|---|---|---|
| **RAP / RAP Extensibility** | BC-ESI-RAP-SRV | **A** | yes | yes | Gold standard for transactional apps |
| **CDS Views — Technology (own CDS views)** | BC-DWB-DIC | **A** | yes | yes | Creating own CDS views |
| **Usage of individual SAP CDS Views** | See individual CDS view | **A/B/C/D** | conditional | conditional | Level depends on release/classification state of individual CDS view |
| Business Object Processing Framework (BOPF) | BC-ESI-BOF | **B** | yes | no | Successor: RAP |
| Business Object Repository (BOR) — Technology | BC-DWB-TOO-BOB | **B** | yes | no | Successors: RAP events, SAP Event Mesh. See SAP Note 3478579 |
| ABAP Shared (Memory) Objects | BC-DWB-TOO-SHM | **B** | yes | no | |
| SAP Query — Framework | BC-SRV-QUE | **C** | yes | no | Successor: CDS Views. Stable as framework, but purpose for arbitrary table access is comparable to direct table read access — same disadvantages → Level C |
| Logical Databases | BC-DWB-TOO-LDB | **C** | yes | no | Successor: CDS Views. Same reasoning as SAP Query |

### Output Management

| Framework / Technology | Component | Level | Upgrade Stable | Public Cloud Ready | Notes |
|---|---|---|---|---|---|
| Email Templates | BC-SRV-COM-OM | **A/B** | yes | conditional | Level A if ABAP Cloud language version; Level B if classic |
| Business Communication Services | BC-SRV-COM | **A/B** | yes | conditional | |
| Forms Processing | BC-SRV-FP | **A/B** | yes | conditional | |
| Adobe Forms | BC-SRV-FP-OM | **A/B** | yes | conditional | |
| Cloud Printing | BC-SRV-PRN-OM | **A/B** | yes | conditional | |
| Alert Management | BC-SRV-GBT-ALM | **B** | yes | no | |
| SAPscript | BC-SRV-SCR | **B** | yes | no | Successor: Output Management — Print Forms |
| SmartForms | BC-SRV-SSF | **B** | yes | no | Successor: Output Management — Print Forms |
| Spool | BC-CCM-PRN | **B** | yes | no | |
| NAST | SD-BF-OC | **B** | yes | no | |

### Process Flow

| Framework / Technology | Component | Level | Upgrade Stable | Public Cloud Ready | Notes |
|---|---|---|---|---|---|
| Business Rules Framework (BRF+) | BC-SRV-BR | **A/B** | yes | conditional | Cloud readiness depends on released framework APIs |
| Classic Workflow | BC-BMT-WFM | **B** | yes | no | Successor: BTP SAP Build Process Automation |
| Flexible Workflow | BC-BMT-WFM | **B** | yes | no | Successor: BTP SAP Build Process Automation |

### Reuse Services

| Framework / Technology | Component | Level | Upgrade Stable | Public Cloud Ready | Notes |
|---|---|---|---|---|---|
| Change Documents | BC-SRV-ASF-CHD | **A/B** | yes | conditional | |
| Number Ranges | BC-SRV-NUM | **A/B** | yes | conditional | |
| Application Log | BC-SRV-BAL | **A/B** | yes | conditional | |
| SAPoffice | BC-SRV-COM | **B** | yes | no | |
| SAPphone | BC-SRV-COM-TEL | **B** | yes | no | |
| Object Link | BC-SRV-GBT-OBL | **B** | yes | no | |
| Appointment Calendar | BC-SRV-GBT-CAL | **B** | yes | no | |
| Case Management | BC-SRV-CM | **B** | yes | no | |
| Records Management | BC-SRV-RM | **B** | yes | no | |
| Geographical Enablement Framework | CA-EPT-GEF | **B** | yes | no | |

### UI-Related

| Framework / Technology | Component | Level | Upgrade Stable | Public Cloud Ready | Notes |
|---|---|---|---|---|---|
| **Fiori / UI5** | CA-UI5 | **A** | yes | yes | Gold standard for UI |
| **SAPUI5 Key User Adaptation** | CA-UI5-FLR-TA | **A** | yes | yes | |
| **SAPUI5 Developer Adaptation (Adaptation Project — "CloudReady")** | CA-UI5-FL-ADP | **A** | yes | yes | |
| **SAP Screen Personas for SAP GUI for HTML (WebGUI)** | BC-PER | **A** | yes | yes | |
| ABAP List Viewer (ALV) Display Functionality | BC-SRV-ALV | **B** | yes | no | Successor: Fiori/UI5 |
| Floor Plan Manager | BC-WD-CMP-FPM | **B** | yes | no | Successor: Fiori Elements |
| Webdynpro | BC-WD-ABA | **B** | yes | no | Successor: Fiori/UI5 |
| WebClient UI | CA-WUI | **B** | yes | no | Successor: Fiori/UI5. See SAP Note 3591718 |
| Standard Dialogs | BC-SRV-ASF-POP | **B** | yes | no | Successor: Fiori/UI5 |
| Dynamical Documents | BC-CI-DYD | **B** | yes | no | |
| ABAP Reports | BC-ABA-LA | **B** | yes | no | |
| Transaction Variants (SHD0) | BC-ABA-TV | **B** | yes | no | |
| Pivot Browser Reporting Framework | PSM-FM-IS | **B** | yes | no | Successor: Fiori/UI5 |
| ABAP List Viewer (ALV) Edit Functionality | BC-SRV-ALV | **C** | yes | no | Successor: Fiori/UI5. Applies only to the experimental ALV edit functionality (not intended for customer use). See SAP Notes 551605 and 695910. The display functionality of ALV remains Level B. |
| **SAP Screen Personas for Web Dynpro ABAP / for SAPGUI for Windows (WinGUI)** | BC-PER | **D** | no | no | Sunsetted. See SAP Notes 3239603, 2080071 |

---

## Related SAP Notes

| Note | Component | Title |
|---|---|---|
| 3632977 | BC-DWB-DIC | Clean Core Extensibility: DDIC Extensions |
| 3478579 | BC-DWB-TOO-BOB | Business Object Repository in Context of Clean Core |
| 3589866 | SD-SLS | Clean Core: User exits & VOFM in SD/LE |
| 3641991 | CA-GTF-TS-BRHF | Business Transaction Events (BTE) — Clean Core |
| 3622023 | BC-SRV-AIF | AIF — Clean Core |
| 3594071 | BC-ESI-WS-ABA | SOAP Web Services — Clean Core |
| 3255746 | BC-BW-ODP | ODP Framework RFC APIs |
| 3591718 | CA-WUI | WebClient UI Framework in Context of Clean Core |
| 3658978 | XX-SER-REL-S4HANA | Object released status and API in Context of Clean Core |
| 3593439 | — | ABAP Cloud for Key Users — language version detection fix |
| 3690029 | BC | Integration Technologies and Frameworks in Context of Clean Core Integration |

---

## Quick Reference: Level Summary

**Level A (cloud ready + upgrade stable):**
BAdI (kernel-based), RAP / RAP Extensibility, CDS Views (own), OData via Service Binding, Fiori/UI5, SAPUI5 Key/Developer Adaptation, SAP Screen Personas for WebGUI, Extension Components Library (XCO), Manage Substitution/Validation Rules (Fiori)

**Level B (upgrade stable, not public-cloud-ready — the "classic API" tier):**
Classic BAdI, Customer Exits (SMOD/CMOD), Classic Workflow, Flexible Workflow, BAPI Framework, OData via SEGW, ALE/IDoc, BOPF, BOR, Webdynpro, ALV Display, Floor Plan Manager, WebClient UI, Classic Batch Jobs, most Reuse Services, most Output Management

**Level C (conditionally stable — avoid where possible):**
SAP Query, Logical Databases, ALV Edit Functionality (experimental), Batch Input sessions on individual transactions (BDC session-level), internal SAP objects not classified as classic API

**Level D (not recommended — eliminate):**
Explicit Enhancement Points/Sections (non-BAdI), Implicit Enhancements, ODP Framework RFC APIs, SAP Screen Personas for WinGUI/WebDynpro
