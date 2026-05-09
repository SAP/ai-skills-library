# SAP Fiori Foundations: Writing And Wording

## Ux Writing > Ux Writing For Notifications

**Design System Hero**

# UX Writing for Notifications

## Intro

[Notifications](https://www.sap.com/design-system/fiori-design-web/ui-elements/notification-center/) are system-generated messages that notify users about significant changes in workflows, processes, or data. They inform without interrupting work, and acting on them is optional.

This guideline defines conventions for message structure, tone, terminology, and information placement to promote consistent, clear, and actionable notifications across products.

*Notifications panel*

## Voice and Tone Principles for Notifications

SAP product notifications use the voice of an approachable expert – someone who knows their domain deeply, communicates with clarity, and supports users without overwhelming them. They act as system-level cues within the product, delivering timely and relevant information that helps users stay informed and take action when needed.

Notifications are not marketing copy or conversation starters; they are functional, concise, and purposeful. They are delivered to channels such as the application shell bar or emails based on user settings. The right tone builds trust and reduces cognitive load.

### 1. Serious but supportive

- Communicate urgency and importance without creating anxiety.
- Be clear and straightforward for critical tasks, while staying calm and reassuring for routine reminders and updates.
- Don't use humor, slang, or exaggerated urgency, as they reduce credibility in enterprise environments.

Do
Submit your timesheet by 5 PM today.

### 2. Formal but approachable

- Use professional but conversational tone that’s simple and human.
- Write in second person (“you”), especially when requesting users to act.
- Keep sentences short, active, and free of jargon.

Do
Your expense report is ready for approval.
and requires further action.

### 3. Respectful and reassuring

- Respect users’ time and attention – only surface notifications that are necessary and meaningful.
- Provide enough context to help users make informed decisions.
- Never manipulate with guilt or urgency.

Do
3 invoices are pending review. Approve them to proceed
with payments.
### 4. Consistent and role-aware

- Use terminology consistent with the product domain and the user’s workflow.
- Align tone and language with the user’s level of responsibility (manager, employee, admin).
- Use consistent urgency indicators and phrasing across all notifications (“Action required,” “Due today,” “Completed”).

## How to Write Notifications

Notifications fall into two broad categories based on their purpose:

- **Action-required notifications:** Require users to do something (Reminders, Alerts).
- **Passive notifications:** Inform users without requiring action (Updates).

### Action-required notification principles

#### Reminders

- **Action-oriented:** Clearly state what the user needs to do and by when. Use direct verbs: “Submit,” “Approve,” “Review.”
- **Time-bound:** Include deadlines or urgency markers to create relevance.
- **Contextual:** Specify what the reminder refers to (for example, task name, report period).
- **Non-judgmental:** Avoid guilt-driven language and emotional triggers.
- **Concise:** Keep the message glanceable – ideally under 80 characters.

Do
Submit your timesheet for Week 39 by 5 PM today.
*(vague, no action or context)*
Your quarterly performance review is due tomorrow.
You still haven’t done this—why wait?”
*(judgmental and unhelpful)*

#### Alerts

- **Clarity first:** State what the issue is and the consequences if ignored.
- **Explicit next step:** Make it obvious how to resolve the situation.
- **Transparent priority:** Signal urgency with consistent phrases like “Action Required” or “Immediate Attention Needed.”
- **Contextual relevance:** Only trigger alerts for meaningful disruptions or risks.
- **Avoid panic language:** Communicate urgency without alarming users.

Do
Action required: Purchase Order #990123 is pending
approval.
3 expense claims are overdue. Review them to avoid
payment delays.

### Passive notifications

#### Updates

- **Informative and reassuring**: Clearly state what happened and whether any follow-up is needed.
- **Concise and glanceable**: Communicate in one line or short phrase.
- **Outcome-focused**: Lead with the result (“Completed,” “Available”).
- **Contextual**: Mention the relevant object, task, or system area.
- **Respectful**: Avoid trivial updates or repetitive confirmations.

Do
System maintenance is completed. All services are
operational.
Your expense report was approved. No action is required.
*(unclear outcome)*

## Shell Bar Notifications

Notification item

1. **Title**
2. **Description**
3. **Product name**

### Title

The main message that communicates the core action or update.

- Keep under 40 characters to avoid truncation.
- Use title case.
- Lead with the action or outcome (for example, “Approve PO #990123”).
- Avoid filler words, exclamation marks, or jargon.

### Description

Secondary details that add context.

- Keep under 80 characters for readability.
- Use sentence case.
- Front-load with the most useful supporting detail.
- Test variables for long values to prevent truncation.
- Avoid repeating the title.

## Email Notifications

Email notification – implementation example

1. **Header**
2. **Body**
3. **Buttons (call to action)**
4. **Footer**

### Subject line

The first impression determines if users will open the email.

- Front-load with value: “Approval Needed: PO #990123.”
- Keep under 60 characters to avoid truncation.
- Use urgency sparingly and with context.
- Prefer an active voice for clarity.

### Optional: Header (intro line)

A short text that reinforces the subject line inside the email.

- Align with subject line; no contradictions.
- Keep concise and informative: “Your purchase order requires approval.”
- Avoid marketing-style slogans in transactional emails.

### Body

The main content explains what happened and what action is needed.

- Use structured hierarchy (short paragraphs, bullet points, tables).
- Keep transactional emails under 240 characters.
- Write clearly and role-aware (manager vs. employee vs. admin).
- Avoid jargon or filler phrases.

### Buttons/call to action (CTA)

The primary action that the email is designed to drive.

- Use short, action-driven text: “Approve Request,” “Submit Report.”
- Limit to one primary CTA; add secondary if absolutely needed.
- Keep under 25 characters.
- Avoid vague CTAs like “Click Here.”
- Use title case for buttons.

### Footer

The closing section provides trust, compliance, and navigation.

- Use a consistent SAP footer format: support contact, copyright, terms.
- Include unsubscribe link, preference center, and SAP branding.
- Keep concise and mobile-friendly.
- Separate visually with a smaller font or divider.

## Additional Considerations

### SAP Generic Target Groups

The source text of SAP software is designed for a variety of target groups – decision makers, consultants/implementers, administrators, developers, and users who all have their own unique needs, abilities, and challenges. This can influence the style and tone of voice of content used in the software. 

### SAP Product Standards
Before writing a notification, familiarize yourself with the SAP product standards that are relevant for the user interface. You don't need to know
all product standards and all their requirements. Some requirements apply directly; others are just helpful background. Here are the relevant product
standards:
- [Product Standard for User Assistance](https://url.sap/uaproductstandard-reqs)
- [Product Standard for User Experience Consistency](https://url.sap/ps-uxc) including the [SAP Fiori Design Guidelines](https://url.sap/fioridesign)
- [Product Standard for Accessibility](https://url.sap/ps-acc-reqs) including [Inclusive Design](https://sap.sharepoint.com/sites/127599)
- [Product Standard for Globalization](https://url.sap/psglob-reqs)

### Translation and Translatability

- Understand the user groups and the languages in which the product will be available.
- Use clear and inclusive language that can be easily understood and accurately translated.
- Do not use idioms, slang, wordplay, or culturally specific expressions that may not translate well.
- Be flexible with stylistic rules when needed to make the content clearer or more suitable for local contexts.

### Usage of Variables

Do
- Variables should only represent untranslatable items like object IDs, values, or technical names.
- Name variables clearly (for example, **{sender}**, **{recipient}**) or use numbering (for example, **&1**, **{0}**). This helps translators reorder them correctly.
- Ensure variables are placed naturally within a full sentence. For example, **“Do you want to delete {documentName}?”**
- Avoid formatting like **“day(s)”** or **“file(s)”**. Variables
should not carry grammar logic (like plural/singular). Handle
such logic in code or with conditional strings.

**Metadata**

**Title**

**Breadcrumbs**
Writing for Notifications

**Description**

---

## Ux Writing

**Design System Hero**

# UX Writing

## General Guidelines

+------------------------------------------------------------------------------------x------------------------------------------------------------------------------------+
Tiles (plain)
+------------------------------------------------------------------------------------x------------------------------------------------------------------------------------+
[UX Writing Guidelines (BETA)](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/ux-writing-guidelines)
First version of the new cross-product UX writing guidelines.
+------------------------------------------------------------------------------------x------------------------------------------------------------------------------------+
[UI Text Guidelines for SAP Fiori Apps](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/ui-text-guidelines-for-sap-fiori)
Apply the basic rules for UI text in SAP applications.

## Specialized Guidelines

The content guidelines below each focus on UI text for a specific domain.

+--------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------+
+--------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------+
[AI UI Text](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/ai-ui-text)
Enable users to understand and trust AI functionality through well-crafted interface text.
+--------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------+
[Overview Page – UI Text Guidelines](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/overview-page-ui-text-guidelines)
Write consistent page and card titles, subtitles, and action texts in overview pages.
+--------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------+
[UX Writing for Notifications](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/ux-writing-for-notifications)
Craft actionable, user-friendly, and consistent notification messages.
+--------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------+
[Situation Handling – UI Text Guidelines](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/situation-handling-framework-ui-text-guidelines)
Create effective and consistent texts for both standard and extended Situation Handling frameworks.
+--------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------+
[Wrapping and Truncating Text](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/wrapping-and-truncating-text)
Ensure readability by applying effective wrapping and truncation strategies across devices.

+--------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------+
Tiles (plain, external_only)
+--------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------+
[Overview Page – UI Text Guidelines](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/overview-page-ui-text-guidelines)
Write consistent page and card titles, subtitles, and action texts in overview pages.
+--------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------+
[UX Writing for Notifications](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/ux-writing-for-notifications)
Craft actionable, user-friendly, and consistent notification messages.
+--------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------+
[Situation Handling – UI Text Guidelines](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/situation-handling-framework-ui-text-guidelines)
Create effective and consistent texts for both standard and extended Situation Handling frameworks.
+--------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------+
[Wrapping and Truncating Text](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/wrapping-and-truncating-text)
Ensure readability by applying effective wrapping and truncation strategies across devices.

**Metadata**

Title

Breadcrumbs

---

## Walkme

**Design System Hero**

# WalkMe

## Overview

+-------------------------------------------------------------------x-------------------------------------------------------------------+
Tiles (plain)
+-------------------------------------------------------------------x-------------------------------------------------------------------+
[About the WalkMe Guidelines](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/walkme/walkme-intro)
Check out our evolving content design resources for WalkMe content creators.

## WalkMe Toolkit

+-----------------------------------------------------------------------x-----------------------------------------------------------------------+
Tiles (plain)
+-----------------------------------------------------------------------x-----------------------------------------------------------------------+
[Content Guidelines](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/walkme/walkme-content-guidelines)
Apply content guidelines that are tailored to the WalkMe experience.
+-----------------------------------------------------------------------x-----------------------------------------------------------------------+
[Toolkit Guidelines](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/walkme/walkme-toolkit-guidelines)
Craft clear, helpful content for WalkMe tour components.
+-----------------------------------------------------------------------x-----------------------------------------------------------------------+
[Bolierplate Text and Examples](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/walkme/walkme-boilerplate)
Find copy-and-paste examples for common tasks and UI elements.

**Metadata**

Title

Breadcrumbs

---

