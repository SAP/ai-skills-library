/**
 * Install: npm install @sap-ai-sdk/openai openai zod
 * Run:     npx tsx openai_native.ts   (or: bun run openai_native.ts)
 * Purpose: Use the native OpenAI SDK surface on Azure OpenAI via SAP AI Core
 *          (chat, streaming, structured parse, embeddings, Responses API).
 * Credentials: run 'aicore configure' or see references/SETUP.md
 */
import { SapOpenAi } from "@sap-ai-sdk/openai";
import { zodResponseFormat, zodTextFormat } from "openai/helpers/zod";
import { z } from "zod";

// Pre-configured client: deployment resolution, auth, and SAP headers handled
// automatically. The `model` field is omitted from request bodies — SAP AI Core
// routes via the deployment URL. createClient accepts either an options object
// ({ deployment: 'gpt-5.4' }) or a plain model-name string shorthand.
const client = await SapOpenAi.createClient({ deployment: "gpt-5.4" });

// --- Chat completion ---
const response = await client.chat.completions.create({
  messages: [{ role: "user", content: "What is the capital of France?" }],
});
console.log("Chat:", response.choices[0].message.content);

// --- Streaming ---
const client2 = await SapOpenAi.createClient("gpt-5.4-nano");
const stream = await client2.chat.completions.create({
  messages: [{ role: "user", content: "Write a short haiku about the sea." }],
  stream: true,
});
let streamed = "";
for await (const chunk of stream) {
  streamed += chunk.choices[0]?.delta?.content ?? "";
}
console.log("Streamed:", streamed);

// --- Structured parse (Zod schema) ---
const CapitalResponse = z.object({ capital: z.string() });
const parsed = await client.chat.completions.parse({
  messages: [{ role: "user", content: "What is the capital of Italy?" }],
  response_format: zodResponseFormat(CapitalResponse, "capital_response"),
});
console.log("Parsed capital:", parsed.choices[0].message.parsed?.capital);

// --- Embeddings ---
const emb = await SapOpenAi.createClient({ deployment: "text-embedding-3-small" });
const e = await emb.embeddings.create({ input: "Hello, world!" });
console.log("Embedding length:", e.data[0].embedding.length);

// --- Responses API ---
const r = await client.responses.create({
  instructions: "You are a helpful assistant.",
  input: "What is the capital of France?",
});
console.log("Response output:", r.output_text);

// Responses streaming (events discriminated by `type`)
const rStream = await client.responses.create({
  input: "Count to three.",
  stream: true,
});
for await (const event of rStream) {
  if (event.type === "response.output_text.delta") {
    process.stdout.write(event.delta);
  }
}
process.stdout.write("\n");

// Responses stateful follow-up (uses previous_response_id)
const followUp = await client.responses.create({
  previous_response_id: r.id,
  input: "And what about Germany?",
});
console.log("Follow-up output:", followUp.output_text);

// Responses structured parse
const rParsed = await client.responses.parse({
  input: "What is the capital of Spain?",
  text: { format: zodTextFormat(CapitalResponse, "capital_response") },
});
console.log("Response parsed capital:", rParsed.output_parsed?.capital);
