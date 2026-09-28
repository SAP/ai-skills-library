# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Create a new data destination.

Usage:
  uv run scripts/create_data_destination.py --name <name> --type <TYPE> [TYPE-SPECIFIC OPTIONS]
      [--description TEXT] [--labels key=value ...] [--adapter-type File]

Supported types and required options:
  HDL          --host <hostname>
  DELTA_SHARING --host <hostname> [--provider hdlf]
  S3           --bucket <bucket> --region <region>
               --access-key-id <key> --secret-access-key <secret>
  GCS          --bucket <bucket> --base64-private-key <base64-encoded-service-account-json>
  AZURE        --account-name <account> --container-uri <uri> --sas-token <token>

Examples:
  uv run scripts/create_data_destination.py --name my-hdl --type HDL \\
      --host abc123.files.hdl.eu10.hanacloud.ondemand.com

  uv run scripts/create_data_destination.py --name my-delta --type DELTA_SHARING \\
      --host abc123.sharing.hdl.eu10.hanacloud.ondemand.com --provider hdlf

  uv run scripts/create_data_destination.py --name my-s3 --type S3 \\
      --bucket my-bucket --region eu-central-1 \\
      --access-key-id AKIAIOSFODNN7EXAMPLE --secret-access-key wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

  uv run scripts/create_data_destination.py --name my-gcs --type GCS \\
      --bucket my-bucket --base64-private-key "$(base64 < service_account.json)"

  uv run scripts/create_data_destination.py --name my-azure --type AZURE \\
      --account-name mystorageaccount \\
      --container-uri "https://mystorageaccount.z2.blob.storage.azure.net/mycontainer" \\
      --sas-token "sv=2023-01-03&..."

Notes:
  - HDL/DELTA_SHARING --host must NOT include https:// or any URL scheme
  - The API responds 202 Accepted (async). Poll GET /dataDestinations/{name} until status=ACTIVE
  - HDL destinations require registering subjectPatterns in the file system before creating artifacts
