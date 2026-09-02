# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
Remove duplicate LLM deployments (RUNNING or DEAD).

Queries all RUNNING and DEAD deployments and deduplicates those that have a
model name (i.e. LLM deployments). For each (scenario_id, executable_id,
model_name) group, keeps the newest RUNNING deployment (or newest overall if
none are RUNNING) and stops + deletes the rest concurrently. DEAD deployments
are deleted directly without a stop step.

Orchestration and custom deployments (no model_name) are never touched.

Usage:
  uv run scripts/dedup_deployments.py
  uv run scripts/dedup_deployments.py --dry-run
  uv run scripts/dedup_deployments.py --resource-group <rg>

Exit codes:
  0 - Success (or nothing to do)
  1 - One or more deletions failed
"""

import argparse
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from ai_core_sdk.models import Status, TargetStatus

POLL_INTERVAL = 10
STOP_TIMEOUT = 600


def get_model_name(dep) -> str:
    try:
        details = dep.details
        if details:
            return details.get("resources", {}).get("backend_details", {}).get("model", {}).get("name", "") or ""
    except Exception:
        pass
    return ""


def fmt_status(dep) -> str:
    return dep.status.value if hasattr(dep.status, "value") else str(dep.status)


def fmt_ts(value) -> str:
    return str(value)[:19] if value else ""


def find_duplicates(client, dry_run: bool) -> list:
    deployments = []
    for status in (Status.RUNNING, Status.DEAD):
        try:
            deployments.extend(client.deployment.query(status=status).resources)
        except Exception as e:
            print(f"WARNING: failed to query {status}: {e}", file=sys.stderr)

    # Only consider LLM deployments (those with a model_name)
    groups: dict = {}
    for dep in deployments:
        model_name = get_model_name(dep)
        if not model_name:
            continue
        key = (
            getattr(dep, "scenario_id", "") or "",
            getattr(dep, "executable_id", "") or "",
            model_name,
        )
        groups.setdefault(key, []).append(dep)

    prefix = "[DRY RUN] " if dry_run else ""
    to_delete = []
    for (scenario, executable, model), deps in groups.items():
        if len(deps) < 2:
            continue
        sorted_by_date = sorted(deps, key=lambda d: getattr(d, "created_at", None) or "", reverse=True)
        # Keep newest RUNNING; fall back to newest overall if none are RUNNING
        running = [d for d in sorted_by_date if fmt_status(d) == "RUNNING"]
        keep = running[0] if running else sorted_by_date[0]
        label = f"{scenario}/{executable}/{model}"
        print(f"{prefix}  {label}: keep {keep.id} [{fmt_status(keep)}] ({fmt_ts(getattr(keep, 'created_at', ''))})")
        for d in sorted_by_date:
            if d.id == keep.id:
                continue
            print(f"{prefix}    - remove {d.id} [{fmt_status(d)}] ({fmt_ts(getattr(d, 'created_at', ''))})")
            to_delete.append(d)
    return to_delete


def stop_and_delete(client, dep) -> tuple:
    dep_id = dep.id
    status = fmt_status(dep)

    if status != "DEAD":
        try:
            client.deployment.modify(deployment_id=dep_id, target_status=TargetStatus.STOPPED)
        except Exception as e:
            return dep_id, False, f"stop failed: {e}"

        start = time.time()
        while time.time() - start < STOP_TIMEOUT:
            try:
                if fmt_status(client.deployment.get(deployment_id=dep_id)) in {"STOPPED", "DEAD"}:
                    break
            except Exception as e:
                return dep_id, False, f"poll failed: {e}"
            time.sleep(POLL_INTERVAL)
        else:
            return dep_id, False, "timed out waiting for STOPPED"

    try:
        client.deployment.delete(deployment_id=dep_id)
    except Exception as e:
        return dep_id, False, f"delete failed: {e}"

    return dep_id, True, "ok"


def main():
    parser = argparse.ArgumentParser(
        description="Remove duplicate LLM deployments (RUNNING or DEAD).",
    )
    parser.add_argument("--dry-run", action="store_true", help="List duplicates without deleting")
    parser.add_argument("--resource-group", dest="resource_group", default=None,
                        help="Resource group (default: read from SDK config)")
    args = parser.parse_args()

    profile = os.environ.get("AICORE_PROFILE", "default")
    print(f"Landscape: {profile}")
    if args.dry_run:
        print("Dry run — no changes will be made.\n")

    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        sys.exit('ERROR: sap-ai-sdk-core not installed. Run: uv add "sap-ai-sdk-core>=3.3.0"')

    try:
        kwargs = {}
        if args.resource_group:
            kwargs["resource_group"] = args.resource_group
        client = AICoreV2Client.from_env(read_timeout=30, connect_timeout=15, client_type="AI Core Skills", **kwargs)
    except Exception as e:
        sys.exit(f"ERROR: {e}")

    print("Fetching RUNNING and DEAD deployments...")
    to_delete = find_duplicates(client, args.dry_run)

    if not to_delete:
        print("\nNo duplicate LLM deployments found.")
        return

    print(f"\n{len(to_delete)} duplicate(s) to remove.")

    if args.dry_run:
        return

    deleted, failed = [], []
    with ThreadPoolExecutor(max_workers=min(len(to_delete), 8)) as pool:
        futures = {pool.submit(stop_and_delete, client, dep): dep.id for dep in to_delete}
        for future in as_completed(futures):
            dep_id, success, message = future.result()
            if success:
                print(f"  OK  {dep_id} deleted")
                deleted.append(dep_id)
            else:
                print(f"  FAILED  {dep_id}: {message}")
                failed.append(dep_id)

    print(f"\nSummary: deleted {len(deleted)}, failed {len(failed)}")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
