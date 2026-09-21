---
name: genai-hub-foundation-models
description: >
  List and explore foundation models available in SAP AI Core GenAI Hub: browse supported
  providers, model names, versions, capabilities, and executable IDs needed to create deployments.
  WHEN: user wants to see what models are available, find an executable-id or model-name for
  deployment, browse providers (Azure OpenAI, Anthropic, Google, Mistral, Cohere, etc.), check
  model capabilities or context length, get the correct model-name to pass to create_llm_deployment,
  or get curl inference examples for a deployed model (chat completions, Responses API, embeddings,
  image generation, etc.).
  DO NOT USE FOR: creating or managing deployments — use `aicore-lifecycle-management`.
compatibility: Requires Python 3.11+, uv, and sap-ai-sdk-core.
---

## Rules

1. Fetch the live model list when the model name is unknown or unconfirmed — skip if the user already named a specific model.
2. `executable-id` and `model-name` values from this skill are the inputs needed by `aicore-lifecycle-management` to create a deployment.
3. If credentials are not configured, invoke `aicore-admin-resources` first.
4. Before executing any curl example, get a Bearer token with:
   ```bash
   export TOKEN=$(uv run skills/aicore-admin-resources/scripts/get_token.py)
   ```
   Never add `2>&1` or pipe the command — that prints the raw JWT into the conversation.

---

## List Available Models

```bash
# Show all options and examples:
uv run scripts/list_foundation_models.py --help

# One provider only (e.g. Azure OpenAI):
uv run scripts/list_foundation_models.py --executable-id azure-openai

# Detailed view (versions, capabilities, context length, streaming support):
uv run scripts/list_foundation_models.py --response-format detailed

# Machine-readable JSON for scripting:
uv run scripts/list_foundation_models.py --json | jq '.[].model'
uv run scripts/list_foundation_models.py --response-format detailed --json | jq '.[] | select(.model == "gpt-4o") | .versions'

# Models supported by the Orchestration service only:
uv run scripts/list_foundation_models.py --scenario-id orchestration
```

---

## Provider → Executable ID Mapping

| Provider       | `--executable-id`   |
| -------------- | ------------------- |
| Azure OpenAI   | `azure-openai`      |
| Anthropic      | `aws-bedrock`       |
| Google         | `gcp-vertexai`      |
| Amazon Bedrock | `aws-bedrock`       |
| Mistral AI     | `aicore-mistralai`  |
| Cohere         | `aicore-cohere`     |
| Perplexity     | `perplexity-ai`     |
| NVIDIA         | `aicore-nvidia`     |
| Open Source    | `aicore-opensource` |
| SAP            | `aicore-sap`        |

Supported models in your instance may differ from this table — use the script to get the live list.

---

## Create a Deployment

Once you have the `executable-id` and `model-name`, check whether a RUNNING deployment for that model already exists:

```bash
uv run skills/aicore-lifecycle-management/scripts/get_deployments.py \
  --scenario foundation-models --status RUNNING --json
```

If one is found, use `AskUserQuestion` to ask whether to reuse it or create a new one. Then invoke `aicore-lifecycle-management` with both values.

The `modelName` value must exactly match the catalog output — a mismatch causes an "Invalid Configuration" error at deployment time, not at configuration creation.

---

## When to Load Reference Files

| Trigger                                                                                      | Load                   |
| -------------------------------------------------------------------------------------------- | ---------------------- |
| Curl inference examples, provider-specific endpoint paths, or about to call a deployed model | `references/MODELS.md` |

---

## Finding the Deployment URL for a Curl Call

1. **Get the `executable-id`** — look it up in the Provider → Executable ID table above.

2. **Find the running deployment:**
   ```bash
   uv run skills/aicore-lifecycle-management/scripts/get_deployments.py \
     --scenario foundation-models --executable-id <executable-id> --status RUNNING --json
   # use .deployment_url and .resource_group from the matching entry
   ```

3. See `references/MODELS.md` for export setup and curl examples per provider.

---

## Handoffs

- **Credential/auth error?** → invoke `aicore-admin-resources`
- **Ready to create a deployment with the model you found?** → invoke `aicore-lifecycle-management`
