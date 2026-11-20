/**
 * Install: npm install @sap-ai-sdk/llm-batch @sap-ai-sdk/ai-api @sap-ai-sdk/foundation-models
 * Run:     npx tsx llm_batch.ts   (or: bun run llm_batch.ts)
 * Purpose: Submit and manage LLM batch jobs — build JSONL input, upload it to the
 *          object store, create a batch, list/poll status, then download and parse output.
 * Credentials: run 'aicore configure' or see references/SETUP.md
 */

import { BatchesApi } from "@sap-ai-sdk/llm-batch";
import { FileApi } from "@sap-ai-sdk/ai-api";
import { createBatchInput, parseBatchOutput } from "@sap-ai-sdk/foundation-models";
import type { BatchOutputLine } from "@sap-ai-sdk/foundation-models";

const headers = { "AI-Resource-Group": "ai-sdk-js-e2e" };

// Object-store paths and URIs. The secret name maps to an object store secret
// registered in AI Core; the ai:// URIs reference files inside that store.
const secretName = "OBJECT_STORE_SECRET";
const fileName = "input.jsonl";
const inputUri = "ai://OBJECT_STORE_SECRET/input.jsonl";
const outputUri = "ai://OBJECT_STORE_SECRET/output/";
const outputFolder = "output/";

// 1. Build the JSONL batch input from a list of chat completion requests.
const blob = createBatchInput([
  {
    model: "gpt-4.1-nano",
    messages: [{ role: "user", content: "What is machine learning?" }],
    max_tokens: 150,
  },
]);

// 2. Upload the input JSONL to the object store.
const up = await FileApi.fileUpload(
  `${secretName}/${fileName}`,
  blob,
  { overwrite: true },
  headers,
).execute();
console.log("Uploaded input file:", up.url);

// 3. Create the batch job pointing at the uploaded input and desired output.
const created = await BatchesApi.createBatch(
  {
    type: "llm-native",
    input: { uri: inputUri },
    output: { uri: outputUri },
    spec: { provider: "azure-openai", model: "gpt-4.1-nano" },
  },
  headers,
).execute();
const batchId = created.id!;
console.log("Created batch:", batchId);

// 4. List all batches and check status of the one we just created.
const batches = await BatchesApi.listBatches(headers).execute();
console.log("Total batches:", batches.resources?.length);

// Batch runs are asynchronous — in a real workflow, poll getBatchStatus until
// `current_status` reaches a terminal state before downloading output.
const status = await BatchesApi.getBatchStatus(batchId, headers).execute();
console.log("Batch status:", status.current_status);

// 5. Once complete, download the output JSONL and parse it into typed lines.
const outBlob = await FileApi.fileDownload(
  `${secretName}/${outputFolder}${batchId}/output.jsonl`,
  headers,
).execute();
const lines: BatchOutputLine[] = await parseBatchOutput(outBlob);
console.log("Parsed output lines:", lines.length);
if (lines.length > 0) {
  console.log(JSON.stringify(lines[0], null, 2));
}
