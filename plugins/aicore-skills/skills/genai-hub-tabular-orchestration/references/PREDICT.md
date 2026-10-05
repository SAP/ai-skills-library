# Tabular Prediction API Reference

Endpoint: `POST /v2/inference/deployments/{deploymentId}/predict`

Additional required headers:
- `ai-main-tenant: <uuid>` — main tenant UUID
- `AI-Resource-Group: <rg>` — resource group

---

## Complete Request Shape

```json
{
  "modelName": "sap-rpt-1-small",
  "scenarioConfigName": "my-scenario",

  "contextSelectionConfig": {
    "numRows": 200,
    "strategy": "heuristic",
    "strategyConfig": {
      "indexColumn": "id",
      "methodRatio": 0.67,
      "chunkSize": 100,
      "chunkThreshold": 150,
      "poolSize": null,
      "fuzzyDateDays": 30,
      "fuzzyNumPct": 0.1,
      "allowTimeoutFallback": true
    }
  },

  "predictionConfig": {
    "targetColumns": [
      {
        "name": "category",
        "predictionPlaceholder": "[PREDICT]",
        "taskType": "classification",
        "topK": 3
      }
    ]
  },

  "columns": {
    "id": ["item-1", "item-2"],
    "category": ["[PREDICT]", "[PREDICT]"],
    "price": [99.99, 49.99]
  },

  "contextColumns": {
    "id": ["ctx-1", "ctx-2"],
    "category": ["Electronics", "Clothing"],
    "price": [199.99, 29.99]
  }
}
```

Use `rows`/`contextRows` instead of `columns`/`contextColumns` for row-oriented format — they are mutually exclusive. `contextSelectionConfig` defaults to `strategy: random` if omitted.

---

## Field Reference

### Top-level

| Field                    | Required | Type   | Notes                                                   |
|--------------------------|----------|--------|---------------------------------------------------------|
| `modelName`              | yes      | string | `sap-rpt-1-small` or `sap-rpt-1-large`                  |
| `scenarioConfigName`     | yes      | string | Must exist in TCR before the request                    |
| `predictionConfig`       | yes      | object | What to predict and how                                 |
| `modelConfig.*`          | no       | any    | Additional TFM-specific parameters passed to the model  |
| `contextSelectionConfig` | no       | object | Defaults to `random` strategy if omitted                |
| `columns`                | yes*     | object | Columnar query data — mutually exclusive with `rows`    |
| `rows`                   | yes*     | array  | Row-wise query data — mutually exclusive with `columns` |
| `contextColumns`         | no       | object | Inline context for `columns` requests                   |
| `contextRows`            | no       | array  | Inline context for `rows` requests                      |

\* Exactly one of `columns` or `rows` must be provided.

### `predictionConfig`

| Field           | Required | Type  | Notes      |
|-----------------|----------|-------|------------|
| `targetColumns` | yes      | array | Min 1 entry |

#### `targetColumns[*]`

| Field                   | Required | Type   | Default       | Notes                                                     |
|-------------------------|----------|--------|---------------|-----------------------------------------------------------|
| `name`                  | yes      | string | —             | Column name to predict; must exist in the query data      |
| `predictionPlaceholder` | no       | string | `"[PREDICT]"` | Marker value in query data                                |
| `taskType`              | no       | string | —             | `classification` or `regression`; auto-detected if omitted |
| `topK`                  | no       | int    | 1             | Number of top predictions to return (classification only) |

### `contextSelectionConfig`

| Field            | Required | Type   | Default  | Notes                                                              |
|------------------|----------|--------|----------|--------------------------------------------------------------------|
| `numRows`        | no       | int    | —        | Context rows to retrieve; skip context selection if 0 or null      |
| `indexColumn`    | no       | string | —        | Index column for context selection; required for heuristic strategy |
| `strategy`       | no       | string | `random` | `none`, `random`, `heuristic`, `auto`                              |
| `strategyConfig` | no       | object | —        | Strategy-specific parameters — see subsections below               |

#### `strategyConfig` — `none` strategy

No `strategyConfig` fields are needed — omit or pass an empty object.

```json
{ "contextSelectionConfig": { "strategy": "none" } }
```

#### `strategyConfig` — `random` strategy

| Field           | Type   | Notes                                       |
|-----------------|--------|---------------------------------------------|
| `deterministic` | bool   | Reproduce the same sample across requests   |
| `indexColumn`   | string | Index column used for deterministic sampling |

#### `strategyConfig` — `heuristic` strategy

| Field                  | Type      | Default | Notes                                                        |
|------------------------|-----------|---------|--------------------------------------------------------------|
| `indexColumn`          | string    | —       | Unique row identifier column                                 |
| `methodRatio`          | float     | 0.67    | Fraction of `numRows` filled by scoring; remainder is random |
| `chunkSize`            | int       | 100     | Max CASE WHEN expressions per SQL subquery chunk             |
| `chunkThreshold`       | int       | 150     | Column count above which chunked SQL is used                 |
| `poolSize`             | int\|null | null    | Scoring candidate pool size; null = full table scan          |
| `fuzzyDateDays`        | int       | 30      | Day window for fuzzy date matching; 0 = exact match          |
| `fuzzyNumPct`          | float     | 0.1     | Numeric fuzzy threshold as fraction of query value (±10%)    |
| `allowTimeoutFallback` | bool      | true    | Fall back to random selection if heuristic times out         |
