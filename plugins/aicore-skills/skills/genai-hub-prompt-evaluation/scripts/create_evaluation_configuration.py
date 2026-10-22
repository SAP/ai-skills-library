# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Create the SAP AI Core configuration that drives a GenAI evaluation execution.

This is an ordinary AI Core configuration (POST /lm/configurations) under the genai-evaluations
scenario, but with the evaluation-specific parameter bindings the workload expects. It supports
all three evaluation types via the binding you supply:
  - Prompt registry:            --prompt-template-id (+ --models)
  - Orchestration registry:     --orchestration-registry-ids
  - Grounding orchestration:    --orchestration-registry-ids (a config whose spec has a grounding module)
Common bindings: repetitions, orchestrationDeploymentURL, metrics, testDataset (a JSON blob).
The dataset artifact is bound as the "datasetFolder" input artifact.

After creating this configuration, start the run via the `aicore-lifecycle-management` skill
(its create_execution.py --configuration-id <id>).

Usage:
  # Orchestration registry (with or without grounding)
  uv run scripts/create_evaluation_configuration.py \
    --executable-id genai-evaluations-simplified \
    --dataset-artifact-id <artifact-id> \
    --test-dataset-path testdata/full_dataset.csv \
    --metrics "Pointwise Conciseness,Pointwise Answer Relevance" \
    --orchestration-registry-ids <registry-config-id> \
    --orchestration-deployment-url https://.../v2/inference/deployments/<id>

  # Prompt registry
  uv run scripts/create_evaluation_configuration.py \
    --executable-id genai-evaluations-simplified \
    --dataset-artifact-id <artifact-id> \
    --test-dataset-path testdata/full_dataset.csv \
    --metrics "Pointwise Correctness" \
    --prompt-template-id <prompt-template-id> \
    --models "gpt-4o:2024-05-13" \
    --orchestration-deployment-url https://.../v2/inference/deployments/<id>

Options:
  --name NAME                    Configuration name (default: genai-eval-conf)
  --scenario-id ID               Scenario ID (default: genai-evaluations)
  --executable-id ID             Evaluation executable ID (required; discover it via
                                 aicore-lifecycle-management get_executables.py --scenario-id genai-evaluations)
  --dataset-artifact-id ID       Artifact ID bound as "datasetFolder" (required)
  --test-dataset-path PATH       Path to the dataset within the artifact, e.g. testdata/data.csv (required)
  --test-dataset-type TYPE       csv, json, or jsonl (default: csv)
  --metrics LIST                 Comma-separated metric names and/or custom metric IDs
  --prompt-template-id ID        Prompt Registry template ID (prompt-registry type; binds `promptTemplate`)
  --models LIST                  Comma-separated models to benchmark, e.g. "gpt-4o:2024-05-13" (binds `models`)
  --orchestration-registry-ids LIST  Comma-separated orchestration-registry config IDs (binds `orchestrationRegistryIds`)
  --orchestration-deployment-url URL Orchestration deployment URL to evaluate against
  --repetitions N                Number of repetitions (default: 1)
  --test-row-count N             Evaluate only the first N rows of the dataset (binds `testRowCount`)
  --variable-mapping JSON        JSON string mapping prompt/metric vars to dataset columns, e.g.
                                 '{"all_metrics/reference":"data/ground_truth"}'
  --param KEY=VALUE              Extra parameter binding (repeatable)
  --artifact KEY=ARTIFACT_ID     Extra input artifact binding (repeatable)
  --json                         Emit JSON to stdout
  --resource-group RG            Resource group override

Exit codes:
  0 - Success
  1 - Error

JSON structure:
  {"id": "<configuration-id>", "message": "Configuration created"}

Examples:
  uv run scripts/create_evaluation_configuration.py --executable-id genai-evaluations-simplified \
    --dataset-artifact-id abc --test-dataset-path testdata/full_dataset.csv \
    --metrics "Pointwise Correctness" --orchestration-registry-ids reg-123 --json
