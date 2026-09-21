# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
Create an AI Core deployment from a configuration ID.

The caller is responsible for creating the configuration first (use scripts/create_configuration.py).

Usage:
  uv run scripts/create_deployment.py --configuration-id <id>
  uv run scripts/create_deployment.py --configuration-id <id> --wait
  uv run scripts/create_deployment.py --configuration-id <id> --wait --timeout 600

Options:
  --configuration-id ID   Configuration ID to deploy (required)
  --resource-group RG     Resource group (default: read from SDK config)
  --wait                  Poll until deployment is RUNNING
  --timeout SECONDS       Polling timeout when using --wait (default: 1800)
  --json                  Emit JSON instead of plain text

Exit codes:
  0 - Success
  1 - Error

json structure (no --wait):  {"configuration_id": "...", "deployment_id": "...", "status": "PENDING"}
json structure (--wait):     {"configuration_id": "...", "deployment_id": "...", "status": "RUNNING", "deployment_url": "..."}

examples:
  uv run scripts/create_deployment.py --configuration-id aa97b177-9383-4934-8543-0f91a7a0283a
  uv run scripts/create_deployment.py --configuration-id aa97b177-9383-4934-8543-0f91a7a0283a --wait
  uv run scripts/create_deployment.py --configuration-id aa97b177-9383-4934-8543-0f91a7a0283a --wait --json
"""

import argparse
import json
import sys
import time


FAILED_STATUSES = {"DEAD", "STOPPED"}
DEFAULT_TIMEOUT = 1800
POLL_INTERVAL = 15


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create an AI Core deployment from a configuration ID.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  uv run scripts/create_deployment.py --configuration-id <id>
  uv run scripts/create_deployment.py --configuration-id <id> --wait
  uv run scripts/create_deployment.py --configuration-id <id> --wait --json
""",
    )
    parser.add_argument("--configuration-id", dest="configuration_id", required=True,
                        help="Configuration ID to deploy")
    parser.add_argument("--resource-group", dest="resource_group", default=None,
                        help="Resource group (default: read from SDK config)")
    parser.add_argument("--wait", action="store_true",
                        help="Poll until deployment is RUNNING")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, metavar="SECONDS",
                        help=f"Polling timeout in seconds (default: {DEFAULT_TIMEOUT})")
    parser.add_argument("--json", action="store_true", dest="as_json",
                        help="Emit JSON instead of plain text")
    return parser.parse_args()


def fmt_status(dep) -> str:
    return dep.status.value if hasattr(dep.status, "value") else str(dep.status)


def main():
    args = parse_args()

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
        print(f"Creating deployment for configuration {args.configuration_id}...", file=sys.stderr)
        deployment = client.deployment.create(
            configuration_id=args.configuration_id,
            resource_group=args.resource_group,
        )
    except Exception as e:
        print(f"ERROR: Failed to create deployment: {e}", file=sys.stderr)
        sys.exit(1)

    if not args.wait:
        if args.as_json:
            print(json.dumps({
                "configuration_id": args.configuration_id,
                "deployment_id": deployment.id,
                "status": "PENDING",
            }))
        else:
            print(f"Deployment ID: {deployment.id}")
            print(f"Status       : PENDING", file=sys.stderr)
            print(f"Check status : uv run scripts/get_deployments.py --deployment-id {deployment.id}", file=sys.stderr)
        return

    print(f"Waiting for deployment to be RUNNING (timeout: {args.timeout}s)...", file=sys.stderr)
    start = time.time()
    while time.time() - start < args.timeout:
        dep = client.deployment.get(deployment_id=deployment.id, resource_group=args.resource_group)
        current = fmt_status(dep)
        elapsed = int(time.time() - start)
        print(f"  [{elapsed:>4}s] status: {current}", end="\r", file=sys.stderr)

        if current == "RUNNING":
            print(f"\nDeployment RUNNING after {elapsed}s.", file=sys.stderr)
            url = getattr(dep, "deployment_url", "") or ""
            if args.as_json:
                print(json.dumps({
                    "configuration_id": args.configuration_id,
                    "deployment_id": dep.id,
                    "status": "RUNNING",
                    "deployment_url": url,
                }))
            else:
                print(f"Deployment ID  : {dep.id}")
                print(f"Deployment URL : {url}")
            return
        if current in FAILED_STATUSES:
            print(f"\nERROR: Deployment entered {current} state.", file=sys.stderr)
            sys.exit(1)
        time.sleep(POLL_INTERVAL)

    print(f"\nERROR: Deployment did not reach RUNNING within {args.timeout}s.", file=sys.stderr)
    print(f"Deployment ID: {deployment.id}", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
