# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Get a specific scenario configuration by name.

Usage:
  uv run scripts/get_scenario_config.py --name <name> [--json]

Examples:
  uv run scripts/get_scenario_config.py --name my-scenario
  uv run scripts/get_scenario_config.py --name my-scenario --json
"""

import argparse
import json
import sys

import requests


def main():
    parser = argparse.ArgumentParser(description="Get a scenario configuration by name")
    parser.add_argument("--name", required=True, help="Scenario configuration name")
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

    url = f"{base_url}/tcr/scenarioConfigurations/{args.name}"
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

    tas = ", ".join(t["name"] for t in r.get("tabularArtifacts", []))
    labels = r.get("labels", [])
    labels_str = ", ".join(f"{l['key']}={l['value']}" for l in labels) if labels else "(none)"

    print(f"Name:              {r.get('name', '')}")
    print(f"Status:            {r.get('status', '')}")
    if r.get("errorMessage"):
        print(f"Error:             {r['errorMessage']}")
    print(f"Description:       {r.get('description', '')}")
    print(f"Strategy:          {r.get('contextSelectionStrategy', '')}")
    print(f"Tabular artifacts: {tas or '(none)'}")
    print(f"Labels:            {labels_str}")
    print(f"Created:           {r.get('createdAt', '')}")
    print(f"Updated:           {r.get('updatedAt', '')}")


if __name__ == "__main__":
    main()
