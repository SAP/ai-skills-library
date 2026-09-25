# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Create a new tabular artifact.

Usage:
  uv run scripts/create_tabular_artifact.py \\
    --name <name> --data-destination <dd-name> --path /data/file.csv --type CSV \\
    --csn-columns "col1:cds.String,col2:cds.Integer,col3:cds.Decimal" --entity-name MyEntity

Schema modes (pick one):
  --definition-type AUTO          Auto-derive schema from the file (default)
  --csn-columns col:cds.Type,...  Provide column names and types inline — RECOMMENDED.
                                  Uses DOCUMENT mode automatically.
  --definition-type REFERENCE     Point to a CSN JSON file on the HDL
      requires: --csn-reference /path/to/csn.json --entity-name <name>
  --definition-type DOCUMENT      Provide full CSN JSON inline
      requires: --csn-document '{"definitions": {...}}' --entity-name <name>

Supported cds.* types:
  cds.UUID, cds.Boolean, cds.Integer, cds.Int16, cds.Int32, cds.Int64, cds.UInt8,
  cds.Decimal, cds.Double, cds.Date, cds.Time, cds.DateTime, cds.Timestamp,
  cds.String, cds.Binary, cds.LargeBinary, cds.LargeString, cds.Map, cds.Vector

Optional:
  --columns col1,col2,...         Include only these columns (selectedColumns in request).
                                  Defaults to all columns when --csn-columns is used.
  --entity-name <name>            Entity name in the CSN model (recommended with --csn-columns)

Examples:
  # AUTO (simplest for CSV with a header row)
  uv run scripts/create_tabular_artifact.py \\
      --name customer-ta --data-destination my-hdl \\
      --path /data/customer.csv --type CSV

  # DOCUMENT via --csn-columns (recommended)
  uv run scripts/create_tabular_artifact.py \\
      --name customer-ta --data-destination my-hdl \\
      --path /data/customer.csv --type CSV \\
      --csn-columns "id:cds.Integer,name:cds.String,score:cds.Decimal,active:cds.Boolean" \\
      --entity-name Customer

  # REFERENCE CSN
  uv run scripts/create_tabular_artifact.py \\
      --name inventory-ta --data-destination my-hdl \\
      --path /data/inventory.csv --type CSV \\
      --definition-type REFERENCE \\
      --csn-reference /data/metadata/inventory_csn.json \\
      --entity-name Inventory
