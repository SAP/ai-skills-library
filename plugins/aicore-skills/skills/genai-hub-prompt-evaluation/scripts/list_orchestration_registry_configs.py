# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
List prompt-registry (orchestration registry) configurations in SAP AI Core.

Use this to find the ID of an existing config to reuse as an "orchestrationRegistryIds" input to
create_evaluation_configuration.py, instead of creating a duplicate.

Endpoint: GET /registry/v2/orchestrationConfigs

Usage:
  uv run scripts/list_orchestration_registry_configs.py
  uv run scripts/list_orchestration_registry_configs.py --scenario genai-evaluations
  uv run scripts/list_orchestration_registry_configs.py --name genai-eval --json

Options:
  --scenario ID         Filter by scenario
  --name SUBSTR         Case-insensitive substring match on the config name
  --response-format FMT concise (default) or detailed
  --json                Emit JSON to stdout
  --resource-group RG   Resource group override

Exit codes:
  0 - Success
  1 - Error

JSON structure:
  [{"id": "...", "name": "...", "version": "...", "scenario": "..."}]

Examples:
  uv run scripts/list_orchestration_registry_configs.py --scenario genai-evaluations
  uv run scripts/list_orchestration_registry_configs.py --name genai-eval --json | jq -r '.[].id'
"""

import argparse
import json
import sys

from _rest import get_rest_context, request


def main():
    parser = argparse.ArgumentParser(
        description="List prompt-registry (orchestration registry) configs in SAP AI Core.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--scenario", default=None, help="Filter by scenario")
    parser.add_argument("--name", default=None, help="Case-insensitive substring match on name")
    parser.add_argument("--response-format", dest="response_format",
                        choices=["concise", "detailed"], default="concise")
    parser.add_argument("--json", dest="as_json", action="store_true")
    parser.add_argument("--resource-group", dest="resource_group", default=None)
    args = parser.parse_args()

    base_url, headers = get_rest_context(args.resource_group)
    body = request("GET", f"{base_url}/registry/v2/orchestrationConfigs", headers)

    if isinstance(body, dict):
        configs = body.get("resources") or body.get("data") or []
    elif isinstance(body, list):
        configs = body
    else:
        configs = []

    def keep(c):
        if args.scenario and c.get("scenario") != args.scenario:
            return False
        if args.name and args.name.lower() not in (c.get("name") or "").lower():
            return False
        return True

    configs = [c for c in configs if keep(c)]

    if args.as_json:
        out = [{"id": c.get("id"), "name": c.get("name"), "version": c.get("version"),
                "scenario": c.get("scenario")} for c in configs]
        print(json.dumps(out, indent=2))
        return

    if not configs:
        print("No orchestration registry configs found.")
        return

    for c in configs:
        print(f"{c.get('name')} v{c.get('version')}  id={c.get('id')}")
        if args.response_format == "detailed":
            print(f"       scenario={c.get('scenario')}")

    print(f"{len(configs)} config(s) found.")


if __name__ == "__main__":
    main()
