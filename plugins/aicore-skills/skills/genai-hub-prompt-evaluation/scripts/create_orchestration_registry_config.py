# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Create a prompt-registry (orchestration registry) configuration in SAP AI Core.

An evaluation runs one or more prompt-registry configs against the test dataset — each config
defines the prompt template (and optionally grounding/RAG, model, etc.) whose output is scored.
This is the "orchestrationRegistryIds" input to create_evaluation_configuration.py.

The config body is read from a JSON file. See templates/orchestration-registry-config.json for a
full example (prompt_templating + document grounding). --name / --version / --scenario override
the corresponding fields in the file when provided.

Endpoint: POST /registry/v2/orchestrationConfigs

Usage:
  uv run scripts/create_orchestration_registry_config.py --file templates/orchestration-registry-config.json
  uv run scripts/create_orchestration_registry_config.py --file cfg.json --name my-cfg --version 0.0.2 --json

Options:
  --file PATH           Path to a JSON file with the config body (required)
  --name NAME           Override the config name
  --version VERSION     Override the config version
  --scenario ID         Override the scenario (default in file: genai-evaluations)
  --json                Emit JSON to stdout
  --resource-group RG   Resource group override

Exit codes:
  0 - Success
  1 - Error

JSON structure:
  {"id": "...", "name": "...", "version": "...", "scenario": "...", "message": "..."}

Examples:
  uv run scripts/create_orchestration_registry_config.py --file templates/orchestration-registry-config.json
  uv run scripts/create_orchestration_registry_config.py --file cfg.json --json | jq -r .id
"""

import argparse
import json
import sys

from _rest import get_rest_context, request


def main():
    parser = argparse.ArgumentParser(
        description="Create a prompt-registry (orchestration registry) config in SAP AI Core.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--file", required=True, help="Path to a JSON config-body file")
    parser.add_argument("--name", default=None, help="Override the config name")
    parser.add_argument("--version", default=None, help="Override the config version")
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
            print(f"ERROR: config body is missing required field: {field}", file=sys.stderr)
            sys.exit(1)

    base_url, headers = get_rest_context(args.resource_group)
    result = request("POST", f"{base_url}/registry/v2/orchestrationConfigs", headers, json_body=body)

    config_id = result.get("id") if isinstance(result, dict) else None
    message = result.get("message", "Orchestration config created.") if isinstance(result, dict) else ""

    if args.as_json:
        print(json.dumps({
            "id": config_id,
            "name": body.get("name"),
            "version": body.get("version"),
            "scenario": body.get("scenario"),
            "message": message,
        }, indent=2))
    else:
        print(config_id or "")
        print(f"{message} (name={body.get('name')} v{body.get('version')})", file=sys.stderr)


if __name__ == "__main__":
    main()
