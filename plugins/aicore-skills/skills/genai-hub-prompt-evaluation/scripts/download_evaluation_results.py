# /// script
# dependencies = ["boto3>=1.34"]
# ///
"""
Download the per-row SQLite results DB for a completed evaluation execution from object storage.

An evaluation produces two outputs: aggregate metrics in the tracking service (fetch with
get_evaluation_results.py) and a SQLite DB (`results.db`) written to the object-store bucket under
a prefix keyed by the execution ID (`<execution-id>/tmp/…/results.db`). `results.db` holds the raw
per-row data: orchestration input/output, every metric value per row, and per-response statistics.

Credentials are resolved by boto3's standard chain (AWS_ACCESS_KEY_ID + AWS_SECRET_ACCESS_KEY
environment variables, ~/.aws/credentials, or IAM role). The bucket name is passed via --bucket.
Credential values are never printed. This is a read-only download.

Usage:
  uv run scripts/download_evaluation_results.py --execution-id <id> --bucket <bucket>
  uv run scripts/download_evaluation_results.py --execution-id <id> --bucket <bucket> --show-tables
  uv run scripts/download_evaluation_results.py --execution-id <id> --bucket <bucket> --dest ./out --json

Options:
  --execution-id ID   Evaluation execution ID (required); default prefix is "<id>/"
  --bucket NAME       S3 bucket name (required)
  --prefix PREFIX     Override the object key prefix (default "<execution-id>/")
  --region REGION     S3 region (default: eu-central-1)
  --endpoint URL      Custom S3 endpoint URL (for non-AWS S3-compatible stores)
  --dest DIR          Local download directory (default "./results-<execution-id>")
  --show-tables       After download, list results.db tables with row counts
  --json              Emit JSON to stdout

Exit codes:
  0 - Success
  1 - Error (missing credentials, nothing found, download failure)

JSON structure:
  {"downloaded": ["<local path>", ...], "db_path": "<path or null>",
   "tables": {"<table>": <row count>, ...}}

Examples:
  uv run scripts/download_evaluation_results.py --execution-id <execution-id> --bucket my-bucket --show-tables
  uv run scripts/download_evaluation_results.py --execution-id <execution-id> --bucket my-bucket --json | jq '.tables'
"""

import argparse
import json
import os
import sqlite3
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Download the per-row SQLite results DB for an evaluation execution.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--execution-id", dest="execution_id", required=True)
    parser.add_argument("--bucket", dest="bucket", required=True)
    parser.add_argument("--prefix", dest="prefix", default=None)
    parser.add_argument("--region", dest="region", default="eu-central-1")
    parser.add_argument("--endpoint", dest="endpoint", default=None)
    parser.add_argument("--dest", dest="dest", default=None)
    parser.add_argument("--show-tables", dest="show_tables", action="store_true")
    parser.add_argument("--json", dest="as_json", action="store_true")
    args = parser.parse_args()

    import boto3  # noqa: E402
    import botocore.exceptions  # noqa: E402

    prefix = args.prefix or f"{args.execution_id}/"
    dest = args.dest or f"results-{args.execution_id}"

    client_kwargs = {"region_name": args.region}
    if args.endpoint:
        client_kwargs["endpoint_url"] = args.endpoint
    s3 = boto3.client("s3", **client_kwargs)

    downloaded = []
    db_path = None
    paginator = s3.get_paginator("list_objects_v2")
    try:
        for page in paginator.paginate(Bucket=args.bucket, Prefix=prefix):
            for obj in page.get("Contents", []):
                key = obj["Key"]
                local_path = os.path.join(dest, os.path.relpath(key, prefix))
                os.makedirs(os.path.dirname(local_path) or ".", exist_ok=True)
                s3.download_file(args.bucket, key, local_path)
                downloaded.append(local_path)
                if os.path.basename(key) == "results.db":
                    db_path = local_path
    except botocore.exceptions.NoCredentialsError:
        print("ERROR: AWS credentials not found. Set AWS_ACCESS_KEY_ID and "
              "AWS_SECRET_ACCESS_KEY, or configure ~/.aws/credentials.",
              file=sys.stderr)
        sys.exit(1)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: download failed ({type(exc).__name__}). "
              "Check bucket name, credentials, and that the execution is COMPLETED.",
              file=sys.stderr)
        sys.exit(1)

    tables = {}
    if db_path and (args.show_tables or args.as_json):
        conn = sqlite3.connect(db_path)
        try:
            cur = conn.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
            for (name,) in cur.fetchall():
                cur.execute(f'SELECT COUNT(*) FROM "{name}"')
                tables[name] = cur.fetchone()[0]
        finally:
            conn.close()

    if args.as_json:
        print(json.dumps({"downloaded": downloaded, "db_path": db_path, "tables": tables},
                         indent=2))
        return

    if not downloaded:
        print(f"No objects found under s3://{args.bucket}/{prefix}. Is the execution COMPLETED, "
              f"and is the prefix correct? (check outputArtifacts, or pass --prefix)")
        return

    for path in downloaded:
        print(f"downloaded {path}")
    if db_path:
        print(f"results DB: {db_path}")
        if tables:
            for name, count in tables.items():
                print(f"  table {name}: {count} row(s)")
    print(f"{len(downloaded)} object(s) downloaded.")


if __name__ == "__main__":
    main()
