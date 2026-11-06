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

import com.sap.ai.sdk.orchestration.DpiMasking;
import com.sap.ai.sdk.orchestration.Message;
import com.sap.ai.sdk.orchestration.OrchestrationAiModel;
import com.sap.ai.sdk.orchestration.OrchestrationClient;
import com.sap.ai.sdk.orchestration.OrchestrationModuleConfig;
import com.sap.ai.sdk.orchestration.OrchestrationPrompt;
import com.sap.ai.sdk.orchestration.model.DPIEntities;

public class MaskingOrchestration {

    public static void main(String[] args) {
        // Credentials are auto-loaded from AICORE_SERVICE_KEY or VCAP_SERVICES
        var client = new OrchestrationClient();

        var config = new OrchestrationModuleConfig()
                .withLlmConfig(OrchestrationAiModel.GPT_4O_MINI);

        // --- Example 1: DPI anonymization by entity type ---
        // DPIEntities.PERSON replaces detected person names with anonymized tokens
        // before the prompt is sent to the LLM.
        var systemMessage = Message.system(
                "Please evaluate the following user feedback and judge if the sentiment is positive or negative.");
        var userMessage = Message.user(
                "I think the SDK is good, but could use some further enhancements. "
                        + "My architect Alice and manager Bob pointed out several areas for improvement.");

        var entityMaskingConfig = DpiMasking.anonymization().withEntities(DPIEntities.PERSON, DPIEntities.EMAIL);
        var configWithEntityMasking = config.withMaskingConfig(entityMaskingConfig);

        var entityPrompt = new OrchestrationPrompt(systemMessage, userMessage);
        var entityResponse = client.chatCompletion(entityPrompt, configWithEntityMasking);
        System.out.println("Entity masking — response: " + entityResponse.getContent());

        // --- Example 2: DPI anonymization by custom regex ---
        // Replaces any token matching the regex pattern with the given replacement string
        // before the prompt is sent to the LLM.
        var regex = "patient_id_[0-9]+";
        var replacement = "REDACTED_ID";
        var regexMaskingConfig = DpiMasking.anonymization().withRegex(regex, replacement);
        var configWithRegexMasking = config.withMaskingConfig(regexMaskingConfig);

        var regexPrompt = new OrchestrationPrompt(
                "Summarize the treatment notes for patient_id_482910 and patient_id_319045.");
        var regexResponse = client.chatCompletion(regexPrompt, configWithRegexMasking);
        System.out.println("Regex masking — response: " + regexResponse.getContent());
    }
}
