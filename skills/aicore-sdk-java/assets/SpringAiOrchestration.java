/**
 * Spring AI integration with SAP AI SDK — Orchestration service
 *
 * Maven dependencies (pom.xml):
 *   <dependency>
 *     <groupId>com.sap.ai.sdk</groupId>
 *     <artifactId>orchestration</artifactId>
 *     <version>1.22.0</version>
 *   </dependency>
 *   <!-- Spring AI support is included in the orchestration module -->
 *
 * Credentials: set AICORE_SERVICE_KEY env var to your AI Core service key JSON.
 * See: https://sap.github.io/ai-sdk/docs/java/connecting-to-ai-core
 */

import com.sap.ai.sdk.orchestration.OrchestrationAiModel;
import com.sap.ai.sdk.orchestration.OrchestrationModuleConfig;
import com.sap.ai.sdk.orchestration.spring.OrchestrationChatModel;
import com.sap.ai.sdk.orchestration.spring.OrchestrationChatOptions;
import com.sap.ai.sdk.orchestration.spring.OrchestrationSpringEmbeddingModel;
import com.sap.ai.sdk.orchestration.OrchestrationEmbeddingModel;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.embedding.EmbeddingOptions;

public class SpringAiOrchestration {

    public static void main(String[] args) {
        // Credentials are auto-loaded from AICORE_SERVICE_KEY or VCAP_SERVICES
        ChatModel client = new OrchestrationChatModel();

        var config = new OrchestrationModuleConfig()
                .withLlmConfig(OrchestrationAiModel.GPT_4O_MINI);
        var options = new OrchestrationChatOptions(config);

        // Simple chat completion
        var prompt = new Prompt("What is the capital of France?", options);
        ChatResponse response = client.call(prompt);
        System.out.println(response.getResult().getOutput().getText());

        // Streaming — returns Flux<ChatResponse>
        var streamPrompt = new Prompt("Give me the first 10 Fibonacci numbers.", options);
        client.stream(streamPrompt)
                .doOnNext(chunk -> System.out.print(chunk.getResult().getOutput().getText()))
                .blockLast();

        // Embeddings via Spring AI EmbeddingModel
        var embedOptions = EmbeddingOptions.builder()
                .model(OrchestrationEmbeddingModel.TEXT_EMBEDDING_3_SMALL.model())
                .build();
        float[] vector = new OrchestrationSpringEmbeddingModel(embedOptions)
                .embed("SAP AI Core enables enterprise AI deployments.");
        System.out.println("Embedding dimensions: " + vector.length);
    }
}
