# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
Delete a SAP AI Core resource group.

Usage:
  uv run scripts/delete_resource_group.py --id <id> --confirm
  uv run scripts/delete_resource_group.py --id <id> --confirm --json

Options:
  --id ID       Resource group ID to delete (required)
  --confirm     Required safety flag to confirm deletion
  --json        Emit JSON instead of plain text

Exit codes:
  0  Success
  1  Error / missing --confirm

examples:
  uv run scripts/delete_resource_group.py --id my-rg --confirm
  uv run scripts/delete_resource_group.py --id my-rg --confirm --json
"""

import argparse
import json
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Delete a SAP AI Core resource group.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  uv run scripts/delete_resource_group.py --id my-rg --confirm
  uv run scripts/delete_resource_group.py --id my-rg --confirm --json
""",
    )
    parser.add_argument("--id", metavar="ID", dest="rg_id", required=True,
                        help="Resource group ID to delete")
    parser.add_argument("--confirm", action="store_true",
                        help="Required safety flag to confirm deletion")
    parser.add_argument("--json", action="store_true", dest="as_json",
                        help="Emit JSON instead of plain text")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not args.confirm:
        print(f"ERROR: Pass --confirm to delete resource group '{args.rg_id}'.", file=sys.stderr)
        sys.exit(1)

    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add \"sap-ai-sdk-core>=3.3.0\"", file=sys.stderr)
        sys.exit(1)

    try:
        client = AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills")
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        response = client.resource_groups.delete(resource_group_id=args.rg_id)
    except Exception as e:
        print(f"ERROR: Failed to delete resource group '{args.rg_id}': {e}", file=sys.stderr)
        sys.exit(1)

    message = getattr(response, "message", "") or ""

    if args.as_json:
        print(json.dumps({"resource_group_id": args.rg_id, "message": message}, indent=2))
    else:
        print(f"Deleted  : {args.rg_id}")
        if message:
            print(f"Message  : {message}")


if __name__ == "__main__":
    main()
