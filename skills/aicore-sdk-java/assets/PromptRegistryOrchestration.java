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
import com.sap.ai.sdk.orchestration.TemplateConfig;

import java.util.Map;

public class PromptRegistryOrchestration {

    public static void main(String[] args) {
        // Credentials are auto-loaded from AICORE_SERVICE_KEY or VCAP_SERVICES
        var client = new OrchestrationClient();

        // Option 1: Reference a stored template by its ID
        var configById = new OrchestrationModuleConfig()
                .withLlmConfig(OrchestrationAiModel.GPT_4O_MINI)
                .withTemplateConfig(
                        TemplateConfig.reference().byId("your-template-id-here"));

        // Option 2: Reference by scenario / name / version
        var configByName = new OrchestrationModuleConfig()
                .withLlmConfig(OrchestrationAiModel.GPT_4O_MINI)
                .withTemplateConfig(
                        TemplateConfig.reference()
                                .byScenario("my-scenario")
                                .name("my-template")
                                .version("0.0.1"));

        // Supply variable values — placeholders defined in the stored template use {{?varName}} syntax
        var prompt = new OrchestrationPrompt(Map.of(
                "language", "Italian",
                "input", "Good morning"));

        var response = client.chatCompletion(prompt, configByName);
        System.out.println(response.getContent());
    }
}
