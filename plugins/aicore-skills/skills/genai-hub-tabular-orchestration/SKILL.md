---
name: genai-hub-tabular-orchestration
description: >
  Manage the SAP AI Core Context Registry — data destinations (HDL connections), tabular artifacts
  (CSV/Parquet/Delta files as queryable tables), and scenario configurations (named artifact bundles).
  Also interactively build and send tabular prediction requests using the SAP AI Core Tabular
  Prediction service (sap-rpt-1-small / sap-rpt-1-large).
  Use this skill whenever the user mentions context registry, data destinations, tabular artifacts,
  scenario configurations, TCR, HDL connections, or wants to register/list/delete structured data
  sources in SAP AI Core. Always use this skill for any tabular-orchestration / tcr API work, even if the user
  just asks "show me my data destinations" or "register this CSV as a tabular artifact".
  Also use for: SAP AI Core tabular prediction, sap-rpt prediction, "predict a column with sap-rpt", TCR row classification.
  NOT FOR general orchestration, generic ML prediction, or LLM pipelines — use `genai-hub-orchestration` for those.
  NOT FOR general classification/prediction requests unrelated to SAP AI Core TCR (e.g. "predict sales next quarter", "classify this text").
compatibility: Requires Python 3.11+, uv, sap-ai-sdk-core, and BTP CLI (btp) for registering
  HDL access. See references/SETUP.md for BTP CLI install and SSO login. All TCR API calls go to
  https://api.ai.{region}.ml.hana.ondemand.com/v2/tcr
allowed-tools: Bash, Read
---

## Rules

1. Run all scripts from the skill root with `uv run scripts/<name>.py`.
2. Never print or log credential values — the SDK reads from the environment.
3. Always verify TCR prerequisites (data destination → tabular artifact → scenario configuration) are in place before sending a prediction request.
4. `rows` and `columns` are mutually exclusive in a prediction request — never include both.
5. For credential or auth errors, invoke `aicore-admin-resources` first.
6. Mutating scripts require `--confirm`; always pass it explicitly for delete operations.
7. Omit `--resource-group` when the user doesn't specify one; the SDK default is used.
8. Before helping a user remove a subject pattern from a BTP service instance: run `btp get services/instance --id <id>` to retrieve the current configuration, show the user the exact entry or entries being removed and the full resulting `authorizations` payload that will be sent, and require explicit confirmation. Do not issue `btp update services/instance` until the user confirms.

---

## Concepts

The Context Registry (TCR) exposes structured data to AI Core scenarios through three layered resources:

```
Data Destination  →  Tabular Artifact  →  Scenario Configuration
(HDL connection)      (file + schema)       (named bundle of TAs)
```

- **Data Destination**: stores connection credentials for an HDL (HANA Data Lake) endpoint.
- **Tabular Artifact (TA)**: points to a specific file on a data destination, with schema metadata
  (CSN). Supports CSV, Parquet, and Delta formats. Schema can be provided inline (`DOCUMENT`),
  referenced via a path (`REFERENCE`), or auto-derived (`AUTO`).
- **Scenario Configuration**: a named, reusable list of tabular artifact names — consumed by
  AI Core scenarios at inference time.

All resources are scoped to a **resource group** (`AI-Resource-Group` header). Use the
`aicore-admin-resources` skill to verify credentials and get the active resource group first.

---

## Quick Start

```bash
# 1. Check setup
uv run scripts/check_setup.py    # from aicore-admin-resources, or verify env vars

# 2. List all three resource types
uv run scripts/list_data_destinations.py
uv run scripts/list_tabular_artifacts.py
uv run scripts/list_scenario_configs.py

# 3. Register a new HDL data destination
uv run scripts/create_data_destination.py --name my-hdl --host <hdl-hostname>

# 4. Register a tabular artifact (AUTO schema, CSV)
uv run scripts/create_tabular_artifact.py \
  --name customer-ta \
  --data-destination my-hdl \
  --path /data/customer.csv \
  --type CSV

# 5. Create a scenario configuration
uv run scripts/create_scenario_config.py \
  --name my-scenario \
  --tabular-artifacts customer-ta,orders-ta
```

