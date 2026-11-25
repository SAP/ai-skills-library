# File:    skills/aicore-sdk-python/assets/responses_api.py
# Install: uv add "sap-ai-sdk-gen>=6.9.0"
# Run:     uv run assets/responses_api.py
#
# OpenAI Responses API via the gen_ai_hub native proxy.
# Credentials: run 'aicore configure' or see aicore-admin-resources/references/SETUP.md
# See: https://help.sap.com/docs/sap-ai-core/generative-ai/quick-start

from gen_ai_hub.proxy.native.openai import responses

# ---------------------------------------------------------------------------
# Non-streaming
# ---------------------------------------------------------------------------
response = responses.create(
    model="gpt-5",
    instructions="You are a helpful assistant that answers concisely.",
    input="What is SAP AI Core?",
)
print(response.output_text)

# ---------------------------------------------------------------------------
# Streaming
# ---------------------------------------------------------------------------
print("\nStreaming response:\n")
with responses.stream(
    model="gpt-5",
    instructions="You are a helpful assistant that answers concisely.",
    input="List three key benefits of SAP AI Core.",
) as stream:
    for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)
print()
