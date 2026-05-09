# SAP Fiori UI Elements: Messages

This reference covers the following UI components:

- [Message Strip](#message-strip)
- [Message Strip Web Component](#message-strip-web-component)

---

## message-strip

+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
Message Strip (information)
+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
This guideline now covers both SAPUI5 and SAP Web Components. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).

## Intro

The message strip component displays application-related messages directly within the interface. It draws attention to important information, such as warnings or status changes, that might otherwise go unnoticed. The message strip component can be embedded within the header or detail area of an object or page, or it might apply only to a single component (for example, a table).

*Message strip*

### Component availability

This component is available in the following libraries:

+-----------x------------+--------------------------------------------------x---------------------------------------------------+----------------x-----------------+
Library                | Technical Name                                                                                       | Identifier
+-----------x------------+------------------------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit        | [sap.m.MessageStrip](https://ui5.sap.com/#/entity/sap.m.MessageStrip)                                | :badge, info, large, _, SAPUI5:
+-----------x------------+--------------------------------------------------x---------------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components     | [ui5-message-strip](https://sap.github.io/ui5-webcomponents/components/MessageStrip/)                | Components:
+-----------x------------+--------------------------------------------------x---------------------------------------------------+----------------x-----------------+
SAP Web UI Kit (Figma) | [Message Strip](https://www.figma.com/design/SILcWzK5uFghKun9jx6D7c/SAP-Web-UI-Kit?node-id=880-2602) | :badge, info, large, _, Figma:

**Table (external_only)**
+----------------x-----------------+-------------------------------------------x-------------------------------------------+----------------x-----------------+
Library                          | Technical Name                                                                        | Identifier
+----------------x-----------------+---------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit                  | [sap.m.MessageStrip](https://ui5.sap.com/#/entity/sap.m.MessageStrip)                 | :badge, info, large, _, SAPUI5:
+----------------x-----------------+-------------------------------------------x-------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components               | [ui5-message-strip](https://sap.github.io/ui5-webcomponents/components/MessageStrip/) | Components:
+----------------x-----------------+-------------------------------------------x-------------------------------------------+----------------x-----------------+
SAP Fiori for Web UI Kit (Figma) | [Message Strip](https://www.figma.com/community/file/1494295794601744471)             | :badge, info, large, _, Figma:

## When to Use

+-----------------------------------------------------------------------x------------------------------------------------------------------------+
When To Use
+-----------------------------------------------------------------------x------------------------------------------------------------------------+
Do
Use the message strip to:
- Display messages that apply to either the entire page or a specific section, such as an object header.
- Inform users about the status of an object, such as a process, item, or workflow.
- Display a warning message to alert users to an issue.
+-----------------------------------------------------------------------x------------------------------------------------------------------------+
Don't
Don’t use the message strip to:
- Display information within another component (for example, a table cell or list item), or to apply the component to another small element.
- Request decisions or immediate user actions. Use a [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog/) instead.
- Communicate issues related to a specific input or form element. Use the component’s value state instead.

+------------------------------------------------------------------------x------------------------------------------------------------------------+
Top Tips
+------------------------------------------------------------------------x------------------------------------------------------------------------+
- Place message strips close to relevant content to avoid interrupting the user flow.
- Use value states consistently so users can understand the urgency and nature of each message.
- Show an icon to identify the message type.
- Include a *Close* button when the message is persistent or requires user dismissal.
- Keep text simple and concise, use formatting only when you need to emphasize or add hyperlink text.
- Add a custom icon when you need to communicate specific meaning not covered by standard value states.
- Apply a custom background color when you need to highlight special message types or match application branding.
- Ensure the message strip adapts responsively, keeping the icon on the left, the *Close* button on the right, and letting text wrap naturally.

## Anatomy

1. **Container:** Holds the icon, message text, and *Close* button.
2. **Icon (optional):** Visual indication of the message type. By default,
the message strip uses standard icons for negative, critical, positive, and
information messages.
3. **Text:** Displays the main message content.
4. ***Close*** **button (optional):** Lets users dismiss the message strip.
## Types

### Message strip with or without icon

A message strip can be displayed with or without an icon, depending on the context and importance of the message. Including an icon helps users quickly recognize the message type.

*Message strip with and without icon*

### Message strip with or without “Close” button

A message strip can appear with or without a *Close* button. Use the *Close* button for temporary or informational messages that users can remove, and omit for persistent messages that convey ongoing status or important system information.

*Message strip with and without “Close” button*

### Message strip with or without formatted text

A message strip can include plain or formatted text. Keep messages simple and concise in both cases. Use formatting, such as bold text or inline links only to emphasize key details, not to add complexity.
Below is an additional example to the formatted text to illustrate that links can be added to the message text.

*Message strip with and without formatted text*

### Message strip with custom icon

A message strip can include a custom icon to represent a specific status or industry-related context not covered by the standard value states. You can use a custom icon when you need to convey a unique meaning or align the message with application-specific semantics.

*Message strip with custom icon*

### Message strip with custom background

Use a custom background color when you need to distinguish special message types or align with app-specific branding. For additional options, see the \ [indication colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/morning-horizon?external#indication-colors)\ palette.

*Message strip with custom background color*

## States

### Value states

The message strip supports four value states: Negative, Critical, Positive, and Information.  Value states appear with a specific color and icon to convey their meaning. Unlike other components, message strips always have a value state.

**A. Negative:** Indicates that an error has occurred,
possibly guiding users to take corrective action.
*Message strip value states*
**B. Critical:** Alerts users to potential issues that
may require attention but are not errors. Users can
typically continue but might run into issues later.
**C. Positive:** Confirms that a user action or system
process has been successfully completed.
**D. Information:** Displays general information or
guidance that is not critical but can help users complete
their tasks.
**> **Guideline:** **

Use message strips sparingly and place them near the related content, so they inform without interrupting the user
flow. Consistent use of these semantic states ensures that users can quickly recognize and interpret the nature and
urgency of a message across the interface.

For more information, see [Value States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-value-states).

### Focus state

All value states can have a focus. A focus state indicates that
the component receives the keyboard interaction input. If a
message strip contains a link, the focus first goes to the link,
and then to the *Close* button.
For more information, see [Focus States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-focus-states).

## Behavior and Interaction

The user can dismiss a message strip from the application's UI by clicking the *Close* button located on the right-hand side. On mobile devices, the tap gesture is used for dismissal instead of mouse interaction.

## Responsiveness

The message strip adapts to different layouts and screen sizes. Icons remain on the left and the *Close* button on the right, while text wraps automatically.

If you place the message strip within the detail area for an object, it always uses 100% of the available width and reacts to the responsiveness of the container.

*Message strip – web and mobile appearance*

## Accessibility

SAP follows international standards, such as WCAG and WAI-ARIA, and strives to make our business solutions accessible and inclusive.

For more information, see [Accessibility in SAP Fiori](https://www.sap.com/design-system/fiori-design-web/discover/sap-design-system/product-standards/accessibility-in-sap-fiori) and the [Accessibility Design Tools Handbook](https://www.sap.com/documents/2023/11/bc210d8b-977e-0010-bca6-c68f7e60039b.html).

### Keyboard navigation

The following keyboard combinations are supported by the SAPUI5 message strip component.

**Table (col-width-30-70)**

Key Combination

**Tab**
If the message strip contains a link, the focus moves to it.
If there is no *Close* button, pressing **Tab** again moves the focus to the next interactive element outside the message strip.
If multiple links exist, pressing **Tab** moves the focus sequentially through the links, after which it moves to the *Close* button, if present.

**Shift \+ Tab**
If the message strip contains a link and the focus is on the *Close* button, the focus moves to the link.
If the focus is on the second link, pressing **Shift \+ Tab** moves the focus to the first link.

### Screen reader support

For details on screen reader support and Accessible Rich Internet Applications (ARIA), see [UI5 Screen Reader Support](https://ui5.sap.com/#/topic/33fae3482358438e93daea5232527093) and [WAI-ARIA Authoring](https://www.w3.org/TR/wai-aria-1.2/).

## Content

### Text

Messages should be simple and concise. Keep the following principles in mind when formulating message texts. For more information, see [UI Text Guidelines for SAP Fiori Apps – Messages](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/ui-text-guidelines-for-sap-fiori#general-message-guidelines).

### Link

All link types (regular, emphasized, subtle, and so on) can be used in the message strip component. Choose the link variant that best fits your use case. However, for a custom message strip using the extended palette, the subtle link is the recommended type. For more information, see [Link](https://www.sap.com/design-system/fiori-design-web/ui-elements/link/).

### Localization

The message strip supports both left-to-right (LTR) and right-to-left (RTL) languages layout helping users to read and interact naturally. In RTL layouts, the positions of the leading icon and the trailing *Close* button are flipped to match the reading direction (icon on the right, *Close* on the left).

Left-to-right message strip

## Framework Comparison

There are no differences between SAPUI5 and SAP Web Components regarding the component's behaviors and framework-specific patterns.

---

## message-strip-web-component

+------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------+
+--------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------+---------x----------+
## This page has been deprecated and is no longer available.
This page was deprecated with guideline version **1.142**.
#### Reason for deprecation
The guidelines for the SAP Web Component and the SAPUI5 component have been merged. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).
#### Looking for the latest information?
Visit the page below for the unified guideline with the most recent updates.
[Message Strip](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-strip/)

---