---

## Data Destinations

A data destination stores the HDL hostname and credentials; the system validates the connection
on creation and stores the credentials securely.

**Before creating a data destination, ask the user for:**
1. **Name** — kebab-case, 1–127 chars (e.g. `my-hdl`)
2. **HDL hostname** — no `https://` prefix (e.g. `abc123.files.hdl.eu10.hanacloud.ondemand.com`)
3. *(Optional)* **Labels** — key=value pairs following `(ext|int).ai.sap.com/<suffix>` pattern
4. *(Optional)* **Description** — free-text description

```bash
uv run scripts/list_data_destinations.py               # list all
uv run scripts/list_data_destinations.py --json        # pipe-friendly JSON

uv run scripts/get_data_destination.py --name <name>   # get details of one destination
uv run scripts/get_data_destination.py --name <name> --json

uv run scripts/create_data_destination.py \
  --name <name> \
  --host <hdl-hostname>
  # hostname only — no https:// prefix, e.g. abc123.files.hdl.eu10.hanacloud.ondemand.com
  # optional: --labels ext.ai.sap.com/env=prod --description "Production HDL"

# Update labels (replaces the entire label set)
uv run scripts/patch_data_destination.py --name <name> --labels ext.ai.sap.com/env=prod
uv run scripts/patch_data_destination.py --name <name> --labels ext.ai.sap.com/env=prod ext.ai.sap.com/team=data

# Search by labels
uv run scripts/search_data_destinations.py --labels ext.ai.sap.com/env=prod
uv run scripts/search_data_destinations.py --labels ext.ai.sap.com/env=prod --json

uv run scripts/delete_data_destination.py --name <name> --confirm
# Note: deletes cascade to all tabular artifacts that reference this destination.
```

**Name constraints**: lowercase letters, numbers, hyphens; 1–127 chars; must start and end
with alphanumeric.

**Labels** follow the pattern `(ext|int).ai.sap.com/<suffix>` and are useful for filtering via
the search endpoint (see `references/API.md`).

**Required post-creation step — register subject patterns in HDL**: After
`create_data_destination.py` succeeds, the response includes one or more X.509 subject DNs
(`subjectPatterns`). These must be added as `authorizations` in the HDL Files service instance
configuration. Walk the user through the following steps:

**0. Verify BTP CLI login**

Before running any `btp` commands, ensure the BTP CLI is installed and you are logged in.
See `references/SETUP.md` for installation and login instructions.

**1. Find the HDL Files instance ID**

```bash
btp target --subaccount <subaccount-id>
btp list services/instance
```

Look for the instance whose name or type corresponds to the HDL Files service used by this data
destination.

**2. Read current instance configuration** (to preserve existing authorizations)

```bash
btp get services/instance --id <hdl-instance-id>
```

Note any existing `authorizations` entries — they must be included in the update.

**3. Add the subject pattern(s)**

```bash
btp update services/instance \
  --id <hdl-instance-id> \
  --parameters '{
    "data": {
      "fileContainer": {
        "authorizations": [
          {
            "pattern": "<subject-pattern-from-ai-core>",
            "rank": 1,
            "roles": ["user"]
          }
        ]
      }
    }
  }'
```

If AI Core returns multiple patterns, add one entry per pattern with sequential ranks. The
`authorizations` array **replaces** the existing one — always include all existing entries
alongside the new AI Core entry.

> **Do you have this role?** Requires **Subaccount Administrator** or **Service Administrator**
> on the subaccount that owns the HDL instance. If not, share the subject pattern(s) with your
> BTP admin and ask them to perform this step.

> **Propagation delay**: changes can take 1–2 minutes to take effect. If tabular artifact
> creation still returns 403 immediately after the update, wait and retry.

