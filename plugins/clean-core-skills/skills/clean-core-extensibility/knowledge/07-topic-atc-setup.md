# ATC Setup for Clean Core Governance

> Synthesized from SAP Community blog posts — see `sources/atc-blogs.md` for source registry and refresh instructions.
> Last sync: 2026-05-28

---

## Sources

When citing content from this file, link to the relevant source below:

| Topic | Source | URL |
|-------|--------|-----|
| Clean core ATC setup, check variant, "Usage of APIs" check, RISE dashboard upload | ATC Recommendations for Governance of Clean Core ABAP Development | https://community.sap.com/t5/technology-blog-posts-by-sap/abap-test-cockpit-atc-recommendations-for-governance-of-clean-core-abap/ba-p/14186130 |
| ATC on BTP: setup, features, CVA, developer scenario, exemptions, baseline, scheduling | Usage of ATC in the Cloud for On-Premise Developments | https://community.sap.com/t5/technology-blog-posts-by-sap/usage-of-abap-test-cockpit-atc-in-the-cloud-for-on-premise-developments/ba-p/13576887 |
| Creating a custom ATC check variant in ADT | How to Create and Use Your Own ATC Check Variant in ADT | https://community.sap.com/t5/technology-blog-posts-by-sap/how-to-create-and-use-your-own-atc-check-variant-in-abap-development-tools/ba-p/13512135 |
| Central ATC check system for multiple systems: overview and architecture | Remote Code Analysis in ATC – One Central Check System (Part 1) | https://community.sap.com/t5/technology-blog-posts-by-sap/remote-code-analysis-in-atc-one-central-check-system-for-multiple-systems/ba-p/13307811 |
| Central ATC technical setup: system role, RFC, object providers, run series | Remote Code Analysis in ATC – Technical Setup Step by Step (Part 2) | https://community.sap.com/t5/application-development-and-automation-blog-posts/remote-code-analysis-in-atc-technical-setup-step-by-step/ba-p/13308088 |
| Baseline to suppress legacy findings | Remote Code Analysis in ATC – Working with Baseline (Part 3) | https://community.sap.com/t5/application-development-and-automation-blog-posts/remote-code-analysis-in-atc-working-with-baseline-to-suppress-findings-in/ba-p/13308684 |
| Exemption workflow in BTP ATC (developer + quality expert), 4-eyes principle, email notifications | How to Work with Exemptions in ATC in the Cloud | https://community.sap.com/t5/technology-blog-posts-by-sap/how-to-work-with-exemptions-using-abap-test-cockpit-atc-in-the-cloud-during/ba-p/13574027 |
| Exemption workflow in remote/on-prem ATC (SAP GUI, ATC Exemption Browser) | Remote Code Analysis in ATC – Working with Exemptions | https://community.sap.com/t5/application-development-and-automation-blog-posts/remote-code-analysis-in-atc-working-with-exemptions/bc-p/13318055 |
| ATC general documentation | SAP Help Portal – ABAP Test Cockpit | https://help.sap.com/docs/ABAP_PLATFORM_NEW/ba879a6e2ea04d9bb740b409dos/4ec5711c6e391014adc9fffe4e204223.html |
| Custom code analysis app (Analyze Custom Code) | SAP Help Portal – Custom Code Analysis | https://help.sap.com/docs/btp/sap-business-technology-platform/custom-code-analysis |

---

## Overview

The ABAP Test Cockpit (ATC) is SAP's central quality assurance infrastructure for static code checks. In the context of Clean Core, ATC is the primary tool to enforce the clean core level concept: it identifies which custom code objects use released APIs (Level A), classic APIs (Level B), SAP internal objects (Level C), or modifications (Level D).

A properly configured central ATC system is the **essential prerequisite** for governing clean core compliance across a development landscape.

---

## Deployment Topologies

Choose the topology based on your system landscape:

### Option 1: ATC on SAP BTP (Recommended)

Use the **SAP BTP ABAP environment** as the central ATC check system for private cloud or on-premise S/4HANA development landscapes.

