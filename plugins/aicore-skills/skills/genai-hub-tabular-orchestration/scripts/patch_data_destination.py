# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Update a data destination (labels, description, and/or credentials).

Usage:
  uv run scripts/patch_data_destination.py --name <name> [OPTIONS]

At least one of --labels, --description, or a credential flag must be provided.

Label options:
  --labels KEY=VALUE [KEY=VALUE ...]   Replace the entire label set

Description:
  --description TEXT                   Update the description

Credential options (pick the set for your destination type):
  S3:    --access-key-id KEY --secret-access-key SECRET
  GCS:   --base64-private-key DATA      (base64-encoded service-account JSON)
  AZURE: --sas-token TOKEN

Examples:
  # Update labels only
  uv run scripts/patch_data_destination.py --name my-hdl \\
      --labels ext.ai.sap.com/env=prod

  # Update description and labels
  uv run scripts/patch_data_destination.py --name my-s3 \\
      --description "Production S3 bucket" --labels ext.ai.sap.com/env=prod

  # Rotate S3 credentials
  uv run scripts/patch_data_destination.py --name my-s3 \\
      --access-key-id NEW_AKID --secret-access-key NEW_SECRET

  # Refresh Azure SAS token
  uv run scripts/patch_data_destination.py --name my-azure \\
      --sas-token "sv=2023-..."
"""

import argparse
import sys

import requests


def parse_label(s):
    if "=" not in s:
        raise argparse.ArgumentTypeError(f"Label must be key=value, got: {s!r}")
    key, _, value = s.partition("=")
    return {"key": key, "value": value}


def main():
    parser = argparse.ArgumentParser(description="Update a data destination")
    parser.add_argument("--name", required=True, help="Data destination name")
    parser.add_argument(
        "--labels",
        nargs="+",
        type=parse_label,
        metavar="KEY=VALUE",
        help="Labels to set (replaces all existing labels)",
    )
    parser.add_argument("--description", help="Updated description")
    # S3 credentials
    parser.add_argument("--access-key-id", dest="access_key_id", help="S3: AWS access key ID")
    parser.add_argument("--secret-access-key", dest="secret_access_key", help="S3: AWS secret access key")
    # GCS credentials
    parser.add_argument("--base64-private-key", dest="base64_private_key",
                        help="GCS: base64-encoded service-account JSON key")
    # Azure credentials
    parser.add_argument("--sas-token", dest="sas_token", help="AZURE: SAS token")
    parser.add_argument("--resource-group", metavar="RG",
                        help="AI-Resource-Group header value. Overrides env/SDK default.")
    args = parser.parse_args()

    body: dict = {}
    if args.labels is not None:
        body["labels"] = args.labels
    if args.description is not None:
        body["description"] = args.description

    config: dict = {}
    if args.access_key_id:
        config["access_key_id"] = args.access_key_id
    if args.secret_access_key:
        config["secret_access_key"] = args.secret_access_key
    if args.base64_private_key:
        config["base64_encoded_private_key_data"] = args.base64_private_key
    if args.sas_token:
        config["sas_token"] = args.sas_token
    if config:
        body["config"] = config

    if not body:
        print("ERROR: at least one of --labels, --description, or a credential flag must be provided",
              file=sys.stderr)
        sys.exit(1)

    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add sap-ai-sdk-core", file=sys.stderr)
        sys.exit(2)

    client = AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills")
    base_url = client.rest_client.base_url.rstrip("/")
    token = client.rest_client.get_token()
    rg = args.resource_group or client.rest_client.headers.get("AI-Resource-Group", "default")

    url = f"{base_url}/tcr/dataDestinations/{args.name}"
    headers = {
        "Authorization": token,
        "AI-Resource-Group": rg,
        "Content-Type": "application/json",
    }

    resp = requests.patch(url, headers=headers, json=body, timeout=15)
    if resp.status_code == 204:
        print(f"Updated data destination: {args.name}")
    elif resp.status_code == 404:
        print(f"Not found: {args.name}", file=sys.stderr)
        sys.exit(1)
    elif resp.status_code == 409:
        print(f"Conflict — destination may be in DELETING state: {resp.text}", file=sys.stderr)
        sys.exit(1)
    elif resp.status_code == 400:
        print(f"Bad request — check label key format or config fields: {resp.text}", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"ERROR {resp.status_code}: {resp.text}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
