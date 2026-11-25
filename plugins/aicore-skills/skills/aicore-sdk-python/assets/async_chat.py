# File:    skills/aicore-sdk-python/assets/async_chat.py
# Install: uv add sap-ai-sdk-gen
# Run:     uv run assets/async_chat.py
#
# Async chat with concurrent inference calls.
# Credentials: run 'aicore configure' or see aicore-admin-resources/references/SETUP.md
# See: https://help.sap.com/docs/sap-ai-core/generative-ai/quick-start

import asyncio
from gen_ai_hub.proxy.native.openai import AsyncOpenAI

client = AsyncOpenAI()

MESSAGES = [
    {"role": "system", "content": "You are a helpful assistant. Be concise."},
    {"role": "user", "content": "What is SAP AI Core?"},
]

# Non-streaming — concurrent requests
async def ask(question: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Be concise."},
            {"role": "user", "content": question},
        ],
        max_completion_tokens=256,
    )
    return response.choices[0].message.content or ""


async def run_concurrent():
    questions = [
        ("What is SAP AI Core?", "Q1"),
        ("What is SAP BTP?", "Q2"),
        ("What is the difference between AI Core and AI Launchpad?", "Q3"),
    ]
    tasks = [ask(q) for q, _ in questions]
    answers = await asyncio.gather(*tasks)
    for (question, label), answer in zip(questions, answers):
        print(f"[{label}] {question}")
        print(f"       {answer}\n")


# Streaming
async def ask_stream(question: str) -> None:
    print(f"User: {question}")
    print("Assistant: ", end="", flush=True)
    async with await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Be concise."},
            {"role": "user", "content": question},
        ],
        max_completion_tokens=256,
        stream=True,
    ) as stream:
        async for chunk in stream:
            delta = chunk.choices[0].delta.content if chunk.choices else None
            if delta:
                print(delta, end="", flush=True)
    print()


async def main():
    print("=== Concurrent non-streaming ===\n")
    await run_concurrent()

    print("=== Streaming ===\n")
    await ask_stream("What are the main use cases for SAP AI Core?")


asyncio.run(main())
