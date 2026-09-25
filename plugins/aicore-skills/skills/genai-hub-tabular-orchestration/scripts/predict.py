# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Send a POST /inference/deployments/{id}/predict request to the Tabular Orchestration service.

Usage:
  uv run scripts/predict.py --body '<json>'
  uv run scripts/predict.py --body '<json>' --json
  uv run scripts/predict.py --main-tenant <uuid> --resource-group <rg> --body '<json>'

Pass the complete request body produced by the interactive skill builder as --body.

Examples:
  uv run scripts/predict.py --body '{
    "modelName": "sap-rpt-1-small",
    "scenarioConfigName": "my-products-config",
    "predictionConfig": {
      "targetColumns": [{"name": "category", "taskType": "classification"}]
    },
    "columns": {
      "name": ["Wireless Headphones", "USB-C Cable"],
      "category": ["[PREDICT]", "[PREDICT]"]
    }
  }'

JSON output structure (--json):
  {
    "predictions": [
      {
        "index": 0,
        "results": [{"columnName": "category", "value": "Electronics", "confidence": 0.92}]
      }
    ]
  }
"""

import argparse
import json
import sys

import requests


def main():
    parser = argparse.ArgumentParser(
        description="Send a predict request to the Tabular Orchestration service",
        epilog=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--body", required=True, help="Complete request body as a JSON string")
    parser.add_argument(
        "--deployment-id",
        help="Deployment ID to send the predict request to.",
        required=True,
    )
    parser.add_argument(
        "--resource-group",
        metavar="RG",
        help="AI-Resource-Group header value. Overrides env/SDK default.",
    )
    parser.add_argument(
        "--main-tenant",
        metavar="UUID",
        help="ai-main-tenant header value. Overrides env/SDK default.",
    )
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output raw JSON response")
    args = parser.parse_args()

    # --- load body ---
    try:
        body = json.loads(args.body)
    except json.JSONDecodeError as exc:
        print(f"ERROR: --body is not valid JSON: {exc}", file=sys.stderr)
        sys.exit(1)

    # --- basic body validation ---
    missing = [f for f in ("modelName", "scenarioConfigName", "predictionConfig") if f not in body]
    if missing:
        print(f"ERROR: request body is missing required field(s): {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)
    if "rows" not in body and "columns" not in body:
        print("ERROR: request body must contain either 'rows' or 'columns'", file=sys.stderr)
        sys.exit(1)
    if "rows" in body and "columns" in body:
        print("ERROR: request body must not contain both 'rows' and 'columns'", file=sys.stderr)
        sys.exit(1)

    # --- SDK client ---
    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print("ERROR: sap-ai-sdk-core not installed. Run: uv add sap-ai-sdk-core", file=sys.stderr)
        sys.exit(2)

    client = AICoreV2Client.from_env(read_timeout=60, connect_timeout=15, client_type="AI Core Skills")

    base_url = client.rest_client.base_url.rstrip("/")
    token = client.rest_client.get_token()
    rg = args.resource_group or client.rest_client.headers.get("AI-Resource-Group", "default")
    deploymentId = args.deployment_id

    # ai-main-tenant: use arg > SDK header > omit (server may derive it)
    main_tenant = args.main_tenant or client.rest_client.headers.get("ai-main-tenant")
    url = f"{base_url}/inference/deployments/{deploymentId}/predict"
    headers = {
        "Authorization": token,
        "ai-resource-group": rg,
        "Content-Type": "application/json",
    }
    if main_tenant:
        headers["ai-main-tenant"] = main_tenant

    try:
        resp = requests.post(url, headers=headers, json=body, timeout=120)
    except requests.exceptions.ConnectionError as exc:
        print(f"ERROR: could not connect to {url}: {exc}", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.Timeout:
        print(f"ERROR: request timed out after 120s (try reducing numRows or batch size)", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.RequestException as exc:
        print(f"ERROR: request failed: {exc}", file=sys.stderr)
        sys.exit(1)

    if not resp.ok:
        try:
            detail = resp.json()
            msg = detail.get("message") or detail.get("error") or resp.text
        except Exception:
            msg = resp.text
        print(f"ERROR {resp.status_code}: {msg}", file=sys.stderr)
        sys.exit(1)

    try:
        result = resp.json()
    except Exception:
        print(f"ERROR: response is not valid JSON:\n{resp.text[:500]}", file=sys.stderr)
        sys.exit(1)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()