"""

import argparse
import json
import sys

import requests


def parse_labels(raw: list[str]) -> list[dict]:
    labels = []
    for item in raw:
        if "=" not in item:
            print(f"ERROR: label '{item}' must be in key=value format", file=sys.stderr)
            sys.exit(1)
        key, value = item.split("=", 1)
        labels.append({"key": key, "value": value})
    return labels


def build_body(args) -> dict:
    dest_type = args.dest_type

    if dest_type == "HDL":
        if not args.host:
            print("ERROR: --host is required for HDL type", file=sys.stderr)
            sys.exit(1)
        if args.host.startswith("http"):
            print("ERROR: --host must be a hostname only, without https://", file=sys.stderr)
            sys.exit(1)
        body = {
            "type": "HDL",
            "config": {"host": args.host},
            "adapterType": "File",
        }

    elif dest_type == "DELTA_SHARING":
        if not args.host:
            print("ERROR: --host is required for DELTA_SHARING type", file=sys.stderr)
            sys.exit(1)
        if args.host.startswith("http"):
            print("ERROR: --host must be a hostname only, without https://", file=sys.stderr)
            sys.exit(1)
        config: dict = {"host": args.host}
        if args.provider:
            config["provider"] = args.provider
        body = {
            "type": "DELTA_SHARING",
            "config": config,
            "adapterType": "DeltaShare",
        }

    elif dest_type == "S3":
        missing = [f for f, v in [
            ("--bucket", args.bucket),
            ("--region", args.region),
            ("--access-key-id", args.access_key_id),
            ("--secret-access-key", args.secret_access_key),
        ] if not v]
        if missing:
            print(f"ERROR: S3 type requires: {', '.join(missing)}", file=sys.stderr)
            sys.exit(1)
        body = {
            "type": "S3",
            "config": {
                "bucket": args.bucket,
                "region": args.region,
                "access_key_id": args.access_key_id,
                "secret_access_key": args.secret_access_key,
            },
        }

    elif dest_type == "GCS":
        missing = [f for f, v in [
            ("--bucket", args.bucket),
            ("--base64-private-key", args.base64_private_key),
        ] if not v]
        if missing:
            print(f"ERROR: GCS type requires: {', '.join(missing)}", file=sys.stderr)
            sys.exit(1)
        body = {
            "type": "GCS",
            "config": {
                "bucket": args.bucket,
                "base64_encoded_private_key_data": args.base64_private_key,
            },
        }

    elif dest_type == "AZURE":
        missing = [f for f, v in [
            ("--account-name", args.account_name),
            ("--container-uri", args.container_uri),
            ("--sas-token", args.sas_token),
        ] if not v]
        if missing:
            print(f"ERROR: AZURE type requires: {', '.join(missing)}", file=sys.stderr)
            sys.exit(1)
        body = {
            "type": "AZURE",
            "config": {
                "account_name": args.account_name,
                "container_uri": args.container_uri,
                "sas_token": args.sas_token,
            },
        }

    else:
        print(f"ERROR: unknown type '{dest_type}'", file=sys.stderr)
        sys.exit(1)

    if args.description:
        body["description"] = args.description
    if args.labels:
        body["labels"] = parse_labels(args.labels)
    return body


def main():
    parser = argparse.ArgumentParser(description="Create a data destination")
    parser.add_argument("--name", required=True, help="Data destination name (1-127 chars, kebab-case)")
    parser.add_argument("--type", required=True, dest="dest_type",
                        choices=["HDL", "DELTA_SHARING", "S3", "GCS", "AZURE"],
                        help="Destination type")

    # HDL / DELTA_SHARING
    parser.add_argument("--host", help="HDL or DELTA_SHARING hostname (no https:// prefix)")
    parser.add_argument("--provider", choices=["hdlf"],
                        help="DELTA_SHARING provider (optional, defaults to hdlf)")

    # S3 / GCS common
    parser.add_argument("--bucket", help="S3 or GCS bucket name")

    # S3
    parser.add_argument("--region", help="S3: AWS region (e.g. eu-central-1)")
    parser.add_argument("--access-key-id", dest="access_key_id", help="S3: AWS access key ID")
    parser.add_argument("--secret-access-key", dest="secret_access_key",
                        help="S3: AWS secret access key (raw, not URL-encoded)")

    # GCS
    parser.add_argument("--base64-private-key", dest="base64_private_key",
                        help="GCS: base64-encoded service-account JSON key")

    # AZURE
    parser.add_argument("--account-name", dest="account_name", help="AZURE: storage account name")
    parser.add_argument("--container-uri", dest="container_uri",
                        help="AZURE: full container URI from BTP Object Store service key")
    parser.add_argument("--sas-token", dest="sas_token",
                        help="AZURE: SAS token (must grant r+l on the container)")

    # Common
    parser.add_argument("--description", help="Optional description")
    parser.add_argument("--labels", nargs="+", default=[], metavar="KEY=VALUE",
                        help="Labels, e.g. ext.ai.sap.com/env=prod")
    parser.add_argument("--resource-group", metavar="RG",
                        help="AI-Resource-Group header value. Overrides env/SDK default.")
    args = parser.parse_args()

    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add sap-ai-sdk-core", file=sys.stderr)
        sys.exit(2)

    body = build_body(args)

    client = AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills")
    base_url = client.rest_client.base_url.rstrip("/")
    token = client.rest_client.get_token()
    rg = args.resource_group or client.rest_client.headers.get("AI-Resource-Group", "default")

    url = f"{base_url}/tcr/dataDestinations/{args.name}"
    headers = {"Authorization": token, "AI-Resource-Group": rg, "Content-Type": "application/json"}

    resp = requests.put(url, headers=headers, json=body, timeout=30)
    if not resp.ok:
        print(f"ERROR {resp.status_code}: {resp.text}", file=sys.stderr)
        sys.exit(1)

    result = resp.json()
    print(f"Accepted: data destination '{result['name']}' creation started (status: PROCESSING).")
    print("Poll 'get_data_destination.py --name ...' until status=ACTIVE before creating tabular artifacts.")

    if result.get("subjectPatterns"):
        print(file=sys.stderr)
        print("ACTION REQUIRED — HDL file system access", file=sys.stderr)
        print("=" * 60, file=sys.stderr)
        print("These subject pattern(s) must be registered in the HDL", file=sys.stderr)
        print("file system BEFORE any tabular artifact can be created:", file=sys.stderr)
        print(file=sys.stderr)
        for p in result["subjectPatterns"]:
            print(f"  {p}", file=sys.stderr)
        print(file=sys.stderr)
        print("Share them with your HDL admin and confirm access is", file=sys.stderr)
        print("granted before proceeding. Skipping this step will cause", file=sys.stderr)
        print("a 403 Access Denied error when creating tabular artifacts.", file=sys.stderr)
        print("=" * 60, file=sys.stderr)


if __name__ == "__main__":
    main()
