# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
Query AI Core deployments: list all or inspect one by ID.

Uses a single API call with server-side filtering — no hardcoded scenario list.

Usage:
  uv run scripts/get_deployments.py
  uv run scripts/get_deployments.py --status RUNNING
  uv run scripts/get_deployments.py --scenario foundation-models
  uv run scripts/get_deployments.py --scenario orchestration --json
  uv run scripts/get_deployments.py --executable-id azure-openai --status RUNNING --json
  uv run scripts/get_deployments.py --response-format detailed
  uv run scripts/get_deployments.py --deployment-id <id>
  uv run scripts/get_deployments.py --deployment-id <id> --response-format detailed
  uv run scripts/get_deployments.py --deployment-id <id> --json

Options:
  --deployment-id ID      Inspect a single deployment (omit to list all)
  --status STATUS         Filter by status: PENDING, RUNNING, STOPPED, STOPPING, DEAD, UNKNOWN
  --scenario ID           Filter by scenario ID
  --executable-id ID      Filter by executable ID
  --configuration-id ID   Filter by configuration ID
  --response-format       concise (default) or detailed
  --json                  Emit JSON instead of a table (pipe-friendly for | jq)
  --resource-group RG     Resource group (default: read from SDK config)

Exit codes:
  0  Success
  1  Error

json structure:
  list concise:   [{"deployment_id", "scenario_id", "executable_id", "status", "model_name",
                    "deployment_url", "resource_group", "created_at"}, ...]
  list detailed:  adds "configuration_id", "configuration_name", "model_version", "modified_at"
  get concise:    {"deployment_id", "scenario_id", "executable_id", "status", "model_name",
                   "deployment_url", "resource_group", "created_at"}
  get detailed:   adds "configuration_id", "configuration_name", "model_version",
                  "created_at", "modified_at", "start_time", "status_message", "details"
"""

import argparse
import json
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Query AI Core deployments: list all or inspect one by ID.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  # List all deployments:
  uv run scripts/get_deployments.py

  # Filter by status:
  uv run scripts/get_deployments.py --status RUNNING

  # Filter by scenario:
  uv run scripts/get_deployments.py --scenario orchestration

  # Filter by executable (all LLM deployments for one provider):
  uv run scripts/get_deployments.py --executable-id azure-openai --status RUNNING

  # JSON output — pipe to jq:
  uv run scripts/get_deployments.py --status RUNNING --json
  uv run scripts/get_deployments.py --scenario foundation-models --json | jq '.[0].deployment_url'

  # Inspect a single deployment:
  uv run scripts/get_deployments.py --deployment-id <id>
  uv run scripts/get_deployments.py --deployment-id <id> --response-format detailed
  uv run scripts/get_deployments.py --deployment-id <id> --json
""",
    )
    parser.add_argument("--deployment-id", dest="deployment_id", metavar="ID",
                        help="Inspect a single deployment by ID (omit to list all)")
    parser.add_argument("--status", metavar="STATUS",
                        help="Filter by status (PENDING, RUNNING, STOPPED, STOPPING, DEAD, UNKNOWN)")
    parser.add_argument("--scenario", metavar="ID",
                        help="Filter by scenario ID")
    parser.add_argument("--executable-id", dest="executable_id", metavar="ID",
                        help="Filter by executable ID")
    parser.add_argument("--configuration-id", dest="configuration_id", metavar="ID",
                        help="Filter by configuration ID")
    parser.add_argument("--response-format", dest="response_format",
                        choices=["concise", "detailed"], default="concise",
                        help="Output verbosity: concise (default) or detailed")
    parser.add_argument("--json", action="store_true", dest="as_json",
                        help="Emit JSON instead of a table")
    parser.add_argument("--resource-group", dest="resource_group", metavar="RG",
                        help="Resource group (default: read from SDK config)")
    return parser.parse_args()


def get_model_name(dep) -> str:
    try:
        details = dep.details
        if details:
            return details.get("resources", {}).get("backend_details", {}).get("model", {}).get("name", "") or ""
    except Exception:
        pass
    return ""


def get_model_version(dep) -> str:
    try:
        details = dep.details
        if details:
            return details.get("resources", {}).get("backend_details", {}).get("model", {}).get("version", "") or ""
    except Exception:
        pass
    return ""


def fmt_status(dep) -> str:
    return dep.status.value if hasattr(dep.status, "value") else str(dep.status)


