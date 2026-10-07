# SAP AI SDK for JavaScript/TypeScript Skill

Generate working TypeScript/JavaScript boilerplate for SAP GenAI Hub using the `@sap-ai-sdk` family of packages.

## What This Skill Covers

- **Chat & streaming** via `@sap-ai-sdk/orchestration` (recommended entry point)
- **Native OpenAI SDK surface** via `@sap-ai-sdk/openai` (no LiteLLM proxy needed)
- **LangChain integration** via `@sap-ai-sdk/langchain`
- **RAG / document grounding** via `@sap-ai-sdk/document-grounding`
- **Managed prompt templates** via `@sap-ai-sdk/prompt-registry`
- **Batch LLM jobs** via `@sap-ai-sdk/llm-batch`
- **Tabular prediction** via `@sap-ai-sdk/rpt` (SAP-RPT-1 model)
- **Context Registry** via `@sap-ai-sdk/context-registry` (data destinations, tabular artifacts, scenario configs)

## Installation

```bash
npx skills add SAP/ai-skills-library --skill aicore-sdk-js
```

## Requirements

- Node.js 22+ with native ESM support
- npm or bun
- SAP AI Core service key (`AICORE_SERVICE_KEY` environment variable)
