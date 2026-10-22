# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Create (or reuse) a Prompt Template in the SAP AI Core Prompt Registry.

This backs the "prompt registry" evaluation type: the template's ID is bound to the evaluation
configuration via --prompt-template-id (parameter key `promptTemplate`), and the models to
benchmark are supplied via --models. Create-or-get by name + scenario + version keeps it
idempotent.

Endpoints: GET/POST /lm/promptTemplates

The template body is read from a JSON file: {"name", "version", "scenario", "spec"} where spec is
{"template": [ {"role": "user", "content": "... {{?var}} ..."} ]}. See templates/prompt-template.json.
--name / --version / --scenario override the file when provided.

Usage:
  uv run scripts/create_prompt_template.py --file templates/prompt-template.json
  uv run scripts/create_prompt_template.py --file templates/prompt-template.json --name my-tmpl --version 1.0.0 --json

Options:
  --file PATH           Path to a JSON prompt-template body file (required)
  --name NAME           Override the template name
  --version VERSION     Override the template version
  --scenario ID         Override the scenario (default in file: genai-evaluations)
  --json                Emit JSON to stdout
  --resource-group RG   Resource group override

Exit codes:
  0 - Success
  1 - Error

JSON structure:
  {"id": "...", "name": "...", "version": "...", "scenario": "...", "created": bool}

Examples:
  uv run scripts/create_prompt_template.py --file templates/prompt-template.json
  uv run scripts/create_prompt_template.py --file templates/prompt-template.json --json | jq -r .id
"""

import argparse
import json
import sys

from _rest import get_rest_context, request


def find_existing(base_url, headers, name, scenario, version):
    """Return the ID of a matching prompt template, or None."""
    from urllib.parse import urlencode

    params = {"name": name, "scenario": scenario}
    if version:
        params["version"] = version
    url = f"{base_url}/lm/promptTemplates?{urlencode(params)}"
    body = request("GET", url, headers)
    resources = body.get("resources", []) if isinstance(body, dict) else []
    if resources:
        return resources[0].get("id")
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Create or reuse a Prompt Registry prompt template.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--file", required=True, help="Path to a JSON prompt-template body file")
    parser.add_argument("--name", default=None, help="Override the template name")
    parser.add_argument("--version", default=None, help="Override the template version")
    parser.add_argument("--scenario", default=None, help="Override the scenario")
    parser.add_argument("--json", dest="as_json", action="store_true")
    parser.add_argument("--resource-group", dest="resource_group", default=None)
    args = parser.parse_args()

    try:
        with open(args.file, "r", encoding="utf-8") as fh:
            body = json.load(fh)
    except OSError as e:
        print(f"ERROR: could not read {args.file}: {e}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: {args.file} is not valid JSON: {e}", file=sys.stderr)
        sys.exit(1)

    if args.name:
        body["name"] = args.name
    if args.version:
        body["version"] = args.version
    if args.scenario:
        body["scenario"] = args.scenario

    for field in ("name", "version", "scenario", "spec"):
        if field not in body:
            print(f"ERROR: prompt-template body is missing required field: {field}", file=sys.stderr)
            sys.exit(1)

    base_url, headers = get_rest_context(args.resource_group)
    endpoint = f"{base_url}/lm/promptTemplates"

    existing_id = find_existing(base_url, headers, body["name"], body["scenario"], body["version"])
    if existing_id:
        print(f"Reused   : {body['name']} v{body['version']} -> {existing_id}", file=sys.stderr)
        result = {"id": existing_id, "name": body["name"], "version": body["version"],
                  "scenario": body["scenario"], "created": False}
    else:
        created = request("POST", endpoint, headers, json_body=body)
        template_id = created.get("id") if isinstance(created, dict) else None
        print(f"Created  : {body['name']} v{body['version']} -> {template_id}", file=sys.stderr)
        result = {"id": template_id, "name": body["name"], "version": body["version"],
                  "scenario": body["scenario"], "created": True}

    if args.as_json:
        print(json.dumps(result, indent=2))
    else:
        print(result["id"] or "")


if __name__ == "__main__":
    main()
