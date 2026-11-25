# Python SDK Reference: sap-ai-sdk-gen

Package: `sap-ai-sdk-gen` (replaces deprecated `generative-ai-hub-sdk`)
Import namespace: `gen_ai_hub` (same for both packages)
GitHub: https://github.com/SAP/ai-sdk-python
Online Documentation: https://sap.github.io/ai-sdk/docs/python/overview

## Modules

The SDK ships as the `sap-ai-sdk-gen` package, importing under the `gen_ai_hub` namespace.
Lifecycle management lives in a separate `sap-ai-sdk-core` package (`ai_core_sdk`).

| Module                                | Purpose                                                        |
| ------------------------------------- | -------------------------------------------------------------- |
| `gen_ai_hub.orchestration_v2`         | Orchestration service client v2 (recommended entry point)                                  |                                                                |
| `gen_ai_hub.proxy.native.openai`      | Native OpenAI surface on AI Core                               |
| `gen_ai_hub.proxy.native.google_genai`| Native Google Gemini client (`[google]` extra)                 |
| `gen_ai_hub.proxy.native.amazon`      | Native Amazon Bedrock client (`[amazon]` extra)                |
| `gen_ai_hub.proxy.native.sap`         | SAP RPT relational/tabular prediction (not chat)               |
| `gen_ai_hub.proxy.langchain`          | LangChain-compatible clients (`init_llm`, `init_embedding_model`) |
| `gen_ai_hub.document_grounding`       | Document grounding / RAG pipelines                             |
| `gen_ai_hub.prompt_registry`          | Managed, versioned prompt templates                            |
| `gen_ai_hub.batch_service`            | Asynchronous batch LLM jobs                                    |
| `gen_ai_hub.evaluations`              | Offline evaluation of models / prompts                         |
| `ai_core_sdk` (`sap-ai-sdk-core`)     | AI Core lifecycle management (deployments, configs, secrets)   |

## Installation

```bash
uv add sap-ai-sdk-gen                      # default
uv add "sap-ai-sdk-gen[google]"            # with Google Gemini
uv add "sap-ai-sdk-gen[amazon]"            # with Amazon Bedrock
uv add "sap-ai-sdk-gen[all]"               # all providers (required for init_llm / init_embedding_model)
```

See `aicore-admin-resources/references` for credential setup.
## Credentials

The Python SDK accepts credentials in **two** ways — pick one:

**Option A — individual environment variables:**

```bash
export AICORE_AUTH_URL="https://<subdomain>.authentication.<region>.hana.ondemand.com/oauth/token"
export AICORE_CLIENT_ID="<clientid>"
export AICORE_CLIENT_SECRET="<clientsecret>"
export AICORE_BASE_URL="https://api.ai.<region>.cfapps.<provider>.hana.ondemand.com/v2"
export AICORE_RESOURCE_GROUP="default"
```

**Option B — the full BTP service key as a single JSON blob**, set via `AICORE_SERVICE_KEY`:

```bash
export AICORE_SERVICE_KEY='{"clientid":"...","clientsecret":"...","url":"https://<subdomain>.authentication.<region>.hana.ondemand.com","serviceurls":{"AI_API_URL":"https://api.ai.<region>.aws.ml.hana.ondemand.com"}}'
export AICORE_RESOURCE_GROUP="<resource-group>"  
```

Or run `aicore configure` to set the individual vars interactively from a BTP service key.

**Common mistakes:**

| Mistake | Symptom |
|---|---|
| `AICORE_AUTH_URL` missing the `/oauth/token` path suffix | 401 Unauthorized |
| `AICORE_BASE_URL` ending without `/v2` | 404 Not Found |
| Wrong resource group | Deployment not found / empty list |

## Key Import Cheatsheet

The most common imports for each entry point, grouped by use case — copy the block for the surface you need.

### Native OpenAI proxy (simplest)

