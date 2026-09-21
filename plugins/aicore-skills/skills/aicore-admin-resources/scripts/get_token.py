# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0"]
# ///
"""
Print a raw token (without "Bearer " prefix) for use with curl or direct REST calls.
Designed for shell variable capture — only the token goes to stdout.

Usage:
  export TOKEN=$(uv run scripts/get_token.py)
  curl -H "Authorization: Bearer $TOKEN" ...

Exit codes:
  0 - Token printed successfully
  1 - Auth or config error
"""

import sys


def main():
    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add \"sap-ai-sdk-core\"", file=sys.stderr)
        sys.exit(1)

    try:
        client = AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills")
        token = client.rest_client.get_token()
    except Exception as e:
        print(f"ERROR: Failed to get token: {e}", file=sys.stderr)
        print("Ensure AICORE_AUTH_URL, AICORE_CLIENT_ID, AICORE_CLIENT_SECRET are set.", file=sys.stderr)
        sys.exit(1)

    # Strip Bearer prefix — callers add it themselves (e.g. Authorization: Bearer $TOKEN)
    if token.startswith("Bearer "):
        token = token[len("Bearer "):]

    # Only the token to stdout — warnings go to stderr so $() capture is clean
    print(token)
    print("Token retrieved successfully.", file=sys.stderr)


if __name__ == "__main__":
    main()