**Why it is the SAP recommended approach:**
- Provides the latest clean core checks (category "Clean Core") always up to date
- Includes SAP CVA (Code Vulnerability Analyzer) security checks at no additional licensing fee
- Full feature set: custom code analysis, scheduling, developer scenario, exemption workflow, baseline
- SAP takes over upgrades, maintenance, and operations
- Avoids the need to upgrade checked systems to get the latest checks

**Key app:** *Analyze Custom Code* app (formerly "Custom Code Migration app" — split into two tiles with BTP ABAP environment 2508)

### Option 2: Central ATC in S/4HANA On-Premise / Private Cloud

Use **SAP S/4HANA 2025** or **SAP S/4HANA 2023** as the central check system for multi-system on-premise landscapes.

- S/4HANA 2025 (FPS01+): includes the `ABAP_CLEAN_CORE_DEVELOPMENT` check variant natively
- S/4HANA 2023: apply SAP Note **3565942** to get the clean core checks
- One central system checks multiple development systems via remote RFC connections

**System sizing guidance (on-prem central system):** ~1 CPU and 4 GB RAM per 16,000 objects; ~400 KB per object on DB.

**Minimum release for checked systems:** SAP_BASIS 7.00 SP15 or higher (see SAP Note 2385520 for supported SP levels).

---

## Technical Setup

### ATC on SAP BTP — Setup Steps

**Recommended: CIAS guided workflow**

1. Subscribe to and activate **Cloud Integration Automation Service (CIAS)** on SAP BTP
2. Execute the CIAS guided workflow — it prepares the on-premise system, sets up BTP ABAP environment, and configures the RFC connection via SAP Cloud Connector

**Manual setup:**

1. Apply SAP Notes from **SAP Note 2364916** (collective note: recommended notes for ATC remote analysis) in your on-premise checked systems
2. Apply **SAP Note 2599695** (remote stubs for checked system) in on-premise systems
3. Set up SAP BTP ABAP environment using the Booster for automated setup
4. Enable the *Analyze Custom Code* app in BTP ABAP environment (SAP Help Portal: *Enable Usage of the Custom Code Migration App*)

**System landscape recommendation for BTP ATC:**

| System | Purpose | Sizing |
|--------|---------|--------|
| Development | ATC custom check implementations; can be hibernated | Min: 8 GB ABAP runtime, 16 GB HANA |
| Test | Pre-upgrade validation; mostly hibernated | 16 GB ABAP runtime, 32 GB HANA |
| Productive | Live ATC governance | 16 GB ABAP runtime, 32 GB HANA (extendable) |

Elastic scaling (activate via ticket on component `BC-DWB-CEX-CCM`) allows parallel ATC runs under high load.

**Blocking mode:** Set up ATC blocking mode in DEV systems for all **Priority 1 and Priority 2** findings for transport tasks and transport requests.

### Central ATC in On-Premise — Setup Steps

1. **Set system role:** Transaction `ATC` → ATC Administration → Setup → Set System Role → select *ATC Checks by Object Providers Only*
2. **Define RFC destinations:** Transaction `SM59` — create RFC destination for each checked system
3. **Maintain Object Providers:** In transaction ATC → ATC Administration → Setup → Maintain Object Providers
   - Create System Groups (one per SAP release or per organizational unit)
   - Add RFC Object Providers per system, assigned to the relevant System Group
   - Note: exemptions are valid per System Group
4. **Configure Run Series:** ATC Administration → Runs → Schedule Runs → Create
   - Define: description, check variant (must be RFC-enabled), object provider, object selection (packages)
5. **Schedule and execute runs:** Select the run series → Schedule → Execute (F8)
6. **View results:** ATC Result Browser in SE80, filter by system group and run series

**Important:** The central ATC check system can only analyze systems at the same or lower software release level.

**Before BTP ABAP environment upgrades:** Ensure all SAP Notes from SAP Note 2364916 are up-to-date in all checked systems. Verify RFC user authorizations (apply SAP Note 3548772 or check SAP Help documentation *Configuring the User*). Update accessible RFC function modules via the ZIP file in SAP Note 2861842 in SAP Cloud Connector.