"""

import argparse
import json
import sys

import requests

_VALID_CDS_TYPES = {
    "cds.UUID", "cds.Boolean", "cds.Integer", "cds.Int16", "cds.Int32", "cds.Int64", "cds.UInt8",
    "cds.Decimal", "cds.Double", "cds.Date", "cds.Time", "cds.DateTime", "cds.Timestamp",
    "cds.String", "cds.Binary", "cds.LargeBinary", "cds.LargeString", "cds.Map", "cds.Vector",
}


def parse_csn_columns(raw: str) -> list[tuple[str, str]]:
    result = []
    for pair in raw.split(","):
        pair = pair.strip()
        if ":" not in pair:
            print(f"ERROR: --csn-columns entry '{pair}' must be in name:cds.Type format", file=sys.stderr)
            sys.exit(1)
        col, typ = pair.split(":", 1)
        col, typ = col.strip(), typ.strip()
        if typ not in _VALID_CDS_TYPES:
            print(f"ERROR: unsupported type '{typ}'. Supported: {', '.join(sorted(_VALID_CDS_TYPES))}", file=sys.stderr)
            sys.exit(1)
        result.append((col, typ))
    return result


def build_csn_document_from_columns(columns: list[tuple[str, str]], entity_name: str) -> dict:
    return {
        "definitions": {
            entity_name: {
                "kind": "entity",
                "elements": {col: {"type": typ} for col, typ in columns},
            }
        }
    }


def build_csn_definition(args) -> tuple[dict, list[str] | None]:
    """Returns (definition dict, auto-derived selectedColumns or None)."""
    if args.csn_columns:
        entity_name = args.entity_name or "Entity"
        parsed = parse_csn_columns(args.csn_columns)
        doc = build_csn_document_from_columns(parsed, entity_name)
        return {"definitionType": "DOCUMENT", "document": doc}, [col for col, _ in parsed]

    dtype = args.definition_type
    if dtype == "AUTO":
        definition: dict = {"definitionType": "AUTO"}
        if args.file_type == "CSV":
            definition["autoConfig"] = {"csvOptions": {"columnListInFirstRow": True, "delimiter": ","}}
        return definition, None
    elif dtype == "REFERENCE":
        if not args.csn_reference:
            print("ERROR: --csn-reference is required for REFERENCE type", file=sys.stderr)
            sys.exit(1)
        return {"definitionType": "REFERENCE", "documentReference": {"path": args.csn_reference}}, None
    elif dtype == "DOCUMENT":
        if not args.csn_document:
            print("ERROR: --csn-document is required for DOCUMENT type", file=sys.stderr)
            sys.exit(1)
        try:
            doc = json.loads(args.csn_document)
        except json.JSONDecodeError as e:
            print(f"ERROR: --csn-document is not valid JSON: {e}", file=sys.stderr)
            sys.exit(1)
        return {"definitionType": "DOCUMENT", "document": doc}, None
    raise ValueError(f"Unknown definition type: {dtype}")


def main():
    parser = argparse.ArgumentParser(description="Create a tabular artifact")
    parser.add_argument("--name", required=True, help="Tabular artifact name (1-80 chars, kebab-case)")
    parser.add_argument("--data-destination", required=True, dest="data_destination",
                        help="Name of the data destination")
    parser.add_argument("--path", required=True, help="Absolute path to the file on the data destination")
    parser.add_argument("--type", required=True, choices=["CSV", "PARQUET", "DELTA"],
                        dest="file_type", help="Source file format")
    parser.add_argument("--csn-columns", dest="csn_columns",
                        help="Column definitions as 'name:cds.Type,...' (DOCUMENT mode, recommended)")
    parser.add_argument("--definition-type", default="AUTO", choices=["AUTO", "REFERENCE", "DOCUMENT"],
                        dest="definition_type", help="Schema definition mode (default: AUTO)")
    parser.add_argument("--csn-reference", dest="csn_reference",
                        help="Path to CSN file on the data destination (REFERENCE mode)")
    parser.add_argument("--csn-document", dest="csn_document",
                        help="CSN JSON string (DOCUMENT mode)")
    parser.add_argument("--entity-name", dest="entity_name",
                        help="Entity name in CSN model (required for DOCUMENT/REFERENCE; optional for AUTO)")
    parser.add_argument("--columns", help="Comma-separated list of columns to include (selectedColumns)")
    parser.add_argument("--resource-group", metavar="RG", help="AI-Resource-Group header value. Overrides env/SDK default.")
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

    definition, auto_columns = build_csn_definition(args)
    csn_metadata: dict = {"definition": definition}
    if args.entity_name:
        csn_metadata["entityName"] = args.entity_name
    elif args.csn_columns:
        csn_metadata["entityName"] = "Entity"

    if args.columns:
        csn_metadata["selectedColumns"] = [c.strip() for c in args.columns.split(",")]
    elif auto_columns:
        csn_metadata["selectedColumns"] = auto_columns

    body = {
        "dataDestinationName": args.data_destination,
        "path": args.path,
        "type": args.file_type,
        "csnMetadata": csn_metadata,
    }

    url = f"{base_url}/tcr/tabularArtifacts/{args.name}"
    headers = {"Authorization": token, "AI-Resource-Group": rg, "Content-Type": "application/json"}

    resp = requests.put(url, headers=headers, json=body, timeout=30)
    if not resp.ok:
        print(f"ERROR {resp.status_code}: {resp.text}", file=sys.stderr)
        sys.exit(1)

    result = resp.json()
    print(f"Created tabular artifact: {result['name']}")


if __name__ == "__main__":
    main()
