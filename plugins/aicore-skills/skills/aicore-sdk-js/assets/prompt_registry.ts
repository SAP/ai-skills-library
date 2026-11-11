// Install: npm install @sap-ai-sdk/prompt-registry
// Run:     npx tsx prompt_registry.ts   (or: bun run prompt_registry.ts)
// Purpose: Create/update and then delete a managed, versioned prompt template
//          via the SAP AI Core Prompt Registry.
// Credentials: run 'aicore configure' or see references/SETUP.md

import { PromptTemplatesApi } from "@sap-ai-sdk/prompt-registry";
import type {
  PromptTemplateDeleteResponse,
  PromptTemplatePostResponse,
} from "@sap-ai-sdk/prompt-registry";

const name = "ai-sdk-js-demo-template";
const scenario = "ai-sdk-js-demo";

// Create or update a versioned prompt template. The fluent request ends with .execute().
const created: PromptTemplatePostResponse =
  await PromptTemplatesApi.createUpdatePromptTemplate(
    {
      name,
      scenario,
      version: "0.0.1",
      spec: { template: [{ content: "Hello, world!", role: "user" }] },
    },
    { "AI-Resource-Group-Scope": "true", "AI-Resource-Group": "ai-sdk-js-e2e" },
  ).execute();

console.log("Created/updated prompt template:", created);

// The id returned from the create/update response identifies the template to delete.
const id = created.id;

const deleted: PromptTemplateDeleteResponse =
  await PromptTemplatesApi.deletePromptTemplate(id, {
    "AI-Resource-Group-Scope": "true",
    "AI-Resource-Group": "ai-sdk-js-e2e",
  }).execute();

console.log("Deleted prompt template:", deleted);
