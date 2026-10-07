# Java SDK Reference: SAP AI SDK for Java

> **Version note** — This reference targets **SAP AI SDK for Java v1.x** (`com.sap.ai.sdk:orchestration:1.22.0`).
> Snippets are drawn from the `sample-code/` directory of the GitHub repo.
> When the Context7 MCP tool is available, prefer it over this file — it always reflects the latest API shapes.
> If a class or method listed here does not appear in Context7 results, trust Context7.

GitHub: https://github.com/SAP/ai-sdk-java
Online Documentation: https://sap.github.io/ai-sdk/docs/java/

## Packages

| Artifact                          | Purpose                                                    |
| --------------------------------- | ---------------------------------------------------------- |
| `com.sap.ai.sdk:orchestration`    | Orchestration service client (recommended entry point)     |
| `com.sap.ai.sdk:core`             | AI Core connectivity and destination resolution — required for custom resource groups (`AiCoreService`) |
| `com.sap.ai.sdk:openai`           | Direct OpenAI client (chat completions + Responses API via `AiCoreOpenAiClient`) |
| `com.sap.ai.sdk:batch`            | LLM batch processing (`BatchesApi`)                        |
| `com.sap.ai.sdk:sap-rpt`          | SAP RPT model — relational prompt table completion (`RptClient`) |

## Installation

```xml
<!-- Maven — orchestration only (default resource group) -->
<dependency>
    <groupId>com.sap.ai.sdk</groupId>
    <artifactId>orchestration</artifactId>
    <version>1.22.0</version>
</dependency>

<!-- Add core if you need AiCoreService (custom resource groups, custom destinations) -->
<dependency>
    <groupId>com.sap.ai.sdk</groupId>
    <artifactId>core</artifactId>
    <version>1.22.0</version>
</dependency>
```

```groovy
// Gradle — orchestration only (default resource group)
implementation 'com.sap.ai.sdk:orchestration:1.22.0'

// Add core if you need AiCoreService (custom resource groups, custom destinations)
implementation 'com.sap.ai.sdk:core:1.22.0'
```

