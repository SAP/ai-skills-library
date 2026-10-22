# GenAI evaluation — end-to-end runbook

Run this skill's own commands (`uv run scripts/…`) from the `prompt-evaluation` skill root. Shared steps are
delegated to sibling skills by name — when a step says **invoke `<skill>`**, self-direct to that
skill's instructions and run the named script there (don't hardcode a path to it, so the flow still
works when this skill is installed on its own). All AI Core credentials come from the environment
(the SDK resolves them); `/v2` is appended to `AICORE_BASE_URL` automatically if not present.

**Step 0 — credentials first:** before anything else, invoke `aicore-admin-resources` and run its
`check_setup.py` to confirm credentials and the resource group. If it fails, **STOP and ask the
user** to export the AI Core environment variables — do not continue and do not source credentials
or workflow steps from notebooks or other files.

## 1. Register the S3 object store secret

The evaluation service reads inputs from an object store registered under a name.

→ Invoke `aicore-admin-resources` to create the object store secret (`create_object_store.py`).
Prefer its browser form so credentials never touch the command line; the S3 fields are name, type
`s3`, bucket, region, endpoint (`s3-<region>.amazonaws.com`), and the AWS access key / secret.

## 2. Upload the dataset to the bucket

The dataset must be a CSV, JSON, or JSONL file whose column names match the template variables used
in step 6. Sample datasets are included in the `data/` directory:

| File | Columns | Use with |
|---|---|---|
| `data/sample_dataset.csv` | `question`, `ground_truth` | Prompt registry / orchestration registry types |
| `data/sample_dataset_rag.csv` | `question`, `answer`, `reference` | Grounding orchestration registry (RAG) type |

Upload your chosen file to the bucket registered in step 1 using your preferred S3-compatible
tooling (AWS CLI, SAP Object Store console, or any S3 client library). Place it under a prefix, e.g.
`genaiEvaluation/testdata/sample_dataset.csv`.

## 3. Register the dataset folder as an artifact

The evaluation service discovers dataset artifacts by the label `ext.ai.sap.com/prompt-evaluation=true`.
This skill owns that registration via `register_eval_artifact.py`.

**How the `ai://` URL works:**
`ai://<object-store-secret-name>/<path-in-bucket>` — the secret name is the name you gave when
creating the object store secret in step 1 (e.g. `my-eval-store`). The path is the folder prefix
in the bucket. The artifact points at the **folder**, not the file itself — the file path is given
separately as `--test-dataset-path` in step 7.

```bash
uv run scripts/register_eval_artifact.py \
  --name my-eval-data \
  --url ai://<object-store-secret-name>/genaiEvaluation \
  --json
# → prints {"id": "<artifact-id>", ...}   ← copy this ID for step 7
```

The `ext.ai.sap.com/prompt-evaluation=true` label is added automatically. `--scenario-id` defaults
to `genai-evaluations`.

## 4. Ensure an orchestration deployment is running

The evaluation calls an orchestration deployment to generate the responses it scores.

→ Invoke `aicore-lifecycle-management`: reuse a running deployment
(`get_deployments.py --scenario orchestration --status RUNNING`), or create one — a configuration
(`create_configuration.py --name orchestration --scenario-id orchestration --executable-id orchestration`)
then `create_deployment.py --configuration-id <config-id> --wait`. The returned `deploymentUrl` is
the `--orchestration-deployment-url` for step 7. (For designing the pipeline, invoke
`genai-hub-orchestration`.)

## 5. Choose metrics

```bash
# System metric names — copy them verbatim
uv run scripts/list_evaluation_metrics.py --kind system

# Optional: create custom LLM-as-a-judge metrics (idempotent). Prints metric IDs.
uv run scripts/create_evaluation_metric.py --file templates/custom-metric.json
```

If the dataset has no reference column, avoid reference-based metrics.

## 6. Create the thing to evaluate (pick ONE type)

The evaluation runs a prompt/config against the dataset. There are three types — choose one and
carry its ID into step 7.

