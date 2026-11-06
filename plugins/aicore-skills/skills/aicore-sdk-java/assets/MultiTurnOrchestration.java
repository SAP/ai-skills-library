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

import com.sap.ai.sdk.orchestration.Message;
import com.sap.ai.sdk.orchestration.OrchestrationAiModel;
import com.sap.ai.sdk.orchestration.OrchestrationClient;
import com.sap.ai.sdk.orchestration.OrchestrationModuleConfig;
import com.sap.ai.sdk.orchestration.OrchestrationPrompt;

public class MultiTurnOrchestration {

    public static void main(String[] args) {
        var client = new OrchestrationClient();

        var config = new OrchestrationModuleConfig()
                .withLlmConfig(OrchestrationAiModel.GPT_4O_MINI);

        // Turn 1
        var firstPrompt = new OrchestrationPrompt(
                Message.system("You are a helpful assistant."),
                Message.user("What is SAP AI Core?"));

        var firstResponse = client.chatCompletion(firstPrompt, config);
        System.out.println("Assistant: " + firstResponse.getContent());

        // Turn 2 — pass message history to maintain context
        var followUpPrompt = new OrchestrationPrompt("Can you give me a code example?")
                .messageHistory(firstResponse.getAllMessages());

        var followUpResponse = client.chatCompletion(followUpPrompt, config);
        System.out.println("Assistant: " + followUpResponse.getContent());
    }
}
