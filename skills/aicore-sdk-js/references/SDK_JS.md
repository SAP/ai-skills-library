# JavaScript/TypeScript SDK Reference: @sap-ai-sdk (v2)

GitHub: https://github.com/SAP/ai-sdk-js
Online Documentation: https://sap.github.io/ai-sdk/docs/js/overview-cloud-sdk-for-ai-js
llms.txt (for fetching): https://sap.github.io/ai-sdk/llms.txt

> **Version note:** This reference targets `@sap-ai-sdk` **v2** (orchestration `2.14+`).
> The v2 config shape is `promptTemplating: { model: { name, params }, prompt: { template } }`.
> If you see older examples using `llm: { model_name }` / `templating: { template }`, those are **v1**
> and will not compile against v2. When the `context7` MCP tool is available, prefer it for the
> freshest API (`/websites/sap_github_io_ai-sdk_js`); otherwise this reference is the source of truth.

## Packages

| Package                         | Purpose                                                       |
| ------------------------------- | ------------------------------------------------------------- |
| `@sap-ai-sdk/orchestration`     | Orchestration service client (recommended entry point)        |
| `@sap-ai-sdk/foundation-models` | Direct Azure OpenAI proxy client                              |
| `@sap-ai-sdk/openai`            | Native OpenAI SDK surface on AI Core (no LiteLLM proxy needed) |
| `@sap-ai-sdk/langchain`         | LangChain-compatible clients (chat, embedding, orchestration) |
| `@sap-ai-sdk/document-grounding`| Document grounding / RAG pipelines                            |
| `@sap-ai-sdk/prompt-registry`   | Managed, versioned prompt templates                           |
| `@sap-ai-sdk/llm-batch`         | Asynchronous batch LLM jobs                                   |
| `@sap-ai-sdk/rpt`               | SAP-RPT-1 relational/tabular prediction (not chat)            |
| `@sap-ai-sdk/context-registry`  | Manage data destinations, tabular artifacts, scenario configs |
| `@sap-ai-sdk/ai-api`            | AI Core lifecycle management (deployments, configs, files)    |

## Installation

```bash
# Orchestration + foundation models
npm install @sap-ai-sdk/orchestration @sap-ai-sdk/foundation-models

# LangChain integration (no LiteLLM proxy needed)
npm install @sap-ai-sdk/langchain @langchain/core

# Or with bun
bun add @sap-ai-sdk/orchestration @sap-ai-sdk/foundation-models
```

## Configuration

Credentials are read from the `AICORE_SERVICE_KEY` environment variable (a JSON blob from the
BTP service binding). Run `aicore configure` to set them up interactively, or set the variable
manually for local testing.

### Service key shape (JS/TS)

The JS SDK uses a **single JSON blob** — not the individual env vars the Python SDK uses.
Copy the service key JSON directly from the BTP cockpit and set it as `AICORE_SERVICE_KEY`.

**`.env` file (recommended for local dev):**

```bash
AICORE_SERVICE_KEY='{"clientid":"...","clientsecret":"...","url":"https://<subdomain>.authentication.<region>.hana.ondemand.com","serviceurls":{"AI_API_URL":"https://api.ai.<region>.aws.ml.hana.ondemand.com"}}'
```

Key points:
- **Single quotes outside, double quotes inside** — required on most shells and in `.env` files.
- `url` is the XSUAA / auth URL (equivalent to `AICORE_AUTH_URL` in Python).
- `serviceurls.AI_API_URL` is the AI Core base URL (equivalent to `AICORE_BASE_URL` in Python).
- `clientid` / `clientsecret` are the OAuth2 client credentials.
- The SDK logs `Cannot create cache key … clientId is undefined` when `clientid` is missing or
  the JSON is malformed (e.g. double-quoted the outer wrapper, breaking the parse).

**Common mistakes:**