### Type 1 — Prompt registry

```bash
uv run scripts/list_prompt_templates.py --scenario genai-evaluations           # reuse?
uv run scripts/create_prompt_template.py \
  --file templates/prompt-template.json --name prompt-registry-eval-demo --version 1.0.0
```

Carry the prompt template ID into step 7 as `--prompt-template-id` (with `--models`).

### Type 2 — Orchestration registry

```bash
uv run scripts/list_orchestration_registry_configs.py --scenario genai-evaluations  # reuse?
uv run scripts/create_orchestration_registry_config.py \
  --file templates/orchestration-registry-config.json \
  --name genai-eval-prompt-config --version 0.0.1
```

Carry the config ID into step 7 as `--orchestration-registry-ids`.

### Type 3 — Grounding orchestration registry (RAG)

First complete the grounding prerequisites in `GROUNDING_SETUP.md` (grounding-enabled resource
group, grounding secret, document-grounding pipeline), then:

```bash
uv run scripts/create_orchestration_registry_config.py \
  --file templates/orchestration-registry-grounding-config.json \
  --name genai-eval-grounding-config --version 0.0.1
```

Carry the config ID into step 7 as `--orchestration-registry-ids`, and select RAG metrics.

## 7. Create the evaluation configuration

Use the executable ID `genai-evaluations-simplified` directly — do not use a version/user-suffixed
variant; a tenant may list many such custom
builds, ignore them. Only if `genai-evaluations-simplified` is absent on the tenant, fall back to
discovery via `aicore-lifecycle-management` (`get_executables.py --scenario-id genai-evaluations`).
Then create the configuration with this skill's script:

```bash
uv run scripts/create_evaluation_configuration.py \
  --executable-id genai-evaluations-simplified \
  --dataset-artifact-id <artifact-id-from-step-3> \
  --test-dataset-path testdata/full_dataset.csv \
  --test-dataset-type csv \
  --metrics "Pointwise Correctness,Pointwise Answer Relevance" \
  --orchestration-registry-ids <config-id-from-step-6> \
  --orchestration-deployment-url <deployment-url-from-step-4> \
  --repetitions 1 \
  --json
```

Bind step 6's output according to the type you chose:
- Prompt registry → `--prompt-template-id <id>` (plus `--models "gpt-4o:2024-05-13"`)
- Orchestration / grounding registry → `--orchestration-registry-ids <id>`

Notes:
- Append custom metric IDs to `--metrics` (comma-separated) alongside system metric names.
- Limit the run to the first N rows with `--test-row-count N`.
- Map variables to dataset columns with `--variable-mapping '{"all_metrics/reference":"data/ground_truth"}'`.
- Extra bindings: `--param KEY=VALUE`; extra input artifacts: `--artifact KEY=ARTIFACT_ID`.

Record the configuration ID.

## 8. Start the execution

→ Invoke `aicore-lifecycle-management` and run `create_execution.py --configuration-id <config-id>`.

## 9. Poll until COMPLETED

→ Invoke `aicore-lifecycle-management` and run `get_executions.py --execution-id <execution-id>`.
Status progresses UNKNOWN → PENDING → RUNNING → COMPLETED. `targetStatus` is always COMPLETED
(the intended final state) — watch `status`, not `targetStatus`.

## 10. Retrieve aggregate results

```bash
uv run scripts/get_evaluation_results.py --execution-id <execution-id>
uv run scripts/get_evaluation_results.py --execution-id <execution-id> --json
```

## 11. (Optional) Per-row analysis

Download the SQLite DB from the output artifact and inspect it locally:

```bash
uv run scripts/download_evaluation_results.py --execution-id <execution-id> --bucket <bucket> --show-tables
```

Needs object-store (AWS) credentials in the environment (not the AI Core ones). See
`RESULTS_ANALYSIS.md` for the schema and querying recipe.

## Cleanup

→ Invoke `aicore-lifecycle-management` and run
`delete_execution.py --execution-id <execution-id> --confirm --auto-stop`.