---

## ATC Check Variant Setup for Clean Core

The check variant defines which checks run during ATC analysis. The right variant differs by system.

### BTP ABAP environment or S/4HANA 2025 FPS01+

SAP delivers the preconfigured **`ABAP_CLEAN_CORE_DEVELOPMENT`** check variant — use this directly or copy it as a basis for customization.

### S/4HANA 2023 or S/4HANA 2025 (before FPS01)

No dedicated clean core variant is shipped. Instead:
- Add the clean core checks to your existing global standard ATC check variant, **or**
- Create a new variant as a copy of **`ABAP_CLOUD_DEVELOPMENT_DEFAULT`** in ADT (Eclipse), then add the clean core checks

### Recommended Clean Core Checks

| Check | Category | Notes |
|-------|----------|-------|
| Allowed SAP Enhancement Technologies | Clean Core | Reports usage of non-allowed enhancement technology in ENHO objects |
| Usage of APIs | Clean Core | Core check — see details below |
| Search for Customer Modifications | Search Functions | Must be parametrized — see note below |
| Critical Statements | Security | Must be parametrized — see note below |
| Code Vulnerability Analyzer (CVA) | Security | Add if CVA is licensed; free on BTP |

**Parametrization notes:**

- **Search for Customer Modifications:** Apply SAP Note **3679781** to add the parameter *Only Business Modifications* — set this to filter out technical modifications (e.g., SD user exits) and focus only on business modifications relevant for clean core. Without this, the check also reports clean-core-compliant technical modifications.
- **Critical Statements:** Parametrize in check details with specific values (refer to blog source 1 / ABAP Extensibility Guide chapter 5 for the exact table of values).

### Creating a Custom ATC Check Variant in ADT

1. In Eclipse: *New → ABAP Repository Object → ATC → Check Variant*
2. Enter name and description → Finish
3. In the variant editor: select checks by checkbox, grouped by category
4. Configure parameters per check in the Parameters/Documentation panel at the bottom
5. Save and activate

**To copy an existing variant:** Open the SAP variant in *Open ABAP Development Object* (Ctrl+Shift+A), right-click → Duplicate → copy into your package.

Custom variants are also available in the *ATC Configurator* app (SAP Fiori) for assignment to ATC configurations.

---

## The "Usage of APIs" Check — Core Clean Core Check

This check is the primary instrument for enforcing the clean core level concept in classic ABAP development. It replaces the older "Usage of Released APIs" check.

### What it checks

Verifies how custom code uses SAP standard objects — classes, interfaces, function modules, CDS views, behavior definitions, DDIC tables and views. (Note: DDIC data elements, domains, table types, structures are excluded — no findings reported.)

### Check behavior by API classification

| Object type | Check result |
|-------------|-------------|
| Released SAP API | No finding (Level A compliant) |
| Classic SAP API | Info message (Level B) |
| Unclassified SAP internal object | Warning (Level C) |
| "No API" object (with successor listed) | Error with successor hint (Level D direction) |
| Reading DDIC database table or view | Warning |
| Writing DDIC database table or view | Error |

### Classic APIs

Classic APIs are SAP-recommended upgrade-stable APIs for classic ABAP development — not released cloud APIs, but stable reuse services and application frameworks (BAPIs, central reuse classes for SAP GUI programming, etc.).

