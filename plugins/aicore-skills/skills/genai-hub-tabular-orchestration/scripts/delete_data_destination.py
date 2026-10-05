# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Delete a data destination and all its dependent tabular artifacts.

Usage:
  uv run scripts/delete_data_destination.py --name <name> --confirm

Warning: deletion cascades — all tabular artifacts referencing this destination are also deleted.
"""

import argparse
import sys

import requests


def main():
    parser = argparse.ArgumentParser(description="Delete a data destination")
    parser.add_argument("--name", required=True, help="Data destination name")
    parser.add_argument("--confirm", action="store_true", help="Required: confirm cascading deletion")
    parser.add_argument("--resource-group", metavar="RG", help="AI-Resource-Group header value. Overrides env/SDK default.")
    args = parser.parse_args()

    if not args.confirm:
        print("ERROR: --confirm is required to delete a data destination (cascades to all its tabular artifacts)", file=sys.stderr)
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
    headers = {"Authorization": token, "AI-Resource-Group": rg}

    resp = requests.delete(url, headers=headers, timeout=15)
    if resp.status_code == 202:
        print(f"Accepted: data destination '{args.name}' is marked for deletion (cascades to dependent tabular artifacts).")
    elif resp.status_code == 404:
        print(f"Not found: {args.name}", file=sys.stderr)
        sys.exit(1)
    elif resp.status_code == 409:
        print(f"Conflict — cannot delete '{args.name}': {resp.text}", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"ERROR {resp.status_code}: {resp.text}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
