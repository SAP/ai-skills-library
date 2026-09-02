# aicore-skills

A growing library of agent skills for the SAP AI Core.

## Skills

- **aicore-admin-resources** — manage AI Core admin resources
- **aicore-lifecycle-management** — manage the full AI Core deployment lifecycle
- **genai-hub-foundation-models** — discover, deploy, and call foundation models

## Requirements

- [SAP AI Core](https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/initial-setup) instance with credentials configured
- [Node.js](https://nodejs.org)
- Python 3.9+, [uv](https://docs.astral.sh/uv/)
- [sap-ai-sdk-core](https://pypi.org/project/sap-ai-sdk-core/)

## Installation

```bash
npx skills add SAP/ai-skills-library --plugin aicore-skills
```

Supported harnesses: Claude Code, Codex, Cursor, Gemini CLI, and any agent that supports the [agentskills.io](https://agentskills.io) specification.

Once installed, just describe what you need:

- `aicore-admin-resources`: "Check if my AI Core setup is working"
- `aicore-lifecycle-management`: "List all running deployments"
- `genai-hub-foundation-models`: "What models are available from Anthropic?"
- `genai-hub-foundation-models`: "Create a gpt-4o-mini deployment and wait for it to be running"
- `genai-hub-foundation-models`: "Generate a curl example using the OpenAI Responses API via GenAI Hub"
