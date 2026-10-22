---
name: genai-hub-prompt-evaluation
description: >
  Run GenAI evaluations on SAP AI Core: benchmark LLMs and prompts against a test dataset using
  system-defined and custom (LLM-as-judge) metrics, then retrieve aggregate results. Supports all
  three evaluation types — prompt registry, orchestration registry, and grounding (RAG)
  orchestration registry.
  WHEN: user wants to evaluate or benchmark an LLM / prompt / orchestration config, run a GenAI
  evaluation, create or list evaluation metrics, define a custom LLM-as-a-judge metric, create a
  prompt template (prompt registry) or an orchestration-registry config (with or without grounding)
  for evaluation, create an evaluation configuration or execution, or fetch evaluation results /
  scores for an execution.
  DO NOT USE FOR: agent evaluation via the offline aeval service — use `aeval-offline-evaluation`;
  building a production orchestration/RAG pipeline for inference — use `genai-hub-orchestration`;
  generic executions, deployments, or artifacts unrelated to evaluation — use
  `aicore-lifecycle-management`; credentials, resource groups, or object stores — use
  `aicore-admin-resources`.
compatibility: Requires Python 3.11+, uv, sap-ai-sdk-core, and requests. /v2 is appended to AICORE_BASE_URL automatically if not present.
allowed-tools:
  - Read
  - Bash
  - WebFetch
---

## Step 0 — ask for credentials first (required)

Before running any other step, confirm the AI Core credentials are set. Invoke
`aicore-admin-resources` and run `check_setup.py`.

- If it succeeds, continue to the workflow.
- If it fails (missing variables, `invalid_client`, or bad credentials), **STOP and ask the user**
  to export the variables listed in **Environment variables** below. Do not continue, and do not
  look for credentials or workflow steps anywhere else (notebooks, other repos, workspace files) —
  this skill's `scripts/` are the only supported path.

---

## Rules

1. Run all scripts from this skill's root directory with `uv run scripts/<name>.py`.
2. Shared lifecycle/admin steps are handled by other skills — invoke them rather than reimplementing:
   object stores and resource groups → `aicore-admin-resources`; artifact registration, executions,
   execution status → `aicore-lifecycle-management`.
3. Never print or log credential values — scripts read them from the environment via the SDK.
4. The evaluation scenario ID is `genai-evaluations`. **Always use the executable ID
   `genai-evaluations-simplified` — hardcode it, do not use any version/user-suffixed variant**. A tenant may list many such custom-built
   images; ignore them. Only fall back to discovery (`aicore-lifecycle-management`
   `get_executables.py --scenario-id genai-evaluations`) if `genai-evaluations-simplified` is not
   present on the tenant at all.
5. Before creating a custom metric or prompt-registry config, list existing ones and reuse by
   name/scenario/version to avoid duplicates. `create_evaluation_metric.py` already does create-or-get.
6. Only fetch results (`get_evaluation_results.py`) once the execution status is `COMPLETED`
   (UNKNOWN → PENDING → RUNNING → COMPLETED). Check status by invoking `aicore-lifecycle-management`
   (`get_executions.py --execution-id <id>`).
7. If a dataset has no reference/ground-truth column, do not select metrics that require a reference.

---

## Environment variables

All scripts in this skill read credentials from the environment — never from CLI arguments.

### AI Core credentials (required for all scripts)

| Variable | Description | Notes |
|---|---|---|
| `AICORE_AUTH_URL` | OAuth token endpoint | Must end in `/oauth/token` |
| `AICORE_CLIENT_ID` | OAuth client ID | From BTP AI Core service key |
| `AICORE_CLIENT_SECRET` | OAuth client secret | From BTP AI Core service key |
| `AICORE_BASE_URL` | AI Core API base URL | `/v2` is appended automatically if not present |
| `AICORE_RESOURCE_GROUP` | Resource group to operate in | Default: `default` |

Source: BTP cockpit → your subaccount → Instances & Subscriptions → AI Core instance → Service Keys.

Set them once via `aicore configure` (saves to `~/.aicore/config.json`) or export each variable:

```bash
export AICORE_AUTH_URL=https://<subdomain>.authentication.<region>.hana.ondemand.com/oauth/token
export AICORE_CLIENT_ID=<client-id>
export AICORE_CLIENT_SECRET=<client-secret>
export AICORE_BASE_URL=https://api.ai.<region>.aws.ml.hana.ondemand.com
export AICORE_RESOURCE_GROUP=default
```

> **Shell syntax:** `AICORE_RESOURCE_GROUP='default'` — no space before `=`.

