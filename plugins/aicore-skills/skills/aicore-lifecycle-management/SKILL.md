---
name: aicore-lifecycle-management
description: >
  Manage SAP AI Core lifecycle resources: scenarios, executables, configurations, and deployments.
  WHEN: user wants to list or inspect scenarios or executables, create or list configurations,
  create or list or stop or delete or patch deployments, get deployment logs, or remove duplicate
  LLM deployments.
  DO NOT USE FOR: listing foundation models or getting inference examples — use
  `genai-hub-foundation-models`; managing resource groups, secrets, or GitOps resources — use
  `aicore-admin-resources`.
compatibility: Requires Python 3.11+, uv, and sap-ai-sdk-core.
---

## Rules

1. Run all scripts from the skill root directory with `uv run scripts/<name>.py`.
2. Never print or log credential values — the SDK reads them from the environment.
3. Scripts that delete or mutate state require `--confirm`. Always pass it explicitly; never bypass it.
4. When the user does not specify a resource group, omit `--resource-group` so the SDK uses its configured default.
5. For LLM deployments: the scenario ID, executable ID, and model parameter names come from `genai-hub-foundation-models` — invoke it first if those values are unknown.
6. Deployment configuration naming convention: use `{executable_id}--{model_name}` for LLM deployments (e.g. `azure-openai--gpt-4o-mini`). Before creating a configuration, check whether one with that name already exists via `get_configurations.py --scenario-id <id>` and reuse it to avoid duplicates.

---

## List / Inspect Scenarios

```bash
# List all scenarios
uv run scripts/get_scenarios.py

# Inspect a specific scenario and its versions
uv run scripts/get_scenarios.py --scenario-id <id>
uv run scripts/get_scenarios.py --scenario-id <id> --response-format detailed

# JSON output for piping
uv run scripts/get_scenarios.py --json
```

---

## List Executables

```bash
# List executables for a scenario
uv run scripts/get_executables.py --scenario-id <id>

# Inspect a specific executable (includes parameters and input artifacts)
uv run scripts/get_executables.py --scenario-id <id> --executable-id <id>
uv run scripts/get_executables.py --scenario-id <id> --executable-id <id> --response-format detailed

# JSON output
uv run scripts/get_executables.py --scenario-id <id> --json
```

Parameters are only returned when inspecting a single executable (`--executable-id`). The list view returns id, name, and description only.

---

## Configurations

```bash
# List configurations
uv run scripts/get_configurations.py
uv run scripts/get_configurations.py --scenario-id <id>
uv run scripts/get_configurations.py --response-format detailed
uv run scripts/get_configurations.py --json

# Inspect a specific configuration
uv run scripts/get_configurations.py --configuration-id <id>

# Create a configuration (binds parameters to an executable)
uv run scripts/create_configuration.py \
  --name my-config \
  --scenario-id <id> \
  --executable-id <id> \
  --param modelName=gpt-4o \
  --param temperature=0.7
```

If a deployment fails or stays PENDING after several minutes, verify parameter names and values against the executable's declared parameters:

```bash
uv run scripts/get_executables.py --scenario-id <id> --executable-id <id> --response-format detailed
```

---

## Deployments

Deployments serve inference endpoints. The standard flow is: create (or reuse) a configuration, then create a deployment from it.

### Configuration naming convention

Always check whether a matching configuration already exists before creating one, to avoid duplicates:

```bash
# Check existing configurations before creating
uv run scripts/get_configurations.py --scenario-id <scenario-id> --json | jq '.[] | select(.name == "<expected-name>")'
```

Naming convention:
- LLM: `{executable_id}--{model_name}` — e.g. `azure-openai--gpt-4o-mini`
- Orchestration: `orchestration`
- Custom: choose a descriptive name

### LLM deployment (from genai-hub-foundation-models handoff)

```bash
# 1. Create configuration (skip if one with this name already exists):
uv run scripts/create_configuration.py \
  --name azure-openai--gpt-4o-mini \
  --scenario-id foundation-models \
  --executable-id azure-openai \
  --param modelName=gpt-4o-mini \
  --param modelVersion=latest

# 2. Deploy:
uv run scripts/create_deployment.py --configuration-id <config-id> --wait
```

### Orchestration deployment

```bash
# 1. Create configuration (skip if "orchestration" config already exists):
uv run scripts/create_configuration.py \
  --name orchestration \
  --scenario-id orchestration \
  --executable-id orchestration

# 2. Deploy:
uv run scripts/create_deployment.py --configuration-id <config-id> --wait --timeout 600
```

### List and inspect deployments

```bash
# List all deployments
uv run scripts/get_deployments.py

# Filter by status or scenario or executable
uv run scripts/get_deployments.py --status RUNNING
uv run scripts/get_deployments.py --scenario orchestration
uv run scripts/get_deployments.py --executable-id azure-openai --status RUNNING
uv run scripts/get_deployments.py --executable-id azure-openai --status RUNNING --json

# Inspect one deployment
uv run scripts/get_deployments.py --deployment-id <id>
uv run scripts/get_deployments.py --deployment-id <id> --response-format detailed
uv run scripts/get_deployments.py --deployment-id <id> --json
```

### Stop, patch, delete, logs

```bash
# Stop a deployment
uv run scripts/stop_deployment.py --deployment-id <id> --confirm
uv run scripts/stop_deployment.py --deployment-id <id> --confirm --wait

# Patch (swap configuration on a running deployment)
uv run scripts/patch_deployment.py --deployment-id <id> --configuration-id <new-config-id>

# Delete (must be STOPPED or DEAD first)
uv run scripts/delete_deployment.py --deployment-id <id> --confirm
# Stop and delete in one step:
uv run scripts/delete_deployment.py --deployment-id <id> --confirm --auto-stop

# Deployment logs
uv run scripts/get_deployment_logs.py --deployment-id <id>
uv run scripts/get_deployment_logs.py --deployment-id <id> --tail 50
uv run scripts/get_deployment_logs.py --deployment-id <id> --order asc
uv run scripts/get_deployment_logs.py --deployment-id <id> --json

# Remove duplicate LLM deployments (only affects LLM deployments with a model name)
uv run scripts/dedup_deployments.py --dry-run
uv run scripts/dedup_deployments.py
```

---

## Handoffs

- **Need a Bearer token or credential setup?** → invoke `aicore-admin-resources`
- **Need executable ID, model name, or model capabilities?** → invoke `genai-hub-foundation-models`
- **Want to list available models or providers?** → invoke `genai-hub-foundation-models`
