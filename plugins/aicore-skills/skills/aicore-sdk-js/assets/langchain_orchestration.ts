/**
 * Install: npm install @sap-ai-sdk/langchain @langchain/core
 *          bun add @sap-ai-sdk/langchain @langchain/core
 * Run:     npx tsx assets/langchain_orchestration.ts
 *          bun run assets/langchain_orchestration.ts
 *
 * LangChain chat and streaming via OrchestrationClient from @sap-ai-sdk/langchain.
 * Supports orchestration features: content filtering, data masking, grounding.
 * Credentials: run 'aicore configure' or see references/SETUP.md
 */

import { OrchestrationClient } from "@sap-ai-sdk/langchain";
import type { LangChainOrchestrationModuleConfig } from "@sap-ai-sdk/langchain";

const config: LangChainOrchestrationModuleConfig = {
  promptTemplating: {
    model: {
      name: "anthropic--claude-4.5-haiku",
      params: { temperature: 0.7, max_tokens: 512 },
    },
  },
};

const client = new OrchestrationClient(config);

const messages = [
  { role: "user", content: "Explain SAP AI Core in three sentences." },
];

// --- Non-streaming ---
const response = await client.invoke(messages);
console.log("Response:", response.content);

// --- Streaming ---
process.stdout.write("\nStreaming response:\n\n");

const stream = await client.stream(messages);
for await (const chunk of stream) {
  process.stdout.write(chunk.content as string);
}

process.stdout.write("\n");
