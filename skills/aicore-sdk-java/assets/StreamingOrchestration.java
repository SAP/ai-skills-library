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

public class StreamingOrchestration {

    public static void main(String[] args) {
        var client = new OrchestrationClient();

        var config = new OrchestrationModuleConfig()
                .withLlmConfig(OrchestrationAiModel.GPT_4O_MINI);

        var prompt = new OrchestrationPrompt("Write a short story about a robot learning to code.");

        // streamChatCompletion returns Stream<String> of text deltas
        try (var stream = client.streamChatCompletion(prompt, config)) {
            stream.forEach(chunk -> {
                System.out.print(chunk);
                System.out.flush();
            });
        }
        System.out.println(); // newline after stream ends
    }
}
