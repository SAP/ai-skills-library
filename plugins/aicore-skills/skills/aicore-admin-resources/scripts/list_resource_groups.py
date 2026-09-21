# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
Query AI Core resource groups: list all or inspect one by ID.

Usage:
  uv run scripts/list_resource_groups.py
  uv run scripts/list_resource_groups.py --response-format detailed
  uv run scripts/list_resource_groups.py --json
  uv run scripts/list_resource_groups.py --resource-group-id <id>
  uv run scripts/list_resource_groups.py --resource-group-id <id> --response-format detailed
  uv run scripts/list_resource_groups.py --resource-group-id <id> --json

Options:
  --resource-group-id ID  Inspect a single resource group (omit to list all)
  --response-format       concise (default) or detailed
  --json                  Emit JSON instead of a table (pipe-friendly for | jq)

Exit codes:
  0  Success
  1  Error

json structure:
  list:           [{resource_group_id, status, created_at}, ...]
  list detailed:  [{resource_group_id, status, created_at, labels}, ...]
  get:            [{resource_group_id, status, created_at}]
  get detailed:   [{resource_group_id, status, created_at, labels}]
"""

import argparse
import json
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Query AI Core resource groups: list all or inspect one by ID.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  # List all resource groups (concise table):
  uv run scripts/list_resource_groups.py

  # Show detailed view (includes labels):
  uv run scripts/list_resource_groups.py --response-format detailed

  # JSON output — pipe to jq:
  uv run scripts/list_resource_groups.py --json
  uv run scripts/list_resource_groups.py --json | jq '.[0].resource_group_id'

  # Inspect a single resource group:
  uv run scripts/list_resource_groups.py --resource-group-id <id>
  uv run scripts/list_resource_groups.py --resource-group-id <id> --response-format detailed
  uv run scripts/list_resource_groups.py --resource-group-id <id> --json
""",
    )
    parser.add_argument(
        "--resource-group-id",
        dest="resource_group_id",
        metavar="ID",
        help="Inspect a single resource group by ID (omit to list all)",
    )
    parser.add_argument(
        "--response-format",
        dest="response_format",
        choices=["concise", "detailed"],
        default="concise",
        help="Output verbosity: concise (default) or detailed",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Emit JSON instead of a table",
    )
    return parser.parse_args()


def fmt_status(rg) -> str:
    status = getattr(rg, "status", None)
    if status is None:
        return ""
    return status.value if hasattr(status, "value") else str(status)


def fmt_ts(value) -> str:
    return str(value)[:19] if value else ""


def fmt_labels(rg) -> dict:
    labels = getattr(rg, "labels", None)
    if not labels:
        return {}
    if isinstance(labels, dict):
        return labels
    try:
        return {item.key: item.value for item in labels}
    except Exception:
        return {}


# ── List mode ─────────────────────────────────────────────────────────────────

def list_mode(client, args: argparse.Namespace) -> None:
    try:
        result = client.resource_groups.query()
        resource_groups = result.resources
    except Exception as e:
        print(f"ERROR: Failed to list resource groups: {e}", file=sys.stderr)
        sys.exit(1)

    if args.as_json:
        _print_list_json(resource_groups, args)
    else:
        _print_list_table(resource_groups, args)


def _print_list_json(resource_groups, args: argparse.Namespace) -> None:
    if args.response_format == "detailed":
        output = [
            {
                "resource_group_id": rg.resource_group_id,
                "status": fmt_status(rg),
                "created_at": str(getattr(rg, "created_at", "")),
                "labels": fmt_labels(rg),
            }
            for rg in resource_groups
        ]
    else:
        output = [
            {
                "resource_group_id": rg.resource_group_id,
                "status": fmt_status(rg),
                "created_at": str(getattr(rg, "created_at", "")),
            }
            for rg in resource_groups
        ]
    print(json.dumps(output, indent=2))


def _print_list_table(resource_groups, args: argparse.Namespace) -> None:
    if not resource_groups:
        print("No resource groups found.")
        return

    rows = [
        {
            "id": rg.resource_group_id,
            "status": fmt_status(rg),
            "created": fmt_ts(getattr(rg, "created_at", "")),
            "labels": json.dumps(fmt_labels(rg)),
        }
        for rg in resource_groups
    ]

    def colw(key: str, header: str) -> int:
        return max(max((len(r[key]) for r in rows), default=0), len(header))

    c_id = colw("id", "ID")
    c_st = colw("status", "STATUS")
    c_cr = colw("created", "CREATED")

    if args.response_format == "detailed":
        c_lb = colw("labels", "LABELS")
        fmt = f"{{id:<{c_id}}}  {{status:<{c_st}}}  {{created:<{c_cr}}}  {{labels:<{c_lb}}}"
        header = fmt.format(id="ID", status="STATUS", created="CREATED", labels="LABELS")
    else:
        fmt = f"{{id:<{c_id}}}  {{status:<{c_st}}}  {{created}}"
        header = fmt.format(id="ID", status="STATUS", created="CREATED")

    print(header)
    print("-" * len(header))
    for row in rows:
        print(fmt.format(**row))
    print(f"\n{len(resource_groups)} resource group(s) found.")


# ── Get mode ──────────────────────────────────────────────────────────────────

def get_mode(client, args: argparse.Namespace) -> None:
    try:
        rg = client.resource_groups.get(resource_group_id=args.resource_group_id)
    except Exception as e:
        print(f"ERROR: Failed to get resource group '{args.resource_group_id}': {e}", file=sys.stderr)
        sys.exit(1)

    status = fmt_status(rg)

    if args.as_json:
        _print_get_json(rg, status, args)
    else:
        _print_get_table(rg, status, args)


def _print_get_json(rg, status: str, args: argparse.Namespace) -> None:
    if args.response_format == "detailed":
        output = {
            "resource_group_id": rg.resource_group_id,
            "status": status,
            "created_at": str(getattr(rg, "created_at", "")),
            "labels": fmt_labels(rg),
        }
    else:
        output = {
            "resource_group_id": rg.resource_group_id,
            "status": status,
            "created_at": str(getattr(rg, "created_at", "")),
        }
    print(json.dumps([output], indent=2))


def _print_get_table(rg, status: str, args: argparse.Namespace) -> None:
    print(f"Resource Group ID : {rg.resource_group_id}")
    print(f"Status            : {status}")
    print(f"Created           : {fmt_ts(getattr(rg, 'created_at', ''))}")
    if args.response_format == "detailed":
        labels = fmt_labels(rg)
        if labels:
            print(f"Labels            : {json.dumps(labels)}")
        else:
            print(f"Labels            : (none)")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    args = parse_args()

    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print(
            "ERROR: sap-ai-sdk-core not installed. Run: uv add \"sap-ai-sdk-core>=3.3.0\"",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        client = AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills")
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    if args.resource_group_id:
        get_mode(client, args)
    else:
        list_mode(client, args)


if __name__ == "__main__":
    main()
