# Context Registry API Reference

Base URL: `https://api.ai.{region}.ml.hana.ondemand.com/v2/tcr`

All endpoints require:
- `Authorization: Bearer <token>` header
- `AI-Resource-Group: <rg>` header

---

## Data Destinations

### PUT /dataDestinations/{name}
Create a data destination (async). Returns `202 Accepted`; poll `GET /dataDestinations/{name}` via `status` to track progress (`PROCESSING` → `ACTIVE` or `ERROR`).

**HDL:**
```json
{
  "type": "HDL",
  "config": { "host": "abc123.files.hdl.eu10.hanacloud.ondemand.com" },
  "adapterType": "File",
  "description": "optional",
  "labels": [{ "key": "ext.ai.sap.com/env", "value": "prod" }]
}
```

**S3:**
```json
{
  "type": "S3",
  "config": {
    "bucket": "my-bucket",
    "region": "eu-central-1",
    "access_key_id": "AKIA...",
    "secret_access_key": "raw-secret-do-not-url-encode"
  }
}
```

**GCS:**
```json
{
  "type": "GCS",
  "config": {
    "bucket": "my-bucket",
    "base64_encoded_private_key_data": "<base64 of service-account JSON>"
  }
}
```

**AZURE:**
```json
{
  "type": "AZURE",
  "config": {
    "account_name": "mystorageaccount",
    "container_uri": "https://mystorageaccount.z2.blob.storage.azure.net/mycontainer",
    "sas_token": "<raw SAS token — must grant r+l on container>"
  }
}
```

**DELTA_SHARING:**
```json
{
  "type": "DELTA_SHARING",
  "adapterType": "DeltaShare",
  "config": {
    "host": "abc123.sharing.hdl.eu10.hanacloud.ondemand.com",
    "provider": "hdlf"
  }
}
```

Response `202`:
```json
{ "name": "my-hdl", "subjectPatterns": ["..."] }
```
`subjectPatterns` is present for HDL only — register these in the HDL file system before creating tabular artifacts.

Status codes: `202` (accepted), `400` (bad request), `409` (ACTIVE or DELETING — use DELETE first), `422` (retry exhausted), `500`.

### GET /dataDestinations
List all data destinations. Query: `$top`, `$skip`, `$count`.

Response `200`: `{ "count": N, "resources": [ <DataDestination>, ... ] }`

### GET /dataDestinations/{name}
Get a specific data destination (credentials excluded).

Response includes `status` (`PROCESSING`, `ACTIVE`, `ERROR`, `DELETING`) and `errorMessage` (non-null when `ERROR`). Poll this endpoint after a `PUT` to confirm the destination becomes `ACTIVE`.

### PATCH /dataDestinations/{name}
Update a data destination (excluding `name` and `type`). Supports `labels`, `description`, and `config` (credentials — for key rotation or token refresh):

```json
{
  "labels": [{ "key": "ext.ai.sap.com/env", "value": "staging" }],
  "description": "updated description",
  "config": { "access_key_id": "NEW_KEY", "secret_access_key": "NEW_SECRET" }
}
```
`config` fields per type — S3: `access_key_id`, `secret_access_key`; GCS: `base64_encoded_private_key_data`; Azure: `sas_token`. Omit fields you do not want to change. Response `204`.

### DELETE /dataDestinations/{name}
Mark the destination for deletion (`DELETING`). The server synchronously checks for dependent tabular artifacts (returns `409` if any exist); then marks the destination `DELETING` and responds `202`. A background cron job handles secret cleanup and hard delete.

Response `202` (accepted), `404` (not found), `409` (has dependents or already DELETING), `500`.

### POST /dataDestinations/search
Search by labels (AND logic):
```json
{ "labels": [{ "key": "ext.ai.sap.com/env", "value": "prod" }] }
```
Query: `$top`, `$skip`, `$count`. Response `200`: same shape as list.

