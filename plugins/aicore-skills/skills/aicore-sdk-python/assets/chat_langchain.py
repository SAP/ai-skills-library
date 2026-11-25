# File:    skills/aicore-sdk-python/assets/chat_langchain.py
# Install: uv add sap-ai-sdk-gen[all]
# Run:     uv run assets/chat_langchain.py
#
# LangChain via the GenAI Hub proxy — ChatOpenAI chat model plus the unified
# init_llm streaming interface. Importing gen_ai_hub.proxy.langchain eagerly loads
# every provider (OpenAI, Google GenAI, Amazon Bedrock), so the [all] extra
# (botocore, langchain_aws, langchain_google_genai) is required.
# Source: docs-python examples gen-ai-hub.mdx (LangChain Chat Model) + streaming.mdx (LangChain).
# Credentials: run 'aicore configure' or see aicore-admin-resources/references/SETUP.md
# See: https://help.sap.com/docs/sap-ai-core/generative-ai/quick-start

from langchain_core.prompts import (
    AIMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from gen_ai_hub.proxy import get_proxy_client
from gen_ai_hub.proxy.langchain import ChatOpenAI, init_llm

proxy_client = get_proxy_client('gen-ai-hub')
chat_llm = ChatOpenAI(proxy_model_name='gpt-4o-mini', proxy_client=proxy_client)

template = 'You are a helpful assistant that translates english to pirate.'
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
example_human = HumanMessagePromptTemplate.from_template('Hi')
example_ai = AIMessagePromptTemplate.from_template('Ahoy!')
human_message_prompt = HumanMessagePromptTemplate.from_template('{text}')
chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, example_human, example_ai, human_message_prompt])

chain = chat_prompt | chat_llm
response = chain.invoke({'text': 'I love planking.'})
print(response.content)

# Streaming — unified init_llm interface (works for any supported model)
def stream_langchain(prompt, model_name):
    llm = init_llm(model_name=model_name, max_tokens=500, proxy_client=proxy_client)
    for chunk in llm.stream(prompt):
        print(chunk.content, end='')

stream_langchain("How do airplanes stay in the air?", model_name='gpt-4o-mini')