Check [Maven Central](https://central.sonatype.com/artifact/com.sap.ai.sdk/orchestration) for the latest version.

## Configuration

Credentials are read automatically from:
1. `AICORE_SERVICE_KEY` environment variable (JSON string) — simplest for local dev
2. `VCAP_SERVICES` — Cloud Foundry / BTP
3. SAP Cloud SDK destination service

```bash
# Local dev — set AICORE_SERVICE_KEY to your service key JSON
export AICORE_SERVICE_KEY='{"clientid":"...","clientsecret":"...","url":"...","serviceurls":{"AI_API_URL":"..."}}'
```

For a custom resource group — from `sample-code/spring-app/.../OrchestrationService.java`:
```java
// Option 1: AiCoreService (requires com.sap.ai.sdk:core dependency)
var destination =
    new AiCoreService().getInferenceDestination(resourceGroup).forScenario("orchestration");
var clientWithResourceGroup = new OrchestrationClient(destination);

// Option 2: withResourceGroup shorthand
var clientWithResourceGroup = client.withResourceGroup("my-resource-group", "orchestration");
```

## OrchestrationClient (recommended)

```java
import com.sap.ai.sdk.orchestration.*;

var client = new OrchestrationClient();

var config = new OrchestrationModuleConfig()
    .withLlmConfig(OrchestrationAiModel.GPT_4O_MINI);

var response = client.chatCompletion(
    new OrchestrationPrompt("What is SAP AI Core?"), config);

System.out.println(response.getContent());
```

## Available Models (`OrchestrationAiModel`)

| Constant                           | Model                       |
| ---------------------------------- | --------------------------- |
| `GPT_4O`                           | gpt-4o (Azure OpenAI)       |
| `GPT_4O_MINI`                      | gpt-4o-mini (Azure OpenAI)  |
| `GPT_5_MINI`                       | gpt-5-mini (Azure OpenAI)   |
| `GPT_41_NANO`                      | gpt-4.1-nano (Azure OpenAI) |
| `CLAUDE_4_5_SONNET`                | Claude Sonnet (Anthropic)   |
| `CLAUDE_4_5_HAIKU`                 | Claude Haiku (Anthropic)    |
| `GEMINI_2_5_FLASH`                 | Gemini 2.5 Flash (Google)   |
| `MISTRAL_MEDIUM`, `MISTRAL_SMALL`  | Mistral AI                  |
| `SONAR`                            | Perplexity Sonar (with citations) |

Use `genai-hub-foundation-models` skill to list all models available in your instance.

## Model Parameters

```java
var config = new OrchestrationModuleConfig()
    .withLlmConfig(
        OrchestrationAiModel.GPT_4O_MINI
            .withParam(OrchestrationAiModel.Parameter.TEMPERATURE, 0.7)
            .withParam(OrchestrationAiModel.Parameter.MAX_TOKENS, 1000));
```

## Messages

```java
// Simple string prompt
new OrchestrationPrompt("What is Java?");

// Multi-message with system prompt
new OrchestrationPrompt(
    Message.system("You are a helpful assistant."),
    Message.user("What is Java?"));

// With image (from sample-code/spring-app/.../OrchestrationService.java)
Message.user("What is in this image?")
    .withImage("https://example.com/image.jpg", ImageItem.DetailLevel.LOW);

// With multiple text parts in one user message
// public OrchestrationChatResponse multiStringInput(List<String> questions)
Message.user(questions.get(0)).withText(questions.get(1)).withText(questions.get(2));

// With file URL (e.g. PDF)
// public OrchestrationChatResponse fileInput(String fileUrl, String filename)
Message.user("What is the title of the topic discussed here?")
    .withFileUrl(fileUrl, filename);

// With local file
Message.user("What is the title of the topic discussed here?")
    .withFile(filePath);
```

## Fallback Configs (Multiple LLM Modules)

```java
// From sample-code/spring-app/.../OrchestrationService.java:
// public OrchestrationChatResponse completionWithFallback(String famousPhrase) {

var workingConfig = new OrchestrationModuleConfig().withLlmConfig(OrchestrationAiModel.GPT_4O_MINI);
var brokenConfig =
    new OrchestrationModuleConfig()
        .withLlmConfig(new OrchestrationAiModel("broken_name", Map.of(), "latest"));
// Pass multiple configs — first to succeed wins
return client.chatCompletion(prompt, brokenConfig, workingConfig);
```

## Streaming

```java
// Convenience method — returns Stream<String> of text deltas
try (var stream = client.streamChatCompletion(prompt, config)) {
    stream.forEach(chunk -> {
        System.out.print(chunk);
        System.out.flush();
    });
}

// Low-level delta streaming (access metadata per chunk)
var request = OrchestrationClient.toCompletionPostRequest(prompt, config);
try (var deltas = client.streamChatCompletionDeltas(request)) {
    deltas.forEach(delta -> System.out.print(delta.getDeltaContent()));
}
```

## Spring Boot Streaming (ResponseBodyEmitter)

The correct Spring Boot pattern uses `ResponseBodyEmitter` with `ThreadContextExecutors` — **not** `Flux.fromStream` (which closes the stream before it can be consumed).

From `sample-code/spring-app/.../OrchestrationController.java`:
```java
// Service method returns Stream<String>
// public Stream<String> streamChatCompletion(String topic) {
//   return client.streamChatCompletion(new OrchestrationPrompt("..."), config);
// }

@GetMapping("/streamChatCompletion")
ResponseEntity<ResponseBodyEmitter> streamChatCompletion() {
  final var stream = service.streamChatCompletion("developing a software project");
  final var emitter = new ResponseBodyEmitter();
  final Runnable consumeStream =
      () -> {
        try (stream) {
          stream.forEach(deltaMessage -> send(emitter, deltaMessage));
        } finally {
          emitter.complete();
        }
      };

  ThreadContextExecutors.getExecutor().execute(consumeStream);

  // TEXT_EVENT_STREAM allows the browser to display the content as it is streamed
  return ResponseEntity.ok().contentType(MediaType.TEXT_EVENT_STREAM).body(emitter);
}
```

Helper `send()` method (reusable across controllers) from `OpenAiController.java`:
```java
public static void send(@Nonnull final ResponseBodyEmitter emitter, @Nonnull final String chunk) {
  try {
    emitter.send(chunk);
  } catch (final IOException e) {
    log.error("Failed to send chunk: {}", e.getMessage(), e);
    emitter.completeWithError(e);
  }
}
```

## Multi-Turn Conversations

```java
var firstResponse = client.chatCompletion(firstPrompt, config);

// Pass getAllMessages() as history for the next turn
var followUp = new OrchestrationPrompt("Tell me more")
    .messageHistory(firstResponse.getAllMessages());

var followUpResponse = client.chatCompletion(followUp, config);
```

## Response Object

```java
OrchestrationChatResponse response = client.chatCompletion(prompt, config);

response.getContent();          // String — the text reply
response.getTokenUsage();       // TokenUsage — prompt/completion/total tokens
response.getAllMessages();       // List<Message> — full conversation history
response.getReasoningText();    // String — reasoning content (Claude extended thinking)
response.getOriginalResponse(); // CompletionPostResponse — raw API response
```

## Exception Handling

```java
try {
    var response = client.chatCompletion(prompt, config);
} catch (OrchestrationFilterException.Input e) {
    // Input was blocked by content filter
} catch (OrchestrationFilterException.Output e) {
    // Output was blocked by content filter
} catch (OrchestrationClientException e) {
    // General API or connectivity error
}
```

## Reasoning (Extended Thinking)

Reasoning is enabled by calling `.withReasoningEffort(ReasoningEffort.X)` on any reasoning-capable model constant.

**Supported models:**
- `CLAUDE_4_5_SONNET`, `CLAUDE_4_5_HAIKU`, `CLAUDE_4_6_SONNET`, `CLAUDE_4_6_OPUS`, `CLAUDE_4_7_OPUS` (Anthropic)
- `COHERE_COMMAND_A_REASONING` (Cohere)

**Reasoning effort levels (`ReasoningEffort` enum):**

| Constant | Effect |
|---|---|
| `MINIMAL` | Fastest, least thinking |
| `LOW` | Light reasoning |
| `MEDIUM` | Balanced |
| `HIGH` | Thorough reasoning |
| `NONE` | Disable reasoning on models that support toggling it |

```java
import com.sap.ai.sdk.orchestration.ReasoningEffort;

var config = new OrchestrationModuleConfig()
    .withLlmConfig(
        OrchestrationAiModel.CLAUDE_4_5_SONNET
            .withReasoningEffort(ReasoningEffort.HIGH));

var response = client.chatCompletion(new OrchestrationPrompt("Explain recursion"), config);

System.out.println("Thinking: " + response.getReasoningText()); // model's internal reasoning
System.out.println("Answer:   " + response.getContent());       // final answer
```

**Multi-turn reasoning** — from `sample-code/spring-app/.../OrchestrationService.java`:

```java
public ReasoningOutput multiTurnReasoning(
    @Nonnull final String firstQuestion, @Nonnull final String followUp) {
  var reasoningConfig =
      config.withLlmConfig(CLAUDE_4_5_SONNET.withReasoningEffort(ReasoningEffort.MEDIUM));

  // Turn 1
  var firstPrompt = new OrchestrationPrompt(firstQuestion);
  var firstResponse = client.chatCompletion(firstPrompt, reasoningConfig);

  // Turn 2 feeds the whole history back. getAllMessages() already carries the reasoning content
  // on the final assistant message.
  var followUpPrompt =
      new OrchestrationPrompt(followUp).messageHistory(firstResponse.getAllMessages());
  var followUpResponse = client.chatCompletion(followUpPrompt, reasoningConfig);

  return new ReasoningOutput(followUpResponse.getContent(), followUpResponse.getReasoningText());
}
```

**Streaming reasoning deltas** — from `sample-code/spring-app/.../OrchestrationService.java`:

```java
// ReasoningOutput record
public record ReasoningOutput(@Nonnull String answer, @Nonnull String reasoning) {}

public Stream<ReasoningOutput> streamReasoning(@Nonnull final String topic) {
  var reasoningConfig =
      config.withLlmConfig(CLAUDE_4_5_SONNET.withReasoningEffort(ReasoningEffort.MEDIUM));
  var prompt = new OrchestrationPrompt("Think carefully and explain step by step: " + topic);
  var request = OrchestrationClient.toCompletionPostRequest(prompt, reasoningConfig);
  return client
      .streamChatCompletionDeltas(request)
      .map(delta -> new ReasoningOutput(delta.getDeltaContent(), delta.getDeltaReasoningText()));
}
```

Spring Boot controller for streaming reasoning from `OrchestrationController.java`:
```java
@GetMapping("/streamReasoning")
ResponseEntity<ResponseBodyEmitter> streamReasoning(
    @RequestParam(value = "topic", defaultValue = "Why is the sky blue?") final String topic) {
  final var emitter = new ResponseBodyEmitter();
  final Runnable consumeStream =
      () -> {
        final var lastLabel = new String[] {""};
        try (var stream = service.streamReasoning(topic)) {
          stream.forEach(chunk -> {
            if (!chunk.answer().isEmpty()) {
              if (!"answer".equals(lastLabel[0])) {
                send(emitter, "\n-----ANSWER-----\n");
                lastLabel[0] = "answer";
              }
              send(emitter, chunk.answer());
            }
            if (!chunk.reasoning().isEmpty()) {
              if (!"reasoning".equals(lastLabel[0])) {
                send(emitter, "\n----REASONING----\n");
                lastLabel[0] = "reasoning";
              }
              send(emitter, chunk.reasoning());
            }
          });
        } finally {
          emitter.complete();
        }
      };
  ThreadContextExecutors.getExecutor().execute(consumeStream);
  return ResponseEntity.ok().contentType(MediaType.TEXT_EVENT_STREAM).body(emitter);
}
```

## Prompt Templates (TemplateConfig)

Use `TemplateConfig` to define message templates with `{{?placeholder}}` variables.

```java
import com.sap.ai.sdk.orchestration.TemplateConfig;
import com.sap.ai.sdk.orchestration.Message;

// From sample-code/spring-app/.../OrchestrationService.java:
// public OrchestrationChatResponse template(String language) {

var template = Message.user("Reply with 'Orchestration Service is working!' in {{?language}}");
var templatingConfig = TemplateConfig.create().withMessages(template);
var configWithTemplate = config.withTemplateConfig(templatingConfig);

var inputParams = Map.of("language", language);
var prompt = new OrchestrationPrompt(inputParams);

return client.chatCompletion(prompt, configWithTemplate);
```

### JSON Schema Response (Structured Output)

```java
import com.sap.ai.sdk.orchestration.ResponseJsonSchema;
import com.sap.ai.sdk.orchestration.TemplateConfig;

// From sample-code/spring-app/.../OrchestrationService.java:
// public record Translation(String translation, String language) {}
// public OrchestrationChatResponse responseFormatJsonSchema(String word, Class<?> targetType) {

var schema =
    ResponseJsonSchema.fromType(targetType)
        .withDescription("Output schema for language translation.")
        .withStrict(true);
var configWithResponseSchema =
    new OrchestrationModuleConfig()
        .withLlmConfig(OrchestrationAiModel.GPT_4O_MINI)
        .withTemplateConfig(TemplateConfig.create().withJsonSchemaResponse(schema));

var prompt =
    new OrchestrationPrompt(
        Message.user("What's 'Hello' in German?"),
        Message.system("You are a language translator."));

var response = client.chatCompletion(prompt, configWithResponseSchema);

// Deserialize the structured response into your target type
Translation result = response.asEntity(Translation.class);
```

### JSON Object Response Format

```java
// From sample-code/spring-app/.../OrchestrationService.java:
// public OrchestrationChatResponse responseFormatJsonObject(String word) {

var template = Message.user("What is '%s' in German?".formatted(word));
var templatingConfig = TemplateConfig.create().withMessages(template).withJsonResponse();
var configWithTemplate = config.withTemplateConfig(templatingConfig);
```

### Template from Prompt Registry (by ID)

```java
import com.sap.ai.sdk.orchestration.TemplateConfig;

// From sample-code/spring-app/.../OrchestrationService.java:
// public OrchestrationChatResponse templateFromPromptRegistryByIdTenant(String topic) {

var template = TemplateConfig.reference().byId("21cb1358-0bf1-4f43-870b-00f14d0f9f16");
var configWithTemplate = new OrchestrationModuleConfig()
    .withLlmConfig(OrchestrationAiModel.GPT_4O_MINI)
    .withTemplateConfig(template);

var inputParams = Map.of("language", "Italian", "input", topic);
var prompt = new OrchestrationPrompt(inputParams);
return client.chatCompletion(prompt, configWithTemplate);
```

### Template from Prompt Registry (by scenario/name/version)

```java
// From sample-code/spring-app/.../OrchestrationService.java:
// public OrchestrationChatResponse templateFromPromptRegistryByScenarioTenant(String topic) {

var template = TemplateConfig.reference().byScenario("test").name("test").version("0.0.1");
var configWithTemplate = config.withTemplateConfig(template);

var inputParams = Map.of("language", "Italian", "input", topic);
var prompt = new OrchestrationPrompt(inputParams);
return client.chatCompletion(prompt, configWithTemplate);
```

---

## Grounding (RAG with Vector Store)

```java
import com.sap.ai.sdk.orchestration.Grounding;
import com.sap.ai.sdk.orchestration.model.DataRepositoryType;
import com.sap.ai.sdk.orchestration.model.DocumentGroundingFilter;
import com.sap.ai.sdk.orchestration.model.GroundingFilterSearchConfiguration;
import com.sap.ai.sdk.orchestration.model.SearchDocumentKeyValueListPair;
import com.sap.ai.sdk.orchestration.model.SearchSelectOptionEnum;

// From sample-code/spring-app/.../OrchestrationService.java:
// public OrchestrationChatResponse grounding(String userMessage, boolean maskGroundingInput) {

// optional filter for collections
var documentMetadata =
    SearchDocumentKeyValueListPair.create()
        .key("document metadata")
        .value("2")
        .addSelectModeItem(SearchSelectOptionEnum.IGNORE_IF_KEY_ABSENT);
// optional filter for document chunks
var databaseFilter =
    DocumentGroundingFilter.create()
        .dataRepositoryType(DataRepositoryType.VECTOR)
        .searchConfig(GroundingFilterSearchConfiguration.create().maxChunkCount(1))
        .addDocumentMetadataItem(documentMetadata);

var groundingConfig = Grounding.create().filters(databaseFilter).metadataParams("*");
var prompt =
    groundingConfig
        .createGroundingPrompt(userMessage)
        .messageHistory(
            List.of(Message.system("Add in the response all metadata from grounding.")));

var configWithGrounding = config.withGrounding(groundingConfig);
return client.chatCompletion(prompt, configWithGrounding);
```

### Grounding with help.sap.com

```java
// From sample-code/spring-app/.../OrchestrationService.java:
// public OrchestrationChatResponse groundingHelpSapCom(String userMessage) {

var groundingHelpSapCom =
    DocumentGroundingFilter.create().dataRepositoryType(DataRepositoryType.HELP_SAP_COM);
var groundingConfig = Grounding.create().filters(groundingHelpSapCom);
var configWithGrounding = config.withGrounding(groundingConfig);
var prompt = groundingConfig.createGroundingPrompt(userMessage);
return client.chatCompletion(prompt, configWithGrounding);
```

---

## Embeddings

```java
import com.sap.ai.sdk.orchestration.DpiMasking;
import com.sap.ai.sdk.orchestration.OrchestrationEmbeddingRequest;
import com.sap.ai.sdk.orchestration.OrchestrationEmbeddingResponse;
import com.sap.ai.sdk.orchestration.model.DPIEntities;
import static com.sap.ai.sdk.orchestration.OrchestrationEmbeddingModel.TEXT_EMBEDDING_3_SMALL;

// From sample-code/spring-app/.../OrchestrationService.java:
// public OrchestrationEmbeddingResponse embed(List<String> texts) {

var masking =
    DpiMasking.anonymization()
        .withEntities(DPIEntities.PERSON)
        .withAllowList(List.of("SAP", "Joule"));

var request =
    OrchestrationEmbeddingRequest.forModel(TEXT_EMBEDDING_3_SMALL)
        .forInputs(texts)
        .withMasking(masking);
return client.embed(request);
```

---

## Content Filtering & Data Masking

### Azure Content Filter with Thresholds

```java
import com.sap.ai.sdk.orchestration.AzureContentFilter;
import com.sap.ai.sdk.orchestration.AzureFilterThreshold;

// From sample-code/spring-app/.../OrchestrationService.java:
// public OrchestrationChatResponse inputFiltering(AzureFilterThreshold policy) {

var filterConfig =
    new AzureContentFilter()
        .hate(policy)
        .selfHarm(policy)
        .sexual(policy)
        .violence(policy)
        .promptShield(true);

var configWithFilter = config.withInputFiltering(filterConfig);
return client.chatCompletion(prompt, configWithFilter);
// AzureFilterThreshold values: ALLOW_SAFE, ALLOW_SAFE_LOW, ALLOW_SAFE_LOW_MEDIUM, ALLOW_ALL
```

### Output Filtering with Protected Material Code Detection

```java
// From sample-code/spring-app/.../OrchestrationService.java:
// public OrchestrationChatResponse outputFiltering(AzureFilterThreshold policy, Boolean isProtected) {

var filterConfig =
    new AzureContentFilter()
        .hate(policy)
        .selfHarm(policy)
        .sexual(policy)
        .violence(policy)
        .protectedMaterialCode(isProtected);

var configWithFilter = config.withOutputFiltering(filterConfig);
```

### LlamaGuard Filter

```java
import com.sap.ai.sdk.orchestration.LlamaGuardFilter;
import com.sap.ai.sdk.orchestration.model.LlamaGuard38b;

// From sample-code/spring-app/.../OrchestrationService.java:
// public OrchestrationChatResponse llamaGuardInputFilter(boolean filter) {

var llamaGuardConfig =
    LlamaGuard38b.create()
        .violentCrimes(filter)
        .nonViolentCrimes(filter)
        .sexCrimes(filter)
        .childExploitation(filter)
        .defamation(filter)
        .specializedAdvice(filter)
        .privacy(filter)
        .intellectualProperty(filter)
        .indiscriminateWeapons(filter)
        .hate(filter)
        .selfHarm(filter)
        .sexualContent(filter)
        .elections(filter)
        .codeInterpreterAbuse(filter);

var filterConfig = new LlamaGuardFilter().config(llamaGuardConfig);
var configWithFilter = config.withInputFiltering(filterConfig);
return client.chatCompletion(prompt, configWithFilter);
```

### Data Masking (Anonymization)

```java
import com.sap.ai.sdk.orchestration.DpiMasking;
import com.sap.ai.sdk.orchestration.model.DPIEntities;

// From sample-code/spring-app/.../OrchestrationService.java:
// public OrchestrationChatResponse maskingAnonymization(DPIEntities entity) {

var systemMessage =
    Message.system("Please evaluate the following user feedback and judge if the sentiment is positive or negative.");
var userMessage =
    Message.user("I think the SDK is good, but could use some further enhancements. My architect Alice and manager Bob pointed out...");

var prompt = new OrchestrationPrompt(systemMessage, userMessage);
var maskingConfig = DpiMasking.anonymization().withEntities(entity);
var configWithMasking = config.withMaskingConfig(maskingConfig);
return client.chatCompletion(prompt, configWithMasking);
```

### Data Masking (Regex)

```java
// From sample-code/spring-app/.../OrchestrationService.java:
// public OrchestrationChatResponse maskingRegex() {

var regex = "patient_id_[0-9]+";
var replacement = "REDACTED_ID";
var maskingConfig = DpiMasking.anonymization().withRegex(regex, replacement);
var configWithMasking = config.withMaskingConfig(maskingConfig);
```

---

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `401 Unauthorized` | `AICORE_SERVICE_KEY` is wrong, expired, or belongs to the wrong instance | Verify the service key JSON is complete and current; invoke `aicore-admin-resources` to re-check credentials |
| `404 Not Found` | No deployment exists for the requested model in the target resource group | Invoke `aicore-lifecycle-management` to list or create the required deployment |
| `No credentials found` | `AICORE_SERVICE_KEY` environment variable is not set (local dev) or `VCAP_SERVICES` is absent (BTP) | Set `export AICORE_SERVICE_KEY='...'` locally, or invoke `aicore-admin-resources` to configure credentials |
| `OrchestrationFilterException.Input` | The input prompt was blocked by the configured content filter (e.g. `AzureContentFilter`, `LlamaGuardFilter`) | Revise the prompt to comply with the filter policy, or adjust filter thresholds via `withInputFiltering()` |
| `OrchestrationFilterException.Output` | The model response was blocked by the configured output content filter | Adjust the output filter thresholds via `withOutputFiltering()`, or refine the prompt to steer the model away from blocked content |
| `OrchestrationClientException` | General API or connectivity error (network issue, malformed request, service outage) | Call `e.getHttpResponse()` / `e.getErrorResponse()` to inspect the HTTP status and error body; check AI Core service availability |