### POST /dataDestinations/validate
Test connectivity **before** saving — nothing is persisted. Supports S3, GCS, and AZURE types (not HDL/DELTA_SHARING).

```json
{
  "type": "S3",
  "config": {
    "bucket": "my-bucket",
    "region": "eu-central-1",
    "access_key_id": "AKIA...",
    "secret_access_key": "..."
  }
}
```

Response `200`:
```json
{ "status": "OK" }
```
or on failure:
```json
{ "status": "FAILED", "reason": "provider-specific error message" }
```

### POST /dataDestinations/{name}/validate
Re-validate an **already-saved** destination using its stored credentials.

Response `200`: same `{ "status": "OK" | "FAILED", "reason": "..." }` shape as above.

---

## Tabular Artifacts

### PUT /tabularArtifacts/{name}
Create a tabular artifact (async). Returns `202 Accepted`; poll `GET /tabularArtifacts/{name}` via `status`.

Request body:
```json
{
  "dataDestinationName": "my-hdl",
  "path": "/data/customer.csv",
  "type": "CSV",
  "csnMetadata": {
    "entityName": "Customer",
    "selectedColumns": ["id", "name"],
    "definition": { ... }
  }
}
```

`type` enum: `CSV`, `PARQUET`, `DELTA`

For DELTA_SHARING destinations `path` uses format `/<share>/<schema>/<table>` (e.g. `/sample_data/tpch/customer`).

`csnMetadata.definition` variants:

**AUTO** (derive schema from file):
```json
{ "definitionType": "AUTO" }
```
Optional `autoConfig` for CSV:
```json
{
  "definitionType": "AUTO",
  "autoConfig": {
    "csvOptions": { "columnListInFirstRow": true, "delimiter": "," }
  }
}
```

**REFERENCE** (CSN file on the data destination):
```json
{
  "definitionType": "REFERENCE",
  "documentReference": { "path": "/data/metadata/csn.json" }
}
```

**DOCUMENT** (inline CSN):
```json
{
  "definitionType": "DOCUMENT",
  "document": { "definitions": { "MyEntity": { ... } } }
}
```

Response `202`: `{ "name": "customer-ta" }`

Status codes: `202` (accepted), `400`, `409` (ACTIVE or DELETING), `422` (retry exhausted), `500`.

### GET /tabularArtifacts
List all. Query: `$top`, `$skip`, `$count`.

Response `200`:
```json
{
  "count": N,
  "resources": [
    {
      "id": "...",
      "name": "customer-ta",
      "tenantId": "...",
      "resourceGroupId": "...",
      "dataDestinationName": "my-hdl",
      "path": "/data/customer.csv",
      "type": "CSV",
      "status": "ACTIVE",
      "errorMessage": null,
      "virtualTableName": "...",
      "remoteSourceName": "...",
      "csnMetadata": { ... },
      "metadata": [ { "type": "csn", "columns": [ { "name": "id", "cdsType": "cds.Integer" } ] } ],
      "createdAt": "2024-02-15T12:45:00.000Z",
      "updatedAt": "2024-02-15T12:45:00.000Z"
    }
  ]
}
```

`status` values: `PROCESSING`, `ERROR`, `ACTIVE`, `DELETING`

### GET /tabularArtifacts/{name}
Get details of a specific artifact. Same response shape as a single entry in the list above. Check `errorMessage` when `status` is `ERROR`.

### GET /tabularArtifacts/{name}/data
Retrieve a preview of the first 10 rows from the virtual table.

Response `200`:
```json
{
  "name": "customer-ta",
  "columns": ["id", "name", "purchase_amount"],
  "data": [
    { "id": "1", "name": "Alice", "purchase_amount": 99.99 }
  ]
}
```

Only available when `status` is `ACTIVE`.

### DELETE /tabularArtifacts/{name}
Soft-delete: transitions to `DELETING`, cleaned up asynchronously.
Response `202 Accepted`.

---