| Mistake | Symptom |
|---|---|
| Missing `clientid` field | `Cannot create cache key … clientId is undefined` |
| Wrong quoting (double-quotes outside) | JSON parse fails silently; fields read as `undefined` |
| Using Python-style individual vars (`AICORE_AUTH_URL` etc.) | SDK ignores them; use `AICORE_SERVICE_KEY` |
| Wrapped in an extra `{ "credentials": {...} }` layer | Inner fields not found |

**Loading with dotenv:**

```typescript
import "dotenv/config"; // npm install dotenv
// AICORE_SERVICE_KEY is now available — SDK picks it up automatically
```


## OrchestrationClient (recommended for JS)

Pass `messages` directly at call time — this is the default style. Use
`promptTemplating.prompt.template` with `{{?placeholder}}` values only when the template
is reused across many calls or managed server-side.

```typescript
import { OrchestrationClient } from "@sap-ai-sdk/orchestration";

const client = new OrchestrationClient({
  promptTemplating: {
    model: {
      name: "anthropic--claude-4.5-haiku",
      params: { temperature: 0.7, max_tokens: 512 },
    },
  },
});

const response = await client.chatCompletion({
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "What is the capital of France?" },
  ],
});

console.log(response.getContent());
console.log(response.getFinishReason());
console.log(JSON.stringify(response.getTokenUsage()));
```

For reusable server-side templates, use `promptTemplating.prompt.template` with
`placeholderValues` instead:

```typescript
const clientWithTemplate = new OrchestrationClient({
  promptTemplating: {
    prompt: {
      template: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: "What is the capital of {{?country}}?" },
      ],
    },
    model: {
      name: "anthropic--claude-4.5-haiku",
      params: { temperature: 0.7, max_tokens: 512 },
    },
  },
});

const response = await clientWithTemplate.chatCompletion({
  placeholderValues: { country: "France" },
});
```

## Streaming (orchestration)

The stream response is **async-iterable** via `response.stream` (this changed from v1's
EventEmitter `.on("data")` pattern). Each chunk exposes `getDeltaContent()`; after the stream
is consumed, `getFinishReason()` and `getTokenUsage()` return final metadata.

```typescript
const response = await client.stream({
  messages: [
    { role: "user", content: "Explain SAP BTP in three sentences." },
  ],
});

for await (const chunk of response.stream) {
  const delta = chunk.getDeltaContent();
  if (delta) {
    process.stdout.write(delta);
  }
}

console.log(response.getFinishReason());
console.log(response.getTokenUsage());
```

## Embeddings (orchestration)

```typescript
import { OrchestrationEmbeddingClient } from "@sap-ai-sdk/orchestration";

const embeddingClient = new OrchestrationEmbeddingClient({
  embeddings: {
    model: {
      name: "text-embedding-3-large",
      // version: "latest",         // optional
      // params: { dimensions: 4 }  // optional, model-specific
    },
  },
});

const response = await embeddingClient.embed({ input: "AI is fascinating" });
const vectors = response.getEmbeddings();
const usage = response.getTokenUsage();
```

## AzureOpenAiChatClient (foundation-models direct)

```typescript
import { AzureOpenAiChatClient } from "@sap-ai-sdk/foundation-models";

const client = new AzureOpenAiChatClient({ modelName: "gpt-4o" });
const response = await client.run({
  messages: [{ role: "user", content: "Hello" }],
});
console.log(response.getContent());
```

## Running TS Scripts

```bash
npx tsx my-script.ts   # with npx
bun run my-script.ts   # with bun
```

## LangChain (@sap-ai-sdk/langchain)

Native LangChain integration — no LiteLLM proxy needed.

### AzureOpenAiChatClient

