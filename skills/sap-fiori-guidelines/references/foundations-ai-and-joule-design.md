# SAP Fiori Foundations: Ai And Joule Design

## Foundation

**Design System Hero**

# AI and Joule Design – Foundation

+----------------------------------------------------------x-----------------------------------------------------------+
Tiles (plain)
+----------------------------------------------------------x-----------------------------------------------------------+
[AI Colors](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/foundation/ai-colors)
Apply the AI color palette for embedded AI and Joule.
+----------------------------------------------------------x-----------------------------------------------------------+
[AI Icon](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/foundation/ai-icon)
Use the AI icon to let users know where embedded AI features are available.

**Metadata**

Title

Breadcrumbs
Foundation

visibility

---

## Guidelines > Explainable Ai Building Explanations

**Design System Hero**

# Explainable AI (XAI) – Building Explanations

## Intro

This page explores how you can create local and global explanations for different progressive disclosure levels.

At the end of the page, you’ll find a series of work-in-progress examples and a checklist that highlights the key takeaways for explainable AI.

Before you start designing explanations, review the [explainable AI overview](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/explainable-ai-overview) to get familiar with the concepts and terms we use. Make sure you also understand the [guiding principles](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/explainable-ai-principles) before moving forward.

## Explanation Levels

We distinguish between **global explanations**, which cover the entire dataset, and **local explanations**, which focus on individual AI outputs.

Keep in mind that “global” and “local” have different meanings here than in some other design patterns.

- When you group multiple AI outputs in a table, graph, or similar format, this still counts as a local explanation.
- A global explanation applies to the entire model, no matter which output instance you look at. As users become more familiar with SAP AI policies, their need for global explanations usually goes down, since they no longer require as much high-level context.

#### &#x20;Local and Global Explanation Scenarios

**Table**

Explanation Level | Explanation Scenario                                                           | Example Explanation

Local (Single)    | “Why did **this candidate** get rejected?”                                     | “The candidate was not shortlisted
| because their experience didn’t match
| the required programming skills.”

Local (Group)     | “Why were **these three candidates** rejected, but the other two shortlisted?” | Show a table with candidate scores
| for skills, years of experience, and
| cultural fit. Highlight the factors
| that led to rejection for each
| candidate, and the attributes that
| contributed to selection for the
| others.

Global            | “What’s the **hiring policy** overall?”                                        | “In general, the AI model ranks
| candidates based on skills, years of
| experience, and education level.”

**> **Guideline:** **

Plan for global explanations when users need to understand the overall system behavior, not just a single AI output.

## Progressive Disclosure Levels – Overview

Progressive disclosure helps you present explanations that match your users’ needs without overwhelming them. Depending on the situation, users may require different amounts of information to understand an AI output. The right level of detail depends on the type of AI, the usage context, the user’s task, and their role.

We define up to four progressive disclosure levels, from no explanation (Level 0) to an extended, detailed report (Level 3):

**Table (col-width-10-20-50-20)**

Level   | What’s Provided?                  | Purpose                     | Typical UI Elements

Level 0 | No explanation                    | Users don’t expect or       | None
| require an explanation for
| an AI output.
Level 1 | Explanation indicator (**What?**) | The minimum explanation     | Icons, badges, or other
| level required whenever AI  | markers
| (ML or LLM) outputs are
| provided. The indicator
| also acts as an access
| point to further
| explanation layers.
Level 2 | Simple explanation (**Why?**)     | A summary that provides the | Popover or inline summary
| main reasons behind the
| output. The simple
| explanation can include
| visual or textual
| highlights, as well as
| links to other explanation
| levels.
Level 3 | Detailed explanation (**How?**)   | A comprehensive view        | Overlay, dedicated page or
| designed for advanced       | app
| users, high-risk scenarios,
| or edge cases. This level
| covers all aspects
| processed by the
| intelligent system,
| including AI performance,
| rationale, supporting data,
| and audit-related
| information.
Progressive disclosure works best for local explanations, where users start with a simple indicator and can drill down for more detail.

### How It Works

**Level 1**\                                                                                          | **Level 2**\                                                                                           | **Level 3**
**Explanation indicator**                                                                             | **Simple explanation**                                                                                 | **Extended explanation**
*Local explanation indicator in lists and tables*                                                     | *Local explanation popover, conversation items*                                                        | *Local explanation page*
*Local explanation indicator for cards*                                                               | *Overlay*                                                                                              | *Dedicated explanation application*

**Level 1**: Users encounter the explanation indicator wherever AI outputs are presented, such as in lists or cards.

**Level 2:** By selecting the indicator, users can open a condensed explanation, usually as a popover, overlay, or inline expand. This view should help clarify the AI proposal with relevant context and highlights.

**Level 3:** For users who need full transparency – such as experts conducting audits or users operating in a high-risk domain – a further link gives access to the most detailed level. Level 3 provides extended information and may use overlays or open in a separate page or flexible column layout.

**> **Guideline:** **

