// Install: npm install @sap-ai-sdk/rpt
// Run:     npx tsx rpt.ts   (or: bun run rpt.ts)
// Purpose: Predict a target column from tabular rows with SAP-RPT-1 (relational/tabular prediction).
// Credentials: run 'aicore configure' or see references/SETUP.md

import { RptClient } from "@sap-ai-sdk/rpt";
import type { PredictResponsePayload, PredictionData } from "@sap-ai-sdk/rpt";

// `as const` is required so PredictionData<typeof schema> can type the rows.
const schema = [
  { name: "PRODUCT", dtype: "string" },
  { name: "PRICE", dtype: "numeric" },
  { name: "PRODUCTION_DATE", dtype: "date" },
  { name: "__row_idx__", dtype: "string" },
  { name: "SALESGROUP", dtype: "string" },
] as const;

const data: PredictionData<typeof schema> = {
  prediction_config: {
    target_columns: [{ name: "SALESGROUP", prediction_placeholder: "[PREDICT]" }],
  },
  index_column: "__row_idx__",
  rows: [
    {
      PRODUCT: "Laptop",
      PRICE: 999.99,
      PRODUCTION_DATE: "2025-01-15",
      __row_idx__: "35",
      SALESGROUP: "[PREDICT]",
    },
    {
      PRODUCT: "Desktop",
      PRICE: 921.5,
      PRODUCTION_DATE: "2024-12-02",
      __row_idx__: "42",
      SALESGROUP: "Electronics",
    },
  ],
};

const client = new RptClient();

// Primary: predict using an explicit, typed schema.
const result: PredictResponsePayload = await client.predictWithSchema(schema, data);
console.log(JSON.stringify(result, null, 2));

// Alternative: let the client infer the schema from the data.
// const inferred: PredictResponsePayload = await client.predictWithoutSchema(data);
// console.log(JSON.stringify(inferred, null, 2));
