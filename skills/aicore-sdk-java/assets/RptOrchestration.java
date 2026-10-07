/**
 * SAP RPT (Relational Prompt Tables) — table completion predictions
 *
 * RPT fills in missing values in structured tabular data using an AI model.
 * Mark cells to predict with a placeholder string (e.g. "[PREDICT]").
 *
 * Maven dependency (pom.xml):
 *   <dependency>
 *     <groupId>com.sap.ai.sdk</groupId>
 *     <artifactId>sap-rpt</artifactId>
 *     <version>1.22.0</version>
 *   </dependency>
 *
 * Credentials: set AICORE_SERVICE_KEY env var to your AI Core service key JSON.
 * See: https://sap.github.io/ai-sdk/docs/java/connecting-to-ai-core
 */

import com.sap.ai.sdk.foundationmodels.rpt.RptClient;
import com.sap.ai.sdk.foundationmodels.rpt.RptModel;
import com.sap.ai.sdk.foundationmodels.rpt.generated.model.ColumnType;
import com.sap.ai.sdk.foundationmodels.rpt.generated.model.PredictRequestPayload;
import com.sap.ai.sdk.foundationmodels.rpt.generated.model.PredictResponsePayload;
import com.sap.ai.sdk.foundationmodels.rpt.generated.model.PredictionConfig;
import com.sap.ai.sdk.foundationmodels.rpt.generated.model.PredictionPlaceholder;
import com.sap.ai.sdk.foundationmodels.rpt.generated.model.RowsInnerValue;
import com.sap.ai.sdk.foundationmodels.rpt.generated.model.SchemaFieldConfig;
import com.sap.ai.sdk.foundationmodels.rpt.generated.model.TargetColumnConfig;

import java.math.BigDecimal;
import java.util.List;
import java.util.Map;

public class RptOrchestration {

    public static void main(String[] args) {
        // Credentials are auto-loaded from AICORE_SERVICE_KEY or VCAP_SERVICES
        RptClient client = RptClient.forModel(RptModel.SAP_RPT_1_SMALL);

        // Define the table schema
        var dataSchema = Map.of(
                "PRODUCT",    SchemaFieldConfig.create().dtype(ColumnType.STRING),
                "PRICE",      SchemaFieldConfig.create().dtype(ColumnType.STRING),
                "ORDERDATE",  SchemaFieldConfig.create().dtype(ColumnType.DATE),
                "ID",         SchemaFieldConfig.create().dtype(ColumnType.STRING),
                "COSTCENTER", SchemaFieldConfig.create().dtype(ColumnType.STRING));

        // Which column(s) to predict, and the placeholder string that marks unknown cells
        var targetColumns = List.of(
                TargetColumnConfig.create()
                        .name("COSTCENTER")
                        .predictionPlaceholder(PredictionPlaceholder.create("[PREDICT]"))
                        .taskType(TargetColumnConfig.TaskTypeEnum.CLASSIFICATION));

        // Table rows — use "[PREDICT]" in the target column for cells you want filled in
        List<Map<String, RowsInnerValue>> rows = List.of(
                Map.of(
                        "PRODUCT",    RowsInnerValue.create("Couch"),
                        "PRICE",      RowsInnerValue.create(BigDecimal.valueOf(999.99)),
                        "ORDERDATE",  RowsInnerValue.create("28-11-2025"),
                        "ID",         RowsInnerValue.create("35"),
                        "COSTCENTER", RowsInnerValue.create("[PREDICT]")),  // <- to be predicted
                Map.of(
                        "PRODUCT",    RowsInnerValue.create("Office Chair"),
                        "PRICE",      RowsInnerValue.create(BigDecimal.valueOf(150.80)),
                        "ORDERDATE",  RowsInnerValue.create("02-11-2025"),
                        "ID",         RowsInnerValue.create("44"),
                        "COSTCENTER", RowsInnerValue.create("Office Furniture")));  // <- known

        var request = PredictRequestPayload.create()
                .predictionConfig(PredictionConfig.create().targetColumns(targetColumns))
                .indexColumn("ID")
                .dataSchema(dataSchema)
                .parseDataTypes(true)
                .rows(rows);

        PredictResponsePayload response = client.tableCompletion(request);
        System.out.println("Predictions: " + response);
    }
}
