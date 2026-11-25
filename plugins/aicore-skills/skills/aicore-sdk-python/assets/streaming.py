# File:    skills/aicore-sdk-python/assets/streaming.py
# Install: uv add sap-ai-sdk-gen[all]
# Run:     uv run assets/streaming.py
#
# Streaming across providers — native SDKs (OpenAI, Google GenAI, Anthropic via
# Amazon, Amazon Bedrock) plus the unified LangChain init_llm interface.
# Verbatim from docs-python examples streaming.mdx (native + LangChain).
# Credentials: run 'aicore configure' or see aicore-admin-resources/references/SETUP.md
# See: https://help.sap.com/docs/sap-ai-core/generative-ai/quick-start

import json
from gen_ai_hub.proxy import get_proxy_client
from gen_ai_hub.proxy.native.openai import chat
from gen_ai_hub.proxy.native.google_genai import Client
from gen_ai_hub.proxy.native.amazon import Session
from gen_ai_hub.proxy.langchain import init_llm
from google.genai.types import GenerateContentConfig

def stream_openai(prompt, model_name='gpt-4o-mini'):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    kwargs = dict(model_name=model_name, messages=messages, max_tokens=500, stream=True)
    stream = chat.completions.create(**kwargs)
    for chunk in stream:
        if chunk.choices:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end='')

stream_openai("Why is the sky blue?")

def stream_genai(prompt, model_name='gemini-3.5-flash'):
    proxy_client = get_proxy_client('gen-ai-hub')
    client = Client(proxy_client=proxy_client)
    response = client.models.generate_content_stream(
        model=model_name,
        contents=prompt,
        config=GenerateContentConfig(max_output_tokens=2500),
    )
    for chunk in response:
        print(chunk.text, end='')

stream_genai("Why is the sky blue?")

def stream_claude(prompt, model_name='anthropic--claude-4.5-haiku'):
    bedrock = Session().client(model_name=model_name)
    body = json.dumps({
        "max_tokens": 500,
        "messages": [{"role": "user", "content": prompt}],
        "anthropic_version": "bedrock-2023-05-31"
    })
    response = bedrock.invoke_model_with_response_stream(body=body)
    stream = response.get("body")
    for event in stream:
        chunk = json.loads(event["chunk"]["bytes"])
        if chunk["type"] == "content_block_delta":
            print(chunk["delta"].get("text", ""), end="")

stream_claude("Why is the sky blue?")

def stream_bedrock(prompt, model_name='amazon--nova-pro'):
    bedrock = Session().client(model_name=model_name)
    body = json.dumps({
        "schemaVersion": "messages-v1",
        "messages": [{"role": "user", "content": [{"text": prompt}]}],
        "system": [{"text": "Act as a creative writing assistant."}],
        "inferenceConfig": {"maxTokens": 500, "topP": 0.9, "topK": 20, "temperature": 0.7},
    })
    response = bedrock.invoke_model_with_response_stream(body=body)
    stream = response.get("body")
    chunk_count = 0
    answer = ""
    if stream:
        for event in stream:
            chunk = event.get("chunk")
            if chunk:
                chunk_json = json.loads(chunk.get("bytes").decode())
                content_block_delta = chunk_json.get("contentBlockDelta")
                if content_block_delta:
                    chunk_count += 1
                    answer += content_block_delta.get("delta").get("text")
        print(f"Total chunks: {chunk_count}")
        print("Final answer:", answer)
    else:
        print("No response stream received.")

stream_bedrock("Why is the sky blue?")

def stream_langchain(prompt, model_name):
    llm = init_llm(model_name=model_name, max_tokens=500, proxy_client=get_proxy_client())
    for chunk in llm.stream(prompt):
        print(chunk.content, end='')

stream_langchain("How do airplanes stay in the air?", model_name='gpt-4o-mini')
stream_langchain("How do airplanes stay in the air?", model_name='gemini-3.5-flash')
