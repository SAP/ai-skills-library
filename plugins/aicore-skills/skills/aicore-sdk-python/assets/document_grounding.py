# File:    skills/aicore-sdk-python/assets/document_grounding.py
# Install: uv add sap-ai-sdk-gen
# Run:     uv run assets/document_grounding.py
#
# Document Grounding — Pipeline, Vector and Retrieval APIs.
# Verbatim from docs-python examples document-grounding2.mdx. Replace the
# <PIPELINE_ID> / <EXECUTION_ID> / <DOCUMENT_ID> / <COLLECTION_ID> /
# <DATA_REPOSITORY_ID> / <KEY> / <VALUE> placeholders with real values before running.
# Credentials: run 'aicore configure' or see aicore-admin-resources/references/SETUP.md
# See: https://help.sap.com/docs/sap-ai-core/generative-ai/quick-start

from gen_ai_hub.proxy import get_proxy_client
from gen_ai_hub.document_grounding.client import PipelineAPIClient, VectorAPIClient, RetrievalAPIClient
from gen_ai_hub.document_grounding.models.pipeline import (
    SearchPipelineRequest, DataRepositoryMetadataItem, ManualPipelineTrigger,
)
from gen_ai_hub.document_grounding.models.vector import (
    CollectionCreateRequest, EmbeddingConfig,
    DocumentsCreateRequest, TextOnlyBaseChunk, BaseDocument, VectorKeyValueListPair,
    TextSearchRequest, VectorSearchFilter, VectorSearchConfiguration,
)
from gen_ai_hub.document_grounding.models.retrieval import (
    RetrievalSearchInput, RetrievalSearchFilter, RetrievalSearchConfiguration,
)

proxy_client = get_proxy_client(proxy_version='gen-ai-hub')

pipelines = PipelineAPIClient(proxy_client)
vector = VectorAPIClient(proxy_client)
retrieval = RetrievalAPIClient(proxy_client)

pipelines_list = pipelines.get_pipelines(top=10)
print(pipelines_list)

search_req = SearchPipelineRequest(
    dataRepositoryMetadata=[
        DataRepositoryMetadataItem(key='<KEY>', value=['<VALUE>'])
    ]
)
search_res = pipelines.search_pipelines(search_req)

pipeline_id = '<PIPELINE_ID>'

status = pipelines.get_pipeline_status(pipeline_id)

trigger_req = ManualPipelineTrigger(pipelineId=pipeline_id)
trigger_res = pipelines.trigger_pipeline(trigger_req)

execs = pipelines.get_pipeline_executions(pipeline_id, top=20)

execution_id = '<EXECUTION_ID>'
execution = pipelines.get_pipeline_execution_by_id(pipeline_id, execution_id)

docs = pipelines.get_execution_documents(pipeline_id, execution_id, top=50)

document_id = '<DOCUMENT_ID>'
doc = pipelines.get_execution_document_by_id(pipeline_id, execution_id, document_id)

pipeline_docs = pipelines.get_pipeline_documents(pipeline_id, top=50)
pipeline_doc = pipelines.get_pipeline_document_by_id(pipeline_id, document_id)

collections = vector.get_collections(top=50)

create_req = CollectionCreateRequest(
    title='My SDK Demo Collection',
    embeddingConfig=EmbeddingConfig(modelName='text-embedding-3-large'),
    metadata=[],
)
create_res = vector.create_collection(create_req)

collection_id = '<COLLECTION_ID>'

doc = BaseDocument(
    chunks=[TextOnlyBaseChunk(content='Hello from SDK Vector API', metadata=[])],
    metadata=[VectorKeyValueListPair(key='source', value=['notebook'])],
)

created = vector.create_documents(collection_id, DocumentsCreateRequest(documents=[doc]))
documents = vector.get_documents(collection_id, top=20)
document_id = documents.resources[0].id

vector.delete_document(collection_id, document_id)

search_req = TextSearchRequest(
    query='Hello',
    filters=[
        VectorSearchFilter(
            id='f1',
            collectionIds=[collection_id],
            configuration=VectorSearchConfiguration(maxChunkCount=5),
            documentMetadata=[],
            chunkMetadata=[],
            collectionMetadata=[],
        )
    ],
)
search_res = vector.search(search_req)

repos = retrieval.get_data_repositories(top=50)

repo_id = '<DATA_REPOSITORY_ID>'
repo = retrieval.get_data_repository_by_id(repo_id)

retrieval_req = RetrievalSearchInput(
    query='How to configure Document Grounding?',
    filters=[
        RetrievalSearchFilter(
            id='r1',
            dataRepositoryType='help.sap.com',
            searchConfiguration=RetrievalSearchConfiguration(maxChunkCount=5),
            dataRepositories=["*"]
        )
    ],
)
retrieval_res = retrieval.search(retrieval_req)
