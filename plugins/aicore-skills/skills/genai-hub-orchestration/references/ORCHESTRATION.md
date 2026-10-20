# Orchestration Reference

SAP AI Core Orchestration is a pipeline service that sits in front of LLM deployments. It adds prompt templating, content filtering, data masking, and grounding — all configured in a single JSON request body. Clients always talk to the **orchestration deployment**, never directly to the LLM deployment.

---

## Orchestration Deployment

The orchestration service uses a fixed executable (`scenario_id` and `executable_id` are both `orchestration`) — no model selection needed. Create a deployment with the `aicore-lifecycle-management` skill:

```bash
# Reuse or create the "orchestration" configuration, then deploy it:
uv run skills/aicore-lifecycle-management/scripts/create_configuration.py \
  --name orchestration --scenario-id orchestration --executable-id orchestration
uv run skills/aicore-lifecycle-management/scripts/create_deployment.py \
  --configuration-id <config-id> --wait --timeout 600
```

## Harmonized API

The Harmonized API normalises all model interactions to the **OpenAI message format**. When you use a non-OpenAI model (e.g. Gemini, Bedrock), the orchestration service translates the request to the model's native format and translates the response back. Your client code stays the same regardless of the underlying model.

### Message format (input)

```json
[
  { "role": "system", "content": "You are a helpful assistant." },
  { "role": "user", "content": "Hello" },
  { "role": "assistant", "content": "Hi" }
]
```

### Response format (output)

The v2 response wraps results in `intermediate_results` (per-module output) and `final_result` (the final answer). Extract the response from `final_result.choices[0].message.content`:

```json
{
  "request_id": "...",
  "intermediate_results": {
    "templating": [
      { "role": "system", "content": "You are a helpful assistant." },
      { "role": "user", "content": "What is SAP BTP?" }
    ],
    "llm": { "choices": [...], "usage": {...} }
  },
  "final_result": {
    "object": "chat.completion",
    "model": "gpt-4o-mini",
    "choices": [
      {
        "index": 0,
        "message": { "role": "assistant", "content": "SAP BTP is ..." },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "completion_tokens": 10,
      "prompt_tokens": 1,
      "total_tokens": 11
    }
  }
}
```

The `final_result` is always in OpenAI chat completion format, even when the underlying model (e.g. Gemini) uses a different native format — the orchestration layer converts it transparently.

---

## Orchestration v2 — REST API

### Endpoint

```
POST {DEPLOYMENT_URL}/v2/completion
```

`DEPLOYMENT_URL` is the full inference URL returned by `get_deployments.py` (already includes the deployment ID). Retrieve it with:

```bash
export DEPLOYMENT_URL=$(uv run skills/aicore-lifecycle-management/scripts/get_deployments.py \
  --scenario orchestration --json 2>/dev/null | jq -r '.[0].deployment_url')
# e.g. https://<host>/v2/inference/deployments/<id>
# → full call URL: https://<host>/v2/inference/deployments/<id>/v2/completion
```

### Required headers

```
Authorization: Bearer <token>
AI-Resource-Group: <resource-group>
Content-Type: application/json
```

### Minimal request body

```json
{
  "config": {
    "modules": {
      "prompt_templating": {
        "prompt": {
          "template": [
            { "role": "system", "content": "You are a helpful assistant." },
            { "role": "user", "content": "{{?user_query}}" }
          ]
        },
        "model": {
          "name": "gpt-4o-mini",
          "params": {
            "max_completion_tokens": 512,
            "temperature": 0.3
          }
        }
      }
    }
  },
  "placeholder_values": {
    "user_query": "What is SAP BTP?"
  },
  "messages_history": []
}
```

### Multi-turn request (messages_history)

Pass prior turns in `messages_history` to continue a conversation:

```json
{
  "config": {
    "modules": {
      "prompt_templating": {
        "prompt": {
          "template": [{ "role": "user", "content": "{{?user_query}}" }]
        },
        "model": {
          "name": "gpt-4o-mini",
          "params": { "max_completion_tokens": 512 }
        }
      }
    }
  },
  "placeholder_values": { "user_query": "And now in French." },
  "messages_history": [
    { "role": "user", "content": "Summarize SAP AI Core in one sentence." },
    {
      "role": "assistant",
      "content": "SAP AI Core is a cloud service for running AI models at scale."
    }
  ]
}
```

### curl example

```bash
export TOKEN=$(uv run skills/aicore-admin-resources/scripts/get_token.py)
export DEPLOYMENT_URL="<your-orchestration-deployment-url>"
export RESOURCE_GROUP="default"

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
              { "role": "system", "content": "You are a helpful assistant." },
              { "role": "user",   "content": "{{?user_query}}" }
            ]
          },
          "model": {
            "name": "gpt-4o-mini",
            "params": { "max_completion_tokens": 256, "temperature": 0.3 }
          }
        }
      }
    },
    "placeholder_values": { "user_query": "What is SAP AI Core?" },
    "messages_history": []
  }'
```

### Reasoning models (gpt-5, Gemini 2.5 Pro, o3, etc.)

Reasoning models consume tokens on internal thinking before the visible response. If `max_completion_tokens` is set too low, the model returns **empty content** — all tokens are spent on reasoning before any visible output is produced. Set `max_completion_tokens` to at least **1024** (2048+ recommended for gpt-5):

```json
"model": {
  "name": "gpt-5",
  "params": { "max_completion_tokens": 2048 }
}
```

---

## Key differences from direct LLM inference

|                   | Direct LLM (`/v1/chat/completions`) | Orchestration (`/completion`)  |
| ----------------- | ----------------------------------- | ------------------------------ |
| Endpoint suffix   | `/v1/chat/completions`              | `/v2/completion`               |
| Request body      | OpenAI standard                     | `config.modules` wrapper       |
| Placeholder vars  | No                                  | `placeholder_values` map       |
| Response shape    | Bare `choices[]`                    | `final_result.choices[]`       |
| Prompt templating | No                                  | Yes (`{{?variable}}` syntax)   |
| Content filtering | No                                  | Yes (Azure Content Safety)     |
| Data masking      | No                                  | Yes (SAP DPI)                  |
| Grounding / RAG   | No                                  | Yes                            |
| Model switching   | Change deployment                   | Change `model_name` in request |