Do not proceed to tabular artifact creation until the user confirms the subject patterns have
been registered (or the BTP admin has done so).

---

## Tabular Artifacts

A tabular artifact registers a file on a data destination as a queryable virtual table. Three
schema definition modes:

| `definitionType` | When to use | What's required |
|------------------|-------------|-----------------|
| `AUTO` | Let the system derive schema from the file | just `definitionType: AUTO` |
| `DOCUMENT` | Provide column names and types inline — **recommended** | `--csn-columns col:cds.Type,...` |
| `REFERENCE` | Point to a CSN file on the data destination | path in `documentReference.path` |

**Before creating a tabular artifact, ask the user for:**
1. **Name** — kebab-case, 1–80 chars (e.g. `customer-data`)
2. **Data destination name** — must already exist (list with `list_data_destinations.py` if unsure)
3. **File path** — absolute path to the file on the HDL (e.g. `/data/customer.csv`)
4. **File type** — `CSV`, `PARQUET`, or `DELTA`
5. *(DOCUMENT mode only)* **Entity name** — a PascalCase label for the table (e.g. `Customer`)
6. *(DOCUMENT mode only)* **Column names** — exactly as they appear in the file header row
7. *(DOCUMENT mode only)* **Type for each column** — use the full `cds.*` type name (e.g. `cds.String`, `cds.Integer`)

Then use `--csn-columns` to pass them inline:

```bash
uv run scripts/list_tabular_artifacts.py               # list all
uv run scripts/list_tabular_artifacts.py --json

uv run scripts/get_tabular_artifact.py --name <name>   # get details of one artifact
uv run scripts/get_tabular_artifact.py --name <name> --json

# AUTO schema (simplest — works well for CSV with a header row)
uv run scripts/create_tabular_artifact.py \
  --name <name> \
  --data-destination <dd-name> \
  --path /data/file.csv \
  --type CSV

# DOCUMENT schema — supply column names and types explicitly
uv run scripts/create_tabular_artifact.py \
  --name <name> \
  --data-destination <dd-name> \
  --path /data/file.csv \
  --type CSV \
  --csn-columns "id:cds.Integer,name:cds.String,score:cds.Decimal,active:cds.Boolean" \
  --entity-name MyEntity

# REFERENCE schema (CSN file lives on the HDL)
uv run scripts/create_tabular_artifact.py \
  --name <name> \
  --data-destination <dd-name> \
  --path /data/file.parquet \
  --type PARQUET \
  --csn-reference /data/metadata/schema.json \
  --entity-name MyEntity

uv run scripts/delete_tabular_artifact.py --name <name> --confirm
# Deletion is async (202 Accepted); the artifact transitions to DELETING status.
```

**`--csn-columns` format**: comma-separated `name:cds.Type` pairs.
Supported types: `cds.UUID`, `cds.Boolean`, `cds.Integer`, `cds.Int16`, `cds.Int32`, `cds.Int64`,
`cds.UInt8`, `cds.Decimal`, `cds.Double`, `cds.Date`, `cds.Time`, `cds.DateTime`, `cds.Timestamp`,
`cds.String`, `cds.Binary`, `cds.LargeBinary`, `cds.LargeString`, `cds.Map`, `cds.Vector`.
Column names must match the file's header row exactly.

**Name constraints**: lowercase letters, numbers, hyphens; 1–80 chars; must start and end
with alphanumeric.

---

## Scenario Configurations

A scenario configuration is a named, stable list of tabular artifact names that AI Core
scenarios reference by name at inference time.

```bash
uv run scripts/list_scenario_configs.py
uv run scripts/list_scenario_configs.py --json

uv run scripts/get_scenario_config.py --name <name>    # get details of one config
uv run scripts/get_scenario_config.py --name <name> --json

uv run scripts/create_scenario_config.py \
  --name <name> \
  --tabular-artifacts ta1,ta2,ta3

# Update the TA list (replaces the entire list)
uv run scripts/patch_scenario_config.py \
  --name <name> \
  --tabular-artifacts ta1,ta2,ta3,ta4

uv run scripts/delete_scenario_config.py --name <name> --confirm
```

