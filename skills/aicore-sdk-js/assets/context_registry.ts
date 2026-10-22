/**
 * Install: npm install @sap-ai-sdk/context-registry
 * Run:     npx tsx context_registry.ts   (or: bun run context_registry.ts)
 *
 * Context Registry (TCR) — manage data destinations, tabular artifacts,
 * and scenario configurations that feed structured data to AI scenarios.
 *
 * Full lifecycle:
 *   1. Create an Azure data destination (points to your storage)
 *   2. Create a tabular artifact (virtual table backed by that destination)
 *   3. Create a scenario configuration (binds artifact(s) to an AI scenario)
 *   4. List resources and clean up
 *
 * Credentials: run 'aicore configure' or see references/SETUP.md
 */

import {
  DataDestinationsApi,
  TabularArtifactsApi,
  ScenarioConfigurationManagerApi,
} from "@sap-ai-sdk/context-registry";
import type {
  GetDataDestinations,
  GetDataDestination,
  TabularArtifactDetails,
  ScenarioConfigurationObject,
} from "@sap-ai-sdk/context-registry";

const resourceGroup = { "AI-Resource-Group": "default" };

// ─── 1. Data Destination ────────────────────────────────────────────────────
// Register an Azure Blob Storage container as a data source.
// Creation is async: the API returns 202 and processes in the background.
// Poll getDataDestinationByName() until status becomes "ACTIVE".

const destName = "my-azure-destination";

await DataDestinationsApi.createUpdateDataDestination(
  destName,
  {
    type: "AZURE",
    config: {
      account_name: process.env.AZURE_STORAGE_ACCOUNT!,
      container_uri: process.env.AZURE_CONTAINER_URI!, // e.g. https://<account>.blob.core.windows.net/<container>
      sas_token: process.env.AZURE_SAS_TOKEN!,         // must grant read + list (r + l)
    },
  },
  resourceGroup,
).execute();
console.log(`Data destination '${destName}' creation accepted (202).`);

// Poll until ACTIVE (simplified — add retry limit in production)
let destination: GetDataDestination;
do {
  destination = await DataDestinationsApi.getDataDestinationByName(
    destName,
    resourceGroup,
  ).execute();
  console.log("Destination status:", destination.status);
  if (destination.status === "ERROR") throw new Error(destination.errorMessage ?? "Destination creation failed.");
  if (destination.status !== "ACTIVE") await new Promise((r) => setTimeout(r, 3000));
} while (destination.status !== "ACTIVE");
console.log("Destination is ACTIVE.");

// ─── 2. Tabular Artifact ─────────────────────────────────────────────────────
// A tabular artifact is a virtual table pointing to a file in the destination.

const artifactName = "my-parquet-artifact";

await TabularArtifactsApi.createTabularArtifact(
  artifactName,
  {
    dataDestinationName: destName,
    type: "PARQUET",
    path: "/data/customers.parquet",
    csnMetadata: {
      selectedColumns: new Set(["customer_id", "customer_name", "region"]),
      definition: { definitionType: "AUTO" },
    },
  },
  resourceGroup,
).execute();
console.log(`Tabular artifact '${artifactName}' creation accepted (202).`);

// Poll until ACTIVE
let artifact: TabularArtifactDetails;
do {
  artifact = await TabularArtifactsApi.getTabularArtifactByName(
    artifactName,
    resourceGroup,
  ).execute();
  console.log("Artifact status:", artifact.status);
  if (artifact.status === "ERROR") throw new Error(artifact.errorMessage ?? "Artifact creation failed.");
  if (artifact.status !== "ACTIVE") await new Promise((r) => setTimeout(r, 3000));
} while (artifact.status !== "ACTIVE");
console.log("Tabular artifact is ACTIVE.");

// Preview the first 10 rows of data
const preview = await TabularArtifactsApi.getTabularArtifactData(
  artifactName,
  resourceGroup,
).execute();
console.log("Data preview:", JSON.stringify(preview, null, 2));

// ─── 3. Scenario Configuration ───────────────────────────────────────────────
// Bind one or more tabular artifacts to a named scenario.

const scenarioName = "my-customer-scenario";

await ScenarioConfigurationManagerApi.createScenarioConfiguration(
  scenarioName,
  {
    description: "Customer data scenario for AI analysis",
    tabularArtifacts: [{ name: artifactName }],
    labels: [{ key: "env", value: "production" }],
  },
  resourceGroup,
).execute();
console.log(`Scenario configuration '${scenarioName}' creation accepted (202).`);

// Poll until ACTIVE
let scenario: ScenarioConfigurationObject;
do {
  scenario = await ScenarioConfigurationManagerApi.getScenarioConfigurationByName(
    scenarioName,
    resourceGroup,
  ).execute();
  console.log("Scenario status:", scenario.status);
  if (scenario.status === "ERROR") throw new Error(scenario.errorMessage ?? "Scenario creation failed.");
  if (scenario.status !== "ACTIVE") await new Promise((r) => setTimeout(r, 3000));
} while (scenario.status !== "ACTIVE");
console.log("Scenario configuration is ACTIVE.");

// ─── 4. List resources ───────────────────────────────────────────────────────

const destinations: GetDataDestinations =
  await DataDestinationsApi.getAllDataDestinations({}, resourceGroup).execute();
console.log(`Total data destinations: ${destinations.count}`);

const artifacts = await TabularArtifactsApi.getAllTabularArtifacts(
  {},
  resourceGroup,
).execute();
console.log(`Total tabular artifacts: ${artifacts.count}`);

// Search destinations by label
const filtered = await DataDestinationsApi.searchDestinations(
  { labels: [{ key: "env", value: "production" }] },
  {},
  resourceGroup,
).execute();
console.log(`Filtered destinations: ${filtered.count}`);

// ─── 5. Clean up ─────────────────────────────────────────────────────────────
// Delete in reverse dependency order: scenario → artifact → destination

await ScenarioConfigurationManagerApi.deleteScenarioConfigurationByName(
  scenarioName,
  resourceGroup,
).execute();
console.log(`Deleted scenario '${scenarioName}'.`);

await TabularArtifactsApi.deleteTabularArtifact(artifactName, resourceGroup).execute();
console.log(`Deleted artifact '${artifactName}'.`);

await DataDestinationsApi.deleteDataDestinationByName(destName, resourceGroup).execute();
console.log(`Deleted destination '${destName}'.`);
