# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Re-validate an already-saved data destination using its stored credentials.

Useful to confirm connectivity is still working (e.g. after a credential rotation or
network change) without needing to re-enter credentials.

Usage:
  uv run scripts/validate_data_destination_by_name.py --name <name>

Examples:
  uv run scripts/validate_data_destination_by_name.py --name my-s3
  uv run scripts/validate_data_destination_by_name.py --name my-azure --resource-group prod-rg
"""

import argparse
import sys

import requests


def main():
    parser = argparse.ArgumentParser(description="Re-validate a saved data destination")
    parser.add_argument("--name", required=True, help="Data destination name")
    parser.add_argument("--resource-group", metavar="RG",
                        help="AI-Resource-Group header value. Overrides env/SDK default.")
    args = parser.parse_args()

    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add sap-ai-sdk-core", file=sys.stderr)
        sys.exit(2)

    client = AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills")
    base_url = client.rest_client.base_url.rstrip("/")
    token = client.rest_client.get_token()
    rg = args.resource_group or client.rest_client.headers.get("AI-Resource-Group", "default")

    url = f"{base_url}/tcr/dataDestinations/{args.name}/validate"
    headers = {"Authorization": token, "AI-Resource-Group": rg}

    resp = requests.post(url, headers=headers, timeout=30)
    if resp.status_code == 404:
        print(f"Not found: {args.name}", file=sys.stderr)
        sys.exit(1)
    if not resp.ok:
        print(f"ERROR {resp.status_code}: {resp.text}", file=sys.stderr)
        sys.exit(1)

    result = resp.json()
    status = result.get("status", "")
    if status == "OK":
        print(f"Validation OK — '{args.name}' credentials are valid.")
    elif status == "FAILED":
        print(f"Validation FAILED for '{args.name}': {result.get('reason', '(no reason provided)')}", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"Unexpected response: {result}")


if __name__ == "__main__":
    main()