```typescript
import {
  AzureOpenAiChatClient,
  AzureOpenAiEmbeddingClient,
} from "@sap-ai-sdk/langchain";
import { HumanMessage, SystemMessage } from "@langchain/core/messages";

const client = new AzureOpenAiChatClient({
  modelName: "gpt-4o-mini",
  temperature: 0.7,
  max_tokens: 512, // note: snake_case, mapped to the OpenAI param internally
});

// invoke
const response = await client.invoke([new HumanMessage("Hello")]);

// stream (async iterable)
const stream = await client.stream([
  new SystemMessage("You are helpful."),
  new HumanMessage("Hello"),
]);
for await (const chunk of stream) process.stdout.write(chunk.content as string);

// embeddings
const embedder = new AzureOpenAiEmbeddingClient({
  modelName: "text-embedding-3-small",
});
const vector = await embedder.embedQuery("Hello world");
```

### OrchestrationClient (LangChain)

Use the LangChain-specific config type `LangChainOrchestrationModuleConfig` (not the plain
`OrchestrationModuleConfig` — they are not assignable).

```typescript
import { OrchestrationClient } from "@sap-ai-sdk/langchain";
import type { LangChainOrchestrationModuleConfig } from "@sap-ai-sdk/langchain";

const config: LangChainOrchestrationModuleConfig = {
  promptTemplating: {
    model: { name: "gpt-4o-mini", params: { temperature: 0.7, max_tokens: 512 } },
  },
};

const client = new OrchestrationClient(config);

// invoke with placeholder values
const response = await client.invoke(messages, {
  placeholderValues: { subject: "SAP" },
});

// stream
const stream = await client.stream(messages);
for await (const chunk of stream) process.stdout.write(chunk.content as string);
```

### Structured output & tool binding

```typescript
import * as z from "zod";
const schema = z.object({ answer: z.string(), confidence: z.number() });
const structured = client.withStructuredOutput(schema, { strict: true });
const llmWithTools = client.bindTools(tools);
```

## Advanced orchestration features

The orchestration module also supports content filtering, data masking, document grounding,
and tool calling, configured as additional keys alongside `promptTemplating` in the config
object (e.g. `masking`, `filtering`, `grounding`). These evolve faster than this reference —
**prefer the `context7` MCP tool** (`/websites/sap_github_io_ai-sdk_js`) or the online docs for
their exact current shape:

- Tool calling: `promptTemplating.prompt.tools` + `chunk.getDeltaToolCalls()` on streams
- Data masking: `masking: { masking_providers: [buildDpiMaskingProvider(...)] }`
- Document grounding: `@sap-ai-sdk/document-grounding` + `grounding` module config
- Prompt registry: `@sap-ai-sdk/prompt-registry` for managed, versioned templates

## Alternative: OpenAI npm package via LiteLLM proxy

> **Prefer `@sap-ai-sdk/openai` (below) for the standard OpenAI surface** — it needs no proxy.
> Use this LiteLLM path only when you specifically require a running OpenAI-compatible proxy
> (e.g. to serve non-JS clients through one endpoint).

For frameworks that expect the standard OpenAI API, run LiteLLM as a local proxy
pointed at AI Core, then use the standard `openai` package with `baseURL` overridden.
See `references/FRAMEWORKS.md` for the LiteLLM proxy setup.

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: process.env.LITELLM_PROXY_URL ?? "http://localhost:4000",
  apiKey: process.env.LITELLM_API_KEY ?? "any",
});

const response = await client.chat.completions.create({
  model: "sap/gpt-4o",
  messages: [{ role: "user", content: "Hello" }],
});
console.log(response.choices[0].message.content);
```

## Native OpenAI SDK (`@sap-ai-sdk/openai`) — preferred over the LiteLLM proxy

If you want the **standard OpenAI SDK surface** (chat, streaming, embeddings, the
Responses API, Zod structured parsing), use `@sap-ai-sdk/openai` — it wraps the official
`openai` npm package and talks to Azure OpenAI on SAP AI Core directly. This **removes the
need for a LiteLLM proxy** for OpenAI-API users: no separate proxy process, native `openai`
types/endpoints, and SAP auth/headers/deployment routing handled for you. The `model` field
is omitted from request bodies because AI Core routes via the deployment URL. Peer dependency:
`openai` (`^6.49 || ^7`).

```typescript
import { SapOpenAi } from "@sap-ai-sdk/openai";

