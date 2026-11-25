# File:    skills/aicore-sdk-python/assets/embeddings.py
# Install: uv add sap-ai-sdk-gen[amazon]
# Run:     uv run assets/embeddings.py
#
# Text embeddings via the GenAI Hub native proxy — OpenAI and Amazon Bedrock.
# Verbatim from docs-python examples gen-ai-hub.mdx (Embeddings section).
# Credentials: run 'aicore configure' or see aicore-admin-resources/references/SETUP.md
# See: https://help.sap.com/docs/sap-ai-core/generative-ai/quick-start

import json
from gen_ai_hub.proxy.native.openai import embeddings
from gen_ai_hub.proxy.native.amazon import Session
# OpenAI Embeddings
response = embeddings.create(
    input="Every decoding is another encoding.",
    model_name="text-embedding-ada-002"
)
print(response.data)
# with base64 encoding
response = embeddings.create(
    input="Every decoding is another encoding.",
    model_name="text-embedding-ada-002",
    encoding_format='base64'
)
print(response.data)
# Amazon Bedrock Embeddings
bedrock = Session().client(model_name="amazon--titan-embed-text")
body = json.dumps({"inputText": "Please recommend books with a theme similar to the movie 'Inception'."})
response = bedrock.invoke_model(body=body)
response_body = json.loads(response.get("body").read())
print(response_body)
