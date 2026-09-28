# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Search scenario configurations by label key-value pairs (AND logic — all labels must match).

Usage:
  uv run scripts/search_scenario_configs.py --labels KEY=VALUE [KEY=VALUE ...]
      [--json] [--top N] [--skip N]

Examples:
  uv run scripts/search_scenario_configs.py --labels ext.ai.sap.com/env=prod
  uv run scripts/search_scenario_configs.py --labels ext.ai.sap.com/env=prod ext.ai.sap.com/team=data
  uv run scripts/search_scenario_configs.py --labels ext.ai.sap.com/env=prod --json
"""

import argparse
import json
import sys

import requests


def parse_label(s):
    if "=" not in s:
        raise argparse.ArgumentTypeError(f"Label must be key=value, got: {s!r}")
    key, _, value = s.partition("=")
    return {"key": key, "value": value}


def main():
    parser = argparse.ArgumentParser(description="Search scenario configurations by labels")
    parser.add_argument("--labels", required=True, nargs="+", type=parse_label, metavar="KEY=VALUE",
                        help="Labels to match (all must match — AND logic)")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output as JSON array")
    parser.add_argument("--top", type=int, default=100, help="Max results (default 100)")
    parser.add_argument("--skip", type=int, default=0, help="Skip N results")
    parser.add_argument("--resource-group", metavar="RG",
                        help="AI-Resource-Group header value. Overrides env/SDK default.")
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

    url = f"{base_url}/tcr/scenarioConfigurations/search"
    params = {"$top": args.top, "$skip": args.skip, "$count": True}
    headers = {"Authorization": token, "AI-Resource-Group": rg, "Content-Type": "application/json"}
    body = {"labels": args.labels}

    resp = requests.post(url, headers=headers, params=params, json=body, timeout=15)
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
        print("No scenario configurations found matching those labels.")
        return

    name_w = max(len(r["name"]) for r in resources)
    name_w = max(name_w, 4)

    print(f"{'NAME':<{name_w}}  STATUS      STRATEGY   CREATED")
    print("-" * (name_w + 40))
    for r in resources:
        created = r.get("createdAt", "")[:10]
        status = r.get("status", "")
        strategy = r.get("contextSelectionStrategy", "")
        print(f"{r['name']:<{name_w}}  {status:<10}  {strategy:<9}  {created}")
    print(f"\n{len(resources)} of {total} scenario configuration(s)")


if __name__ == "__main__":
    main()
