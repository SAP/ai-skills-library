# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests"]
# ///
"""
List available models from the AI Core foundation-models scenario.

Calls GET /v2/lm/scenarios/foundation-models/models and displays model metadata
including version, executable, and orchestration eligibility.

Usage:
  uv run scripts/list_foundation_models.py
  uv run scripts/list_foundation_models.py --response-format detailed
  uv run scripts/list_foundation_models.py --json
  uv run scripts/list_foundation_models.py --response-format detailed --json
  uv run scripts/list_foundation_models.py --executable-id azure-openai
  uv run scripts/list_foundation_models.py --scenario-id orchestration

Options:
  --response-format FORMAT  Output verbosity: concise (default) or detailed
  --json                    Emit JSON instead of a table (pipe-friendly for | jq)
  --executable-id ID        Show models for a specific executable only
  --scenario-id ID          Show only models allowed in a given scenario (e.g. orchestration)

Exit codes:
  0  Success
  1  Configuration or API error
  2  No models match the given filter
"""

import argparse
import json
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="List available models from the AI Core foundation-models scenario.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  # Concise table (default):
  uv run scripts/list_foundation_models.py

  # Detailed table (all fields, one row per model×version):
  uv run scripts/list_foundation_models.py --response-format detailed

  # JSON output — pipe to jq:
  uv run scripts/list_foundation_models.py --json | jq '.[0]'
  uv run scripts/list_foundation_models.py --response-format detailed --json | jq '.[] | select(.model == "gpt-4o") | .versions'

  # Orchestration-eligible models only:
  uv run scripts/list_foundation_models.py --scenario-id orchestration

  # Filter by executable:
  uv run scripts/list_foundation_models.py --executable-id azure-openai

json structure:
  concise:  [{model, executable_id, latest_version, context_length, capabilities, orchestration}, ...]
  detailed: [{model, executable_id, access_type, description, orchestration,
              versions: [{name, is_latest, deprecated, context_length,
                          capabilities, streaming_supported}]}, ...]
