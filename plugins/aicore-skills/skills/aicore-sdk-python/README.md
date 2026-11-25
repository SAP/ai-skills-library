# SAP GenAI Hub for Python Skill

Generate working Python boilerplate for SAP GenAI Hub using the `sap-ai-sdk-gen` package (import namespace `gen_ai_hub`).

## What This Skill Covers

- **Chat & streaming** via `gen_ai_hub.proxy.native.openai` (native OpenAI proxy, recommended entry point)
- **Multi-provider streaming** via `gen_ai_hub.proxy.native.openai`, `gen_ai_hub.proxy.native.google_genai`, and `gen_ai_hub.proxy.native.amazon` (OpenAI GPT, Google Gemini, Amazon Bedrock)
- **LangChain integration** via `gen_ai_hub.proxy.langchain`
- **Tool calling** via `gen_ai_hub.proxy.native.openai` (function-calling loop)
- **Native OpenAI Responses API** via `gen_ai_hub.proxy.native.openai.responses`
- **Structured output** via `gen_ai_hub.proxy.native.openai` + Pydantic schemas
- **Multi-turn stateful chat** via `gen_ai_hub.proxy.native.openai` with message history
- **Async & concurrent calls** via `gen_ai_hub.proxy.native.openai.AsyncOpenAI`
- **Text embeddings** via `gen_ai_hub.proxy.native.openai.embeddings`
- **Batch LLM jobs** via `gen_ai_hub.batch_service.BatchService`
- **Managed prompt templates** via `gen_ai_hub.prompt_registry.PromptTemplateClient`
- **RAG / document grounding** via `gen_ai_hub.document_grounding`
- **Tabular prediction** via `gen_ai_hub.proxy.native.sap.RPTClient`

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- [`sap-ai-sdk-gen`](https://pypi.org/project/sap-ai-sdk-gen/)
- SAP AI Core service key (`AICORE_SERVICE_KEY` environment variable)
