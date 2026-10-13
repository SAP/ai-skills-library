# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Retrieve aggregate evaluation results for a completed evaluation execution.

An evaluation execution spawns one child run per model/prompt-config combination. Their aggregate
metrics are stored in the tracking service and tagged with the parent execution ID. This script
queries them via:
  GET /lm/metrics?tagFilters=evaluation.ai.sap.com/child-of=<execution-id>

Run this only once the execution status is COMPLETED (check with
aicore-lifecycle-management get_executions.py --execution-id <id>). For instance-level results
(per-row scores, logs) download the SQLite DB — see references/RESULTS_ANALYSIS.md.

Usage:
  uv run scripts/get_evaluation_results.py --execution-id <id>
  uv run scripts/get_evaluation_results.py --execution-id <id> --json

Options:
  --execution-id ID     Parent evaluation execution ID (required)
  --response-format FMT concise (default) or detailed
  --json                Emit JSON to stdout
  --resource-group RG   Resource group override

Exit codes:
  0 - Success
  1 - Error

JSON structure:
  [{"run_id": "...", "run_name": "...", "model": "...",
    "metrics": [{"name": "...", "value": ...}], "tags": [{"name": "...", "value": "..."}]}]

Examples:
  uv run scripts/get_evaluation_results.py --execution-id <execution-id>
  uv run scripts/get_evaluation_results.py --execution-id <execution-id> --json | jq
"""

import argparse
import json
import sys
from urllib.parse import quote

from _rest import get_rest_context, request

MODEL_TAG = "evaluation.ai.sap.com/model"


def model_from_tags(tags):
    for t in tags or []:
        if t.get("name") == MODEL_TAG:
            return t.get("value")
    return "Unknown"


def main():
    parser = argparse.ArgumentParser(
        description="Retrieve aggregate evaluation results for an execution.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--execution-id", dest="execution_id", required=True)
    parser.add_argument("--response-format", dest="response_format",
                        choices=["concise", "detailed"], default="concise")
    parser.add_argument("--json", dest="as_json", action="store_true")
    parser.add_argument("--resource-group", dest="resource_group", default=None)
    args = parser.parse_args()

    base_url, headers = get_rest_context(args.resource_group)
    tag_filter = quote(f"evaluation.ai.sap.com/child-of={args.execution_id}", safe="=/.")
    body = request("GET", f"{base_url}/lm/metrics?tagFilters={tag_filter}", headers)
    runs = body.get("resources", []) if isinstance(body, dict) else []

    if args.as_json:
        out = []
        for r in runs:
            tags = r.get("tags", []) or []
            out.append({
                "run_id": r.get("executionId") or r.get("runId"),
                "run_name": next((t.get("value") for t in tags
                                  if t.get("name") == "evaluation.ai.sap.com/run-name"), None),
                "model": model_from_tags(tags),
                "metrics": [{"name": m.get("name"), "value": m.get("value")}
                            for m in (r.get("metrics") or [])],
                "tags": [{"name": t.get("name"), "value": t.get("value")} for t in tags],
            })
        print(json.dumps(out, indent=2))
        return

    if not runs:
        print("No evaluation results found. Is the execution COMPLETED?")
        return

    for r in runs:
        tags = r.get("tags", []) or []
        run_id = r.get("executionId") or r.get("runId") or "?"
        print(f"run {run_id}  model={model_from_tags(tags)}")
        for m in (r.get("metrics") or []):
            print(f"  {m.get('name')}: {m.get('value')}")
        if args.response_format == "detailed":
            for t in tags:
                print(f"  [tag] {t.get('name')}: {t.get('value')}")

    print(f"{len(runs)} run(s) found.")


if __name__ == "__main__":
    main()
