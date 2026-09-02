# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
List or inspect SAP AI Core configurations.

Usage:
  uv run scripts/get_configurations.py [options]

Options:
  --configuration-id ID   Get a single configuration by ID
  --scenario-id ID        Filter list by scenario ID
  --response-format FMT   Output format: concise or detailed (default: concise)
  --json                  Emit JSON to stdout
  --resource-group RG     Override resource group

Exit codes:
  0 - Success
  1 - Error

JSON structure:
  list: [{"id", "name", "scenario_id", "executable_id", "created_at"}, ...]
  get:  [{"id", "name", "scenario_id", "executable_id", "created_at", "parameter_bindings", "input_artifact_bindings"}]

Examples:
  uv run scripts/get_configurations.py
  uv run scripts/get_configurations.py --scenario-id my-scenario
  uv run scripts/get_configurations.py --configuration-id abc123
  uv run scripts/get_configurations.py --json | jq '.[].name'
"""

import argparse
import json
import sys


def fmt_ts(value) -> str:
    return str(value)[:19] if value else ""


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


def list_configurations(client, scenario_id, response_format, as_json):
    try:
        kwargs = {}
        if scenario_id:
            kwargs["scenario_id"] = scenario_id
        result = client.configuration.query(**kwargs)
        configs = result.resources if hasattr(result, "resources") else (result if isinstance(result, list) else [])
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    rows = []
    for c in configs:
        row = {
            "id": c.id or "",
            "name": c.name or "",
            "scenario_id": c.scenario_id or "",
            "executable_id": c.executable_id or "",
            "created_at": fmt_ts(c.created_at),
        }
        if response_format == "detailed":
            pb = []
            if c.parameter_bindings:
                for p in c.parameter_bindings:
                    pb.append({"key": p.key, "value": p.value})
            iab = []
            if c.input_artifact_bindings:
                for a in c.input_artifact_bindings:
                    iab.append({"key": a.key, "artifact_id": a.artifact_id})
            row["parameter_bindings"] = pb
            row["input_artifact_bindings"] = iab
        rows.append(row)

    if as_json:
        print(json.dumps(rows, indent=2))
        return

    if not rows:
        print("0 configuration(s) found.")
        return

    w_id = max(max(len(r["id"]) for r in rows), len("ID"))
    w_name = max(max(len(r["name"]) for r in rows), len("NAME"))
    w_scenario = max(max(len(r["scenario_id"]) for r in rows), len("SCENARIO"))
    w_executable = max(max(len(r["executable_id"]) for r in rows), len("EXECUTABLE"))
    w_created = max(max(len(r["created_at"]) for r in rows), len("CREATED"))

    header = (
        f"{'ID':<{w_id}}  {'NAME':<{w_name}}  {'SCENARIO':<{w_scenario}}  "
        f"{'EXECUTABLE':<{w_executable}}  {'CREATED':<{w_created}}"
    )
    print(header)
    print("-" * len(header))

    for r in rows:
        print(
            f"{r['id']:<{w_id}}  {r['name']:<{w_name}}  {r['scenario_id']:<{w_scenario}}  "
            f"{r['executable_id']:<{w_executable}}  {r['created_at']}"
        )

    if response_format == "detailed":
        for r in rows:
            print()
            print(f"Configuration: {r['id']}")
            pb = r.get("parameter_bindings", [])
            if pb:
                print("  Parameter Bindings:")
                for p in pb:
                    print(f"    {p['key']} = {p['value']}")
            else:
                print("  Parameter Bindings: (none)")
            iab = r.get("input_artifact_bindings", [])
            if iab:
                print("  Input Artifact Bindings:")
                for a in iab:
                    print(f"    {a['key']} -> {a['artifact_id']}")
            else:
                print("  Input Artifact Bindings: (none)")

    print(f"\n{len(rows)} configuration(s) found.")


def get_configuration(client, configuration_id, response_format, as_json):
    try:
        c = client.configuration.get(configuration_id)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    pb = []
    if c.parameter_bindings:
        for p in c.parameter_bindings:
            pb.append({"key": p.key, "value": p.value})
    iab = []
    if c.input_artifact_bindings:
        for a in c.input_artifact_bindings:
            iab.append({"key": a.key, "artifact_id": a.artifact_id})

    row = {
        "id": c.id or "",
        "name": c.name or "",
        "scenario_id": c.scenario_id or "",
        "executable_id": c.executable_id or "",
        "created_at": fmt_ts(c.created_at),
        "parameter_bindings": pb,
        "input_artifact_bindings": iab,
    }

    if as_json:
        print(json.dumps([row], indent=2))
        return

    w_label = len("Executable ID")
    print(f"{'ID':<{w_label}} : {row['id']}")
    print(f"{'Name':<{w_label}} : {row['name']}")
    print(f"{'Scenario ID':<{w_label}} : {row['scenario_id']}")
    print(f"{'Executable ID':<{w_label}} : {row['executable_id']}")
    print(f"{'Created':<{w_label}} : {row['created_at']}")

    if response_format == "detailed":
        print()
        if pb:
            print("Parameter Bindings:")
            for p in pb:
                print(f"  {p['key']} = {p['value']}")
        else:
            print("Parameter Bindings: (none)")

        if iab:
            print("Input Artifact Bindings:")
            for a in iab:
                print(f"  {a['key']} -> {a['artifact_id']}")
        else:
            print("Input Artifact Bindings: (none)")


def main():
    parser = argparse.ArgumentParser(
        description="List or inspect SAP AI Core configurations.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  uv run scripts/get_configurations.py
  uv run scripts/get_configurations.py --scenario-id my-scenario
  uv run scripts/get_configurations.py --configuration-id abc123
  uv run scripts/get_configurations.py --json | jq '.[].name'
        """,
    )
    parser.add_argument("--configuration-id", dest="configuration_id", default=None, help="Get a single configuration by ID")
    parser.add_argument("--scenario-id", dest="scenario_id", default=None, help="Filter list by scenario ID")
    parser.add_argument(
        "--response-format",
        dest="response_format",
        choices=["concise", "detailed"],
        default="concise",
        help="Output format: concise or detailed (default: concise)",
    )
    parser.add_argument("--json", dest="as_json", action="store_true", help="Emit JSON to stdout")
    parser.add_argument("--resource-group", dest="resource_group", default=None, help="Override resource group")
    args = parser.parse_args()

    client = _get_client(resource_group=args.resource_group)

    if args.configuration_id:
        get_configuration(client, args.configuration_id, args.response_format, args.as_json)
    else:
        list_configurations(client, args.scenario_id, args.response_format, args.as_json)


if __name__ == "__main__":
    main()