### Object-store credentials (required only for `download_evaluation_results.py`)

The per-row SQLite DB is downloaded directly from S3 — AI Core credentials are not used here.
Set the standard AWS SDK environment variables; the script uses boto3's credential chain directly:

| Variable | Description |
|---|---|
| `AWS_ACCESS_KEY_ID` | S3 access key ID |
| `AWS_SECRET_ACCESS_KEY` | S3 secret access key |

The bucket name is passed as `--bucket <name>` on the command line (not read from env).
Source: the same AWS credentials used when creating the object store secret in `aicore-admin-resources`.

---

## End-to-end workflow

The full runbook (with every command and how the pieces connect) is in
`references/WORKFLOW.md`. The high-level flow, and which skill owns each step:

| # | Step | Owner |
|---|------|-------|
| 1 | Register S3 object store secret (input source) | `aicore-admin-resources` `create_object_store.py` |
| 2 | Upload the dataset to the bucket | user — sample datasets in `data/` |
| 3 | Register the dataset folder as an artifact (with the prompt-evaluation label) | **this skill** `register_eval_artifact.py` |
| 4 | Ensure an orchestration deployment is running (for the deployment URL) | `aicore-lifecycle-management` + `genai-hub-orchestration` |
| 5 | Select system metrics / create custom metrics | **this skill** `list_evaluation_metrics.py`, `create_evaluation_metric.py` |
| 6 | Create the thing to evaluate (see **Evaluation types** below) | **this skill** `create_prompt_template.py` or `create_orchestration_registry_config.py` |
| 7 | Create the evaluation configuration | **this skill** `create_evaluation_configuration.py` |
| 8 | Start the execution | `aicore-lifecycle-management` `create_execution.py` |
| 9 | Poll status until COMPLETED | `aicore-lifecycle-management` `get_executions.py` |
| 10 | Retrieve aggregate results | **this skill** `get_evaluation_results.py` |
| 11 | (Optional) Download the raw SQLite DB for per-row analysis | **this skill** `download_evaluation_results.py` |

---

## Evaluation types

Choose one — it determines what you create in step 6 and which binding you pass to
`create_evaluation_configuration.py` in step 7:

| Type | What you evaluate | Create with | Config binding |
|------|-------------------|-------------|----------------|
| **Prompt registry** | A prompt template + one or more models | `create_prompt_template.py` | `--prompt-template-id` (+ `--models`) |
| **Orchestration registry** | An orchestration config (prompt_templating) | `create_orchestration_registry_config.py` | `--orchestration-registry-ids` |
| **Grounding orchestration registry** | An orchestration config with a grounding (RAG) module | `create_orchestration_registry_config.py` (grounding template) | `--orchestration-registry-ids` |

All three share steps 1–5 and 7–11; only step 6 and the config binding differ. The grounding type
additionally needs grounding prerequisites (grounding-enabled resource group, grounding secret,
document-grounding pipeline) — see `references/GROUNDING_SETUP.md`.

---

## Evaluation metrics

```bash
# Discover system metric names (use these verbatim in --metrics later)
uv run scripts/list_evaluation_metrics.py --kind system
uv run scripts/list_evaluation_metrics.py --kind system --name "Pointwise"

# List your custom metrics and their IDs
uv run scripts/list_evaluation_metrics.py --kind custom --json | jq '.[] | {id, name}'

# Create (or reuse) custom LLM-as-a-judge metrics from a definition file (idempotent).
# See templates/custom-metric.json. Prints the resulting metric ID(s).
uv run scripts/create_evaluation_metric.py --file templates/custom-metric.json
```

Common system metrics: `Pointwise Conciseness`, `Pointwise Answer Relevance`,
`Pointwise Instruction Following`, `Pointwise Correctness`, `Pointwise RAG Context Relevance`,
`Pointwise RAG Groundedness`, `Pointwise RAG Context Precision`, `Pointwise RAG Completeness`.
Confirm the exact names for the tenant with `list_evaluation_metrics.py --kind system`.

---

## Step 6 — create the thing to evaluate

### Type 1 — Prompt registry

Create (or reuse) a prompt template in the Prompt Registry, then benchmark it across models.

```bash
uv run scripts/list_prompt_templates.py --scenario genai-evaluations          # reuse?
uv run scripts/create_prompt_template.py --file templates/prompt-template.json \
  --name prompt-registry-eval-demo --version 1.0.0
```

Returns a prompt template ID → pass as `--prompt-template-id`, together with `--models`
(e.g. `"gpt-4o:2024-05-13"`) in step 7.

### Type 2 — Orchestration registry

