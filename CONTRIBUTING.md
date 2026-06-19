# Contributing

## Code of Conduct

All members of the project community must abide by the [SAP Open Source Code of Conduct](https://github.com/SAP/.github/blob/main/CODE_OF_CONDUCT.md).
Only by respecting each other we can develop a productive, collaborative community.
Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting [a project maintainer](REUSE.toml).

## How to Contribute

### Documentation Fixes

Found a typo or want to improve documentation? Fork the repository and open a PR directly — no prior issue needed.

### Improving an Existing Skill

To avoid duplicate efforts and make sure your contribution is a good fit, please **open an issue first** to describe the improvement. A maintainer will review it and give a go-ahead via assignment and a comment. Once approved, fork the repository and open a pull request.

* [Propose an improvement to an existing skill](https://github.com/SAP/ai-skills-library/issues/new?template=improve-skill.yml)

### Registering a New Skill

The AI Skills Library uses a **bring-your-own-repo** model. Your skill code lives in your own public GitHub repository — you do not submit skill code to this repository. Instead, you open an issue to request onboarding, and a maintainer adds your repo to the Skill Hub so it appears on [skills.cloud.sap](https://skills.cloud.sap).

#### 1. Structure your repository

Your repository must follow this layout for the Skill Hub to discover your skills:

```
your-repo/
├── package.json          # must include an "author" field
└── skills/
    └── <skill-slug>/
        └── SKILL.md      # must include "name" and "description" frontmatter
```

Example `SKILL.md`:

```markdown
---
name: My Skill
description: Does X when the user asks about Y. Use this skill whenever...
---

# My Skill

...skill content...
```

The `description` field is what appears on the Skill Hub listing and drives AI trigger matching — make it specific and trigger-rich.

#### 2. Open a registration issue

Once your repository is ready and public on github.com, open a [Register a New Skill](https://github.com/SAP/ai-skills-library/issues/new?template=new-skill.yml) issue. A maintainer will review your submission and onboard your repo to the Skill Hub.

## Governing Rules

The following rules apply to all contributions:

* Contributions must be licensed under the [Apache 2.0 License](./LICENSE).
* Due to legal reasons, contributors will be asked to accept a Developer Certificate of Origin (DCO) when they create the first pull request to this project. This happens in an automated fashion during the submission process. SAP uses [the standard DCO text of the Linux Foundation](https://developercertificate.org/).
* Contributions must follow our [guidelines on AI-generated code](https://github.com/SAP/.github/blob/main/CONTRIBUTING_USING_GENAI.md) in case you are using such tools.
