# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
List all scenario configurations in the current resource group.

Usage:
  uv run scripts/list_scenario_configs.py [--json] [--top N] [--skip N]

Examples:
  uv run scripts/list_scenario_configs.py
  uv run scripts/list_scenario_configs.py --json | jq '.[].name'
"""

import argparse
import json
import sys

import requests


def main():
    parser = argparse.ArgumentParser(description="List scenario configurations")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output as JSON array")
    parser.add_argument("--top", type=int, default=100, help="Max results (default 100)")
    parser.add_argument("--skip", type=int, default=0, help="Skip N results")
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

    url = f"{base_url}/tcr/scenarioConfigurations"
    params = {"$top": args.top, "$skip": args.skip, "$count": True}
    headers = {"Authorization": token, "AI-Resource-Group": rg}

    resp = requests.get(url, headers=headers, params=params, timeout=15)
    if not resp.ok:
        print(f"ERROR {resp.status_code}: {resp.text}", file=sys.stderr)
        sys.exit(1)

    data = resp.json()
    resources = data.get("resources", [])
    total = data.get("count", len(resources))

    if args.as_json:
        print(json.dumps(resources, indent=2))
        return

    if not resources:
        print("No scenario configurations found.")
        return

    name_w = max(len(r["name"]) for r in resources)
    name_w = max(name_w, 4)

    print(f"{'NAME':<{name_w}}  TABULAR ARTIFACTS")
    print("-" * (name_w + 40))
    for r in resources:
        tas = ", ".join(t["name"] for t in r.get("tabularArtifacts", []))
        print(f"{r['name']:<{name_w}}  {tas}")
    print(f"\n{len(resources)} of {total} scenario configuration(s)")


if __name__ == "__main__":
    main()
