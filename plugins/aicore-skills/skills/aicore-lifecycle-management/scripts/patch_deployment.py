# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
Patch a running AI Core deployment to use a new configuration.

This swaps the configuration on a RUNNING deployment without stopping it.
The deployment must be in RUNNING, PENDING, or DEAD status.
Use this to update image, parameters, or model settings in-place.

Usage:
  uv run scripts/patch_deployment.py --deployment-id <id> --configuration-id <id>

Options:
  --deployment-id ID      Deployment ID to patch (required)
  --configuration-id ID   New configuration ID to apply (required)
  --resource-group RG     Resource group (default: read from SDK config)

Exit codes:
  0 - Success
  1 - Error

examples:
  uv run scripts/patch_deployment.py --deployment-id d8ea25e7afc61c65 --configuration-id 43b690ba-42b7-40cd-8233-c45b4b7e2614
"""

import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Patch an AI Core deployment to use a new configuration.")
    parser.add_argument("--deployment-id", dest="deployment_id", required=True,
                        help="Deployment ID to patch")
    parser.add_argument("--configuration-id", dest="configuration_id", required=True,
                        help="New configuration ID to apply")
    parser.add_argument("--resource-group", dest="resource_group", default=None,
                        help="Resource group (default: read from SDK config)")
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add \"sap-ai-sdk-core\"", file=sys.stderr)
        sys.exit(1)

    try:
        client = AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills")
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        resp = client.deployment.modify(
            deployment_id=args.deployment_id,
            configuration_id=args.configuration_id,
            resource_group=args.resource_group,
        )
        msg = getattr(resp, "message", "") or ""
        print(f"Patched  : {args.deployment_id}")
        print(f"Config   : {args.configuration_id}")
        if msg:
            print(f"Message  : {msg}")
    except Exception as e:
        print(f"ERROR: Failed to patch deployment: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
