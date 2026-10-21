# Document Grounding (RAG) with Orchestration

The SAP AI Core Orchestration service supports retrieval-augmented generation (RAG) via the **Document Grounding module**. It retrieves relevant content from indexed document repositories and injects it into the LLM context before inference — all within a single orchestration request.

## Prerequisites

1. **Running orchestration deployment** — use `aicore-lifecycle-management` to create one if needed.
2. **Document repository with indexed documents** — configured in AI Core Launchpad or via the Document Grounding API. You need the `DATA_REPOSITORY_ID` from this setup.

## Python Imports

```python
from gen_ai_hub.orchestration.models.document_grounding import (
    GroundingModule,
    DocumentGrounding,
    DocumentGroundingFilter,
    GroundingType,
    DataRepositoryType,
)
from gen_ai_hub.document_grounding.clients.retrieval_api_client import RetrievalAPIClient
from gen_ai_hub.document_grounding.clients.vector_api_client import VectorAPIClient
```

## GroundingModule Configuration

```python
grounding = GroundingModule(
    type=GroundingType.DOCUMENT_GROUNDING_SERVICE.value,
    config=DocumentGrounding(
        input_params=["groundingInput"],   # template variable to use as the query
        output_param="groundingOutput",    # variable that receives retrieved context
        filters=[
            DocumentGroundingFilter(
                id="<your-data-repository-id>",
                data_repository_type=DataRepositoryType.VECTOR.value,
            )
        ],
    ),
)
```

Add it to your `OrchestrationConfig`:

```python
from gen_ai_hub.orchestration.models.config import OrchestrationConfig

config = OrchestrationConfig(
    template=template,
    llm=llm,
    grounding=grounding,   # ← add here
)
```

The template variable referenced in `input_params` (e.g. `groundingInput`) must appear in the template as `{{?groundingInput}}`. The orchestration service replaces it with the retrieved context before passing to the LLM.

## Full Working Example

See `assets/rag_grounding.py` for a complete runnable example including streaming.

## Retrieval API Client (direct access)

For querying document repositories outside of an orchestration pipeline:

```python
from gen_ai_hub.document_grounding.clients.retrieval_api_client import RetrievalAPIClient

client = RetrievalAPIClient()
results = client.query(
    collection_id="<your-data-repository-id>",
    query="What are the main features of SAP AI Core?",
    top_k=5,
)
for doc in results.documents:
    print(doc.content)
```

## Vector API Client (manage collections)

```python
from gen_ai_hub.document_grounding.clients.vector_api_client import VectorAPIClient

client = VectorAPIClient()
collections = client.list_collections()
```

## Common Issues

| Issue                                | Fix                                                                  |
| ------------------------------------ | -------------------------------------------------------------------- |
| `DATA_REPOSITORY_ID` not found       | Create a data repository in AI Core Launchpad and copy the ID        |
| Grounding returns empty context      | Check that documents are indexed and the query matches their content |
| `orchestration deployment not found` | Create one first with `aicore-lifecycle-management`                           |
