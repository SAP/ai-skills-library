# File:    skills/aicore-sdk-python/assets/multi_turn.py
# Install: uv add sap-ai-sdk-gen
# Run:     uv run assets/multi_turn.py
#
# Multi-turn conversation — maintains history across messages.
# Credentials: run 'aicore configure' or see aicore-admin-resources/references/SETUP.md
# See: https://help.sap.com/docs/sap-ai-core/generative-ai/quick-start

from gen_ai_hub.proxy.native.openai import OpenAI

client = OpenAI()

# Non-streaming multi-turn
conversation = [{"role": "system", "content": "You are a helpful assistant."}]


def chat(user_message: str) -> str:
    conversation.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation,
        max_completion_tokens=512,
    )
    assistant_reply = response.choices[0].message.content or ""
    conversation.append({"role": "assistant", "content": assistant_reply})
    return assistant_reply


print("User: What is SAP AI Core?")
print(f"Assistant: {chat('What is SAP AI Core?')}\n")

print("User: What are its main use cases?")
print(f"Assistant: {chat('What are its main use cases?')}\n")

# Streaming multi-turn
stream_conversation = [{"role": "system", "content": "You are a helpful assistant."}]


def chat_stream(user_message: str) -> None:
    stream_conversation.append({"role": "user", "content": user_message})
    print(f"User: {user_message}")
    print("Assistant: ", end="", flush=True)

    collected = []
    for chunk in client.chat.completions.create(
        model="gpt-4o-mini",
        messages=stream_conversation,
        max_completion_tokens=512,
        stream=True,
    ):
        delta = chunk.choices[0].delta.content if chunk.choices else None
        if delta:
            print(delta, end="", flush=True)
            collected.append(delta)

    print()
    stream_conversation.append({"role": "assistant", "content": "".join(collected)})


chat_stream("How does SAP AI Core compare to AWS SageMaker?")
print()
chat_stream("Which one would you recommend for SAP-native workloads?")
print()
