# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
List Prompt Templates in the SAP AI Core Prompt Registry.

Use this to find the ID of an existing prompt template to bind to an evaluation configuration
(--prompt-template-id), instead of creating a duplicate.

Endpoint: GET /lm/promptTemplates

Usage:
  uv run scripts/list_prompt_templates.py
  uv run scripts/list_prompt_templates.py --scenario genai-evaluations
  uv run scripts/list_prompt_templates.py --name prompt-registry-eval --json

Options:
  --scenario ID         Filter by scenario
  --name SUBSTR         Case-insensitive substring match on the template name
  --response-format FMT concise (default) or detailed
  --json                Emit JSON to stdout
  --resource-group RG   Resource group override

Exit codes:
  0 - Success
  1 - Error

JSON structure:
  [{"id": "...", "name": "...", "version": "...", "scenario": "..."}]

Examples:
  uv run scripts/list_prompt_templates.py --scenario genai-evaluations
  uv run scripts/list_prompt_templates.py --name eval --json | jq -r '.[].id'
"""

import argparse
import json
import sys

from _rest import get_rest_context, request


def main():
    parser = argparse.ArgumentParser(
        description="List Prompt Registry prompt templates.",
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
    body = request("GET", f"{base_url}/lm/promptTemplates", headers)
    templates = body.get("resources", []) if isinstance(body, dict) else []

    def keep(t):
        if args.scenario and t.get("scenario") != args.scenario:
            return False
        if args.name and args.name.lower() not in (t.get("name") or "").lower():
            return False
        return True

    templates = [t for t in templates if keep(t)]

    if args.as_json:
        out = [{"id": t.get("id"), "name": t.get("name"), "version": t.get("version"),
                "scenario": t.get("scenario")} for t in templates]
        print(json.dumps(out, indent=2))
        return

    if not templates:
        print("No prompt templates found.")
        return

    for t in templates:
        print(f"{t.get('name')} v{t.get('version')}  id={t.get('id')}")
        if args.response_format == "detailed":
            print(f"       scenario={t.get('scenario')}")

    print(f"{len(templates)} template(s) found.")


if __name__ == "__main__":
    main()
