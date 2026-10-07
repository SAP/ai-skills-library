# SAP AI SDK for Java Skill

Generate working Java boilerplate for SAP GenAI Hub using the `com.sap.ai.sdk` family of packages.

## What This Skill Covers

- **Chat & streaming** via `com.sap.ai.sdk:orchestration`
- **Multi-turn conversations** with message history
- **Text embeddings** via OrchestrationClient
- **RAG / vector store grounding** via orchestration grounding module
- **Managed prompt templates** via `@sap-ai-sdk/prompt-registry`
- **Content filtering** (Azure Content Filter + LlamaGuard)
- **Data masking** via DPI anonymization
- **Spring AI integration** (chat + OpenAI client)
- **Batch LLM jobs** via `com.sap.ai.sdk:batch`
- **Native OpenAI Responses API** via `com.sap.ai.sdk:openai`
- **Tabular prediction** via `com.sap.ai.sdk:sap-rpt` (SAP-RPT-1 model)

## Installation

```bash
npx skills add SAP/ai-skills-library --skill aicore-sdk-java
```

## Requirements

- Java 17+
- Maven or Gradle
- SAP AI Core service key (`AICORE_SERVICE_KEY` environment variable)
