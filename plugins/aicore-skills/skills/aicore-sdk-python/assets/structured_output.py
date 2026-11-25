# File:    skills/aicore-sdk-python/assets/structured_output.py
# Install: uv add "sap-ai-sdk-gen>=6.9.0" pydantic
# Run:     uv run assets/structured_output.py
#
# Structured model outputs — JSON conforming to a Pydantic schema (chat.parse + responses.parse).
# Credentials: run 'aicore configure' or see aicore-admin-resources/references/SETUP.md
# See: https://help.sap.com/docs/sap-ai-core/generative-ai/quick-start

from pydantic import BaseModel
from gen_ai_hub.proxy.native.openai import chat, responses


class Person(BaseModel):
    name: str
    age: int


# ---------------------------------------------------------------------------
# Structured output via chat.completions.parse
# ---------------------------------------------------------------------------
response = chat.completions.parse(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Tell me about John Doe, aged 30."}],
    response_format=Person,
)
person = response.choices[0].message.parsed  # Fully typed Person
print(person)

# ---------------------------------------------------------------------------
# Structured output via responses.parse  (requires sap-ai-sdk-gen>=6.9.0)
# ---------------------------------------------------------------------------
response = responses.parse(
    model="gpt-5",
    input="Tell me about John Doe aged 30.",
    text_format=Person,
)
print(response.output_parsed)  # Fully typed Person