```python
from gen_ai_hub.proxy.native.openai import chat
response = chat.completions.create(model_name="gpt-4o-mini", messages=[...])
```

### Full OpenAI client

```python
from gen_ai_hub.proxy.native.openai import OpenAI, AsyncOpenAI
client = OpenAI()
response = client.chat.completions.create(model="gpt-4o", messages=[...])
```

### LangChain wrappers

```python
from gen_ai_hub.proxy.langchain.openai import ChatOpenAI, OpenAIEmbeddings
from gen_ai_hub.proxy.langchain import init_llm, init_embedding_model

llm = init_llm("gpt-4o", temperature=0.2, max_tokens=1024)
embedder = init_embedding_model("text-embedding-3-small")
```

### Orchestration service

```python
from gen_ai_hub.orchestration_v2 import (
    OrchestrationService,
    OrchestrationConfig,
    ModuleConfig,
    LLMModelDetails,
    PromptTemplatingModuleConfig,
    Template,
    UserMessage,
    SystemMessage,
)
```

### Content filtering & masking

```python
from gen_ai_hub.orchestration_v2 import (
    FilteringModuleConfig,
    AzureContentSafetyInputFilterConfig,
    AzureContentSafetyOutputFilterConfig,
    AzureContentFilter,
    MaskingModuleConfig,
    MaskingProviderConfig,
)
```

### Document grounding (RAG)

```python
from gen_ai_hub.document_grounding import (
    VectorAPIClient, RetrievalAPIClient, PipelineAPIClient,
)
```

### Prompt registry

```python
from gen_ai_hub.prompt_registry import PromptTemplateClient, PromptTemplateSpec, PromptTemplate
```

### Batch service

```python
from gen_ai_hub.batch_service import BatchService
```

### Proxy client management

```python
from gen_ai_hub.proxy import get_proxy_client, set_proxy_version, GenAIHubProxyClient
client = GenAIHubProxyClient()
deployment = client.select_deployment(model_name="gpt-4o")
```

## OrchestrationService API

The orchestration service runs a prompt through a configurable pipeline of modules (templating, LLM, filtering, masking, grounding). You build a `Template`, attach an `LLMModelDetails`, wrap them in a `ModuleConfig` / `OrchestrationConfig`, and call `run`.

### OrchestrationService -- Base pipeline

The four-step pipeline: define the template (with `{{?placeholder}}` variables and optional `defaults`), define the LLM, assemble the config, then `run()` with placeholder values.

```python
# Define the Template
from gen_ai_hub.orchestration_v2 import Template, SystemMessage, UserMessage

template = Template(
    template=[
        SystemMessage(content="You are a helpful translation assistant."),
        UserMessage(content="Translate the following text to {{?to_lang}}: {{?user_query}}"),
    ],
    defaults={"to_lang": "German"}
)

# Define the LLM
from gen_ai_hub.orchestration_v2 import LLMModelDetails

llm = LLMModelDetails(name="gpt-5-nano", params={"max_completion_tokens": 2048})

# Create the Configuration
from gen_ai_hub.orchestration_v2 import PromptTemplatingModuleConfig, ModuleConfig, OrchestrationConfig

prompt_template = PromptTemplatingModuleConfig(prompt=template, model=llm)
module_config = ModuleConfig(prompt_templating=prompt_template)
config = OrchestrationConfig(modules=module_config)

# Run the Request
from gen_ai_hub.orchestration_v2 import OrchestrationService

orchestration_service = OrchestrationService(config=config)

result = orchestration_service.run(placeholder_values={"user_query": "The Orchestration Service is working!"})
print(result.final_result.choices[0].message.content)
```

### OrchestrationService -- Embeddings

Generate embeddings through the orchestration pipeline with `EmbeddingsOrchestrationConfig` and `svc.embed()` — use this when embeddings should flow through the same orchestration modules (e.g. masking) as chat requests.

