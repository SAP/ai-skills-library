/**
 * Install: npm install @sap-ai-sdk/langchain @langchain/core
 *          bun add @sap-ai-sdk/langchain @langchain/core
 * Run:     npx tsx assets/langchain_openai.ts
 *          bun run assets/langchain_openai.ts
 *
 * LangChain chat and streaming via AzureOpenAiChatClient from @sap-ai-sdk/langchain.
 * No LiteLLM proxy needed — the SDK handles AI Core auth natively.
 * Credentials: run 'aicore configure' or see references/SETUP.md
 */

import { AzureOpenAiChatClient } from "@sap-ai-sdk/langchain";
import { HumanMessage, SystemMessage } from "@langchain/core/messages";

const client = new AzureOpenAiChatClient({
  modelName: "gpt-4o-mini",
  temperature: 0.7,
  max_tokens: 512,
});

const messages = [
  new SystemMessage("You are a helpful assistant."),
  new HumanMessage("Explain SAP AI Core in three sentences."),
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
