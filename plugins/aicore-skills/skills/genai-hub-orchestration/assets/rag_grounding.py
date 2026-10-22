# Install: uv add sap-ai-sdk-gen
# Run:     uv run assets/rag_grounding.py
#
# RAG via the orchestration document grounding module.
# Requires:
#   1. A running orchestration deployment — create one with the aicore-lifecycle-management skill
#      (see its "Orchestration deployment" section).
#   2. A document grounding data repository configured in AI Core with indexed documents
#
# Credentials: configure with the aicore-admin-resources skill (aicore configure or AICORE_* env vars).

from gen_ai_hub.orchestration.service import OrchestrationService
from gen_ai_hub.orchestration.models.config import OrchestrationConfig
from gen_ai_hub.orchestration.models.llm import LLM
from gen_ai_hub.orchestration.models.template import Template, TemplateValue
from gen_ai_hub.orchestration.models.message import SystemMessage, UserMessage
from gen_ai_hub.orchestration.models.document_grounding import (
    GroundingModule,
    DocumentGrounding,
    DocumentGroundingFilter,
    GroundingType,
    DataRepositoryType,
)

# Replace with your actual data repository ID from AI Core
DATA_REPOSITORY_ID = "<your-data-repository-id>"

config = OrchestrationConfig(
    template=Template(
        messages=[
            SystemMessage(
                "You are a helpful assistant. Answer questions using only the provided context. "
                "If the answer is not in the context, say so."
            ),
            UserMessage("Context:\n{{?groundingOutput}}\n\nQuestion: {{?groundingInput}}"),
        ]
    ),
    llm=LLM(
        name="gpt-4o-mini",
        version="latest",
        parameters={"temperature": 0.0, "max_completion_tokens": 1024},
    ),
    grounding=GroundingModule(
        type=GroundingType.DOCUMENT_GROUNDING_SERVICE.value,
        config=DocumentGrounding(
            input_params=["groundingInput"],
            output_param="groundingOutput",
            filters=[
                DocumentGroundingFilter(
                    id=DATA_REPOSITORY_ID,
                    data_repository_type=DataRepositoryType.VECTOR.value,
                )
            ],
        ),
    ),
)

svc = OrchestrationService(config=config)

template_values = [
    TemplateValue(name="groundingInput", value="What are the main features of SAP AI Core?"),
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
