# Install: uv add sap-ai-sdk-gen
# Run:     uv run assets/orchestration_basic.py
#
# Orchestration service with a prompt template — requires a running orchestration deployment.
# Create one first with the aicore-lifecycle-management skill (see its "Orchestration deployment" section).
#
# Credentials: configure with the aicore-admin-resources skill (aicore configure or AICORE_* env vars).

from gen_ai_hub.orchestration.service import OrchestrationService
from gen_ai_hub.orchestration.models.config import OrchestrationConfig
from gen_ai_hub.orchestration.models.llm import LLM
from gen_ai_hub.orchestration.models.template import Template, TemplateValue
from gen_ai_hub.orchestration.models.message import SystemMessage, UserMessage

config = OrchestrationConfig(
    template=Template(
        messages=[
            SystemMessage("You are a helpful assistant specialised in {{?topic}}."),
            UserMessage("{{?user_query}}"),
        ]
    ),
    llm=LLM(
        name="gpt-4o-mini",
        version="latest",
        parameters={"temperature": 0.3, "max_completion_tokens": 512},
    ),
)

svc = OrchestrationService(config=config)

template_values = [
    TemplateValue(name="topic", value="SAP BTP"),
    TemplateValue(name="user_query", value="What are the main components of SAP BTP?"),
]

# ---------------------------------------------------------------------------
# Non-streaming
# ---------------------------------------------------------------------------
result = svc.run(template_values=template_values)
print(result.orchestration_result.choices[0].message.content)

# ---------------------------------------------------------------------------
# Streaming
# ---------------------------------------------------------------------------
print("\nStreaming response:\n")
for chunk in svc.stream(template_values=template_values):
    delta = chunk.orchestration_result.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
print()
