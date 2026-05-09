# SAP Fiori UI Elements: Actions

This reference covers the following UI components:

- [Button](#button)
- [Link](#link)
- [Link Web Component](#link-web-component)
- [Toggle Button](#toggle-button)
- [Toggle Button Web Component](#toggle-button-web-component)

---

## button

Buttons enable users to trigger actions in applications, from submitting data to opening menus or toggling views. They are available in different types and visual styles to reflect purpose, priority, and intent. Button behavior and appearance can change depending on user interaction, layout context, or the type of task.

*Button component*

There are 4 button types:

- [Simple button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/#types) for one action
- [Toggle button](https://www.sap.com/design-system/fiori-design-web/ui-elements/toggle-button/) to switch between different states
- [Segmented button](https://www.sap.com/design-system/fiori-design-web/ui-elements/segmented-button/) with a group of options
- [Menu button](https://www.sap.com/design-system/fiori-design-web/v1-136/ui-elements/button/#menu-button) with a group of actions

## When to Use

+-----------------------------------------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------------------------------------------+
When To Use
+-----------------------------------------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------------------------------------------+
Do
Use the button types as follows:
- Use **simple buttons** for specific actions, such as *Create/Edit/Save, Approve/Reject, Accept/Decline, OK/Cancel.*
- Use **toggle buttons** in a toolbar to activate or deactivate an object or element. You can also use toggle buttons to switch between different states.
- If you want the user to select one option from a small group, offer a **segmented button** in the toolbar. For example: *Year/Month/Day,* or *Small/Medium/Large.*
- Use the **menu button** if you need a menu that provides more than one option.
+-----------------------------------------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------------------------------------------+
Don't
Do not use buttons if:
- You want to link to a different page or object. Use the [link](https://www.sap.com/design-system/fiori-design-web/ui-elements/link/) instead.
- You want to display general navigation functions. Use *Home* or [breadcrumbs](https://www.sap.com/design-system/fiori-design-web/ui-elements/breadcrumb/), ensuring navigation is clearly distinguished by positioning items on the left side.
- You want to provide the ability to navigate within a multi-step process. Use a [wizard](https://www.sap.com/design-system/fiori-design-web/ui-elements/wizard/) instead.
- You want to let users upload content. Use the [upload set](https://www.sap.com/design-system/fiori-design-web/ui-elements/upload-set/) control instead.
- You want to let users select from multiple related options. Use [radio buttons](https://www.sap.com/design-system/fiori-design-web/ui-elements/radio-button/) or [checkboxes](https://www.sap.com/design-system/fiori-design-web/ui-elements/checkbox/).

## Anatomy

1. **Text:** Describes the action triggered by the button.
2. **Icon:** Shows a symbol to help clarify what the button does.
3. **Stroke:** Outlines the button with a border to define its
shape, especially in low-contrast environments.
4. **Background:** Indicates the button’s semantic meaning using
different background colors (for example, neutral or warning).
## Types

### Button

Buttons can trigger different types of actions, with appropriate styling to help users recognize the intent and importance of each one. These different action types are explained in more detail in the [action placement](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement) guideline.

#### Button Variants
**A. Text Only**
**B. Icon Only**
**C. Icon and Text**
**> **Guideline:** **

Within SAP S/4HANA, a button can contain either **an icon or a text**.
The SAP Fiori Elements framework supports only **text** buttons, except for in tables, where inline action buttons can be either icon or text, **not both**.

#### Button Priority and Emphasis
**A. Primary Action:** Emphasized with filled color
appearance; used for primary or most frequent action.
**B. Secondary Action:** Light or minimally styled
appearance; used for supporting actions.
**C. Tertiary Action:** Minimally styled button, often
with color-only text and no border; used for low-priority
actions.
#### Button Intent and Styling
**A. Success Action:** Positive styling (green); used to
confirm successful or desirable outcomes.
**B. Negative Action:** Error styling (red); used for
actions that delete, remove, or cancel, such as delete
account or cancel subscription.
**C. Attention Action:** Caution styling (yellow); used
for actions that might lead to unintended consequences,
such as continue without saving or send anyway.
**> **Guideline:** **

Always use a text button for primary, secondary, semantic, and negative path actions.
\Use icon buttons only if the icon metaphor is easily recognizable. Ideally, it should have same meaning worldwide.\ \ For more information about icons in general, check out the article on [iconography](https://www.sap.com/design-system/fiori-design-web/foundations/visual/iconography/horizon).

#### Header and Footer Toolbars

Use the following button styling for the different action types in the header and footer toolbar:

- **Primary action:** Use the **emphasized** button style. Note that there can only be **one primary action per page**.
- **Secondary action:** Use the **default** button style. In SAPUI5, you must implement **type=”ghost”** to achieve this style in the header and footer toolbar.
- **Negative path action:** Use the **transparent** button style.
- **Semantic action:** Use the **semantic buttons** for positive and negative actions. Use the “Accept” style for positive actions, and “Reject” for negative actions. Semantic actions must always be text buttons.

#### Content Toolbars

Use the following button styles in content toolbars for tables, forms, or charts:

- If the single primary action for the whole page is in the toolbar, use the emphasized button style.
- If the single primary action for the whole page is **not** in the toolbar, highlight the most important button in the toolbar with the default button style.
- For secondary actions and negative path actions, use the transparent button style.
- For split buttons and menu buttons, use the transparent button style.
- Do not use semantic button styles.

### Toggle Button

A toggle button switches between two actions. One of the actions is always active, one is inactive. Use the toggle button for secondary actions.

*Toggle button - regular and pressed state*

For more information, see [Toggle Button](https://www.sap.com/design-system/fiori-design-web/ui-elements/toggle-button/).

### Segmented Button

A segmented button is a group of connected buttons that users can select. The group appears as a single component divided into multiple segments.

*Segmented button*

For more information, see [Segmented Button](https://www.sap.com/design-system/fiori-design-web/ui-elements/segmented-button/).

### Menu Button

There are two types of menu buttons. Both can contain items and submenus.

#### Standard Menu Button

When the user activates the button, the menu opens. This is the **default type**.

*Standard menu button*

#### Split Menu Button

The split menu button is separated into two areas: the text and the arrow icon. The separator between them signals that the two areas result in different actions. The user has two choices: activating the text on the button triggers the action. Activating the arrow opens the menu. The split button consolidates a variety of commands, especially when one of the commands is used more often.

In split mode, the text depends on the default action. If the default action is displayed as an icon only, all the menu items must contain icons.

*Split menu button*

The split menu button can have two different behaviors:

1. The button always triggers the default action set by the app developer. If no default action has been defined, the first item in the menu list becomes the default.
2. The button triggers the last action chosen by the user. Initially, it also triggers the default action. However, when the user selects a different action, this user action becomes the default, and the button text changes accordingly. The button has a fixed size and the text truncates if the menu item exceeds the available width (as with the combo box).

## Behavior and Interaction

Buttons can be triggered through mouse, keyboard, touchscreen, and screen reader interaction.

- A **button** provides visual feedback for “hover”, “press-down”, and “focused” states.
- A **toggle button** remains in the pressed state until it is pressed again.
- In a **segmented button**, the chosen option stays active until the user presses one of the other options.
- A **menu button** displays a dropdown menu on activation.
- In a **split button,** selecting the button text triggers that action directly. Activating the arrow opens a dropdown menu. If the user selects a menu item, the action is triggered and the menu closes.

If an action cannot be triggered, or is temporarily unavailable, use the disabled state for the corresponding button.

If you want to switch a text, icon or tooltip after a button click, bear in mind to use the invisible message control to also convey the information to screen reader listeners.

All three button types support the cozy and compact form factors. For more information, check out the article on [content density](https://www.sap.com/design-system/fiori-design-web/foundations/visual/cozy-compact).

*Button states - regular, hover, pressed, focused, and disabled*

## Responsiveness

### Button

The button usually grows to fit the size of the text. If you set a fixed size for the button, the text truncates.

If the button is used in a responsive container or toolbar, it follows the responsive behavior defined for that element. For example, the button can move to another line.

*Button with different lengths and fixed size with truncated text*

### Menu ButtonMenu Button

The maximum width of the menu button is 12 rem (192 px). If the button text exceeds the maximum or fixed width, it truncates.

On **tablet and desktop devices (sizes M and L)**, the menu button triggers a cascading dropdown menu.

On **smartphones (size S)**, the menu opens in a full screen dialog, and the button label becomes the title of the dialog. The footer contains a *Cancel* button. Items with submenus become navigable. Navigation is similar to that used in a [popover](https://www.sap.com/design-system/fiori-design-web/ui-elements/popover/), with a *Back* button.

## Badge

The button can be visualized with a badge. This badge attracts the user’s attention and is typically used in browse and collect use cases. Badges are available for all types and sizes of the standard button.

There are two different badge types: **counter badge** and **attention badge**. A button can show either a counter badge or an attention badge, but never both.

### Counter Badge

- **Usage:** To show a number.
- **Example:** To display the number of items in a shopping cart.
- **Placement:** Depends on the form factor. Either inside the button (compact size) or on the top right corner (cozy size).

*Counter badge on different button types*

### Attention Badge

- **Usage:** To just attract the user's attention.
- **Example:** To indicate that a new comment is available.
- **Placement:** The attention badge is always placed in the top right corner, independent of the button size (compact or cozy form factor).

*Attention badge on different button types*

## Guidelines

### Button Text

- Choose a button text that is short and meaningful. Check out the [UI text guidelines](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/ui-text-guidelines-for-sap-fiori) for more information.
- Use a verb in the imperative for all actions (for example: *Save*, *Cancel*, *Edit*).
  Note: The grammatical form for actions can differ for other languages. For example, German action labels use the infinitive (*Sichern*, *Abbrechen*, *Bearbeiten*).
- Keep in mind that the text can be up to 300% longer in other languages.
- If you need to show the number of items that will be affected by the action of the button, you can add the number in parentheses. For example, *Edit (3)*.
- Do not change the text or icon of a toggle button when it is pressed. Screen readers announce the “pressed” state for the action. If you use a different text for the pressed state, the screen reader announcement doesn’t make sense.

### Icon Buttons

- \\Use icon buttons only if the icon metaphor is easily recognizable. Ideally, it should have same meaning worldwide.
- Make sure the default accessibility text for the icon is correct for your use case.\ If the text is not ideal, define an app-specific accessibility text.
- Offer a [tooltip](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/using-tooltips) to show the label for icon buttons.
- Don’t use the icon control for buttons. Use the icon property for the button instead.

### Button Shortcut

You can show the keyboard shortcut for an action. The keyboard shortcut appears on hover or on keyboard focus, and its positioning (top or bottom) is context-dependent. When a tooltip is needed, it is combined with the shortcut information.

> **Hint, Col-1:** To show a keyboard shortcut, use `sap.ui.core.CommandExecution`. Do not use a tooltip.

## Localization

The button supports left-to-right (LTR) and right-to-left (RTL) reading directions.

*Button – left-to-right*

---

## link

+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
Message Strip (information)
+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
This guideline now covers both SAPUI5 and SAP Web Components. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).

## Intro

A link (also known as a hyperlink) is an interactive text element. It is typically used for navigation, allowing users to move between different pages or sections of an application.

Link

### Component availability

This component is available in the following libraries:

+-----------x------------+------------------------------------------------x------------------------------------------------+--------------------x--------------------+
Library                | Technical Name                                                                                  | Identifier
+-----------x------------+-------------------------------------------------------------------------------------------------+--------------------x--------------------+
SAPUI5 Demo Kit        | [sap.m.Link](https://ui5.sap.com/#/entity/sap.m.Link)                                           | <u>:badge, info, large, _, SAPUI5:</u>
+-----------x------------+------------------------------------------------x------------------------------------------------+--------------------x--------------------+
| <u>:badge, info, large, _, SAP Web
SAP Web Components     | [ui5-link](https://ui5.github.io/webcomponents/components/Link/)                                | Components:</u>
+-----------x------------+------------------------------------------------x------------------------------------------------+--------------------x--------------------+
SAP Web UI Kit (Figma) | [Link](https://www.figma.com/design/SILcWzK5uFghKun9jx6D7c/SAP-Web-UI-Kit?node-id=200579-38785) | <u>:badge, info, large, _, Figma:</u>

**Table (external_only)**
+----------------x-----------------+--------------------------------x---------------------------------+--------------------x--------------------+
Library                          | Technical Name                                                   | Identifier
+----------------x-----------------+------------------------------------------------------------------+--------------------x--------------------+
SAPUI5 Demo Kit                  | [sap.m.Link](https://ui5.sap.com/#/entity/sap.m.Link)            | <u>:badge, info, large, _, SAPUI5:</u>
+----------------x-----------------+--------------------------------x---------------------------------+--------------------x--------------------+
| <u>:badge, info, large, _, SAP Web
SAP Web Components               | [ui5-link](https://ui5.github.io/webcomponents/components/Link/) | Components:</u>
+----------------x-----------------+--------------------------------x---------------------------------+--------------------x--------------------+
SAP Fiori for Web UI Kit (Figma) | [Link](https://www.figma.com/community/file/1494295794601744471) | <u>:badge, info, large, _, Figma:</u>

## When to Use

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
When To Use
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
Do
Use the link to:
- Navigate to another page.
- Jump to an anchor.
- Open an external URL.
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
Don't
Don't use the link to:
- Тrigger actions (like submitting a form). Use a [button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/) instead.
- Represent the object itself. In this case, use an [object identifier](https://www.sap.com/design-system/fiori-design-web/ui-elements/object-display-elements/#object-identifier) that displays the object's details in a [quick view](https://www.sap.com/design-system/fiori-design-web/ui-elements/quickview/) or a [popover](https://www.sap.com/design-system/fiori-design-web/ui-elements/popover/).
- Serve decorative purposes when there is no target or reference to link to.

+----------------------------------------------------------------------x----------------------------------------------------------------------+
Top Tips
+----------------------------------------------------------------------x----------------------------------------------------------------------+
- Use meaningful link text that describes the outcome (for example, *View Sales Order*). Avoid generic text such as *Click here* or *Link*.
- Avoid using two icons simultaneously in a link.

## Anatomy

A link is interactive text, indicated by color and underline.
1. **Text link:** Provides context about what the link refers to.
2. **Underline:** Helps recognize the link by applying an underline based on
the link style and the corresponding interaction state.
3. **Icon (optional):** Displays a symbol to help clarify what the link does.
## Types

### Link types

**A. Default link:** A standard link style. Use it for regular navigation.

**B. Emphasized link:** A link style with increased visual emphasis. Use it when a link needs stronger visual prominence than default links.

**C. Subtle link:** A link style with reduced visual emphasis. Use it only in tables to distinguish secondary links in dense data lists. Do not use subtle links outside tables.

Link types

### Link with icon

Use a link with an icon when the icon helps clarify the link’s purpose and destination, such as a file type (PDF, spreadsheet) or an object type (user, order, attachment).

Link with icons on the leading and trailing sides

## States

### Component states

The link component has two states: enabled and disabled.

**A. Enabled state:** The link is interactive.
**B.** **Disabled state:** The link is not interactive.

Link component states: enabled (A) and disabled (B)

For more information, see [Component States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-component-states).

### Interaction states

The link component has four interaction states: regular, hover, visited, and down.

**A. Regular state:** Displays the default interaction state of the component.
**B. Hover state:** Displays the hover state when the cursor is over an enabled link.
**C. Visited state:** Displays the visited state after the link has been clicked.
**D. Down state:** Displays the pressed state while the link is pressed.

Link interaction states: regular (A), hover (B), visited (C), and down (D)

For more information, see [Interaction States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-interaction-states).

### Focus states

The focus state indicates which component is currently focused and ready for keyboard interaction.

**A. Unfocused state:** Displays the unfocused state with no extra highlight.
**B. Focused state:** Displays the focused state with a visible highlight.

Link focus states: unfocused (A) and focused (B)

For more information, see [Focus States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-focus-states).

### Empty state :badge, info, large, _, SAPUI5 only:

The empty state indicator uses an en dash (–) line. It is displayed when the link component has no text.

Regular link (A) and empty state of a link (B)

## Behavior and Interaction

### Mouse interaction

The link appears in its default style when presented (A). When the cursor moves over it, the link provides visual feedback, typically by adding an underline, to indicate that it is interactive (B). When the user clicks the link, it momentarily displays a pressed state to confirm the interaction (C). After the click, the link retains a visible focus indicator (D). This helps maintain orientation, supports keyboard accessibility, and aligns with standard interaction patterns across the system.

Mouse interaction

### Canceling link activation

You can cancel the activation of the link before releasing the mouse button during the activation process.

The link appears in its default style when presented (A). As the cursor moves over it, the link offers immediate visual feedback, typically by adding an underline, to indicate that it is interactive (B). If the user presses the mouse button while over the link but then drags the pointer outside the link’s active area before releasing, the link’s activation is canceled (C). In this scenario, the link does not navigate or trigger any action. However, after the mouse button is released, even outside the link boundaries, the link retains a visible focus indicator to reflect the recent interaction (D).

Canceling link activation

### Activating a link via context menu

The link appears in its default style when presented (A). As the user moves the cursor over it, the link provides visual feedback to indicate that it is interactive (B). When the user right-clicks the link, it briefly acknowledges the interaction before the context menu opens near the pointer (C). As the user moves through the menu, each item highlights to signal that it is selectable (D). Selecting a menu item triggers the corresponding action, for example, opening the link in a new tab or performing another browser-supported operation. This interaction follows standard platform conventions and does not interrupt the primary workflow.

Triggering a link via context menu

### Touch interaction

Tapping the link initiates the interaction. Since hover states are unavailable on touch devices, a single-finger tap gesture is used to initiate the link interaction.

For more information, see [Tap (press and release).](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/gestures#tap-press-and-release)

### Tooltips

Provide a tooltip when the link text is truncated, for text-only links and links with icons.

Link with truncated text and a tooltip

For more information, see [Using Tooltips](https://www.sap.com/design-system/fiori-design-web/v1-136/foundations/best-practices/ui-elements/using-tooltips).

## Responsiveness

The link does not change size according to the cozy or compact mode.

Link in compact and cozy mode

For more information, see [Content Density](https://www.sap.com/design-system/fiori-design-web/foundations/visual/cozy-compact).

## Accessibility

SAP follows international standards, such as WCAG and WAI-ARIA, and strives to make our business solutions accessible and inclusive.

For more information, see [Accessibility in SAP Fiori](https://www.sap.com/design-system/fiori-design-web/discover/sap-design-system/product-standards/accessibility-in-sap-fiori) and the [Accessibility Design Tools Handbook](https://www.sap.com/documents/2023/11/bc210d8b-977e-0010-bca6-c68f7e60039b.html).

### Keyboard navigation

The following keyboard combinations are supported by the SAPUI5 Link component.

**Table (col-width-30-70)**

Key Combination

**Tab**
to the next UI element.

**Shift \+ Tab**

**Enter/ Return** or **Spacebar**

**Shift**

### Screen reader support

For additional details on screen reader support and Accessible Rich Internet Applications (ARIA), see the [UI5 Screen Reader Support](https://ui5.sap.com/#/topic/33fae3482358438e93daea5232527093) and [WAI-ARIA Authoring](https://www.w3.org/TR/wai-aria-1.2/).

## Content

### Localization

The link component supports both left-to-right (LTR) and right-to-left (RTL) reading directions.

Link in left-to-right mode

### Wrapping and Truncation

The link component supports wrapping and truncation.

**A. Wrapping:** The link text automatically wraps to the next line when there isn’t enough horizontal space, so the full content remains visible on all screen sizes. This is the default behavior of the component.

**B. Truncation:** Avoid truncation. If you truncate the link text, provide the full text in a tooltip.

Wrapped (A) and truncated (B) link

For more information, see [Wrapping and Truncation](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/wrapping-and-truncation).

## Features

### Opening a popover and a context menu

A link can be configured to open a popover when clicked, revealing additional content or options without navigating away from the current view. Alternatively, users can right-click the link to access a context menu, which provides additional actions based on standard browser behavior.

Link opening a popover (A) or a context menu (B)

### Target options

The link supports different target options that define where the linked content opens.

The following target options are available: The link can open the linked document in a new browser window or tab (**blank**), in the parent frame if applicable (**parent**), in the same frame as the current page (**self**), or in the full browser window, replacing any existing frames (**top**).

Demonstrating interaction with target destination

## Framework Comparison Overview

Some behaviors differ between frameworks due to implementation specifics. The table below summarizes the differences between SAPUI5 and SAP Web Components and lists the framework-specific patterns.

**Table (col-width-60-20-20)**

Features                                                                                                                                                                                                                                                      | SAPUI5    | SAP Web Components

The link shows an empty state indicator using an en dash (–) line when no text content is provided. For more information, see [Empty State](https://www.sap.com/design-system/fiori-design-web/ui-elements/link/#empty-state-badge-info-large-_-sapui5-only). | Available | Not available

---

## link-web-component

+------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------+
+--------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------+---------x----------+
## This page has been deprecated and is no longer available.
This page was deprecated with guideline version **1.145**.
#### Reason for deprecation
The guidelines for the SAP Web Component and the SAPUI5 component have been merged. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).
#### Looking for the latest information?
Visit the page below for the unified guideline with the most recent updates.
[Link](https://www.sap.com/design-system/fiori-design-web/ui-elements/link/)

---

## toggle-button

+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
Message Strip (information)
+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
This guideline now covers both SAPUI5 and SAP Web Components. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).

## Intro

The toggle button is a UI component that switches between two states: active and inactive.

Use the toggle button for secondary actions like showing or hiding a screen element or providing a filtered view of a dataset.

Toggle button

### Component availability

The toggle button is available in the following libraries:

+-----------x------------+---------------------------------------------------------------x---------------------------------------------------------------+----------------x-----------------+
Library                | Technical Name                                                                                                                | Identifier
+-----------x------------+-------------------------------------------------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit        | [sap.m.ToggleButton](https://ui5.sap.com/#/entity/sap.m.ToggleButton)                                                         | :badge, info, large, _, SAPUI5:
+-----------x------------+---------------------------------------------------------------x---------------------------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components     | [ui5-toggle-button](https://ui5.github.io/webcomponents/components/ToggleButton/)                                             | Components:
+-----------x------------+---------------------------------------------------------------x---------------------------------------------------------------+----------------x-----------------+
SAP Web UI Kit (Figma) | [Toggle Button](https://www.figma.com/design/SILcWzK5uFghKun9jx6D7c/SAP-Web-UI-Kit?node-id=365511-5609\&t=E4ejx9oEHVg9l0a5-4) | :badge, info, large, _, Figma:

**Table (external_only)**
+----------------x-----------------+-----------------------------------------x-----------------------------------------+----------------x-----------------+
Library                          | Technical Name                                                                    | Identifier
+----------------x-----------------+-----------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit                  | [sap.m.ToggleButton](https://ui5.sap.com/#/entity/sap.m.ToggleButton)             | :badge, info, large, _, SAPUI5:
+----------------x-----------------+-----------------------------------------x-----------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components               | [ui5-toggle-button](https://ui5.github.io/webcomponents/components/ToggleButton/) | Components:
+----------------x-----------------+-----------------------------------------x-----------------------------------------+----------------x-----------------+
SAP Fiori for Web UI Kit (Figma) | [Toggle Button](https://www.figma.com/community/file/1494295794601744471)         | :badge, info, large, _, Figma:

## When to Use

+---------------------------------------------------------------------------------------x----------------------------------------------------------------------------------------+
When To Use
+---------------------------------------------------------------------------------------x----------------------------------------------------------------------------------------+
Do
Use the toggle button to:
- Switch between two states.
- Activate or deactivate an element in a toolbar.
+---------------------------------------------------------------------------------------x----------------------------------------------------------------------------------------+
Don't
Don’t use the toggle button to:
- Trigger an activity, flow, or process (such as *Create*, *Edit*, or *Save*). Use a [button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/) instead.
- Display a large number of options. Use a menu button instead.

+------------------------------------x------------------------------------+
Top Tips
+------------------------------------x------------------------------------+
- Use the standard toggle button for secondary actions.
- Use the transparent toggle button for tertiary actions.
- Always pair icon-only toggle buttons with a tooltip that labels them.

## Anatomy

The toggle button component consists of the following
elements:
Toggle button anatomy
1. **Background:** Different background colors indicate
the state of the toggle button.
2. **Text or icon:** Describes or visualizes the action
triggered by the toggle button.
## Types

### Display types

The toggle button supports three display types:

**A:** Text only
**B:** Icon only
**C:** Text and icon

Display types

### Hierarchy types

The toggle button has two hierarchy types:

**A. Standard:** The standard toggle button appears with a white background and subtle gray border and is used for secondary actions.
**B. Transparent:** The transparent toggle button appears with a transparent background and no border and is used for tertiary actions.

Hierarchy types

## States

### Component states

The toggle button supports two component states: enabled
and disabled. Each state can appear as untoggled or
toggled.
**A. Enabled:** The toggle button is interactive,
enabling the user to select it and trigger its associated
action.
**B. Disabled:** The toggle button is not interactive and
cannot be selected or triggered by the user.
For more information, see [Component States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-component-states).

### Interaction states

The toggle button supports three interaction states: regular, hover, and down. Each state appears as untoggled or toggled.

#### Regular states

**A. Regular untoggled:** Displays the default, unselected state.
**B. Regular toggled:** Displays the selected state.
Regular states: untoggled (A) and toggled (B)

#### Hover states

**A. Hover untoggled:** Displays a hover state when the
cursor moves over an enabled, unselected toggle button.
**B. Hover toggled:** Displays a hover state when the
cursor moves over an enabled, selected toggle button.
#### Down state

**Down untoggled:** Displays a down state while the user
is pressing an unselected toggle button.
Down untoggled state

For more information, see [Interaction States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-interaction-states).

### Focus state

The focus state indicates that the toggle button is
focused and displays a visible focus highlight.
Focused untoggled (A) and focused toggled (B) states
The focus state appears with an additional border.
When interaction begins, the focus state appears on the
active toggle button.
For more information, see [Focus States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-focus-states).

## Behavior and Interaction

### Mouse interaction

#### Toggling a toggle button

Clicking an untoggled toggle button switches it to the toggled state.

**A:** The user starts pressing an untoggled toggle button.
**B:** When the user releases the toggle button, it toggles, triggers its action, and retains focus.
**C:** After the user moves the cursor away from the toggle button, it becomes regular toggled.

Toggling interaction

#### Untoggling a toggle button

Clicking a toggled toggle button switches it to the untoggled state.

### Touch interaction

On touch devices, tapping the toggle button toggles its state. Hover and focus states are not supported.

### Tooltips

When designing icon-only toggle buttons, always pair them with a tooltip that labels them.

Icon-only toggle button with tooltip

For more information, see [Using Tooltips](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/using-tooltips).

## Responsiveness

By default, the toggle button expands and shrinks with the width of the text or icon.

Toggle button with different lengths

The toggle button supports cozy and compact content densities.

Compact (A) and cozy (B) content densities

For more information, see [Content Density](https://www.sap.com/design-system/fiori-design-web/foundations/visual/cozy-compact).

## Accessibility

SAP follows international standards, such as WCAG and WAI-ARIA, and strives to make our business solutions accessible and inclusive.

For more information, see [Accessibility in SAP Fiori](https://www.sap.com/design-system/fiori-design-web/discover/sap-design-system/product-standards/accessibility-in-sap-fiori) and the [Accessibility Design Tools Handbook](https://www.sap.com/documents/2023/11/bc210d8b-977e-0010-bca6-c68f7e60039b.html).

### Keyboard navigation

The following keyboard combinations are supported by the SAPUI5 Toggle Button component.

**Table (col-width-30-70)**

Key Combination

**Tab**
already there, the focus is moved to the next UI element.

**Shift \+ Tab**

**Enter/ Return** or **Spacebar**

### Screen reader support

For additional details on screen reader support and Accessible Rich Internet Applications (ARIA), see [UI5 Screen Reader Support](https://ui5.sap.com/#/topic/33fae3482358438e93daea5232527093) and [WAI-ARIA Authoring](https://www.w3.org/TR/wai-aria-1.2/).

## Content

### Localization

The toggle button supports left-to-right (LTR) and right-to-left (RTL) reading directions.

Toggle button – left-to-right

## Framework Comparison

There are no differences between SAPUI5 and SAP Web Components regarding thе component's behaviors and framework-specific patterns.

---

## toggle-button-web-component

+------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------+
+--------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------+---------x----------+
## This page has been deprecated and is no longer available.
This page was deprecated with guideline version **1.142**.
#### Reason for deprecation
The guidelines for the SAP Web Component and the SAPUI5 component have been merged. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).
#### Looking for the latest information?
Visit the page below for the unified guideline with the most recent updates.
[Toggle Button](https://www.sap.com/design-system/fiori-design-web/ui-elements/toggle-button/)

---