def fmt_ts(value) -> str:
    return str(value)[:19] if value else ""


# ── List mode ─────────────────────────────────────────────────────────────────

def list_mode(client, args: argparse.Namespace) -> None:
    from ai_core_sdk.models import Status
    status_map = {
        "PENDING": Status.PENDING,
        "RUNNING": Status.RUNNING,
        "STOPPED": Status.STOPPED,
        "STOPPING": Status.STOPPING,
        "DEAD": Status.DEAD,
        "UNKNOWN": Status.UNKNOWN,
    }
    resource_group = args.resource_group or client.rest_client.headers.get("AI-Resource-Group", "default")
    kwargs = {}
    if args.scenario:
        kwargs["scenario_id"] = args.scenario
    if args.executable_id:
        kwargs["executable_ids"] = [args.executable_id]
    if args.configuration_id:
        kwargs["configuration_id"] = args.configuration_id
    if args.status:
        want = args.status.upper()
        if want not in status_map:
            print(f"ERROR: unknown status '{args.status}'. Valid values: {', '.join(status_map)}", file=sys.stderr)
            sys.exit(1)
        kwargs["status"] = status_map[want]

    try:
        result = client.deployment.query(**kwargs)
        deployments = result.resources
    except Exception as e:
        print(f"ERROR: Failed to list deployments: {e}", file=sys.stderr)
        sys.exit(1)

    if args.as_json:
        _print_list_json(deployments, args, resource_group)
    else:
        _print_list_table(deployments, args)


def _print_list_json(deployments, args: argparse.Namespace, resource_group: str) -> None:
    if args.response_format == "detailed":
        output = [
            {
                "deployment_id": dep.id,
                "scenario_id": getattr(dep, "scenario_id", ""),
                "executable_id": getattr(dep, "executable_id", ""),
                "status": fmt_status(dep),
                "model_name": get_model_name(dep),
                "model_version": get_model_version(dep),
                "deployment_url": getattr(dep, "deployment_url", "") or "",
                "resource_group": resource_group,
                "configuration_id": getattr(dep, "configuration_id", ""),
                "configuration_name": getattr(dep, "configuration_name", ""),
                "created_at": fmt_ts(getattr(dep, "created_at", "")),
                "modified_at": fmt_ts(getattr(dep, "modified_at", "")),
            }
            for dep in deployments
        ]
    else:
        output = [
            {
                "deployment_id": dep.id,
                "scenario_id": getattr(dep, "scenario_id", ""),
                "executable_id": getattr(dep, "executable_id", ""),
                "status": fmt_status(dep),
                "model_name": get_model_name(dep),
                "deployment_url": getattr(dep, "deployment_url", "") or "",
                "resource_group": resource_group,
                "created_at": fmt_ts(getattr(dep, "created_at", "")),
            }
            for dep in deployments
        ]
    print(json.dumps(output, indent=2))


def _print_list_table(deployments, args: argparse.Namespace) -> None:
    if not deployments:
        print("No deployments found.")
        return

    rows = []
    for dep in deployments:
        row = {
            "id": dep.id,
            "scenario": getattr(dep, "scenario_id", "") or "",
            "executable": getattr(dep, "executable_id", "") or "",
            "model": get_model_name(dep) or "-",
            "status": fmt_status(dep),
            "created": fmt_ts(getattr(dep, "created_at", "")),
        }
        if args.response_format == "detailed":
            row["url"] = getattr(dep, "deployment_url", "") or "-"
            row["modified"] = fmt_ts(getattr(dep, "modified_at", ""))
        rows.append(row)

    def colw(key: str, header: str) -> int:
        return max(max(len(r[key]) for r in rows), len(header))

    c_id = colw("id", "ID")
    c_sc = colw("scenario", "SCENARIO")
    c_ex = colw("executable", "EXECUTABLE")
    c_mo = colw("model", "MODEL")
    c_st = colw("status", "STATUS")
    c_cr = colw("created", "CREATED")

    if args.response_format == "detailed":
        c_url = colw("url", "URL")
        fmt = (f"{{id:<{c_id}}}  {{scenario:<{c_sc}}}  {{executable:<{c_ex}}}  "
               f"{{model:<{c_mo}}}  {{status:<{c_st}}}  {{url:<{c_url}}}  "
               f"{{created:<{c_cr}}}  {{modified}}")
        header = fmt.format(id="ID", scenario="SCENARIO", executable="EXECUTABLE",
                            model="MODEL", status="STATUS", url="URL",
                            created="CREATED", modified="MODIFIED")
    else:
        fmt = (f"{{id:<{c_id}}}  {{scenario:<{c_sc}}}  {{executable:<{c_ex}}}  "
               f"{{model:<{c_mo}}}  {{status:<{c_st}}}  {{created}}")
        header = fmt.format(id="ID", scenario="SCENARIO", executable="EXECUTABLE",
                            model="MODEL", status="STATUS", created="CREATED")

    print(header)
    print("-" * len(header))
    for row in rows:
        print(fmt.format(**row))
    print(f"\n{len(deployments)} deployment(s) found.")


