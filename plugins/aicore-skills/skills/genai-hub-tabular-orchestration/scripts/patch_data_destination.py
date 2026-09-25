# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Update the labels of a data destination (replaces the entire label set).

Usage:
  uv run scripts/patch_data_destination.py --name <name> --labels key=value [key=value ...]

Examples:
  uv run scripts/patch_data_destination.py --name my-hdl --labels ext.ai.sap.com/env=prod
  uv run scripts/patch_data_destination.py --name my-hdl --labels ext.ai.sap.com/env=staging ext.ai.sap.com/team=data

Note: --labels replaces the entire label set. To remove all labels, this endpoint is not
designed for that — use an empty list via the raw API.
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
    parser = argparse.ArgumentParser(description="Update data destination labels")
    parser.add_argument("--name", required=True, help="Data destination name")
    parser.add_argument(
        "--labels",
        required=True,
        nargs="+",
        type=parse_label,
        metavar="KEY=VALUE",
        help="Labels to set (replaces all existing labels)",
    )
    parser.add_argument("--resource-group", metavar="RG", help="AI-Resource-Group header value. Overrides env/SDK default.")
    args = parser.parse_args()

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
    body = {"labels": args.labels}

    resp = requests.patch(url, headers=headers, json=body, timeout=15)
    if resp.status_code == 204:
        print(f"Updated labels for data destination: {args.name}")
    elif resp.status_code == 404:
        print(f"Not found: {args.name}", file=sys.stderr)
        sys.exit(1)
    elif resp.status_code == 400:
        print(f"Bad request — check label key format: {resp.text}", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"ERROR {resp.status_code}: {resp.text}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