The list is maintained as `objectClassifications_SAP.json` on GitHub: [SAP/abap-atc-cr-cv-s4hc](https://github.com/sap/abap-atc-cr-cv-s4hc). Browse via the [Cloudification Repository Viewer](https://sap.github.io/abap-atc-cr-cv-s4hc/?version=objectClassifications_SAP.json).

Object types covered: Function modules (FUNC), Classes/interfaces (CLAS/INTF), CDS views (STOB), BO interfaces (BDEF).

Classic APIs classified as *transactional-consistent* can be used in RAP-based applications.

### Check parameter: `classicAPIDataSource`

The check takes the JSON file as input. If the ABAP system has no internet access, upload the file using program `SYCM_API_CLASSIFICATION_MANAGR` and provide the filename as the `classicAPIDataSource` parameter value.

**Partner APIs:** Apply SAP Note **3630552** to enable the `partnerAPIDataSources` parameter and include partner-provided classic API JSON files.

### SAP Notes for clean core checks

| SAP Note | Purpose |
|----------|---------|
| 3565942 | Delivers new clean core ATC checks for S/4HANA 2023 |
| 3627152 | Updates and bug fixes for clean core checks — includes Note Analyzer files to verify system is current |
| 3578329 | SAP recommendations for classic ABAP development technologies and reuse services |
| 3630552 | Classic API support for SAP partners |
| 3679781 | Adds "Only Business Modifications" parameter to the Search for Customer Modifications check |

### Key difference vs. ABAP Cloud readiness checks

The clean core checks (Usage of APIs) produce significantly fewer findings than the older ABAP Cloud readiness checks (Usage of Released APIs) for classic ABAP developments — because cloud compliance (ABAP Cloud language version) is not required for classic developments. This focuses analysis on actual technical debt rather than architectural mismatches.

---

## Checking ECC or S/4HANA < 2023 Systems for Clean Core Readiness

Clean core checks are not available natively in ECC or S/4HANA below version 2023. Use ATC on BTP to check these systems remotely:

1. Create a new ATC check variant in BTP ABAP environment in ADT
2. Add all checks from the **Clean Core** category to the variant
3. For the *Usage of APIs* check: set the `releasedAPIDataSource` parameter to the latest released SAP APIs for S/4HANA Cloud Private Edition (use Ctrl+Space for code completion)
4. Parametrize the *Critical Statements* check as described above
5. Execute a remote ATC run via the *Analyze Custom Code* app against the ECC / S/4HANA < 2023 system

A preconfigured **`ABAP_CLEAN_CORE_READINESS`** variant for this purpose is planned for BTP ABAP environment 2605.

---

## Developer Scenario

Developers in on-premise systems can use ATC checks from the central BTP check system **during development** (not just in scheduled batch runs):

- Configured via SAP Help Portal: *Configuring the ATC Developer Scenario*
- Developer runs ATC in ADT (context menu → Run As → ABAP Test Cockpit) and sees findings from the central check system in real time
- Developers can request exemptions directly from ADT findings

---

## Exemption Workflow

An exemption suppresses a specific ATC finding from future results. Use exemptions for:
- False-positive results
- Findings that are accepted from a quality perspective (with documented justification)
- Legacy code where fixing is not ROI-justified (consider baseline instead)

### Exemptions in BTP ABAP ATC (on-prem developer → BTP central system)

**Available from:** BTP ABAP environment 2311 (November 2023)

**Roles:**
- **Developer** (on-premise ADT): requests exemptions per finding, provides justification and approver
- **Quality Expert** (BTP Fiori Launchpad): processes exemptions via the *Approve ATC Exemptions* app
  - Required business role template: `SAP_BR_QUALITY_MNGR_SW_DEV`

**Workflow:**

1. Developer runs ATC in ADT → sees findings
2. Transport release is blocked for P1/P2 findings
3. Developer right-clicks finding → *Request Exemption* → selects scope, enters approver and justification
4. Quality expert opens *Approve ATC Exemptions* app → reviews pending exemptions → Approve or Reject
5. If rejected: developer must fix before transport can be released
6. If approved: finding is suppressed in next ATC run

**Email notifications (from BTP ABAP environment 2511):** Quality experts can subscribe to email notifications for new exemption requests in the *Approve ATC Exemptions* app. Requires outbound email service to be configured.

**4-eyes principle (from BTP ABAP environment 2602):** ATC prevents the requester of an exemption from approving their own exemption, using Global User ID matching. Requires SAP Note **3003462** (Global User ID in on-premise systems) and SAP Note **3605916** (4-eyes principle for exemptions).

**Transferring exemptions from on-premise ATC system:** Use transaction `SATC_EXPORT_XMPT` to export existing exemptions as JSON, then import via the *Import* button in the *Approve ATC Exemptions* app. Apply SAP Note **3480722** for lower releases.

**Limitations:** Exemptions can only be created via ADT (not SAP GUI) when using BTP as central check system.

### Exemptions in Remote ATC (on-prem central check system)

**Prerequisite:** Enable exemptions in the central check system via transaction ATC → Setup → Configure ATC.

**Roles:**
- **Developer** (local development system, ADT): requests exemption via context menu on ATC finding
- **Quality Expert** (central ATC system, SAP GUI): processes via *ATC Exemption Browser* (ATC Administration → Exemption Browser in transaction ATC)

**Workflow:**

1. Developer positions cursor on ATC finding → context menu → *Request Exemption*
2. Step 1 dialog: review finding, select scope → Next
3. Step 2 dialog: enter approver, reason, justification; choose notification preference
4. Quality expert logs on to central ATC system → ATC Exemption Browser → double-click exemption
5. Quality expert reviews details, toggles Edit mode → Approve or Deny
6. Developer re-runs ATC: approved findings are marked as exempted and hidden by default
7. Use *View Menu → Include Exempted Findings* to display exempted findings when needed

**Exemption scope:** Can be per object or per single finding. Single-finding exemptions stay valid as long as the relevant code context is not changed.

---

## Baseline — Suppressing Legacy Findings

Baseline is an alternative to exemptions for bulk-suppressing known or legacy findings, allowing teams to focus quality assurance on new or changed code only.

**When to use:** Large legacy code base where fixing all historical findings is not ROI-justified. Create a baseline after the first full ATC run, then only new findings from that point forward appear in results.

**Setup (on-prem central system):**
1. Log on to ATC system as administrator
2. Transaction ATC → ATC Administration → Runs → Manage Results
3. Run query, select findings → Baseline → Add to Baseline → choose option (suppress / exempt / assign low priority)
4. Schedule subsequent ATC run — baseline findings no longer appear
5. Suppressed findings can still be displayed optionally

**Key behavior:** A baseline entry stays valid as long as the finding's code context is unchanged (e.g., changing line 20 of an INCLUDE doesn't invalidate a finding at line 200).

