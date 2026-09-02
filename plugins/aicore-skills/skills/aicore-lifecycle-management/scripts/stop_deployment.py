# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
Stop a running AI Core deployment (sets target status to STOPPED).

Must stop before deleting. Use delete_deployment.py afterwards.

Usage:
  uv run scripts/stop_deployment.py --deployment-id <id> --confirm

Options:
  --deployment-id ID    Deployment ID to stop (required)
  --confirm             Required to confirm the stop action
  --wait                Poll until deployment reaches STOPPED status
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
    parser = argparse.ArgumentParser(description="Stop an AI Core deployment.")
    parser.add_argument("--deployment-id", dest="deployment_id", required=True,
                        help="Deployment ID to stop")
    parser.add_argument("--confirm", action="store_true",
                        help="Required flag to confirm the stop action")
    parser.add_argument("--wait", action="store_true",
                        help="Poll until deployment is STOPPED")
    parser.add_argument("--resource-group", dest="resource_group", default=None,
                        help="Resource group (default: read from SDK config)")
    return parser.parse_args()


def main():
    args = parse_args()

    if not args.confirm:
        print("ERROR: --confirm flag is required to stop a deployment.", file=sys.stderr)
        print(f"  Re-run with: --deployment-id {args.deployment_id} --confirm", file=sys.stderr)
        sys.exit(1)

    try:
        from ai_core_sdk.models import TargetStatus
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add \"sap-ai-sdk-core\"", file=sys.stderr)
        sys.exit(1)

    client = _get_client(resource_group=args.resource_group)

    try:
        print(f"Stopping deployment {args.deployment_id}...", file=sys.stderr)
        client.deployment.modify(
            deployment_id=args.deployment_id,
            target_status=TargetStatus.STOPPED,
        )
    except Exception as e:
        print(f"ERROR: Failed to stop deployment: {e}", file=sys.stderr)
        sys.exit(1)

    if not args.wait:
        print(f"Stop request sent for {args.deployment_id}. It will reach STOPPED shortly.", file=sys.stderr)
        return

    print(f"Waiting for deployment to be STOPPED (timeout: {TIMEOUT_SECONDS}s)...", file=sys.stderr)
    start = time.time()
    while time.time() - start < TIMEOUT_SECONDS:
        dep = client.deployment.get(deployment_id=args.deployment_id)
        current = dep.status.value if hasattr(dep.status, "value") else str(dep.status)
        elapsed = int(time.time() - start)
        print(f"  [{elapsed:>3}s] status: {current}", end="\r", file=sys.stderr)

        if current == "STOPPED":
            print(f"\nDeployment {args.deployment_id} is STOPPED.", file=sys.stderr)
            return
        if current == "DEAD":
            print(f"\nDeployment {args.deployment_id} is DEAD (also safe to delete).", file=sys.stderr)
            return
        time.sleep(POLL_INTERVAL)

    print(f"\nWARN: Deployment did not reach STOPPED within {TIMEOUT_SECONDS}s.", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
