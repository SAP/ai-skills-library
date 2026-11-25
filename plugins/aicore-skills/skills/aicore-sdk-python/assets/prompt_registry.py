# File:    skills/aicore-sdk-python/assets/prompt_registry.py
# Install: uv add sap-ai-sdk-gen
# Run:     uv run assets/prompt_registry.py
#
# Prompt Registry — create, retrieve, modify, fill and inspect versioned prompt templates.
# Credentials: run 'aicore configure' or see aicore-admin-resources/references/SETUP.md
# See: https://help.sap.com/docs/sap-ai-core/generative-ai/quick-start

from gen_ai_hub.proxy import get_proxy_client
from gen_ai_hub.prompt_registry import PromptTemplateClient
from gen_ai_hub.prompt_registry import PromptTemplateSpec, PromptTemplate


# Initialize Client
proxy_client = get_proxy_client(proxy_version="gen-ai-hub")
prompt_registry_client = PromptTemplateClient(proxy_client=proxy_client)

# Create a Prompt Template
prompt_template_spec = PromptTemplateSpec(
    template=[PromptTemplate(role='system', content='You are a helpful assistant.')]
)
template_id = prompt_registry_client.create_prompt_template(
    scenario='MyScenario',
    name='prompt_template_name',
    version='1.0.0',
    prompt_template_spec=prompt_template_spec
).id

print(f"Created Prompt Template with ID: {template_id}")

# Retrieve a Prompt Template
response = prompt_registry_client.get_prompt_template_by_id(template_id)
print(response.spec.template)

# Modify a Prompt Template
prompt_template_spec = PromptTemplateSpec(
    template=[PromptTemplate(role='system', content='You are a helpful assistant for {{ ?topic }}.')]
)
response = prompt_registry_client.create_prompt_template(
    scenario='MyScenario',
    name='prompt_template_name',
    version='1.0.0',
    prompt_template_spec=prompt_template_spec
)
input_template_id = response.id
print(response.message)

# Prompt Template History
response = prompt_registry_client.get_prompt_template_history(
    scenario='MyScenario', name='prompt_template_name', version='1.0.0'
)
print(response.model_dump_json())

# Fill a Prompt Template
response = prompt_registry_client.fill_prompt_template_by_id(
    template_id=input_template_id, input_params={"topic": "chemistry"}
)
print(response.parsed_prompt)
