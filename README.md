[![REUSE status](https://api.reuse.software/badge/github.com/SAP/ai-skills-library)](https://api.reuse.software/info/github.com/SAP/ai-skills-library)

# AI Skills Library

## About this project

Discover AI skills for SAP — search, filter, and install skills for your digital assistant.

## Requirements and Setup

Install skills using the [skills CLI](https://github.com/vercel-labs/skills), which supports Claude Code, Codex, Cursor, OpenCode, and many more agents.

### Install all skills

```bash
npx skills add SAP/ai-skills-library
```

### Install a specific skill

```bash
npx skills add SAP/ai-skills-library --skill <skill-name>
```

### List available skills

```bash
npx skills add SAP/ai-skills-library --list
```

## Contribute a Skill

**Have a skill to share? Get it listed on [skills.cloud.sap](https://skills.cloud.sap).**

The AI Skills Library uses a **bring-your-own-repo** model — your skill code stays in your own public GitHub repository. You don't submit skill code here. Instead, open a registration issue and a maintainer onboards your repo.

### 1. Structure your repository

```
your-repo/
└── skills/
    └── <skill-slug>/
        └── SKILL.md      # must include "name" and "description" frontmatter
```

### 2. Register your skill

👉 **[Open a "Register a New Skill" issue](https://github.com/SAP/ai-skills-library/issues/new?template=new-skill.yml)**

See the [Contribution Guidelines](CONTRIBUTING.md) for the full details, the `SKILL.md` example, and other contribution paths (improvements, docs).

## Support & Feedback

This project is open to feature requests/suggestions, bug reports etc. via [GitHub issues](https://github.com/SAP/ai-skills-library/issues).

## Security / Disclosure
If you find any bug that may be a security problem, please follow our instructions at [in our security policy](https://github.com/SAP/ai-skills-library/security/policy) on how to report it. Please do not create GitHub issues for security-related doubts or problems.

## Code of Conduct

We as members, contributors, and leaders pledge to make participation in our community a harassment-free experience for everyone. By participating in this project, you agree to abide by its [Code of Conduct](https://github.com/SAP/.github/blob/main/CODE_OF_CONDUCT.md) at all times.

## Licensing

Copyright 2026 SAP SE or an SAP affiliate company and ai-skills-library contributors. Please see our [LICENSE](LICENSE) for copyright and license information. Detailed information including third-party components and their licensing/copyright information is available [via the REUSE tool](https://api.reuse.software/info/github.com/SAP/ai-skills-library).