"""

import argparse
import json
import sys

from _rest import get_rest_context, request


def parse_key_value(value, flag):
    if "=" not in value:
        print(f"ERROR: {flag} must be KEY=VALUE, got: {value!r}", file=sys.stderr)
        sys.exit(1)
    k, v = value.split("=", 1)
    return k.strip(), v.strip()


def main():
    parser = argparse.ArgumentParser(
        description="Create the AI Core configuration for a GenAI evaluation execution.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--name", default="genai-eval-conf")
    parser.add_argument("--scenario-id", dest="scenario_id", default="genai-evaluations")
    parser.add_argument("--executable-id", dest="executable_id", required=True)
    parser.add_argument("--dataset-artifact-id", dest="dataset_artifact_id", required=True)
    parser.add_argument("--test-dataset-path", dest="test_dataset_path", required=True)
    parser.add_argument("--test-dataset-type", dest="test_dataset_type",
                        choices=["csv", "json", "jsonl"], default="csv")
    parser.add_argument("--metrics", default=None)
    parser.add_argument("--prompt-template-id", dest="prompt_template_id", default=None)
    parser.add_argument("--models", default=None)
    parser.add_argument("--orchestration-registry-ids", dest="orchestration_registry_ids", default=None)
    parser.add_argument("--orchestration-deployment-url", dest="orchestration_deployment_url", default=None)
    parser.add_argument("--repetitions", default="1")
    parser.add_argument("--test-row-count", dest="test_row_count", default=None)
    parser.add_argument("--variable-mapping", dest="variable_mapping", default=None)
    parser.add_argument("--param", metavar="KEY=VALUE", action="append", default=[])
    parser.add_argument("--artifact", metavar="KEY=ARTIFACT_ID", action="append", default=[])
    parser.add_argument("--json", dest="as_json", action="store_true")
    parser.add_argument("--resource-group", dest="resource_group", default=None)
    args = parser.parse_args()

    if args.variable_mapping:
        try:
            json.loads(args.variable_mapping)
        except json.JSONDecodeError as e:
            print(f"ERROR: --variable-mapping is not valid JSON: {e}", file=sys.stderr)
            sys.exit(1)

    if bool(args.prompt_template_id) == bool(args.orchestration_registry_ids):
        print("ERROR: provide exactly one of --prompt-template-id or "
              "--orchestration-registry-ids.", file=sys.stderr)
        sys.exit(1)
    if args.prompt_template_id and not args.models:
        print("ERROR: --models is required when using --prompt-template-id.", file=sys.stderr)
        sys.exit(1)

    test_dataset = json.dumps({"path": args.test_dataset_path, "type": args.test_dataset_type})

    parameter_bindings = [
        {"key": "repetitions", "value": str(args.repetitions)},
        {"key": "testDataset", "value": test_dataset},
    ]
    if args.orchestration_deployment_url:
        parameter_bindings.append({"key": "orchestrationDeploymentURL",
                                   "value": args.orchestration_deployment_url})
    if args.metrics:
        parameter_bindings.append({"key": "metrics", "value": args.metrics})
    if args.prompt_template_id:
        parameter_bindings.append({"key": "promptTemplate", "value": args.prompt_template_id})
    if args.models:
        parameter_bindings.append({"key": "models", "value": args.models})
    if args.orchestration_registry_ids:
        parameter_bindings.append({"key": "orchestrationRegistryIds",
                                   "value": args.orchestration_registry_ids})
    if args.test_row_count:
        parameter_bindings.append({"key": "testRowCount", "value": str(args.test_row_count)})
    if args.variable_mapping:
        parameter_bindings.append({"key": "variableMapping", "value": args.variable_mapping})
    for raw in args.param:
        k, v = parse_key_value(raw, "--param")
        parameter_bindings.append({"key": k, "value": v})

    input_artifact_bindings = [{"key": "datasetFolder", "artifactId": args.dataset_artifact_id}]
    for raw in args.artifact:
        k, v = parse_key_value(raw, "--artifact")
        input_artifact_bindings.append({"key": k, "artifactId": v})

    body = {
        "name": args.name,
        "scenarioId": args.scenario_id,
        "executableId": args.executable_id,
        "inputArtifactBindings": input_artifact_bindings,
        "parameterBindings": parameter_bindings,
    }

    base_url, headers = get_rest_context(args.resource_group)
    result = request("POST", f"{base_url}/lm/configurations", headers, json_body=body)

    config_id = result.get("id") if isinstance(result, dict) else None
    message = result.get("message", "Configuration created") if isinstance(result, dict) else ""

    if args.as_json:
        print(json.dumps({"id": config_id, "message": message}, indent=2))
    else:
        print(config_id or "")
        print(f"{message}: {config_id}", file=sys.stderr)


if __name__ == "__main__":
    main()
