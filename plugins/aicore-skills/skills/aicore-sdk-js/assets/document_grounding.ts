/**
 * Install: npm install @sap-ai-sdk/document-grounding
 *          bun add @sap-ai-sdk/document-grounding
 * Run:     npx tsx document_grounding.ts   (or: bun run document_grounding.ts)
 *
 * Full RAG lifecycle with @sap-ai-sdk/document-grounding: create a vector
 * collection, add documents, run a retrieval search, then clean up.
 * Credentials: run 'aicore configure' or see references/SETUP.md
 */

import {
  VectorApi,
  RetrievalApi,
  PipelinesApi,
} from "@sap-ai-sdk/document-grounding";
import type {
  GetPipelineStatus,
  RetrievalSearchResults,
} from "@sap-ai-sdk/document-grounding";

const resourceGroup = { "AI-Resource-Group": "ai-sdk-js-e2e" };

// --- Create collection (executeRaw + parse id from Location header) ---
const res = await VectorApi.createCollection(
  {
    title: "ai-sdk-js-e2e",
    embeddingConfig: { modelName: "text-embedding-3-small" },
    metadata: [],
  },
  resourceGroup,
).executeRaw();
const collectionId = (res.headers.location as string).split("/").at(-2)!;
console.log("Created collection:", collectionId);

// --- Add documents (each with chunks + metadata) ---
await VectorApi.createDocuments(
  collectionId,
  {
    documents: [
      {
        metadata: [],
        chunks: [
          {
            content: "SAP AI Core runs generative-AI and ML workloads on SAP BTP.",
            metadata: [{ key: "context", value: ["sap-ai-sdk-js"] }],
          },
        ],
      },
    ],
  },
  resourceGroup,
).execute();
console.log("Documents added to collection.");

// --- Retrieval search over the vector data repositories ---
const query = "What does SAP AI Core do?";
const searchResults: RetrievalSearchResults = await RetrievalApi.search(
  {
    query,
    filters: [
      {
        id: "my-filter",
        searchConfiguration: { maxChunkCount: 10 },
        dataRepositories: ["*"],
        dataRepositoryType: "vector",
      },
    ],
  },
  resourceGroup,
).execute();
console.log("Search results:", JSON.stringify(searchResults, null, 2));

// --- (Optional) inspect a pipeline's ingestion status ---
const pipelineId = process.env.PIPELINE_ID;
if (pipelineId) {
  const status: GetPipelineStatus = await PipelinesApi.getPipelineStatus(
    pipelineId,
    resourceGroup,
  ).execute();
  console.log("Pipeline status:", status);
}

// --- Clean up ---
await VectorApi.deleteCollectionById(collectionId, resourceGroup).execute();
console.log("Deleted collection:", collectionId);
