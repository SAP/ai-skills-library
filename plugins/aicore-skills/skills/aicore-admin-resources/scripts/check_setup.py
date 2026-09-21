# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
Verify that AI Core credentials and SDK are configured correctly.

Usage:
  uv run scripts/check_setup.py

Exit codes:
  0 - Setup is working
  1 - Configuration error (missing env vars or auth failure)
  2 - Package not installed
"""

import json
import sys


def main():
    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
        from ai_core_sdk.credentials import fetch_credentials
    except ImportError:
        print("ERROR: sap-ai-sdk-core is not installed.", file=sys.stderr)
        print("\nInstall it with:", file=sys.stderr)
        print('  uv add "sap-ai-sdk-core"', file=sys.stderr)
        print("\nOr run scripts directly with:", file=sys.stderr)
        print('  uv run scripts/check_setup.py', file=sys.stderr)
        sys.exit(2)

    try:
        client = AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills")
    except Exception as e:
        print(f"ERROR: Failed to initialise AI Core client: {e}", file=sys.stderr)
        print("\nEnsure the following environment variables are set:", file=sys.stderr)
        print("  AICORE_AUTH_URL    (must be the OAuth token endpoint)", file=sys.stderr)
        print("  AICORE_CLIENT_ID", file=sys.stderr)
        print("  AICORE_CLIENT_SECRET", file=sys.stderr)
        print("  AICORE_BASE_URL    (must end in /v2)", file=sys.stderr)
        print("  AICORE_RESOURCE_GROUP  (optional, defaults to 'default')", file=sys.stderr)
        print("\nOr run: aicore configure --help", file=sys.stderr)
        print("See: references/SETUP.md for full setup guide.", file=sys.stderr)
        sys.exit(1)

    resource_group_id = client.rest_client.headers.get("AI-Resource-Group", "default")
    try:
        rg = client.resource_groups.get(resource_group_id=resource_group_id)
    except Exception as e:
        print(f"ERROR: Could not reach AI Core API: {e}", file=sys.stderr)
        print("\nCheck that AICORE_BASE_URL ends in /v2 and your credentials are valid.", file=sys.stderr)
        print("Run: aicore configure --help", file=sys.stderr)
        sys.exit(1)

    creds = fetch_credentials()
    result = {
        "status": "ok",
        "resource_group": rg.resource_group_id if hasattr(rg, "resource_group_id") else str(rg),
        "base_url": creds.get("base_url"),
        "auth_url": creds.get("auth_url"),
    }
    print(json.dumps(result, indent=2))
    print("\n✓ AI Core setup is working.", file=sys.stderr)


if __name__ == "__main__":
    main()