- Always include at least Level 1 for any AI-generated result.
- Adjust the initial explanation level based on risk, user role, and context. In high-risk scenarios, consider linking directly from Level 1 to Level 3.
- Users should decide how much detail to access at each step – don’t force deeper disclosure unless necessary for compliance or risk management.
- For global explanations, provide a summary of the overall system or model behavior – typically as a Level 3 explanation. Over time, as users become more familiar with AI
policies, demand for these global explanations usually decreases.
- Explanations should stay attached to the relevant conversational turn for as long as the thread remains accessible, ensuring clarity and traceability.
- In contexts with higher risk, it is advisable to also include timestamps to provide additional accountability.
- Use [seamful design](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/explainable-ai-principles#seamful-design) to empower users.

The sections below look at each of these explanation levels in more detail.

## Disclosure Level 1: Explanation Indicator

Use the explanation indicator to mark elements or combinations of elements created or manipulated with the help of AI. It gives users context about the nature and quality of the service. When users click the indicator, show a more detailed explanation (Level 2).

An explanation indicator is a form of AI notice. For more information, see [AI Notice User Research](https://sap.sharepoint.com/sites/206415/Lists/User%20Studies/DispForm.aspx?ID=604\&e=KhBG4c) in the User Research Library.

The following sections describe the explanation indicator variants and when to use them.

### Explanation Type

Local explanation indicators can apply for a **group** of items or a **single** item. This affects both the type of information they contain and their placement on the UI.

**Table**

Local Group Indicator

Explains a collection of AI outputs.
*Example: Use a local single indicator on
individual cards to explain each output directly.*
*Example: Use a local group indicator above a table or list to explain the individual outputs in that collection.*
Poorly worded or overly technical explanations damage trust. Ensure that local explanations follow human-centered principles and are tailored to the user’s role. For more details on voice and language, [see the user assistance guidelines](https://www.sap.com/design-system/btp/writing-guidelines/basics/basics-of-ua/overview/).

### Indicator Style

The styling of the indicator influences how the user perceives and interprets the displayed output. We distinguish between a **default style** and an **extended style**.

**Table**

Default Style

The default style provides the minimum indication about
the type of AI output. It uses explicit, descriptive
labels and blue coloring for clickable explanations.
Use this style for non-critical AI applications.
or want to emphasize the importance of the information.

**> **Guideline:** **

- If users need to be fully aware of the nature and quality of the output from the start, use the extended style with
semantic colors for the explanation indicator.
- Don’t use decorative AI icons (such as robot heads or brain symbols) to show that the result came from machine
learning or a large language model. They don’t improve understanding. Instead, use the SAP Design System to create
accessible explanation indicators.

### Explanation Indicator Patterns / Examples

To help you understand XAI concepts in practice, this section shows illustrative scenarios and example explanation indicators. These are conceptual examples, not technical specifications. They show how explanations can be represented in a design.

For visual design specifications – colors, spacing, typography, or component usage – see the official [Visual Core](https://wiki.one.int.sap/wiki/display/visualcore/Horizon) guidelines. This ensures consistency with the SAP Design System and avoids duplicating technical guidance.

*Note: This version of the guidelines does not include equivalent design patterns for global explanations. Future iterations will add them.*

**Table**

Scenario               | Pattern                       | Examples

Local group indicator  | Ranking for table items       | A “View Ranking Criteria” link in the
| toolbar shows the factors used to
| sort the items, such as price and
| delivery time.

Local single indicator | Predicted priority of an item | A table column labeled “Recommended
| Priority” contains values like “Very
| High” or “Low.” Can include a numeric
| score to support the label.

Local single indicator | Quality classification        | A product has a tag indicating the
| predicted quality (such as
| “Premium”), based on the model
| output.

Local single indicator | Price prediction              | A column labeled “Predicted
| Achievable Price”
| Example: “100 EUR (\+/- 10%).”

### Styling Conditions

The length of the explanation indicator and whether you display a link to a simple explanation (Level 2) depends on your use case:

**Table**

Form Factor                 | Length              | Action       | Conditions

**All form factors**\       | **Short** (default) | Display only | The user’s display
S, M, L, XL, larger than XL |                     |              | permission is limited to
|              | Level 1.
|              | **or**
|              | Level 2 explanation is
|              | missing.

**Large**\                  | **Long** (optional) | Clickable    | The user has display
L, XL, larger than XL       |                     |              | permission for Levels 1 and
|              | 2\.
|              | **and**
|              | Level 2 explanation is
|              | available.

**> **Guideline:** **

Display clickable explanation indicators if:
- The context is explained in more detail in Level 2.
- The user needs access to the Level 2 explanations and has the appropriate authorization.
Ensure that the length of the explanation indicator is suitable for the screen size. To prevent truncated explanation indicators, apply the following rules:
- If there is sufficient space and no collision with other UI elements, use the optional long style.
- If you are listing criteria, show 3 criteria and use the ellipsis to indicate that there are more. If there is not enough space to show 3 criteria, use a short explanation indicator or allow the user to open
Joule in full screen mode.
***:decline:**&#x52;anked By: Price, De…*
***:accept:** Ranked By: Price, Delivery Time, Minimum Order Quantity, …*
- If you use the long style, always offer a fallback to the default short indicator for smaller screens or form factors.
- If you have no other options to free up space on the UI (for example, by moving other actions into the overflow), wrap the text.
For more information about responsive and adaptive design, see [Multi-Device Support](https://www.sap.com/design-system/fiori-design-web/discover/sap-design-system/vision-and-mission/responsiveness-adaptiveness).

## Disclosure Level 2: Simple Explanation

### Accessing Explanations

Users must be able to access an explanation directly from the explanation indicator. The interaction model (such as a popover, walkthrough, or assistant) is still under review as part of ongoing research and design work. No matter which interaction you use, make sure the explanation space offers contextual information that helps users understand the AI output at the right level – local or global. Include key factors, inputs, or criteria that influenced the result.

### Explanation Elements

Explanation popovers, screen overlays, or conversational items like [Joule](https://www.sap.com/products/artificial-intelligence/ai-assistant.html) can include the following elements:

**Table**

Explanation Element

Header title

Minimum content
For AI outputs shown on a scale (such as risk, priority, or probability), a **key or legend** that clarifies how to interpret the current value.

Recommended content
**Timestamp** indicating when the result or prediction was computed; for time-critical outputs, an indication of the last update.
List of **the three to five most important parameters** influencing the result, which may include a comparison with averages or reference values.

Optional content
prediction accuracy. This may be combined with performance indicators or a trend.
**In-place feedback components** for collecting explicit user feedback.

Level 2 – explanation elements

Level 2 – example of explanation elements (1)

Level 2 – example of explanation elements (2)

**> **Guideline:** **

#### Structure
Limit the breakdown to three to five factors, unless there’s a critical reason to include more, such as in a high-risk use case. More detail can make content harder to navigate and may prompt additional questions or cross-checks.
For a consistent experience, follow the suggested structure above.
#### Content
Make it easy to identify the most relevant information:
- Choose the most suitable format for conveying information – language, visual elements, or both.
- In longer texts, emphasize important information so users can scan content quickly.
- Use text formatting and visuals purposefully, and not just for decoration.
- Restrict text explanations to no more than three short sentences.
Reveal information progressively:
- Add value with each disclosure and avoid simply repeating information from previous levels.
- Make sure that the information on each level is self-contained and that all elements form a natural flow.
For general guidance on wording, see the [UI Text Guidelines for SAP Fiori Apps](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/ui-text-guidelines-for-sap-fiori) in the SAP design system.

### Natural Language Explanations

Natural language explanations are a human-centered approach to AI explanations that apply conversational interaction principles as they are used in conversational interfaces. Reasoning and relationships appear as sentences in non-technical language, making explanations easier for users to interpret (see [The Two Main Goals of Explainability](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/explainable-ai-principles#the-two-main-goals-of-explainability)).

The use of natural language explanations is limited to explanation popovers and screen overlays, explanation pages (see [progressive disclosure](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/explainable-ai-building-explanationsi#overview-of-progressive-disclosure-levels)), recommendation items, and the [Joule AI copilot](https://www.sap.com/products/artificial-intelligence/ai-assistant.html).

The table below provides examples of natural language explanations.

**Table**

Objective

Add value at each disclosure level
*Ranked By: Price, Delivery Time, Minimum Order Quantity, …*
**Level 2:**
:accept: *The price has the biggest impact on the score, followed by the delivery time and then the minimum order quantity.*
:decline: *Suppliers are ranked by price, delivery time, and minimum order quantity.*

Specific information
:decline: *Best price with lowest minimum order quantity. Delivery takes longer than average.*

Just enough formatting
:decline: *This is **high priority** because the **net payment** is due soon (**in 3 days**) and the **amount** is **small** (**1.200,00 USD**). Customer Electronics usually pays **on time**.*

**> **Guideline:** **

- Use natural language to summarize the overall situation and to explain dependencies, origins, or principles.
- To display the simple description, we recommend using plain text.

## Disclosure Level 3: Extended Explanation

You can offer users a more in-depth analysis by providing an extended explanation page, tailored to their role and the risk level of the use case. You can direct users to a separate, dedicated application or add an extra page within your own app. The decision depends on how much control and insight you want to provide for the technology in use. In most cases, extended explanations serve a unique use case and require a separate implementation.

**Explanation Page**
*Detail explanation page in a flexible column layout*

**> **Guideline:** **

- Provide links from explanation level 2 to the extended explanation page or app only to users with appropriate roles
(role-based access). AI analysis is usually relevant only for roles like data scientists or system owners, so offer
detailed explanations on a need-to-know basis.
- Limit exposure for general users. Don’t give regular business users access to these links, since detailed AI
analysis is rarely needed for their tasks.
- In high-risk scenarios or edge cases, be aware that any user might need to move directly from level 1 to level 3.
- Account for exceptions. Certain roles, such as developers, may not be decision makers but could still require
detailed explanations for troubleshooting or integration purposes.

## Examples

The examples below show different explanation scenarios.

These images are **illustrative only**, early-stage / beta / work-in-progress examples to support understanding, not final design specifications.

### SAP SuccessFactors

Explanation in SAP SuccessFactors

**Explanation level:** Local
**Explanation type:** Rationale
**Explanation content:** Source
**Progressive disclosure level:** 2 – simple explanation
**User role:** Impacted users

Read the full article on this use case in the [SAP Community Blog](https://community.sap.com/t5/technology-blog-posts-by-sap/sap-ux-q3-2025-update-part-3-beta-ai-innovations-in-sap-s-4hana-cloud/ba-p/14173657).

### Joule Chat Interface

Explanation in Joule chat interface (work in progress)

**Explanation level:** Local
**Explanation type:** Rationale
**Explanation content:** Source
**Progressive disclosure level:** 2 – simple explanation
**User role:** Impacted users

### SAP Deep Research and Planning Agent (1)

Initializing orchestration – information in Joule (work in progress)

### SAP Deep Research and Planning Agent (2)

Task updates – information in Joule (work in progress)

### SAP Deep Research and Planning Agent (3)

Task completion – information in Joule (work in progress)

### SAP Deep Research and Planning Agent (4)

Task breakdown – information in Joule (work in progress)

### SAP Deep Research and Planning Agent (5)

Task detail – explanation in Joule (work in progress)

**Explanation level:** Local
**Explanation type:** Data and rationale
**Explanation content:** Source
**Progressive disclosure level:** 3 – extended explanation
**User role:** Producers of explanations, ethicists and impacted users

### SAP Deep Research and Planning Agent (6)

Completed task – information in Joule

## Top Tips

This section summarizes the most important XAI principles and guidelines.

Before you start with your design, conduct research to figure out the answers to the questions below. If user research is not an option, use [a heuristic evaluation method](https://sap.sharepoint.com/sites/206103/SitePages/Understand%20research/Heuristic%20Evaluation.aspx) as outlined in the [SAP User Research Portal SharePoint](https://sap.sharepoint.com/sites/206103) to test your design. This should be the minimum investment.

**Keep explanations human-centered**

- Write in plain language and avoid jargon.
- Tailor explanations to the user’s role (decision maker, impacted user, producer, ethicist).

**Use progressive disclosure**

- Start with simple explanations (Level 1 – indicator).
- Offer additional context when needed (Level 2 – popover or overlay).
- Provide detailed analysis only for advanced users or high-risk cases (Level 3 – extended page or app).

**Match explanation level to risk**

- Low risk: Lightweight explanations (indicators, optional details)
- Standard risk: Add rationale and key influencing factors
- High risk: Offer extended explanations including transparency, sources, and timestamps

**Support both local and global perspectives**

- Local: Explains why a specific output happened (for example, candidate rejection).
- Global: Describes how the system generally works (for example, hiring policy).
- Grouped local explanations, such as tables or charts, are still local rather than global.

**Design for understandability and intervenability**

- Explanations should help users make sense of outputs (understandability).
- Explanations should empower users to act, contest, or adjust (intervenability).

**Use accessible, consistent indicators**

- Don’t rely on color alone – combine text, icons, or labels for clarity.
- Avoid decorative “AI” icons, such as robot heads or brain symbols.
- Follow the SAP design system for styling and components.

**Apply seamful design when needed**

- Show limitations instead of hiding them.
- Add friction for high-stakes actions (for example, by adding pauses or requiring confirmation).
- Reveal seams in ways that help build [calibrated trust](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/explainable-ai-principles#calibrated-trust-scale) without overwhelming users.

**Always respect privacy and ethics**

- Follow the [SAP AI Ethics Policy](https://sap.sharepoint.com/teams/SAPOneAssets/Library/company_policies_and_guidelines/Global_AI_Ethics_Policy_English.pdf) and [Agentic AI Ethics Guidelines](https://sap.sharepoint.com/teams/AISecurity-CoE/SitePages/Agentic-AI-Ethics-Guidelines.aspx).
- Ensure explanations don't expose sensitive data unnecessarily.
- Make fairness and accountability visible when relevant.

---

## Guidelines > Explainable Ai Overview

**Design System Hero**

# Explainable AI (XAI) – Overview

## Intro

To help users trust AI, it’s important to provide enough information about the model behind it and explain how and why it produces certain results.

This guideline outlines our approach to explainable AI and is organized into three separate pages:

- [Overview](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/explainable-ai-overview)
  Understand why explainable AI matters, its main goals, and the terminology we use.
- [Guiding Principles](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/explainable-ai-principles)
  Learn the fundamentals for designing explanations. This section also provides a list of resources where you can find more details.
- [Building Explanations](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/explainable-ai-building-explanations)
  Learn how to apply progressive disclosure levels for explanations. You’ll also find examples, as well as top tips that summarize all the important points.

Explanation in SAP SuccessFactors (work in progress)

## Why Explainable AI?

Explainable AI (XAI) isn’t just a nice-to-have design feature. Laws require you to provide human oversight for AI outputs, especially in high-risk situations. You can find more details about risk and legal requirements in the [SAP AI Ethics Handbook](https://www.sap.com/products/artificial-intelligence/ai-ethics.html?pdf-asset=7211ee96-647e-0010-bca6-c68f7e60039b\&page=1) on SAP.com and in [SAP’s AI Ethics Policy](https://sap.sharepoint.com/teams/SAPOneAssets/Library/company_policies_and_guidelines/Global_AI_Ethics_Policy_English.pdf) on SharePoint.

An explanation doesn’t just lay out technical processes. It also needs to make sense to users and work in their daily context. SAP’s approach to XAI is human-centered (HCXAI), which means you should design explanations with the end user in mind. For more about HCXAI, see [SAP’s research findings](https://sap.sharepoint.com/sites/206415/Lists/User%20Studies/DispForm.aspx?ID=674\&e=dby1Iz) on explainability in the [SAP user research library](https://sap.sharepoint.com/sites/206415/SitePages/Home.aspx).

In short, explanations should:

- Be human-centric, concise, glanceable, and tailored to the user’s role where possible.
- Enable data transparency by providing explanations with an appropriate level of detail.
- Use global explanations to prioritize ethics and privacy, which SAP business users highlight as top concerns.
  For the full list of ethical and responsible AI principles, see [SAP’s AI Ethics Policy on SharePoint](https://sap.sharepoint.com/teams/SAPOneAssets/Library/company_policies_and_guidelines/Global_AI_Ethics_Policy_English.pdf).
- Follow the [Agentic AI Ethics Guidelines on SharePoint](https://sap.sharepoint.com/teams/AISecurity-CoE/SitePages/Agentic-AI-Ethics-Guidelines.aspx).
  Example: “Human-in-the-loop” (HITL) as a core ethical safeguard.

Although these guidelines focus on design best practices and policies, you should also use the inclusive research methods described in the [Inclusive Research Handbook](https://www.sap.com/documents/2023/11/24adccec-967e-0010-bca6-c68f7e60039b.html) on SAP.com. This ensures human-centered XAI reflects the needs of all users and promotes equity. As a designer, you’ll benefit from this foundation when creating explanations for diverse audiences.

## XAI Terminology

These guidelines use the terms below to describe the explainable AI framework.

**Table**

Term

Explainable artificial intelligence (XAI)
reached a result, what actions it took, why its insights or recommendations
matter for the user’s task, and what measurable impact is expected. This also
includes details about the model, reasoning, data, APIs, and other data
sources used.

Human-centered explainable artificial intelligence
(HCXAI)
social values.
See: [Explainable AI Reloaded: Challenging the XAI Status Quo in the Era of
Large Language Models](https://arxiv.org/pdf/2408.05345v2).

Explainable

Interpretable

Understandable

Intervenable

Explanation level: Local (single)
response.

Explanation level: Global
model training data, or tool stakeholders.

Role: Decision maker
who use AI to make decisions for or about others.

Role: Producer of explanations

Role: Ethicists
accountability, and ethical concerns surrounding AI tools, and ensure compliance
with relevant standards.

Role: Decision subjects
tools themselves.

---

## Guidelines > Explainable Ai Principles

**Design System Hero**

# Explainable AI (XAI) – Guiding Principles

## Intro

This page covers core principles and widely accepted best practices for explainable AI, or XAI. These concepts form the foundation for crafting your own explanations.

#### Related Guidelines

- To get an introduction to explainable AI and the terms we use, check out [Explainable AI (XAI) - Overview](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/explainable-ai-overview).
- To learn about the explanation components in detail, see [Explainable AI (XAI) - Building Explanations](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/explainable-ai-building-explanations).

## Designing for Trust

Building trust is essential when designing AI-powered tools. In this section, you’ll learn how to assess and support the right level of user trust in your application by using a calibrated trust scale and following practical guidelines.

### Calibrated Trust Scale

A calibrated trust scale in explainable AI helps you understand how users perceive and respond to system recommendations or decisions. The scale lets you identify if users place too little, too much, or just the right amount of trust in AI – especially after they see its explanations.

The scale usually includes three levels:

- **Distrust**: Users don’t trust the AI’s outputs and may ignore useful suggestions.
- **Calibrated trust**: Users’ trust matches the AI’s real capabilities, so they rely on it appropriately.
- **Over trust**: Users put too much confidence in the AI and might follow its recommendations even when they aren’t correct.

Calibrated trust scale. Distrust quotation from [BBC News](https://www.bbc.com/news/articles/c2l799gxjjpo). Over trust quotation from [SAP research on AI Notice](https://sap.sharepoint.com/sites/206415/Lists/User%20Studies/DispForm.aspx?ID=604\&e=KhBG4c) in the user research library.

### Building Trust: “How Might We” Checklist

To help users develop the right level of trust in your AI tools, use the “how might we” checklist below. These guidelines reflect the current academic consensus on building effective and trustworthy AI explanations.

**Table**

Guideline

Evaluate trade-offs

Complement with XAI methods
explainability.

Understand dependencies

Align explanations with the user’s goal

Provide meaningful explanations

Calibrate user trust

Empower and educate users

Structure explanations
1\) What happened?
2\) Why did this happen?
3\) How did this happen?
4\) What if…?

Tailor to the user’s role

Ensure understandability

Enable user intervention

Make explanations easy to access

Protect privacy and security

Be transparent about gaps or uncertainty

For more guidance on using “how might we” statements, see [Innovation for Scalable Impact](https://sap.sharepoint.com/teams/DesignforScalable/Lists/Method%20Store/DispForm.aspx?ID=23\&e=x0ALTG) on SharePoint.

## Risk Level Framework

The scope and content of the explanations you need to provide depend on the inherent risk level of the use case. Use the [AI Use Case Impact Assessment](https://forms.office.com/pages/responsepage.aspx?id=bGf3QlX0PEKC9twtmXka9zf8tKw_q5tKgiS22ce24yJUMkFGOTBOWURSTFhGWllKUEpISVRZNDBGWiQlQCN0PWcu\&route=shorturl) to determine the risk level for each use case.

**Table**

Risk Level         | SAP AI Ethics definition    | Why It’s important                                                                                                                                                                                                                                                       | Examples

Redline/prohibited | Use of AI for this purpose  | AI Ethics Policy, p. 11: “AI systems must not have any harmful impacts on users.”                                                                                                                                                                                        | Human surveillance
is highly unethical. If     |
your use case is built for  | AI Ethics Policy, p. 13: “Negative social, economic, and environmental impacts must be avoided.”                                                                                                                                                                         | Social scoring
a redline purpose, you must |
**immediately** stop        | For full details, see the [SAP AI Ethics Policy](https://sap.sharepoint.com/teams/SAPOneAssets/Library/company_policies_and_guidelines/Global_AI_Ethics_Policy_English.pdf) on SharePoint.                                                                               | Deliberate discrimination
developing, deploying, or   |
selling it.\                |                                                                                                                                                                                                                                                                          | De-anonymizing data that
\                           |                                                                                                                                                                                                                                                                          | was previously anonymized
The solution involves       |
inherent risks that could   |                                                                                                                                                                                                                                                                          | Foreseeable harm or
negatively impact society   |                                                                                                                                                                                                                                                                          | development of tools to
or is designed with this in |                                                                                                                                                                                                                                                                          | manipulate individuals or
mind.                       |                                                                                                                                                                                                                                                                          | groups
|                                                                                                                                                                                                                                                                          | Undermining public debate
|                                                                                                                                                                                                                                                                          | or democratic elections
|                                                                                                                                                                                                                                                                          | Environmental harm

High<sup>1)</sup>  | AI used in a similar way to | High risk use cases require a high degree of transparency for accountability and oversight.                                                                                                                                                                              | Processing personal
AI solutions that have led  |                                                                                                                                                                                                                                                                          | information
to negative consequences    | Requires a continuous cycle of internal and external auditing.
for individuals or whole    |                                                                                                                                                                                                                                                                          | Automated decision making
populations in the past.    |
|                                                                                                                                                                                                                                                                          | Consequences for people,
Your use case has potential |                                                                                                                                                                                                                                                                          | either direct or indirect
consequences for people,    |
whether negative or         |                                                                                                                                                                                                                                                                          | Categorizing people
positive.                   |
|                                                                                                                                                                                                                                                                          | Management and operation of
|                                                                                                                                                                                                                                                                          | critical infrastructure
|                                                                                                                                                                                                                                                                          | Employment and HR
|                                                                                                                                                                                                                                                                          | Healthcare
|                                                                                                                                                                                                                                                                          | Private services, public
|                                                                                                                                                                                                                                                                          | services and benefits
|                                                                                                                                                                                                                                                                          | Law enforcement
|                                                                                                                                                                                                                                                                          | Migration
|                                                                                                                                                                                                                                                                          | Democratic processes

Standard/Low       | Use cases that involve      | Consider the user roles and scenarios present in the use case and the types of local explanations users will expect.                                                                                                                                                     | Chatbots answering
minimal potential for harm  |                                                                                                                                                                                                                                                                          | frequently asked questions
or adverse consequences.    | Set up a feedback system to identify which types of explanations are most useful, based on [SAP multi-agent system research findings](https://sap.sharepoint.com/sites/206415/Lists/User%20Studies/DispForm.aspx?ID=315\&e=Fu5mmo) in the user research library.
|                                                                                                                                                                                                                                                                          | Automatic content
| Use *Principle 6: Human oversight and determination* from the [SAP Global AI Ethics Policy](https://sap.sharepoint.com/teams/SAPOneAssets/Library/company_policies_and_guidelines/Global_AI_Ethics_Policy_English.pdf) as the guiding principle for global explanations. | summarization
|                                                                                                                                                                                                                                                                          | Internal knowledge base
|                                                                                                                                                                                                                                                                          | assistants
|                                                                                                                                                                                                                                                                          | Personalized learning
|                                                                                                                                                                                                                                                                          | suggestions

<sup>1)</sup> High-risk use cases aren’t prohibited within SAP. However, you must first submit them to the AI Ethics steering committee for assessment before you develop, deploy, or sell them. The AI Ethics team uses sub-classifications of high-risk use cases to determine the evaluation cycle your use case will follow.

## XAI User Roles

The literature on explainable AI describes various user roles in relation to explainability. For these guidelines, we’ve combined several taxonomies to create an aggregated list of user roles that impact or are impacted by XAI. Treat these XAI-specific roles as an extra layer on top of your existing line of business personas. Real-world deployments will often reveal additional roles as you define edge cases.

As a high-level guide, here are the main XAI user roles you should consider:

**Table**

User Role                             | Definition                           | Examples
+-------------------x-------------------+--------------------------------------+---------------------------------------+
Institutions that deploy automated   | SAP, Salesforce, Meta, Google
decision pipelines and who are under
Decision Maker                        | an obligation to explain the output
to end-users.
People who decide whether and how AI | CTO, IT manager
systems are adopted, integrated,
evaluated, purchased, deployed, and
monitored.
People who use AI to make decisions  | Recruiter, doctor
for or about others.
Producer of Explanations (Builders)   | People who directly design and build | AI development, Joule development,
AI systems and their explanation     | knowledge graph, LoB team, AI
mechanisms.                          | practitioner, user researcher,
| conversation designer, user
| assistance developer

Ethicists                             | People with domain expertise who     | Policymaker, auditor, consultant to a
focus primarily on fairness,         | decision maker
transparency, accountability, and
ethical concerns surrounding AI
tools.
Impacted Users (Consumers): End Users | People who interact directly with AI | \-
outputs and explanations for their
own purposes.
Impacted Users (Consumers):  Decision | People who don’t interact directly   | People receiving a medical diagnosis
Subjects                              | with AI systems but are still        | produced by AI, people whose loan
affected by the outputs.             | requests are approved or denied based
| on AI analysis, business users who
| receive reports generated by AI

The third type of decision maker – such as a doctor or recruiter – might seem different from an institution or an IT manager. However, this person also makes decisions on behalf of others, just on a smaller scale. This sets a decision maker apart from end users, who rely on AI for their own purposes. For an end user, the consequences of an AI-supported decision mainly affect that user directly, while a decision maker’s choices impact other people.

**Table**

Role           | Definition                          | Key Impact

Decision Maker | Someone who uses AI outputs to make | The use of AI by this person has **consequences for other people**.
decisions for or about others.
End User       | Someone who uses AI outputs to make | The use of AI by this person has **consequences for themselves**.
decisions for themselves to support
their work
## The Anatomy of an Explanation

When an explanation is both explainable and interpretable, it becomes understandable. Making explanations understandable is a key goal of XAI. The diagram below comes from a presentation to the SAP engineering ecosystem. You can read the [slide deck on FigJam](https://www.figma.com/slides/7TgFZnaFhjKuVUWMpDB7OT/JXAI-Ecosystem-Share-out?node-id=4039-513\&t=0gTR58kMGjat6yeb-1), access the [full recorded presentation](https://sap-my.sharepoint.com/:v:/r/personal/klaus_haeuptle_sap_com/Documents/Recordings/Ecosystem%20What%20Will%20It%20Take%20to%20Design%20and%20Operationalize%20Responsible,%20Human-Centered%20Explainable%20AI%20\(HCXAI\)%20Opportunities%20and%20Challenges%20for%20Joule%20and%20Multidisc-20250731_150112-Meeting%20Recording.mp4?csf=1\&web=1\&e=SWnjRB\&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D), or find related [SAP research findings](https://sap.sharepoint.com/sites/206415/Lists/User%20Studies/DispForm.aspx?ID=674\&e=dby1Iz) on explainability in the user research library.

Venn diagram showing the anatomy of an explanation

### The Two Main Goals of Explainability

AI explanations address two main goals that form the foundation of explainable AI: **understandability** and **intervenability:**

**Table**

Key Goal          | What It Means        | Key Question Answered | Purpose               | Examples

Understandability | Helps users *make    | *“What happened and   | Builds confidence and | Present the factors
sense of what the AI | why?”*                | trust in AI outputs,  | that influenced a
is doing*            |                       | and is especially     | recommendation in
|                       | important in          | plain language
|                       | high-risk scenarios
Intervenability   | Helps users *take    | *“What can I do about | Empowers users to     | Provide an option to
action when needed*  | it?”*                 | monitor, correct,     | override an AI
|                       | contest, or           | decision or request a
|                       | troubleshoot AI       | human review,
|                       | decisions, supporting | enabling human agency
|                       | user autonomy
**Why These Goals Matter**

**Table**

Goal              | What It Means                 | Why It Matters

Understandability | Users understand AI outputs   | Builds adequate trust and confidence. See [Designing for Trust](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/explainable-ai-principles#designing-for-trust).

Intervenability   | Users can act on AI decisions | Ensures user control and agency

For more details on measuring adequate trust, see the research findings on [AI trust scores](https://sap.sharepoint.com/sites/206415/Lists/User%20Studies/DispForm.aspx?ID=841\&e=oapaFH) in the [SAP user research library](https://sap.sharepoint.com/sites/206415/SitePages/Home.aspx).

### Explanation Types

The [EU GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) and [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689) on EUR-Lex set key obligations for transparency, interpretability, and human oversight, but neither outlines a detailed taxonomy of explanation types. However, the UK GDPR highlights six main explanation types that cover both local and global levels:

**Table**

Explanation Type                       | Description                  | Purpose

**Rationale** explanation              | Reasons behind decisions,    | Challenge decisions, change behavior
non-technical
**Responsibility** explanation         | Accountability and contact   | Challenge decisions, traceable
information                  | accountability, provide information

**Data** explanation                   | Data used in decisions       | Challenge decisions, reassurance

**Fairness** explanation               | Efforts to mitigate bias     | Challenge decisions, reassurance

**Safety** and performance explanation | Reliability and robustness   | Challenge decisions, provide
| information, reassurance, help users
| gain understanding or confidence

**Impact** explanation                 | Effects on users and society | Help users understand impact or
| consequences, human in control,
| reassurance

### Explanation Content

An AI explanation isn’t a fixed attribute. Instead, it’s a multifaceted concept shaped by multiple interrelated components.

**Table**

Explanation Content

Source

Timing

Trigger

Autonomy

Content
1\) Sensitivity
2\) Personal data
3\) Confidentiality
4\) Minimum content

Level (scope)

Criticality

Goal(s)

Intended recipient

## Progressive Disclosure

Progressive disclosure in explainable AI means presenting information in layers, starting with simple, high-level explanations. Users can then access more detailed or technical information if they want to. This method helps avoid overwhelming users with complexity and aligns explanations with the user’s needs and expertise.

For more information, see [Progressive Disclosure Levels](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/explainable-ai-building-explanations#progressive-disclosure-levels).

## Seamful Design

Traditional UX often aims for seamlessness: removing friction, hiding complexity, and smoothing transitions. However, in AI-driven systems, seamlessness can lead to opacity, false trust, or user disempowerment. Seamful design takes a different approach by acknowledging imperfection and supporting users in building a realistic mental model of how the system works.

Seamful design is useful when a system shows expected or unexpected limitations, and there’s a risk of over- or under-reliance. This approach plays a key role in developing [calibrated trust](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/explainable-ai-principles#calibrated-trust-scale) and understanding what a tool can and can’t do.

Rather than hiding seams, seamful design turns these moments into design patterns that are integral to the solution. This empowers users to decide when and how to engage with limitations. However, it’s important to reveal system limitations at a level of detail that’s appropriate for the context.

**Table**

Scenario                  | Seam                       | Design Choice              | Example

Deliberate slow-downs     | Fast automation can bypass | Introduce pauses that      | In healthcare
(speed vs. reflection)    | human judgment             | encourage user reflection  | decision-support, the AI
|                            | may require doctors to
|                            | acknowledge critical risks
|                            | before moving forward,
|                            | rather than auto-filling
|                            | recommendations

Require user input before | The AI can’t infer intent  | Add friction by asking for | A financial AI assistant
critical actions          | perfectly                  | clarification or           | might say, “I’ve prepared a
| confirmation before        | wire transfer to X. Please
| high-stakes actions        | review and confirm.”

**> **Guideline:** **

If your use case includes known limitations, strategically disclose them and pair the message with SAP’s ethical
principles to build trust and support user agency.

## Sources

**Table (col-width-50-10-40)**

Title                                                                                                                                                                                                                                                  | Year     | Author(s)

[A typology of explanations to support Explainability-by-Design](https://doi.org/10.1145/3708504)                                                                                                                                                      | 2025     | Niko Tsakalakis, Sophie
| Stalla-Bourdillon, Dong Huynh, and
| Luc Moreau

[What goes into an explanation?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-1-the-basics-of-explaining-ai/what-goes-into-an-explanation/) | 2024     | Information Commissioner’s Office
| (ICO)

[Seamful Design and Ubicomp Infrastructure](https://www.dcs.gla.ac.uk/~matthew/papers/ubicomp2003HCISystems.pdf)                                                                                                                                       | 2003     | Matthew Chalmers

[Seamful XAI: Operationalizing Seamful Design in Explainable AI](https://doi.org/10.1145/3637396)                                                                                                                                                      | 2024     | Upol Ehsan, Q. Vera Liao, Samir
| Passi, Mark O. Riedl, and Hal Daumé

[Explainable AI Reloaded: Challenging the XAI Status Quo in the Era of Large Language Models](https://arxiv.org/pdf/2408.05345v2)                                                                                                                      | 2024     | Upol Ehsan and Mark O. Riedl

[Human-Centered Explainable AI (HCXAI): Beyond Opening the Black-Box of AI](https://doi.org/10.1145/3491101.3503727)                                                                                                                                   | 2022     | Upol Ehsan, Philipp Wintersberger, Q.
| Vera Liao, Elizabeth Anne Watkins,
| Carina Manger, Hal Daumé Iii, Andreas
| Riener, and Mark O Riedl

[“Explanation” is Not a Technical Term: The Problem of Ambiguity in XAI](https://doi.org/10.48550/arXiv.2207.00007)                                                                                                                                    | 2022     | Leilani H. Gilpin, Andrew R. Paley,
| Mohammed A. Alam, Sarah Spurlock, and
| Kristian J. Hammond

[Explainable Artificial Intelligence (XAI): What we know and what is left to attain Trustworthy Artificial Intelligence](https://doi.org/10.1016/j.inffus.2023.101805)                                                                                 | 2023     | Sajid Ali, Tamer Abuhmed, Shaker
| El-Sappagh, Khan Muhammad, Jose M.
| Alonso-Moral, Roberto Confalonieri,
| Riccardo Guidotti, Javier Del Ser,
| Natalia Díaz-Rodríguez, and Francisco
| Herrera

[The Need for Interpretable Features: Motivation and Taxonomy](https://arxiv.org/pdf/2202.11748)                                                                                                                                                       | 2022     | Alexandra Zytek, Ignacio Arnaldo,
| Dongyu Liu, Laure Berti-Equille,
| Kalyan Veeramachaneni

[What is AI, how does it work and why are some people concerned about it?](https://www.bbc.com/news/articles/c2l799gxjjpo)                                                                                                                             | 2025     | BBC News

---

## Guidelines

**Design System Hero**

# AI and Joule Design – Guidelines

## AI Design Basics

+----------------------------------------------------------------------------------------------------x----------------------------------------------------------------------------------------------------+
Tiles (plain)
+----------------------------------------------------------------------------------------------------x----------------------------------------------------------------------------------------------------+
[Design Principles for Generative AI](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/design-principles-for-generative-ai)
Follow five guiding principles whenever you design generative AI features.
+----------------------------------------------------------------------------------------------------x----------------------------------------------------------------------------------------------------+
[Building Trust with Generative AI](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/building-trust-with-generative-ai)
Build trust in generative AI by being transparent, giving users control, and preventing bias.
+----------------------------------------------------------------------------------------------------x----------------------------------------------------------------------------------------------------+
[Designing Agentic AI Ecosystems and Experiences](https://www.sap.com/design-system/fiori-design-web/v1-136/foundations/ai-and-joule-design/guidelines/designing-agentic-ai-ecosystems-and-experiences)
Design agentic systems with humans and ethics at the center.

## Crafting AI Experiences

+---------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------+
Tiles (plain)
+---------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------+
[Designing Effective AI Prompts](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/effective-ai-prompts)
Use the prompt patterns and best practices to craft better inputs.
+---------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------+
[Designing Safety into Generative AI Experiences](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/designing-safety-into-gen-ai-experiences)
Prioritize transparency, explainability, user control, and bias mitigation.
+---------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------+
[Designing Sustainable Generative AI Experiences](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/designing-sustainable-gen-ai-experiences)
Consider the environmental, social, and economic impacts of your designs.

## Explainable AI (XAI)

+-----------------------------------------------------------------------------------x-----------------------------------------------------------------------------------+
Tiles (plain)
+-----------------------------------------------------------------------------------x-----------------------------------------------------------------------------------+
[Explainable AI – Overview](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/explainable-ai-overview)
Understand why explainable AI matters, its main goals, and the terminology we use.
+-----------------------------------------------------------------------------------x-----------------------------------------------------------------------------------+
[Explainable AI – Guiding Principles](https://www.sap.com/design-system/fiori-design-web/v1-142/foundations/ai-and-joule-design/guidelines/explainable-ai-principles)
Learn the fundamentals for designing explanations and explore key resources.
+-----------------------------------------------------------------------------------x-----------------------------------------------------------------------------------+
[Building Explanations](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/guidelines/explainable-ai-building-explanations)
Learn how to apply progressive disclosure levels for explanations.

## Situation Handling

+----------------------------------------------------------------------x-----------------------------------------------------------------------+
Tiles (plain)
+----------------------------------------------------------------------x-----------------------------------------------------------------------+
[Situation Handling](https://www.sap.com/design-system/fiori-design-web/discover/sap-products/sap-s4hana-only/situation-handling-guidelines)
Explore the guidelines for the Situation Handling framework.

**Metadata**

Title

Breadcrumbs
Guidelines

visibility

---

## Joule

**Design System Hero**

# Joule

+--------------------------------------------------------------x--------------------------------------------------------------+
Tiles (plain)
+--------------------------------------------------------------x--------------------------------------------------------------+
[Joule Icon](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/joule-assistant/joule-icon)
Learn how to use the icon for SAP's conversational AI panel.

**Metadata**

Title

Breadcrumbs

visibility

---

## Overview

**Design System Hero**

# AI and Joule Design – Overview

+---------------------------------------------------------------------------x----------------------------------------------------------------------------+
Tiles (plain)
+---------------------------------------------------------------------------x----------------------------------------------------------------------------+
[Designing for Generative AI](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/overview/generative-ai-design)
Learn about SAP's generative AI strategy, our approach to developing guidelines, and the foundation guidelines you'll need to get started.
+---------------------------------------------------------------------------x----------------------------------------------------------------------------+
[AI Design Quality Checklist](https://www.sap.com/design-system/fiori-design-web/foundations/ai-and-joule-design/overview/ai-design-quality-checklist)
Use this AI Design Quality Checklist to assess SAP AI experience quality, flag technical follow-ups, and align with the design reviews.

**Metadata**

Title

Breadcrumbs
Overview

visibility

---