# ── Get mode ──────────────────────────────────────────────────────────────────

def get_mode(client, args: argparse.Namespace) -> None:
    try:
        dep = client.deployment.get(
            deployment_id=args.deployment_id,
        )
    except Exception as e:
        print(f"ERROR: Failed to get deployment '{args.deployment_id}': {e}", file=sys.stderr)
        sys.exit(1)

    resource_group = args.resource_group or client.rest_client.headers.get("AI-Resource-Group", "default")
    status = fmt_status(dep)

    if args.as_json:
        _print_get_json(dep, status, resource_group, args)
    else:
        _print_get_table(dep, status, resource_group, args)


def _print_get_json(dep, status: str, resource_group: str, args: argparse.Namespace) -> None:
    base = {
        "deployment_id": dep.id,
        "scenario_id": getattr(dep, "scenario_id", ""),
        "executable_id": getattr(dep, "executable_id", ""),
        "status": status,
        "model_name": get_model_name(dep),
        "deployment_url": getattr(dep, "deployment_url", "") or "",
        "resource_group": resource_group,
        "created_at": fmt_ts(getattr(dep, "created_at", "")),
    }
    if args.response_format == "detailed":
        base.update({
            "model_version": get_model_version(dep),
            "configuration_id": getattr(dep, "configuration_id", ""),
            "configuration_name": getattr(dep, "configuration_name", ""),
            "modified_at": fmt_ts(getattr(dep, "modified_at", "")),
            "start_time": fmt_ts(getattr(dep, "start_time", "")),
            "status_message": getattr(dep, "status_message", None),
            "details": getattr(dep, "details", {}),
        })
    print(json.dumps(base, indent=2))


def _print_get_table(dep, status: str, resource_group: str, args: argparse.Namespace) -> None:
    print(f"Deployment ID  : {dep.id}")
    print(f"Scenario       : {getattr(dep, 'scenario_id', '') or 'N/A'}")
    print(f"Executable     : {getattr(dep, 'executable_id', '') or 'N/A'}")
    model_name = get_model_name(dep)
    if model_name:
        model_version = get_model_version(dep)
        print(f"Model          : {model_name}  (version: {model_version or 'N/A'})")
    print(f"Status         : {status}")
    print(f"URL            : {getattr(dep, 'deployment_url', '') or 'N/A'}")
    print(f"Resource Group : {resource_group}")
    print(f"Created        : {fmt_ts(getattr(dep, 'created_at', ''))}")
    if args.response_format == "detailed":
        print(f"Config ID      : {getattr(dep, 'configuration_id', '') or 'N/A'}")
        print(f"Config Name    : {getattr(dep, 'configuration_name', '') or 'N/A'}")
        print(f"Modified       : {fmt_ts(getattr(dep, 'modified_at', ''))}")
        print(f"Start Time     : {fmt_ts(getattr(dep, 'start_time', '')) or 'N/A'}")
        status_msg = getattr(dep, "status_message", None)
        if status_msg:
            print(f"Status Message : {status_msg}")
        details = getattr(dep, "details", None)
        if details:
            print(f"Details        :\n{json.dumps(details, indent=2)}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    args = parse_args()

    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add \"sap-ai-sdk-core>=3.3.0\"", file=sys.stderr)
        sys.exit(1)

    try:
        kwargs = {}
        if args.resource_group:
            kwargs["resource_group"] = args.resource_group
        client = AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills", **kwargs)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    if args.deployment_id:
        get_mode(client, args)
    else:
        list_mode(client, args)


if __name__ == "__main__":
    main()
