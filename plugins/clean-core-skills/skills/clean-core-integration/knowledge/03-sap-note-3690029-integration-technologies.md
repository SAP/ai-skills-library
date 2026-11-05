# Clean Core Integration — SAP Note 3690029

**Source:** SAP Note 3690029 — Integration Technologies and Frameworks in Context of Clean Core Integration  
**Component:** BC (Basis Components) | **Version:** 8 | **Released:** 16.07.2026  
**Ingested:** 2026-09-13  
**Purpose:** Authoritative classification of integration technologies by clean core level. The definitive reference for determining which interface technology to use for SAP S/4HANA Cloud Private Edition integrations. Complements but does not overlap with SAP Note 3578329 (extensibility).

---

## Overview

This note provides the **clean core level** for common interface technologies and indicates their public cloud readiness and conformity with modern integration standards.

It introduces a **level-based clean core integration model** and classifies commonly used interface technologies, protocols, and patterns according to their cloud readiness and modern integration standards.

**Guidance principle:** Aim for the highest clean core level by using standard, released SAP integration content. If standard content does not meet the requirement, choose the next-best level and minimize local changes. Reassess regularly to adopt standard content when it becomes available.

---

## Differentiation from SAP Note 3578329 (Extensibility)

SAP Note 3578329 is **only applicable for extensibility use cases**. This SAP Note complements, but does not overlap with, the clean core extensibility guidance.

**Where a framework/technology relates to multiple clean core principles (e.g., BAPIs relate to both extensibility and integration), the rating in this note exclusively applies to the integration principle, not to any other.**

**Extensibility-specific use cases (covered by SAP Note 3578329):**
- Calling an API of a framework from within custom or partner code
- Extending SAP standard objects or implementing SAP enhancements in the context of a given framework or technology
- Creating own objects in customer or partner namespace related to a given framework or technology

**Integration use cases (covered by this note — SAP Note 3690029):**
- Calling a standard SAP remote API (OData, web service, IDoc, BAPI...) from another system
- The way integrations are implemented with external systems (including the use of remote function modules via released interfaces)

**When both principles apply** (e.g., IDoc integration + an IDoc extension): aim for the highest possible clean core level and apply both notes — integration guidance from this note to choose the technology, extensibility guidance from SAP Note 3578329 to implement the extension.

---

## Level Concept and Usage

The same level concept as used for extensibility (A–D) applies for integration:
- **Stay clean:** choose the highest level available for your use case
- **Get clean:** from your current clean core level, plan to move to the next higher level

---

## Evaluation Criteria

Classification of an integration technology or pattern is based on:

1. **Public cloud readiness:** Supported in SAP S/4HANA Cloud Public Edition
2. **Modern integration standards:**
   - Based on established cloud and internet standards
   - Alignment with modern integration approaches — event-driven architecture (EDA) and API-managed strategy

*Note: Upgrade stability depends on the release status of the underlying ABAP object and has not been included in this evaluation. Verify upgrade stability via SAP Business Accelerator Hub, SAP Note 3578329, and/or the Cloudification Repository.*

---

## Where to Find Released Remote APIs and Events

