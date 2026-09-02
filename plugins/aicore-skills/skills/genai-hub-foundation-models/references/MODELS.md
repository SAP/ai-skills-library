# Supported Models

Models available in your AI Core instance depend on your subscription. Always fetch the live list rather than relying on hardcoded values.

## Providers

| Provider       | `scenario-id`       | `executable-id`     |
| -------------- | ------------------- | ------------------- |
| Azure OpenAI   | `foundation-models` | `azure-openai`      |
| Anthropic      | `foundation-models` | `aws-bedrock`       |
| Google         | `foundation-models` | `gcp-vertexai`      |
| Amazon Bedrock | `foundation-models` | `aws-bedrock`       |
| Mistral AI     | `foundation-models` | `aicore-mistralai`  |
| Cohere         | `foundation-models` | `aicore-cohere`     |
| Perplexity     | `foundation-models` | `perplexity-ai`     |
| NVIDIA         | `foundation-models` | `aicore-nvidia`     |
| Open Source    | `foundation-models` | `aicore-opensource` |
| SAP            | `foundation-models` | `aicore-sap`        |

> Supported models in your instance may differ. Use `list_foundation_models.py` to see what is actually available.

## Listing Supported Models

Use `scripts/list_foundation_models.py` to fetch the current model list from the API:

```bash
# All executables and their supported models:
uv run scripts/list_foundation_models.py

# One provider only (e.g. Azure OpenAI):
uv run scripts/list_foundation_models.py --executable-id azure-openai

# Machine-readable JSON:
uv run scripts/list_foundation_models.py --json

# Help:
uv run scripts/list_foundation_models.py --help
```

The script reads the `modelName` parameter description from each executable, which is the canonical source of supported model names.

## Using a Model Name

Once you have the `executable-id` and `modelName`, invoke `aicore-lifecycle-management` with these values to create a configuration and deployment. Pass:
- `scenario-id`: `foundation-models`
- `executable-id`: from the provider table above (e.g. `azure-openai`)
- `modelName` parameter: the exact model name from the script output (e.g. `gpt-4o-mini`)
- `modelVersion` parameter: `latest` (unless the user specifies otherwise)

## Inference via LLM Deployment

> **Path prefix:** Azure OpenAI endpoints use a `/v1/` prefix (e.g. `/v1/chat/completions`, `/v1/responses`). SAP-hosted open source LLMs (e.g. `mistralai--mistral-large-instruct`) use `/chat/completions` directly — no `/v1/` prefix.

All examples assume the following variables are set:

```bash
export DEPLOYMENT_URL="<deploymentUrl from get_deployments.py>"
export RESOURCE_GROUP="default"
```

> **Get a token first:** invoke `aicore-admin-resources` — it will set `$TOKEN` safely.

### Azure OpenAI (`azure-openai`)

