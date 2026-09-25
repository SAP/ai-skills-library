# Context Registry API Reference

Base URL: `https://api.ai.{region}.ml.hana.ondemand.com/v2/tcr`

All endpoints require:
- `Authorization: Bearer <token>` header
- `AI-Resource-Group: <rg>` header

---

## Data Destinations

### PUT /dataDestinations/{name}
Create an HDL data destination (async).

Request body (HDL type):
```json
{
  "type": "HDL",
  "config": { "host": "abc123.files.hdl.eu10.hanacloud.ondemand.com" },
  "adapterType": "File",
  "description": "optional",
  "labels": [{ "key": "ext.ai.sap.com/env", "value": "prod" }]
}
```

Response `200`:
```json
{ "name": "my-hdl", "subjectPatterns": ["..."] }
```

### GET /dataDestinations
List all data destinations. Query: `$top`, `$skip`, `$count`.

Response `200`: `{ "count": N, "resources": [ <DataDestination>, ... ] }`

### GET /dataDestinations/{name}
Get a specific data destination (credentials excluded).

### PATCH /dataDestinations/{name}
Update labels only (replaces entire label set):
```json
{ "labels": [{ "key": "ext.ai.sap.com/env", "value": "staging" }] }
```
Response `204`.

### DELETE /dataDestinations/{name}
Delete destination + cascade delete all its tabular artifacts.
Response `204`. Returns `409` if there are dependencies that block deletion.

### POST /dataDestinations/search
Search by labels:
```json
{ "labels": [{ "key": "ext.ai.sap.com/env", "value": "prod" }] }
```
Query: `$top`, `$skip`, `$count`. Response `200`: same as list.

---

## Tabular Artifacts

### PUT /tabularArtifacts/{name}
Create a tabular artifact (async).

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

**REFERENCE** (CSN file on the HDL):
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

Response `200`: `{ "name": "customer-ta" }`

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
      "virtualTableName": "...",
      "remoteSourceName": "...",
      "csnMetadata": { ... },
      "createdAt": "2024-02-15T12:45:00.000Z",
      "updatedAt": "2024-02-15T12:45:00.000Z"
    }
  ]
}
```

`status` values: `ACTIVE`, `DELETING`

### GET /tabularArtifacts/{name}
Get details of a specific artifact.

### DELETE /tabularArtifacts/{name}
Soft-delete: transitions to `DELETING`, cleaned up asynchronously.
Response `202 Accepted`.

### POST /tabularArtifacts/cleanup (internal)
Trigger cleanup of soft-deleted artifacts:
```json
{ "names": ["customer-ta"] }
```
Response `200`: `{ "message": "Cleanup completed" }`

---

## Scenario Configurations

### PUT /scenarioConfigurations/{name}
Create a scenario configuration (async):
```json
{
  "tabularArtifacts": [{ "name": "customer-ta" }, { "name": "orders-ta" }]
}
```
Response `200`: `{ "name": "my-scenario" }`

### GET /scenarioConfigurations
List all. Query: `$top`, `$skip`, `$count`.

Response `200`:
```json
{
  "count": N,
  "resources": [
    {
      "name": "my-scenario",
      "tabularArtifacts": [{ "name": "customer-ta" }, { "name": "orders-ta" }],
      "createdAt": "2024-02-15T12:45:00.000Z",
      "updatedAt": "2024-02-15T12:45:00.000Z"
    }
  ]
}
```

### GET /scenarioConfigurations/{name}
Get a specific scenario configuration.

### PATCH /scenarioConfigurations/{name}
Replace the tabular artifact list (cannot change name):
```json
{ "tabularArtifacts": [{ "name": "customer-ta" }, { "name": "orders-ta" }, { "name": "inventory-ta" }] }
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