```python
from gen_ai_hub.orchestration_v2 import (
    OrchestrationService, EmbeddingsOrchestrationConfig, EmbeddingsModuleConfigs,
    EmbeddingsModelConfig, EmbeddingsModelDetails, EmbeddingsInput
)

service = OrchestrationService()
embeddings_config = EmbeddingsOrchestrationConfig(
    modules=EmbeddingsModuleConfigs(
        embeddings=EmbeddingsModelConfig(model=EmbeddingsModelDetails(name="text-embedding-3-large"))
    )
)
response = service.embed(config=embeddings_config, input=EmbeddingsInput(text="Hello World!"))
embedding = response.final_result.data[0].embedding
print(f"Embedding dimensions: {len(embedding)}")
print(f"First 5 values: {embedding[:5]}")
```

## OrchestrationService -- Streaming

Use the `stream` method of the `OrchestrationService` with the `stream` option in `OrchestrationConfig`. This method returns an object that streams chunks of the response as they become available. You can then extract relevant information from the `delta` field.

```python
from gen_ai_hub.orchestration_v2 import (
    Template, SystemMessage, UserMessage, LLMModelDetails, PromptTemplatingModuleConfig,
    ModuleConfig, OrchestrationConfig, OrchestrationService, GlobalStreamOptions
)

template = Template(template=[
    SystemMessage(content="You are a helpful AI assistant."),
    UserMessage(content="{{?text}}"),
])
llm = LLMModelDetails(name="gpt-4o")
prompt_template = PromptTemplatingModuleConfig(prompt=template, model=llm)
module_config = ModuleConfig(prompt_templating=prompt_template)

config = OrchestrationConfig(modules=module_config, stream=GlobalStreamOptions(enabled=True))
client = OrchestrationService(config=config)

result = client.stream(placeholder_values={"text": "Which color is the sky? Answer in one sentence."})
for part in result:
    print(part.final_result.choices[0].delta.content)
    print("*" * 20)
```

For native-SDK and LangChain streaming (OpenAI, Google GenAI, Anthropic/Amazon Bedrock, and the unified `init_llm`), see `assets/streaming.py`.

## Advanced orchestration features