// Options object or plain model-name string shorthand.
const client = await SapOpenAi.createClient({ deployment: "gpt-5.4" });

// Chat
const response = await client.chat.completions.create({
  messages: [{ role: "user", content: "What is the capital of France?" }],
});
console.log(response.choices[0].message.content);

// Streaming
const stream = await client.chat.completions.create({
  messages: [{ role: "user", content: "..." }],
  stream: true,
});
for await (const chunk of stream) process.stdout.write(chunk.choices[0]?.delta?.content ?? "");

// Responses API (stateful multi-turn via previous_response_id, plus .parse for structured output)
const r = await client.responses.create({ input: "What is the capital of France?" });
console.log(r.output_text);

// Embeddings
const emb = await SapOpenAi.createClient({ deployment: "text-embedding-3-small" });
const e = await emb.embeddings.create({ input: "Hello, world!" });
```

See `assets/openai_native.ts` for the full runnable example (chat, streaming, parse,
embeddings, and the Responses API including streaming + stateful follow-ups).

## Prompt Registry (`@sap-ai-sdk/prompt-registry`)

Manage versioned, server-side prompt templates in SAP AI Core. Requests are built with
`PromptTemplatesApi` and dispatched with the fluent `.execute()` call. Every call takes the
`AI-Resource-Group-Scope` and `AI-Resource-Group` headers as its final argument.
`createUpdatePromptTemplate` takes the template body (`name`, `scenario`, `version`, and a
`spec.template` array of `{ role, content }` messages); `deletePromptTemplate` takes the id.

```typescript
import { PromptTemplatesApi } from "@sap-ai-sdk/prompt-registry";

const created = await PromptTemplatesApi.createUpdatePromptTemplate(
  { name, scenario, version: "0.0.1", spec: { template: [{ content: "Hello, world!", role: "user" }] } },
  { "AI-Resource-Group-Scope": "true", "AI-Resource-Group": "ai-sdk-js-e2e" },
).execute();

await PromptTemplatesApi.deletePromptTemplate(created.id, {
  "AI-Resource-Group-Scope": "true",
  "AI-Resource-Group": "ai-sdk-js-e2e",
}).execute();
```

See `assets/prompt_registry.ts`.

## Document grounding / RAG (`@sap-ai-sdk/document-grounding`)

RAG building blocks: `VectorApi` (collections + documents), `RetrievalApi` (search), and
`PipelinesApi` (ingestion status). All calls take an `AI-Resource-Group` header.
`createCollection` returns no body — use `.executeRaw()` and parse the collection id from the
`Location` response header. Documents are added as chunks with key/value metadata;
`RetrievalApi.search` queries across data repositories (`dataRepositoryType: "vector"`,
`dataRepositories: ["*"]`).

```typescript
import { VectorApi, RetrievalApi } from "@sap-ai-sdk/document-grounding";

const rg = { "AI-Resource-Group": "ai-sdk-js-e2e" };

const res = await VectorApi.createCollection(
  { title: "ai-sdk-js-e2e", embeddingConfig: { modelName: "text-embedding-3-small" }, metadata: [] },
  rg,
).executeRaw();
const collectionId = (res.headers.location as string).split("/").at(-2)!;

await VectorApi.createDocuments(
  collectionId,
  { documents: [{ metadata: [], chunks: [{ content: "...", metadata: [{ key: "context", value: ["sap-ai-sdk-js"] }] }] }] },
  rg,
).execute();

const results = await RetrievalApi.search(
  { query: "What does SAP AI Core do?", filters: [{ id: "my-filter", searchConfiguration: { maxChunkCount: 10 }, dataRepositories: ["*"], dataRepositoryType: "vector" }] },
  rg,
).execute();

