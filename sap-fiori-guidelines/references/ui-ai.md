# SAP Fiori UI Elements: Ai

This reference covers the following UI components:

- [Ai Acknowledgment](#ai-acknowledgment)
- [Ai Button](#ai-button)
- [Ai Writing Assistant](#ai-writing-assistant)
- [Guided Prompts](#guided-prompts)
- [Home Page Banner](#home-page-banner)
- [Local Ai Notice](#local-ai-notice)
- [Quick Prompts](#quick-prompts)
- [Regenerate](#regenerate)

---

## ai-acknowledgment

The AI acknowledgment pattern informs users during
onboarding about the presence of AI capabilities in the
product. It provides a standardized message using
predefined UI components to ensure clarity,
accessibility, and consistency across SAP products.
## When to Use

+----------------------------------x----------------------------------+
When To Use
+----------------------------------x----------------------------------+
Do
Use the AI acknowledgment pattern to:
- Inform the user about a present AI service or function.
- Educate the user on important properties of the AI system.
+----------------------------------x----------------------------------+
Don't
Don’t use the AI acknowledgment pattern to:
- Notify the user about failed or successful AI processes.
- Send marketing or advertisement information about the AI service.
- Display any other system-related information.

### High-stakes situations

AI acknowledgment is highly recommended in situations where educated user decisions on AI-created results are critical. In other words, the risks associated with such an action are usually high.

Examples of high-stake scenarios include:

- Financial forecasting
- Contract recommendations
- Human resources insights
- Customer communications

### Low-stakes situations

AI acknowledgment may be optionally used in situations where the risks associated with applied actions are usually low and can be easily reverted at any time. Other patterns, such as AI explainability and AI notice, may already provide enough visual cues to inform the user of possible AI involvement in the provided content.

Examples of low-stake scenarios include:

- Entertainment
- Recipe/lifestyle suggestions
- Generic communication responses and greetings

## Anatomy

The AI acknowledgment pattern extends the [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog-web-component/) ([message box](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-box/)) component to enable new AI-specific interactions.

Structure of the AI acknowledgment message

1. **Container:** Dialog component (message box type).
2. **Intro/primary message:** Describe what the message is about. Tailor it to the given context.
3. **Details/link:** Link to relevant documentation defined by the product.
4. **Title:** *Disclaimer* headline.
5. **Disclaimer text:** Standard AI notice message text.
6. **Checkbox (optional):** *Don’t show me again.*

## Types

The AI acknowledgment provides a standard message text. We advise adhering to the suggested wording to maintain consistency and ensure user familiarity. Modify the text only if necessary\.

### Recommended message text

#### Purpose

Onboarding/welcome message
more information, see \<link>.
Show this message when a user opens an AI-enabled
application for the first time.
Artificial Intelligence (AI) generates results based on
multiple sources. Outputs may contain errors and
inaccuracies. Consider reviewing all generated results
and adjust as necessary.
☑ Don’t show me again

### Footer actions

Footer actions should align with the purpose of the message.

**Informational only (no action required):**
Message with *Close* (tertiary) button.

**Informational with** ***Don’t show me again*** **option:**
Message with *OK* (primary) button and a checkbox to hide future messages.

**Acknowledgment required with** ***Don’t show me again*** **option:**
Message with *Accept* (primary) and *Dismiss* (tertiary) buttons, with a checkbox to hide future messages.
## Behavior and Interaction

### Trigger and events

The AI acknowledgment dialog is displayed when the user opens a screen that provides AI-enabled features.

### “Don’t show me again” option

You can provide a *Don’t show me again* option in the
acknowledgment popover to avoid the repetition of
identical messages. If this option is activated, the
message is no longer displayed in future sessions in the
same application locally, or for the same AI service
globally. It does not prevent other messages from showing
up.
We recommend providing a dedicated location where users
can retrieve this information again at any time.

### When to show again

The message box can be displayed again if the status or properties of the AI service have changed significantly, even if the user has selected *Don’t show me again*. We recommend displaying the AI acknowledgment again when:

- An application that previously had no AI features is now enhanced with AI capabilities.
- An application with existing AI features has been upgraded with a new AI capability.

**> **Information:** **

This behavior might be configured and personalized by the customer. Customers might also choose to communicate the
related information through different means.

## Responsive Behavior

The AI acknowledgment builds on the foundation of the message box. To learn more about the responsive behavior of the AI acknowledgment, refer to the [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog-web-component/) ([message box](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-box/)) guidance.

## Localization

To learn more about the support for left-to-right (LTR) and right-to-left (RTL) languages in the AI acknowledgment, refer to the [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog-web-component/) ([message box](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-box/)) guidance.

## Responsible AI

**Communicate clearly**
Use clear, simple language to ensure users understand the meaning of the message and linked information. Avoid technical jargon or legal
language that may confuse users.

---

## ai-button

AI buttons allow users to trigger AI-powered actions. Refer to the  [quick prompts](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/) guidance for examples.
*AI button variants*

## When to Use

Do
Use the AI button:
- To enable users to access AI-powered functions.
- To group AI actions related to one specific element or
page.
+------------------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------------------+
Top Tips
+------------------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------------------+
- Adhere to the rules for SAP design system buttons. For details, see the button guidelines for [SAPUI5](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/) and [SAP Web Components](https://www.sap.com/design-system/fiori-design-web/ui-elements/button-web-component/).
- Use secondary action buttons by default.
- Use primary buttons only for the primary action on the page or panel.
- Only use leading icons.
- Only use the sparkles icon.
- Use concise button labels that clearly describe the action they represent.
- Don’t include “AI” in the button label (such as *Create with AI*, *Enhance with AI*, *Generate with AI*).

## Anatomy

The AI button is made up of the following elements to enable AI-powered functions:

**Base components**
- [Button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button-web-component/)
- [Menu button](https://www.sap.com/design-system/fiori-design-web/ui-elements/menu-button-web-component/)
- [Split button](https://www.sap.com/design-system/fiori-design-web/ui-elements/split-button-web-component/)
- [Menu](https://www.sap.com/design-system/fiori-design-web/ui-elements/menu-web-component/)
**Base components**
- [Button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button-web-component/)
- [Menu button](https://www.sap.com/design-system/fiori-design-web/ui-elements/menu-button-web-component/)
- [Split button](https://www.sap.com/design-system/fiori-design-web/ui-elements/split-button-web-component/)
- [Menu](https://www.sap.com/design-system/fiori-design-web/ui-elements/menu-web-component/)
### AI Button

1. **Container:** Different background colors visualize the
type and state of the AI button.
2. **Text:** Descriptive label that clearly conveys the
action that is invoked by the AI button.
3. **Icon:** Provides emphasis and symbolic identification
of the action as AI-powered in addition to the label.
### AI Menu Button

1. **Container:** Different background colors visualize the
type and state of the AI button.
2. **Text:** Descriptive label that clearly conveys the
group of actions that can be triggered by the AI menu
button.
3. **Icon:** Provides emphasis and symbolic identification
of the action as AI-powered in addition to the label.
4. **Arrow:** Indicates that choosing this button opens a
menu with a group of options.
### AI Split Button

1. **Container:** Different background colors visualize the
type and state of the AI button.
2. **Text:** Descriptive label that clearly conveys the
action that can be triggered by the left interactive area.
3. **Icon:** Provides emphasis and symbolic identification
of the action as AI-powered in addition to the label.
4. **Arrow:** Indicates that choosing this button opens a
menu with a group of options.
5. **Separator:** Indicates that the two areas result in different actions.
## Variants

### AI Button

Use the simple variant for scenarios involving a single
AI action.
*AI button with icon and label*

**> **Guideline:** **

Your button label and tooltip must clearly reveal that the action is enabled by AI.

### AI Menu Button

Use the menu variant to offer multiple AI actions. Users can select and trigger an AI-powered action from the drop-down menu.

*AI menu button with icon and label*

**> **Guideline:** **

Hiding the button label is allowed only for the menu button and within the [AI writing assistant](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-writing-assistant/).

### AI Split Button

Use the split variant to offer one main action with
additional related options. The drop-down menu can list
refinements or variations for the main action.

## Behavior and Interaction

The example below shows how the AI button changes during the content generation process.

1. Choosing the *Generate* AI button triggers content generation.
*AI button before triggering the content generation*

2. During content generation, the button changes its appearance and function. The *Generate* button changes into a *Stop Generating* button, allowing users to stop the process at any time.
*AI button during content generation*

3. Once generation is complete or stopped by the user, the *Stop Generating* button changes into an AI menu button. In this example, it becomes *Revise* following the quick prompt pattern. This could otherwise be *Regenerate*.
*AI button after content generation*

---

## ai-writing-assistant

This article discusses the usage of the AI writing assistant.

The AI writing assistant streamlines interactions with generative AI, helping users complete tasks more efficiently and making the experience intuitive and valuable for them.

The AI writing assistant is available within an input field, text area, or rich text editor component to assist users in creating, iterating, and improving their text input through [quick prompts](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/). These instructions for generative AI are crafted by experts known as prompt engineers, who focus on prompt quality and achieving the most optimal output. The AI writing assistant menu provides writing-specific prompts such as *Change Tone*, *Adjust Length*, *Translate*, and *Make Bulleted List*, which users can apply to the entire text.

*AI writing assistant applied to a rich text editor*

## When to Use

+----------------------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------------------+
When To Use
+----------------------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------------------+
Do
Use the AI writing assistant:
- For repetitive text writing and editing tasks.
- To spark creativity with diverse, unexpected AI outputs.
- To enhance and speed up text iteration and refinement.
+----------------------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------------------+
Don't
Don’t use the AI writing assistant:
- For non-AI functions.
- For non-text editing tasks.
- Together with the button or menu for [quick prompts](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/).
- For personalized or customized outputs. Use [guided prompts](https://www.sap.com/design-system/fiori-design-web/ui-elements/guided-prompts/), custom prompts, or Joule instead.
- Where AI-assisted editing adds no value, for example:
- Pre-populated fields with confident AI recommendations
- Unpredictable user intent
- Lack of context or data for high-quality results; consider using [guided prompts](https://www.sap.com/design-system/fiori-design-web/ui-elements/guided-prompts/), custom prompts, or Joule instead.

+------------------------------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------------------------------+
+------------------------------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------------------------------+
- Use the AI writing assistant with the [AI notice base concept](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/ai-notice-base-concept) to inform users they’re interacting with AI.
- Make sure that the language used by the AI agent is unbiased and inclusive. It should also correspond to the company tone and identity.
- Use recommended AI action labels and keyboard shortcuts.
- Ensure text area and rich text editor components have the proper minimum height to accommodate the AI writing assistant.
- Prioritize AI value and performance:
- Enable the AI writing assistant only on key fields that benefit from creative or iterative suggestions.
- Coordinate with your product team to limit AI prompts based on user needs and subscription costs.
- Use a character limit as a parameter for content generation to reduce subscription costs and improve user outcomes.

+------------------------------------------------------------x------------------------------------------------------------+
Top Tips (external_only)
+------------------------------------------------------------x------------------------------------------------------------+
- Make sure that the language used by the AI agent is unbiased and inclusive.
- Use recommended AI action labels and keyboard shortcuts.
- Ensure text area and rich text editor components have the proper minimum height to accommodate the AI writing
assistant.
- Prioritize AI value and performance:
- Enable the AI writing assistant only on key fields that benefit from creative or iterative suggestions.
- Use a character limit as a parameter for content generation to reduce subscription costs and improve user outcomes.

## Components

The AI writing assistant pattern extends the following components to enable new AI-specific interactions:

- [AI button](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-button/)
- [Menu](https://www.sap.com/design-system/fiori-design-web/ui-elements/menu-web-component/)
- [Input](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-web-component/)
- [Text area](https://www.sap.com/design-system/fiori-design-web/ui-elements/text-area-web-component/)
- [Rich text editor](https://www.sap.com/design-system/fiori-design-web/ui-elements/rich-text-editor/)

### Within input

In a single-line input, the AI writing assistant includes the following components:

1. **AI icon menu button:** Embedded within the input
field, the button indicates AI writing assistance and
offers a menu with AI prompts.
2. **Menu:** Popover menu consisting of AI prompts
configured by product teams.
3. **Versioning:** Enables users to navigate through the
different versions of text. Positioned within the menu, it
includes:
**a. Version indicator**
**b.*****Previous Version*** **button** for navigation
**c.** ***Next Version*** **button** for navigation
### Within a text area or rich text editor

In the text area and rich text editor components, the AI writing assistant includes the following components:

1. **AI writing assistant toolbar:** Embedded within the text area or rich text editor, the toolbar spans the entire width of the parent component. The AI icon menu button is shown alongside the performed AI prompt label and versioning elements when supported.
2. **Versioning**: Enables users to view different versions of AI-generated content. Positioned within the AI writing assistant toolbar, it includes:
   ***a. Previous Version*** **icon button** for navigation
   **b. Version indicator**
   ***c. Next Version*** **icon** **button** for navigation
3. **Performed AI prompt:** Label displaying the AI prompt applied to this version of the content. When available, the prompt label is shown to the right of the versioning elements.
4. **AI icon menu button:** Positioned within the AI writing assistant toolbar, the button indicates AI writing assistance and provides a menu with AI prompts.

*Anatomy of the AI writing assistant for a text area or rich text editor*

## Behavior and Interaction

When the user focuses on an AI-enabled field, the AI
writing assistant appears within the component. Choosing
the AI icon menu button opens the AI writing assistant
menu, allowing users to generate content or refine
existing text.
### Content generation in input

#### Starting the generation process

The AI icon menu button opens the menu for the AI writing assistant
prompts, allowing the user to select the *Generate* AI action.
*Initiating the AI writing assistant for an input*

#### During generation

1. **Busy indicator:** The input shows a busy indicator, informing the user that the AI is
processing the request. Once the generation starts, the busy indicator is replaced by text
streaming – AI-generated text that appears token by token in the input.
2. ***Stop Generating*** **icon button:** The AI icon menu button changes to a *Stop Generating*
icon button, allowing the user to halt the AI process at any time. If the user chooses this
button, the input reverts to its previous state.
#### After generation

When generation is complete, the new text is displayed. A
version control is embedded in the menu for refinement.
The versioning element appears when an AI prompt is
applied to a populated field, or when more than one AI
prompt is applied to the same field.
### Content generation in a text area or rich text editor

#### Starting the generation process

The AI icon menu button, located in the AI writing assistant toolbar, opens the menu for the AI writing assistant prompts, allowing the user to choose the *Generate* AI action.

*AI writing assistant in the rich text editor*

#### During generation

1. **Busy indicator:** The text area shows a busy indicator, informing the user that the AI is processing the request. Once the generation starts, the busy indicator is replaced by text streaming.
2. **AI writing assistant toolbar:** Embedded within the text area or rich text editor, the toolbar allows the user to see the applied prompt and the *Stop Generating* action.
3. ***Stop Generating*** **icon button:** The AI icon menu button changes to a *Stop Generating* icon button, allowing the user to halt the AI process at any time. If the user chooses this button, the text area reverts to its previous state.

*Generating content in the rich text editor*

#### After generation

Once the generation process is completed, the new text is displayed in the text area.

AI menu options now include recommended AI writing assistant quick prompts, which can be applied to the entire text.

*Generation completed*

For details on how to display the busy indicator during content generation, see [Busy Indicator](https://www.sap.com/design-system/fiori-design-web/ui-elements/busy-indicator-web-component/).

### Refining

Users can iterate and refine the generated text as needed by applying more AI writing assistant prompts. The number of prompts should be determined by your product team, as it affects the customer’s AI subscription costs.

*AI writing assistant completed generation of content within the rich text editor*

### Versioning

The versioning elements appear in the AI writing assistant when an AI prompt is applied to a populated field, or when more than one AI prompt is applied to the same field.
If no prompts have been used, the versioning elements are hidden.
*Versioning for an input within the menu of the AI writing assistant*
If versioning is supported, the versioning elements appear inside the menu for input fields. In text areas or rich text editors, the versioning elements appear in the
toolbar.
Each time new content is generated through an AI prompt, a new version is created and the version number updates. The *Previous Version* and *Next Version* icon buttons
adjust to the appropriate states (regular or disabled). If the user adds text, applies formatting, or manually edits the generated text, these changes are retained within
the version and won’t create new versions.
After [form field validation](https://www.sap.com/design-system/fiori-design-web/ui-elements/form-field-validation/?external), the value state remains within each version.
*AI writing assistant after generating content within the rich text editor*

**> **Guideline:** **

**Align with your product team** on the use of the AI writing assistant:
- To manage costs and sustainability, follow product team guidance on the number of prompts users can apply in a given use case.
- Define the relationship between global AI actions and the AI writing assistant version control.
- If versioning functionality is not supported, we recommend adding a warning [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog-web-component/) to ensure users are aware of potential content loss when applying more prompts to fine-tune the content.

### Quick prompts

#### Using AI actions

To ensure a consistent user experience across all SAP products, we recommend using the AI writing assistant prompts listed in the [terminology](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-writing-assistant/ai-writing-assistant/#terminology) section below, as long as they align with your product use case.

We don’t recommend using *Make Bulleted List* and *Adjust Length* prompts for single-line input fields.

#### Grouping

For guidance on menu and submenu terminology, see [Quick Prompts – Grouping](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/#grouping) and the [Terminology](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-writing-assistant/usage#terminology) section below.

### Handling errors

If the AI writing assistant prompt is interrupted or fails, follow the guidance for error messages from the [message handling](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/messaging) pattern.

For a consistent user experience, we suggest using the following error message:
*Something went wrong while generating your content. Please try again.*

## Terminology

The following guidance is based on the default labels provided in the [quick prompts](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/) article. To ensure a consistent and familiar experience for users, we recommend using the suggested wording. Only make changes to the default text if absolutely necessary for your specific use case.

### Recommended AI UI text for the AI writing assistant

**Table**

Label for Menu Items     | Text for Performed AI Prompt        | Description

Generate                 | Generated Text                      | Create first text version.

Regenerate               | Regenerated Text                    | Regenerate the text using the same
| prompt.

Fix Spelling and Grammar | Fixed Spelling and Grammar          | Correct errors in spelling and
| grammar.

Rewrite Text             | \*\* choose performed AI prompt for | Change the structure of the text.
applied submenu action
Adjust Length            | \*\* choose performed AI prompt for | Adjust the length of the text.
applied submenu action
Make Bulleted List       | Made Bulleted List                  | Organize information into a list.

Change Tone              | \*\* choose performed AI prompt for | Adjust the style or emotional quality
applied submenu action              | of the text.

Translate                | Translated to < Language # >        | Convert text from one language to
| another.

**Table**

Menu Items with Submenu | Labels for Submenu Items | Text for Performed AI      | Description
| Prompt
Rewrite Text            | Simplify                 | Simplified Text            | Make text easier to
|                            | understand.
Expand                   | Expanded Text              | Elaborate on the content,
|                            | providing more detail or
|                            | depth.
Summarize                | Summarized Text            | Condense information while
|                            | retaining the key points.

Change Tone             | Make More Casual         | Made More Casual           | Make text less formal.
Make More Professional   | Made More Professional     | Makestext more formal.

Adjust Length           | Make Shorter             | Shortened Text             | Reduce the length of the
|                            | text.
Make Longer              | Lengthened Text            | Increase the length of the
|                            | text.

Translate               | Language 1               | Translated to < Language 1 | Translate text into the
| \>                         | selected language.
Language 2               | Translated to < Language 2 | Translate text into the
| \>                         | selected language.

**> **Guideline:** **

For prompts not covered above, apply the following guidelines:
- Use an imperative verb.
- Keep AI action labels as short and clear as possible while prioritizing clarity for users.
- Use the same AI action labels consistently.

## Responsible AI

Responsible AI guidance for the AI writing assistant extends the following guidance:

- [Quick Prompts: Responsible AI](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/#responsible-ai)

### Appropriate use of the AI writing assistant

To ensure responsible use, carefully assess which prompt types suit your use case. Remember that the AI writing assistant uses [quick prompts](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/). These are predefined AI prompts, crafted by prompt engineers, and provided by the system to save users from writing their own.

Use the AI writing assistant only when it enhances user experience by sparking creativity, improving and refining text, accelerating delivery, and improving user confidence and outcome quality.

Avoid using this pattern when the AI lacks the context to produce high-quality outcomes; use guided or custom prompts or a combination instead.

For guidance on menu and submenu terminology, see [Quick Prompts – Grouping](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/#grouping) and the [Terminology](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-writing-assistant/#terminology) section above.

### Building trust


#### Transparency
Ensure users know they’re interacting with AI when they use the AI writing assistant. Follow the provided pattern guideline, incorporating recommended components and patterns, such as the [AI icon](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/foundation/ai-icon), [AI menu button](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-button/#menu-button), and [AI notice](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/ai-notice-base-concept). Use [consistent terminology](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/#terminology).
For more information, refer to the [responsible AI guidance](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/#responsible-ai) within the quick prompt guidelines.

**Default (external_only)**

#### Transparency
Ensure users know they’re interacting with AI when they use the AI writing assistant. Follow the provided pattern guideline and incorporate recommended components and patterns, such as [AI menu button](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-button/#menu-button). Use [consistent terminology](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/#terminology).
For more information, refer to the [responsible AI guidance](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/#responsible-ai) within the quick prompt guidelines.

#### Fairness and inclusion

Ensure our AI avoids using harmful stereotypes from its training data. To achieve this, it’s crucial to craft prompts carefully, rigorously evaluate data sources, regularly test LLMs for bias and fairness, and use methods like blocklists.

### Designing for AI safety

#### Fail-safes

Ensure users are able to cancel generative AI actions in progress. Provide transparency into AI errors and interruptions using the [message strip](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-strip-web-component/) component.

#### Give users control over the system

People should always have control of what’s being created by generative AI applications, including the ability to turn it off or to override its decisions.

### Designing for AI sustainability

#### Energy consumption

Generative AI models use a lot of energy. This can have a significant environmental impact since the energy used to power these models comes from fossil fuels. Be proactive and mindful of keeping \products energy-efficient by:

- Only applying the AI writing assistant when it delivers measurable value to users and customers.
- Limiting the number of times users can apply AI writing assistant prompts to an input field or text area.
- Using recommended quick prompts for text editing and limiting them to those most relevant to your use case.

## Helpful Terms

### Blocklist

A list of specific words, phrases, or types of content that are filtered out to prevent the AI from producing inappropriate outputs.

### Fine-tuning

Fine-tuning LLMs is the resource-intensive process of customizing a pre-trained language model on specific tasks or datasets to make it more proficient and accurate in generating relevant text.

### Generative AI

A type of artificial intelligence that, when instructed by a user, can generate novel content — such as text, images, sound, or video — based on patterns learned from training data.

### Quick prompt

Predefined instructions provided by the system and expertly crafted by prompt engineers, eliminating the need for users to write their own prompts.

---

## guided-prompts

**> **Information:** **

This guideline focuses on guided prompts within dialogs. Variants for popovers and side panels are not included.
Product teams may adapt the example provided to fit their use cases.

## Intro

Guided prompts provide structured input fields and controls that help users instruct the generative AI model on the desired output without having to write descriptive \custom prompts\\. Guided prompts are useful when users want to specify attributes, styles, or criteria for the generated content, such as length or language.

Users can provide specific details through form fields and guided UI elements. The system combines these inputs into a backend prompt, offering control and precision in generating output that aligns with user preferences.

*Guided prompt in a dialog*

## When to Use

+------------------------------------------------------------------------------------x------------------------------------------------------------------------------------+
When To Use
+------------------------------------------------------------------------------------x------------------------------------------------------------------------------------+
Do
Use guided prompts when:
- Users typically submit a limited set of queries.
- The system supports only a specific set of actions.
- Users lack experience in writing prompts.
- Users need consistent and predictable outcomes.
- Users need ways to direct the AI model’s output.
+------------------------------------------------------------------------------------x------------------------------------------------------------------------------------+
Don't
Don’t use guided prompts when:
- Users need a high degree of flexibility and control over the outcome. Use custom prompts instead.
- Tasks are repetitive or common within a workflow. Use [quick prompts](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/) instead.
- The use case requires only one or a few specific actions. Use [quick prompts](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/) instead.
- User intents or desired outcomes are uncertain or undefined. Use custom prompts instead.
- Tasks are complex or multi-step, requiring nuanced input. Use custom prompts instead.

## Anatomy

The guided prompt pattern uses a variety of components to enable new AI-specific interactions. In this example, it is based on a [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog-web-component/) container that can be triggered via an [AI button](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-button/) or [AI menu button](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-button/#ai-menu-button-1). Any container or input component available in the design system can be selected and configured by product teams to afford the options provided in the guided prompt. Examples are: [label](https://www.sap.com/design-system/fiori-design-web/ui-elements/label-web-component/), [select](https://www.sap.com/design-system/fiori-design-web/ui-elements/select-web-component/), [range slider](https://www.sap.com/design-system/fiori-design-web/ui-elements/range-slider-web-component/), and [segmented button](https://www.sap.com/design-system/fiori-design-web/ui-elements/segmented-button-web-component/). Refer to each component guideline when adopting it in your use case.

1. **Container:** A guided prompt is always based on a container, which provides the structure for content input.
2. **Content:** The content consists of a selection of form input components. The structure and visual design depend on the respective guidelines.

Choose input components based on the use case. Select components appropriate to the context and output, and avoid using dropdown menus as the default for all inputs.
3. **Action:** The action is implemented using the [AI button](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-button/) or [AI menu button](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-button/#ai-menu-button-1).

The action applies the chosen prompt criteria and ensures AI processing only begins with user confirmation.

This prevents automatic regeneration or loss of content, avoiding unintended AI modifications.

The container includes an explicit cancel option as a safeguard, allowing users to explore guided prompt options and exit at any point, with clear control over the process.

Action placement follows the general guideline for the container. Wording should be ultimately defined depending on the use case\. For more guidance on terminology, refer to the [quick prompts](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/#terminology) or [AI writing assistant](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-writing-assistant/#terminology) guideline.
## Behavior and Interaction

The guided prompt flow follows a standard interaction pattern based on the chosen container. In this example, users open the dialog, adjust criteria, and confirm to generate content.

### Opening a dialog

Clicking the AI button opens a menu with actions (for example, *Compose Text*) that can trigger the guided prompt.

*Guided prompt button applied to a form input in an object page Floorplan schematic*

### Adjusting criteria

The guided prompt dialog opens with controls to adjust criteria and refine the generated content.

*Guided prompt in a dialog*

### Generating content

Clicking the confirmation action starts content generation based on the specified criteria. As the generation process begins, a busy state is displayed, and the AI button changes into the *Stop Generating* button, allowing users to stop generation at any time.

*Busy state behavior during the generative AI process*

Refer to the [AI writing assistant](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-writing-assistant/) and [regenerate](https://www.sap.com/design-system/fiori-design-web/ui-elements/regenerate/) guidelines for how to handle warnings about overwriting content when versioning is not supported.

Refer to the [busy indicator](https://www.sap.com/design-system/fiori-design-web/ui-elements/busy-indicator-web-component/) guideline for when and how to display the indicator during content generation.

### After generation

The AI-generated content appears in the respective field, and the AI button transitions back to the default state.

*Content generated with guided prompt*

### Handling errors

If the guided prompt is interrupted or fails, follow the guidelines for error messages in the [message handling](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/messaging) guidelines.

For a consistent user experience, we suggest using the following error message:

*Something went wrong while generating your content. Please try again.*

*Error handling for content generation using guided prompts*

### Combining with quick prompts

The AI menu button can be used to combine the easy access for predefined actions of quick prompts with the structured controls of guided prompts.
Add a meaningful action to trigger the guided prompt dialog. In the example, the menu item is labeled *Compose Text*, but the final wording should be \tailored to the use case.
For more information, see the guidelines for [quick prompts](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/) guidelines and [grouping AI actions](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/#grouping).
## Recommendations

### Example scenario: Text composition

One of the most common scenarios for using guided prompts is text composition. Since the guided prompt pattern reuses existing components, you must follow the guidelines for the chosen components.

The following are some examples of prompt criteria that could be used in the context of text composition.

#### Language
*Select component used to provide language options*

#### Text length
*Range slider used to set the length of generated output*

#### Application-specific criteria

For scenarios such as generating a customer response or
handling different types of support responses, criteria
such as *Type of Response* can be added, and the selected
type can be used as a reference for the content
generation process.
## Terminology

The following guidance is based on the default labels provided in the [quick prompts](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/#terminology) guidelines. We strongly recommend maintaining these labels to ensure consistency and support user familiarity across AI tooling. Adjust the labels only as needed for your specific use case\.

#### Standard AI action labels for AI text generation and transformation

**Table (col-width-30-70)**

AI Button Labels

Compose Text
generation.

Revise

**Table (col-width-30-70)**

AI Action Labels for Input Components

Structure
paragraph or list.

Text Length

Language

Tone of Voice

**> **Guideline:** **

For actions not covered above, apply the following guidelines:
- Use a verb in the imperative.
- Keep AI action labels as short as possible while prioritizing clarity for users.
- Use the same AI action labels consistently.
For more information, see [UI Text Guidelines for SAP Fiori Apps](https://www.sap.com/design-system/fiori-design-web/v1-136/foundations/writing-and-wording/ux-writing/ui-text-guidelines-for-sap-fiori#word-choice).

---

## home-page-banner


Implementation of the home page banner web component is still in progress. This guideline provides a preview for
product teams in SAP Business Suite.

## Intro

The home page banner is a standard card used in the hero space of the product home page. It can accommodate different elements, depending on the needs of each product. The banner creates a consistent experience across SAP Business Suite home pages while still allowing for flexibility at the product level.

Product home page banner

## When to Use

Do
Use the home page banner on any product home page that is
part of SAP Business Suite.
standard element to unify product home pages.


The home page banner will be **mandatory** for product home pages in SAP Business Suite, starting with SAP S4/HANA Cloud Public Edition ERP and SuccessFactors.

## Anatomy

Anatomy of the banner component

1. **Banner**
2. **Date**
3. **Salutation**
4. **Background image**
5. **Background color**
6. **Content area** (optional)
7. **Action area** (optional)

### Mandatory elements

1. **Banner:** Standard visual element that unifies all product home pages.
2. **Date:** Shows the current date. Use the full format (Weekday, Month DD, YYYY), for example: Thursday, November 5, 2025.
3. **Salutation:** Personalized static greeting [title](https://www.sap.com/design-system/fiori-design-web/ui-elements/title/), usually shown as “Hello, \<First Name>”. Appears below the date.
4. **Background image:** Default background image. Every product must use a CSS linear transparent gradient.
5. **Background color:** Default background color that appears behind the background image gradient and colors the banner.

### Optional elements

6. **Content area:** The content area displays information that requires user attention, such as KPIs, buttons, search fields, or text.
   - Product requirements determine the content and layout.
   - Content must be responsive.
   - Most content needs to be enclosed in cards to ensure proper color contrast.
7. **Action area:** The action area provides quick-access [buttons](https://www.sap.com/design-system/fiori-design-web/ui-elements/button-web-component/) that guide users to common or high-priority tasks in the product context.
   - Display buttons based on roles, showing or hiding them according to product requirements.
   - Use only secondary button styling, not primary or tertiary.

### Banner height

The banner height is flexible to fit the content.

- Minimum height: 5.75rem (92px)
- Maximum recommended height: 24rem (384px)

Banner with minimum height

Banner with maximum recommended height

### Banner position

Place the home page banner below the persistent [shell bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/shell-bar/) at the top, and beneath the optional [tab bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/tab-bar-web-component/) if it’s present.

Banner position

**> **Guideline:** **

The banner must scroll out of view when users scroll down the page. It must not be sticky.

### Theming

The home page banner supports standard SAP Fiori [themes](https://www.sap.com/design-system/fiori-design-web/foundations/visual/theming).

## Layout Examples

You can tailor the layout to your product context.

### Basic banner

Basic banner with date and salutation

### Full banner

Content area in the bottom half, full width

### Variation – SuccessFactors

50/50 layout

## Customization

If the product supports a theme designer, administrators can fully customize the banner for each theme. They can:

- Change the background color
- Use a different background image
- Change the text color for date, salutation or any other text that sits directly on the background to achieve the right color contrast and remain accessible.
- Remove the banner altogether

Banner with custom color

Banner with custom background

No banner

## Behavior and Interaction

The banner itself is non-interactive. However, elements within the banner follow the behavior of their corresponding components, such as buttons.

## Responsiveness

The home page banner is responsive and supports standard SAP Fiori breakpoints.


Although SAP Fiori doesn’t yet include XS, MAX, and 4K breakpoints, these sizes are included for reference at the
request of product teams.

### Up to 1024px

Responsive behavior up to 1024px

**XS:** 320px
**S:** 450px
**M:** 600px
**L:** 1024px

The banner elements adapt as follows:

- The **date** wraps to show the full format and increases the banner height as needed.
- The **salutation** wraps to the next line, making the banner taller as needed. After three lines, it truncates with the ellipsis (…).
- The **action area** buttons move into the overflow if the screen is too narrow to display all actions. If needed, the entire section can wrap underneath the salutation area.
- The height of the banner hugs its contents. The banner resizes responsively, becoming taller or shorter depending on the **content** elements it holds.

### Large Screens

On large screens, choose either a full-width banner or a letterboxing layout, depending on product requirements.

Large screens include:

- **XL**: 1440px
- **MAX**: 1920px
- **4K**: 2560px

Full width layout

Letterboxing layout

---

## local-ai-notice

The local AI notice pattern ensures users are informed
when content is AI-generated, encouraging them to verify
its accuracy prior to use.
For simplicity, this guideline shows illustrations of the
object page floorplan as an example, but the fundamental
rule of placement is applicable to all page types and
layouts.
**> **Information:** **

This guideline is **mandatory** according to [Article 50 of the EU AI Act](https://artificialintelligenceact.eu/article/50/) and in alignment with the [SAP AI Ethics Policy](https://www.sap.com/documents/2022/01/a8431b91-117e-0010-bca6-c68f7e60039b.html) for all user interfaces that involve AI-generated or AI-edited information. For more information on application scenarios, AI notice lifecycle, and AI impact assessment process, see the [AI notice base concept](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/ai-notice-base-concept).

Currently this pattern is not available in [SAP Fiori Elements](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/smart-templates).

## When to Use

+----------------------------------------x-----------------------------------------+
When To Use
+----------------------------------------x-----------------------------------------+
Do
Use the local AI notice pattern:
- To explicitly mark content areas that contain information generated by AI.
+----------------------------------------x-----------------------------------------+
Don't
Don’t use the local AI notice pattern:
- For any purpose other than disclosing AI content as defined in this guideline.
- To mark non-AI-related content.

## Components

This pattern is based on the following concept and components:

**Foundational AI concepts**                                                                                                                     | **Components**
- [AI notice base concept](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/ai-notice-base-concept) | - [Link](https://www.sap.com/design-system/fiori-design-web/ui-elements/link-web-component/)
- [Smart link](https://www.sap.com/design-system/fiori-design-web/ui-elements/smart-link/?external)
- [Label](https://www.sap.com/design-system/fiori-design-web/ui-elements/label-web-component/)
## Guidelines

The local AI notice is always paired with other patterns. Refer to the [AI notice base concept](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/ai-notice-base-concept) to learn how it fits into the overall experience.

**Standard text**

For a consistent user experience, use the following standard text:
*Created with AI. Verify before use.*

## Variants

### Interactive AI notice label

This variant is **recommended** for all applications with **high and very high impact decision scenarios**. It enables progressive disclosure of further information through a popover. For more information, see the [link](https://www.sap.com/design-system/fiori-design-web/ui-elements/link-web-component/) component.

**Link styling**
The interactive AI notice uses the standard link styling as defined in the link component specification.

If necessary, you can use the [subtle state](https://www.sap.com/design-system/fiori-design-web/ui-elements/link-web-component/#types) of the link component to further reduce the visual impact when compared to other interactive elements in the environment.
### Read-only AI notice label

Use this variant to fulfill basic labeling requirements when no further **details on the validation of AI results** can be provided. For more information, see the [label](https://www.sap.com/design-system/fiori-design-web/ui-elements/label-web-component/) component.
*Read-only AI notice label embedded below the subsection title*

## Placement

The placement of the AI notice label is crucial to support correct association of the AI notice label with the related AI results.

Limit the number of AI notice labels to **one per screen**. If you find it difficult to identify the correct placement of the AI notice label, apply the following rule of thumb:

**Place the label next to the lowest possible hierarchical title element that contains all present AI results.**

You have AI results distributed within one sub-section **→** AI notice is placed next to the sub-section title.
*AI notice label placed on subsection level*

You have AI results distributed across multiple sub-sections on your object page **→** AI notice is placed on the next higher section title.
*AI notice label placed on section level*

AI has created content for multiple sections in your object page or generated the entire object itself **→** AI notice is placed next to the object title.
*AI notice label placed on page level*

### Information hierarchy

**On top of the content area**
For high–very high impact scenarios.
Place the embedded AI notice label between the section
header and the content area where the AI result is
displayed.
**At the end of the content area**
For low–medium impact scenarios.
Place the embedded AI notice label in the footer of the
AI results area. No additional AI content should appear
below it, and it must remain within the boundaries of the
associated section.
**> **Guideline:** **

Product teams must **apply correct accessibility annotations** when placing the local AI notice label. As a rule, you
must inform the user when an area contains AI-generated or AI-assembled information. You do this by placing the local
AI notice label at the beginning of the area that contains the AI content.
As an exception, in low-impact scenarios, you can place the AI notice at the end of the area. To comply with the
latest accessibility guidance, we advise using the following ARIA attribute to the accessibility region marker if the
label is placed at the end of the content area:
*invisible label: \<region name>. Contains AI-generated content*

## Behavior and Interaction

The interactive AI notice variant uses **progressive disclosure** to indicate that the content was generated with AI and to advise users to review and fact-check results before use. For that purpose, the AI notice can include a link to open a long text description providing more details than the short text.

### Progressive disclosure

The interactive AI notice allows progressive disclosure at 3 levels:

1. Link: AI notice short text
2. Popover: AI notice long text
3. External page: SAP Help Portal product documentation

#### 1. Link: AI notice short text

- Predefined AI notice text to mark AI content areas.
- Can link to a long text in a popover, if provided.
*Interactive AI notice label*

#### 2. Popover: AI notice long text

- Provides a more contextualized explanation of what the
notice means in the current context.
- Can be adjusted to fit the context it is used in.

**> **Guideline:** **

Define the content required in the AI notice long text together with your local AI user experience and user
assistance experts in your product area.

#### 3. External page: SAP Help product documentation

- Can contain a link to a dedicated page on SAP Help
Portal.
- Product teams must work with their local UA experts to
define the appropriate destination and content in their
product documentation.
## Responsive Behavior

The AI notice label must never be truncated. The notice must always be fully readable. Avoid wrapping to keep the notice in one line. To allow for limited space, use breakpoints to show longer or shorter variants of the AI notice text.

How these principles are applied in practice is defined within the related pattern and component guidelines. See the [Related Links](https://www.sap.com/design-system/fiori-design-web/ui-elements/local-ai-notice/#related-links) section below.

#### Standard AI notice label

**Default** for all AI application scenarios.
*Created with AI. Verify before use.*

#### Short AI notice label

**Exceptional use** for placement in limited space.
*Created with AI.*

---

## quick-prompts

In generative AI, prompts are essential for guiding the AI's output. Clear and effective instructions ensure that the output aligns with the user’s needs.
Content generation with quick prompts
Quick prompts are predefined actions integrated into workflows for easy access. These types of prompts are crafted by experts known as prompt engineers, who focus on the efficiency of AI.

## When to Use

+--------------------------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------------------------+
When To Use
+--------------------------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------------------------+
Do
Use quick prompts when:
- Tasks are repetitive or for common actions within a workflow.
- The system can only assist with specific actions.
- Users lack expertise in the subject matter.
- It’s crucial to minimize any bias introduced by users’ writing prompts.
- Maintaining consistent and predictable output is essential.
+--------------------------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------------------------+
Don't
Don’t use quick prompts:
- When a user’s intent is unpredictable.
- When users need more flexibility in directing the output of the AI model.
- For non-AI functions.
- For multiple fields in the form – use actions at the form level instead.
- When implemented through the [AI button](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-button/) or menu button alongside the [AI writing assistant](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-writing-assistant/).

+------------------------------------------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------------------------------------------+
+------------------------------------------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------------------------------------------+
- Use quick prompts with the [AI notice base concept](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/ai-notice-base-concept) to inform users they’re interacting with AI.
- Clearly identify quick prompts with the [AI icon](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/foundation/ai-icon).
- Make sure that the AI output is unbiased, inclusive, and aligns with the company tone and identity.
- Use recommended [AI action labels](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/#standard-ai-action-labels-for-ai-text-generation-and-transformation).
- Follow the [action placement](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement) guidelines and use the emphasized button style only when a quick prompt is the primary action for the page.
- Ensure users can complete the task without using quick prompts and without using AI.

+---------------------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------------------+
Top Tips (external_only)
+---------------------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------------------+
- Clearly identify quick prompts with the AI icon.
- Make sure that the AI output is unbiased, inclusive, and aligns with the company tone and identity.
- Use recommended [AI action labels](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/#standard-ai-action-labels-for-ai-text-generation-and-transformation).
- Follow the [action placement](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement) guidelines and use the emphasized button style only when a quick prompt is the page’s primary action.
- Ensure users can complete the task without using quick prompts and without using AI.

## Components

The quick prompts pattern extends the following components to enable new AI-specific interactions:

- [AI button](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-button/)
- [Menu](https://www.sap.com/design-system/fiori-design-web/ui-elements/menu-web-component/)

### AI button

Use an AI button when only one quick prompt is available.
Style it properly with the AI icon to show that the
action is AI-powered and use a clear label to describe
the action.
### AI menu button

Use an AI menu button when multiple quick prompts are
available. Pair it with the AI icon and a label that
describes the set of AI-powered actions accessible from
the menu.
For more information, see [Menu Button](https://www.sap.com/design-system/fiori-design-web/ui-elements/menu-button-web-component/), [Menu](https://www.sap.com/design-system/fiori-design-web/ui-elements/menu-web-component/), and the [Terminology](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/#terminology) section.

## Behavior and Interaction

### Generating content

##### Starting the generation process

Clicking the AI button initiates content generation with
AI.

##### During generation

When generation begins, the AI button switches to *Stop Generating*,
giving users the option to interrupt the process at any time. The
text area first displays a busy indicator to show that the request
is being processed. As soon as output starts streaming in, the busy
indicator is replaced by the generated text. During this time,
primary actions are temporarily disabled to prevent interaction with
partially generated content.
### Refining

When generation finishes or is stopped, the button transitions to an AI menu button, offering quick prompts users can apply to refine the output. Users can also edit the content directly.

Refining generated content with quick prompts

For information on handling warnings when versioning is not supported, see [AI Writing Assistant](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-writing-assistant/) and [Regenerate](https://www.sap.com/design-system/fiori-design-web/ui-elements/regenerate/).

For information on how to display the text area during generation, see [Busy Indicator](https://www.sap.com/design-system/fiori-design-web/v1-130/ui-elements/busy-indicator-web-component/).

### Handling Errors

If the quick prompt is interrupted or fails, follow the guidance for error messages in the [message handling](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/messaging) article.

For a consistent user experience, we suggest using the following error message:
*Something went wrong while generating your content. Please try again.*

Error handling for content generation using quick prompts

### Grouping

If necessary, organize prompts into submenus to improve
navigation and reduce visual clutter. Group them by
purpose or task, prioritize essential actions at the top,
and keep group sizes manageable to avoid overwhelming
users.
##### Grouping AI and non-AI actions

Group related actions by purpose or outcome, whether they are AI or non-AI functions. When combining both in the same
menu, use the AI icon to identify AI-powered quick prompts and visual dividers to clearly separate them from non-AI
actions.
For more information and labels for submenus, refer to the [terminology](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/#terminology) section.
## Terminology

Use the default labels provided below for text generation scenarios. To ensure a consistent and familiar experience for users, we recommend using the suggested wording. Only make changes to the default text if absolutely necessary for your specific use case.

### Recommended AI UI text for AI text generation and transformation

**Table (col-width-50-50)**

AI Button Labels

Generate

Revise

**Table (col-width-50-50)**

AI Action Labels for Menu Items

Regenerate

Fix Spelling and Grammar

Summarize

Paraphrase

Make Bulleted List

Explain Content

**Table (col-width-20-30-50)**

Menu Items with Submenu | Labels for Submenu Items | Description

Rewrite Text            | Simplify                 | Makes text easier to understand.
Expand                   | Elaborate on the content, providing
| more detail or depth.

Change Tone             | Make More Casual         | Make writing less formal.
Make More Professional   | Make writing more formal.

Adjust Length           | Make Shorter             | Reduce the length of the text.
Make Longer              | Increase the length of the text.

Translate               | Language 1               | Translate text into the selected
| language.
Language 2               | Translate text into the selected
| language.

**> **Guideline:** **

For actions not covered above, apply the following guidelines:
- Use a verb in the imperative.
- Keep AI action labels as short as possible while prioritizing clarity for users.
- Use the same AI action labels consistently.
For more information, see [UI Text Guidelines for SAP Fiori Apps](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/ui-text-guidelines-for-sap-fiori#word-choice).

## Responsible AI

### Appropriate use of quick prompts

Quick prompts are designed to make interactions easier by providing clear, predefined options. They help users complete tasks faster and reduce confusion. However, it's important to use them appropriately. Quick prompts should align with the user's needs. In complex scenarios where more detail or context is required, they may fall short. In such cases, guided or custom prompts can lead to more accurate and comprehensive responses.

### User autonomy

Empower users by enabling them to disable quick prompts and AI features in their workflow. Ensure alternative methods are available for users to complete their tasks without relying on AI.

### AI transparency

Ensure clarity in the deployment of quick prompts, making their use and purpose transparent to users. Use clear indicators, like AI icons or buttons, to ensure users know when they’re interacting with AI. Follow our design guidelines to maintain consistency in how these features are presented.

### Prevent bias in prompt design

Ensure the prompt design process actively involves measures to prevent bias. Like biased training data, poorly designed prompts can produce skewed or harmful results.

Advocate for a diverse group of users and technical experts to focus on thoughtful prompt design, conduct comprehensive evaluations of user needs and outcomes, and iterate to ensure that AI-generated content is as free from bias as possible.

## Prompt Engineering

Prompt engineering is the process of designing and refining instructions to guide the behavior and output of generative AI models.

Your product team is responsible for engineering effective prompts tailored to the underlying AI model, ensuring users get the desired results when using quick prompts.

Follow the \\best practices\ and, where necessary, use advanced LLM techniques like embeddings and fine-tuning to get the best outcomes.

## Helpful Terms

### Foundation models

Large deep learning models trained on massive unlabeled data with self-supervised learning. They provide general-purpose capabilities across domains (text, images, audio, multimodal).

### Large language models (LLMs)

A subset of foundation models specialized in natural language. Trained on vast text datasets, they excel at understanding and generating human language and can be fine-tuned for specific tasks or domains.

### Prompt engineering

The process of designing and refining instructions to guide the behavior and output of generative AI models.

### Embeddings

A way to represent language or data as numbers that capture meaning and similarity. This enables AI to recognize when different words or phrases convey similar ideas, allowing it to retrieve relevant information even without exact word matches and to generalize beyond its training data.

### Fine-tuning

Fine-tuning LLMs is the resource-intensive process of customizing a pre-trained language model on specific tasks or datasets to make it more proficient and accurate in generating relevant text.

---

## regenerate

The regenerate pattern provides a general approach for using AI to create or modify content across different scenarios. It lets users generate alternative AI results or update existing AI-generated content, such as text, images, or other digital items, with the help of AI. Users can also iteratively refine the results to better match their needs or preferences.

## When to Use

+-----------------------------------------------------------x-----------------------------------------------------------+
When To Use
+-----------------------------------------------------------x-----------------------------------------------------------+
Do
Use the regenerate pattern:
- To rerun the generation of information for a defined content element.
- To re-initiate the generation of content based on a form that provides further configuration options to control the
final output.
+-----------------------------------------------------------x-----------------------------------------------------------+
Don't
Don’t use the regenerate button:
- For non-AI functions.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------x----------------------------------------------------------------------------------------------------------------------------------------------------------------+
Top Tips
+----------------------------------------------------------------------------------------------------------------------------------------------------------------x----------------------------------------------------------------------------------------------------------------------------------------------------------------+
- Use clear, meaningful labels that make the purpose of each action easy to understand in context.
- Always check\ if the generic labels used in this guideline are sufficient or if you need to apply more descriptive labels to guide your users.
- Message the user before overwriting the existing content.
- Inform the user where to retrieve previous variants if you use versioning.
- Use loading indicators, busy state and messaging patterns to inform users that new content is being generated.
- Consider user needs, subscription costs, and \\sustainability\ when enabling content regeneration.

## Components

This pattern is based on the following key elements to support regeneration scenarios:

**Foundational AI patterns**                                                                       | **Global patterns**                                                                                                                       | **Components**
- [Quick prompts](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/)   | - [Action placement](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement)      | - [AI button](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-button/)
- [Guided prompts](https://www.sap.com/design-system/fiori-design-web/ui-elements/guided-prompts/) | - [Messaging overview](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/messaging)
- [Handling busy states](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/busy-handling)
### AI Button

The [AI button](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-button/) is the base component for placing AI-related actions in the user interface.
*AI button and AI split button in the regenerate pattern*

**> **Information:** **

The AI button component extends common base components like [button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button-web-component/), [menu button](https://www.sap.com/design-system/fiori-design-web/ui-elements/menu-button-web-component/), [split button](https://www.sap.com/design-system/fiori-design-web/ui-elements/split-button-web-component/), and [menu](https://www.sap.com/design-system/fiori-design-web/ui-elements/menu-web-component/). For more information, see the [AI button](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-button/) component guideline.

### Guidelines

#### Icon Usage

Only use the standard icons as described in the [AI button](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-button/) guideline.
*Don’t use alternative icons on the ‘Regenerate’ button*

#### Button Types

Don’t use the icon button for regenerate use cases.
Always use buttons with both an icon and a label.
*Don’t use an icon-only ‘Regenerate’ button*

#### Label

Use the generic term *Regenerate* only if the outcome of the action is obvious or explained through the context.

## Behavior and Interaction

### Regenerate

When an AI action is triggered, the user is passed through the following steps:

- **Event:** Content regeneration can be triggered by a user activating an AI action, by a system event (such as auto-generation), or through interaction with Joule.
- **Send request:** The results provided by AI might be influenced by given directions (prompts) as well as available and accessible contextual information (for example, document data, user inputs, or relational data).
- **Response time:** If the response takes too long, inform the user and let them choose to either cancel the request or continue processing it in the background and get notified when it’s ready. For more information, see the guidance for [message handling](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/messaging).
- **Process time:** AI results might be provided using a batch job approach. However, we recommend enabling content streaming and allowing for asynchronous processing to shorten the perceived waiting time for the user. Alternatively, the target element may be set to [placeholder loading](https://www.sap.com/design-system/fiori-design-web/ui-elements/placeholder-loading/) or [busy state](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/busy-handling) if the generation process is ongoing.
- **Delivery:** The final AI result can be provided in different ways, as outlined in the [output handling](https://www.sap.com/design-system/fiori-design-web/ui-elements/regenerate/#output-handling) section of this guideline.
- **Finalization:** The user may need to provide explicit approval, either through a confirmation [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog-web-component/) or by selecting which AI-generated result should be applied.
- **Implementation:** Some implemented AI results might receive additional visible and invisible markup to ensure compliance with public legal regulations\, as well as to increase user trust and ensure proper user control over AI results.
*Regenerate pattern applied to a text area in a dialog*

### Output Handling

This pattern might be applied in the following setups:

#### Overwriting

Results provided by AI are implemented directly and overwrite any existing data in the affected target element. Always notify users before overwriting content. We recommend providing options to easily revert previous actions (such as an *Undo* button).

#### Preserving Content

- **Versioning:** Results are provided in addition to existing data. The user chooses their preferred option **within the affected target element** before finalizing.
- **Sandbox:** Results are first provided in a separate, safe environment before they are implemented in the target destination. For example, a sandbox can be any UI element like a dialog or side-panel, or an element inside the Joule conversational UI. The output can then be compared with any existing content, refined, and optimized. Once approved, the finished content is transferred to the final destination.

**> **Warning:** **

Versioning is currently only supported within the [AI writing assistant](https://www.sap.com/design-system/fiori-design-web/ui-elements/ai-writing-assistant/) experience.

### Update after Changed Context

#### Change Contextual Information

Generated results might become invalid due to changes in the data used by the AI system to generate the result – known as the context. We recommend [messaging](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/messaging) the user if the information on which the output was based has changed. New context can lead to different outcomes, and relying on outdated information may result in undesirable consequences.

#### Time and Status Stamps

AI results might receive additional status and time attributes to let the user know when they were generated or when they expired.

**> **Guideline:** **

- When versioning is not supported, it's important to inform users that regenerating will replace existing content. For
details, see [Overwriting](https://www.sap.com/design-system/fiori-design-web/ui-elements/regenerate/#overwriting).
- In mixed forms that contain both user input and AI-generated content, the regeneration process should replace only the
AI-generated fields to ensure that user content is preserved.

## Placement

In most cases, the placement of the *Regenerate* action is defined by the global [action placement](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement) guidance. However, there are a few additional aspects to consider:

### Principles

- AI flows **are always optional.** Users must always have the option to complete the task manually or through traditional, non-AI, methods. This means most AI buttons are non-primary actions.
- *Generate* and *Regenerate* actions can only be primary if they are a consecutive or finalizing step of a defined AI flow (for example, *Generate* as a finalizing action for preceding action *Generate Job Description*).
- Related actions that lead to the same or similar end goal should be grouped together, **regardless of whether they are AI or non-AI functions** (for example, *Create Report* opens the options *Menu,* *From Document*, and *Generate*). Avoid individual placement of multiple AI functions in the same toolbar.
- In most cases, the *Regenerate* button should replace the *Generate* button if the AI has previously provided results in the same session, keeping its original position.

### Placement on the Page

AI actions can be placed in [toolbars](https://www.sap.com/design-system/fiori-design-web/ui-elements/toolbar-overview/) at any hierarchy level of the page, depending on the affected target of the AI action.

**> **Guideline:** **

It is considered a best practice to place actions near their associated target element. For example, if your AI
action provides generative functions that affect the entire page, place it in the header toolbar. If your AI feature
only affects a specific text field within a page section, place your embedded AI action close to the target field.

*‘Regenerate’ for a full page*

#### Placement in the Object Page Footer Bar

The object page footer bar is reserved for finalizing actions applied to the entire object. We don’t recommend placing AI functions in the footer bar as primary actions. In alignment with our AI design principles, AI interaction is always optional and should not block users from achieving their task through traditional non-AI methods.

### Placement in Dialogs

You can place AI actions in dialogs to support regeneration functions. See the guideline on [dialogs](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog-web-component/) for proper action placement.

#### In the Dialog Body

Use a secondary button embedded in a toolbar to regenerate individual editable parts of content inside the body of the dialog.

#### In the Dialog Footer

Use a secondary button to regenerate all of the content within the dialog. Use a primary button to regenerate content outside of the dialog.

*Dialog with secondary ‘Regenerate’ action*

### Placement on a Single Element

To enable regeneration of single elements, place the *Regenerate* button as close to the content as possible, following the [action placement](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement) guidelines. If additional customization options are available, consider using [quick prompts](https://www.sap.com/design-system/fiori-design-web/ui-elements/quick-prompts/).
*Regenerate split button attached to text area*

**> **Guideline:** **

Placing dedicated AI functions directly on individual elements should be the exception, not the standard. Consider
whether this placement is truly necessary, or if the same value can be achieved by integrating the function into the
common toolbar of the next higher-level wrapping element (for example, form, subsection, or section toolbar).

## Messaging

### Pending Request

You may inform the user if the system is under heavy load
and can’t process requests immediately.
*Info message dialog*
**Example**
*“The system is taking longer than usual. We’ll notify
you as soon as your request is complete.”*
### Overwriting

When versioning is not supported, use a message [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog-web-component/) to inform users about content replacement and data loss. For a consistent user experience, we recommend using the following warning message:
**Example**
*“Regenerating will overwrite all fields with AI-generated content. Do you want to continue?*”
### Finalization

Some AI application scenarios require explicit
confirmation or selection from the user before AI results
are finalized, or the page is exited. You may notify the
user about any unconfirmed results and ask how they
should be handled.
**Example**
*“You have \<number> unconfirmed recommendations.
Unconfirmed AI results will be lost.*”
For low-impact scenarios where repeated warnings are unnecessary, include an option to skip the message in the future (*Don’t ask me again* or *Don't show me again)*.

### Warning Message Strip

In scenarios where a warning needs to be shown permanently, use a message strip after showing the initial warning dialog.

For more information, see the guidelines for the [message box](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-box/) and [message strip](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-strip-web-component/).

*Warning message strip in a full page*

---

