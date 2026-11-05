# Changelog

All notable changes to the Clean Core Assistant plugin are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).  
Version numbers follow [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.

- **MAJOR** — breaking changes to skill interfaces or fundamental restructuring
- **MINOR** — new knowledge content, new features, new skills
- **PATCH** — corrections, clarifications, small updates to existing knowledge

---


---


---

## [2.0.0] — 2026-09-14

Initial deep-skill release covering all five Clean Core principles.

### Skills

- **`clean-core-general`** — cross-principle entry point; RISE Dashboard full reference; L1/L2 decks; Governance & Maturity framework; KPI framework
- **`clean-core-extensibility`** — whitepaper, FAQ, SAP Note 3578329, L300 deck, G&M (EXT-GOV-01–EXT-SYS-05), KPIs, ATC setup, Project Kernseife, SAP API Policy, SAP Note 3761018 (Object Type Harmonization, August 2026)
- **`clean-core-integration`** — whitepaper, L3 deck, SAP Note 3690029, KPIs, G&M (INT-01–INT-06)
- **`clean-core-data`** — whitepaper, L3 deck, KPIs + RISE Dashboard data KPIs, G&M (DAT-01–DAT-05)
- **`clean-core-operations`** — whitepaper, L300 deck, KPIs + RISE Dashboard Operations View, G&M (OPS-01–OPS-08)
- **`clean-core-processes`** — whitepaper (SAP1178764), KPIs (4 KPIs, SAP1240359), G&M (PRO-01–PRO-05)
- **`clean-core-extensibility-atc-assessment`** — Python tool generating HTML dashboard from SAP ATC findings ZIP (Technical Debt Score, Level distribution, top objects/packages, upgrade recommendations)

### Infrastructure

- `publish.sh` — strips internal content (`knowledge/internal/`, INTERNAL marker blocks) and pushes to external GitHub; `--zip` flag builds EKX-distributable zip
- Knowledge gap issue flow — skills offer to log `knowledge-gap` GitHub issues when questions exceed the knowledge base