The orchestration service also supports **content filtering, data masking, image/multimodal
input, document grounding, tool calling, reasoning, translation, conversation history,
prompt-registry template referencing, deployment resolution, async calls, few-shot
templating, and additional pipeline options**.
These evolve faster than this reference — **prefer the [Orchestration Service V2 docs](https://sap.github.io/ai-sdk/docs/python/examples/orchestration-service2)**
for their exact current shape. Do not guess these shapes from memory.

- **Content filtering** — the `Content Filtering` module filters both the input to the LLM module (input filter) and the output generated by the LLM (output filter); Azure Content Safety or Llama Guard 3. (docs: [Content Filtering](https://sap.github.io/ai-sdk/docs/python/examples/orchestration-service2#content-filtering))
- **Data masking** — the `Data Masking` module anonymizes or pseudonymizes personally identifiable information (PII) before it is processed by the LLM module. (docs: [Data Masking](https://sap.github.io/ai-sdk/docs/python/examples/orchestration-service2#data-masking))
- **Image / multimodal input** — multimodal prompts let you include images alongside text in your messages (add an `ImageItem` to a `UserMessage`). (docs: [Using Images as Input](https://sap.github.io/ai-sdk/docs/python/examples/orchestration-service2#using-images-as-input))
- **Document grounding (RAG)** — the `grounding` module, or standalone `gen_ai_hub.document_grounding` clients. (docs: [document_grounding](https://sap.github.io/ai-sdk/docs/python/examples/document-grounding))
- **Tool calling** — allows LLMs to request the execution of external operations such as Python functions, API calls, or other tools. (docs: [Tool Calling](https://sap.github.io/ai-sdk/docs/python/examples/orchestration-service2#tool-calling-function-calling))
- **Reasoning** — a harmonized `reasoning_effort` parameter controls the level of reasoning a model performs. (docs: [Reasoning](https://sap.github.io/ai-sdk/docs/python/examples/orchestration-service2#reasoning))
- **Translation** — the `Translation` module translates text from one language to another, either input before the LLM module or output generated by it. (docs: [Translation](https://sap.github.io/ai-sdk/docs/python/examples/orchestration-service2#translation))
- **Conversation history / memory** — integrate the `OrchestrationService` with a chatbot to handle conversational flow. (docs: [Chatbot with Memory](https://sap.github.io/ai-sdk/docs/python/examples/orchestration-service2#chatbot-with-memory))
- **Prompt-registry** — reference a stored template from inside a `prompt_templating` module instead of defining it inline, either by id (`TemplateRefByID(id=...)`) or by scenario/name/version (`TemplateRefByScenarioNameVersion(scenario=..., name=..., version=...)`). To store, retrieve, version, and export whole orchestration configs (not just templates) in the registry, use `OrchestrationConfigClient`. (docs: [Referencing Templates](https://sap.github.io/ai-sdk/docs/python/examples/orchestration-service2#referencing-templates-from-the-prompt-registry), [Orchestration Config Management](https://sap.github.io/ai-sdk/docs/python/examples/prompt-registry#orchestration-config-management))
- **Deployment resolution** — the `OrchestrationService` class provides multiple ways to specify and target orchestration deployments when sending requests. (docs: [Understanding Deployment Resolution](https://sap.github.io/ai-sdk/docs/python/examples/orchestration-service2#understanding-deployment-resolution))
- **Async support** — the `OrchestrationService` also supports asynchronous calls. (docs: [Async Support](https://sap.github.io/ai-sdk/docs/python/examples/orchestration-service2#async-support))
- **Sentiment analysis with few-shot learning** — demonstrates the different message `roles` in the templating module through a few-shot learning use case. (docs: [Sentiment Analysis with Few-Shot Learning](https://sap.github.io/ai-sdk/docs/python/examples/orchestration-service2#sentiment-analysis-with-few-shot-learning))
- **Additional pipeline options** — the orchestration pipeline supports further configuration beyond the core modules, including fallback configurations, response format options, and more. (docs: [Additional Pipeline Options](https://sap.github.io/ai-sdk/docs/python/examples/orchestration-service2#additional-pipeline-options))

## Batch Service API

Requires an object store secret registered in AI Core and a pre-uploaded `.jsonl` input file.
Batch consumption supports native LLM calls only (not orchestration requests).
All methods have async counterparts: `acreate`, `alist`, `aget`, `aget_status`, `acancel`, `adelete`.
Results land in `{output_uri}{batch_id}/output.jsonl`; failures in `.../error.jsonl`.

```python
import time
from gen_ai_hub.batch_service import BatchService

batch_service = BatchService()

# Or with an explicit proxy client:
# from gen_ai_hub.proxy import get_proxy_client
# batch_service = BatchService(proxy_client=get_proxy_client('gen-ai-hub'))

INPUT_URI = "ai://<object_store_secret_name>/<path>/input.jsonl"
OUTPUT_URI = "ai://<object_store_secret_name>/<output_folder>/"
MODEL = "gpt-4.1"
PROVIDER = "azure-openai"

create_response = batch_service.create(
    type="llm-native",
    input_uri=INPUT_URI,
    output_uri=OUTPUT_URI,
    provider=PROVIDER,
    model=MODEL,
)

BATCH_ID = create_response.id
print(f"Batch ID: {BATCH_ID}")
print(f"Status:   {create_response.status}")
print(f"Message:  {create_response.message}")
```

See `assets/batch_service.py` for the runnable script.

## Prompt Registry API

Create, retrieve, fill, and version server-side prompt templates with `PromptTemplateClient`. Templates use `{{?placeholder}}` variables filled at request time via `fill_prompt_template_by_id`, and every template is addressed by a `scenario` / `name` / `version` triple.

```python
from gen_ai_hub.proxy import get_proxy_client
from gen_ai_hub.prompt_registry import PromptTemplateClient
from gen_ai_hub.prompt_registry import PromptTemplateSpec, PromptTemplate


# Initialize Client
proxy_client = get_proxy_client(proxy_version="gen-ai-hub")
prompt_registry_client = PromptTemplateClient(proxy_client=proxy_client)

# Create a Prompt Template
prompt_template_spec = PromptTemplateSpec(
    template=[PromptTemplate(role='system', content='You are a helpful assistant.')]
)
template_id = prompt_registry_client.create_prompt_template(
    scenario='MyScenario',
    name='prompt_template_name',
    version='1.0.0',
    prompt_template_spec=prompt_template_spec
).id

print(f"Created Prompt Template with ID: {template_id}")
```

See `assets/prompt_registry.py` for the runnable script.

## Document Grounding / RAG

Full RAG lifecycle: Pipeline API, Vector API (collections, documents, search), and Retrieval API.

Replace the `<PIPELINE_ID>` / `<EXECUTION_ID>` / `<DOCUMENT_ID>` / `<COLLECTION_ID>` / `<DATA_REPOSITORY_ID>` / `<KEY>` / `<VALUE>` placeholders with real values before running. Collection creation returns 202 Accepted (async) — match by title via `vector.get_collections()` to retrieve the id.

```python
from gen_ai_hub.proxy import get_proxy_client
from gen_ai_hub.document_grounding.client import PipelineAPIClient, VectorAPIClient, RetrievalAPIClient
from gen_ai_hub.document_grounding.models.pipeline import (
    SearchPipelineRequest, DataRepositoryMetadataItem, ManualPipelineTrigger,
)
from gen_ai_hub.document_grounding.models.vector import (
    CollectionCreateRequest, EmbeddingConfig,
    DocumentsCreateRequest, TextOnlyBaseChunk, BaseDocument, VectorKeyValueListPair,
    TextSearchRequest, VectorSearchFilter, VectorSearchConfiguration,
)
from gen_ai_hub.document_grounding.models.retrieval import (
    RetrievalSearchInput, RetrievalSearchFilter, RetrievalSearchConfiguration,
)

proxy_client = get_proxy_client(proxy_version='gen-ai-hub')

pipelines = PipelineAPIClient(proxy_client)
vector = VectorAPIClient(proxy_client)
retrieval = RetrievalAPIClient(proxy_client)

pipelines_list = pipelines.get_pipelines(top=10)
print(pipelines_list)
```

See `assets/document_grounding.py` for the runnable script.

## Relational / Tabular Prediction (SAP RPT)

`RPTClient` runs the SAP RPT model for relational/tabular prediction — it fills in
missing values in a table given context rows and a target column.

```python
from gen_ai_hub.proxy.native.sap import RPTRequest, PredictionConfig, TargetColumn, RPTClient

rows_regression = [
    {"PRODUCT": "Couch", "PRICE": 999.99, "ORDERDATE": "28-11-2025", "ID": "35", "DISCOUNT_RATE": "[PREDICT]"},
    {"PRODUCT": "Office Chair", "PRICE": 150.80, "ORDERDATE": "02-11-2025", "ID": "44", "DISCOUNT_RATE": 0.12},
    {"PRODUCT": "Server Rack", "PRICE": 2200.00, "ORDERDATE": "01-11-2025", "ID": "104", "DISCOUNT_RATE": 0.05},
    {"PRODUCT": "Standing Desk", "PRICE": 640.00, "ORDERDATE": "05-11-2025", "ID": "205", "DISCOUNT_RATE": 0.10},
    {"PRODUCT": "Monitor 27 inch", "PRICE": 289.99, "ORDERDATE": "08-11-2025", "ID": "306", "DISCOUNT_RATE": "[PREDICT]"},
]

client = RPTClient()
body = RPTRequest(
    prediction_config=PredictionConfig(
        target_columns=[TargetColumn(name="DISCOUNT_RATE", prediction_placeholder="[PREDICT]", task_type="regression")]
    ),
    rows=rows_regression
)
response = client.predict(body=body, model_name="sap-rpt-1.6")
print(response.predictions)
```

Use `genai-hub-foundation-models` to list the RPT models deployed in your tenant.

See `assets/rpt.py` for the runnable script.

## Embeddings

Turn text into vectors via the native proxy `embeddings` helper. Install: `uv add "sap-ai-sdk-gen[amazon]"` (Amazon block needs the `[amazon]` extra; native OpenAI blocks work with the base `sap-ai-sdk-gen`). For the LangChain `init_embedding_model` wrapper, see the LangChain — Unified Init section below; for embeddings routed through the orchestration pipeline, see the orchestration embeddings section above.

### Native OpenAI proxy

```python
from gen_ai_hub.proxy.native.openai import embeddings

response = embeddings.create(
    input="Every decoding is another encoding.",
    model_name="text-embedding-ada-002"
)
print(response.data)
```

With encoding format:

```python
from gen_ai_hub.proxy.native.openai import embeddings

response = embeddings.create(
    input="Every decoding is another encoding.",
    model_name="text-embedding-ada-002",
    encoding_format='base64'
)
print(response.data)
```

### Amazon

```python
import json
from gen_ai_hub.proxy.native.amazon import Session

bedrock = Session().client(model_name="amazon--titan-embed-text")
body = json.dumps({"inputText": "Please recommend books with a theme similar to the movie 'Inception'."})
response = bedrock.invoke_model(body=body)
response_body = json.loads(response.get("body").read())
print(response_body)
```

See `assets/embeddings.py` for the runnable embedding script.

## Google GenAI Native Client

Access Google Gemini models through the native `google-genai` client surface on AI Core, covering non-streaming, streaming, async, and function calling.

Install: `uv add "sap-ai-sdk-gen[google]"`

```python
from gen_ai_hub.proxy.native.google_genai import Client
from gen_ai_hub.proxy import get_proxy_client

proxy_client = get_proxy_client('gen-ai-hub')
client = Client(proxy_client=proxy_client)

# Non-streaming
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain the theory of relativity in simple terms.",
)
print(response.text)

# Streaming
for chunk in client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents="Explain singularity in short terms.",
):
    print(chunk.text, end="")

# Async (use inside async context)
async with Client(proxy_client=proxy_client).aio as aclient:
    response = await aclient.models.generate_content(
        model="gemini-3.5-flash",
        contents="Explain the relativity theory in simple terms.",
    )
    print(response.text)
```

Function calling with Google GenAI:

```python
from google.genai import types

def get_current_weather(location: str) -> str:
    """Returns the current weather. Args: location: City and state, e.g. San Francisco, CA"""
    return "sunny"

chat = client.chats.create(
    model="gemini-3.5-flash",
    config=types.GenerateContentConfig(tools=[get_current_weather]),
)
response = chat.send_message("What is the weather like in Boston?")
print(response)
```

## Amazon Bedrock Native Client

Access Amazon Bedrock models (including Claude) through the native boto3-style `Session` client, using the Bedrock Converse API for chat and `converse_stream` for streaming.

Install: `uv add "sap-ai-sdk-gen[amazon]"`

```python
import json
from gen_ai_hub.proxy.native.amazon import Session

# Converse (Claude via Amazon)
bedrock_claude = Session().client(model_name="anthropic--claude-4-sonnet")
conversation = [
    {"role": "user", "content": [{"text": "Describe the purpose of a 'hello world' program in one line."}]}
]
response = bedrock_claude.converse(
    messages=conversation,
    inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
)
print(response)

# Streaming
response = bedrock_claude.converse_stream(
    messages=conversation,
    inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
)
for event in response["stream"]:
    delta = event.get("contentBlockDelta", {}).get("delta", {})
    if "text" in delta:
        print(delta["text"], end="")
```

## LangChain — Unified Init (recommended)

`init_llm` and `init_embedding_model` support all providers (OpenAI, Gemini, Claude, etc.) from a single import.

Install: `uv add "sap-ai-sdk-gen[all]"` — required because `init_llm` eagerly imports all provider backends at module load time.

```python
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from gen_ai_hub.proxy.langchain import init_llm
from gen_ai_hub.proxy import get_proxy_client

template = """Question: {question}
    Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=['question'])
question = 'What is a supernova?'

llm = init_llm('gpt-5.4-nano', max_tokens=300, proxy_client=get_proxy_client('gen-ai-hub'))
chain = prompt | llm | StrOutputParser()
response = chain.invoke({'question': question})
print(response)
```

```python
from gen_ai_hub.proxy.langchain import init_embedding_model

text = 'Every decoding is another encoding.'
embeddings = init_embedding_model('text-embedding-ada-002')
response = embeddings.embed_query(text)
print(response)
```

For provider-specific LangChain clients:

```python
from gen_ai_hub.proxy.langchain import (
    ChatOpenAI,          # OpenAI models
    ChatBedrock,         # Anthropic Claude via Amazon Bedrock
    ChatBedrockConverse, # Bedrock Converse API
    ChatGoogleGenerativeAI,  # Google Gemini
)
```

## Tool Calling

Define tools using the OpenAI function schema, then handle the model's tool call and return the result in a second request.

```python
import json
from gen_ai_hub.proxy.native.openai import OpenAI

client = OpenAI()

# Define tools using the OpenAI function schema
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name, e.g. Berlin"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"], "default": "celsius"},
                },
                "required": ["city"],
            },
        },
    }
]

messages = [{"role": "user", "content": "What's the weather in Berlin right now?"}]

# First call — model may request a tool
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)

msg = response.choices[0].message
```

See `assets/tool_calling.py` for the runnable script.

## Multi-turn Chat

Maintain conversation history across messages by appending each user message and assistant reply to the same list.

```python
from gen_ai_hub.proxy.native.openai import OpenAI

client = OpenAI()

# Non-streaming multi-turn
conversation = [{"role": "system", "content": "You are a helpful assistant."}]


def chat(user_message: str) -> str:
    conversation.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation,
        max_completion_tokens=512,
    )
    assistant_reply = response.choices[0].message.content or ""
    conversation.append({"role": "assistant", "content": assistant_reply})
    return assistant_reply


print("User: What is SAP AI Core?")
print(f"Assistant: {chat('What is SAP AI Core?')}\n")
```

See `assets/multi_turn.py` for the runnable script.

## Async (AsyncOpenAI + concurrent calls)

Use `AsyncOpenAI` to issue many requests concurrently with `asyncio.gather` — each call is non-blocking, so independent prompts run in parallel instead of one after another.

```python
import asyncio
from gen_ai_hub.proxy.native.openai import AsyncOpenAI

client = AsyncOpenAI()

MESSAGES = [
    {"role": "system", "content": "You are a helpful assistant. Be concise."},
    {"role": "user", "content": "What is SAP AI Core?"},
]

# Non-streaming — concurrent requests
async def ask(question: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Be concise."},
            {"role": "user", "content": question},
        ],
        max_completion_tokens=256,
    )
    return response.choices[0].message.content or ""
```

See `assets/async_chat.py` for the full runnable example including streaming.

## Notes
- `UNKNOWN` status during deployment init is **not** a failure — it's intermediate
- Use `gen_ai_hub`, never `generative_ai_hub` (old deprecated package)
- `model_name` kwarg is used in native clients; `model` (standard OpenAI style) also works via the OpenAI client wrapper
