# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
List SAP AI Core evaluation metrics (system-defined and custom).

Use this to discover the exact metric names to pass to create_evaluation_configuration.py, and to
find the IDs of custom metrics you have already created.

Usage:
  uv run scripts/list_evaluation_metrics.py
  uv run scripts/list_evaluation_metrics.py --kind system
  uv run scripts/list_evaluation_metrics.py --kind custom
  uv run scripts/list_evaluation_metrics.py --name "Pointwise"
  uv run scripts/list_evaluation_metrics.py --scenario genai-evaluations-test
  uv run scripts/list_evaluation_metrics.py --json

Options:
  --kind KIND           Filter: all (default), system (systemPredefined=true), custom
  --name SUBSTR         Case-insensitive substring match on the metric name
  --scenario ID         Filter by scenario
  --response-format FMT concise (default) or detailed
  --json                Emit JSON to stdout
  --resource-group RG   Resource group override

Exit codes:
  0 - Success
  1 - Error

JSON structure:
  [{"id": "...", "name": "...", "scenario": "...", "version": "...",
    "systemPredefined": bool, "evaluationMethod": "...", "metricType": "..."}]

Examples:
  uv run scripts/list_evaluation_metrics.py --kind system --name conciseness
  uv run scripts/list_evaluation_metrics.py --kind custom --json | jq '.[].id'
"""

import argparse
import json
import sys

from _rest import get_rest_context, request


def main():
    parser = argparse.ArgumentParser(
        description="List SAP AI Core evaluation metrics.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--kind", choices=["all", "system", "custom"], default="all")
    parser.add_argument("--name", default=None, help="Case-insensitive substring match on name")
    parser.add_argument("--scenario", default=None, help="Filter by scenario")
    parser.add_argument("--response-format", dest="response_format",
                        choices=["concise", "detailed"], default="concise")
    parser.add_argument("--json", dest="as_json", action="store_true")
    parser.add_argument("--resource-group", dest="resource_group", default=None)
    args = parser.parse_args()

    base_url, headers = get_rest_context(args.resource_group)
    body = request("GET", f"{base_url}/lm/evaluationMetrics", headers)
    metrics = body.get("resources", []) if isinstance(body, dict) else []

    def keep(m):
        sp = bool(m.get("systemPredefined"))
        if args.kind == "system" and not sp:
            return False
        if args.kind == "custom" and sp:
            return False
        if args.scenario and m.get("scenario") != args.scenario:
            return False
        if args.name and args.name.lower() not in (m.get("name") or "").lower():
            return False
        return True

    metrics = [m for m in metrics if keep(m)]

    if args.as_json:
        out = [
            {
                "id": m.get("id"),
                "name": m.get("name"),
                "scenario": m.get("scenario"),
                "version": m.get("version"),
                "systemPredefined": bool(m.get("systemPredefined")),
                "evaluationMethod": m.get("evaluationMethod"),
                "metricType": m.get("metricType"),
            }
            for m in metrics
        ]
        print(json.dumps(out, indent=2))
        return

    if not metrics:
        print("No evaluation metrics found.")
        return

    for m in metrics:
        tag = "system" if m.get("systemPredefined") else "custom"
        line = f"[{tag}] {m.get('name')}"
        if not m.get("systemPredefined"):
            line += f"  id={m.get('id')}"
        print(line)
        if args.response_format == "detailed":
            print(f"       scenario={m.get('scenario')} version={m.get('version')} "
                  f"method={m.get('evaluationMethod')} type={m.get('metricType')}")

    print(f"{len(metrics)} metric(s) found.")


if __name__ == "__main__":
    main()