**Name constraints**: same as data destinations (lowercase, hyphens, 1–127 chars).

---

## Tabular Prediction (predict.py)

Use `predict.py` to send inference requests to a deployed tabular RPT model (`sap-rpt-1-small`
or `sap-rpt-1-large`). The model reads context rows from TCR and predicts values for query rows.

```bash
uv run scripts/predict.py --deployment-id <id> --body '<json>'
# optional: --json  --main-tenant <uuid>  --resource-group <rg>
```

### Rules

1. **TCR prerequisites must be in place** — a tabular artifact, a scenario configuration, and a
   data destination must all be registered (see sections above) before sending a prediction request.

2. **`rows` and `columns` are mutually exclusive** — never include both in the same request.

3. **Prediction target must contain `"[PREDICT]"`** — every entry in the target column for query
   rows must be the placeholder string `"[PREDICT]"`.

---

### Interactive Builder Flow

Work through these steps in order. Skip any step the user has already answered.

#### Step 1 — Confirm TCR prerequisites

Ask:
```
Before we proceed, please confirm you have already set up the following in TCR:
  ✓ Tabular artifact (context dataset uploaded)
  ✓ Scenario configuration (scenarioConfigName you want to use)
  ✓ Data destination

If any of these are missing, I can help you set them up first.
```

If not set up, help the user register them using the TCR scripts above, then return to the
prediction flow.

---

#### Step 2 — Resolve scenarioConfigName and deploymentId

```bash
uv run scripts/list_scenario_configs.py
```

**Get deployment ID** (tabular RPT deployments may not appear under known scenarios):
```bash
uv run ../aicore-lifecycle-management/scripts/get_deployments.py --status RUNNING
```

Once both are confirmed, also ask for these in a single message:

| Parameter | What to ask                                                                                          |
|-----------|------------------------------------------------------------------------------------------------------|
| `deploymentId` | "What is your deployment ID?"                                                                        |
| `modelName` | "Which model: `sap-rpt-1-small` (faster) or `sap-rpt-1-large` (more accurate)?"                      |
| Target column | "Which column do you want to predict?"                                                               |
| Task type | "Is this classification (predicts a category) or regression (predicts a number)? (optional — model can auto-detect)" |
| Data format | "How will you provide your data — as **columns** (object of arrays) or **rows** (array of objects)?" |

---

#### Step 3 — Collect and format data

Ask the user to provide their query data. Accept any format:
- Pasted table / CSV text
- JSON rows `[{...}, {...}]`
- Key-value pairs
- Spreadsheet-style

**Transform it according to the format chosen in Step 2:**

If **columns** format:

```json
"columns": {
  "Col A": ["val1", "val2", "val3"],
  "Col B": [10, 20, 30],
  "Target": ["[PREDICT]", "[PREDICT]", "[PREDICT]"]
}
```

If **rows** format:

```json
"rows" : [
  {"Col A": "val1", "Col B": 10, "Target": "[PREDICT]"},
  {"Col A": "val2", "Col B": 20, "Target": "[PREDICT]"}
]
```

Rules for formatting:
- Replace the target column values with `"[PREDICT]"` for all query rows
- Ensure all arrays have the same length
- Preserve column names exactly as the user provided them

Also ask whether the user has **context data** (rows with known answers for the model to learn
from). If yes, collect it and format it as `contextColumns` — keeping the real target values
(do **not** use `"[PREDICT]"` in context data).

---

#### Step 4 — Build `predictionConfig`

```json
"predictionConfig": {
  "targetColumns": [
    {
      "name": "<target column name>",
      "predictionPlaceholder": "[PREDICT]",
      "taskType": "<classification | regression>"
    }
  ]
}
```
---

#### Step 5 — Build `contextSelectionConfig`