await VectorApi.deleteCollectionById(collectionId, rg).execute();
```

See `assets/document_grounding.ts`.

## Batch LLM jobs (`@sap-ai-sdk/llm-batch`)

Run many prompts asynchronously as a single batch. Build a JSONL input with `createBatchInput`
(from `@sap-ai-sdk/foundation-models`), upload it to the object store via `FileApi.fileUpload`
(from `@sap-ai-sdk/ai-api`), then submit with `BatchesApi.createBatch`. Poll with
`getBatchStatus` (its terminal field is `current_status`) or `listBatches` (results are under
`resources`), and when finished download the result with `FileApi.fileDownload` and turn it
into typed `BatchOutputLine[]` via `parseBatchOutput` (async — remember to `await`). Every call
takes an `AI-Resource-Group` header. Requires an object store secret registered in AI Core;
`ai://` URIs reference files inside it. These APIs are marked `@experimental`.

```typescript
import { BatchesApi } from "@sap-ai-sdk/llm-batch";
import { FileApi } from "@sap-ai-sdk/ai-api";
import { createBatchInput, parseBatchOutput } from "@sap-ai-sdk/foundation-models";
import type { BatchOutputLine } from "@sap-ai-sdk/foundation-models";

const headers = { "AI-Resource-Group": "ai-sdk-js-e2e" };

const blob = createBatchInput([
  { model: "gpt-4.1-nano", messages: [{ role: "user", content: "What is machine learning?" }], max_tokens: 150 },
]);
await FileApi.fileUpload("OBJECT_STORE_SECRET/input.jsonl", blob, { overwrite: true }, headers).execute();

const created = await BatchesApi.createBatch(
  { type: "llm-native", input: { uri: "ai://OBJECT_STORE_SECRET/input.jsonl" }, output: { uri: "ai://OBJECT_STORE_SECRET/output/" }, spec: { provider: "azure-openai", model: "gpt-4.1-nano" } },
  headers,
).execute();

await BatchesApi.listBatches(headers).execute();               // .resources / .count
await BatchesApi.getBatchStatus(created.id!, headers).execute(); // .current_status

const outBlob = await FileApi.fileDownload(`OBJECT_STORE_SECRET/output/${created.id}/output.jsonl`, headers).execute();
const lines: BatchOutputLine[] = await parseBatchOutput(outBlob);
```

See `assets/llm_batch.ts`.

## Relational / tabular prediction (`@sap-ai-sdk/rpt`)

`@sap-ai-sdk/rpt` runs the SAP-RPT-1 model for relational/tabular prediction — it fills a
target column for rows whose value is a placeholder, using the other rows as context. **This is
not an LLM chat package** — there is no prompt/message/streaming API. Use
`RptClient.predictWithSchema(schema, data)` with a schema declared `as const` (required so
`PredictionData<typeof schema>` types the rows), or `predictWithoutSchema(data)` to let the
client infer the schema.

```typescript
import { RptClient } from "@sap-ai-sdk/rpt";
import type { PredictResponsePayload, PredictionData } from "@sap-ai-sdk/rpt";

const schema = [
  { name: "PRODUCT", dtype: "string" },
  { name: "PRICE", dtype: "numeric" },
  { name: "__row_idx__", dtype: "string" },
  { name: "SALESGROUP", dtype: "string" },
] as const;

const data: PredictionData<typeof schema> = {
  prediction_config: { target_columns: [{ name: "SALESGROUP", prediction_placeholder: "[PREDICT]" }] },
  index_column: "__row_idx__",
  rows: [
    { PRODUCT: "Laptop", PRICE: 999.99, __row_idx__: "35", SALESGROUP: "[PREDICT]" },
    { PRODUCT: "Desktop", PRICE: 921.5, __row_idx__: "42", SALESGROUP: "Electronics" },
  ],
};

const client = new RptClient();
const result: PredictResponsePayload = await client.predictWithSchema(schema, data);
```

See `assets/rpt.ts`.

