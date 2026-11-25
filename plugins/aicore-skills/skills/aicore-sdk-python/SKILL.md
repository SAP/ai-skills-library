---
name: aicore-sdk-python
description: >
  Generate working Python boilerplate for SAP GenAI Hub using sap-ai-sdk-gen: native OpenAI
  proxy, Google GenAI, Amazon Bedrock, LangChain (init_llm/ ChatOpenAI /
  ChatBedrock / ChatGoogleGenerativeAI), tool calling, structured output, async,
  multi-turn, embeddings, batch jobs, prompt registry, document grounding / RAG, tabular prediction (SAP RPT
  classification & regression).
  WHEN: user asks for Python code, a Python starter project, how to use GenAI Hub in Python,
  how to connect LangChain to AI Core, how to use OpenAI (GPT), Google Gemini, or Amazon Bedrock models via SAP AI Core,
  how to run batch LLM jobs on SAP AI Core (BatchService),
  how to manage prompt templates or orchestration configs on SAP AI Core (Prompt Registry / OrchestrationService),
  how to generate embeddings or do RAG / document grounding through SAP AI Core,
  how to use the Responses API via the GenAI Hub proxy,
  how to do tabular prediction with SAP RPT models on SAP AI Core (classification & regression) via RPTClient.
  DO NOT USE FOR: TypeScript or JavaScript code — use `aicore-sdk-js`; managing deployments
  — use `aicore-lifecycle-management`; credential setup — use `aicore-admin-resources`.
compatibility: Requires Python 3.11+, uv, and sap-ai-sdk-gen.
---

## Rules

1. Always use `sap-ai-sdk-gen` — never `generative-ai-hub-sdk` (deprecated). Import namespace `gen_ai_hub` is the same for both.
2. If no deployment URL is known, invoke `aicore-lifecycle-management` to list or create one before generating code.
3. Always include `aicore configure` credential guidance in generated code comments.
4. **Never emit TypeScript, JavaScript or Java code snippets** — this skill is Python only. If the user asks for TypeScript, JavaScript, or Node.js code, invoke `aicore-sdk-js` immediately without producing any JS/TS code. If the user asks for Java code, invoke `aicore-sdk-java` immediately. Do not relay or present any output from that skill — simply hand off and stop.
5. Gather these details before generating code via `AskUserQuestion` — ask only for what the user hasn't provided:
   - **Language**: Python (confirmed for this skill)
   - **Use case**: chat / streaming / tool calling / structured output / agentic framework / async / batch / prompt registry/ document grounding/ orchestration?
   - **Model**: which model? (suggest gpt-4o-mini as default)
   - **Deployment ID**: run `aicore-lifecycle-management` scripts to list existing ones, or offer to create

---

## Sources & Fallback

Use the best source available, in this order. Never block on a source that isn't present.

1. **Baked-in reference (always available).** `references/SDK_PYTHON.md` and `assets/*.py` are the verified floor. They are correct for all common paths and require no network. Use them by default.
2. **Web docs (fallback for gaps).** For features not covered by the baked-in reference (e.g. new models, orchestration v2 internals), fetch the online docs:
   - SDK reference: https://sap.github.io/ai-sdk/docs/python/overview
   - Examples: https://sap.github.io/ai-sdk/docs/python/examples/gen-ai-hub

Do not fabricate API shapes from memory — `sap-ai-sdk-gen` has changed across versions. When unsure, check the reference files before guessing.

---

## Asset Map

Pick the template that matches the user's use case:

