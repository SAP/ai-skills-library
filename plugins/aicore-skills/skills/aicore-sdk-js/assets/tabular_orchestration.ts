// Install: npm install @sap-ai-sdk/tabular-orchestration
// Run:     npx tsx tabular_orchestration.ts   (or: bun run tabular_orchestration.ts)
// Purpose: Predict missing column values from tabular rows using SAP RPT models
//          via the Tabular Orchestration service (higher-level than @sap-ai-sdk/rpt —
//          context is pulled from a Scenario Configuration in the Context Registry).
// Credentials: run 'aicore configure' or see references/SETUP.md

import { TabularOrchestrationClient } from "@sap-ai-sdk/tabular-orchestration";

const client = new TabularOrchestrationClient({ resourceGroup: "default" });

// ─── Predict with scenario-based context ────────────────────────────────────
// The scenarioConfigName refers to a Scenario Configuration created via
// @sap-ai-sdk/context-registry that binds tabular artifacts to this scenario.

const response = await client.predict({
  modelName: "sap-rpt-1.6",
  scenarioConfigName: "my-customer-scenario",
  contextSelectionConfig: {
    strategy: "random",
    numRows: 100,
  },
  predictionConfig: {
    targetColumns: [{ name: "salesgroup", task_type: "classification" }],
  },
  modelConfig: { index_column: "id" },
  rows: [
    { id: "1", product: "Laptop Pro 15",    price: 1299, region: "EMEA", salesgroup: "[PREDICT]" },
    { id: "2", product: "Wireless Headset", price: 149,  region: "EMEA", salesgroup: "[PREDICT]" },
  ],
});

console.log("Predictions:", JSON.stringify(response.predictions, null, 2));

// ─── Predict with inline context (no Scenario Configuration needed) ──────────
// Pass contextRows directly when you already have representative training rows
// available in memory and don't need a managed Context Registry setup.

const inlineResponse = await client.predict({
  modelName: "sap-rpt-1.6",
  contextRows: [
    { id: "c1", product: "Laptop Pro 15",    price: 1299, region: "EMEA", salesgroup: "Electronics" },
    { id: "c2", product: "Wireless Headset", price: 149,  region: "EMEA", salesgroup: "Accessories" },
    { id: "c3", product: "Office Chair",     price: 399,  region: "EMEA", salesgroup: "Furniture"   },
  ],
  predictionConfig: {
    targetColumns: [{ name: "salesgroup", task_type: "classification" }],
  },
  modelConfig: { index_column: "id" },
  rows: [
    { id: "10", product: "Mechanical Keyboard", price: 89, region: "EMEA", salesgroup: "[PREDICT]" },
  ],
});

console.log("Inline predictions:", JSON.stringify(inlineResponse.predictions, null, 2));
