# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Create a new HDL data destination.

Usage:
  uv run scripts/create_data_destination.py --name <name> --host <hostname>
      [--description TEXT] [--labels key=value ...] [--adapter-type File]

Examples:
  uv run scripts/create_data_destination.py --name my-hdl \\
      --host abc123.files.hdl.eu10.hanacloud.ondemand.com

  uv run scripts/create_data_destination.py --name prod-hdl \\
      --host abc123.files.hdl.eu10.hanacloud.ondemand.com \\
      --labels "ext.ai.sap.com/env=prod" --description "Production HDL"

Notes:
  - hostname must NOT include https:// or any URL scheme
  - name: lowercase letters, numbers, hyphens; 1-127 chars
"""

import argparse
import json
import sys

import requests


def parse_labels(raw: list[str]) -> list[dict]:
    labels = []
    for item in raw:
        if "=" not in item:
            print(f"ERROR: label '{item}' must be in key=value format", file=sys.stderr)
            sys.exit(1)
        key, value = item.split("=", 1)
        labels.append({"key": key, "value": value})
    return labels


def main():
    parser = argparse.ArgumentParser(description="Create an HDL data destination")
    parser.add_argument("--name", required=True, help="Data destination name")
    parser.add_argument("--host", required=True, help="HDL hostname (no https:// prefix)")
    parser.add_argument("--description", help="Optional description")
    parser.add_argument("--labels", nargs="+", default=[], metavar="KEY=VALUE",
                        help="Labels, e.g. ext.ai.sap.com/env=prod")
    parser.add_argument("--adapter-type", choices=["File"], default="File",
                        help="Adapter type (default: File)")
    parser.add_argument("--resource-group", metavar="RG", help="AI-Resource-Group header value. Overrides env/SDK default.")
    args = parser.parse_args()

    if args.host.startswith("http"):
        print("ERROR: --host must be a hostname only, without https://", file=sys.stderr)
        sys.exit(1)

    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add sap-ai-sdk-core", file=sys.stderr)
        sys.exit(2)

    client = AICoreV2Client.from_env(read_timeout=15, connect_timeout=15, client_type="AI Core Skills")
    base_url = client.rest_client.base_url.rstrip("/")
    token = client.rest_client.get_token()
    rg = args.resource_group or client.rest_client.headers.get("AI-Resource-Group", "default")

    body = {
        "type": "HDL",
        "config": {"host": args.host},
        "adapterType": args.adapter_type,
    }
    if args.description:
        body["description"] = args.description
    if args.labels:
        body["labels"] = parse_labels(args.labels)

    url = f"{base_url}/tcr/dataDestinations/{args.name}"
    headers = {"Authorization": token, "AI-Resource-Group": rg, "Content-Type": "application/json"}

    resp = requests.put(url, headers=headers, json=body, timeout=30)
    if not resp.ok:
        print(f"ERROR {resp.status_code}: {resp.text}", file=sys.stderr)
        sys.exit(1)

    result = resp.json()
    print(f"Created data destination: {result['name']}")
    if result.get("subjectPatterns"):
        print(file=sys.stderr)
        print("ACTION REQUIRED — HDL file system access", file=sys.stderr)
        print("=" * 60, file=sys.stderr)
        print("These subject pattern(s) must be registered in the HDL", file=sys.stderr)
        print("file system BEFORE any tabular artifact can be created:", file=sys.stderr)
        print(file=sys.stderr)
        for p in result["subjectPatterns"]:
            print(f"  {p}", file=sys.stderr)
        print(file=sys.stderr)
        print("Share them with your HDL admin and confirm access is", file=sys.stderr)
        print("granted before proceeding. Skipping this step will cause", file=sys.stderr)
        print("a 403 Access Denied error when creating tabular artifacts.", file=sys.stderr)
        print("=" * 60, file=sys.stderr)


if __name__ == "__main__":
    main()
