/**
 * Native OpenAI Responses API via SAP AI SDK (AiCoreOpenAiClient)
 *
 * Use this when you need the OpenAI Responses API features:
 * persistent responses, background processing, multi-turn via response IDs,
 * structured output, tool calling, or prompt caching.
 *
 * For standard chat completions, prefer OrchestrationClient instead.
 *
 * Maven dependency (pom.xml):
 *   <dependency>
 *     <groupId>com.sap.ai.sdk</groupId>
 *     <artifactId>openai</artifactId>
 *     <version>1.22.0</version>
 *   </dependency>
 *
 * Credentials: set AICORE_SERVICE_KEY env var to your AI Core service key JSON.
 * See: https://sap.github.io/ai-sdk/docs/java/connecting-to-ai-core
 */

import com.openai.models.responses.Response;
import com.openai.models.responses.ResponseCreateParams;
import com.openai.models.responses.ResponseOutputItem;
import com.openai.models.responses.ResponseOutputMessage;
import com.openai.models.responses.ResponseRetrieveParams;
import com.openai.models.responses.ResponseStatus;
import com.openai.services.blocking.ResponseService;
import com.sap.ai.sdk.foundationmodels.openai.AiCoreOpenAiClient;
import com.sap.ai.sdk.foundationmodels.openai.OpenAiModel;

import java.util.stream.Collectors;

public class OpenAiNative {

    public static void main(String[] args) throws InterruptedException {
        // Credentials are auto-loaded from AICORE_SERVICE_KEY or VCAP_SERVICES
        // Second argument is the resource group (use "default" if unsure)
        ResponseService responseClient =
                AiCoreOpenAiClient.forModel(OpenAiModel.GPT_5, "default").responses();

        // Simple non-persistent response
        var params = ResponseCreateParams.builder()
                .input("What is SAP AI Core?")
                .store(false)
                .build();
        Response response = responseClient.create(params);
        System.out.println(extractText(response));

        // Persistent response — can be retrieved or continued later
        Response persistent = responseClient.create(
                ResponseCreateParams.builder()
                        .input("Explain transformer architecture.")
                        .store(true)
                        .build());
        String responseId = persistent.id();
        System.out.println("Stored response ID: " + responseId);

        // Multi-turn: continue from previous response by ID (no need to resend history)
        Response followUp = responseClient.create(
                ResponseCreateParams.builder()
                        .input("How does attention work in that context?")
                        .previousResponseId(responseId)
                        .store(true)
                        .build());
        System.out.println(extractText(followUp));

        // Background response — fires async, poll until done
        Response background = responseClient.create(
                ResponseCreateParams.builder()
                        .input("Summarize the history of machine learning.")
                        .store(true)
                        .background(true)
                        .build());
        while (background.status().filter(ResponseStatus.QUEUED::equals).isPresent()
                || background.status().filter(ResponseStatus.IN_PROGRESS::equals).isPresent()) {
            Thread.sleep(2000);
            background = responseClient.retrieve(
                    ResponseRetrieveParams.builder().responseId(background.id()).build());
        }
        System.out.println("Background result: " + extractText(background));
    }

    // The OpenAI Response holds a list of output items — collect the text parts.
    private static String extractText(final Response response) {
        return response.output().stream()
                .filter(ResponseOutputItem::isMessage)
                .map(ResponseOutputItem::asMessage)
                .flatMap(message -> message.content().stream())
                .filter(ResponseOutputMessage.Content::isOutputText)
                .map(text -> text.asOutputText().text())
                .collect(Collectors.joining());
    }
}