Chat Completions ([API Reference](https://learn.microsoft.com/en-us/azure/foundry/openai/latest#create-chat-completion)):

```bash
curl -X POST "$DEPLOYMENT_URL/v1/chat/completions" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"messages":[{"role":"user","content":"Hello"}]}'
```

Responses API (gpt-5 and newer only) ([API Reference](https://learn.microsoft.com/en-us/azure/foundry/openai/latest#create-response)):

```bash
curl -X POST "$DEPLOYMENT_URL/v1/responses" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"model":"gpt-5.5","input":"Hello"}'
```

> The response `output` array may contain a `reasoning` item first. The text is at the `message` item: `output[] | select(.type=="message") | .content[0].text`.

Embeddings:

```bash
curl -X POST "$DEPLOYMENT_URL/embeddings?api-version=2023-05-15" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"input":"The food was delicious"}'
```

Image generation (dall-e-3):

```bash
curl -X POST "$DEPLOYMENT_URL/images/generations?api-version=2024-06-01" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"prompt":"A sunset over mountains","n":1,"size":"1024x1024"}'
```

Audio transcription (whisper):

```bash
curl -X POST "$DEPLOYMENT_URL/audio/transcriptions?api-version=2024-06-01" \
  -H "Authorization: Bearer $TOKEN" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -F "file=@audio.wav"
```

Audio translation to English (whisper):

```bash
curl -X POST "$DEPLOYMENT_URL/audio/translations?api-version=2024-06-01" \
  -H "Authorization: Bearer $TOKEN" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -F "file=@audio.wav"
```

Realtime audio (gpt-realtime) — WebSocket, not HTTP:

```bash
# Connect via WebSocket (e.g. using wscat):
wscat -c "$DEPLOYMENT_URL/v1/realtime" \
  -H "Authorization: Bearer $TOKEN" \
  -H "AI-Resource-Group: $RESOURCE_GROUP"
```

### Google Gemini Live (`gcp-vertexai`)

Real-time bidirectional audio/video via WebSocket — not HTTP. Use `assets/gemini_live_interactive.py` for a ready-to-run browser demo.

Model: `gemini-live-2.5-flash-native-audio`
Executable ID: `gcp-vertexai`
WS path: `/ws/google.cloud.aiplatform.v1.LlmBidiService/BidiGenerateContent`

```bash
# Connect via WebSocket (e.g. wscat):
wscat -c "$DEPLOYMENT_URL/ws/google.cloud.aiplatform.v1.LlmBidiService/BidiGenerateContent" \
  -H "Authorization: Bearer $TOKEN" \
  -H "AI-Resource-Group: $RESOURCE_GROUP"

# First message must be a setup frame:
# {"setup":{"generationConfig":{"responseModalities":["AUDIO"],"speechConfig":{"voiceConfig":{"prebuiltVoiceConfig":{"voiceName":"Kore"}}}}}}
```

### Google Gemini (`gcp-vertexai`)

Text generation ([API Reference](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.publishers.models/generateContent)):

```bash
curl -X POST "$DEPLOYMENT_URL/models/gemini-2.5-pro:generateContent" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"contents":{"role":"user","parts":{"text":"Hello"}}}'
```

Embeddings ([API Reference](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.publishers.models/predict)):

```bash
curl -X POST "$DEPLOYMENT_URL/models/gemini-embedding:predict" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"instances":[{"task_type":"RETRIEVAL_DOCUMENT","content":"Hello world"}]}'
```

Image generation (gemini-2.5-flash-image — returns base64 PNG in response):

```bash
curl -X POST "$DEPLOYMENT_URL/models/gemini-2.5-flash-image:generateContent" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{
    "contents": {"role":"user","parts":{"text":"A sunset over mountains"}},
    "generationConfig": {"responseModalities": ["IMAGE","TEXT"]}
  }'
```

The response contains `candidates[0].content.parts[]`. Image parts have `inlineData.mimeType` and `inlineData.data` (base64-encoded PNG). To save the image:

```bash
# Pipe curl output to jq + base64 decode:
... | jq -r '.candidates[0].content.parts[] | select(.inlineData) | .inlineData.data' | base64 -d > output.png
```

After saving, offer to open the image with `open output.png` if the user wants to view it.

### AWS Bedrock (`aws-bedrock`)

Anthropic Claude — Messages API at `/invoke` ([API reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)):

```bash
curl -X POST "$DEPLOYMENT_URL/invoke" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"anthropic_version":"bedrock-2023-05-31","max_tokens":1024,"messages":[{"role":"user","content":"Hello"}]}'
```

Amazon Nova — Converse API at `/converse` ([API reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html)):

```bash
curl -X POST "$DEPLOYMENT_URL/converse" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"messages":[{"role":"user","content":[{"text":"Hello"}]}]}'
```

Amazon Titan — text embeddings:

```bash
curl -X POST "$DEPLOYMENT_URL/invoke" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"inputText":"Hello world"}'
```

Amazon Titan — image generation:

```bash
curl -X POST "$DEPLOYMENT_URL/invoke" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"taskType":"TEXT_IMAGE","textToImageParams":{"text":"A sunset over mountains"},"imageGenerationConfig":{"numberOfImages":1}}'
```

### Mistral AI (`aicore-mistralai`)

```bash
curl -X POST "$DEPLOYMENT_URL/chat/completions" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"model":"mistralai--mistral-large-instruct","messages":[{"role":"user","content":"Hello"}]}'
```

### Cohere (`aicore-cohere`)

Reranker:

```bash
curl -X POST "$DEPLOYMENT_URL/rerank" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"model":"cohere-reranker","query":"fast animals","documents":["The cheetah is fast","Snails are slow"],"top_n":2}'
```

Command A (reasoning chat):

```bash
curl -X POST "$DEPLOYMENT_URL/chat" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"model":"cohere--command-a-reasoning","messages":[{"role":"user","content":"Hello"}]}'
```

### Perplexity (`perplexity-ai`)

Response includes a `citations` array with source URLs.

```bash
curl -X POST "$DEPLOYMENT_URL/chat/completions" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"model":"sonar-pro","messages":[{"role":"user","content":"What is SAP AI Core?"}]}'
```

### NVIDIA (`aicore-nvidia`)

```bash
curl -X POST "$DEPLOYMENT_URL/embeddings" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"model":"nvidia--llama-3.2-nv-embedqa-1b","input":["Hello world"],"input_type":"query"}'
```

### Open Source — Meta Llama / Mixtral (`aicore-opensource`)

```bash
curl -X POST "$DEPLOYMENT_URL/chat/completions" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"model":"meta--llama3.1-70b-instruct","messages":[{"role":"user","content":"Hello"}]}'
```

### SAP (`aicore-sap`)

ABAP / code models (`abap-codestral`, `abap-starcoder2-7b`, `sap-abap-1`, `llama-cinderella-dn`):

```bash
curl -X POST "$DEPLOYMENT_URL/chat/completions" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{"model":"abap-codestral","messages":[{"role":"user","content":"Hello"}]}'
```

SAP RPT-1 (`sap-rpt-1-small`, `sap-rpt-1-large`) — tabular predictions, not chat.

Example: predict `COSTCENTER` for a row given context rows with known values:

```bash
curl -X POST "$DEPLOYMENT_URL/predict" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "AI-Resource-Group: $RESOURCE_GROUP" \
  -d '{
    "prediction_config": {
      "target_columns": [{"name": "COSTCENTER", "prediction_placeholder": "[PREDICT]", "task_type": "classification", "top_k": 1}]
    },
    "index_column": "ID",
    "rows": [
      {"ID": "35",  "PRODUCT": "Couch",        "PRICE": 999.99,  "ORDERDATE": "28-11-2025", "COSTCENTER": "[PREDICT]"},
      {"ID": "44",  "PRODUCT": "Office Chair",  "PRICE": 150.80,  "ORDERDATE": "02-11-2025", "COSTCENTER": "Office Furniture"},
      {"ID": "104", "PRODUCT": "Server Rack",   "PRICE": 2200.00, "ORDERDATE": "01-11-2025", "COSTCENTER": "Data Infrastructure"}
    ],
    "data_schema": {
      "ID":         {"dtype": "string"},
      "PRODUCT":    {"dtype": "string"},
      "PRICE":      {"dtype": "numeric"},
      "ORDERDATE":  {"dtype": "date"},
      "COSTCENTER": {"dtype": "string"}
    }
  }'
```

The row marked `[PREDICT]` is the query; the other rows are in-context examples — no training needed. Response includes `prediction` and `confidence` per row.

RPT-1 also accepts Parquet files via `POST $DEPLOYMENT_URL/predict_parquet` with multipart form data.

