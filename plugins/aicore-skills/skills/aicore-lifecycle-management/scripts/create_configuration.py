# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
Create a SAP AI Core configuration.

Usage:
  uv run scripts/create_configuration.py [options]

Options:
  --name NAME                   Configuration name (required)
  --scenario-id ID              Scenario ID (required)
  --executable-id ID            Executable ID (required)
  --param KEY=VALUE             Parameter binding (repeatable)
  --artifact KEY=ARTIFACT_ID    Input artifact binding (repeatable)
  --resource-group GROUP        Resource group override
  --json                        Emit JSON to stdout
  --response-format FORMAT      Output format: concise or detailed (default: concise)

Exit codes:
  0 - Success
  1 - Error

JSON structure:
  {"id": "<configuration-id>", "message": "Configuration created."}

Examples:
  uv run scripts/create_configuration.py --name my-config --scenario-id my-scenario --executable-id my-exe
  uv run scripts/create_configuration.py --name my-config --scenario-id s1 --executable-id e1 --param epochs=10 --param lr=0.01
  uv run scripts/create_configuration.py --name my-config --scenario-id s1 --executable-id e1 --artifact model=abc-123 --json
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


def parse_key_value(value, flag_name):
    if "=" not in value:
        print(f"ERROR: {flag_name} must be in KEY=VALUE format, got: {value!r}", file=sys.stderr)
        sys.exit(1)
    k, v = value.split("=", 1)
    return k.strip(), v.strip()


def main():
    parser = argparse.ArgumentParser(
        description="Create a SAP AI Core configuration.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--name", required=True, help="Configuration name")
    parser.add_argument("--scenario-id", required=True, dest="scenario_id", help="Scenario ID")
    parser.add_argument("--executable-id", required=True, dest="executable_id", help="Executable ID")
    parser.add_argument("--param", metavar="KEY=VALUE", action="append", default=[], help="Parameter binding (repeatable)")
    parser.add_argument("--artifact", metavar="KEY=ARTIFACT_ID", action="append", default=[], help="Input artifact binding (repeatable)")
    parser.add_argument("--resource-group", dest="resource_group", default=None, help="Resource group override")
    parser.add_argument("--json", dest="as_json", action="store_true", help="Emit JSON to stdout")
    parser.add_argument("--response-format", choices=["concise", "detailed"], default="concise", help="Output format (default: concise)")

    args = parser.parse_args()

    from ai_api_client_sdk.models.parameter_binding import ParameterBinding
    from ai_api_client_sdk.models.input_artifact_binding import InputArtifactBinding

    parameter_bindings = []
    for raw in args.param:
        k, v = parse_key_value(raw, "--param")
        parameter_bindings.append(ParameterBinding(key=k, value=v))

    input_artifact_bindings = []
    for raw in args.artifact:
        k, v = parse_key_value(raw, "--artifact")
        input_artifact_bindings.append(InputArtifactBinding(key=k, artifact_id=v))

    client = _get_client(resource_group=args.resource_group)

    try:
        result = client.configuration.create(
            name=args.name,
            scenario_id=args.scenario_id,
            executable_id=args.executable_id,
            parameter_bindings=parameter_bindings,
            input_artifact_bindings=input_artifact_bindings,
        )
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    config_id = result.id if hasattr(result, "id") else str(result)
    message = result.message if hasattr(result, "message") else "Configuration created."

    if args.as_json:
        print(json.dumps({"id": config_id, "message": message}, indent=2))
    else:
        print(f"Created  : {config_id}")


if __name__ == "__main__":
    main()
