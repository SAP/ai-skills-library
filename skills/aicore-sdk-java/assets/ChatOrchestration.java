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
import com.sap.ai.sdk.orchestration.OrchestrationModuleConfig;
import com.sap.ai.sdk.orchestration.OrchestrationPrompt;

public class ChatOrchestration {

    public static void main(String[] args) {
        // Credentials are auto-loaded from AICORE_SERVICE_KEY or VCAP_SERVICES
        var client = new OrchestrationClient();

        var config = new OrchestrationModuleConfig()
                .withLlmConfig(
                        OrchestrationAiModel.GPT_4O_MINI
                                .withParam(OrchestrationAiModel.Parameter.TEMPERATURE, 0.3)
                                .withParam(OrchestrationAiModel.Parameter.MAX_TOKENS, 512));

        var prompt = new OrchestrationPrompt("What is SAP AI Core?");

        var response = client.chatCompletion(prompt, config);
        System.out.println(response.getContent());
    }
}
