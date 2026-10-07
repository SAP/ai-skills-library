/**
 * LLM Batch processing via SAP AI SDK
 *
 * Maven dependencies (pom.xml):
 *   <dependency>
 *     <groupId>com.sap.ai.sdk</groupId>
 *     <artifactId>batch</artifactId>
 *     <version>1.22.0</version>
 *   </dependency>
 *   <dependency>
 *     <groupId>com.sap.ai.sdk</groupId>
 *     <artifactId>openai</artifactId>
 *     <version>1.22.0</version>
 *   </dependency>
 *
 * Prerequisites:
 *   - An S3 Object Store secret configured in AI Launchpad > AI Core Administration
 *   - Input file uploaded to the S3 bucket (JSONL format, one request per line)
 *
 * Credentials: set AICORE_SERVICE_KEY env var to your AI Core service key JSON.
 * See: https://sap.github.io/ai-sdk/docs/java/connecting-to-ai-core
 */

import com.sap.ai.sdk.batch.generated.client.BatchesApi;
import com.sap.ai.sdk.batch.generated.model.BatchCreateRequest;
import com.sap.ai.sdk.batch.generated.model.BatchCreateRequest.TypeEnum;
import com.sap.ai.sdk.batch.generated.model.BatchCreateRequestInput;
import com.sap.ai.sdk.batch.generated.model.BatchCreateRequestOutput;
import com.sap.ai.sdk.batch.generated.model.BatchCreateRequestSpec;
import com.sap.ai.sdk.batch.generated.model.BatchCreateResponse;
import com.sap.ai.sdk.batch.generated.model.BatchDetailResponse;
import com.sap.ai.sdk.batch.generated.model.BatchListResponse;
import com.sap.ai.sdk.core.client.FileApi;
import com.sap.ai.sdk.foundationmodels.openai.OpenAiBatchInput;
import com.sap.ai.sdk.foundationmodels.openai.OpenAiChatCompletionRequest;

import java.util.Map;

public class BatchOrchestration {

    static final BatchesApi CLIENT = new BatchesApi();
    // Content-Type: application/jsonl is required — omitting it causes the upload to fail
    static final FileApi FILE_CLIENT =
            new FileApi().withDefaultHeaders(Map.of("Content-Type", "application/jsonl"));

    static final String RESOURCE_GROUP = "default";
    static final String S3_INPUT_FILE = "s3secret/input-batch.jsonl";
    static final String S3_OUTPUT_DIR = "s3secret/batch-output/";

    public static void main(String[] args) {
        // Step 1: Upload input JSONL to S3
        uploadInput();

        // Step 2: Create a batch job
        BatchCreateResponse created = CLIENT.createBatch(
                RESOURCE_GROUP,
                BatchCreateRequest.create()
                        .type(TypeEnum.LLM_NATIVE)
                        .input(BatchCreateRequestInput.create().uri("ai://" + S3_INPUT_FILE))
                        .output(BatchCreateRequestOutput.create().uri("ai://" + S3_OUTPUT_DIR))
                        .spec(BatchCreateRequestSpec.create()
                                .provider("azure-openai")
                                .model("gpt-4.1"))); // BatchCreateRequestSpec requires a raw model string — OrchestrationAiModel constants only work with OrchestrationClient, not the Batch API

        System.out.println("Batch created: " + created.getId());

        // Step 3: Poll for status (getId() returns a UUID)
        BatchDetailResponse detail = CLIENT.getBatchById(RESOURCE_GROUP, created.getId());
        System.out.println("Status: " + detail.getStatus());

        // Step 4: List all batches
        BatchListResponse list = CLIENT.listBatches(RESOURCE_GROUP);
        System.out.println("Total batches: " + list.getCount());
    }

    static void uploadInput() {
        // Build JSONL batch input — each item is one chat completion request
        var batchInput = new OpenAiBatchInput(
                new OpenAiChatCompletionRequest("What is machine learning?"),
                new OpenAiChatCompletionRequest("Explain neural networks in simple terms"));

        FILE_CLIENT.upload(S3_INPUT_FILE, RESOURCE_GROUP, true, batchInput);
        System.out.println("Input uploaded to S3.");
    }
}