| Use case                               | Template                       | Install                                     |
| -------------------------------------- | ------------------------------ | ------------------------------------------- |
| Simple chat + streaming (native proxy) | `assets/chat_native_openai.py` | `uv add sap-ai-sdk-gen`                     |
| Multi-provider streaming               | `assets/streaming.py`          | `uv add "sap-ai-sdk-gen[all]"`              |
| Chat + streaming via LangChain         | `assets/chat_langchain.py`     | `uv add "sap-ai-sdk-gen[all]"`              |
| Tool calling (function calling loop)   | `assets/tool_calling.py`       | `uv add sap-ai-sdk-gen`                     |
| Responses API (gpt-5, streaming)       | `assets/responses_api.py`      | `uv add "sap-ai-sdk-gen>=6.9.0"`            |
| Structured output (Pydantic)           | `assets/structured_output.py`  | `uv add "sap-ai-sdk-gen>=6.9.0" pydantic`   |
| Multi-turn stateful chat               | `assets/multi_turn.py`         | `uv add sap-ai-sdk-gen`                     |
| Async + concurrent calls               | `assets/async_chat.py`         | `uv add sap-ai-sdk-gen`                     |
| Embeddings (text vectors)              | `assets/embeddings.py`         | `uv add "sap-ai-sdk-gen[amazon]"`           |
| Batch LLM jobs                         | `assets/batch_service.py`      | `uv add sap-ai-sdk-gen`                     |
| Managed prompt templates               | `assets/prompt_registry.py`    | `uv add sap-ai-sdk-gen`                     |
| Document grounding / RAG               | `assets/document_grounding.py` | `uv add sap-ai-sdk-gen`                     |
| Relational / tabular prediction        | `assets/rpt.py`                | `uv add sap-ai-sdk-gen`                     |

For Google GenAI or Amazon Bedrock native clients, read `references/SDK_PYTHON.md` (Google GenAI / Amazon Bedrock sections) and use inline code generation — no dedicated asset file.

---

## Install

**`sap-ai-sdk-gen` install extras** (optional extras bundled with the SDK):

| Extra                         | Install command                              |
| ----------------------------- | -------------------------------------------- |
| Default / native OpenAI proxy | `uv add sap-ai-sdk-gen`                      |
| Google Gemini (native + LC)   | `uv add "sap-ai-sdk-gen[google]"`            |
| Amazon Bedrock (native + LC)  | `uv add "sap-ai-sdk-gen[amazon]"`            |
| All providers                 | `uv add "sap-ai-sdk-gen[all]"`               |

---

## Quick Start (native OpenAI proxy)

```python
# uv add sap-ai-sdk-gen
# Credentials: run 'aicore configure' or set AICORE_* env vars

from gen_ai_hub.proxy.native.openai import chat

response = chat.completions.create(
    model_name="gpt-4o-mini",
    messages=[{"role": "user", "content": "What is SAP AI Core?"}],
)
print(response.choices[0].message.content)
```
---

## Handoffs

- **No deployment yet?** → invoke `aicore-lifecycle-management`
- **Credential/auth error?** → invoke `aicore-admin-resources` (see also: [Connecting to AI Core](https://help.sap.com/docs/sap-ai-core/generative-ai/initial-setup))
- **Need to find a model name or executable-id?** → invoke `genai-hub-foundation-models`
- **Want TypeScript/JavaScript code instead?** → invoke `aicore-sdk-js`
- **Want Java code instead?** → invoke `aicore-sdk-java`

---

## When to Load Reference Files

| Trigger                                                               | Load                       |
| --------------------------------------------------------------------- | -------------------------- |
| Python SDK imports, gen_ai_hub API, OrchestrationService              | `references/SDK_PYTHON.md` |
| Batch jobs, prompt registry, document grounding, embeddings           | `references/SDK_PYTHON.md` |
| Google GenAI native client, Amazon Bedrock native client              | `references/SDK_PYTHON.md` |
| LangChain init_llm, ChatBedrock, ChatGoogleGenerativeAI               | `references/SDK_PYTHON.md` |
| Async/concurrent calls, OrchestrationConfig fallback                  | `references/SDK_PYTHON.md` |
| OrchestrationConfigClient, prompt registry config templates           | `references/SDK_PYTHON.md` |
| Tool calling, function calling loop                                   | `references/SDK_PYTHON.md` |
| Structured output, Pydantic schema, responses API                     | `references/SDK_PYTHON.md` |
| Streaming (native OpenAI, Google GenAI, Amazon Bedrock, LangChain)    | `references/SDK_PYTHON.md` |
| Relational / tabular prediction, RPTClient                            | `references/SDK_PYTHON.md` |
| Multi-turn chat, conversation history                                 | `references/SDK_PYTHON.md` |