Ask the user to choose how context rows should be sampled from the data destination and how many to include.:
```
How should context rows be sampled?
  A) random    — default, good general purpose
  B) heuristic — scoring-based, finds similar rows
  C) none      — take from HEAD or TAIL of the table
How many context rows? (default: 50)
```
Based on selection, refer to the `contextSelectionConfig` section in `references/PREDICT.md` to build the JSON object. If the user chooses heuristic sampling, ask for or confirm the unique row ID column required as `indexColumn`. Give the user the option if they want to customise the `strategyConfig`, otherwise use sensible defaults.

---

#### Step 6 — Assemble and send

Show the user the complete assembled JSON body, then run:

```bash
uv run scripts/predict.py \
  --deployment-id <deploymentId> \
  --body '<assembled-json>'
```

---

## Common Errors

### TCR / Context Registry

| Error | Likely cause | Fix |
|-------|-------------|-----|
| `401 Unauthorized` | Invalid token / credentials | Re-run `aicore configure` |
| `404 Not Found` | Wrong name or resource group | Check `--name` and `AI-Resource-Group` |
| `409 Conflict` | Resource with that name already exists | Choose a different name or delete first |
| `400 Bad Request` | Name pattern violation or missing field | See name constraints above |
| `403 Access Denied` on TA creation | Subject patterns not yet registered in HDL instance | Follow the "register subject patterns" steps in the Data Destinations section above; wait 1–2 min after update |
| HDL connection refused | Wrong hostname or no network access | Omit `https://`, check connectivity |
| TA stuck in `DELETING` | Background cleanup pending | Run `cleanup` endpoint; see `references/API.md` |

For full endpoint details, field schemas, and pagination parameters see `references/API.md`.
### Prediction

| HTTP | Error code | Description | Fix |
|------|-----------|-------------|-----|
| 400 | `VALIDATION_ERROR` | Request validation failed | Check required fields — `modelName`, `scenarioConfigName`, `predictionConfig.targetColumns`; ensure exactly one of `rows`/`columns` is provided; verify all arrays have the same length |
| 401 | — | Authentication failed | Check `--main-tenant` and `--resource-group` headers |
| 404 | `MODEL_NOT_FOUND` | Model not available | Verify `modelName` is `sap-rpt-1-small` or `sap-rpt-1-large` and the deployment is running |
| 404 | `SCENARIO_CONFIG_NOT_FOUND_ERROR` | Scenario configuration not found | Create it via the Scenario Configurations section above |
| 500 | `CONTEXT_SELECTOR_ERROR` | Context selector failure | Check TCR setup — tabular artifact and data destination must be healthy |
| 500 | `SAP_RPT1_SMALL_ERROR` | SAP RPT-1 Small failure | Check deployment status; retry or switch to `sap-rpt-1-large` |
| 500 | `SAP_RPT1_LARGE_ERROR` | SAP RPT-1 Large failure | Check deployment status; retry or switch to `sap-rpt-1-small` |
| 502 | `BAD_GATEWAY` | External service failure | Check deployment status; TFM or Context Selector unreachable |
| 504 | `GATEWAY_TIMEOUT` | Request timeout | Reduce `numRows` or batch size |

---

## Handoffs

| When | Use skill |
|------|-----------|
| Credential or auth errors, resource group management | `aicore-admin-resources` |
| Checking deployment status, creating/stopping deployments | `aicore-lifecycle-management` |
| Looking up executable IDs or browsing foundation models | `genai-hub-foundation-models` |

---

## When to Load Reference Files

| Trigger | Load |
|---------|------|
| Any credential or auth error | `aicore-admin-resources` skill |
| BTP CLI not installed or not logged in | `references/SETUP.md` |
| About to walk the user through BTP steps (registering subject patterns) | `references/API.md` |
| Need full field reference or a complete request example for prediction | `references/PREDICT.md` |
| User provides unusual data format and needs transformation guidance | `references/PREDICT.md` |
