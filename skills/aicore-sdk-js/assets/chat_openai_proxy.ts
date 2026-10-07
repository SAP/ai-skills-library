/**
 * Install: npm install openai
 * Requires: LiteLLM proxy running locally — see references/FRAMEWORKS.md
 * Run:      npx tsx assets/js/chat_openai_proxy.ts
 *
 * Uses the standard openai npm package pointed at a LiteLLM proxy.
 * This pattern works with any framework that accepts an OpenAI-compatible API.
 *
 * Start the proxy first:
 *   pip install litellm
 *   litellm --config config.yaml   # see references/FRAMEWORKS.md for config.yaml
 *
 * Env vars:
 *   LITELLM_PROXY_URL  (default: http://localhost:4000)
 *   LITELLM_API_KEY    (any non-empty string for local proxy)
 */

import OpenAI from "openai";

const client = new OpenAI({
  baseURL: process.env.LITELLM_PROXY_URL ?? "http://localhost:4000",
  apiKey: process.env.LITELLM_API_KEY ?? "any",
});

const response = await client.chat.completions.create({
  model: "sap/gpt-4o-mini",
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "What is SAP AI Core?" },
  ],
  max_completion_tokens: 512,
});

console.log(response.choices[0].message.content);
