# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
Update labels on a SAP AI Core resource group.

Usage:
  uv run scripts/patch_resource_group.py --id <id> --label key=value [--label key2=value2 ...]

Options:
  --id ID             Resource group ID (required)
  --label KEY=VALUE   Label as key=value pair (repeatable, required)
  --json              Emit JSON instead of plain text

Exit codes:
  0  Success
  1  Error

Note: patch replaces the full label set on the resource group.

examples:
  uv run scripts/patch_resource_group.py --id my-rg --label team=data
  uv run scripts/patch_resource_group.py --id my-rg --label team=data --label env=prod
"""

import argparse
import json
import sys


def parse_labels(label_args: list[str]):
    from ai_api_client_sdk.models.label import Label
    labels = []
    for item in label_args:
        if "=" not in item:
            print(f"ERROR: --label value '{item}' is not in key=value format", file=sys.stderr)
            sys.exit(1)
        key, _, value = item.partition("=")
        labels.append(Label(key=key, value=value))
    return labels


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Update labels on a SAP AI Core resource group.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  uv run scripts/patch_resource_group.py --id my-rg --label team=data
  uv run scripts/patch_resource_group.py --id my-rg --label team=data --label env=prod
""",
    )
    parser.add_argument("--id", metavar="ID", dest="rg_id", required=True,
                        help="Resource group ID")
    parser.add_argument("--label", metavar="KEY=VALUE", action="append", required=True,
                        help="Label as key=value pair (repeatable)")
    parser.add_argument("--json", action="store_true", dest="as_json",
                        help="Emit JSON instead of plain text")
    return parser.parse_args()


def _get_client():
    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add \"sap-ai-sdk-core>=3.3.0\"", file=sys.stderr)
        sys.exit(1)
    try:
        return AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills")
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    args = parse_args()
    client = _get_client()
    labels = parse_labels(args.label)

    try:
        client.resource_groups.modify(resource_group_id=args.rg_id, labels=labels)
    except Exception as e:
        print(f"ERROR: Failed to update resource group '{args.rg_id}': {e}", file=sys.stderr)
        sys.exit(1)

    if args.as_json:
        print(json.dumps({"resource_group_id": args.rg_id}, indent=2))
    else:
        print(f"Updated  : {args.rg_id}")


if __name__ == "__main__":
    main()