## Context Registry (`@sap-ai-sdk/context-registry`)

Manage the three resource types that feed structured (tabular) data to AI scenarios:
**data destinations** (storage connections), **tabular artifacts** (virtual tables backed
by a destination), and **scenario configurations** (bind artifacts to an AI scenario).

All three creation operations are **async**: the API returns 202 immediately and processes
in the background. Poll the GET endpoint until `status` becomes `"ACTIVE"` (or `"ERROR"`).
Delete resources in reverse dependency order: scenario → artifact → destination.

The three API objects are `DataDestinationsApi`, `TabularArtifactsApi`, and
`ScenarioConfigurationManagerApi`. All calls take an `AI-Resource-Group` header.

```typescript
import {
  DataDestinationsApi,
  TabularArtifactsApi,
  ScenarioConfigurationManagerApi,
} from "@sap-ai-sdk/context-registry";

const rg = { "AI-Resource-Group": "default" };

// Create an Azure data destination (async — poll until ACTIVE)
await DataDestinationsApi.createUpdateDataDestination(
  "my-destination",
  {
    type: "AZURE",
    config: {
      account_name: process.env.AZURE_STORAGE_ACCOUNT!,
      container_uri: process.env.AZURE_CONTAINER_URI!,  // https://<account>.blob.core.windows.net/<container>
      sas_token: process.env.AZURE_SAS_TOKEN!,          // must grant read + list (r + l)
    },
  },
  rg,
).execute();

// Create a tabular artifact — a virtual table pointing to a Parquet file
await TabularArtifactsApi.createTabularArtifact(
  "my-artifact",
  {
    dataDestinationName: "my-destination",
    type: "PARQUET",                     // "CSV" | "PARQUET" | "DELTA"
    path: "/data/customers.parquet",     // must start with /
    csnMetadata: {
      selectedColumns: new Set(["customer_id", "region"]),  // Set<string> is serialised to an array
      definition: { definitionType: "AUTO" },
    },
  },
  rg,
).execute();

// Preview data (first 10 rows)
const preview = await TabularArtifactsApi.getTabularArtifactData("my-artifact", rg).execute();

// Create a scenario configuration binding the artifact
await ScenarioConfigurationManagerApi.createScenarioConfiguration(
  "my-scenario",
  {
    description: "Customer data scenario",
    tabularArtifacts: [{ name: "my-artifact" }],
  },
  rg,
).execute();

// List and search
const all = await DataDestinationsApi.getAllDataDestinations({}, rg).execute();   // .count / .resources
const filtered = await DataDestinationsApi.searchDestinations(
  { labels: [{ key: "env", value: "production" }] }, {}, rg,
).execute();

// Delete (reverse order)
await ScenarioConfigurationManagerApi.deleteScenarioConfigurationByName("my-scenario", rg).execute();
await TabularArtifactsApi.deleteTabularArtifact("my-artifact", rg).execute();
await DataDestinationsApi.deleteDataDestinationByName("my-destination", rg).execute();
```

See `assets/context_registry.ts` for the full lifecycle example with polling.

## AI Core lifecycle (`@sap-ai-sdk/ai-api`) — read-side only in this skill

`@sap-ai-sdk/ai-api` exposes deployment/scenario/configuration management (`DeploymentApi`,
`ScenarioApi`, `FileApi`, …). This JS skill uses it only for **read/support** operations (e.g.
`FileApi` for batch I/O, or `DeploymentApi.deploymentQuery` to list deployments). For
**creating, stopping, or deleting** deployments and configurations, hand off to
`aicore-lifecycle-management` rather than emitting lifecycle-mutating JS here.

```typescript
import { DeploymentApi } from "@sap-ai-sdk/ai-api";

// List RUNNING deployments in a resource group (read-side).
const deployments = await DeploymentApi.deploymentQuery(
  { status: "RUNNING" },
  { "AI-Resource-Group": "default" },
).execute();
```
