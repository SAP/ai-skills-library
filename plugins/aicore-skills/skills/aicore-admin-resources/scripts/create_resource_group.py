# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
Create a SAP AI Core resource group.

Usage:
  uv run scripts/create_resource_group.py --id <id>
  uv run scripts/create_resource_group.py --id <id> --label key=value [--label key2=value2 ...]

Options:
  --id ID             Resource group ID (3–10 lowercase alphanumeric characters, required)
  --label KEY=VALUE   Label to attach (repeatable, optional)
  --json              Emit JSON instead of plain text

Exit codes:
  0  Success
  1  Error

examples:
  uv run scripts/create_resource_group.py --id my-rg
  uv run scripts/create_resource_group.py --id my-rg --label team=data --label env=prod
"""

import argparse
import json
import re
import sys


def validate_id(rg_id: str) -> None:
    if not 3 <= len(rg_id) <= 10:
        raise ValueError(f"Resource group ID must be 3–10 characters (got {len(rg_id)})")
    if not re.match(r"^[a-z0-9][a-z0-9\-]*[a-z0-9]$", rg_id):
        raise ValueError(
            f"Invalid resource group ID '{rg_id}': must be lowercase alphanumeric or hyphens, "
            "start and end with alphanumeric"
        )


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
        description="Create a SAP AI Core resource group.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  uv run scripts/create_resource_group.py --id my-rg
  uv run scripts/create_resource_group.py --id my-rg --label team=data --label env=prod
""",
    )
    parser.add_argument("--id", metavar="ID", dest="rg_id", required=True,
                        help="Resource group ID (3–10 characters)")
    parser.add_argument("--label", metavar="KEY=VALUE", action="append", default=[],
                        help="Label as key=value pair (repeatable)")
    parser.add_argument("--json", action="store_true", dest="as_json",
                        help="Emit JSON instead of plain text")
    return parser.parse_args()


def fmt_status(rg) -> str:
    status = getattr(rg, "status", None)
    if status is None:
        return ""
    return status.value if hasattr(status, "value") else str(status)


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

    try:
        validate_id(args.rg_id)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    client = _get_client()
    labels = parse_labels(args.label) if args.label else None

    try:
        response = client.resource_groups.create(resource_group_id=args.rg_id, labels=labels)
    except Exception as e:
        print(f"ERROR: Failed to create resource group '{args.rg_id}': {e}", file=sys.stderr)
        sys.exit(1)

    status = fmt_status(response)

    if args.as_json:
        print(json.dumps({"resource_group_id": args.rg_id, "status": status}, indent=2))
    else:
        print(f"Created  : {args.rg_id}")
        if status:
            print(f"Status   : {status}")


if __name__ == "__main__":
    main()
