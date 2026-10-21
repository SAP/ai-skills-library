---
name: genai-hub-orchestration
description: >
  Configure and use the SAP AI Core Orchestration service: build prompt templates, add content
  filtering and data masking, set up document grounding (RAG) pipelines, and call models via
  the Harmonized API.
  WHEN: user asks about the orchestration service, Harmonized API, prompt
  templating with variables, content filtering, data masking, grounding, RAG pipeline, document
  grounding, or building a pipeline that wraps an LLM.
  DO NOT USE FOR: creating an orchestration deployment — use `aicore-lifecycle-management` for that;
  credential setup — use `aicore-admin-resources`; browsing or deploying foundation models
  directly without a pipeline — use `genai-hub-foundation-models`; direct LLM inference without a pipeline — use `aicore-sdk-java` or `aicore-sdk-js`
compatibility: Requires Python 3.11+, uv, and sap-ai-sdk-gen.
allowed-tools: Bash, Read
---

## Rules

1. Orchestration always requires a **running orchestration deployment** as a prerequisite — invoke `aicore-lifecycle-management` first if one does not exist.
2. The orchestration endpoint is `POST {DEPLOYMENT_URL}/v2/completion` — not `/v1/chat/completions`.
3. Orchestration `scenario_id` and `executable_id` are always `"orchestration"` — these are fixed.
4. The Harmonized API normalizes all models to OpenAI message format — the same client code works for GPT, Gemini, and Bedrock.
5. If credentials are not configured, invoke `aicore-admin-resources` first.
6. `generative-ai-hub-sdk` is deprecated — always use `sap-ai-sdk-gen`. Import namespace `gen_ai_hub` is shared by both.
7. **If the user's request does not explicitly specify an approach, use `AskUserQuestion` to ask whether they prefer the REST API (curl) or the Python SDK before writing or running any code.**

---

## Deployment Prerequisite

Before using the orchestration service, a deployment must be running:

```bash
# Check for an existing orchestration deployment:
uv run skills/aicore-lifecycle-management/scripts/get_deployments.py --scenario orchestration

# If none exists, create a configuration first (reuse if "orchestration" config already exists):
uv run skills/aicore-lifecycle-management/scripts/get_configurations.py --scenario-id orchestration --json | jq '.[] | select(.name == "orchestration")'
uv run skills/aicore-lifecycle-management/scripts/create_configuration.py \
  --name orchestration \
  --scenario-id orchestration \
  --executable-id orchestration

# Then deploy (takes up to 10 minutes):
uv run skills/aicore-lifecycle-management/scripts/create_deployment.py --configuration-id <config-id> --wait --timeout 600
```

---

## Workflow

| Step | Action                                                                              | Key Gate                                      |
| ---- | ----------------------------------------------------------------------------------- | --------------------------------------------- |
| 1    | Verify orchestration deployment is RUNNING                                          | `get_deployments.py --scenario orchestration` |
| 2    | **If approach not stated: ask curl (REST API) or Python SDK** via `AskUserQuestion` | User preference                               |
| 3    | Choose pipeline features (templating only / + filtering / + grounding)              | User intent                                   |
| 4    | Select template from `assets/` or build from scratch                                | See asset map below                           |
| 5    | Run and verify output                                                               | `uv run assets/<template>.py`                 |

---

## Asset Map

| Use case                                     | Template                            |
| -------------------------------------------- | ----------------------------------- |
| Basic chat via orchestration pipeline        | `assets/orchestration_basic.py`     |
| Chat with content filtering (input + output) | `assets/orchestration_filtering.py` |
| RAG with document grounding                  | `assets/rag_grounding.py`           |

---

## Python SDK — Key Patterns

### Basic pipeline

```python
from gen_ai_hub.orchestration.service import OrchestrationService
from gen_ai_hub.orchestration.models.config import OrchestrationConfig
from gen_ai_hub.orchestration.models.llm import LLM
from gen_ai_hub.orchestration.models.template import Template, TemplateValue
from gen_ai_hub.orchestration.models.message import SystemMessage, UserMessage

config = OrchestrationConfig(
    template=Template(messages=[
        SystemMessage("You are a helpful assistant."),
        UserMessage("{{?user_query}}"),
    ]),
    llm=LLM(name="gpt-4o-mini", version="latest"),
)
svc = OrchestrationService(config=config)
result = svc.run(template_values=[TemplateValue("user_query", "Hello")])
print(result.orchestration_result.choices[0].message.content)
```

### Add content filtering

```python
from gen_ai_hub.orchestration.models.content_filtering import (
    ContentFiltering,
    InputFiltering,
    OutputFiltering,
)
from gen_ai_hub.orchestration.models.azure_content_filter import AzureContentFilter

filtering = ContentFiltering(
    input_filtering=InputFiltering(filters=[AzureContentFilter(hate=2, violence=2, sexual=2, self_harm=2)]),
    output_filtering=OutputFiltering(filters=[AzureContentFilter(hate=2, violence=2, sexual=2, self_harm=2)]),
)
config = OrchestrationConfig(template=..., llm=..., filtering=filtering)
```

### Add data masking

```python
from gen_ai_hub.orchestration.models.data_masking import DataMasking
```

---

## REST API (curl)

```bash
export TOKEN=$(uv run skills/aicore-admin-resources/scripts/get_token.py)
export DEPLOYMENT_URL=$(uv run skills/aicore-lifecycle-management/scripts/get_deployments.py \
  --scenario orchestration --json 2>/dev/null | jq -r '.[0].deployment_url')
export RESOURCE_GROUP=$(uv run skills/aicore-admin-resources/scripts/check_setup.py 2>/dev/null | jq -r '.resource_group')

curl --request POST "${DEPLOYMENT_URL}/v2/completion" \
  --header "Authorization: Bearer ${TOKEN}" \
  --header "AI-Resource-Group: ${RESOURCE_GROUP}" \
  --header "content-type: application/json" \
  --data-raw '{
    "config": {
      "modules": {
        "prompt_templating": {
          "prompt": {
            "template": [
              {"role": "system", "content": "You are a helpful assistant."},
              {"role": "user",   "content": "{{?user_query}}"}
            ]
          },
          "model": {
            "name": "gpt-4o-mini",
            "params": {"max_completion_tokens": 512}
          }
        }
      }
    },
    "placeholder_values": {"user_query": "What is SAP AI Core?"},
    "messages_history": []
  }'
```

Extract the answer with: `jq '.final_result.choices[0].message.content'`

> **Reasoning models** (Gemini 2.5 Pro, o3): set `max_completion_tokens` to at least **1024** — reasoning tokens consume the budget before the visible response.

---

## Handoffs

- **No orchestration deployment running?** → invoke `aicore-lifecycle-management`
- **Credential/auth error?** → invoke `aicore-admin-resources`
- **Need to find a model name?** → invoke `genai-hub-foundation-models`
- **Want full Java SDK boilerplate (non-orchestration)?** → invoke `aicore-sdk-java`
- **Want full JS SDK boilerplate (non-orchestration)?** → invoke `aicore-sdk-js`

---

## When to Load Reference Files

| Trigger                                                  | Load                          |
| -------------------------------------------------------- | ----------------------------- |
| REST API details, request/response shape, Harmonized API | `references/ORCHESTRATION.md` |
| Document grounding setup, GroundingModule config, RAG    | `references/GROUNDING.md`     |
