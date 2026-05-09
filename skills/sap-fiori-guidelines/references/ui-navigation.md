# SAP Fiori UI Elements: Navigation

This reference covers the following UI components:

- [Icontabbar](#icontabbar)
- [Segmented Button](#segmented-button)
- [Segmented Button Web Component](#segmented-button-web-component)
- [Shell Search](#shell-search)
- [Side Navigation](#side-navigation)

---

## icontabbar

The icon tab bar is a **navigation** and **filtering** control that contains a set of tabs, each of which can display an icon, text, or both and link to a different content area or view.

There are two key use cases:

- To let users navigate between different sections of content on the screen.
- To let users filter lists, with the option to display all items or only those matching a specific attribute.

In both cases, users switch between tab pages by clicking the respective tab.

*Icon tab bar*

## When to Use

Do
Use the icon tab bar if:
- Your business objects need to show multiple facets at
the same time.
- You want to allow the user to browse through these
facets.
- You need a prominent or very visual filter on top of a
list.
- You have clear-cut process steps that need to be
visualized.
## Anatomy

### Tab Bar

1. **Main bar:** Contains the tabs, tab separators, and
the overflow menu.
2. **Tabs:** Represent navigation items that reveal
corresponding content when selected.
3. **Overflow menu:** Contains any remaining tabs that
can’t be displayed in the available space.
4. **Content area:** Displays the content associated with
the currently selected tab.
### Tab

1. **Icon:** Icon for the tab.
2. **Additional text:** Displays supplementary information for a tab, such as a count. It can appear above the label or next to it in parentheses.
3. **Text:** Text for the tab.
4. **Subtabs:** A tab can contain subtabs. For details, see [Hierarchies](https://www.sap.com/design-system/fiori-design-web/ui-elements/icontabbar/#hierarchies).
## Types

The horizontal layout of the icon tab bar never changes. The tabs always appear side by side. However, there are several types of tab bar to choose from: text only, icon tabs, tabs as filters, tabs as process steps, and semantic tabs. Each type offers different ways to present and navigate information on the screen. The choice of type depends on whether you want to guide users through a process, filter content, or simply switch between different content areas.

### Text Only

The text-only variant is one of the most common types. It allows longer labels, and can also display counters next to the text to indicate the number of items on the tab page.

Unlike all other tab variants, the labels **do not get truncated**. The full text is always shown. As a result, you need to ensure that your labels do not become too long. They should still be easy to read on smaller screens.

If you use text-only tabs, make sure that the `UpperCase` property **is disabled** and that you enter the labels in title case (for example: *Approval Flow*).

Icon tab bar – text-only tabs (left) and text-only tabs with counters shown inline in parentheses (right)

**> **Hint:** **

- If counters are used, set the property `HeaderMode` to “Inline” so the counters appear in brackets after the labels.
- **Do not** use the old layout that shows the counters on top of the labels (`HeaderMode` = “Standard”).

### Icon Tabs

Icon tabs are also common tab types. These round tabs can be populated with any icon from the [SAP icon font](https://www.sap.com/design-system/fiori-design-web/resources/libraries/downloads#sap-icon-font).

Labels are optional. If you decide to use labels, use them for all tabs. You can use counters as needed.

*Icon tab bar – icon-only tabs (left) and icon-only tabs with counters shown above the icons (right)*

**> **Guideline:** **

- **Please note that starting with SAPUI5 version 1.40, you should only use the horizontal type of label (icon and
label side by side).**
- If your labels get truncated, consider using shorter labels or text tabs (without icons), since text tabs cannot
get truncated.

### Tabs as Filters

If you build the tab bar as a filter, it can comprise two parts: an optional “all” tab on the left that shows the total number of items and describes the type of item (for example, 123 Products), and tabs for specific filters in which the tab text specifies the filter type (for example, laptops, monitors, printers, accessories).

Icon tab bar starting with a filter for all items with a counter followed by icon tabs with labels and counters displayed in the top right corner

### Tabs as Process Steps

You can also use the tab bar to depict a process. In this case, each tab stands for one step.

To connect the process steps, you can use the triple-chevron icon (:process: ) from the \[SAP icon font](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/resources/libraries/downloads#sap-icon-font)\ (technical name: process). Do not use the triple-chevron icon in the anchor bar of an object page.

If the process steps have a fixed order, set the property `TabsOverflowMode` to “StartAndEnd” to show an overflow menu on both sides and to keep the order of the tabs intact.

*Icon tab bar used for process steps from Ordered to Paid, with tabs containing an icon and a count.*

> **Hint:** When using icons with labels, add a comment in the properties file to make editors and translators aware that space
is limited.
Example: *Label for icon tab on detail screen. Max 14-16 characters (depending on character width).*
Test whether your labels and their translations are displayed in full, and do not get truncated.

### Semantic Tabs

You can apply semantic colors to tabs to alert users or provide visual guidance. Colors indicate different states: neutral (blue), positive (green), critical (orange), or negative (red).

*Icon tab bar with semantic colors applied: Neutral (blue) and negative (red) on the left, and neutral (blue), critical (orange), and positive (green) on the right.*

**> **Guideline:** **

- Only use semantic colors if it is important for users to know that they need to take action (for example, to indicate errors or critical situations requiring action). Otherwise,
use the neutral default colors. For more information, see [How to Use Semantic Colors](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/how-to-use-semantic-colors).
- To comply with the two-senses accessibility principle, display semantic icons on all semantic tabs. In addition, use tab text that reflects the semantic meaning.
- To apply semantic colors to the icons and the text-only tabs, you can use the property [`sap.ui.core.IconColor`](https://ui5.sap.com/#/api/sap.m.IconTabFilter/controlProperties).

### Sub-Tabs

Depending on the content, there are two different modes possible: menu mode and split mode.

#### Sub-Tab in Menu Mode

The tab with sub-tabs in menu mode acts like a menu button and is used if the parent tab doesn’t have its own content. This means the main tab just acts as a headline and has only one interactive area.

Sub-tab in menu mode

#### Sub-Tab in Split Mode

The tab with sub-tabs in split mode acts like a split button and is used if the parent tab has its own content. This means the main tab has two interactive areas. One that directly leads to the content of the main tab and the other opens the menu which contains the sub-tabs.

Sub-tab in split mode

### Hierarchies

The tab bar supports hierarchies, allowing multiple tabs underneath one main tab. This way, you can group several tabs together, with the main tab acting as a headline.

You can illustrate a simple hierarchy using subtabs, which have no specific order other than their sequence, or present deeper hierarchies by nesting tabs with indentations to indicate the level of each tab.

*Icon tab bar with subtabs on the left, and nested tabs on the right*

**> **Hint:** **

By default, the property `maxNestingLevel` is “0” (zero). To enable nesting, adjust this value to the highest level of nesting that your app allows.

## Behavior and Interaction

### Clicking a Tab

To navigate through the views, the user clicks the tabs.

**Optional behavior:** If the user clicks a tab that is already open, the container collapses. It opens again when the user clicks any tab.

**> **Hint:** **

Use the `expandable` property to specify whether users can collapse the tab container (default = “true”):
- Let users collapse the container if there is additional content below the container, and the information inside the
container is not always needed.
- If there is no content below the tab container, set the `expandable` property to “false”.
The `expandable` property controls the initial state of the container. Do not change the default state (“true”).

### Changing the Order of Tabs

You can allow users to rearrange the tab order in a desktop environment (property: `enableTabReordering`). If this feature is enabled, users can drag and drop tabs to reorder them, either directly on the tab bar or inside the overflow menu.

It is also possible to drag and drop tabs from the tab bar to the overflow menu and vice versa.

If nesting is enabled (property `maxNestingLevel` > 0), users can choose the level at which they want to drop a tab. Dragging a tab activates a visual indicator for positioning the tab. For example, when a tab is dragged over another, it will be nested as a child of the highlighted tab. If the user drags a tab between two other tabs, the indicator shows the level at which level the tab will be nested.

*Reordering the tabs: dragging a tab activates visual indicators that let users choose the drop position – to place it at the same level between existing tabs (left), or to nest the tab as a child of another (right).*

> **Guideline:** **Do not use** this feature for:
- **Tabs as process steps:** This ensures that consecutive steps do not get mixed up.
- **Anchor bar navigation:** Sections that are represented in the anchor bar have a fixed order.

## Responsiveness

The icon tab bar stretches horizontally, which often exceeds the available width on small screens. It responds to limited space by offering a scrolling mechanism.

### Overflow

If there isn’t enough space to show all the tabs on the main bar, an overflow menu appears automatically, containing all the remaining tabs. In addition to the responsive overflow behavior, the icon tab bar can be forced into compact mode or even react dynamically to the application’s global density setting. See the [Tab Density](https://www.sap.com/design-system/fiori-design-web/ui-elements/icontabbar/#tab-density) section for details.

*Icon tab bar overflow*

You can set the overflow mode, depending on your use case:

- **End (default):** The overflow only appears at the end of the tab bar. Use this mode if the order of the tabs isn’t relevant.
- **Start and End:** The overflow menu can appear dynamically either on one or on both sides of the tab bar. Where the overflow appears depends on which tab is activated. Use this mode if the tabs need to stay in the same order.

You can also replace the buttons for the overflow menus with custom buttons.

*Icon tab bar overflow Start and End*

**> **Hint:** **

- For [processes with a fixed order](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/icontabbar/#tabs-as-process-steps) or in [the anchor bar of an object page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/#anchor-bar-navigation), display an overflow menu on both sides (property: `TabsOverflowMode`, value: `StartAndEnd`).
- For tabs that can be rearranged, display only one overflow menu on the far right (property: `TabsOverflowMode`, value: `End`).

### Tab Density

The default responsive design of the icon tab bar applies to both compact and cozy modes.  However, in addition to this responsive behavior, the control can be forced into a compact mode, or even react dynamically to the application’s global density setting. This feature can be used to:

- Save vertical space on the page (applies to both text and icon tabs)
- Save horizontal space (icon tabs only; this is especially helpful when there are many tabs)
- Generally use less space on mobile devices
- Reduce noise when there are already more important visual elements on the screen (primarily icon tabs)

The property for the override is called `tabDensityMode`, which can be set to “Cozy”, “Compact”, or “Inherit”. “Cozy” is the default setting that renders the control in its regular dimensions. “Compact” reduces the control’s height and icon sizes (if applicable), even if there would be enough space for the cozy design. “Inherit” instructs the control to follow the global density mode defined for the application. For backward compatibility, the default setting is “Cozy”.

The following image shows some types of tabs with their default style (cozy, left) and the reduced density mode (compact, right).

*Tab density in cozy (left) and compact mode (right)*

\---

## Badge

A tab can have an attention badge to indicate that new items were added to that tab. Only display a badge if new items are triggered from outside the app. Do not display a badge when users add new items themselves.

*Tab with an attention badge*

### Badge in Default or Value State

You can add a badge to all types of icon tab bar. The badge inherits the state of its tab (default state or value state):

- For the default tab state, the default red badge is displayed.
- If the tab has a semantic state, the badge inherits the semantic color for the current state.

Don’t mix tabs in the default state with tabs that have a semantic state.

A badge on the chevron icon indicates that a tab within the overflow menu has received new items. The tab in question is indicated by a second badge on the item in the overflow menu.

*Semantic tab with a badge and a badge within the overflow menu*

### Badge Interaction

The badge becomes part of the tab. When the user selects a tab with a badge, the badge disappears. If a new item is added to the tab that is currently open, no badge is shown.

In addition, the badge inherits the interaction of its tab. For example, if a tab is moved using drag and drop, the attention badge moves with it.

*Selecting a tab with a badge*

## Guidelines

#### Apply the styles as follows:

- **Icons only**: Use this option if you have only 4-5 tabs that can be very clearly identified by their icon. If a short description is needed, use icons and labels.
- **Text only:** Use this option if you have more than 4-5 tabs, or if there are no clear icons to represent the content. The text-only style also allows for longer labels. Set the property `HeaderMode` to “Inline”.

#### If you use icon tabs, ensure the following:

- Use icons that clearly represent the tab content.
- Each tab must have a unique, easily distinguishable icon.
- Separator or connector icons must look visually different from tab icons.
- Apply labels consistently: either all tabs have them or none.

#### Implement the focus as follows:

- By default, the first tab opens. Technically you can override this, but it’s not recommended.
- Optionally, reopen the last tab selected by the user.

#### Additional guidelines:

- Don’t show a loading indicator above a tab while item counts are loading.
- Empty tabs:
  - **Hide** tabs with no content if users can’t add anything.
  - **Show** empty tabs only if they allow content creation (for example, notes or attachments).
- Use the tab bar only for switching tabs. Don’t create cross-navigation (for example, clicking an item in tab A to open tab B), as it confuses users and breaks back navigation.

## Localization

In left-to-right (LTR) layouts, the tabs in the icon tab bar are arranged in their natural order with the “More” overflow menu positioned on the right. When the application is localized for right-to-left (RTL) languages, the order of the tabs is reversed to match the reading direction, and the “More” menu moves to the left, so it remains at the end of the tab sequence. Visual indicators, such as the selection highlight, adapt to the new orientation.

*Icon tab bar in left-to-right (LTR) layout with “More”
menu on the right*

---

## segmented-button

+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
Message Strip (information)
+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
This guideline now covers both SAPUI5 and SAP Web Components. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).

## Intro

A segmented button is a group of connected buttons that users can select. The group appears as a single component divided into multiple segments.

Segmented button

### Component availability

This component is available in the following libraries:

+-----------x------------+-----------------------------------------------------------------x-----------------------------------------------------------------+----------------x-----------------+
Library                | Technical Name                                                                                                                    | Identifier
+-----------x------------+-----------------------------------------------------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit        | [sap.m.SegmentedButton](https://ui5.sap.com/#/entity/sap.m.SegmentedButton)                                                       | :badge, info, large, _, SAPUI5:
+-----------x------------+-----------------------------------------------------------------x-----------------------------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components     | [ui5-segmented-button](https://ui5.github.io/webcomponents/components/SegmentedButton/)                                           | Components:
+-----------x------------+-----------------------------------------------------------------x-----------------------------------------------------------------+----------------x-----------------+
SAP Web UI Kit (Figma) | [Segmented Button](https://www.figma.com/design/SILcWzK5uFghKun9jx6D7c/SAP-Web-UI-Kit?node-id=100495-10450\&t=LpIIvfuDWdfuZTIU-4) | :badge, info, large, _, Figma:

**Table (external_only)**
+----------------x-----------------+--------------------------------------------x--------------------------------------------+----------------x-----------------+
Library                          | Technical Name                                                                          | Identifier
+----------------x-----------------+-----------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit                  | [sap.m.SegmentedButton](https://ui5.sap.com/#/entity/sap.m.SegmentedButton)             | :badge, info, large, _, SAPUI5:
+----------------x-----------------+--------------------------------------------x--------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components               | [ui5-segmented-button](https://ui5.github.io/webcomponents/components/SegmentedButton/) | Components:
+----------------x-----------------+--------------------------------------------x--------------------------------------------+----------------x-----------------+
SAP Fiori for Web UI Kit (Figma) | [Segmented Button](https://www.figma.com/community/file/1494295794601744471)            | :badge, info, large, _, Figma:

## When to Use

+------------------------------------------------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------------------------------------------------+
When To Use
+------------------------------------------------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------------------------------------------------+
Do
Use the segmented button to:
- Let users choose from a small set of related options, such as “Year, Month, Day” or “Small, Medium, Large”.
+------------------------------------------------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------------------------------------------------+
Don't
Don’t use the segmented button to:
- Display a large number of options. Use a [split menu button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/#split-menu-button) or [radio button](https://www.sap.com/design-system/fiori-design-web/ui-elements/radio-button/) group instead.

+---------------------------------------------------------x---------------------------------------------------------+
Top Tips
+---------------------------------------------------------x---------------------------------------------------------+
- Use single selection mode when users should be able to select only one segment at a time.
- Use multiple selection mode when users should be able to select any combination of segments (SAP Web Components
only).
- Start with no selection when appropriate.
- For icon-only segmented buttons, add a tooltip to each segment with a clear label.

## Anatomy

The segmented button component consists of the following elements:
1. **Background:** Different background colors visualize the state of
the segmented button and indicate the interactive areas (segments).
2. **Text or icon:** Describes the action associated with each segment.
## Types

### Display types

The segmented button supports three display types:

**A:** Text only
**B:** Icon only
**C:** Text and icon

Display types

### Selection modes

There are two types of selection mode: single selection and multiple selection (SAP Web Components only).

**A: Single selection:** When the user clicks a segment, it becomes selected. All other segments are deselected. Only one segment is selected at a time.

**B: Multiple selection** :badge, info, medium, _, SAP Web Components: **:** When the user clicks a segment, it toggles between selected and unselected, without affecting the other segments. In multiple selection mode, the user can select any combination of buttons.

Selection modes

**Note:** The segmented button can be configured to start with no segments selected.

## States

### Component states

The segments of the segmented button each have one of two
states: enabled or disabled.
Component states: enabled (A) and disabled (B)
**A: Enabled:** In this state, the segment is
interactive, enabling the user to select it and trigger
its associated action.
**B: Disabled:** In this state, the segment is not
interactive and cannot be selected or triggered by the
user.
The segmented button can simultaneously contain both
enabled and disabled segments.
For more information, see [Component States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-component-states).

### Interaction states

Segmented buttons feature three interaction states – regular, hover, and down – each of which is paired with either an unselected or selected state.

#### Regular states

**A: Regular unselected** is the default, unselected state for a segment.
**B: Regular selected** is the state when the segment is selected.

#### Hover states

**A: Hover unselected** is the state when the cursor of a
pointing device (such as a mouse or pen) is currently
placed on an unselected segment that is in an enabled
state.
**B: Hover selected** is the state when the cursor of a
pointing device (such as a mouse or pen) is currently
placed on a selected segment that is in an enabled state.
#### Down state

**Down unselected** is the state when currently pressing
an unselected segment.
Down unselected state

For more information, see [Interaction States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-interaction-states).

### Focus state

The focus state determines which component receives input from the keyboard or another input device. Keyboard and assistive technology users rely on the focus state to follow the interaction.

The **focus** state is visualized by an additional border
around the segment.
Focused unselected (A) and focused selected (B) states
When interaction begins, focus is set on the active
segment.
For more information, see [Focus States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-focus-states).

## Behavior and Interaction

### Mouse interaction

#### Single selection

On mouse down, the segment becomes active and receives focus.

**A:** The user starts pressing an unselected segment.
**B:** When the user releases while still on the segment, the segment is selected, its action is triggered, and the previously selected segment is deselected.

Single selection interactions

#### Multiple selection :badge, info, large, _, SAP Web Components only:

**A:** The user starts pressing an unselected segment.
**B:** When the user releases while still on the segment, the segment is selected, its action is triggered, and the other segments remain unchanged.

Multiple selection interactions

#### Selection cancellation

If the user releases the mouse button outside the pressed segment, all segments remain in their current interaction state, and no action is triggered. This applies to both single selection and multiple selection.

Focus appears without any action being triggered

### Touch interaction

On touch devices, the behavior is similar to the mouse interaction, without the hover and focus states.

### Tooltips

When designing icon-only segmented buttons, always pair them with a tooltip that labels each icon-only segment.

Segmented button with tooltip – icon only

For more information, see [Using Tooltips](https://www.sap.com/design-system/fiori-design-web/v1-136/foundations/best-practices/ui-elements/using-tooltips).

## Responsiveness

By default, all segments share the same width, based on the longest text label. Alternatively, the component can be configured so that each individual segment adapts to the width of its text or icon.

Segmented button with different text lengths – default width and content fit

The segmented button supports cozy and compact [content densities](https://www.sap.com/design-system/fiori-design-web/foundations/visual/cozy-compact).

Compact (A) and cozy (B) content densities

## Accessibility

SAP follows international standards, such as WCAG and WAI-ARIA, and strives to make our business solutions accessible and inclusive.

For more information, see [Accessibility in SAP Fiori](https://www.sap.com/design-system/fiori-design-web/discover/sap-design-system/product-standards/accessibility-in-sap-fiori) and the [Accessibility Design Tools Handbook](https://www.sap.com/documents/2023/11/bc210d8b-977e-0010-bca6-c68f7e60039b.html).

### Keyboard navigation

The following key combinations are supported by the segmented button component.

**Table (col-width-30-70)**

Key Combination

**Tab**
segmented button. If the focus is already there, the
focus is moved to the next UI element.

**Shift \+ Tab**

**Right Arrow** or **Down Arrow**
button.

**Left Arrow** or **Up Arrow**
segmented button.

**Page Up** or **Home**
button.

**Page Down** or **End**
button.

**Spacebar** or **Enter/Return**

### Screen reader support

For additional details on screen reader support and Accessible Rich Internet Applications (ARIA), see [UI5 Screen Reader Support](https://ui5.sap.com/#/topic/33fae3482358438e93daea5232527093) and [WAI-ARIA Authoring](https://www.w3.org/TR/wai-aria-1.2/).

## Content

### Localization

The segmented button supports left-to-right (LTR) and right-to-left (RTL) reading directions.

Segmented button – left-to-right

## Framework Comparison

The table below summarizes the differences between SAPUI5 and SAP Web Components and lists the framework-specific patterns.

**Table (col-width-50-20-30)**
+---------------------------------------------------------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------------------------------------------------------+-------x-------+---------x----------+
Feature                                                                                                                                                                                                                                                                                                                       | SAPUI5        | SAP Web Components
+---------------------------------------------------------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------------------------------------------------------+-------x-------+---------x----------+
Multiple selection mode                                                                                                                                                                                                                                                                                                       |
Not аvailable | Available
See [Types – Selection Modes](https://www.sap.com/design-system/fiori-design-web/ui-elements/segmented-button/#selection-modes) and [Mouse Interaction – Multiple Selection](https://www.sap.com/design-system/fiori-design-web/ui-elements/segmented-button/#multiple-selection-badge-info-large-_-sap-web-components-only). |

---

## segmented-button-web-component

+------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------+
+--------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------+---------x----------+
## This page has been deprecated and is no longer available.
This page was deprecated with guideline version **1.142**.
#### Reason for deprecation
The guidelines for the SAP Web Component and the SAPUI5 component have been merged. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).
#### Looking for the latest information?
Visit the page below for the unified guideline with the most recent updates.
[Segmented Button](https://www.sap.com/design-system/fiori-design-web/ui-elements/segmented-button/)

---

## shell-search

Currently, it's available only as an experimental **SAP Web Component**. You can integrate it into SAPUI5 using [UI5 Web Components integration](https://help.sap.com/docs/SAPUI5/b2f662dd9d7a4ec680056733050b4d34/1c80793df5bb424091954697fc0b2828.html?version=LATEST\&locale=en-US).

## Intro

The shell search in the [shell bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/shell-bar/) helps users quickly find information and resources across your product or product suite. It provides a unified experience with results from all connected systems, enabling users to locate objects from a single entry point.

*Shell search*

## When to Use

Do
Use the shell search:
When a product-wide or cross-product search is required,
allowing users to find content, objects, or features
across the application or suite.
shell bar.

+------------------------------------------------------------------------x------------------------------------------------------------------------+
Top Tips
+------------------------------------------------------------------------x------------------------------------------------------------------------+
- Keep the search field expanded by default to improve discoverability.
- Keep the suggestion list short and relevant. If a search results page is available, use the button in the footer area of the suggestion list
to load more results.
- We recommend grouping search results rather than presenting them as a static list.
- When a search results page isn't available and a group has more than five results, use a *Show More* list item to load results progressively.

## Anatomy

The shell search has two main parts:

- **Search field:** Users type their queries in this input field.
- **Suggestion list (optional):** Displays a dropdown list of suggestions or results when the search field is focused or when the user starts typing. As the search input changes, the list updates to show relevant results.

### Search field

Anatomy of the shell search field

1. **Placeholder (mandatory):** A guiding text that is displayed when the search field is empty or not selected. See the [guidelines for placeholder text](https://www.sap.com/design-system/fiori-design-web/ui-elements/shell-search/usage#guidelines-for-placeholder-text).
2. **Magnifier icon button (mandatory):**
   The magnifier icon button (:search:) supports two actions, depending on the state of the search field:
   a. **Inactive State:** When the search is inactive (no query), the button expands or collapses the search field.
   b. **Active State:** When the search is active, the button executes the search.
3. **Search query:** Text the user enters in the search field. This input triggers the suggestion list with relevant results.
4. **Autocomplete (mandatory):** Provides real-time query completions and suggestions as users type.
5. ***Clear Search*** **button (mandatory):** Clears the search field.
6. **Scope selector (optional):** Lets users preselect a search scope, such as a business object, area, or type. The default scope is "All." Users can switch to a specific scope to search only within that scope.
7. **Advanced filtering (optional):** Provides quick access to advanced filter options through a filter icon button (:filter1:). The presentation, interaction pattern, and structure of advanced filters are flexible and tailored to individual product requirements.

### Suggestion list

Anatomy of the suggestion list (includes all types of list items for reference)

1. **Suggestions dropdown:** Contains the list of search results.
2. **Text message area (optional):** Displays contextual guidance to help users understand what to search for or to highlight newly introduced capabilities within the search experience.
3. **List:** Displays search results ordered by relevance. The top five best matches are shown first, followed by additional relevant results.
4. **Suggestion list item:** Displays search suggestions in the list using different list item types. See [Suggestion List Item Types](https://www.sap.com/design-system/fiori-design-web/ui-elements/shell-search/usage#suggestion-list-item-types).
5. **Tertiary footer button (optional):** When a dedicated search results page is available, a footer button provides access to the complete set of results.
6. **Action buttons (optional):**
   a. **Delete search history** (:decline1:)**:** Removes search history entries from the suggestions (as configured at application level).
   b. **Secondary action:** Supports secondary actions that don't affect the list item itself. These actions typically open additional information about the suggestion, allowing users to access more details without leaving the search context. Don't use the secondary actions for navigation or for performing business actions like approve or reject.
   See [List Item Actions](https://www.sap.com/design-system/fiori-design-web/ui-elements/shell-search/#list-item-actions)**.**

**> **Guideline:** **

Don't use an overlay or dim the rest of the screen when the shell search is active. The suggestion list dropdown
already provides the visual separation.

## Suggestion List Item Types

To help users easily identify how suggestions relate to their search query, matched text within each suggestion list item is highlighted in bold. The following types of suggestion list items are available out of the box.

### Standard list item

The standard list item is used in simple lists. It's
typically used to display less complex text suggestions
with a prefix icon.
Standard list items are also used to display search
history entries and query completion suggestions. Search
history entries are denoted by a history icon
(:history1:), while query completions are denoted by a
search icon (:search:).
### Text message area

The text message area is used to display contextual
guidance to help users understand what to search for, or
to highlight newly introduced capabilities within the
search experience.
**> **Guideline:** **

- Place the text message at the top of the suggestion list.
- Use sentence case for the title.
- Keep the text as short as possible.

### Group header

The group header organizes search results into meaningful
categories, making it easier for users to scan and
quickly choose the most relevant option.

Keep the group header text as short as possible.
### "Show More"

When no search results page is available, and results are
grouped with more than five items per group, add a *Show More*
list item at the end of each group to load additional results
inline.
If a search results page is available, don't use inline
loading. Instead, open a filtered search results view to
display additional results.
### List item with byline

A list item with a byline displays a title alongside an
avatar or icon. It's used to show either a single detail,
such as a title, or a more detailed set of information,
like a product name with key attributes or contact
details.
### Prefix list item

A prefix in a list item indicates its scope. The prefix
is typically shown when users apply commands to limit a
query to a specific category.
For example, in the query "apps: Customer", "apps:" acts
as the prefix. When you use queries in this way,
typeahead suggestions are disabled.
When building a query, prefix list items help define the scope of each part, guiding the search toward specific categories.

Example of a guided query

### "Search In" list item

"Search In" list items indicate whether results are
present within a specific category.
*Example of a "Search In" list item*
Format:
Search In [Scope]
Example:
Search In Sales Orders
**> **Guideline:** **

All list items support multi-line text wrapping except **“**&#x53;how Mor&#x65;**”** and **“**&#x53;earch I&#x6E;**”.** Keep text concise across all translations for readability.

## Behavior and Interaction

The following examples illustrate the search flow, from typing a query to displaying the list of suggestions.

### Search icon button: expand and collapse

The default state of the shell search can be either expanded, showing the whole search field, or collapsed, displaying only the search icon.

*Expanding and collapsing the shell search button*

**A: Default (collapsed)**
**B: Pressed (collapsed)**
**C: Active (expanded)**
**D: Hover (expanded)**
**E: Pressed (expanded)**
**F: Back to default (collapsed)**

**> **Guideline:** **

For better usability, we recommend keeping the search field expanded by default.

### Search query and trigger

When the user triggers the search field, the field transitions to the pressed state and provides immediate visual feedback. On focusing, the field becomes active, allowing the user to enter a query.

As the user types, results are loaded dynamically via autocomplete. A suggestion list appears below the search field, showing relevant suggestions based on the input.

*Basic search interaction flow*

When the search is triggered, the suggestion list popover closes, and the search field transitions to one of two states, depending on the navigation outcome: **Regular** or **Searched.**

*Two states after triggering the shell search*

**A: Regular state:** Applied when the search opens results in a new window or tab, or navigates within the product (for example, selecting an object from the suggestion list that opens its overview page).

**B: Searched state:** Applied when the search navigates to a dedicated search results page, or when returning to the page where the search was initiated after navigating elsewhere (for example, navigating from search results to an object page and then back to the results to continue exploration).

### Autocomplete

Autocomplete suggests system-generated values that start with the user's input. The first matching suggestion is offered as the autocomplete value, with the matching text visually emphasized. Users can accept the suggestion by pressing the Right Arrow key to complete the query.

*Autocomplete in shell search*

### Initial state

If the user hasn't enabled search tracking and has no usage history, and no help content is available, use an [illustrated message](https://www.sap.com/design-system/fiori-design-web/ui-elements/illustrated-message-web-component/) to prompt the user to enter a search query.
*No initial suggestions*

If search tracking is enabled and a search history
exists, list the queries or objects the user recently
accessed via the shell search. Display these suggestions
with a history icon (:history1:).
### Empty state

If the user hasn't enabled search tracking and has no usage history, and no help content is available, use an [illustrated message](https://www.sap.com/design-system/fiori-design-web/ui-elements/illustrated-message-web-component/) to indicate that no results are available.
*No suggestions or results*

If search tracking is enabled and a search history exists, show an
information message at the top of the suggestion list. Below the
message, list the recent queries or objects the user recently
accessed using the shell search. Display these suggestions with a
history icon (:history1:).
If fuzzy search is available, show users the most relevant results
for their current query using fuzzy matching. These can include:
- **Completions:** Suggest ways to complete what users have typed.
* **Corrections:** Suggest spelling corrections or synonyms.
Display both completions and corrections with a search icon
(:search:).
### Busy state

If loading suggestions takes more than one second, the
component automatically displays the loader.
*Loading suggestions*

### Clearing a search query

The *Clear Search* icon button appears when the search field is active and contains text. The query remains in the search field until the user removes it using the backspace key or by triggering the *Clear Search* button (:decline1:).

*Clearing a search query*

### List item actions

Users can remove individual search history entries from the suggestions list using the remove icon button (:decline1:). For mouse users, the delete button appears on hover. For keyboard users, it becomes visible when focused. On touch devices, the delete button is always visible.

Deleting suggestions from the search history

You can add an optional secondary action icon button to list items for actions that don't affect the list item itself. These actions typically display additional information, allowing users to access helpful content without leaving the search context. Avoid using secondary actions for navigation or for performing business actions on list items, such as approve and reject.

Secondary action button

## Responsive Behavior

### Desktop and tablet devices

*Responsiveness for desktop and tablet devices*

On tablets and desktop devices, the suggestion list appears as a dropdown. The suggestion list follows the responsive popover behavior. The search field is displayed either in expanded form or as a collapsed icon, depending on the available space in the shell bar.

For smaller breakpoints, the search field is represented by an icon button that expands to fill the full width of the shell bar. If there are multiple icon buttons in the shell bar, the search may move into the overflow menu. When space in the shell bar is limited, the search input expands to occupy the full width, and a *Cancel* button appears. The C*ancel* button clears any existing queries and collapses the search field.

*Shell search input field with smaller breakpoints*

### Phones

For mobile phones, the search field is represented by an icon button. If there are multiple icon buttons in the shell bar, the search may move into the overflow menu. When triggered, the icon button expands to fill the full width of the shell bar. If a suggestion list is configured, it opens in full screen mode.

*Responsiveness for phones*

If scope selection or advanced filtering is enabled, the scope selection opens in fulls creen mode.

*Scope selection for phones*

## Guidelines for Placeholder Text

The placeholder text must clearly indicate the scope of the shell search.

### General Rules

- Start the placeholder text with **Search**.
- Avoid truncation. Only add one or multiple scopes if there is sufficient space. Remember that other languages may require more space than English.
- Use title case.
- Align the placeholder text with your content and translation experts.

### Format

Use the following format:

**Table**
Scope

All

Single scope
**Examples**:
*Search in Sales*
*Search for Devices*
*Search by ID*

Multiple scopes
**Examples**:
*Search in Sales, Finance*
*Search for Tag, Keyword*
*Search by Task, Assignee, Due Date*
*Search by Company, Department, Team*

Scope text exceeds available space

**> **Hint:** **

Always expose the full placeholder text as a translatable string. Never concatenate text via the code. This can
result in translation errors.

Do
Full placeholder is visible.

---

## side-navigation


## Intro

The side navigation component provides a vertical menu that lets users open applications or modules in your product. It can be implemented as an embedded panel or as an overlay. In embedded mode, the navigation can be expanded or collapsed using the side navigation button. In overlay mode, the button opens the navigation as an overlay.

*Side navigation in embedded mode (left – expanded, center – collapsed) and overlay mode (right)*

## When to Use

+---------------------------------------------x----------------------------------------------+
When To Use
+---------------------------------------------x----------------------------------------------+
Do
Use side navigation:
- As the main navigation paradigm across the application, to navigate to multiple targets.
+---------------------------------------------x----------------------------------------------+
Don't
Don't use side navigation:
- For structuring the application layout or implementing application-specific logic.
- If your product has only a single navigation target.
- In a combination of embedded and overlay modes. Use either of them.

+-----------------------------------------------------------x-----------------------------------------------------------+
Top Tips
+-----------------------------------------------------------x-----------------------------------------------------------+
- Use the side navigation in embedded mode for easier discovery.
- Label each navigation item clearly and keep the text short to avoid wrapping.
- Group related items for quick access to information.
- We recommend using only one action button in the side navigation footer, focusing on the most essential task. Don't
nest elements in the footer area.
- The first element must be called "Home" and linked to the entry page.

## Anatomy

*Anatomy of the side navigation*

1. **Main navigation area:** This area contains primary navigation elements, including navigation groups (4), navigation list items (3, 5), and navigation child items (6). It has its own scrolling section.
2. **Fixed footer area:** The footer area remains fixed and always visible, independent of the main navigation scroll. A divider visually separates it from the navigation content. The footer provides access to a primary action through a quick action button and offers entry points to key areas of the product. Limit the fixed footer to a maximum of four elements: one action button and up to three navigation list items. For phone-first use cases, limit the footer to a single element: either an action button or a list item.
3. **Navigation group:** The side navigation supports up to three levels of nested items. The navigation group is the topmost, non-interactive, text-only level grouping. It can be expanded or collapsed to show or hide its nested navigation list items (which may further contain nested child items). When the side navigation is collapsed, navigation groups are hidden and indicated only by visual spacing.
4. **Navigation item:** A navigation list item consists of text and an icon and may optionally have a navigation target.
   a. **Without nested navigation elements:** A navigation item without nested child items always has a navigation target. In collapsed mode, only the icon is displayed.
   b. **With nested navigation elements:** A navigation item with nested navigation subitems, which can be collapsed or expanded.
5. **Navigation child item:** A navigation child item is nested within a navigation item and typically displays text only. If the child item opens an external link, an arrow (:arrow-right:) appears on the right to indicate an external link.
6. **Quick action:** Quick actions let users access the most common tasks quickly. The fast action button must always be placed at the top of the footer area.
7. **External link:** A navigation item with an external link that opens in a new tab or window, outside of the current application. External link is indicated by the right arrow icon (:arrow-right:) on the right.
8. **Child items in collapsed mode**: When the side navigation is collapsed, the child items appear in a popover.
9. **Overflow in collapsed mode:** When there isn't enough space in the main navigation area while in collapsed mode, the remaining navigation items are moved into a popover menu. If a navigation item contains child items, they are displayed in a cascaded menu.
10. **Overlay mode:** Displays the expanded side navigation as a popover. In this mode, selecting the side navigation button closes the popover instead of collapsing the navigation.

## Behavior and Interaction

### Embedded Mode

In embedded mode, the side navigation button expands or collapses the panel.

*Expanding and collapsing the side navigation in embedded mode*

### Overlay Mode

In overlay mode, the side navigation button opens and closes the popover. When a navigation item is selected, the popover closes.

*Opening the side navigation in overlay mode*

### Navigation Elements

When users trigger a navigation group, it expands to reveal its navigation items. The side navigation supports up to three levels. If there are more items than fit in the area, a scroll bar appears. The fixed footer always stays in place.

*Expanding navigation groups and navigation items*

*Expanded mode: Navigation element interaction, selection indication, and collapsing*

In collapsed mode, the child items appear in a popover.

*Collapsed mode: Navigation element interaction, selection indication*

In collapsed mode, navigation elements move into the overflow area when space is limited. If a navigation item in the overflow area contains child items, they are displayed in a cascaded menu.

Selecting an overflow element brings its parent navigation element into view above the overflow button.

*Embedded mode – collapsed state overflow*

## Responsiveness

### Embedded Mode

In embedded mode, the side navigation remains embedded across all screen sizes until it reaches the breakpoint at 600px (or size S).

Responsiveness for screen sizes up to size M

Users can choose to collapse the side navigation using the side navigation button.

Expanded and collapsed modes in embedded mode

On size S (600px) for non-touch devices, and on phones, it switches to a full-screen slide-in overlay over the content area. The side navigation will be hidden and can be opened using the side navigation button. On phones, the side navigation is displayed in full-screen mode over the content area, regardless of device orientation.

*Side navigation on size S and phones*

### Overlay-Only Mode

On the web and tablets, the side navigation appears as a responsive popover for all sizes. It follows the responsive behavior of the responsive popover control.

*Overlay mode – in web and tablets*

When navigation items are expanded, the overlay grows in height to display the expanded content. If there is more content than the popover's height, a scrollbar appears, and the fixed footer remains at the bottom of the popover.

*Overlay mode – popover height and scrollbar*

On phones, side navigation always appears as a full-screen dialog.

---

