# Install: uv add sap-ai-sdk-gen
# Run:     uv run assets/orchestration_filtering.py
#
# Orchestration with Azure content safety filtering (input + output).
# Requires a running orchestration deployment.
# Create one first with the aicore-lifecycle-management skill:
#   uv run skills/aicore-lifecycle-management/scripts/create_deployment.py --configuration-id <config-id> --wait
#
# Credentials: configure with the aicore-admin-resources skill (aicore configure or AICORE_* env vars).

from gen_ai_hub.orchestration.service import OrchestrationService
from gen_ai_hub.orchestration.models.config import OrchestrationConfig
from gen_ai_hub.orchestration.models.llm import LLM
from gen_ai_hub.orchestration.models.template import Template, TemplateValue
from gen_ai_hub.orchestration.models.message import SystemMessage, UserMessage
from gen_ai_hub.orchestration.models.content_filtering import ContentFiltering
from gen_ai_hub.orchestration.models.azure_content_filter import AzureContentFilter

# Azure content safety filter — thresholds: 0 (allow all) to 6 (block most)
# Categories: Hate, Violence, Sexual, SelfHarm
input_filter = AzureContentFilter(Hate=2, Violence=2, Sexual=2, SelfHarm=2)
output_filter = AzureContentFilter(Hate=2, Violence=2, Sexual=2, SelfHarm=2)

config = OrchestrationConfig(
    template=Template(
        messages=[
            SystemMessage("You are a helpful assistant."),
            UserMessage("{{?user_query}}"),
        ]
    ),
    llm=LLM(
        name="gpt-4o-mini",
        version="latest",
        parameters={"temperature": 0.3, "max_completion_tokens": 512},
    ),
    filtering=ContentFiltering(
        input_filter=input_filter,
        output_filter=output_filter,
    ),
)

svc = OrchestrationService(config=config)

template_values = [TemplateValue(name="user_query", value="Explain cloud computing.")]

# ---------------------------------------------------------------------------
# Non-streaming
# ---------------------------------------------------------------------------
try:
    result = svc.run(template_values=template_values)
    print(result.orchestration_result.choices[0].message.content)
except Exception as e:
    # Content filtering may raise if thresholds are exceeded
    print(f"Request blocked or failed: {e}")

# ---------------------------------------------------------------------------
# Streaming
# ---------------------------------------------------------------------------
print("\nStreaming response:\n")
try:
    for chunk in svc.stream(template_values=template_values):
        delta = chunk.orchestration_result.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
    print()
except Exception as e:
    print(f"\nRequest blocked or failed: {e}")
