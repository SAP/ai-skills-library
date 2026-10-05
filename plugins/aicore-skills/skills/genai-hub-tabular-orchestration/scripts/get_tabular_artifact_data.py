# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Preview the first 10 rows of a tabular artifact's virtual table.

The artifact must have status=ACTIVE before data can be retrieved.

Usage:
  uv run scripts/get_tabular_artifact_data.py --name <name> [--json]

Examples:
  uv run scripts/get_tabular_artifact_data.py --name customer-ta
  uv run scripts/get_tabular_artifact_data.py --name customer-ta --json
"""

import argparse
import json
import sys

import requests


def main():
    parser = argparse.ArgumentParser(description="Preview data rows from a tabular artifact")
    parser.add_argument("--name", required=True, help="Tabular artifact name")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output as JSON")
    parser.add_argument("--resource-group", metavar="RG",
                        help="AI-Resource-Group header value. Overrides env/SDK default.")
    args = parser.parse_args()

    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add sap-ai-sdk-core", file=sys.stderr)
        sys.exit(2)

    client = AICoreV2Client.from_env(read_timeout=30, connect_timeout=15, client_type="AI Core Skills")
    base_url = client.rest_client.base_url.rstrip("/")
    token = client.rest_client.get_token()
    rg = args.resource_group or client.rest_client.headers.get("AI-Resource-Group", "default")

    url = f"{base_url}/tcr/tabularArtifacts/{args.name}/data"
    headers = {"Authorization": token, "AI-Resource-Group": rg}

    resp = requests.get(url, headers=headers, timeout=30)
    if resp.status_code == 404:
        print(f"Not found: {args.name}", file=sys.stderr)
        sys.exit(1)
    if not resp.ok:
        print(f"ERROR {resp.status_code}: {resp.text}", file=sys.stderr)
        sys.exit(1)

    result = resp.json()

    if args.as_json:
        print(json.dumps(result, indent=2))
        return

    columns = result.get("columns", [])
    rows = result.get("data", [])

    if not rows:
        print(f"No rows returned for '{args.name}'.")
        return

    col_widths = {c: max(len(c), max((len(str(row.get(c, ""))) for row in rows), default=0)) for c in columns}

    header = "  ".join(f"{c:<{col_widths[c]}}" for c in columns)
    separator = "  ".join("-" * col_widths[c] for c in columns)
    print(header)
    print(separator)
    for row in rows:
        print("  ".join(f"{str(row.get(c, '')):<{col_widths[c]}}" for c in columns))
    print(f"\n{len(rows)} row(s) (preview, up to 10)")


if __name__ == "__main__":
    main()
