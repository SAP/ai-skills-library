# Grounding (RAG) prerequisites for the grounding-orchestration evaluation type

The **grounding orchestration registry** evaluation type runs a prompt template whose orchestration
config includes a `grounding` (document_grounding_service) module — the model answers using chunks
retrieved from a document repository. The repository can be either:

- **SAP Help Portal (`help.sap.com`)** — a public, built-in repository. This is what the shipped
  template (`templates/orchestration-registry-grounding-config.json`) uses, and it needs **no
  object store, secret, or pipeline** — only a grounding-enabled resource group (section 1).
- **Your own documents in S3** — needs a grounding secret and a document-grounding pipeline, and
  the template's grounding filter must target `S3` (section 3).

> Document grounding as a concept (grounding module config, RAG pipeline design, data repositories)
> is owned by the `genai-hub-orchestration` skill — invoke it for grounding pipeline design or
> `GroundingModule` details. This page covers only what the **evaluation** flow additionally needs.

## 1. A grounding-enabled resource group

The resource group must carry the label `ext.ai.sap.com/document-grounding=true`.

→ Invoke `aicore-admin-resources` to create it (`create_resource_group.py --id rag-eval
--label ext.ai.sap.com/document-grounding=true`). If the group already exists without the label,
patch or recreate it via the same skill.

## 2. Default path — SAP Help Portal (`help.sap.com`)

Nothing more is required. The shipped template already filters the public `help.sap.com`
repository:

```json
"filters": [{ "id": "helpRepo", "data_repositories": ["*"],
              "data_repository_type": "help.sap.com" }]
```

Skip to section 4, create the orchestration config, and select RAG metrics for the evaluation
configuration.

## 3. Optional path — your own documents in S3

Use this only if you want to ground on your own documents instead of `help.sap.com`.

1. **Grounding secret** — → invoke `aicore-admin-resources` `create_secret.py` (browser form keeps
   credentials off the CLI) with:

   ```
   name:   groundingsecret
   labels: ext.ai.sap.com/document-grounding=true, ext.ai.sap.com/documentRepositoryType=S3
   data:   url, authentication, access_key_id, bucket, host, region, secret_access_key, username
   ```

2. **Document-grounding pipeline** — this connects the secret to the grounding service so documents
   are chunked and retrievable. Pipeline creation is owned by `genai-hub-orchestration` — invoke it
   to register the pipeline. It is a single call to `POST /lm/document-grounding/pipelines` (with the
   `AI-Resource-Group` header and a bearer token from `aicore-admin-resources` `get_token.py`) whose
   body is:

   ```json
   {"type": "S3", "configuration": {"destination": "groundingsecret"}}
   ```

   Confirm the repository is registered (chunking has started) by listing
   `GET /lm/document-grounding/retrieval/dataRepositories` for the same resource group.

3. **Point the template at S3** — in `templates/orchestration-registry-grounding-config.json`,
   change the grounding filter's `data_repository_type` from `help.sap.com` to `S3` so the
   evaluation retrieves from your documents.

## 4. Create the grounding orchestration config

```bash
uv run scripts/create_orchestration_registry_config.py \
  --file templates/orchestration-registry-grounding-config.json \
  --name genai-eval-grounding-config --version 0.0.1
```

The returned config ID is the `--orchestration-registry-ids` input to
`create_evaluation_configuration.py` — the rest of the flow is identical to the plain
orchestration-registry type. RAG metrics (e.g. `Pointwise RAG Groundedness`,
`Pointwise RAG Context Relevance`) require the grounding context, so select them for this type.