- **SAP Business Accelerator Hub** (https://hub.sap.com) — catalogs of released APIs and events, documentation, versioning information
- **SAP Help Portal** (https://help.sap.com) — integration and modernization guides, release information for SAP S/4HANA remote APIs and business events
- **Cloudification Repository** (https://sap.github.io/abap-atc-cr-cv-s4hc) — object-level release state and classification for SAP S/4HANA (current version focuses on local APIs including remote-enabled BAPIs)

---

## Classification Table

*Note: The table below reflects general guidance; actual design and applicability are use-case dependent. The table covers integration technologies available in SAP S/4HANA Cloud, private edition; HANA platform and BW-specific capabilities are out of scope.*

### Event Integration

| Name | Clean Core Level | Public Cloud Ready | Modern Integration Standards | Notes |
|---|---|---|---|---|
| **Eventing via RAP (AMQP/MQTT)** | **A** | Yes | High — cloud-native, open standard, supports EDA | Strategic approach for event-driven integration |
| **Eventing via Event Enablement Add-On** | **B** | No | High | No migration path to SAP S/4HANA Cloud |
| **Business Events via AIF** | **C** | No | Low — legacy event handling, no alignment with modern EDA standards | No migration path to SAP S/4HANA Cloud |

### Process Integration

| Name | Clean Core Level | Public Cloud Ready | Modern Integration Standards | Notes |
|---|---|---|---|---|
| **OData** | **A** | Yes | High — open internet standard, supports API-managed strategy | V4 should be preferred over V2 |
| **OData via RAP Service Binding** | **A** | Yes | High — cloud-native, open standard, supports API-managed strategy | |
| **OData via SAP Gateway Service Builder** | **B** | Yes | Medium | |
| **CDS Views via Service Binding Configuration** | **A** | Yes | High — supporting API-managed strategy and EDA | |
| **Web Services via SOA Manager** | **A** | Yes | High — based on established web service standards | |
| **IDoc via HTTPS** | **B** | No | Low — SAP maintenance support only | Only partially supported in SAP S/4HANA Cloud; no migration path |
| **IDoc via RFC** | **C** | No | Low — SAP maintenance support only | No migration path to SAP S/4HANA Cloud; valid for e.g. on-premise to on-premise |
| **BAPI via RFC** | **B** | No | Low — SAP maintenance support only | Not supported in SAP S/4HANA Cloud Public Edition |
| **BAPI via SOAP Wrapper** | **B** | No | Low — SAP maintenance support only | Only partially supported in SAP S/4HANA Cloud |

### Process Integration (Runtime)

| Name | Clean Core Level | Public Cloud Ready | Modern Integration Standards | Notes |
|---|---|---|---|---|
| **ABAP Proxy using Web Services runtime via SOA Manager** | **B** | Partially | Low — limited public cloud readiness, not aligned with modern integration standards | Refer to SAP Help Portal for ABAP Proxy guidance |
| **ABAP Proxy using XI (Integration Engine)** | **C** | No | Low — legacy integration technology, no cloud readiness | Requires migration to RAP-based approach; refer to SAP Help Portal |

### Communication Protocols

| Name | Clean Core Level | Public Cloud Ready | Modern Integration Standards | Notes |
|---|---|---|---|---|
| **HTTP(S)** | **A** | Yes | High — supports API-managed strategy | |
| **RFC (CPI-C)** | **B** | Partially | Low — limited cloud readiness | E.g., for public cloud to on-premises scenarios |
| **WebSocket RFC** | **B** | Yes | Medium | For SAP S/4HANA 1909 and higher |
| **AMQP/MQTT/PCP** | **C** | Yes | Low — see ABAP Integration and Connectivity Guide | In general, specific use case; check documentation |
| **SFTP** | **D** | No | Very Low — no API contract or governance | Not supported in SAP S/4HANA Cloud |
| **FTP** | *(D)* | No | Very Low — unencrypted, no API contract or governance | No migration path available; neither cloud nor private cloud |

### Data Integration — Interfaces / Technologies

| Name | Clean Core Level | Public Cloud Ready | Modern Integration Standards | Notes |
|---|---|---|---|---|
| **OData CDS Views** | **A** | Yes | Yes (OData; V4 analytical services endorsed) | For released CDS views; Analytical CDS Views and OData |
| **Delta Share** | **A** | Yes | Yes | Part of SAP BDC data product story |
| **JDBC/ODBC** | **D** | No | No (DB-level access, not an SAP modern API) | Non-published interface; usage as wholesale data extraction prohibited by API Policy (Section 2.2.2); distinguish Clean Core Level D from API Policy prohibition |
| **RFC (ODP)** | **Forbidden** (Level concept not applicable) | No | No | Prohibited by the API Policy; any use of ODP-RFC by customers in BW/4HANA, on-premise or private cloud is prohibited |
| **ODP-OData (HTTP)** | **Supported** (Level concept not applicable) | No | No | Supported interface for delta extraction with controls; endorsed alternative to ODP-RFC |

### Data Integration — Products / Components

| Name | Clean Core Level | Public Cloud Ready | Modern Integration Standards | Notes |
|---|---|---|---|---|
| **Data Replication Framework** | **A** | Yes | Yes (leverages released APIs; scenario-dependent) | Strategic SAP solution for data integration; exposed to customers via SAP Note |
| **Data Products** | **A** | Yes | Yes | Part of SAP BDC data product story |
| **BW Extractors** | **B** | No | Medium | Available for SAP BW/4HANA |
| **SLT** | **C** | No | No (not based on HTTP/OData for extraction) | Not supported on SAP S/4HANA Cloud Public Edition |

### Flat File

| Name | Clean Core Level | Public Cloud Ready | Modern Integration Standards | Notes |
|---|---|---|---|---|
| **Flat File** | **D** | No | Very Low — no API contract, governance, or observability | No migration path to SAP S/4HANA Cloud |

---

## Summary Reference Table (Quick Lookup)

| Level | Technologies |
|---|---|
| **A** (Target state) | Eventing via RAP (AMQP/MQTT), OData, OData via RAP Service Binding, CDS Views via Service Binding, Web Services via SOA Manager, HTTP(S), OData CDS Views, Delta Share, Data Replication Framework, Data Products |
| **B** (Acceptable with limitations) | Eventing via Event Enablement Add-On, IDoc via HTTPS, BAPI via RFC, BAPI via SOAP Wrapper, OData via SAP Gateway Service Builder, ABAP Proxy via SOA Manager, RFC (CPI-C), WebSocket RFC, BW Extractors |
| **C** (Limited alignment — candidates for modernization) | Business Events via AIF, IDoc via RFC, ABAP Proxy via XI, AMQP/MQTT/PCP, SLT |
| **D** (Non-compliant — should be avoided or replaced) | Flat File, SFTP, JDBC/ODBC |
| **Forbidden** | RFC (ODP) — prohibited by the API Policy |

---

## Changelog (Relevant Content Changes)

- **v4:** Initial Release; table included process integration categories
- **v5:** Categories added for data integration — Data Integration Interfaces/Technologies; Product/Component; Product/Add-On
- **v7:** Changelog added to the note
- **v8:** Current version (released 16.07.2026)

---

## Key Reference Links

- SAP Note 3690029: https://me.sap.com/notes/3690029
- SAP Note 3578329 (extensibility guidance): https://me.sap.com/notes/3578329
- SAP Business Accelerator Hub: https://hub.sap.com
- Cloudification Repository: https://sap.github.io/abap-atc-cr-cv-s4hc
- ABAP Integration and Connectivity Guide: https://help.sap.com/docs/abap-cloud/abap-integration-connectivity/abap-integration-and-connectivity
