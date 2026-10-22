# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Create (or reuse) custom SAP AI Core evaluation metrics from a definition file.

For each metric definition, the script looks
for an existing metric with the same scenario + name + version and reuses its ID; otherwise it
creates a new metric via POST /lm/evaluationMetrics. This makes the script idempotent.

The definition file is either:
  - a JSON array of metric-definition objects, or
  - a JSONL file with one metric-definition object per line.

Each definition must include: scenario, name, version, evaluationMethod, metricType, and (for
llm-as-a-judge metrics) a spec block. See templates/custom-metric.json for a full example.

Usage:
  uv run scripts/create_evaluation_metric.py --file templates/custom-metric.json
  uv run scripts/create_evaluation_metric.py --file my-metrics.jsonl --json

Options:
  --file PATH           Path to a JSON (array) or JSONL metric-definition file (required)
  --json                Emit JSON to stdout
  --resource-group RG   Resource group override

Exit codes:
  0 - Success
  1 - Error

JSON structure:
  [{"id": "...", "name": "...", "scenario": "...", "version": "...", "created": bool}]

Examples:
  uv run scripts/create_evaluation_metric.py --file templates/custom-metric.json
  uv run scripts/create_evaluation_metric.py --file templates/custom-metric.json --json | jq -r '.[].id'
"""

import argparse
import json
import sys

from _rest import get_rest_context, request

REQUIRED_FIELDS = ["scenario", "name", "version", "evaluationMethod", "metricType"]


def _parse_jsonl(path, text):
    defs = []
    for i, line in enumerate(text.splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        try:
            defs.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"ERROR: {path} line {i} is not valid JSON: {e}", file=sys.stderr)
            sys.exit(1)
    if not defs:
        print(f"ERROR: no metric definitions found in {path}.", file=sys.stderr)
        sys.exit(1)
    return defs


def load_definitions(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
    except OSError as e:
        print(f"ERROR: could not read {path}: {e}", file=sys.stderr)
        sys.exit(1)

    # Whole-file JSON first: an array of objects, or a single (possibly pretty-printed) object.
    if text.lstrip().startswith(("[", "{")):
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            data = None  # likely JSONL (multiple objects, one per line) — fall through
        if isinstance(data, dict):
            return [data]
        if isinstance(data, list):
            return data
        if data is not None:
            print("ERROR: JSON metric file must contain an object or an array of objects.",
                  file=sys.stderr)
            sys.exit(1)

    # JSONL form (one JSON object per non-empty line).
    return _parse_jsonl(path, text)


def main():
    parser = argparse.ArgumentParser(
        description="Create or reuse custom evaluation metrics from a definition file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--file", required=True, help="Path to a JSON array or JSONL metric file")
    parser.add_argument("--json", dest="as_json", action="store_true")
    parser.add_argument("--resource-group", dest="resource_group", default=None)
    args = parser.parse_args()

    definitions = load_definitions(args.file)

    base_url, headers = get_rest_context(args.resource_group)
    endpoint = f"{base_url}/lm/evaluationMetrics"

    existing = request("GET", endpoint, headers)
    existing_metrics = existing.get("resources", []) if isinstance(existing, dict) else []

    results = []
    for metric in definitions:
        missing = [f for f in REQUIRED_FIELDS if f not in metric]
        if missing:
            print(f"ERROR: metric '{metric.get('name', '?')}' missing required field(s): "
                  f"{', '.join(missing)}", file=sys.stderr)
            sys.exit(1)

        scenario, name, version = metric["scenario"], metric["name"], metric["version"]

        match = next(
            (m for m in existing_metrics
             if m.get("scenario") == scenario and m.get("name") == name
             and m.get("version") == version),
            None,
        )
        if match:
            metric_id = match.get("id")
            print(f"Reused   : {name} v{version} -> {metric_id}", file=sys.stderr)
            results.append({"id": metric_id, "name": name, "scenario": scenario,
                            "version": version, "created": False})
            continue

        created = request("POST", endpoint, headers, json_body=metric)
        metric_id = created.get("id") if isinstance(created, dict) else None
        print(f"Created  : {name} v{version} -> {metric_id}", file=sys.stderr)
        results.append({"id": metric_id, "name": name, "scenario": scenario,
                        "version": version, "created": True})

    if args.as_json:
        print(json.dumps(results, indent=2))
    else:
        ids = ",".join(r["id"] for r in results if r["id"])
        print(ids)
        print(f"{len(results)} metric(s) processed "
              f"({sum(1 for r in results if r['created'])} created).", file=sys.stderr)


if __name__ == "__main__":
    main()
