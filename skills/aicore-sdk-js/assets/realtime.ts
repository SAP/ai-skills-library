// Install: npm install @sap-ai-sdk/openai openai ws
// Run:     npx tsx realtime.ts   (or: bun run realtime.ts)
// Purpose: Real-time speech/text conversation via SAP AI Core using the
//          OpenAI Realtime WebSocket API (gpt-realtime model).
// Credentials: run 'aicore configure' or see references/SETUP.md

import { SapOpenAiRealtimeWs } from "@sap-ai-sdk/openai/realtime";

const client = await SapOpenAiRealtimeWs.createClient("gpt-realtime");

// Configure the session for text-in / text-out (swap output_modalities to
// ['audio'] and add an audio block for speech-to-speech use cases).
client.send({
  type: "session.update",
  session: {
    output_modalities: ["text"],
    instructions: "You are a helpful assistant. Reply concisely.",
  },
});

// ─── Send a text message and request a response ──────────────────────────────

client.send({
  type: "conversation.item.create",
  item: {
    type: "message",
    role: "user",
    content: [{ type: "input_text", text: "What is SAP AI Core in one sentence?" }],
  },
});

client.send({ type: "response.create" });

// ─── Stream the text response delta-by-delta ─────────────────────────────────

client.on("response.output_text.delta", (event) => {
  process.stdout.write(event.delta ?? "");
});

client.on("response.done", () => {
  console.log("\nResponse complete.");
  client.close();
});

client.on("error", (err) => {
  console.error("Realtime error:", err);
  client.close();
});
