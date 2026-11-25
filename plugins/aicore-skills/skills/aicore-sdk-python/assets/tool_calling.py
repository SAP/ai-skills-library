# File:    skills/aicore-sdk-python/assets/tool_calling.py
# Install: uv add sap-ai-sdk-gen
# Run:     uv run assets/tool_calling.py
#
# Tool/function calling — model decides when to call a defined tool.
# Credentials: run 'aicore configure' or see aicore-admin-resources/references/SETUP.md
# See: https://help.sap.com/docs/sap-ai-core/generative-ai/quick-start

import json
from gen_ai_hub.proxy.native.openai import OpenAI

client = OpenAI()

# Define tools using the OpenAI function schema
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name, e.g. Berlin"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"], "default": "celsius"},
                },
                "required": ["city"],
            },
        },
    }
]

messages = [{"role": "user", "content": "What's the weather in Berlin right now?"}]

# First call — model may request a tool
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)

msg = response.choices[0].message

if msg.tool_calls:
    # Handle tool call
    for tool_call in msg.tool_calls:
        args = json.loads(tool_call.function.arguments)
        print(f"Tool called: {tool_call.function.name}({args})")

        # Simulate tool execution
        tool_result = json.dumps({"temperature": "18°C", "condition": "Partly cloudy"})

        # Append assistant message and tool result
        messages.append(msg)
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": tool_result,
        })

    # Second call — stream the final answer with tool result
    print("Assistant: ", end="", flush=True)
    for chunk in client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        stream=True,
    ):
        delta = chunk.choices[0].delta.content if chunk.choices else None
        if delta:
            print(delta, end="", flush=True)
    print()
else:
    # Model answered directly without a tool call
    print(msg.content)
