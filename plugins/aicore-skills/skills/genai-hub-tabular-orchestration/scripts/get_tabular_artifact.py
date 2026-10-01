# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Get a specific tabular artifact by name.

Usage:
  uv run scripts/get_tabular_artifact.py --name <name> [--json]

Examples:
  uv run scripts/get_tabular_artifact.py --name customer-ta
  uv run scripts/get_tabular_artifact.py --name customer-ta --json
"""

import argparse
import json
import sys

import requests


def main():
    parser = argparse.ArgumentParser(description="Get a tabular artifact by name")
    parser.add_argument("--name", required=True, help="Tabular artifact name")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output as JSON")
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

    url = f"{base_url}/tcr/tabularArtifacts/{args.name}"
    headers = {"Authorization": token, "AI-Resource-Group": rg}

    resp = requests.get(url, headers=headers, timeout=15)
    if resp.status_code == 404:
        print(f"Not found: {args.name}", file=sys.stderr)
        sys.exit(1)
    if not resp.ok:
        print(f"ERROR {resp.status_code}: {resp.text}", file=sys.stderr)
        sys.exit(1)

    r = resp.json()

    if args.as_json:
        print(json.dumps(r, indent=2))
        return

    print(f"Name:         {r.get('name', '')}")
    print(f"Destination:  {r.get('dataDestinationName', '')}")
    print(f"Path:         {r.get('path', '')}")
    print(f"Type:         {r.get('type', '')}")
    print(f"Status:       {r.get('status', '')}")
    if r.get("errorMessage"):
        print(f"Error:        {r['errorMessage']}")
    print(f"Virtual table: {r.get('virtualTableName', '')}")
    print(f"Remote source: {r.get('remoteSourceName', '')}")
    print(f"Created:      {r.get('createdAt', '')}")
    print(f"Updated:      {r.get('updatedAt', '')}")


if __name__ == "__main__":
    main()
