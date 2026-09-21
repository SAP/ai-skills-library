# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
List or inspect SAP AI Core scenarios and their versions.

Usage:
  uv run scripts/get_scenarios.py
  uv run scripts/get_scenarios.py --scenario-id <id>
  uv run scripts/get_scenarios.py --scenario-id <id> --response-format detailed
  uv run scripts/get_scenarios.py --json

Options:
  --scenario-id ID        Inspect a single scenario and list its versions
  --response-format       concise (default) or detailed
  --json                  Emit JSON instead of a table
  --resource-group RG     Override the default resource group

Exit codes:
  0 - Success
  1 - Error

JSON structure:
  list: [{"id", "name", "description", "created_at", "modified_at"}, ...]
  get:  [{"id", "name", "description", "created_at", "modified_at",
          "versions": [{"id", "scenario_id", "created_at", "modified_at"}, ...]}]

Examples:
  uv run scripts/get_scenarios.py
  uv run scripts/get_scenarios.py --scenario-id foundation-models --json
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


def get_mode(client, args):
    try:
        scenario = client.scenario.get(scenario_id=args.scenario_id)
        versions = client.scenario.query_versions(scenario_id=args.scenario_id)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    ver_list = [
        {
            "id": v.id if hasattr(v, "id") else str(v),
            "scenario_id": getattr(v, "scenario_id", ""),
            "created_at": fmt_ts(getattr(v, "created_at", "")),
            "modified_at": fmt_ts(getattr(v, "modified_at", "")),
        }
        for v in (versions.resources if hasattr(versions, "resources") else [])
    ]
    row = {
        "id": scenario.id,
        "name": getattr(scenario, "name", ""),
        "description": getattr(scenario, "description", "") or "",
        "created_at": fmt_ts(getattr(scenario, "created_at", "")),
        "modified_at": fmt_ts(getattr(scenario, "modified_at", "")),
        "versions": ver_list,
    }
    if args.as_json:
        print(json.dumps([row], indent=2))
        return

    print(f"ID          : {row['id']}")
    print(f"Name        : {row['name']}")
    if args.response_format == "detailed":
        print(f"Description : {row['description']}")
    print(f"Created     : {row['created_at']}")
    if args.response_format == "detailed":
        print(f"Modified    : {row['modified_at']}")

    print()
    if ver_list:
        colw = lambda key, hdr: max(max(len(r[key]) for r in ver_list), len(hdr))
        c_id = colw("id", "VERSION ID")
        c_cr = colw("created_at", "CREATED")
        if args.response_format == "detailed":
            c_mo = colw("modified_at", "MODIFIED")
            header = f"{'VERSION ID':<{c_id}}  {'CREATED':<{c_cr}}  MODIFIED"
            print(header)
            print("-" * len(header))
            for v in ver_list:
                print(f"{v['id']:<{c_id}}  {v['created_at']:<{c_cr}}  {v['modified_at']}")
        else:
            header = f"{'VERSION ID':<{c_id}}  CREATED"
            print(header)
            print("-" * len(header))
            for v in ver_list:
                print(f"{v['id']:<{c_id}}  {v['created_at']}")
        print(f"{len(ver_list)} version(s) found.")
    else:
        print("0 version(s) found.")


def list_mode(client, args):
    try:
        resp = client.scenario.query()
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    scenarios = resp.resources if hasattr(resp, "resources") else []
    rows = [
        {
            "id": s.id,
            "name": getattr(s, "name", ""),
            "description": (getattr(s, "description", "") or "")[:60],
            "created_at": fmt_ts(getattr(s, "created_at", "")),
            "modified_at": fmt_ts(getattr(s, "modified_at", "")),
        }
        for s in scenarios
    ]

    if args.as_json:
        print(json.dumps(rows, indent=2))
        return

    if not rows:
        print("0 scenario(s) found.")
        return

    def colw(key, header):
        return max(max(len(r[key]) for r in rows), len(header))

    c_id = colw("id", "ID")
    c_nm = colw("name", "NAME")
    c_cr = colw("created_at", "CREATED")

    if args.response_format == "detailed":
        c_ds = colw("description", "DESCRIPTION")
        header = f"{'ID':<{c_id}}  {'NAME':<{c_nm}}  {'DESCRIPTION':<{c_ds}}  {'CREATED':<{c_cr}}  MODIFIED"
        sep = "-" * len(header)
        print(header)
        print(sep)
        for r in rows:
            print(f"{r['id']:<{c_id}}  {r['name']:<{c_nm}}  {r['description']:<{c_ds}}  {r['created_at']:<{c_cr}}  {r['modified_at']}")
    else:
        header = f"{'ID':<{c_id}}  {'NAME':<{c_nm}}  CREATED"
        print(header)
        print("-" * len(header))
        for r in rows:
            print(f"{r['id']:<{c_id}}  {r['name']:<{c_nm}}  {r['created_at']}")

    print(f"{len(rows)} scenario(s) found.")


def main():
    parser = argparse.ArgumentParser(
        description="List or inspect AI Core scenarios.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  uv run scripts/get_scenarios.py
  uv run scripts/get_scenarios.py --scenario-id foundation-models
  uv run scripts/get_scenarios.py --json
        """,
    )
    parser.add_argument("--scenario-id", dest="scenario_id", metavar="ID")
    parser.add_argument("--response-format", dest="response_format", choices=["concise", "detailed"], default="concise")
    parser.add_argument("--json", dest="as_json", action="store_true")
    parser.add_argument("--resource-group", dest="resource_group", metavar="RG", default=None)
    args = parser.parse_args()

    client = _get_client(args.resource_group)
    if args.scenario_id:
        get_mode(client, args)
    else:
        list_mode(client, args)


if __name__ == "__main__":
    main()
