# Instance-level results — download & inspect the SQLite DB

The evaluation job produces two outputs:

1. **Aggregate metrics** — stored in the tracking service; fetch with
   `scripts/get_evaluation_results.py --execution-id <id>` (no AWS access needed).
2. **A SQLite DB** (`results.db`) stored as an output artifact in object storage. It holds the raw
   per-row data: orchestration input/output, every metric value per row, and per-response
   statistics (latency, etc.).

This reference covers (2), which requires direct object-store (AWS) credentials — these are NOT
the AI Core credentials the skill scripts use, so the download reads them from the environment.

## 0. Quick path — the download script

`scripts/download_evaluation_results.py` wraps the download below and prints a table summary.
Set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in the environment, then pass the bucket:

```bash
uv run scripts/download_evaluation_results.py --execution-id <execution-id> --bucket <bucket> --show-tables
uv run scripts/download_evaluation_results.py --execution-id <execution-id> --bucket <bucket> --dest ./out --json
```

It downloads everything under `<execution-id>/` (override with `--prefix`), reports the local
`results.db` path, and with `--show-tables` lists each table's row count. The remaining sections
explain the download and schema if you want to do it by hand.

## 1. Find where the output artifact lives

Inspect the completed execution and read the `outputArtifacts[].url` field: invoke
`aicore-lifecycle-management` and run
`get_executions.py --execution-id <execution-id> --response-format detailed`.

The results are stored under a prefix keyed by the execution ID, typically
`<EXECUTION_ID>/tmp/…/results.db` in the bucket.

## 2. Download from S3

```python
# pip install boto3
import os, boto3

AWS_ACCESS_KEY = os.environ["AWS_ACCESS_KEY"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_REGION = os.environ["AWS_REGION"]
AWS_BUCKET_ID = os.environ["AWS_BUCKET_ID"]

EXECUTION_ID = "<execution-id>"
prefix = f"{EXECUTION_ID}/tmp/"          # adjust to the outputArtifacts url
destination_folder = "results-new"

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)

paginator = s3.get_paginator("list_objects_v2")
for page in paginator.paginate(Bucket=AWS_BUCKET_ID, Prefix=prefix):
    for obj in page.get("Contents", []):
        key = obj["Key"]
        local_path = os.path.join(destination_folder, os.path.relpath(key, prefix))
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        print(f"Downloading {key} -> {local_path}")
        s3.download_file(AWS_BUCKET_ID, key, local_path)
```

## 3. Inspect the tables

`results.db` contains, among others: `run`, `configuration`, `submission`,
`submission_result`, and `evaluation_result`.

```python
import sqlite3, pandas as pd

conn = sqlite3.connect("results-new/results.db")
for table in ["run", "configuration", "submission", "submission_result", "evaluation_result"]:
    df = pd.read_sql_query(f"SELECT * FROM {table};", conn)
    print(f"\n=== {table} ({len(df)} rows) ===")
    print(df.head(5).to_string(index=False))
conn.close()
```

- `run` — one row per model/prompt-config run, with `tags` and `config` JSON columns (the model
  name is under `config.modules.prompt_templating.model.name` or the
  `evaluation.ai.sap.com/model` tag).
- `evaluation_result` — the per-row metric values (the "raw" metrics the aggregates are computed
  from).
- `submission` / `submission_result` — the orchestration input and generated output per row.
