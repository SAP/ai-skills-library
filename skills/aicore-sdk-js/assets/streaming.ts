/**
 * Install: npm install @sap-ai-sdk/orchestration
 * Run:     npx tsx assets/streaming.ts
 *
 * Streaming chat using @sap-ai-sdk/orchestration — prints delta tokens as they arrive.
 * The stream response is async-iterable; helper methods expose finish reason and token usage.
 * Credentials: run 'aicore configure' or see references/SETUP.md
 */

import { OrchestrationClient } from "@sap-ai-sdk/orchestration";

const client = new OrchestrationClient({
  promptTemplating: {
    model: {
      name: "anthropic--claude-4.5-haiku",
      params: { temperature: 0.3, max_tokens: 512 },
    },
  },
});

process.stdout.write("Streaming response:\n\n");

const response = await client.stream({
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "Explain SAP BTP in three sentences." },
  ],
});

// The response is async-iterable — iterate to receive delta chunks.
for await (const chunk of response.stream) {
  const delta = chunk.getDeltaContent();
  if (delta) {
    process.stdout.write(delta);
  }
}

// After the stream is consumed, helper methods expose the final metadata.
process.stdout.write("\n\nDone.\n");
console.log("Finish reason:", response.getFinishReason());
console.log("Token usage:", JSON.stringify(response.getTokenUsage()));
