<!-- Source: Clean Core Extensibility Level Concept FAQ (SAP) -->

# Source: Clean Core Extensibility — Level Concept FAQ

---

## Sources

| Topic | Source | URL |
|-------|--------|-----|
| All content in this file | Clean Core Extensibility Level Concept FAQ (SAP) | Referenced from the Clean Core Extensibility Whitepaper and L300 Deck |
| Classification JSON file | SAP GitHub — ABAP ATC CR CV S4HC | https://github.com/SAP/abap-atc-cr-cv-s4hc |
| Framework/technology classification | SAP Note 3578329 | https://me.sap.com/notes/3578329 |
| ABAP Cloud language version fix | SAP Note 3593439 | https://me.sap.com/notes/3593439 |

---

## QA — Classification of SAP Objects

### QA1: What are the criteria for an object to be classified as "not recommended" / "noAPI"?

Two criteria:
1. SAP objects that involve **known risks** (e.g., data inconsistencies) if wrongly used by customers — but are still needed for SAP internal purposes.
2. **Orphaned or obsolete objects** still present in the SAP S/4HANA shipment that are no longer (or have never been) associated with officially supported functionality.

### QA2: Can I see why an object was classified as "not recommended"?

Currently **not visible** to customers. SAP is working on extending the [classification JSON file](https://github.com/SAP/abap-atc-cr-cv-s4hc) and the ATC check to display the reason.

### QA3: Does a "not recommended" object always have a successor?

**No.** A successor is not always provided. Cases where no successor exists:
- The object was never intended for customer use (SAP internal only)
- The functionality was removed before the first SAP S/4HANA shipment
- The functionality was sunsetted and replaced by architecturally different successor functionality (no 1:1 replacement possible)

If a successor exists, it is included in the [classification JSON file](https://github.com/SAP/abap-atc-cr-cv-s4hc) and displayed by the ATC check.

### QA4: Do C1/C2 release contracts apply to both local and remote usage?

**Yes.** The classification applies to both local and remote consumption where applicable. This particularly affects remote-enabled function modules (BAPIs) — the only legacy APIs that can be consumed both locally and remotely.

### QA5: Does the level concept apply to 3rd-party solutions on top of SAP S/4HANA?

SAP is looking into giving **partners** the ability to classify their own APIs. Partners and customers can already release their own APIs under a C-contract (C1/C2).

---

## QB — Change of Classification of SAP Objects

### QB1: Which classification changes are possible?

| From \ To | Released API | Classic API | Unclassified | Not recommended / noAPI |
|---|---|---|---|---|
| **Released API** | — | Possible but rare | No | Covered by deprecation process + mandatory successor |
| **Classic API** | Possible but rare | — | No | Planned to be covered by deprecation process* |
| **Unclassified** | No | Possible (standard process) | — | Possible. No deprecation process, no mandatory successor |
| **Not recommended / noAPI** | No | No | No | — |

*A deprecation process for classic APIs is not yet in place. SAP plans to establish this in the future.

### QB2: If an SAP object gets deleted, is it also classified as "noAPI"?

**No.** Object deletion is planned to be covered by the **changelog of SAP objects** mechanism, not by noAPI classification.

### QB3: Is it guaranteed that classic APIs never change incompatibly?

**No.** Classic API status means the object has not or rarely changed in the past and is unlikely to change in the near future — but it does **not** carry the same syntactic stability guarantee as APIs released under a C contract.

### QB4: If a classic API changes incompatibly, does it get re-classified as "not recommended"?

**No.** The classic API classification represents a **long-term view** on upgrade stability. A single, exceptional incompatible change does not affect that long-term classification.

### QB5: How can I request that an object be classified as classic API or released?

- **Feature requests** for developing, releasing, or classifying APIs: raise via the **customer influence channel** of the relevant SAP S/4HANA Cloud Private Edition application area.
- **Issues with released or classic APIs**: report as an incident on the support application component of the affected API.

---

## QC — Development Model

### QC1: How does the level concept map to ABAP language versions?

| ABAP Language Version | Level |
|---|---|
| ABAP Cloud for Developers (LV5) | **Level A** |
| ABAP Cloud for Key Users (LV2) | **Level A** |
| ABAP classic (any) | Level B, C, or D depending on references |

Note: Some objects generated when developing with ABAP Cloud for Key Users technically have classic language version but are still correctly detected as Level A — requires SAP Note 3593439.

### QC2: When should I still use wrapper patterns?

Wrapper patterns (adapters, proxies, decorators) remain **good practice in all cases** — ABAP classic or ABAP Cloud.

The specific wrapper used to expose classic/unreleased SAP APIs to ABAP Cloud custom developments is still required:
- The **wrapper itself** = Level B
- The **ABAP Cloud object consuming the wrapper** = Level A

For developments purely within Level B/C/D (no ABAP Cloud artifacts), this wrapper pattern is not required.

### QC3: Is an ABAP classic object that only references released APIs considered Level A?

**No.** The object must also have **ABAP language version LV5 or LV2** (ABAP Cloud for developers or key users). Compliance with ABAP Cloud restrictions alone is insufficient — language version is mandatory.

### QC4: Is a customer object that references no SAP objects at all considered Level A?

**Yes**, if it has ABAP language version LV5 (ABAP Cloud for developers) or LV2 (ABAP Cloud for key users).

---

## QD — Classification of Frameworks and Technologies

### QD2: Does ATC flag Level B/C/D framework usage?

**Only partially.** ATC can detect framework-level issues only when the usage is linked to a reference from custom code to SAP objects that the ATC check supports and can classify. Not all framework usage patterns are detectable.

### QD3: How does the level concept apply to frameworks vs. individual SAP objects?

For **individual SAP objects**: SAP classifies them (released / classic API / not recommended) and this directly determines the level of custom code referencing them.

For **frameworks and technologies**: usage is often not bound to specific SAP artifacts. Therefore, **levels are directly assigned to frameworks/technologies** rather than derived from object references. See SAP Note 3578329 for the full framework classification table.

### QD4: What does "conditional classification" of a framework mean?

A **conditionally classified** framework (per SAP Note 3578329) can be used in different ways or accessed via differently classified APIs. The level assignment depends on **how and via which APIs** the framework is used. Details are in SAP Note 3578329 per framework.

---

## QE — How to Measure

### QE1: How is clean core adherence per level concept measured in the RISE dashboard?

Level-based KPIs are **not yet included** in the RISE with SAP Methodology Dashboard (as of the FAQ publication). SAP plans to add them:
- **First step (planned Q4/2025)**: option to manually upload results of ATC checks "Usage of APIs" and "Allowed Enhancement Technologies" to SAP Cloud ALM, displaying extension classification by clean core level.

---

## QG — Relation to Other Concepts and Tools

### QG1: How does the level concept relate to Simplification Item Database (SID) ATC checks?

**Currently unrelated** — they serve different purposes. SAP is looking into combining them in the future.

### QG2: How does the level concept relate to the Blocklist Monitor?

**Currently unrelated** — different purposes, different use cases. SAP is looking into combining them.

### QG3: How does the level concept relate to object deprecation?

When a C1 released object is marked **deprecated**:
- It remains **fully available and supported**
- Deprecation signals a potential future decommissioning and that customers should plan migration to the successor
- The object does **not** get classified as "not recommended" — it retains its original classification during the deprecation phase

The same logic is planned for classic APIs, but deprecation information for classic APIs is not yet available.

### QG4: Does the level concept apply to other clean core dimensions (integration, data, processes)?

**No.** The level concept (A–D) is **specific to the clean core extensibility dimension only**. It does not currently apply to integration, data, processes, or operations.
