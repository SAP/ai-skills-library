# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Create a new scenario configuration.

Usage:
  uv run scripts/create_scenario_config.py --name <name> --tabular-artifacts ta1,ta2,...
      [--description TEXT] [--strategy random|embedding]
      [--labels KEY=VALUE ...]

Examples:
  uv run scripts/create_scenario_config.py \\
      --name my-scenario --tabular-artifacts customer-ta,orders-ta

  uv run scripts/create_scenario_config.py \\
      --name my-scenario --tabular-artifacts customer-ta,orders-ta \\
      --description "Production HR scenario" --strategy embedding \\
      --labels ext.ai.sap.com/env=prod
"""

import argparse
import sys

import requests


def parse_labels(raw: list[str]) -> list[dict]:
    labels = []
    for item in raw:
        if "=" not in item:
            print(f"ERROR: label '{item}' must be in key=value format", file=sys.stderr)
            sys.exit(1)
        key, value = item.split("=", 1)
        labels.append({"key": key, "value": value})
    return labels


def main():
    parser = argparse.ArgumentParser(description="Create a scenario configuration")
    parser.add_argument("--name", required=True, help="Scenario configuration name (1-127 chars, kebab-case)")
    parser.add_argument("--tabular-artifacts", required=True, dest="tabular_artifacts",
                        help="Comma-separated list of tabular artifact names")
    parser.add_argument("--description", help="Optional description")
    parser.add_argument("--strategy", choices=["random", "embedding"], dest="strategy",
                        help="Context selection strategy (default: random)")
    parser.add_argument("--labels", nargs="+", default=[], metavar="KEY=VALUE",
                        help="Labels, e.g. ext.ai.sap.com/env=prod")
    parser.add_argument("--resource-group", metavar="RG", help="AI-Resource-Group header value. Overrides env/SDK default.")
    args = parser.parse_args()

    ta_names = [t.strip() for t in args.tabular_artifacts.split(",") if t.strip()]
    if not ta_names:
        print("ERROR: --tabular-artifacts must contain at least one name", file=sys.stderr)
        sys.exit(1)
    ta_objects = [{"name": n} for n in ta_names]

    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add sap-ai-sdk-core", file=sys.stderr)
        sys.exit(2)

    client = AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills")
    base_url = client.rest_client.base_url.rstrip("/")
    token = client.rest_client.get_token()
    rg = args.resource_group or client.rest_client.headers.get("AI-Resource-Group", "default")

    body: dict = {"tabularArtifacts": ta_objects}
    if args.description:
        body["description"] = args.description
    if args.strategy:
        body["contextSelectionStrategy"] = args.strategy
    if args.labels:
        body["labels"] = parse_labels(args.labels)

    url = f"{base_url}/tcr/scenarioConfigurations/{args.name}"
    headers = {"Authorization": token, "AI-Resource-Group": rg, "Content-Type": "application/json"}

    resp = requests.put(url, headers=headers, json=body, timeout=30)

    if resp.status_code == 400:
        err_text = resp.text
        err_lower = err_text.lower()
        # Landscape hasn't rolled out the new contract yet — retry with the legacy format.
        # Only trigger when the field itself is rejected as unknown/unrecognized, not for
        # validation errors on the field's contents (e.g. invalid artifact names).
        _UNKNOWN_FIELD = ("unknown", "unrecognized", "unexpected")
        if "tabularartifacts" in err_lower and "tabularartifacts[" not in err_lower and any(
            kw in err_lower for kw in _UNKNOWN_FIELD
        ):
            print("Note: landscape does not support new contract yet, retrying with legacy format", file=sys.stderr)
            legacy_url = f"{base_url}/api/v1/tcr/scenarioConfigurations"
            legacy_body = {"name": args.name, "tabularArtifactNames": ta_names}
            resp = requests.post(legacy_url, headers=headers, json=legacy_body, timeout=30)
        if not resp.ok:
            print(f"ERROR {resp.status_code}: {resp.text}", file=sys.stderr)
            sys.exit(1)
    elif not resp.ok:
        print(f"ERROR {resp.status_code}: {resp.text}", file=sys.stderr)
        sys.exit(1)

    result = resp.json()
    ta_confirmed = (
        ", ".join(t["name"] for t in result.get("tabularArtifacts", []))
        or ", ".join(result.get("tabularArtifactNames", []))
    )
    print(f"Created scenario configuration: {result['name']}")
    if ta_confirmed:
        print(f"Tabular artifacts: {ta_confirmed}")


if __name__ == "__main__":
    main()
