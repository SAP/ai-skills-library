# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Update an existing scenario configuration.
At least one of --tabular-artifacts, --strategy, --labels, or --description must be provided.
Replaces the fields you supply — omitted fields are left unchanged.

Usage:
  uv run scripts/patch_scenario_config.py --name <name> [OPTIONS]

Options:
  --tabular-artifacts ta1,ta2,...   Replace the entire tabular artifact list
  --strategy random|embedding       Update context selection strategy
  --labels KEY=VALUE [...]          Replace the entire label set
  --description TEXT                Update the description

Examples:
  uv run scripts/patch_scenario_config.py \\
      --name my-scenario --tabular-artifacts customer-ta,orders-ta,inventory-ta

  uv run scripts/patch_scenario_config.py \\
      --name my-scenario --strategy embedding --labels ext.ai.sap.com/env=prod
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
    parser = argparse.ArgumentParser(description="Update a scenario configuration")
    parser.add_argument("--name", required=True, help="Scenario configuration name")
    parser.add_argument("--tabular-artifacts", dest="tabular_artifacts",
                        help="Comma-separated list of tabular artifact names (replaces existing list)")
    parser.add_argument("--strategy", choices=["random", "embedding"], dest="strategy",
                        help="Context selection strategy")
    parser.add_argument("--labels", nargs="+", default=None, metavar="KEY=VALUE",
                        help="Labels to set (replaces all existing labels)")
    parser.add_argument("--description", help="Updated description")
    parser.add_argument("--resource-group", metavar="RG", help="AI-Resource-Group header value. Overrides env/SDK default.")
    args = parser.parse_args()

    body: dict = {}

    if args.tabular_artifacts is not None:
        ta_names = [t.strip() for t in args.tabular_artifacts.split(",") if t.strip()]
        if not ta_names:
            print("ERROR: --tabular-artifacts must contain at least one name", file=sys.stderr)
            sys.exit(1)
        body["tabularArtifacts"] = [{"name": n} for n in ta_names]
    else:
        ta_names = []

    if args.strategy:
        body["contextSelectionStrategy"] = args.strategy
    if args.labels is not None:
        body["labels"] = parse_labels(args.labels)
    if args.description is not None:
        body["description"] = args.description

    if not body:
        print("ERROR: at least one of --tabular-artifacts, --strategy, --labels, or --description must be provided",
              file=sys.stderr)
        sys.exit(1)

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
    headers = {"Authorization": token, "AI-Resource-Group": rg, "Content-Type": "application/json"}

    resp = requests.patch(url, headers=headers, json=body, timeout=15)

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
            legacy_body = {"tabularArtifactNames": ta_names}
            resp = requests.patch(url, headers=headers, json=legacy_body, timeout=15)
        if not resp.ok:
            print(f"ERROR {resp.status_code}: {resp.text}", file=sys.stderr)
            sys.exit(1)

    if resp.status_code == 204:
        print(f"Updated scenario configuration: {args.name}")
        if ta_names:
            print(f"New tabular artifacts: {', '.join(ta_names)}")
    elif resp.status_code == 404:
        print(f"Not found: {args.name}", file=sys.stderr)
        sys.exit(1)
    elif not resp.ok:
        print(f"ERROR {resp.status_code}: {resp.text}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
