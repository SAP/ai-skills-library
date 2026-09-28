# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Validate a data destination's connectivity BEFORE saving it.
Nothing is persisted — use this to verify credentials before calling create_data_destination.py.

Supports S3, GCS, and AZURE types (HDL and DELTA_SHARING are not supported by this endpoint).

Usage:
  uv run scripts/validate_data_destination.py --type S3 \\
      --bucket my-bucket --region eu-central-1 \\
      --access-key-id AKIA... --secret-access-key SECRET

  uv run scripts/validate_data_destination.py --type GCS \\
      --bucket my-bucket --base64-private-key "$(base64 < service_account.json)"

  uv run scripts/validate_data_destination.py --type AZURE \\
      --account-name myaccount --container-uri https://myaccount.blob.core.windows.net/container \\
      --sas-token "sv=2023-..."
"""

import argparse
import sys

import requests


def main():
    parser = argparse.ArgumentParser(description="Validate a data destination before creation")
    parser.add_argument("--type", required=True, choices=["S3", "GCS", "AZURE"],
                        dest="dest_type", help="Destination type")

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

    parser.add_argument("--resource-group", metavar="RG",
                        help="AI-Resource-Group header value. Overrides env/SDK default.")
    args = parser.parse_args()

    if args.dest_type == "S3":
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

    elif args.dest_type == "GCS":
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

    else:  # AZURE
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

    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add sap-ai-sdk-core", file=sys.stderr)
        sys.exit(2)

    client = AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills")
    base_url = client.rest_client.base_url.rstrip("/")
    token = client.rest_client.get_token()
    rg = args.resource_group or client.rest_client.headers.get("AI-Resource-Group", "default")

    url = f"{base_url}/tcr/dataDestinations/validate"
    headers = {"Authorization": token, "AI-Resource-Group": rg, "Content-Type": "application/json"}

    resp = requests.post(url, headers=headers, json=body, timeout=30)
    if not resp.ok:
        print(f"ERROR {resp.status_code}: {resp.text}", file=sys.stderr)
        sys.exit(1)

    result = resp.json()
    status = result.get("status", "")
    if status == "OK":
        print(f"Validation OK — {args.dest_type} credentials are valid.")
    elif status == "FAILED":
        print(f"Validation FAILED: {result.get('reason', '(no reason provided)')}", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"Unexpected response: {result}")


if __name__ == "__main__":
    main()
