# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
Delete an AI Core deployment, optionally stopping it first.

Usage:
  uv run scripts/delete_deployment.py --deployment-id <id> --confirm
  uv run scripts/delete_deployment.py --deployment-id <id> --confirm --auto-stop

Options:
  --deployment-id ID    Deployment ID to delete (required)
  --confirm             Required to confirm the delete action
  --auto-stop           Stop the deployment first if it is not already STOPPED
  --resource-group RG   Resource group (default: read from SDK config)

Exit codes:
  0 - Success
  1 - Error
"""

import argparse
import sys
import time


TIMEOUT_SECONDS = 600
POLL_INTERVAL = 10


def _get_client(resource_group=None):
    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add \"sap-ai-sdk-core\"", file=sys.stderr)
        sys.exit(1)
    try:
        kwargs = {}
        if resource_group:
            kwargs["resource_group"] = resource_group
        return AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills", **kwargs)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


def parse_args():
    parser = argparse.ArgumentParser(description="Delete an AI Core deployment.")
    parser.add_argument("--deployment-id", dest="deployment_id", required=True,
                        help="Deployment ID to delete")
    parser.add_argument("--confirm", action="store_true",
                        help="Required flag to confirm the delete action")
    parser.add_argument("--auto-stop", action="store_true", dest="auto_stop",
                        help="Stop the deployment first if it is not already STOPPED")
    parser.add_argument("--resource-group", dest="resource_group", default=None,
                        help="Resource group (default: read from SDK config)")
    return parser.parse_args()


def main():
    args = parse_args()

    if not args.confirm:
        print("ERROR: --confirm flag is required to delete a deployment.", file=sys.stderr)
        print(f"  Re-run with: --deployment-id {args.deployment_id} --confirm", file=sys.stderr)
        sys.exit(1)

    try:
        from ai_core_sdk.models import TargetStatus
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add \"sap-ai-sdk-core\"", file=sys.stderr)
        sys.exit(1)

    client = _get_client(resource_group=args.resource_group)

    # Check current status; auto-stop if not already stopped
    try:
        dep = client.deployment.get(deployment_id=args.deployment_id)
        current = dep.status.value if hasattr(dep.status, "value") else str(dep.status)
    except Exception as e:
        print(f"ERROR: Could not retrieve deployment status: {e}", file=sys.stderr)
        sys.exit(1)

    if current not in {"STOPPED", "DEAD", "UNKNOWN"}:
        if not args.auto_stop:
            print(f"ERROR: Deployment {args.deployment_id} is {current}. Stop it first or use --auto-stop.", file=sys.stderr)
            print(f"  Stop first : uv run scripts/stop_deployment.py --deployment-id {args.deployment_id} --confirm --wait", file=sys.stderr)
            print(f"  Or re-run  : add --auto-stop to this command", file=sys.stderr)
            sys.exit(1)
        print(f"Deployment {args.deployment_id} is {current} — stopping first...", file=sys.stderr)
        try:
            client.deployment.modify(
                deployment_id=args.deployment_id,
                target_status=TargetStatus.STOPPED,
            )
        except Exception as e:
            print(f"ERROR: Failed to stop deployment: {e}", file=sys.stderr)
            sys.exit(1)

        start = time.time()
        while time.time() - start < TIMEOUT_SECONDS:
            dep = client.deployment.get(deployment_id=args.deployment_id)
            current = dep.status.value if hasattr(dep.status, "value") else str(dep.status)
            elapsed = int(time.time() - start)
            print(f"  [{elapsed:>3}s] status: {current}", end="\r", file=sys.stderr)
            if current in {"STOPPED", "DEAD"}:
                print(f"\nDeployment {args.deployment_id} is {current}.", file=sys.stderr)
                break
            time.sleep(POLL_INTERVAL)
        else:
            print(f"\nERROR: Deployment did not stop within {TIMEOUT_SECONDS}s.", file=sys.stderr)
            sys.exit(1)

    try:
        print(f"Deleting deployment {args.deployment_id}...", file=sys.stderr)
        client.deployment.delete(deployment_id=args.deployment_id)
        print(f"✓ Deployment {args.deployment_id} deleted.", file=sys.stderr)
    except Exception as e:
        print(f"ERROR: Failed to delete deployment: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