Create (or reuse) an orchestration config (prompt_templating, no grounding).

```bash
uv run scripts/list_orchestration_registry_configs.py --scenario genai-evaluations   # reuse?
uv run scripts/create_orchestration_registry_config.py \
  --file templates/orchestration-registry-config.json \
  --name genai-eval-prompt-config --version 0.0.1
```

Returns a config ID → pass as `--orchestration-registry-ids` in step 7.

### Type 3 — Grounding orchestration registry (RAG)

First complete the grounding prerequisites in `references/GROUNDING_SETUP.md`, then create the
config from the grounding template (adds a `grounding` module):

```bash
uv run scripts/create_orchestration_registry_config.py \
  --file templates/orchestration-registry-grounding-config.json \
  --name genai-eval-grounding-config --version 0.0.1
```

Returns a config ID → pass as `--orchestration-registry-ids` in step 7. Select RAG metrics
(`Pointwise RAG Groundedness`, `Pointwise RAG Context Relevance`, …) for this type.

---

## Step 7 — evaluation configuration + execution

Use the executable ID `genai-evaluations-simplified` directly (per Rule 4 — do not use a
version/user-suffixed variant). Then create the configuration with this skill's script:

```bash
# 2a. Create the evaluation configuration — ORCHESTRATION / GROUNDING types
uv run scripts/create_evaluation_configuration.py \
  --executable-id genai-evaluations-simplified \
  --dataset-artifact-id <artifact-id> \
  --test-dataset-path testdata/full_dataset.csv \
  --test-dataset-type csv \
  --metrics "Pointwise Correctness,Pointwise Answer Relevance" \
  --orchestration-registry-ids <registry-config-id> \
  --orchestration-deployment-url <orchestration-deployment-url> \
  --repetitions 1

# 2b. Create the evaluation configuration — PROMPT REGISTRY type
uv run scripts/create_evaluation_configuration.py \
  --executable-id genai-evaluations-simplified \
  --dataset-artifact-id <artifact-id> \
  --test-dataset-path testdata/full_dataset.csv \
  --metrics "Pointwise Correctness" \
  --prompt-template-id <prompt-template-id> \
  --models "gpt-4o:2024-05-13" \
  --orchestration-deployment-url <orchestration-deployment-url>
```

Custom metric IDs (from `create_evaluation_metric.py`) can be appended to `--metrics`. Limit rows
with `--test-row-count N`. Map variables to dataset columns with
`--variable-mapping '{"all_metrics/reference":"data/ground_truth"}'`.

Then hand off to `aicore-lifecycle-management` for the run itself:
- **Start the execution** — `create_execution.py --configuration-id <config-id>`
- **Poll until COMPLETED** — `get_executions.py --execution-id <execution-id>`
  (status goes UNKNOWN → PENDING → RUNNING → COMPLETED)

---

## Results

```bash
# Aggregate metrics per model/prompt run (only once COMPLETED)
uv run scripts/get_evaluation_results.py --execution-id <execution-id>
uv run scripts/get_evaluation_results.py --execution-id <execution-id> --json
```

For instance-level results (per-row scores, latency, logs), download the SQLite DB
(`<execution-id>/tmp/results.db`) from object storage. Set `AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY` in the environment, then pass the bucket name via `--bucket`:

```bash
uv run scripts/download_evaluation_results.py --execution-id <execution-id> --bucket <bucket> --show-tables
```

For the full download + local inspection recipe (table schema, querying per-row metrics), see
`references/RESULTS_ANALYSIS.md`.

---

## Handoffs

- **Credentials, resource group, or object store secret not set up?** → invoke `aicore-admin-resources`
- **Need to start/stop/inspect executions, discover executables, or manage deployments?** → invoke `aicore-lifecycle-management`
- **Need a running orchestration deployment or want to design the prompt/RAG pipeline?** → invoke `genai-hub-orchestration`
- **Setting up grounding (RAG) for the grounding type?** → see `references/GROUNDING_SETUP.md` (uses `aicore-admin-resources` for the resource group and secret)
- **Evaluating an agent (not a prompt/LLM) via the offline service?** → invoke `aeval-offline-evaluation`

---

## When to Load Reference Files

| Trigger | Load |
| ------- | ---- |
| Running the full end-to-end evaluation, or unsure which command comes next | `references/WORKFLOW.md` |
| Setting up grounding (RAG) prerequisites for the grounding orchestration type | `references/GROUNDING_SETUP.md` |
| Downloading and inspecting the raw per-row results (SQLite DB from object storage) | `references/RESULTS_ANALYSIS.md` |