**BTP ATC:** Baseline is also supported — see blog *ABAP Test Cockpit in the Cloud – How to use baseline*.

---

## RISE with SAP Methodology Integration

ATC clean core check results can be uploaded to the **RISE with SAP Methodology dashboard**, directly linking ATC findings to the KPI tracking for clean core compliance. The dashboard provides:
- Clean core share (Level A/B/C/D distribution)
- Technical debt score (based on ATC Priority 1/2/3 findings)
- Customer Objects deep dive for detailed clean core compliance analysis

See `knowledge/04-kpi-extensibility.md` and `knowledge/02-l300-extensibility-deck.md` for KPI definitions and dashboard roadmap.

---

## Key SAP Notes Reference

| SAP Note | Topic |
|----------|-------|
| 2364916 | Collective note: recommended SAP Notes for ATC remote analysis (checked systems) |
| 2385520 | Supported SP levels for checked systems |
| 2599695 | Remote stubs for checked system (BTP setup) |
| 2672703 | Authorization roles for remote check scenarios |
| 2861842 | Updated RFC function modules list for SAP Cloud Connector access control |
| 3003462 | Global User ID in ABAP on-premise systems (for 4-eyes principle) |
| 3480722 | Export exemptions from on-premise ATC (SATC_EXPORT_XMPT) for lower releases |
| 3548772 | All relevant authorizations for technical RFC user in checked systems |
| 3565942 | Clean core ATC checks for S/4HANA 2023 |
| 3578329 | SAP recommendations for classic ABAP development technologies and reuse services |
| 3605916 | 4-eyes principle for ATC exemption release |
| 3627152 | Updates/bug fixes for clean core checks + Note Analyzer files |
| 3630552 | Classic API support for SAP partners |
| 3679781 | "Only Business Modifications" parameter for Search for Customer Modifications check |
