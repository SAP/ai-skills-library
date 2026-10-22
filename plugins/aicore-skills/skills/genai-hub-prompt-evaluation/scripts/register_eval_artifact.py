# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Register the evaluation dataset folder as an AI Core artifact, with the evaluation label.

The GenAI evaluation service only discovers dataset artifacts that carry the label
`ext.ai.sap.com/prompt-evaluation=true`. This script owns that evaluation-specific registration
(POST /lm/artifacts) so the flow stays self-contained. For generic (non-evaluation) artifact
registration, use the `aicore-lifecycle-management` skill instead.

The artifact URL points at the folder root in the object store, e.g.
ai://<object-store-secret>/genaiEvaluation/<user>. The evaluation config's --test-dataset-path is
then relative to that root (e.g. testdata/full_dataset.csv).

Usage:
  uv run scripts/register_eval_artifact.py \
    --name genai-eval-test-data \
    --url ai://default/genaiEvaluation/<user>

Options:
  --name NAME           Artifact name (required)
  --url URL             Artifact URL, e.g. ai://<object-store-secret>/genaiEvaluation/<user> (required)
  --scenario-id ID      Scenario ID (default: genai-evaluations)
  --kind KIND           Artifact kind: other (default), dataset
  --description TEXT    Optional description
  --label KEY=VALUE     Extra label (repeatable); the prompt-evaluation label is always added
  --json                Emit JSON to stdout
  --resource-group RG   Resource group override

Exit codes:
  0 - Success
  1 - Error

JSON structure:
  {"id": "<artifact-id>", "message": "...", "url": "..."}

Examples:
  uv run scripts/register_eval_artifact.py --name genai-eval-test-data --url ai://default/genaiEvaluation/u1
  uv run scripts/register_eval_artifact.py --name eval-data --url ai://store/genaiEvaluation/u1 --json | jq -r .id
"""

import argparse
import json
import sys

from _rest import get_rest_context, request

PROMPT_EVAL_LABEL = {"key": "ext.ai.sap.com/prompt-evaluation", "value": "true"}


def parse_labels(label_args):
    labels = [dict(PROMPT_EVAL_LABEL)]
    for item in label_args:
        if "=" not in item:
            print(f"ERROR: --label value '{item}' is not in key=value format", file=sys.stderr)
            sys.exit(1)
        key, _, value = item.partition("=")
        labels.append({"key": key.strip(), "value": value.strip()})
    return labels


def main():
    parser = argparse.ArgumentParser(
        description="Register the evaluation dataset artifact (with the prompt-evaluation label).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--name", required=True, help="Artifact name")
    parser.add_argument("--url", required=True, help="Artifact URL, e.g. ai://<secret>/genaiEvaluation/<user>")
    parser.add_argument("--scenario-id", dest="scenario_id", default="genai-evaluations")
    parser.add_argument("--kind", choices=["other", "dataset"], default="other")
    parser.add_argument("--description", default="Dataset for GenAI evaluation")
    parser.add_argument("--label", metavar="KEY=VALUE", action="append", default=[],
                        help="Extra label (repeatable); the prompt-evaluation label is always added")
    parser.add_argument("--json", dest="as_json", action="store_true")
    parser.add_argument("--resource-group", dest="resource_group", default=None)
    args = parser.parse_args()

    body = {
        "name": args.name,
        "kind": args.kind,
        "url": args.url,
        "scenarioId": args.scenario_id,
        "description": args.description,
        "labels": parse_labels(args.label),
    }

    base_url, headers = get_rest_context(args.resource_group)
    result = request("POST", f"{base_url}/lm/artifacts", headers, json_body=body)

    artifact_id = result.get("id") if isinstance(result, dict) else None
    message = result.get("message", "Artifact registered.") if isinstance(result, dict) else ""
    url = result.get("url", args.url) if isinstance(result, dict) else args.url

    if args.as_json:
        print(json.dumps({"id": artifact_id, "message": message, "url": url}, indent=2))
    else:
        print(artifact_id or "")
        print(f"{message} (id={artifact_id})", file=sys.stderr)


if __name__ == "__main__":
    main()