## Scenario Configurations

### PUT /scenarioConfigurations/{name}
Create a scenario configuration (async). Returns `202 Accepted`; poll `GET /scenarioConfigurations/{name}` via `status`.

```json
{
  "tabularArtifacts": [{ "name": "customer-ta" }, { "name": "orders-ta" }],
  "description": "optional description",
  "contextSelectionStrategy": "embedding",
  "labels": [{ "key": "ext.ai.sap.com/env", "value": "prod" }]
}
```

`contextSelectionStrategy`: `random` (default) or `embedding`.

Response `202`: `{ "name": "my-scenario" }`

Status codes: `202`, `400`, `409` (ACTIVE or DELETING), `422` (retry exhausted), `500`.

### GET /scenarioConfigurations
List all. Query: `$top`, `$skip`, `$count`.

Response `200`:
```json
{
  "count": N,
  "resources": [
    {
      "name": "my-scenario",
      "description": "...",
      "contextSelectionStrategy": "random",
      "tabularArtifacts": [{ "name": "customer-ta" }, { "name": "orders-ta" }],
      "labels": [],
      "status": "ACTIVE",
      "errorMessage": null,
      "createdAt": "2024-02-15T12:45:00.000Z",
      "updatedAt": "2024-02-15T12:45:00.000Z"
    }
  ]
}
```

`status` values: `PROCESSING`, `ACTIVE`, `ERROR`, `DELETING`

### GET /scenarioConfigurations/{name}
Get a specific scenario configuration. Same response shape as a single list entry. Check `errorMessage` when `status` is `ERROR`.

### POST /scenarioConfigurations/search
Search for scenario configurations that match **all** specified labels (AND logic):

```json
{
  "labels": [{ "key": "ext.ai.sap.com/env", "value": "prod" }]
}
```

Query: `$top`, `$skip`, `$count`. Response `200`: same shape as list.

### PATCH /scenarioConfigurations/{name}
Update a scenario configuration (excluding `name`). Supports `tabularArtifacts`, `contextSelectionStrategy`, `labels`, and `description`. At least one field required.

```json
{
  "tabularArtifacts": [{ "name": "customer-ta" }, { "name": "orders-ta" }, { "name": "inventory-ta" }],
  "contextSelectionStrategy": "embedding",
  "labels": [{ "key": "ext.ai.sap.com/env", "value": "staging" }],
  "description": "updated description"
}
```

Response `204`.

### DELETE /scenarioConfigurations/{name}
Delete a scenario configuration. Response `204`.

---

## Name constraints (all resources)

| Field | Pattern | Max length |
|-------|---------|-----------|
| data destination | `^[a-z0-9]([-a-z0-9]*[a-z0-9])?$` | 127 |
| tabular artifact | `^[a-z0-9]([-a-z0-9]*[a-z0-9])?$` | 80 |
| scenario config | `^[a-z0-9]([-a-z0-9]*[a-z0-9])?$` | 127 |

All: lowercase letters, numbers, hyphens only; must start and end with alphanumeric.

## Label key constraints

Data Destinations and Tabular Artifacts accept both `ext.ai.sap.com/` and `int.ai.sap.com/` prefixes.
Scenario Configurations accept only `ext.ai.sap.com/` prefix.

Pattern: `^(ext|int)\.ai\.sap\.com/[A-Za-z0-9][-A-Za-z0-9_.]*[A-Za-z0-9]$`
Max key length: 63 chars. Max value length: 63 chars.

## Pagination

All list endpoints support:
- `$top` (int 0–1000): max results per page
- `$skip` (int ≥ 0): offset
- `$count` (bool): when `true`, `count` in the response reflects total on server, not just current page

## Error format

```json
{
  "error": {
    "code": "DESCRIPTIVE_CODE",
    "message": "human-readable description",
    "requestId": "...",
    "target": "the URL called",
    "details": [{ "code": "...", "message": "..." }]
  }
}
```
