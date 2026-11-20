/**
 * Maven dependency (pom.xml):
 *   <dependency>
 *     <groupId>com.sap.ai.sdk</groupId>
 *     <artifactId>orchestration</artifactId>
 *     <version>1.22.0</version>
 *   </dependency>
 *
 * Credentials: set AICORE_SERVICE_KEY env var to your AI Core service key JSON,
 * or run 'aicore configure' (Python CLI) to use ~/.aicore/config.json.
 * See: https://sap.github.io/ai-sdk/docs/java/connecting-to-ai-core
 */

import com.sap.ai.sdk.orchestration.OrchestrationAiModel;
import com.sap.ai.sdk.orchestration.OrchestrationClient;
import com.sap.ai.sdk.orchestration.OrchestrationEmbeddingRequest;
import com.sap.ai.sdk.orchestration.OrchestrationEmbeddingResponse;

import java.util.List;

import static com.sap.ai.sdk.orchestration.OrchestrationEmbeddingModel.TEXT_EMBEDDING_3_SMALL;

public class EmbeddingsOrchestration {

    public static void main(String[] args) {
        // Credentials are auto-loaded from AICORE_SERVICE_KEY or VCAP_SERVICES
        var client = new OrchestrationClient();

        var request = OrchestrationEmbeddingRequest.forModel(TEXT_EMBEDDING_3_SMALL)
                .forInputs(List.of(
                        "SAP AI Core enables enterprise AI deployments.",
                        "The SAP AI SDK simplifies calling GenAI Hub from Java."
                ));

        OrchestrationEmbeddingResponse response = client.embed(request);

        // getEmbeddingVectors() returns List<float[]> — one vector per input
        List<float[]> vectors = response.getEmbeddingVectors();
        vectors.forEach(vector ->
                System.out.println("Dimensions: " + vector.length)); // typically 1536
    }
}