""",
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
    parser.add_argument(
        "--executable-id",
        dest="executable_id",
        metavar="ID",
        help="Show models for a specific executable only (e.g. azure-openai)",
    )
    parser.add_argument(
        "--scenario-id",
        dest="scenario_id",
        metavar="ID",
        help="Show only models allowed in a given scenario (e.g. orchestration)",
    )
    return parser.parse_args()


def fetch_models(client) -> list[dict]:
    """Call /v2/lm/scenarios/foundation-models/models and return the resources list."""
    import requests

    rest = client.rest_client
    url = rest.base_url.rstrip("/") + "/lm/scenarios/foundation-models/models"
    token = rest.get_token()
    auth = token if token.startswith("Bearer ") else f"Bearer {token}"
    resource_group = rest.headers.get("AI-Resource-Group", "default")
    headers = {
        "Authorization": auth,
        "AI-Resource-Group": resource_group,
        "Content-Type": "application/json",
    }
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()
    return resp.json().get("resources", [])


def is_orchestration_eligible(resource: dict) -> bool:
    return any(
        s.get("scenarioId") == "orchestration"
        for s in resource.get("allowedScenarios", [])
    )


def latest_version(resource: dict) -> str:
    for v in resource.get("versions", []):
        if v.get("isLatest"):
            return v.get("name", "")
    versions = resource.get("versions", [])
    return versions[0].get("name", "") if versions else ""


def apply_filters(resources: list[dict], args: argparse.Namespace) -> list[dict]:
    if args.executable_id:
        resources = [r for r in resources if r.get("executableId") == args.executable_id]
    if args.scenario_id:
        resources = [
            r for r in resources
            if any(s.get("scenarioId") == args.scenario_id for s in r.get("allowedScenarios", []))
        ]
    return resources


# ── JSON output ──────────────────────────────────────────────────────────────

def to_concise_json(resources: list[dict]) -> list[dict]:
    output = []
    for r in resources:
        versions = r.get("versions", [])
        ver = next((v for v in versions if v.get("isLatest")), versions[0] if versions else {})
        output.append({
            "model": r["model"],
            "executable_id": r.get("executableId", ""),
            "latest_version": latest_version(r),
            "context_length": ver.get("contextLength"),
            "capabilities": ver.get("capabilities", []),
            "orchestration": is_orchestration_eligible(r),
        })
    return output


def to_detailed_json(resources: list[dict]) -> list[dict]:
    output = []
    for r in resources:
        versions = [
            {
                "name": v.get("name", ""),
                "is_latest": v.get("isLatest", False),
                "deprecated": v.get("deprecated", False),
                "context_length": v.get("contextLength"),
                "capabilities": v.get("capabilities", []),
                "streaming_supported": v.get("streamingSupported", False),
            }
            for v in r.get("versions", [])
        ]
        output.append(
            {
                "model": r["model"],
                "executable_id": r.get("executableId", ""),
                "access_type": r.get("accessType", ""),
                "description": r.get("description", ""),
                "orchestration": is_orchestration_eligible(r),
                "versions": versions,
            }
        )
    return output


# ── Table output ─────────────────────────────────────────────────────────────

def print_concise_table(resources: list[dict]) -> None:
    col_model = max((len(r["model"]) for r in resources), default=5)
    col_model = max(col_model, len("MODEL"))
    col_exe = max((len(r.get("executableId", "")) for r in resources), default=13)
    col_exe = max(col_exe, len("EXECUTABLE-ID"))
    col_ver = max((len(latest_version(r)) for r in resources), default=7)
    col_ver = max(col_ver, len("VERSION"))

    header = (
        f"{'MODEL':<{col_model}}  {'EXECUTABLE-ID':<{col_exe}}  "
        f"{'VERSION':<{col_ver}}  ORCHESTRATION"
    )
    print(header)
    print("-" * (len(header) + 2))
    for r in resources:
        orch = "yes" if is_orchestration_eligible(r) else "no"
        print(
            f"{r['model']:<{col_model}}  {r.get('executableId', ''):<{col_exe}}  "
            f"{latest_version(r):<{col_ver}}  {orch}"
        )
    print(f"\n{len(resources)} model(s) found.")


def print_detailed_table(resources: list[dict]) -> None:
    DESC_MAX = 32

    # Flatten to one row per model×version
    rows = []
    for r in resources:
        desc = (r.get("description") or "")[:DESC_MAX]
        orch = "yes" if is_orchestration_eligible(r) else "no"
        for v in r.get("versions", []) or [{"name": "", "isLatest": False, "deprecated": False}]:
            caps = ",".join(v.get("capabilities") or [])
            ctx = str(v.get("contextLength") or "")
            rows.append(
                {
                    "model": r["model"],
                    "executable_id": r.get("executableId", ""),
                    "access_type": r.get("accessType", ""),
                    "description": desc,
                    "version": v.get("name", ""),
                    "latest": "yes" if v.get("isLatest") else "no",
                    "context": ctx,
                    "capabilities": caps,
                    "streaming": "yes" if v.get("streamingSupported") else "no",
                    "deprecated": "yes" if v.get("deprecated") else "no",
                    "orchestration": orch,
                }
            )

    if not rows:
        return

    def colw(key: str, header: str) -> int:
        return max(max(len(row[key]) for row in rows), len(header))

    c_model = colw("model", "MODEL")
    c_exe   = colw("executable_id", "EXECUTABLE-ID")
    c_acc   = colw("access_type", "ACCESS-TYPE")
    c_desc  = colw("description", "DESCRIPTION")
    c_ver   = colw("version", "VERSION")
    c_ctx   = colw("context", "CONTEXT")
    c_cap   = colw("capabilities", "CAPABILITIES")

    fmt = (
        f"{{model:<{c_model}}}  {{executable_id:<{c_exe}}}  {{access_type:<{c_acc}}}  "
        f"{{description:<{c_desc}}}  {{version:<{c_ver}}}  {{latest:<6}}  "
        f"{{context:<{c_ctx}}}  {{capabilities:<{c_cap}}}  "
        f"{{streaming:<9}}  {{deprecated:<10}}  {{orchestration}}"
    )
    header = fmt.format(
        model="MODEL", executable_id="EXECUTABLE-ID", access_type="ACCESS-TYPE",
        description="DESCRIPTION", version="VERSION", latest="LATEST",
        context="CONTEXT", capabilities="CAPABILITIES",
        streaming="STREAMING", deprecated="DEPRECATED", orchestration="ORCHESTRATION",
    )
    print(header)
    print("-" * len(header))
    for row in rows:
        print(fmt.format(**row))
    print(f"\n{len(rows)} row(s) across {len(resources)} model(s).")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    args = parse_args()

    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print(
            "Error: sap-ai-sdk-core is not installed.\n"
            'Fix: uv add "sap-ai-sdk-core>=3.3.0"',
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        client = AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills")
    except Exception as e:
        print(f"Error: Failed to initialise AI Core client: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        resources = fetch_models(client)
    except Exception as e:
        print(f"Error: Failed to fetch models: {e}", file=sys.stderr)
        sys.exit(1)

    resources = apply_filters(resources, args)

    if not resources:
        filters = []
        if args.executable_id:
            filters.append(f"executable-id={args.executable_id!r}")
        if args.scenario_id:
            filters.append(f"scenario-id={args.scenario_id!r}")
        print(
            f"No models found" + (f" matching {', '.join(filters)}" if filters else "") + ".",
            file=sys.stderr,
        )
        sys.exit(2)

    if args.as_json:
        if args.response_format == "detailed":
            print(json.dumps(to_detailed_json(resources), indent=2))
        else:
            print(json.dumps(to_concise_json(resources), indent=2))
    else:
        if args.response_format == "detailed":
            print_detailed_table(resources)
        else:
            print_concise_table(resources)


if __name__ == "__main__":
    main()
