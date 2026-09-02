# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
List or inspect executables for a SAP AI Core scenario.

Usage:
  uv run scripts/get_executables.py --scenario-id SCENARIO_ID [options]

Options:
  --scenario-id ID          Scenario ID (required)
  --executable-id ID        Get a specific executable by ID
  --response-format FORMAT  Output format: concise or detailed (default: concise)
  --json                    Emit JSON to stdout
  --resource-group GROUP    Resource group override

Exit codes:
  0 - Success
  1 - Error

JSON structure:
  list: [{"id": "...", "name": "...", "description": "..."}, ...]
  get:  [{"id": "...", "name": "...", "scenario_id": "...", "description": "...", "parameters": [{"name": "...", "description": "...", "default": "..."}], "input_artifacts": [{"name": "...", "kind": "..."}], "output_artifacts": [{"name": "...", "kind": "..."}]}]

Examples:
  uv run scripts/get_executables.py --scenario-id my-scenario
  uv run scripts/get_executables.py --scenario-id my-scenario --executable-id my-executable
  uv run scripts/get_executables.py --scenario-id my-scenario --json
  uv run scripts/get_executables.py --scenario-id my-scenario --response-format detailed
"""

import argparse
import json
import sys


def _get_client(resource_group=None):
    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add \"sap-ai-sdk-core>=3.3.0\"", file=sys.stderr)
        sys.exit(1)
    try:
        kwargs = {}
        if resource_group:
            kwargs["resource_group"] = resource_group
        return AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills", **kwargs)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


def list_executables(args):
    client = _get_client(args.resource_group)
    try:
        resp = client.executable.query(scenario_id=args.scenario_id)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    items = resp.resources if hasattr(resp, "resources") else (resp if isinstance(resp, list) else [])

    if args.as_json:
        rows = []
        for item in items:
            rows.append({
                "id": item.id if hasattr(item, "id") else "",
                "name": item.name if hasattr(item, "name") else "",
                "description": item.description if hasattr(item, "description") else "",
            })
        print(json.dumps(rows, indent=2))
        return

    if not items:
        print("0 executable(s) found.")
        return

    rows = [
        {
            "id": item.id if hasattr(item, "id") else "",
            "name": item.name if hasattr(item, "name") else "",
            "description": item.description if hasattr(item, "description") else "",
        }
        for item in items
    ]

    colw = lambda key, hdr: max(max(len(r[key]) for r in rows), len(hdr))

    id_w = colw("id", "ID")
    name_w = colw("name", "NAME")

    if args.response_format == "detailed":
        header = f"{'ID':<{id_w}}  {'NAME':<{name_w}}  DESCRIPTION"
        print(header)
        print("-" * len(header))
        for r in rows:
            print(f"{r['id']:<{id_w}}  {r['name']:<{name_w}}  {r['description']}")
    else:
        header = f"{'ID':<{id_w}}  NAME"
        print(header)
        print("-" * len(header))
        for r in rows:
            print(f"{r['id']:<{id_w}}  {r['name']}")

    print(f"{len(rows)} executable(s) found.")


def get_executable(args):
    client = _get_client(args.resource_group)
    try:
        item = client.executable.get(scenario_id=args.scenario_id, executable_id=args.executable_id)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    def _extract_params(item):
        params = []
        raw = item.parameters if hasattr(item, "parameters") else []
        if raw:
            for p in raw:
                params.append({
                    "name": p.name if hasattr(p, "name") else "",
                    "description": p.description if hasattr(p, "description") else "",
                    "default": p.default if hasattr(p, "default") else "",
                })
        return params

    def _extract_artifacts(attr):
        artifacts = []
        raw = getattr(item, attr, []) or []
        for a in raw:
            kind = a.kind.value if hasattr(a, "kind") and hasattr(a.kind, "value") else str(getattr(a, "kind", ""))
            artifacts.append({
                "name": a.name if hasattr(a, "name") else "",
                "kind": kind,
            })
        return artifacts

    if args.as_json:
        row = {
            "id": item.id if hasattr(item, "id") else "",
            "name": item.name if hasattr(item, "name") else "",
            "scenario_id": item.scenario_id if hasattr(item, "scenario_id") else args.scenario_id,
            "description": item.description if hasattr(item, "description") else "",
            "parameters": _extract_params(item),
            "input_artifacts": _extract_artifacts("input_artifacts"),
            "output_artifacts": _extract_artifacts("output_artifacts"),
        }
        print(json.dumps([row], indent=2))
        return

    exe_id = item.id if hasattr(item, "id") else ""
    exe_name = item.name if hasattr(item, "name") else ""
    exe_desc = item.description if hasattr(item, "description") else ""
    exe_scenario = item.scenario_id if hasattr(item, "scenario_id") else args.scenario_id

    print(f"ID          : {exe_id}")
    print(f"Name        : {exe_name}")
    print(f"Scenario ID : {exe_scenario}")

    if args.response_format == "detailed":
        print(f"Description : {exe_desc}")

        params = _extract_params(item)
        if params:
            print("Parameters  :")
            for p in params:
                default_str = f" (default: {p['default']})" if p["default"] else ""
                print(f"  {p['name']}{default_str} - {p['description']}")

        input_artifacts = _extract_artifacts("input_artifacts")
        if input_artifacts:
            print("Input Artifacts  :")
            for a in input_artifacts:
                print(f"  {a['name']} ({a['kind']})")

        output_artifacts = _extract_artifacts("output_artifacts")
        if output_artifacts:
            print("Output Artifacts :")
            for a in output_artifacts:
                print(f"  {a['name']} ({a['kind']})")

    print("1 executable(s) found.")


def main():
    parser = argparse.ArgumentParser(
        description="List or inspect executables for a SAP AI Core scenario.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  uv run scripts/get_executables.py --scenario-id my-scenario
  uv run scripts/get_executables.py --scenario-id my-scenario --executable-id my-executable
  uv run scripts/get_executables.py --scenario-id my-scenario --json
  uv run scripts/get_executables.py --scenario-id my-scenario --response-format detailed
""",
    )
    parser.add_argument("--scenario-id", required=True, dest="scenario_id", help="Scenario ID")
    parser.add_argument("--executable-id", dest="executable_id", default=None, help="Get a specific executable by ID")
    parser.add_argument(
        "--response-format",
        dest="response_format",
        choices=["concise", "detailed"],
        default="concise",
        help="Output format (default: concise)",
    )
    parser.add_argument("--json", dest="as_json", action="store_true", help="Emit JSON to stdout")
    parser.add_argument("--resource-group", dest="resource_group", default=None, help="Resource group override")

    args = parser.parse_args()

    if args.executable_id:
        get_executable(args)
    else:
        list_executables(args)


if __name__ == "__main__":
    main()
