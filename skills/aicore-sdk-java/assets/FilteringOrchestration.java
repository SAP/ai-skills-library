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

import com.sap.ai.sdk.orchestration.AzureContentFilter;
import com.sap.ai.sdk.orchestration.AzureFilterThreshold;
import com.sap.ai.sdk.orchestration.LlamaGuardFilter;
import com.sap.ai.sdk.orchestration.OrchestrationAiModel;
import com.sap.ai.sdk.orchestration.OrchestrationClient;
import com.sap.ai.sdk.orchestration.OrchestrationClientException;
import com.sap.ai.sdk.orchestration.OrchestrationFilterException;
import com.sap.ai.sdk.orchestration.OrchestrationModuleConfig;
import com.sap.ai.sdk.orchestration.OrchestrationPrompt;
import com.sap.ai.sdk.orchestration.model.LlamaGuard38b;

public class FilteringOrchestration {

    public static void main(String[] args) {
        // Credentials are auto-loaded from AICORE_SERVICE_KEY or VCAP_SERVICES
        var client = new OrchestrationClient();

        var config = new OrchestrationModuleConfig()
                .withLlmConfig(OrchestrationAiModel.GPT_4O_MINI);

        // --- Example 1: Azure Content Filter on input ---
        // ALLOW_SAFE blocks content rated low, medium, or high in each category.
        // promptShield(true) additionally detects prompt-injection attacks.
        var azureFilterConfig =
                new AzureContentFilter()
                        .hate(AzureFilterThreshold.ALLOW_SAFE)
                        .selfHarm(AzureFilterThreshold.ALLOW_SAFE)
                        .sexual(AzureFilterThreshold.ALLOW_SAFE)
                        .violence(AzureFilterThreshold.ALLOW_SAFE)
                        .promptShield(true);

        var configWithAzureFilter = config.withInputFiltering(azureFilterConfig);

        var prompt = new OrchestrationPrompt("Explain the history of nuclear energy.");

        try {
            var response = client.chatCompletion(prompt, configWithAzureFilter);
            System.out.println("Azure filter — response: " + response.getContent());
        } catch (OrchestrationFilterException.Input e) {
            System.out.println("Input was blocked by Azure content filter: " + e.getMessage());
        } catch (OrchestrationFilterException.Output e) {
            System.out.println("Output was blocked by Azure content filter: " + e.getMessage());
        } catch (OrchestrationClientException e) {
            System.out.println("API error: " + e.getMessage());
        }

        // --- Example 2: LlamaGuard input filter ---
        // Set each category to true to enable filtering for that harm type.
        var llamaGuardConfig =
                LlamaGuard38b.create()
                        .violentCrimes(true)
                        .nonViolentCrimes(true)
                        .sexCrimes(true)
                        .childExploitation(true)
                        .hate(true)
                        .selfHarm(true)
                        .indiscriminateWeapons(true);

        var llamaGuardFilter = new LlamaGuardFilter().config(llamaGuardConfig);
        var configWithLlamaGuard = config.withInputFiltering(llamaGuardFilter);

        var llamaPrompt = new OrchestrationPrompt("What safety measures are used in chemical labs?");

        try {
            var llamaResponse = client.chatCompletion(llamaPrompt, configWithLlamaGuard);
            System.out.println("LlamaGuard filter — response: " + llamaResponse.getContent());
        } catch (OrchestrationFilterException.Input e) {
            System.out.println("Input was blocked by LlamaGuard filter: " + e.getMessage());
        } catch (OrchestrationFilterException.Output e) {
            System.out.println("Output was blocked by LlamaGuard filter: " + e.getMessage());
        } catch (OrchestrationClientException e) {
            System.out.println("API error: " + e.getMessage());
        }

        // --- Example 3: Combined input + output filtering (Azure + LlamaGuard) ---
        // Apply Azure filter on both input and output; add LlamaGuard on output as well.
        var configWithCombined = config
                .withInputFiltering(azureFilterConfig)
                .withOutputFiltering(azureFilterConfig, llamaGuardFilter);

        var combinedPrompt = new OrchestrationPrompt("Describe the risks of extreme sports.");

        try {
            var combinedResponse = client.chatCompletion(combinedPrompt, configWithCombined);
            System.out.println("Combined filter — response: " + combinedResponse.getContent());
        } catch (OrchestrationFilterException.Input e) {
            System.out.println("Input was blocked: " + e.getMessage());
        } catch (OrchestrationFilterException.Output e) {
            System.out.println("Output was blocked: " + e.getMessage());
        } catch (OrchestrationClientException e) {
            System.out.println("API error: " + e.getMessage());
        }
    }
}
