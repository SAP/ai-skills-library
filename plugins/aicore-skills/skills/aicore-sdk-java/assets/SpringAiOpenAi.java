/**
 * Spring AI integration with SAP AI SDK — OpenAI foundation model client
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

import com.sap.ai.sdk.foundationmodels.openai.OpenAiClient;
import com.sap.ai.sdk.foundationmodels.openai.OpenAiModel;
import com.sap.ai.sdk.foundationmodels.openai.spring.OpenAiChatModel;
import com.sap.ai.sdk.foundationmodels.openai.spring.OpenAiSpringEmbeddingModel;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.embedding.EmbeddingOptions;
import org.springframework.ai.embedding.EmbeddingRequest;
import org.springframework.ai.embedding.EmbeddingResponse;

import java.util.List;

public class SpringAiOpenAi {

    public static void main(String[] args) {
        // Credentials are auto-loaded from AICORE_SERVICE_KEY or VCAP_SERVICES

        // Chat via Spring AI ChatModel interface
        ChatModel chatClient = new OpenAiChatModel(OpenAiClient.forModel(OpenAiModel.GPT_5_MINI));

        var prompt = new Prompt("What is the capital of France?");
        ChatResponse response = chatClient.call(prompt);
        System.out.println(response.getResult().getOutput().getText());

        // Streaming — returns Flux<ChatResponse>
        chatClient.stream(new Prompt("Explain Java generics briefly."))
                .doOnNext(chunk -> System.out.print(chunk.getResult().getOutput().getText()))
                .blockLast();

        // Embeddings via Spring AI EmbeddingModel
        var embeddingClient = new OpenAiSpringEmbeddingModel(
                OpenAiClient.forModel(OpenAiModel.TEXT_EMBEDDING_3_SMALL));

        var embedOptions = EmbeddingOptions.builder().dimensions(128).build();
        EmbeddingResponse embedResponse = embeddingClient.call(
                new EmbeddingRequest(List.of("The quick brown fox."), embedOptions));

        System.out.println("Embedding dimensions: " +
                embedResponse.getResults().get(0).getOutput().length);
    }
}
