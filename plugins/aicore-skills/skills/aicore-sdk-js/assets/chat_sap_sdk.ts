/**
 * Install: npm install @sap-ai-sdk/orchestration
 * Run:     npx tsx assets/chat_sap_sdk.ts
 *
 * Chat completion using @sap-ai-sdk/orchestration — the recommended JS/TS entry point.
 * Credentials: run 'aicore configure' or see references/SETUP.md
 */

import { OrchestrationClient } from "@sap-ai-sdk/orchestration";

const client = new OrchestrationClient({
  promptTemplating: {
    model: {
      name: "anthropic--claude-4.5-haiku", // replace with a model available in your resource group

      params: { temperature: 0.3, max_tokens: 512 },
    },
  },
});

const response = await client.chatCompletion({
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "What is SAP AI Core?" },
  ],
});

console.log(response.getContent());
console.log(response.getFinishReason());
console.log(JSON.stringify(response.getTokenUsage()));

// Alternative: use promptTemplating.prompt.template with {{?placeholder}} values
// when the template is defined server-side or reused across many calls:
//
// const clientWithTemplate = new OrchestrationClient({
//   promptTemplating: {
//     prompt: {
//       template: [
//         { role: "system", content: "You are a helpful assistant." },
//         { role: "user", content: "{{?user_query}}" },
//       ],
//     },
//     model: { name: "anthropic--claude-4.5-haiku", params: { temperature: 0.3 } },
//   },
// });
// const r = await clientWithTemplate.chatCompletion({ placeholderValues: { user_query: "Hello" } });
