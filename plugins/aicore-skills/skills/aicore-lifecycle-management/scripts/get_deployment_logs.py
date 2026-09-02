# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
Retrieve logs for an AI Core deployment.

Usage:
  uv run scripts/get_deployment_logs.py --deployment-id <id>
  uv run scripts/get_deployment_logs.py --deployment-id <id> --tail 50
  uv run scripts/get_deployment_logs.py --deployment-id <id> --start 2026-06-22T15:00:00Z --end 2026-06-22T16:00:00Z
  uv run scripts/get_deployment_logs.py --deployment-id <id> --json

Options:
  --deployment-id ID  Deployment ID to fetch logs for (required)
  --tail N            Max number of log lines to return, up to 5000 (default: 100)
  --start DATETIME    Start time in RFC 3339 format (default: 1 hour ago)
  --end DATETIME      End time in RFC 3339 format (default: now)
  --order asc|desc    Sort order (default: desc); table always renders oldest-first
  --resource-group RG Resource group (default: read from SDK config)
  --json              Emit JSON array instead of formatted table

Exit codes:
  0  Success
  1  Error

Note: Deployment logs are available for RUNNING deployments and for a short
window after stopping.

json structure:
  [{"timestamp": "...", "level": "...", "msg": "..."}, ...]
"""

import argparse
import json
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Retrieve logs for an AI Core deployment.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  uv run scripts/get_deployment_logs.py --deployment-id d1234abcd
  uv run scripts/get_deployment_logs.py --deployment-id d1234abcd --tail 50
  uv run scripts/get_deployment_logs.py --deployment-id d1234abcd --start 2026-06-22T15:00:00Z --end 2026-06-22T16:00:00Z
  uv run scripts/get_deployment_logs.py --deployment-id d1234abcd --order asc
  uv run scripts/get_deployment_logs.py --deployment-id d1234abcd --json

json structure:
  [{"timestamp": "2026-06-22T15:01:18Z", "level": "INFO", "msg": "..."}]
""",
    )
    parser.add_argument("--deployment-id", required=True, help="Deployment ID")
    parser.add_argument(
        "--tail",
        type=int,
        default=100,
        metavar="N",
        help="Max number of log lines to return, up to 5000 (default: 100)",
    )
    parser.add_argument(
        "--start",
        metavar="DATETIME",
        help="Start time in RFC 3339 format, e.g. 2026-06-22T15:00:00Z (default: 1 hour ago)",
    )
    parser.add_argument(
        "--end",
        metavar="DATETIME",
        help="End time in RFC 3339 format, e.g. 2026-06-22T16:00:00Z (default: now)",
    )
    parser.add_argument(
        "--order",
        choices=["asc", "desc"],
        default="desc",
        help="Sort order: asc (oldest first) or desc (newest first), default: desc",
    )
    parser.add_argument(
        "--resource-group",
        metavar="RG",
        help="Resource group (default: read from SDK config)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Emit JSON array (pipe-friendly)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client

        client = AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills")
    except Exception as exc:
        print(f"ERROR: failed to initialise AI Core client: {exc}", file=sys.stderr)
        sys.exit(1)

    try:
        rest = client.rest_client
        params: dict = {"$top": args.tail, "$order": args.order}
        if args.start:
            params["start"] = args.start
        if args.end:
            params["end"] = args.end
        response_dict = rest.get(
            path=f"/lm/deployments/{args.deployment_id}/logs",
            params=params,
            resource_group=args.resource_group,
        )
        if not isinstance(response_dict, dict):
            raise ValueError(f"unexpected response type: {type(response_dict)}")
        raw_entries = response_dict.get("data", {}).get("result", [])
    except Exception as exc:
        print(f"ERROR: failed to retrieve logs for {args.deployment_id}: {exc}", file=sys.stderr)
        sys.exit(1)

    entries = []
    for entry in raw_entries:
        ts = entry.get("timestamp", "") or ""
        msg = entry.get("msg", "") or ""
        level = entry.get("level", "") or ""
        entries.append({"timestamp": ts, "level": level, "msg": msg})

    # API returns desc order by default; reverse so table reads oldest-first
    if args.order == "desc":
        entries = list(reversed(entries))

    if args.as_json:
        print(json.dumps(entries, indent=2))
        return

    if not entries:
        print(f"no logs available for deployment {args.deployment_id}")
        return

    # Dynamic column widths
    ts_w = max(len(e["timestamp"]) for e in entries) if entries else 0
    ts_w = max(ts_w, len("TIMESTAMP"))
    lvl_w = max(len(e["level"]) for e in entries) if entries else 0
    lvl_w = max(lvl_w, len("LEVEL"))

    header = f"{'TIMESTAMP':<{ts_w}}\t{'LEVEL':<{lvl_w}}\tMESSAGE"
    print(header)
    print("-" * (ts_w + lvl_w + 40))
    for e in entries:
        print(f"{e['timestamp']:<{ts_w}}\t{e['level']:<{lvl_w}}\t{e['msg']}")

    print(f"\n{len(entries)} log line(s) shown")


if __name__ == "__main__":
    main()
