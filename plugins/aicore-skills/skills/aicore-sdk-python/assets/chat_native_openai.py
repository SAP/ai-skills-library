# File:    skills/aicore-sdk-python/assets/chat_native_openai.py
# Install: uv add sap-ai-sdk-gen
# Run:     uv run assets/chat_native_openai.py
#
# Native OpenAI-compatible proxy — chat completions (non-streaming + streaming).
# Credentials: run 'aicore configure' or see aicore-admin-resources/references/SETUP.md
# See: https://help.sap.com/docs/sap-ai-core/generative-ai/quick-start

from gen_ai_hub.proxy.native.openai import OpenAI

client = OpenAI()

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is SAP AI Core?"},
]

# ---------------------------------------------------------------------------
# Non-streaming
# ---------------------------------------------------------------------------
response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
print(response.choices[0].message.content)

# ---------------------------------------------------------------------------
# Streaming
# ---------------------------------------------------------------------------
print("\nStreaming response:\n")
stream = client.chat.completions.create(model="gpt-4o-mini", messages=messages, stream=True)
for chunk in stream:
    delta = chunk.choices[0].delta.content if chunk.choices else None
    if delta:
        print(delta, end="", flush=True)
print()