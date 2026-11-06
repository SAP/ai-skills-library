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

import com.sap.ai.sdk.orchestration.Grounding;
import com.sap.ai.sdk.orchestration.OrchestrationAiModel;
import com.sap.ai.sdk.orchestration.OrchestrationClient;
import com.sap.ai.sdk.orchestration.OrchestrationModuleConfig;
import com.sap.ai.sdk.orchestration.model.DataRepositoryType;
import com.sap.ai.sdk.orchestration.model.DocumentGroundingFilter;
import com.sap.ai.sdk.orchestration.model.GroundingFilterSearchConfiguration;

public class GroundingOrchestration {

    public static void main(String[] args) {
        // Credentials are auto-loaded from AICORE_SERVICE_KEY or VCAP_SERVICES
        var client = new OrchestrationClient();

        var config = new OrchestrationModuleConfig()
                .withLlmConfig(OrchestrationAiModel.GPT_4O_MINI);

        // Configure the grounding filter — points to your vector store collection
        var groundingFilter = DocumentGroundingFilter.create()
                .dataRepositoryType(DataRepositoryType.VECTOR)
                .searchConfig(GroundingFilterSearchConfiguration.create().maxChunkCount(3));

        var groundingConfig = Grounding.create()
                .filters(groundingFilter)
                .metadataParams("*");

        var configWithGrounding = config.withGrounding(groundingConfig);

        // createGroundingPrompt wraps the user question with retrieved context
        var userQuestion = "What is the return policy?";
        var prompt = groundingConfig.createGroundingPrompt(userQuestion);

        var response = client.chatCompletion(prompt, configWithGrounding);
        System.out.println(response.getContent());
    }
}
