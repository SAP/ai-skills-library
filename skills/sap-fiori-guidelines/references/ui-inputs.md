# SAP Fiori UI Elements: Inputs

This reference covers the following UI components:

- [Checkbox](#checkbox)
- [Date Picker](#date-picker)
- [Date Picker Web Component](#date-picker-web-component)
- [Date Time Picker Web Component](#date-time-picker-web-component)
- [Datetime Picker](#datetime-picker)
- [Input Field](#input-field)
- [Input Web Component](#input-web-component)
- [Range Slider](#range-slider)
- [Range Slider Web Component](#range-slider-web-component)
- [Select](#select)
- [Select Web Component](#select-web-component)
- [Slider](#slider)
- [Slider Web Component](#slider-web-component)
- [Switch](#switch)
- [Switch Web Component](#switch-web-component)

---

## checkbox

A checkbox lets users make a yes or no choice or turn a setting on or off. The checked state means the option is on or selected.

Checkboxes can also be grouped. Within a group, users can check any combination of options.

*Checkbox – unchecked and checked*

## When to Use

Do
Use the checkbox if:
- Only one option can be selected or deselected, for
example to accept terms of use. Use it only if the meaning
is obvious (single checkbox).
- You have a group or a list of options that can be
selected independently of each other (checkbox group).
- Your use case requires all available options to be
displayed right away without any user interaction (also in
read-only cases).
- The values of the option list are primary information
and need to be displayed right away.
- Changes to the settings need to be confirmed and
reviewed by the user before they are submitted. This helps
prevent users from changing settings accidentally.
- You want to group multiple suboptions under a parent
option, and require an intermediate selection state
(indeterminate state). This state indicates that some (but
not all) suboptions are selected.
*Use for a list of options that can be selected
independently of each other.*
## Anatomy

1. **Box:** Represents a selectable control with 3 possible states: selected, unselected, or [indeterminate](https://www.sap.com/design-system/fiori-design-web/ui-elements/checkbox/#indeterminate-state).
2. **Text:** Describes the purpose of the checkbox. If the purpose of the checkbox is already described by another element, such as a label, the checkbox
text is optional.

> **Guideline:** - If there is only one checkbox, you can use a label or a checkbox text, depending on the form format.
- If there is more than one checkbox, the label describes the whole group of checkboxes. In this case, use the `text` property of the checkbox to describe the individual checkboxes.

## Behavior and Interaction

### Checked/Unchecked

Clicking a checkbox toggles the state of the checkbox between checked and unchecked.

*Checkbox click interaction*

A checkbox doesn't apply a setting right away; the changes take effect after user confirmation via a triggering action button (such as *Save*).

### Indeterminate State

The main purpose of this state is to represent the mixed selection states of dependent input fields. If some (but not all) of the dependent fields are selected, the checkbox shows a partially selected state. This is only a visual state and can’t be achieved by direct user interaction.

*Checkbox selection states*

### Error Handling for a Checkbox Group

You can apply selection rules to a checkbox group. If an error occurs, the checkbox group is displayed in an error state. You can also display an error message below the checkbox group to explain the problem. For the error message, use the [message strip](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-strip/).

*Error handling for checkbox group*

## Responsiveness

### Checkbox Sizes

A checkbox can appear in two different sizes. In cozy mode, it is bigger than it is in compact mode. This makes the checkbox easier to select on touch devices. For more information on cozy and compact modes, see the article on [content density](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/visual/cozy-compact).

*Compact and cozy mode*

### Active Area

In both sizes, the touch/click area around the checkbox is bigger than the checkbox itself, making the checkbox easier to select. Clicking inside this area toggles the checkbox.

**Note**: Because the touch/click area doesn't include the label on the left, clicking the label won't toggle the checkbox.

*Checkbox touch/click area with label*

## Layout

### Checkbox Control

The checkbox control consists of a box and a text that describes the purpose of the checkbox. If the checkbox is checked, an indicator is shown inside the box.

Focus is indicated by a solid line that surrounds both the checkbox and the text to the right of it.

If the checkbox appears alone inside a form, the text can be omitted if the label in front of the checkbox takes over its function.

*Checkbox layout*

If there are several options to choose from in a form, the label describes the entire checkbox group, and the texts describe the individual checkboxes. When selection rules need to be explained, add the explanation in parentheses ( ) as part of the label component.

*Layout for a checkbox group*

### Text Formatting

Since **checkbox texts** are also a type of label, use **title case** to be consistent with other labels.  If a label is too long, it wraps to fit within the visible area. There is no limit on the number of lines a text can wrap.

**Exception:** If one or several of the checkbox texts is too long, or is framed as a phrase, use sentence case and appropriate ending punctuation.

*Short text in title case; Long text in sentence case; Text wrap*

### Labels and Text

For forms with **labels above the fields**, place the label above the checkbox group. For a single checkbox, use only a checkbox text.

*Labels for a checkbox group / single checkbox – form labels **above** fields*

For forms with **labels to the left of the fields**, place the label next to the group, aligned with the first checkbox field. For a single checkbox, use only a label, or only a checkbox text.

*Labels for a checkbox group / single checkbox – form labels **left** of fields*

> **Hint:** **Don't use empty labels to arrange the checkboxes.** Creating a label in front of each checkbox and leaving the text
empty looks fine – nobody sees the label, and the checkboxes are aligned correctly underneath each other. However,
the screen reader will notice these labels and read each of them as “label”. Instead, use the layout data property
(layoutData) for the checkbox. In this property, force a line break (linebreak) and set the value of the indents in
sizes L and M (indentL, indentM) according to the value of the label span in the simple form (labelSpanL,
labelSpanM).

## States

### Interaction States

A checkbox can appear in different interaction states depending on
how a user interacts with it.
*Checkbox interaction states*
**A. Regular:** Default appearance when the checkbox is enabled.
**B. Hover:** Highlights the checkbox when the cursor moves over it.
**C. Disabled:** Shows the checkbox is unavailable. Users can’t select or change it.
**D. Read Only:** Displays a fixed selection that can't be changed by the user.
**E. Display Only:** Shows a non-interactive checkbox for visual reference only.
### Value States

In addition to interaction states, checkboxes can be styled to reflect intent or meaning, which are indicated using [semantic colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/morning-horizon#semantic-colors).
**A. Information:** Provides context or neutral guidance.
**B. Positive:** Highlights a successful or desirable option.
**C. Critical:** Draws attention to a potentially risky or sensitive choice.
**D. Negative:** Signals an irreversible or destructive option, such as file or account deletion or service cancelation.
**> **Information:** **

For details on the different states, see [States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/interaction-design-foundations-states).
For more information on semantic colors for value states, see [Using Semantic and Industry-Specific Colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/how-to-use-semantic-colors).

## Localization

In left-to-right languages like English, the checkbox is typically aligned to the left of the label text. For right-to-left languages like Arabic or Hebrew, the checkbox should be aligned to the right of the label text to maintain consistency with the reading flow.

*Left-to-right checkbox use*

---

## date-picker

+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
Message Strip (information)
+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
This guideline now covers both SAPUI5 and SAP Web Components. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).

## Intro

The date picker is a UI component used to select a single date using touch, mouse, or keyboard input. It supports manual entry in the input field and calendar-based selection via the date picker button.

Date picker

### Component availability

This component is available in the following libraries:

+-----------x------------+-------------------------------------------------------x-------------------------------------------------------+----------------x-----------------+
Library                | Technical Name                                                                                                | Identifier
+-----------x------------+---------------------------------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit        | [sap.m.DatePicker](https://ui5.sap.com/#/entity/sap.m.DatePicker)                                             | :badge, info, large, _, SAPUI5:
+-----------x------------+-------------------------------------------------------x-------------------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components     | [ui5-date-picker](https://ui5.github.io/webcomponents/components/DatePicker/)                                 | Components:
+-----------x------------+-------------------------------------------------------x-------------------------------------------------------+----------------x-----------------+
SAP Web UI Kit (Figma) | [Date (Range) Picker](https://www.figma.com/design/SILcWzK5uFghKun9jx6D7c/SAP-Web-UI-Kit?node-id=165167-1225) | :badge, info, large, _, Figma:

**Table (external_only)**
+----------------x-----------------+---------------------------------------x---------------------------------------+----------------x-----------------+
Library                          | Technical Name                                                                | Identifier
+----------------x-----------------+-------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit                  | [sap.m.DatePicker](https://ui5.sap.com/#/entity/sap.m.DatePicker)             | :badge, info, large, _, SAPUI5:
+----------------x-----------------+---------------------------------------x---------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components               | [ui5-date-picker](https://ui5.github.io/webcomponents/components/DatePicker/) | Components:
+----------------x-----------------+---------------------------------------x---------------------------------------+----------------x-----------------+
SAP Fiori for Web UI Kit (Figma) | [Date Picker](https://www.figma.com/community/file/1494295794601744471)       | :badge, info, large, _, Figma:

## When to Use

+-----------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------+
When To Use
+-----------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------+
Do
Use the date picker to:
- Let users select a single date.
- Let users navigate directly from one month or year to another.
+-----------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------+
Don't
Don’t use the date picker to:
- Provide a combined date and time input component. In this case, use the [date/time picker](https://www.sap.com/design-system/fiori-design-web/ui-elements/datetime-picker/).
- Keep the calendar visible and prominent or offer multiple days selection. Use the [calendar](https://www.sap.com/design-system/fiori-design-web/ui-elements/calendar/) instead.
- Enter a date range. Use the [date range selection](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-range-selection/) instead.

+---------------------------------------------------------x----------------------------------------------------------+
Top Tips
+---------------------------------------------------------x----------------------------------------------------------+
- Support direct date entry by typing the value in the input field.
- Choose the appropriate date picker type (date, month, or year) depending on the required level of granularity.
- Use value-state messages to provide meaningful and actionable feedback.
- Define minimum and maximum dates when business rules apply to prevent invalid input at the source.
- Use placeholders to clearly indicate the expected date format.
- Use an icon button, text button, or a link to trigger the opening of the popover when you need to hide the input
field.
- Provide tooltips on the date picker button and the calendar to improve clarity and usability.
- Offer a “current date” shortcut to help users return quickly to the present moment.
- Enable special dates with a legend to highlight important days, such as holidays or events.
- Add a footer with *OK* and *Cancel* buttons when you need users to explicitly confirm the date selection.
- Use mixed calendar views only when users need to compare or work across different calendar systems.
- Apply the appropriate content density (compact or cozy) based on device size and interaction mode.

## Anatomy

A date picker consists of the following elements:
1. **Date picker input field:** The container in which a user enters data.
2. **Date picker button:** The button that opens the date picker popover.
3. **Date picker popover:** The popover that contains the calendar.
Note: For more detailed explanation of what the calendar container contains, refer to the [calendar](https://www.sap.com/design-system/fiori-design-web/ui-elements/calendar/).
## Types

The date picker supports several configuration modes that control the level of selection. Each mode defines whether the component functions as a date, month, or year picker.

### Basic date picker

The basic date picker allows users to enter a date by
either typing it in the input field or selecting it from
the calendar.

### Month picker

This type supports selecting a specific month. The
calendar opens in month view, where only months can be
selected. Users can also type a month directly in the
input field.
Note: Day selection is not supported in this mode.
### Year picker

This type allows users to pick a specific year. The
calendar opens in year view, where only years can be
selected. Users can also type in the input field to enter
the desired year.
Note: Day and month selections are not available in this
mode. Year ranges are part of the year view and cannot be
selected independently.
### Mixed calendar

The mixed calendar displays a combination of two
different calendars into one calendar view. One of the
calendars is defined as primary and the other one as
secondary.
Note: Do not display week numbers for this type of
calendar.
## States

The date picker component supports different states to reflect its current interaction and validation status. Each state indicates whether the component is available for interaction and whether the entered value is valid or requires attention.

### Component states

**A. Enabled:** Supports manual date entry in the input field
and calendar-based selection via the date picker button.
Date picker component states
**B. Disabled:** The component is visible but not interactive.
**C. Read-only:** Displays a value that cannot be edited.
Supports focus for copying only.
For more information, see [Component States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-component-states).

### Interaction states

The date picker supports the following interaction
states, which indicate the current interaction status of
the input field and the date picker button:
**A. Regular:** Displays the default interaction state of
the input field and the date picker button.
**B. Hover on input:** Displays the hover state when the
cursor is over the input field.
**C. Hover on button:** Displays the hover state when the
cursor is over the date picker button.
**D. Active:** Displays the focused state of the input
field ready for user input.
**E. Active button state:** Displays the pressed state of
the date picker button while the calendar is open.
For more information, see [Interaction States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-interaction-states).

### Value states

The date picker input supports four value states to indicate
different validation or informational statuses:
Date picker value states
**A. Negative:** Indicates an invalid date value.
**B. Critical:** Indicates a date value that requires attention.
**C. Positive:** Confirms a valid date value.
**D. Information:** Signals neutral status or context without
implying errors or warnings.
For more information, see [How to Use Semantic Colors](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/how-to-use-semantic-colors).

### Value states with value state message

When users enter a date in the input field, the date
picker displays value state messages that indicate
whether the entered date is valid or requires attention.
These states provide visual feedback and messages that
help users understand whether the value is negative (A),
requires attention (B), valid (C), or contains additional
information (D).
Note: The positive state does not display an input
message popover.
### Value state messages in the date picker popover

When the date picker popover is open, the value state message appears inside the popover.

Date picker value state messages in the popover

For more information, see [Value States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-value-states).

### Focus state

The focus state indicates which element is currently
focused.
Date picker focus state
**A. Unfocused:** Applies to elements that are not focused.
**B. Focused:** Displays a visible focus highlight around
the input field or the selected calendar element (date,
month, year, and the previous/next buttons).
For more information, see [Focus States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-focus-states).

### Selection state

The selection state indicates whether an element is selected.
**A. Unselected:** Displays the default, unselected state.
**B. Selected:** Displays the selected state with visual distinction.
For more information, see [Selection States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-selection-states).

## Behavior and Interaction

Users can set the date in two ways:

- By typing in the input field.
- By choosing a date from the calendar. After selection, the calendar closes and the date appears in the date input field.

### Input field entry

When the user types a valid date in the input field, the
calendar updates to reflect the entered date.
Date picker input entry
**A. Regular:** Displays the input field with placeholder text.
**B. Input active:** Displays the focused input field.
**C. Date entered:** Displays the entered date.
To confirm the entry, the user presses **Enter** or clicks
outside the input field. If the value is valid, the date is
applied; otherwise, a value state message appears.
### Date selection

Clicking the date picker button (A) opens the calendar
(B), allowing users to select a date. Once a date is
selected, the value is updated in the input field, and
the calendar closes automatically (C).
The calendar previous/next buttons navigate between month
and year views. Selecting the current month switches the
calendar to the month view, where users can choose a
different month. After a month is selected, the calendar
returns to the day view.
The same interaction pattern applies when selecting a
year: choosing a year switches back to the day view.
Note: The user can decide not to select a date after
opening the calendar. Clicking outside of the component
closes the calendar and no selection is made.
### Opening the date picker by another component :badge, info, large, _, SAPUI5 Only:

The date picker can be opened by a separate component,
such as a button, an icon button, or a link, which acts
as the trigger for the calendar popup. The opening
component should include clear visible text or a tooltip
describing the action (for example, “Open Date Picker”).
### Tooltip

The date picker supports tooltips at two levels:
- Input field (optional)
- Date picker button.
Note: For detailed guidance on interaction patterns and tooltip behavior, please refer to the [tooltip](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/using-tooltips).
The calendar also supports tooltips for the following elements:
- Today
- Non-working days
- Previous/next
- Month and year.
## Responsiveness

### Date picker sizes

The date picker adapts to different screen sizes and interaction modes to remain usable and efficient across all devices. Its responsive behavior ensures consistent date selection regardless of form factor.

- **Compact** reduces component dimensions to display more information within the interface, making it suitable for devices operated with a mouse and keyboard.
- **Cozy** provides larger component dimensions optimized for comfortable fingertip interaction, making it ideal for touch-operated devices.

For more information, see [Content Density (Cozy and Compact)](https://www.sap.com/design-system/fiori-design-web/foundations/visual/cozy-compact).

### Size S (Smartphones)

On mobile phones, the calendar opens in cozy mode and a full-screen dialog to optimize the experience for small screens. The dialog title uses the input field’s label. If no label is provided, it defaults to “Select”. Selecting a date updates the input field and closes the dialog. A *Cancel* button in the footer allows users to close the dialog without making a selection.

Date picker on smartphone in cozy mode

### Size M and L

On size M (tablets) and L (desktops), the date picker opens as a popover containing a calendar. Selecting a date updates the value in the input field and closes the popover. Clicking anywhere outside the popover cancels the interaction and dismisses it without changing the value. Only one date can be selected. For multiple date selection, refer to the [calendar](https://www.sap.com/design-system/fiori-design-web/ui-elements/calendar/).

Date picker in compact and cozy mode

## Accessibility

SAP follows international standards, such as WCAG and WAI-ARIA, and strives to make our business solutions accessible and inclusive.

For more information, see [Accessibility in SAP Fiori](https://www.sap.com/design-system/fiori-design-web/discover/sap-design-system/product-standards/accessibility-in-sap-fiori) and the [Accessibility Design Tools Handbook](https://www.sap.com/documents/2023/11/bc210d8b-977e-0010-bca6-c68f7e60039b.html).

### Keyboard navigation

The following keyboard combinations are supported by the SAPUI5 date picker component.

**Table (col-width-30-70)**

Key Combination

**Tab**
popover remains closed. If the focus is already on the
input field, the focus is moved to the next UI element.
If the date picker popover is open and focus is there, the
Tab key navigates between the elements inside the popover.

**Shift \+ Tab**

**Alt \+ Up Arrow or**
moves to the calendar.
**Alt \+ Down Arrow**
moves back to the input field.

**F4**
moves to the calendar.
If the picker popover is opened, the view is changed to
month selection.

**Shift \+ F4**
year selection.

**Enter**
and closes the popover.

**Esc**
selection.

**Home**
**End**

**Right Arrow**
one position to the right or left.
**Left Arrow**
**Ctrl \+ A**

**Delete**
If text is selected, it gets deleted.
**Backspace**
**Shift \+ Right Arrow**
starting at the cursor position.
**Shift \+ Left Arrow**
**Shift \+ Ctrl \+ Right Arrow**
starting at the cursor position.
**Shift \+ Ctrl \+ Left Arrow**
**Ctrl \+ Right Arrow**
**Ctrl \+ Left Arrow**
**Ctrl \+ C оr Ctrl \+ Insert**

**Ctrl \+ X оr Shift \+ Delete**

**Ctrl \+ V оr Shift \+ Insert**

**Page Up**
incremented or decremented by one day.
**Page Down**
next or previous month. The focus stays on the same day,
if possible. If the month has fewer days, the focus moves
to the next possible day before (for example, January 31
will lead to February 28).

**Shift \+ Page Up**
incremented or decremented by one month.
**Shift \+ Page Down**
next or previous year.

**Shift \+ Ctrl \+ Page Up**
decrements the date by one year.
**Shift \+ Ctrl \+ Page Down**
or decremented by 10 years.

### Screen reader support

For details on screen reader support and Accessible Rich Internet Applications (ARIA), see the [UI5 Screen Reader Support](https://ui5.sap.com/#/topic/33fae3482358438e93daea5232527093) and [WAI-ARIA Authoring](https://www.w3.org/TR/wai-aria-1.2/).

## Content

### Placeholder

A custom placeholder text can be provided in the input
field to indicate the expected date format. If no
placeholder is provided, the date picker displays a
sample date on December 31 of the current year, formatted
according to the configured format pattern.
### Display format

It is possible to customize the formatting of dates in the input. Supported formats include short, medium, and long, as well as specific custom formats. These formats adjust to different local settings that have been configured in the browser.

Date picker with different display formats

### Value format

The value format defines how the date is parsed and stored internally, and depending on the level of detail specified, also determines which calendar view (days, months, or years) is presented to the user.

**A.** When set to YYYY-MM-DD, the picker displays days for selecting a date.
**B.** When set to YYYY-MM, the picker displays months for selecting a month.
**C.** When set to YYYY, the picker displays years for selecting a year.

Date picker value format examples

**> **Guideline:** **

Whenever possible, we recommend using the user's default date format for clarity and familiarity.

### Special dates with legend :badge, info, large, _, SAPUI5 Only:

Special dates can be marked in the calendar to visually distinguish and communicate their meaning (for example, holidays, booked/unavailable days, events, or reminders). The dates are mapped to a legend that explains their meaning. The legend comes with 20 predefined color placeholders plus the standard colors for today, selected, working, and non-working day. It can appear as a static element that stays visible next to the calendar, or as a dynamic option opened through a *Special Days* button. Choose the static or dynamic presentation based on available screen space and legend complexity.

Date picker with special dates and legend

### Localization

The date picker supports left-to-right (LTR) and right-to-left (RTL) reading directions.

Left-to-right date picker

## Features

### Restricted date range

Define a minimum and maximum date to restrict the
selectable date range. Only dates within this range can
be selected.

### Custom initial focus date :badge, info, large, _, SAPUI5 Only:

By default, the calendar opens with focus on the current
day, but the initial focus date can be customized to any
target date. For example, when a user is choosing an
event end date, the focus can propose a date after the
event’s start date, so the user lands in the relevant
range.
### Current date :badge, info, large, _, SAPUI5 Only:

The current date can be enabled as a quick navigation
through the “Today” button, which jumps the calendar to
the current date. When used in month, year or year-range
picker view, the calendar navigates to the default date
picker view and highlights today.
### Footer :badge, info, large, _, SAPUI5 Only:

An optional footer with *OK* and *Cancel* buttons can be
added to the date picker popover. When used, the popover
remains open until the selection is either confirmed or
canceled via these buttons.
Add a footer only when users need to review, confirm, or
adjust multiple values before applying the selection (for
example, selecting a date and then changing the month or
year).
### Date input shortcuts

A specific date can be entered directly into the input field by typing a shortcut and pressing *Enter* to confirm the selection:

- "today"
- "yesterday"
- “tomorrow”
- “in X days”
- “X days ago”
- “next month”
- “last month”
- “next year”
- “last year”

Note: “Days” can be replaced with “months” or “years” in the relevant shortcuts.

Using shortcuts in the date picker input

### Supported calendars

The date picker supports five calendar types – Gregorian (default), Islamic, Japanese (A), Persian (B), and Buddhist (C).

Examples of date picker with different calendar types

### Calculating calendar weeks

The calendar allows defining the first day of the week, and the first week of the year. This allows you to select different calendar conventions, such as Default (A), which is based on the active format locale, ISO 8601, Middle Eastern (B), or Western Traditional (C).

Note: For more information, see the [calendar](https://www.sap.com/design-system/fiori-design-web/ui-elements/calendar/).

Examples of date picker with different calendar options

### Show/Hide week numbers :badge, info, large, _, Web Components Only:

The date picker allows to hiding the week numbers from the dedicated column to the left of the calendar grid. This is typically used in views where planning by week is not relevant. Whether week numbers are shown depends on the app use case and should be configured accordingly.

Date picker with and without week numbers

## Framework Comparison

Some behaviors differ between frameworks due to implementation specifics. The table below summarizes the differences between SAPUI5 and SAP Web Components and lists the framework-specific patterns.

**Table (col-width-50-20-30)**
Feature                                                                                                                                                                                                                                                                                             | SAPUI5        | SAP Web Components

The date picker can be opened by another component. For more information, see the [Open time picker popover by another component](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-picker/#opening-the-date-picker-by-another-component-badge-info-large-_-sapui5-only) section. | Available     | Not available

Special dates can be marked in the calendar. For more information, see the [Special dates with legend](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-picker/#special-dates-with-legend-badge-info-large-_-sapui5-only) section.                                               | Available     | Not available

The initial focus date can be customized to any target date. For more information, see the [Custom initial focus date](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-picker/#custom-initial-focus-date-badge-info-large-_-sapui5-only) section.                               | Available     | Not available

The “Today” button can be enabled as a quick navigation component. For more information, see the [Current date](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-picker/#current-date-badge-info-large-_-sapui5-only) section.                                                   | Available     | Not available

A footer with *OK* and *Cancel* buttons can be added to the date picker popover. For more information, see the [Footer](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-picker/#footer-badge-info-large-_-sapui5-only) section.                                                 | Available     | Not available

The week numbers to the left of the calendar grid can be hidden. For more information, see the [Show/Hide week numbers](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-picker/#showhide-week-numbers-badge-info-large-_-web-components-only) section.                          | Not available | Available

**\**

---

## date-picker-web-component

+------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------+
+--------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------+---------x----------+
## This page has been deprecated and is no longer available.
This page was deprecated with guideline version **1.145**.
#### Reason for deprecation
The guidelines for the SAP Web Component and the SAPUI5 component have been merged. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).
#### Looking for the latest information?
Visit the page below for the unified guideline with the most recent updates.
[Date Picker](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-picker/)

---

## date-time-picker-web-component

+------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------+
+--------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------+---------x----------+
## This page has been deprecated and is no longer available.
This page was deprecated with guideline version **1.142**.
#### Reason for deprecation
The guidelines for the SAP Web Component and the SAPUI5 component have been merged. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).
#### Looking for the latest information?
Visit the page below for the unified guideline with the most recent updates.

[Date/Time Picker](https://www.sap.com/design-system/fiori-design-web/ui-elements/datetime-picker/)

---

## datetime-picker

+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
Message Strip (information)
+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
This guideline now covers both SAPUI5 and SAP Web Components. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).

## Intro

The date/time picker is a UI component that lets users select both date and time values within a unified input field. It combines a calendar view with time selection, supporting both compact and cozy display modes.

Date/time picker

### Component availability

This component is available in the following libraries:

+-----------x------------+------------------------------------------------------x------------------------------------------------------+----------------x-----------------+
Library                | Technical Name                                                                                              | Identifier
+-----------x------------+-------------------------------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit        | [sap.m.DateTimePicker](https://ui5.sap.com/#/entity/sap.m.DateTimePicker)                                   | :badge, info, large, _, SAPUI5:
+-----------x------------+------------------------------------------------------x------------------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components     | [ui5-date-time-picker](https://ui5.github.io/webcomponents/components/DateTimePicker/)                      | Components:
+-----------x------------+------------------------------------------------------x------------------------------------------------------+----------------x-----------------+
SAP Web UI Kit (Figma) | [Date Time Picker](https://www.figma.com/design/SILcWzK5uFghKun9jx6D7c/SAP-Web-UI-Kit?node-id=195120-61096) | :badge, info, large, _, Figma:

**Table (external_only)**
+----------------x-----------------+-------------------------------------------x--------------------------------------------+----------------x-----------------+
Library                          | Technical Name                                                                         | Identifier
+----------------x-----------------+----------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit                  | [sap.m.DateTimePicker](https://ui5.sap.com/#/entity/sap.m.DateTimePicker)              | :badge, info, large, _, SAPUI5:
+----------------x-----------------+-------------------------------------------x--------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components               | [ui5-date-time-picker](https://ui5.github.io/webcomponents/components/DateTimePicker/) | Components:
+----------------x-----------------+-------------------------------------------x--------------------------------------------+----------------x-----------------+
SAP Fiori for Web UI Kit (Figma) | [Date Time Picker](https://www.figma.com/community/file/1494295794601744471)           | :badge, info, large, _, Figma:

## When to Use

+-----------------------------------------------------------------------x------------------------------------------------------------------------+
When To Use
+-----------------------------------------------------------------------x------------------------------------------------------------------------+
Do
Use the date/time picker to:
- Let the user select both date and time in a single input field.
+-----------------------------------------------------------------------x------------------------------------------------------------------------+
Don't
Don’t use the date/time picker to:
- Let the user select only a date. Use the [date picker](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-picker/) instead.
- Let the user select only a time. Use the [time picker](https://www.sap.com/design-system/fiori-design-web/ui-elements/time-picker/) instead.

+----------------------------------------------------------x----------------------------------------------------------+
Top Tips
+----------------------------------------------------------x----------------------------------------------------------+
- Define minimum and maximum limits to restrict date and time selection to an approved range.
- Configure minute and second step values to create predictable increments for time selection.
- Allow users to manually enter values and rely on the component to parse valid input automatically.
- Offer a “current date” or “current time” shortcut to help users return quickly to the present moment.
- Use interaction and value states to provide clear visual and semantic feedback during user input.
- Use Compact or Cozy modes to adapt the component to different screen sizes.
- Use an icon button, text button, or link to trigger the opening of the popover when space is limited or when
required by application logic.
- Provide tooltips on the date/time picker button and calendar or clock selection interfaces to improve clarity and
discoverability.
- Support week numbers when the business use case requires weekly planning.
- Show a timezone indicator when the input depends on regional time accuracy.
- Use mixed calendar mode when you need to support two calendar systems in a single view.

## Anatomy

A date/time picker consists of the following elements:

1. **Date/time picker input field:** Displays the selected value and enables manual entry.
2. **Date/time picker button:** Opens a popover for selecting date and time.
3. **Time picker container:** Displays the clock interface and lets users select a time in hours, minutes and seconds.
4. **Footer:** Provides the *OK* and *Cancel* actions.
5. **Date picker container:** Displays the calendar for selecting a date.

Data/time picker anatomy

**> **Guideline:** **

For more details on date and time containers, see the [date picker](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-picker/) and the [time picker](https://www.sap.com/design-system/fiori-design-web/ui-elements/time-picker/).

## Types

### Basic date/time picker

The date/time picker lets users select both the date (day, month, and year) and time (hours, minutes, and seconds) in a combined input.

Basic date/time picker

### Restricted date range

The date/time picker component can be configured with minimum and maximum limits so the user can select only within the valid range.

Restricted date/time picker

## States

The date/time picker incorporates various states to ensure a clear and intuitive user experience, enhancing both interaction and status validation. Each state visually communicates the component's current status and supports user navigation.

### Component states

**A. Enabled:** The component is interactive and can receive input.
**B. Disabled:** The component is not interactive and cannot receive input.
**C. Read-only:** The value is visible but cannot be edited.
For more information, see [Component States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-component-states).

### Interaction states

The date/time picker has five interaction states, which represent different parts of the component:

**A. Regular:** The default state of the input field and the button.
**B. Hover on input:** When the cursor hovers over the input field.
**C. Hover on button:** When the cursor hovers over the date/time picker button.
**D. Active:** The input field is focused, allowing the user to enter or edit text.
**E. Active button state:** The date/time picker button is active, displaying the calendar and the clock.

Date/time picker interaction states

For more information, see [Interaction States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-interaction-states).

### Value states

The date/time picker input field supports four value
states to indicate validation and guidance: negative,
critical, positive, and information. Each state is
represented by a distinct semantic color to help users
quickly understand the meaning: red for negative (A),
yellow for critical (B), green for positive (C), and blue
for information (D).
For more information, see [How to Use Semantic Colors](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/how-to-use-semantic-colors).

### Value states with value state message

**A. Negative:** Signals an error and instructs the user
to correct the value.
Date/time picker value states with value state message
**B. Critical:** Indicates a potential issue that
requires attention but is not an error.
**C. Positive:** Confirms a valid input.
Note: The positive state does not display a message
popover.
**D. Information:** Displays general information or
guidance that is not critical but can help users complete
their tasks.
For more information, see [Value States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-value-states).

### Focus state

The focus state determines which component receives the user input when using an input device, such as a keyboard. By default, the focus is on the current date, but another date can be set as the initial focus if needed, depending on the app’s context or user flow.
**A. Unfocused** state applies to all date and time units that are not focused.
**B. Focused** state is visualized by an additional border around the focused date time units.

Unfocused and focused states for the date/time picker

**> **Guideline:** **

When focus is applied to the hours, minutes, and seconds output, it maintains a selection state. However, for the
AM/PM toggle button, the focus is detached and does not follow the selection.

For more information, see [Focus States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-focus-states).

### Selection state

The selection state indicates which date or time option is currently chosen by the user. The state is applied after the user selects an element, clearly distinguishing the selected element from others.
**A. Unselected:** The state occurs when an element is not selected, displaying the element in its regular (default) state.
**B. Selected:** The state shows that an element is selected and visually differs from the unselected state.

Selected and unselected states for the date/time picker

For more information, see [Selection States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-selection-states).

## Behavior and Interaction

### Manual entry

The date/time picker component provides the option to
manually enter date and time values directly into the
input field. The manually typed values should follow the
format shown in the placeholder text.
When the user clicks the input field (A), the component
becomes active and focused (B). After the user enters a
valid date and time according to the expected format, the
component automatically parses this value (C). The newly
entered date and time then display within the field,
reflecting the successful input.
### Date/time picker button and popover interaction

The date/time picker component includes a dedicated button that opens a popover with calendar and clock selection controls. When the user clicks this button (A), the popover (B) appears, providing an intuitive interface for navigating through months and years, selecting a date, and adjusting time values. After choosing the desired date and time, the user confirms the selection by clicking the *OK* button in the footer, which closes the popover and populates the input field. If the user clicks *Cancel* or anywhere outside the popover, the selection is discarded, and the input field retains its placeholder text.

Date/time picker button and popover interaction

### Opening the date/time picker by another component :badge, info, large, _, SAPUI5 Only:

The date/time picker can be opened by another component such as text button, icon button, or link. In this case, the component appears as a popover with date and time selection without the input field.

Date/time picker opened by another component

### Tooltip

The date/time picker supports tooltips for the date section, the time section, and the input (optional). For more information and visuals, see the [calendar](https://www.sap.com/design-system/fiori-design-web/ui-elements/calendar/) and the [time picker](https://www.sap.com/design-system/fiori-design-web/ui-elements/time-picker/).

Tooltip on the date/time picker button

## Responsiveness

### Date/time picker sizes

The date/time picker is responsive and works on all devices and form factors. The examples below illustrate how the component adapts its size and layout based on screen resolution and interaction type. For sizes S and M use Cozy mode, whereas for size L and XL, use Compact mode. For more information, see [Content Density (Cozy and Compact)](https://www.sap.com/design-system/fiori-design-web/foundations/visual/cozy-compact).

### Size S (Smartphones)

On smaller devices, the user can choose the date and time value in arbitrary order by tapping the segmented button on top of the screen. Be aware that the [popover](https://www.sap.com/design-system/fiori-design-web/ui-elements/popover/) is superimposed on the [input field](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/) during the selection process for **mobile S sizes**.

The user can select the desired date from the [calendar](https://www.sap.com/design-system/fiori-design-web/ui-elements/planning-calendar/), and the time from the clock. For the time, it’s possible to select hours, minutes, and even seconds. Clicking a date in the calendar automatically takes the user to the time selection screen.

When the user selects *OK*, the popover closes, and the selected date and time appear in the input field. When the user selects *Cancel*, the action is canceled, and the input field remains unchanged.

Date/time picker in size S cozy mode

### Size M (Tablets)

The popover opens as a standard overlay near the [input field](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/), offering a balanced layout that supports both touch input and manual text entry. The interaction is the same as that on Size S.

Date/time picker in size M cozy mode

### Size L (Desktops)

The date/time picker appears as a [popover](https://www.sap.com/design-system/fiori-design-web/ui-elements/popover/) when the user clicks the date/time button in the [input field](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/). The user can then select the desired date from the calendar and the time from the clock. For the time, it’s possible to select hours, minutes, and seconds.

When the user clicks the *OK* button, the popover closes, and the selected date and time appear in the input field. When the user selects *Cancel*, the action is canceled, and the input field remains unchanged.

If there is no value in the input field, no date is selected. The user needs to explicitly pick a date from the calendar. If a date is already selected and the user changes the year or the month, the date selection is cleared, and the user needs to pick again.

Date/time picker in size L compact mode

## Accessibility

SAP follows international standards, such as WCAG and WAI-ARIA, and strives to make our business solutions accessible and inclusive.

For more information, see [Accessibility in SAP Fiori](https://www.sap.com/design-system/fiori-design-web/discover/sap-design-system/product-standards/accessibility-in-sap-fiori) and the [Accessibility Design Tools Handbook](https://www.sap.com/documents/2023/11/bc210d8b-977e-0010-bca6-c68f7e60039b.html).

### Keyboard navigation

The following keyboard combinations are supported by the SAPUI5 Date/time picker component.

Note that, in addition to the standard behaviors, the date/time picker introduces specific focus management between the date picker container and the time picker container. For more information on date selection and time navigation, see the [date picker](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-picker/) and the [time picker](https://www.sap.com/design-system/fiori-design-web/ui-elements/time-picker/).

**Table (col-width-30-70)**

Key Combination

**Tab**
Pressing **Tab** moves the focus to the **Hours output field** in the time picker container.
If a different date is defined as the initial focus, pressing **Tab** still moves focus to the **Hours output field**.
Whenever focus is moved to a new date, pressing **Tab** transfers focus to the **Hours output field** in the time picker container.

**Shift \+ Tab**

### Screen reader support

For details on screen reader support and Accessible Rich Internet Applications (ARIA), see [UI5 Screen Reader Support](https://ui5.sap.com/#/topic/33fae3482358438e93daea5232527093) and [WAI-ARIA Authoring](https://www.w3.org/TR/wai-aria-1.2/).

## Content

### Placeholder

If no specific placeholder is defined, the date/time
picker displays a placeholder with a sample date of
December 31 of the current year and a sample time of
23:59:58, formatted according to the format pattern. If
the sample date is invalid, the closest valid year-end,
highest valid month-end, or highest valid date is used in
descending order.
### Formatting dates and times

You can use three different types of date and time formats: **short**, **medium**, and **long**. The formatting and order of the values differ based on the local settings that have been configured in the browser.

Formatting dates and times examples

**> **Guideline:** **

For guidelines and information on the SAPUI5 date and time formatters, see [formatting dates](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/formatting/formatting-dates) and [formatting times](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/formatting/formatting-time).

### Special dates with legend :badge, info, large, _, SAPUI5 Only:

For irregular or non-recurring events, the date/time picker supports special dates that can be highlighted in the calendar. Provide a legend whenever special dates are displayed to explain the meaning of the highlighted dates. Select from the predefined set of legend colors.

The legend can appear as a static element that stays visible next to the calendar, or as a dynamic option opened through a “Special Days” button. Choose the static or dynamic presentation based on available screen space and legend complexity.

Date/time picker with legend

### Localization

The date/time picker supports left-to-right (LTR) and right-to-left (RTL) reading directions.

Right-to-left text direction in the date/time picker

## Features

### Timezone

#### Global configuration

The date/time picker can rely on both local and global configuration for timezone handling. The implementation determines which timezone is applied for the given use case.

#### Local configuration :badge, info, large, _, SAPUI5 Only:

The date/time picker can display a timezone next to the
selected date and time. This helps users understand which
timezone their input refers to, which is especially
useful in applications where time accuracy across regions
matters.

The timezone is shown inside the input field. When users
click on it, a popover appears showing the full name of
the timezone.
**> **Guideline:** **

If the user needs to set a time that is time zone-sensitive, offer a select control next to the date/time picker
component to choose the appropriate time zone.

### Minutes and seconds step :badge, info, large, _, SAPUI5 Only:

The time picker allows configuration of step values for both minutes and seconds. By default, time values increase or decrease by 1 unit (for example 1 → 2 → 3). However, you can define a custom step increment, such as 5 or 15, to skip values accordingly. For example, if the minute step is set to 5, the sequence will follow 0 → 5 → 10 → 15, and so on.

Date/time picker with minute step set to 5

**> **Guideline:** **

Step values must be defined separately for minutes and seconds. Both are optional, and the default step value of 1
will apply if no custom value is provided.

### Current date and time :badge, info, large, _, SAPUI5 Only:

The date/time picker can include shortcut buttons for quickly setting the current date or current time. When clicked, these buttons automatically update the input to reflect either today’s date or the exact current time, depending on the context.

Each button appears within the calendar or time selection view, providing users an easy way to return to the present moment without needing to scroll or manually adjust the fields.

These shortcut buttons are optional and can be enabled depending on the specific requirements of the use case.

Date/time picker with current date and time buttons

**> **Guideline:** **

To minimize unnecessary scrolling for the user, consider also setting default values. For time selection, using
full-hour or half-hour increments (00 or 30 minutes) is often the most efficient default setting, offering
convenience alongside the shortcut buttons. In certain contexts, it may be appropriate to use the current date and
time as the default setting, aligning with the shortcut button functionality for a seamless user experience.

### Show/hide week numbers

The date/time picker can optionally display week numbers in a dedicated column to the left of the calendar grid. This feature is typically used in views where planning by week is relevant. Whether week numbers are shown depends on the app’s use case and should be configured accordingly.

Date/time picker with and without week numbers

### Mixed calendar

The mixed calendar view supports a combination of two different calendars into one calendar view. The week numbers are not available for this type of calendar.

Date/time picker with primary (Islamic) and secondary (Gregorian) calendar type

**> **Information:** **

The date/time picker can be configured to specify how calendar weeks are calculated. This supports different calendar
conventions, such as ISO 8601, Middle Eastern, or Western Traditional, among others. For more information and
visuals, see the [calendar](https://www.sap.com/design-system/fiori-design-web/ui-elements/calendar/).

## Framework Comparison

Some behaviors differ between frameworks due to implementation specifics. The table below summarizes the differences between SAPUI5 and SAP Web Components and lists the framework-specific patterns.

**Table (col-width-50-20-30)**
Feature                                                                                                                                                                                                                                                                                               | SAPUI5        | SAP Web Components

The input field can be hidden. For more information, see the [Open date/time picker by another component](https://www.sap.com/design-system/fiori-design-web/ui-elements/datetime-picker/#opening-the-datetime-picker-by-another-component-badge-info-large-_-sapui5-only) section.                   | Available     | Not available

The date/time picker supports special dates that can be highlighted in the calendar. For more information, see the [Special dates with legend](https://www.sap.com/design-system/fiori-design-web/ui-elements/datetime-picker/#special-dates-with-legend-badge-info-large-_-sapui5-only) section.     | Available     | Not available

The date/time picker can display a timezone next to the selected date and time. For more information, see the [Local configuration](https://www.sap.com/design-system/fiori-design-web/ui-elements/datetime-picker/#local-configuration-badge-info-large-_-sapui5-only) section.                      | Available     | Not available

The time/picker allows configuration of step values for both minutes and seconds. For more information, see the [Minutes and seconds step](https://www.sap.com/design-system/fiori-design-web/ui-elements/datetime-picker/#minutes-and-seconds-step-badge-info-large-_-sapui5-only) section.          | Available     | Not available

The date/time picker can include a shortcut button for setting the current date or current time. For more information, see the [Current date and time](https://www.sap.com/design-system/fiori-design-web/ui-elements/datetime-picker/#current-date-and-time-badge-info-large-_-sapui5-only) section. | Available     | Not available

**\**

---

## input-field

+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
Message Strip (information)
+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
This guideline now covers both SAPUI5 and SAP Web Components. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).

## Intro

The input component lets users enter or edit single-line text or numeric values. You can enable autocomplete suggestions and value help to make data entry faster and more accurate.

Input

### Component availability

The component is available in the following libraries:

+-----------x------------+---------------------------------------------x----------------------------------------------+----------------x-----------------+
Library                | Technical Name                                                                             | Identifier
+-----------x------------+--------------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit        | [sap.m.Input](https://ui5.sap.com/#/entity/sap.m.Input)                                    | :badge, info, large, _, SAPUI5:
+-----------x------------+---------------------------------------------x----------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components     | [ui5-input](https://ui5.github.io/webcomponents/components/Input/)                         | Components:
+-----------x------------+---------------------------------------------x----------------------------------------------+----------------x-----------------+
SAP Web UI Kit (Figma) | [Input](https://www.figma.com/design/SILcWzK5uFghKun9jx6D7c/SAP-Web-UI-Kit?node-id=2-1352) | :badge, info, large, _, Figma:

**Table (external_only)**
+----------------x-----------------+---------------------------------x----------------------------------+----------------x-----------------+
Library                          | Technical Name                                                     | Identifier
+----------------x-----------------+--------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit                  | [sap.m.Input](https://ui5.sap.com/#/entity/sap.m.Input)            | :badge, info, large, _, SAPUI5:
+----------------x-----------------+---------------------------------x----------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components               | [ui5-input](https://ui5.github.io/webcomponents/components/Input/) | Components:
+----------------x-----------------+---------------------------------x----------------------------------+----------------x-----------------+
SAP Fiori for Web UI Kit (Figma) | [Input](https://www.figma.com/community/file/1494295794601744471)  | :badge, info, large, _, Figma:

## When to Use

**When To Use**

Do
Use the input to:
- Enter a short, single-line text or number.
- Enter a password, URL, phone number, or email address.
- Select a single item from a large amount of data (for example, more than 200 items).
- Find an object by searching for more than one attribute, such as an ID, city, and customer name. Use this component in combination with the autocomplete and suggestion features, and the value help option. For small data sets (fewer than 20 items), consider using the [select](https://www.sap.com/design-system/fiori-design-web/ui-elements/select/) component. Otherwise, use the [combo box](https://www.sap.com/design-system/fiori-design-web/ui-elements/combo-box/) (for 20-200 items). For more information on which selection control to choose, see the [selection component](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/which-selection-control-to-use) overview.

Don't
Don’t use the input to:
- Enter dates and times. In this case, use the [date picker](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-picker/), [date range selection](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-range-selection/), or [date/time picker](https://www.sap.com/design-system/fiori-design-web/ui-elements/datetime-picker/).
- Enter long texts. In this case, use the [text area](https://www.sap.com/design-system/fiori-design-web/ui-elements/text-area/).
- Select multiple values. In this case, use the [multi-combo box](https://www.sap.com/design-system/fiori-design-web/ui-elements/multi-combobox/) (for fewer than 200 items) or the [multi-input field](https://www.sap.com/design-system/fiori-design-web/ui-elements/multiinput/) (for more than 200 items).

+-----------------------------------------------------------x-----------------------------------------------------------+
Top Tips
+-----------------------------------------------------------x-----------------------------------------------------------+
- Ensure that input fields are consistently spaced and aligned to maintain a clean and organized layout.
- Design input fields with appropriate lengths to accommodate typical entries without excessive scrolling or
truncation.
- Use clear, concise, and easily understandable labels for each input field to guide users. Don't replace labels with
placeholders because placeholder text disappears once the user starts typing in the field.
- Utilize placeholder text within input fields to provide hints or examples of the expected input format.
- Provide real-time feedback for input validation, highlighting errors as users type instead of waiting for form
submission.
- Implement suggestions and autocomplete features to help users enter information quickly and accurately.

## Anatomy

An input consists of the following elements:
1. **Field**: A container that holds the input area.
2. **Text**: A placeholder or typed text.
3. **Icon (optional):** An icon visualizing an available action (for example, a *Clear* icon to remove the typed text).
## Types

The input component supports six types: basic input, input with label, input with suggestions, input with value help, input with description, and input as a search (which is specific to SAP Web Components).

### Basic input

The basic input is a field that allows the user to type in any kind of text. It does not offer any suggestions or additional actions.

Basic input

**> **Hint:** **

You can limit the length of the input field. For example, if you don’t want users to enter more than 5 characters,
set the maximum length to 5. By default, the maximum permissible character length is not defined. If the back-end
system has a limit, ensure that you configure this property accordingly.

### Input with label

Use an input with a label to clearly describe the expected value. Use short, descriptive label text (for example, “First Name”, “Invoice Date”). The input is often combined with the label component.

Input with label

**> **Information:** **

An input field should always have a visible label. Visible labels improve usability, accessibility, and clarity,
ensuring that everyone, including users who rely on screen readers, can easily identify the purpose of each field.
Without a visible label, users may rely on placeholder text, which disappears once they start typing and can lead to
uncertainty about what the field expects. An exceptional use case can be found in the Input as a search section.

### Input with suggestions

Use an input with suggestions when users benefit from type-ahead help – when there’s a known set of likely values or searchable items that can be filtered as the user types, to speed input, reduce errors, and improve discoverability. Input fields can provide helpful suggestions that appear as the user types, using autocomplete and a dropdown list, such as when searching for products, customers, employees, tags, addresses, and so on.

Input with suggestions

For more information, see [Suggestions and autocomplete](https://www.sap.com/design-system/web-design-system-drafts/ui-elements/input-field/usage#suggestions-and-autocomplete).

### Input with value help

Inputs can also trigger a value-help dialog to assist users in selecting the correct value. This dialog is opened via a value-help icon button displayed on the right-hand side of the input field. Use inputs with value help when users need to pick from a large or complex dataset, such as material lists for inventory, vendor lists for procurement, and so on.

Input with value-help icon

For more information, see [Value help](https://www.sap.com/design-system/web-design-system-drafts/ui-elements/input-field/usage#value-help).

### Input with description

An input field can include an additional description after the field that serves as contextual information, such as a unit of measurement, currency, or another descriptive reference.

Input with description

### Input as a search :badge, info, large, _, SAP Web Components only:

Use the input component as a search field for free-text searches or to filter data. Global or contextual search lets users find items across lists, tables, catalogs, or site areas, for example, products or documents.

Note: The SAPUI5 Input component doesn't provide search capabilities on its own. Use the [search field](https://www.sap.com/design-system/fiori-design-web/ui-elements/search/) instead.

Input as a search field

**> **Guideline:** **

We highly recommend using only two icons as standalone labels for input fields: the magnifying glass icon for search
and the paper plane icon for sending messages.

## States

### Component states

The input component supports the following component states: enabled, disabled, and read-only.

**A. Enabled:** Indicates that the field can be used to
perform an action. The input component is both enabled
and editable by default, allowing the user to enter a
value.
**B. Disabled:** Visually indicates the field is inactive
and cannot be edited or interacted with. Set the
component to disabled in an edit scenario to indicate
that the user cannot change the component, for example,
due to missing access rights or previous conditions not
having been fulfilled or selected.
**C. Read-only:** Shows the field as non-editable and
fully readable, typically with a grey background.
For more information, see [Component States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-component-states).

### Interaction states

**A. Regular:** The regular state is the default state. The component
is shown in the regular visual state if the user isn’t interacting with
it.
**B. Hover:** Highlights the input field when the cursor moves over it.
**C. Active:** Indicates the field is focused and ready for data entry.
For more information, see [Interaction States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-interaction-states).

### Value states

**A. Negative:** Highlights an error or invalid input.
**B. Critical:** Highlights input that might need correction or review.
**C. Positive:** Confirms a valid input.
**D. Information:** Signals neutral status or context without implying errors or warnings.
For more information, see [Value States.](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-value-states)

### Value states with value state message

**A. Negative:** Highlights an error or invalid input that
needs to be corrected.
Input value states with value state message
**B. Critical:** Indicates a warning that may require user
attention but is not an error.
**C. Positive:** Confirms valid input or successful completion.
Note: The positive state does not display an input popover.
**D. Information:** Signals neutral status or context without
implying errors or warnings.
For more information on how values are validated in the input, see [Form Field Validation](https://www.sap.com/design-system/fiori-design-web/ui-elements/form-field-validation/).

### Focus state

The focus state becomes active when the input field
receives focus. If a keyboard is available, all
interactive elements must provide a focus state.
Note: The active and focus states are identical for the
input component.
For more information, see [Focus States.](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-focus-states)

## Behavior and Interaction

### Activating an input field

The standard way to activate an input component is for a
user to position the cursor inside the field and click.
Input interaction – click and caret position
**A:** The component starts in its regular, inactive state.
**B:** When the user moves the pointer over the field, the
component displays a hover state.
**C:** When the user presses the left mouse button inside
the field, the component activates the input and a caret
appears in front of the placeholder text.
**D:** Upon releasing the mouse button, the component keeps
the input active, and the caret and placeholder remain in
the same position, ready for text entry.
Note: The placeholder text is application-specific.
### Entering text using autocomplete

The autocomplete feature helps users quickly select items by
suggesting matches as they type. The interaction flow is as
follows:
**A:** The user activates the input field by clicking on it.
The component responds by displaying the caret in front of
any placeholder text.
**B:** As the user begins typing, the placeholder text
disappears. Once the user enters the minimum number of
characters required to trigger suggestions (for example, one
character), the autocomplete list appears, and the first
matching item is autocompleted. As a visual hint for the
user, matched characters are highlighted (bold) in the list
items.
**C:** To confirm the selection, the user presses **Enter.**
The suggestion list closes, and the autocompleted text
becomes regular typed text. The caret automatically moves to
the end of this confirmed value.
### Selecting an item using list options

This component allows users to select an item from a dynamic list of options, similar to autocomplete. However, users manually select an item from the displayed list rather than confirming an autocompleted value.
**A:** The user activates the input field by clicking into it. The component then displays the caret in front of the placeholder text.
**B:** As the user begins typing in the input field, the component removes the placeholder text. Once the user enters the minimum number of characters required, the component automatically displays the suggestion list. When the user moves the pointer over a
suggestion, the component shows its hover state.
Note: By default, this feature requires the entry of one character to trigger suggestions. For the SAPUI5 Input component, it is possible to define more than one required character to trigger suggestions. For more information, see [Defining characters for triggering suggestions](https://main--builder-prospect--sapudex.aem.page/design-system/web-design-system-drafts/ui-elements/input-field/#defining-characters-for-triggering-suggestions---badge-info-large-_-sapui5-only).
**C:** If the user presses and holds the left mouse button on a suggestion, the component activates the down state and moves focus to the selected item.
**D:** When the user releases the mouse button, the component sets the clicked item as the input value. The suggestion list closes, and the text becomes regular typed text. The caret moves to the end of the value.
### Defining characters for triggering suggestions   :badge, info, large, _, SAPUI5 only:

You can define how many characters users must type before
suggestions appear.
Input with suggestions – suggestion trigger
By default, suggestions and autocomplete appear after the
first character is entered.
For information on how to manage leading and trailing white space (blanks) when copying and pasting text into input components, see [Removing Leading and Trailing White Space](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/formatting/leading-trailing-blank-removal).

## Responsiveness

In the examples below, the input field is shown in combination with the tabular autocomplete feature for different device sizes. For sizes S and M, use Cozy mode of the component, whereas for size L, use Compact mode. For more information, see [Content Density (Cozy and Compact)](https://www.sap.com/design-system/fiori-design-web/foundations/visual/cozy-compact).

Note that when tabular suggestions are used, the column headers stay sticky when scrolling within the suggestion list.

### Size S (smartphones)

When the user taps the input field, the keyboard appears, and the view switches to full screen, with the input field at the top and
suggestions listed below. This utilizes the pop-in feature of the [responsive table](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/).
Tabular autocomplete suggestion feature on a smartphone
To select an item, a one-finger tap gesture is used. When an item is tapped, the full-screen view immediately closes, and the selected
value is applied to the input field.
### Size M (tablets)

The pop-in feature of the [responsive table](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/) is used here, and defined columns are wrapped into a new line due to the limited space available.

Tabular autocomplete suggestion feature on a tablet

### Size L (desktops)

The full table is shown by the suggestion feature.

Tabular autocomplete suggestion feature on a desktop

## Accessibility

SAP follows international standards, such as WCAG and WAI-ARIA, and strives to make our business solutions accessible and inclusive.

For more information, see [Accessibility in SAP Fiori](https://www.sap.com/design-system/fiori-design-web/discover/sap-design-system/product-standards/accessibility-in-sap-fiori) and the [Accessibility Design Tools Handbook](https://www.sap.com/documents/2023/11/bc210d8b-977e-0010-bca6-c68f7e60039b.html).

### Keyboard navigation

The following keyboard combinations are supported by the SAPUI5 Input component.

**Table (col-width-30-70)**

Key Combination

**Tab**
text, it is selected. If the focus is already there, it
is moved to the next UI element.

**Shift \+ Tab**

**F4, or Alt \+ Up Arrow**
**Alt \+ Down Arrow**
**Escape**
If the suggestion list is closed, any changes are
canceled and reverted to the value which the Input field
had when it got the focus.

**Right Arrow**
**Left Arrow**
of the selection and removes the selection.
Any character or number
Adds the character to the input field. If text is
selected, it gets overwritten by the new text.

**Ctrl \+ A**

**Delete**
**Backspace**
deleted.

**Ctrl \+ C or Ctrl \+ Insert**

**Ctrl \+ X or Shift \+ Delete**

**Ctrl \+ V or Shift \+ Insert**
position.

**Page Up**
**Page Down**
accordingly.

**Home**
**End**

**Up Arrow**
**Down Arrow**

**Enter/Return**

**Ctrl \+ Alt \+ F8**
Focuses the first link in a value state message or header
with links, whether in a popup or header when suggestions
are present. In case of suggestions popover, if the focus
is on a suggestion item, it moves to the first link in
the value state header.
**Tab**
If the focus is on the first link after using Ctrl \+ Alt
\+ F8 and there are more links in the value state
message, it moves to the next link in the value state
message or header.
If the focus is on the first link after using Ctrl \+ Alt
\+ F8 and there are no more links in the value state
message, it closes the popup message or suggestion
popover, and moves to the next element in the tab chain.
**Shift \+ Tab**
If the focus is on the first link in the value state
message, it returns to the input.
If the focus is on the second, third and so on link in
the value state message, it moves to the previous link.
**Down Arrow**
If the focus is on a link in the value state header and
there are input suggestions, it moves to a suggestion
item.

### Screen reader support

For additional details on screen reader support and Accessible Rich Internet Applications (ARIA), see [UI5 Screen Reader Support](https://ui5.sap.com/#/topic/33fae3482358438e93daea5232527093) and [WAI-ARIA Authoring](https://www.w3.org/TR/wai-aria-1.2/).

## Content

This section outlines the guidelines for crafting effective and consistent content within the input component, ensuring clarity, accessibility, and a seamless user experience.

### Input with Clear icon

A *Clear* icon can be added to the input field. It will
appear as soon as the input field has a value. Clicking the *Clear*
icon removes the value from the field. If used, make sure
that the input field is wide enough to show the *Clear* icon in addition to the value.
**A:** The component is enabled and displays its regular
state, including the typed text.
**B:** Positioning the pointer on the *Clear* icon changes
the state to hover to both icon and input field.
**C:** Clicking on the *Clear* icon changes the state to
active and removes the content from the input field.
**D:** Input field with removed content and in active state.
A *Clear* icon can also be displayed if the input is of the
type “input with value help”. In this case, the *Clear*
icon appears to the left of the value help icon in
left-to-right (LTR) languages.
### Data entry

The input component supports six types of entered data: text (default), numbers, email, URL, telephone number, and password. For more information, see the [sample input types](https://ui5.sap.com/#/sample/sap.m.sample.InputTypes/preview). Each type is optimized for its intended content and adjusts the keyboard layout on mobile devices to match the expected input format.

**Note**: The entered data is not automatically validated. Applications must handle validation and display error messages or feedback separately.

**A. Text (default):** Supports letters, used for general text entry.
**B. Number:** Supports numbers, used for general entry.
**C. Email**: Optimized for entering email addresses, displaying a
keyboard with the “@” symbol on mobile devices.
**D. URL**: Designed for web addresses, showing a keyboard with quick
access to “/” and “.com” keys on mobile devices.
**E. Telephone number:** Supports numbers and some special symbols
(#\*\+). An appropriate keyboard layout is shown on touch devices.
**F. Password**: Masks the entered characters for secure password input.
### Required input

To indicate that a particular field is mandatory and
requires user input, set the “Required” indicator for its
label, which displays an asterisk (\*) next to the label.
If no value is provided, the input receives a negative
state to also indicate that a value is required.
### Placeholder

The placeholder provides a short hint to help users enter valid data.
Avoid using placeholders instead of labels, because placeholder text disappears when users enter data and no longer indicates the field’s purpose.
For more information on how to write placeholder text, see [UI Text Guidelines for SAP Fiori Apps](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/ui-text-guidelines-for-sap-fiori#input-field).
### Text alignment

The input field supports six text alignment options ([API](https://ui5.sap.com/#/api/sap.ui.core.TextAlign)): initial, begin, center, end, left, and right.
- **Initial** (default): Uses the browser’s default alignment.
- **Begin:** Aligns text to the beginning of the field based on the reading direction (left in left-to-right languages, right in right-to-left languages).
- **Center:** Use sparingly, only when center alignment improves visual balance (for example, short codes or isolated labels).
- **End:** Aligns text to the end of the field based on the reading direction (right in left-to-right languages, left in right-to-left languages).
- **Left:** Use for text-based input types such as phone numbers, URLs, passwords, and email addresses, where left alignment remains standard regardless of
language direction.
- **Right:** Use for numeric input such as amounts or decimal values, where users need to compare or add numbers easily.
### Localization

The input component supports both left-to-right (LTR) and right-to-left (RTL) reading directions.

Input in left-to-right mode

## Features

### Suggestions and autocomplete

The suggestions list and autocomplete features help users quickly scan and select relevant terms or values. Suggestions appear below the input field as soon as the user starts typing. The position of the suggestion box depends on the space available below the component. If there is not enough space, the suggestion box is shown above the component. By default, the suggestion box matches the width of the input field.

Autocomplete completes the first suggestion that starts with the entered characters. Depending on the list ordering, this may not be the top item shown.

The input component supports three suggestion types: single, two-value, and tabular (which is specific to SAPUI5).

**> **Warning:** **

The typeahead input feature is not available on Android devices.

#### Single-value suggestion

The single-value suggestion displays a list of
suggestions where each option contains only one value
(such as a name or an ID), aligned to the left.
Use this feature when a single attribute is sufficient
for users to find and select an item.
#### Two-value suggestion

The two-value suggestion displays a list of suggestions
where each option shows two attributes (such as a name
and an ID) instead of just one. The primary value is
left-aligned, while the secondary value is right-aligned.
Use this feature when users need both attributes to
identify and select the correct item.
#### Tabular suggestions:badge, info, large, _, SAPUI5 only:

Suggestions can be displayed in a table layout, with each row representing a suggestion and the columns visualizing different attributes. Use the tabular autocomplete feature if you need to display more than two attributes. We recommend using a maximum of 4 columns. Focus on columns that are really relevant for the use case.

If there are too many columns for the available space, the width of the columns shrinks. Alternatively, you can enable the responsive behavior of the table to achieve appropriate responsive behavior for sizes S and M. For more information, see the article on the [responsive table](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/).

Tabular autocomplete, suggestion box wider than the input field

А *Show All Items* button can be shown at the end of the suggestion result list. Because the number of results is limited, this option helps the user find the relevant item via an alternative dialog, such as:

- [Select dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/select-dialog/) (simple)
- [Value help dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/value-help-dialog/) (complex)

The width of the columns is distributed equally by default. To avoid truncation, accurately estimate the primary attribute length and set a minimum width for this column.

The column headers remain in place when the user scrolls through the suggestion list.

#### Grouping

You can group the items in a suggestion list by a specific attribute and separate each group visually with a group header. This feature is also available for tabular suggestion lists.

The group headers are not interactive.

Input with grouped tabular suggestions

#### Key and value text format :badge, info, large, _, SAPUI5 only:

For some use cases, the permitted input values are
key-value pairs. Suggestions and autocomplete functions
operate for both the key and the value. The display
format in the input field can be configured as follows:
- Key
- KeyValue
- Value (default)
- ValueKey
Key-value pairs can use various suggestion
visualizations, including single-value suggestions,
two-value suggestions, and tabular suggestions.
### Width

The width of the input field is set to 100% by default. Input fields are usually used in [forms](https://www.sap.com/design-system/fiori-design-web/ui-elements/form/),
where the width is determined by the form element or container that the input field is embedded in. Instead of
defining a fixed width, we recommend working with proper layout containers, like the form, simple form, and
responsive grid layout, and with the layout data property, where the width is defined by the 12-column
approach.
### Value help

Enable value help to let users choose the correct value from a dataset. To give a better indication of the type of
data that can be selected, you can exchange the value help icon. Once the value help option is enabled, the click
event can be registered and one of the following displayed:
- [Value help dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/value-help-dialog/) (complex)
- [Select dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/select-dialog/) (simple)
- [Custom dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog/)
Use this option in combination with the autocomplete suggestion feature. The value help dialog should tell users
what values have already been entered into an input field.
## Framework Comparison

Some behaviors differ between frameworks due to implementation specifics. The table below summarizes the differences between SAPUI5 and SAP Web Components and lists the framework-specific patterns.

**Table (col-width-50-20-30)**
Feature                                                                                                                                                                                                                                                                                                                                                                                     | SAPUI5        | SAP Web Components

The input component can act as a search field for conducting free-text searches, or it can be used to filter information within datasets. For more information, see the [Input as a search](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/#input-as-a-search-badge-info-large-_-sap-web-components-only) section.                                              | Not available | Available

The suggestion trigger can be defined how many characters need to be typed to trigger the auto completion and suggestion list to open. For more information, see the [Defining characters for triggering suggestions](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/#defining-characters-for-triggering-suggestions---badge-info-large-_-sapui5-only) section. | Available     | Not available

For some use cases, the permitted input values are key-value pairs. Suggestions and autocomplete functions operate for both the key and the value. For more information, see the [Key and value text format](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/#key-and-value-text-format-badge-info-large-_-sapui5-only) section.                                 | Available     | Not available

The tabular suggestions feature displays the values in a table layout. For more information, see the [Tabular suggestions](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/#tabular-suggestionsbadge-info-large-_-sapui5-only) section.                                                                                                                          | Available     | Not available

**\**

---

## input-web-component

+------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------+
+--------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------+---------x----------+
## This page has been deprecated and is no longer available.
This page was deprecated with guideline version **1.142**.
#### Reason for deprecation
The guidelines for the SAP Web Component and the SAPUI5 component have been merged. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).
#### Looking for the latest information?
Visit the page below for the unified guideline with the most recent updates.
[Input Field](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/)

---

## range-slider

+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
Message Strip (information)
+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
This guideline now covers both SAPUI5 and SAP Web Components. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).

## Intro

A range slider is a UI component that lets users select a value range within a predefined numeric or non-numeric interval.

*Range slider*

### Component availability

The component is available in the following libraries:

+-----------x------------+-------------------------------------------------x--------------------------------------------------+----------------x-----------------+
Library                | Technical Name                                                                                     | Identifier
+-----------x------------+----------------------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit        | [sap.m.RangeSlider](https://ui5.sap.com/#/entity/sap.m.RangeSlider/)                               | :badge, info, large, _, SAPUI5:
+-----------x------------+-------------------------------------------------x--------------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components     | [ui5-range-slider](https://ui5.github.io/webcomponents/components/RangeSlider/)                    | Components:
+-----------x------------+-------------------------------------------------x--------------------------------------------------+----------------x-----------------+
SAP Web UI Kit (Figma) | [Range Slider](https://www.figma.com/design/SILcWzK5uFghKun9jx6D7c/SAP-Web-UI-Kit?node-id=19-2025) | :badge, info, large, _, Figma:

**Table (external_only)**
+----------------x-----------------+----------------------------------------x----------------------------------------+----------------x-----------------+
Library                          | Technical Name                                                                  | Identifier
+----------------x-----------------+---------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit                  | [sap.m.RangeSlider](https://ui5.sap.com/#/entity/sap.m.RangeSlider)             | :badge, info, large, _, SAPUI5:
+----------------x-----------------+----------------------------------------x----------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components               | [ui5-range-slider](https://ui5.github.io/webcomponents/components/RangeSlider/) | Components:
+----------------x-----------------+----------------------------------------x----------------------------------------+----------------x-----------------+
SAP Fiori for Web UI Kit (Figma) | [Range Slider](https://www.figma.com/community/file/1494295794601744471)        | :badge, info, large, _, Figma:

## When to Use

+--------------------------------------------------------------------------x--------------------------------------------------------------------------+
When To Use
+--------------------------------------------------------------------------x--------------------------------------------------------------------------+
Do
Use the range slider to:
- Let users select a minimum and maximum value within a predefined numeric or non-numeric interval.
- Display and adjust settings such as volume, brightness, saturation, or contrast.
+--------------------------------------------------------------------------x--------------------------------------------------------------------------+
Don't
Don’t use the range slider to:
- Select a single value within a predefined range. Use the [slider](https://www.sap.com/design-system/fiori-design-web/ui-elements/slider) instead.

+---------------------------------------x---------------------------------------+
Top Tips
+---------------------------------------x---------------------------------------+
- Choose an appropriate size for the range slider that matches the use case.
- Use stepped increments to allow users to select from predefined intervals.
- Ensure values are clearly labeled to provide context and enhance usability.
- Display the current value as the user interacts with the slider.

## Anatomy

1. **Start point:** Minimum value of the slider range.
2. **Track (active or inactive):** Shows the full slider range. The active track represents the selected portion of the range, while the inactive track shows the unselected areas outside of it.
3. **Value indicators (optional):** Display the current values and can switch to input fields for direct editing.
4. **Tick marks (optional):** Represent the value intervals (steps). Each tick mark corresponds to a selectable value.
5. **End point:** Maximum value of the slider range.
6. **Labels (optional):** Display the values of selected tick marks along the slider.
7. **Slider handle (left and right):** Represent the current minimum and maximum values. Each handle moves independently, and their positions may swap as the selected range changes.

Anatomy of a range slider

## Types

The following range slider variants are available:

### Basic range slider

A simple range slider with handles and no extra elements, such as value indicators or tick marks and labels. Lets users select a range of values between a defined minimum and maximum. The two handles can be dragged independently to adjust the start and end values of the range.

Use when a clean, minimal interface is needed, or when additional visual guidance is unnecessary.

Basic range slider

### Range slider with value indicators

The value indicators appear above the handles to show or edit the current value. Users can edit the values directly when editable indicators are enabled.

**A. Value indicators:** Display the current values above the handles.

**B. Editable value indicators:** Display the current values above the handles as input fields that users can edit directly.

Range slider with value Indicators in display and edit mode

### Range slider with tick marks and labels

Tick marks appear along the track to represent predefined value steps and help users align their selections to consistent intervals. Labels can be added to certain tick marks to display their corresponding values.

Use this variant when the range includes predefined or incremental steps.

Range slider with tick marks and labels

### Custom scale and custom value indicators :badge, info, large, _, SAPUI5 only:

The range slider supports custom scales with descriptive labels instead of numeric values. Keep labels concise and reduce the number of tick marks if longer labels would create clutter.

Range slider with custom scale and custom value indicators

**> **Hint:** **

To use custom scales in a range slider, you must map them to the floats for the range slider scale.

## States

### Component states

The range slider supports two component states: enabled and disabled.
**A. Enabled:** The range slider is interactive and the user can adjust the value.
**B. Disabled:** The range slider is non-interactive and cannot be adjusted.
For more information, see [Component States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-component-states).
### Interaction states

The range slider has the following interaction states: regular, hover (on the handles and on the active track), and down.
**A. Regular:** The default state of the component.
**B. Hover on the handle:** When the cursor is over a handle, the handle highlights to indicate it can be adjusted.
**C. Hover on the active track:** When the cursor is on the active track, both handles highlight to indicate that the entire range is interactive.
**D. Down:** The state shown while a handle is pressed or being dragged.
For more information, see [Interaction States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-interaction-states).
### Focus state

The range slider supports separate focus states for the handles and the active track.
**A. On the handle:** When a handle is focused, it displays a visible border with a transparent fill, so the current value remains visible beneath it.
**B. On the active track:** When the active track is focused, a border appears around both handles and the active track, indicating that the entire range can be adjusted.
For more information, see [Focus State](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-focus-states).
## Behavior and Interaction

### Dragging a handle to adjust values

Users can drag a handle to adjust the selected values. As the handle is moved, value indicators provide real-time feedback by displaying the current value. The behavior progresses as follows:

**A. Default state:** The range slider is in its default state. Handles are placed either at the default range values (such as 0 and 100) or at positions defined by your application.

**B. Clicking the handle:** When a user clicks on one of the handles, it becomes transparent, ensuring the current value underneath remains visible and easy to track.

**C. Dragging the handle:** The user can drag the handle along the track to adjust the value. If value indicators are enabled, they remain visible throughout the interaction and update continuously as the user moves the handle.

Once the user releases the handle, the final value is applied to the component according to the application logic.

Dragging a handle to adjust the selected values

### Clicking on the track to adjust values

Users can also adjust a value by interacting directly with the track itself. Clicking the inactive track moves the nearest handle to the clicked position.

**A. Start of interaction:** The range slider is in its default state with either predefined values or values that were previously modified.

**B. End of interaction:** The moment the user clicks on an inactive part of the slider track, the component identifies which handle is nearest to the clicked point and moves that handle directly to the clicked position.

The clicked point becomes the new value for that handle, updating the selected range according to the application logic.

Clicking or tapping the track moves the closer handle to that point

### Snapping

The snapping mechanism in a range slider is based on preconfigured step intervals. When a user drags a handle or clicks on the track, the handle automatically snaps to the nearest valid value based on these intervals. This feature helps users make accurate adjustments with ease and confidence, minimizing the likelihood of errors.

**A. Start of interaction:** The user drags the handle to a new position.

**B. End of interaction:** When released, the handle automatically snaps to the nearest tick mark, and the value indicator updates accordingly.

Snapping to tick marks by handle dragging

### Range movement

Users can move the entire selected range at once. When a range slider has a selected range, a user can move the entire selection at once rather than adjusting each handle individually.

**A. Start of interaction:** Hovering over the active track highlights both handles, indicating that the full range can be moved.

**B. End of interaction:** From that point, the user can click and drag this highlighted section, moving the entire range (both handles simultaneously) to a new position, all while preserving the width of the selected range.

Moving the entire range

### Editable value indicators

If the value indicators are configured to be editable, they transform into input fields when activated, so users can directly type the desired values instead of dragging the handles.

**A. Start of interaction:** The user clicks on the input field and type the new value.

**B. End of interaction:** The user confirms the newly entered input value by pressing **Enter**. The handle automatically moves to the new position and shows the corresponding value.

Editing the value using the value indicators

## Responsiveness

By default, the range slider takes the width of its parent container. It supports both [cozy and compact](https://www.sap.com/design-system/fiori-design-web/foundations/visual/cozy-compact)  form factors.

### Tick marks and labels

When space is limited, tick marks and labels start hiding to prevent overlap. The first and last labels always remain visible.

**A. Original size:** All tick marks and labels are visible.

**B. Reduced size:** Some tick marks and labels are visible.

**C. Further reduced size:** A few tick marks and labels are visible.

Responsiveness of tick marks and labels

## Accessibility

SAP follows international standards, such as WCAG and WAI-ARIA, and strives to make our business solutions accessible and inclusive.

For more information, see [Accessibility in SAP Fiori](https://www.sap.com/design-system/fiori-design-web/discover/sap-design-system/product-standards/accessibility-in-sap-fiori) and the [Accessibility Design Tools Handbook](https://www.sap.com/documents/2023/11/bc210d8b-977e-0010-bca6-c68f7e60039b.html).

### Keyboard navigation

The following keyboard combinations are supported by the SAPUI5 Range Slider component.

**Table (col-width-30-70)**

Key Combination

**Tab**
handle, right handle.

**Shift \+ Tab**

**Up Arrow or Right Arrow or \+**
one unit.

**Down Arrow or Left Arrow or -**
one unit.

**Ctrl \+ Up Arrow or Ctrl \+ Right Arrow or Page Up**
one larger step (for example, up to the next tick mark).

**Ctrl \+ Down Arrow or Ctrl \+ Down Arrow or Page Down**
one larger step (for example, up to the next tick mark).

**Home**
current minimum or maximum position.
**End**
**Esc**
the value it had when it got the focus.

**F2**
the input field, the focus goes to the input field and
you can type directly. Pressing **Enter** triggers the
update and F2 moves the focus back to the handle.

### Screen reader support

For details on screen reader support and Accessible Rich Internet Applications (ARIA), see the [UI5 Screen Reader Support](https://ui5.sap.com/#/topic/33fae3482358438e93daea5232527093) and [WAI-ARIA Authoring](https://www.w3.org/TR/wai-aria-1.2/).

## Content

### Wrapping and truncation

If the content exceeds the available width, it is truncated automatically. Define an appropriate label width to maintain clarity and avoid unnecessary truncation.

Range slider with truncating labels

### Localization

The range slider supports both left-to-right and right-to-left layouts. In right-to-left mode, the track direction and handle movement mirror the reading flow.

Range slider in left-to-right mode

## Framework Comparison

Some behaviors differ between frameworks due to implementation specifics. The table below summarizes the differences between SAPUI5 and SAP Web Components and lists the framework-specific patterns.

**Table (col-width-50-20-30)**

Feature                                                                                                                                                                                  | SAPUI5    | SAP Web Components

The range slider supports custom scales and value indicators, enabling the use of descriptive labels in place of numeric values. For more                                                | Available | Not available
information, see [Custom scale and custom value indicators](https://www.sap.com/design-system/fiori-design-web/ui-elements/range-slider/usage#custom-scale-and-custom-value-indicators). |
**\**

---

## range-slider-web-component

+------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------+
+--------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------+---------x----------+
## This page has been deprecated and is no longer available.
This page was deprecated with guideline version **1.142**.
#### Reason for deprecation
The guidelines for the SAP Web Component and the SAPUI5 component have been merged. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).
#### Looking for the latest information?
Visit the page below for the unified guideline with the most recent updates.
[Range Slider](https://www.sap.com/design-system/fiori-design-web/v1-139/ui-elements/range-slider/)

---

## select

The select component, sometimes called a dropdown, lets users pick an item from a small, predefined list.

The select control can be placed in toolbars, such as [chart toolbars](https://www.sap.com/design-system/fiori-design-web/ui-elements/chart-toolbar/), [footer toolbars](https://www.sap.com/design-system/fiori-design-web/ui-elements/footer-toolbar/), or [header toolbars](https://www.sap.com/design-system/fiori-design-web/ui-elements/toolbar-overview/), as well as in [forms](https://www.sap.com/design-system/fiori-design-web/ui-elements/form/) or [tables](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/).

Select component

## When to Use

**When To Use**

Do
Use the select component if:
- Users need to choose only one item from a short list, typically [between 2 and 12 items](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/which-selection-control-to-use#best-practices).
- Users don't need to see all options at once, and it's fine for the list to stay hidden until they open it.
- It's helpful for users to start with a default selection, especially if one option is used most often.
- Users would benefit from a logically grouped list, with the most common items shown first and the others sorted alphabetically, numerically, or by topic.
- Users need to select from a predefined list of options instead of entering free-form text.

Don't
Don’t use the select component if:
- Users need to choose between only two options. Use a [switch](https://www.sap.com/design-system/fiori-design-web/ui-elements/switch/) instead.
- Users need to pick one item from a very large set. Use a [combo box](https://www.sap.com/design-system/fiori-design-web/ui-elements/combo-box/) instead.
- You need to display more than one attribute or allow searching on multiple attributes. In this case, use an [input field](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/) with a [select dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/select-dialog/) or [value help dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/value-help-dialog/).
- You need to display all available options right away, without any user interaction. Use [radio buttons or a radio button group](https://www.sap.com/design-system/fiori-design-web/ui-elements/radio-button/) instead.

For more information on which selection control to choose, see the [selection control overview](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/which-selection-control-to-use).

+-----------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------+
Top Tips
+-----------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------+
- Don’t overload the select component. Keep texts concise and avoid complex content.
- Whenever possible, define a default selection.
- [Sort](https://www.sap.com/design-system/fiori-design-web/ui-elements/select/#sorting) the values in the selection list in a meaningful order.
- If you need a “[not selected](https://www.sap.com/design-system/fiori-design-web/ui-elements/select/#no-selection)” option, use an appropriate text and not a blank value.
- Avoid using [icons](https://www.sap.com/design-system/fiori-design-web/ui-elements/select/#tselect-with-icons) in the selection list. If you do, make sure they match the text.
- Avoid using a fixed [width](https://www.sap.com/design-system/fiori-design-web/ui-elements/select/#width) and don’t allow the width to auto-adjust based on the selection.
- If using a [two-column layout](https://www.sap.com/design-system/fiori-design-web/ui-elements/select/#two-column-layout), place the most relevant value in the first column.
- Avoid disabling selection options.

## Anatomy

1. **Value/Text:** The selected value.
2. **Input field:** Displays the selected option.
3. **Dropdown button:** Expands and collapses the dropdown list.
4. **Selection list:** Contains the values users can choose from.
## Types

### Layout Options

#### Simple Layout

In the simple layout, the dropdown list shows only the
value for each item.
Selection list with simple layout

#### Two-Column Layout

Use the two-column layout if you need to display additional information for each option, such as currencies or abbreviations. You can adjust the width ratio of the columns.

**Enabled**
Only the content of the first column appears in the input
field. Users see the second value when they open the
dropdown.
**Read-Only**
Both values are displayed in the input field, separated
by an en dash.
If the standard en dash separator isn’t suitable for your
use case, you can use a vertical line or bullet separator
instead.

**Disabled**
Only the content of the first column is shown.

**> **Guideline:** **

When using a two-column layout, place the more common or more relevant value in the first column.

### Select with Icons

The selection list can include text-only values or text with an icon. For more information about adding icons to list items, see [Standard List Item](https://www.sap.com/design-system/fiori-design-web/ui-elements/standard-list-item/).

Select with an icon

**> **Guideline:** **

While it's technically possible to include icons, we advise against it unless they enhance recognition or
understanding.
If your use case requires icons:
- Ensure that the icons match their intended meaning and follow established metaphors.
- Set icons via the `icon` property.
- Keep the accompanying text concise.

## States

### Component and Interaction States

[Component states](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-component-states) and [interaction states](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-interaction-states) define how the select control appears and behaves in response to user actions or its current condition.
**A. Hover:** Highlights the control when the cursor is placed over it.
**B. Active:** Indicates the control is focused or interacted with (clicked).
**C. Read only:** Shows that the control is visible but cannot be modified.
**D. Disabled:** Grays out the control, making it unavailable for any user interaction.
### Value States

You can use [semantic colors](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/how-to-use-semantic-colors#semantic-colors-1) to visualize [value states](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-value-states) for the selected item. This helps users quickly spot error, warning, confirmation, or information messages.

Select components using semantic colors for information, success, critical, and error value states

**A. Information:** Offers neutral or helpful context, without implying success or error.

**B. Positive:** Confirms a valid or successful selection.

**C. Critical:** Highlights a warning or a value that may need review.

**D. Negative:** Marks an error or invalid value that users need to correct.

Note that the positive or success value state doesn't show a message when focused.

For more information, see [Using Semantic and Industry-Specific Colors](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/how-to-use-semantic-colors).

## Behavior and Interaction

### Initial Display

The input field displays the current selection. If no previous selection has been made and no default option is specified, the first option is automatically selected.

**> **Guideline:** **

Whenever possible, define a default selection.

### Selection

When the user clicks the input field, the dropdown opens. Once an option is chosen, the list closes, and the selected option appears in the field. If there’s only an icon instead of a select input field, clicking the icon opens the dropdown. The currently selected item is always highlighted in the list to help the user see what's selected.

Select component – choosing a different item from the dropdown list

## Guidelines

### Selection List

#### Disabling Selection Options

Avoid [disabling](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-component-states#disabled) options, since users may not know how to re-enable them. Instead, [hide](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-component-states#hidden) options that aren’t available.

#### No Selection

Offer a “not selected” option when there’s no initial selection or when users can clear a selection. Show this option in parentheses and place it at the start of the list.
Recommended texts:
- **(Not Selected)**
- **(No Values Selected)**
For more examples, see the [UI text guidelines](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/ui-text-guidelines-for-sap-fiori#selection-list-options).
Don’t use a blank value to show that nothing is selected. If your use case needs a blank input field, use a [combo box](https://www.sap.com/design-system/fiori-design-web/ui-elements/combo-box/).
#### No Selection – Sort/Filter/Group

When you use an icon to open options for sorting,
grouping, or filtering a set of items, use the texts
below for the “not selected” option. Place this option in
parentheses at the start of the list.
- **(Not Sorted)**
Note: In most cases, this option isn’t necessary. Show
the default sort settings instead.
- **(Not Filtered)**
- **(Not Grouped)**
### Sorting

The sorted selection list contains all items available to the user. Choose one of the following styles to order the content:

- **Logical**: Sort items in a meaningful order. Group related options together and show the most common options first, followed by less common options. If you have more than eight select options, sort them alphabetically.
- **Alphabetical**: Sort currencies, names, and similar content alphabetically.
- **Numeric:** Sort numeric values in ascending order, starting with the lowest number.
- **Chronological**: Sort time related information with the most recent item first.

Example of logical sorting

Example of numeric sorting

### Label

You can display the select component with or without a label. If the field is attached to another field, you don’t need to define a second label.

### Unit of Measurement

You can use the [form](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/form/) layout options to add the unit of measurement (UoM) after the select component. Use the [label-field ratio](https://www.sap.com/design-system/fiori-design-web/ui-elements/form/#label-field-ratio) to display the UoM after the field. Make sure the UoM is clearly visible and doesn’t wrap to the next row.

> **Hint:** 
For accessibility, you can use "ariaDescribedBy" from the input component.

## Responsiveness

### Appearance

The display of the select component depends on the device:
- Opening the select on a smartphone brings up the option
list in full screen mode. The full screen mode can be
closed using the icon on the top right corner.
- On desktop and tablet devices, the select appears as a
popover. If there isn’t enough space to show the selection
list below the field, it opens above the field.
### Title for Size S
You need to set a title for the full screen mode. We
recommend the following format:
#### Single Selection
**Select [Entity]**
*Example: Select Product*
#### Multi Selection
**Select [Entities]**
*Example: Select Products*
### Width

The select control is usually used in [forms](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/form/), where the width is determined by the form element or container in which the select control is embedded.

If you need to limit the width to a specific value, you can set the width accordingly.

> **Guideline:** We do not recommend defining a fixed width. Where possible, use layout containers (such as a form, simple form, or
responsive grid layout), and define the width via the layout data property.
Don't allow the control to auto-adjust based on the selection.
If the text length is fixed and doesn’t require localization (for example, currency codes), consider reducing the
width.

#### Width of the Selection List

The width of the selection list automatically adjusts to
fit the longest item, with a maximum width of 600px.
Maximum width of the selection list

#### Text Wrap in the Selection List

The selection list doesn’t support horizontal scrolling.
By default, entries that exceed the maximum width of
600px for the dropdown are truncated.
If you expect the dropdown to contain longer entries, we
recommend wrapping items in the selection list to enable
users to read the full text (property: `wrapItemsText`).
If wrapping is enabled, the text can wrap to multiple
lines.
## Localization

Select is also available for right-to-left (RTL) usage. All its functionality and features are fully available in the RTL version.

Select in a left-to-right mode

---

## select-web-component

##

## Intro

The select component lets users choose an item from a
small, predefined list.
Select component

## When to Use

+----------------------------------------------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------------------------------------------+
When To Use
+----------------------------------------------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------------------------------------------+
Do
Use the select component if:
- Users need to choose one item exclusively from a short list.
- Users don't need to see all options at once, and it's fine for the list to stay hidden until they open it.
+----------------------------------------------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------------------------------------------+
Don't
Don’t use the select component if:
- Users need to choose between only two options. Use a [switch](https://www.sap.com/design-system/fiori-design-web/ui-elements/switch-web-component/) instead.
- Users need to pick one item from a very large set. Use a [combobox](https://www.sap.com/design-system/fiori-design-web/ui-elements/combo-box-web-component/) instead.
- You need to display more than one attribute or allow searching on multiple attributes. In this case, use an [input](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-web-component/) component with a select dialog or value help.
- You need to display all available options right away, without any user interaction. Use [radio buttons](https://www.sap.com/design-system/fiori-design-web/ui-elements/radio-button-web-component/) instead.

## Anatomy

### Select

1. **Input field:** Displays the selected value.
2. **Dropdown button:** Expands and collapses the dropdown list.
3. **Selection list:** Contains the values users can choose from.

### Dropdown List Item

1. **Value/Text:** Shows the value of the item or the name of the group.
Anatomy of the dropdown list item

**> **Guideline:** **

Although it's technically possible to include icons, we don't recommend it. If your use case requires icons, make
sure you choose icons that match their intended meaning and follow established metaphors.

## Types

The select component doesn't offer multiple types. Only the items in the dropdown list can have different types. You can also combine different dropdown list item variants.

### Simple Layout

In the simple layout, the dropdown list shows only the
value for each item.
Selection list with simple layout

**> **Guideline:** **

If the texts for the select options are very long and contain more than one piece of information, consider using a [two-column layout](https://www.sap.com/design-system/fiori-design-web/v1-139/ui-elements/select-web-component/#two-column-layout).

### Group Header

You can include group headers in dropdown lists to help
users scan and understand the options more easily. Group
headers are non-interactive; users can't select them as
values.
Keep in mind that the select component is designed for
small lists of items.
### Two-Column Layout

A two-column layout lets you show two values for every selectable
item. Each dropdown list item has two columns, and you can adjust
their width ratio.
The text in the input field depends on the state of the select
component:
**A. Enabled state**: Only the content of the first column appears in
the input field. Users see the second value when they open the
dropdown.
**B. Read-only state**: Both values are displayed in the input field,
separated by an en dash. If text is truncated, desktop users can
access the full text using a tooltip.
**C. Disabled state**: Only the content of the first column is shown.
**> **Guideline:** **

- Keep texts concise and avoid complex content, so you don't overload the component.
- Place the more common or more relevant value in the first column.

#### Alternative Separator

If the default en dash separator used in the input field
in read-only mode is ambiguous or unclear, you can use a
vertical line or bullet separator instead.
**A. Bullet separator**
**B. Vertical line separator**
For example, if column values include characters that
could be mistaken for separators, choosing a different
separator can help distinguish between columns.
## Behavior and Interaction

If the select component is editable, users can select an item by clicking the dropdown button and choosing an item from the list.

The component can start with no item selected or with a default value already set, which means one item in the dropdown list appears selected.

Interaction flow when no item is initially selected

## Responsive Behavior

The input field uses truncation and doesn't wrap text. Users can see the full text by opening the dropdown list or, in read-only mode, by using the tooltip on desktop devices. Items in the dropdown list use either wrapping or truncation.

Truncation and wrapping in edit mode
**> **Guideline:** **

Use simple and short text. This helps keep the select component clear and easy to use, and prevents a cluttered or
overwhelming experience for users.

### Width of the Dropdown List

The dropdown uses the same minimum width as the field. It
expands to fit the text until it reaches the maximum
width you have set. After that, text either truncates or
wraps, depending on your settings.

---

## slider

+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
Message Strip (information)
+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
This guideline now covers both SAPUI5 and SAP Web Components. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).

## Intro

The slider lets users select a value within a predefined numeric or non-numeric interval by dragging a handle along a track.

Slider component

### Component availability

The component is available in the following libraries:

+-----------x------------+----------------------------------------------x-----------------------------------------------+----------------x-----------------+
Library                | Technical Name                                                                               | Identifier
+-----------x------------+----------------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit        | [sap.m.Slider](https://ui5.sap.com/#/entity/sap.m.Slider)                                    | :badge, info, large, _, SAPUI5:
+-----------x------------+----------------------------------------------x-----------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components     | [ui5-slider](https://ui5.github.io/webcomponents/components/Slider/)                         | Components:
+-----------x------------+----------------------------------------------x-----------------------------------------------+----------------x-----------------+
SAP Web UI Kit (Figma) | [Slider](https://www.figma.com/design/SILcWzK5uFghKun9jx6D7c/SAP-Web-UI-Kit?node-id=19-2025) | :badge, info, large, _, Figma:

**Table (external_only)**
+----------------x-----------------+----------------------------------x-----------------------------------+----------------x-----------------+
Library                          | Technical Name                                                       | Identifier
+----------------x-----------------+----------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit                  | [sap.m.Slider](https://ui5.sap.com/#/entity/sap.m.Slider)            | :badge, info, large, _, SAPUI5:
+----------------x-----------------+----------------------------------x-----------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components               | [ui5-slider](https://ui5.github.io/webcomponents/components/Slider/) | Components:
+----------------x-----------------+----------------------------------x-----------------------------------+----------------x-----------------+
SAP Fiori for Web UI Kit (Figma) | [Slider](https://www.figma.com/community/file/1494295794601744471)   | :badge, info, large, _, Figma:

## When to Use

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
When To Use
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
Do
Use the slider to:
- Adjust a value along a continuous or gradual range.
- Handle values that change smoothly, such as volume or brightness.
- Allow people to make quick adjustments without typing.
- Provide immediate visual feedback as the handle moves.
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
Don't
Don’t use the slider to:
- Make specific choices, such as selecting a category or an item from a list. Consider using [radio buttons](https://www.sap.com/design-system/fiori-design-web/ui-elements/radio-button/) or [checklists](https://www.sap.com/design-system/fiori-design-web/ui-elements/checkbox/) instead.
- Make selections without full accessibility support. Ensure keyboard interaction, visible value indicators, and clear min and max labels. Alternatively, use [dropdowns](https://www.sap.com/design-system/fiori-design-web/ui-elements/select/) or [input fields](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/).
- Make selections when space is limited. On small screens, sliders can take up too much room. Consider using smaller [input](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/) options when the screen is crowded.

+----------------------------------------------------------x-----------------------------------------------------------+
Top Tips
+----------------------------------------------------------x-----------------------------------------------------------+
- Always label the slider to indicate what the selected value represents.
- When using custom sliders, keep labels short and meaningful to maintain a clear, easy-to-read, and visually
balanced descriptive scale.
- Use steps that match the required precision. Smaller steps help users choose more exact values when necessary.
- If relevant, display the unit of measurement next to or inside the slider or its related input field (for example,
%, kg, or °C).
- Display the current value near the slider or in a connected input field to enhance clarity and ease of use.

## Anatomy

1. **Start point:** Minimum value of the slider range.
2. **Track (active or inactive):** Shows the slider range. The active track extends from the start point to the current value, and the inactive track covers the remainder of the range.
3. **Value indicator (optional):** Displays the current value and can switch to an input field for direct editing.
4. **Tick marks (optional):** Represent the value steps. Each tick mark corresponds to a selectable value.
5. **End point:** Maximum value of the slider range.
6. **Labels (optional):** Display the values for selected tick marks along the slider.
7. **Slider handle:** Draggable grip used to select a value.

Anatomy of a slider

## Types

### Basic slider

Standard slider with a handle and track for selecting a value within a defined range.  It includes no additional elements, such as a value indicator or tick marks. Use when the value selection is simple, and no additional visual guidance is required.

Basic slider

### Slider without progress bar

A slider without a progress bar is useful when visual emphasis on the current value is not required.

Slider without progress bar

### Slider with value indicator

The value indicator appears above the handle to show or edit the current value. Use this option when precise feedback or direct manual entry is required.

**A. Value indicator:** Displays the current value above the handle.

**B. Editable value indicator:** Displays the current value above the handle in an input field that users can edit directly.

Slider with value Indicator – display and edit mode

### Slider with tick marks and labels

Tick marks appear along the track to represent value steps. Labels can be added to selected tick marks to show their values. Use this variant when the range includes predefined or incremental values.

Slider with tick marks and labels

### Custom scale and custom value indicators  :badge, info, large, _, SAPUI5 only:

The slider supports custom scales and value indicators, allowing descriptive labels instead of numeric values. Labels should be concise and meaningful to ensure clarity and usability. When labels are longer, the number of tick marks should be reduced to prevent visual clutter.

Slider with custom scale and value indicator

**> **Hint:** **

To use custom scales in a slider, you must map them to the floats for the slider scale.

## States

Components change their appearance based on their state, which helps users predict outcomes and understand how to interact with them.

### Component states

**Columns (col-2)**

The slider supports two component states: enabled and disabled.
**A. Enabled:** The slider is interactive and the user can adjust the value.
**B. Disabled:** The slider is non-interactive and cannot be adjusted.
For more information, see [Component States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-component-states)<u>.</u>
### Interaction states

**Columns (col-2)**

The slider has three interaction states: regular, hover, and down.
**A. Regular:** The default state for a component.
**B. Hover:** When the cursor is over the handle, it highlights to indicate it can be adjusted.
**C. Down:** Shown while the handle is pressed or being dragged.
For more information, see [Interaction States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-interaction-states)<u>.</u>
### Focus state

**Columns (col-2)**

When the handle is focused, it displays a visible border with a transparent fill, so the current value remains visible beneath it.
For more information, see [Focus States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-focus-states).

## Behavior and Interaction

### Dragging the handle to adjust the value

Users can drag the handle to precisely adjust the value within a defined range. The behavior follows these steps:

**A. Default state:** The slider is in its default state. The handle is placed either at a default range value (such as 0 and 100) or at a position defined by your application.

**B. Clicking the handle:** When a user clicks on the handle, it becomes transparent, ensuring that the current value underneath remains visible and easy to track.

**C. Dragging the handle:** The user can drag the handle along the track to adjust the value. If the value indicator is enabled, it remains visible throughout the interaction and provides real-time feedback by continuously updating as the user moves the handle.

This behavior offers direct manipulation and immediate feedback, making the slider ideal for scenarios where continuous value adjustment is necessary, such as setting a volume level, a percentage, or a specific range.

Dragging a handle to adjust a value

### Clicking on the track to adjust the value

Users can also adjust a value by interacting directly with the track itself. Clicking the track moves the handle to the clicked position.

**A. Start of interaction:** The slider is in its default state, with either a predefined value or a value that was previously modified.

**B. End of interaction:** When a user clicks anywhere on the track, the component instantly repositions the handle to that clicked location. This new position then becomes the slider’s current value, and the component updates accordingly.

This functionality is ideal for scenarios where users need to make quick, approximate selections or large jumps in value, rather than fine-tuned adjustments. For example, a user might click the track to jump from 20% to 80% quickly, then drag the handle for a precise adjustment from 80% to 83%.

Clicking or tapping the track moves the handle to a new point

### Snapping

The snapping mechanism in a slider is based on preconfigured step intervals. When the user drags the handle or clicks the track, the handle snaps to the nearest value according to the configured step interval. This feature helps users make accurate adjustments with ease and confidence, minimizing the likelihood of errors.

**A. Start of interaction:** As the user drags the handle to a new position, or after they click on the track, the component determines the intended value.

**B. End of interaction:** When the user releases the handle or after the click is registered, the handle automatically snaps to the nearest tick mark according to the component’s configured step interval. Simultaneously, the value indicator updates accordingly.

This snapping functionality is ideal for scenarios where continuous, free-form value selection is not desired. For example, you might use snapping to select quantities in whole numbers, adjust time intervals in 15-minute increments, or set percentages with specific jumps like 25%, 50%, 75%, and 100%. It reduces user error by only allowing valid selections and provides immediate visual confirmation of the chosen increment.

Tick marks snapping by handle dragging

### Editable value indicator

If the value indicator is editable, it switches to an input field, so the user can type a specific value instead of dragging the handle.

**A. Start of interaction:** The component allows the user to directly click on the value indicator, which then transforms into an input field. The user types a new value and then presses the **Enter** key to confirm their input.

**B. End of interaction:** The handle moves to its new position, and the value indicator updates accordingly.

This functionality provides flexibility. It’s ideal for scenarios where numeric precision is crucial, or when users find typing more efficient than visual adjustment.

Editing a value using the value indicator

## Responsiveness

By default, the slider takes the width of its parent container. It supports both [cozy and compact](https://www.sap.com/design-system/fiori-design-web/foundations/visual/cozy-compact) form factors.

### Tick marks and labels

When space becomes limited, the slider hides labels and tick marks to prevent overlap. The first and last labels always remain visible.

**A. Original size:** All tick marks and labels are visible.

**B. Reduced size:** Some tick marks and labels are visible.

**C. Further reduced size:** Only a few tick marks and labels remain visible.

 Tick marks and labels hidden progressively as space decreases

## Accessibility

SAP follows international standards, such as WCAG and WAI-ARIA, and strives to make our business solutions accessible and inclusive.

For more information, see [Accessibility in SAP Fiori](https://www.sap.com/design-system/fiori-design-web/discover/sap-design-system/product-standards/accessibility-in-sap-fiori) and the [Accessibility Design Tools Handbook](https://www.sap.com/documents/2023/11/bc210d8b-977e-0010-bca6-c68f7e60039b.html).

### Keyboard navigation

The following keyboard combinations are supported by the SAPUI5 Slider component.

**Table (col-width-30-70)**

Key Combination

**Tab**

**Shift \+ Tab**

**Right Arrow or Up Arrow / \+**
unit.

**Left Arrow or Down Arrow / -**
one unit.

**Ctrl \+ Right Arrow or Ctrl \+ Up Arrow or Page Up**
The handle moves to the right.

**Ctrl \+ Left Arrow or Ctrl \+ Down Arrow or Page Down**
The handle moves to the left.

**Home**
position.

**End**
position.

**Esc**
got the focus.

**F2**
handle. The user can type the value they want to set.

### Screen reader support

For details on screen reader support and Accessible Rich Internet Applications (ARIA), see the [UI5 Screen Reader Support](https://ui5.sap.com/#/topic/33fae3482358438e93daea5232527093) and [WAI-ARIA Authoring](https://www.w3.org/TR/wai-aria-1.2/).

## Content

### Wrapping and truncation

If the content exceeds the container width, it will be truncated automatically. Define an appropriate label width to maintain clarity and avoid unnecessary truncation.

Slider with truncating labels

### Localization

The slider supports both left-to-right and right-to-left layouts. In right-to-left mode, the track direction and handle movement mirror the reading flow.

Slider in left-to-right mode

## Framework Comparison

Some behaviors differ between frameworks due to implementation specifics. The table below summarizes the differences between SAPUI5 and SAP Web Components and lists the framework-specific patterns.

**Table (col-width-50-20-30)**

Feature                                                                                                                                                                            | SAPUI5    | SAP Web Components

The slider supports custom scale and value indicators, enabling the use of descriptive labels in place of numeric values. For more                                                 | Available | Not available
information, see [Custom scale and custom value indicators](https://www.sap.com/design-system/fiori-design-web/ui-elements/slider/usage#custom-scale-and-custom-value-indicators). |
**\**

---

## slider-web-component

+------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------+
+--------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------+---------x----------+
## This page has been deprecated and is no longer available.
This page was deprecated with guideline version **1.142**.
#### Reason for deprecation
The guidelines for the SAP Web Component and the SAPUI5 component have been merged. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).
#### Looking for the latest information?
Visit the page below for the unified guideline with the most recent updates.
[Slider](https://www.sap.com/design-system/fiori-design-web/ui-elements/slider/)

---

## switch

+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
Message Strip (information)
+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
This guideline now covers both SAPUI5 and SAP Web Components. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).

## Intro

The switch is a UI component used to toggle a setting on or off with a button. It lets users turn individual features on or off to adjust display settings or personalize the application’s appearance.

Switch with label

### Component availability

This component is available in the following libraries:

+-----------x------------+----------------------------------------------x-----------------------------------------------+----------------x-----------------+
Library                | Technical Name                                                                               | Identifier
+-----------x------------+----------------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit        | [sap.m.Switch](https://ui5.sap.com/#/entity/sap.m.Switch)                                    | :badge, info, large, _, SAPUI5:
+-----------x------------+----------------------------------------------x-----------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components     | [ui5-switch](https://ui5.github.io/webcomponents/components/Switch/)                         | Components:
+-----------x------------+----------------------------------------------x-----------------------------------------------+----------------x-----------------+
SAP Web UI Kit (Figma) | [Switch](https://www.figma.com/design/SILcWzK5uFghKun9jx6D7c/SAP-Web-UI-Kit?node-id=19-2027) | :badge, info, large, _, Figma:

**Table (external_only)**
+----------------x-----------------+----------------------------------------------x----------------------------------------------+----------------x-----------------+
Library                          | Technical Name                                                                              | Identifier
+----------------x-----------------+---------------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit                  | [sap.m.Switch](https://ui5.sap.com/#/entity/sap.m.Switch)                                   | :badge, info, large, _, SAPUI5:
+----------------x-----------------+----------------------------------------------x----------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components               | [ui5-switch](https://ui5.github.io/webcomponents/components/Switch/)                        | Components:
+----------------x-----------------+----------------------------------------------x----------------------------------------------+----------------x-----------------+
SAP Fiori for Web UI Kit (Figma) | [Switch](https://www.figma.com/community/file/1494295794601744471/sap-fiori-for-web-ui-kit) | :badge, info, large, _, Figma:

## When to Use

+-------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------+
When To Use
+-------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------+
Do
Use the switch to:
- Set a setting as active or inactive (for example, in a [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog/)).
- Clearly show the current mode or state of a setting.
- Apply changes that take effect immediately.
+-------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------+
Don't
Don't use the switch to:
- Allow selection of multiple options or require extra steps for changes to take effect.
- Show a state or action when it's unclear which one the component is displaying. Use a [checkbox](https://www.sap.com/design-system/fiori-design-web/ui-elements/checkbox/) instead.
- Include text inside the switch component, as this can cause localization issues.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
Top Tips
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
- Use a default switch when you need a simple on/off component with predefined icons and standard colors.
- Use a semantic switch when the action represents a positive or negative state.
- Add a descriptive label either above or directly before a switch component. This helps users understand which value or feature it controls.
- If the main label doesn't fully explain what "active" and "inactive" mean in your context, add a short text element (such as "On"/"Off" or status by using [text](https://www.sap.com/design-system/fiori-design-web/ui-elements/text/) or [object status](https://www.sap.com/design-system/fiori-design-web/ui-elements/object-display-elements/)) next to the switch to clarify.

## Anatomy

The switch consists of a background track and a movable handle.

1. **Track:** Displays the container for the handle.
2. **Handle:** Indicates whether the switch is on or off, depending on its position within the track.

Switch anatomy

## Types

There are four switch types: default, semantic, switch with label, and switch with optional text. While switches don’t typically support value states, the semantic type uses color to add specific meaning to the on or off states.

### Default switch

The default switch type uses an icon inside the handle
and the default colors for on or off states.
Default switch

### Semantic switch

The semantic switch represents a positive or negative
status by using specific colors instead of the default
ones: green indicates the positive (on) state, and red
indicates the negative (off) state. Each semantic state
also displays a system-defined icon that cannot be
changed.
### Switch with label

Make it clear what value or feature the switch controls by placing a [label](https://www.sap.com/design-system/fiori-design-web/ui-elements/label/)  above or before the switch. For example, “Enable Notifications” or “Receive Updates”.
Switch with label

### Switch with optional text

Add optional text after the switch to explain what
“active” and “inactive” mean for the specific use case.
Keep the text short, ideally a single word.

## States

States define how components look and behave in different scenarios, helping users predict interaction outcomes.

### Component states

The switch has two component states – enabled and
disabled. When enabled, the switch is interactive and can
be toggled. When disabled, the switch is not interactive
and only displays its current value, either unselected
(off) or selected (on).
**A. Enabled state:** The switch is interactive and the
user can turn it on or off.
**B. Disabled state:** The switch is not interactive, but
remains visible so the user can view its current state.
For more information, see [Component States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-component-states).

### Interaction states

The switch has two interaction states – regular and hover. The regular and
hover interaction states are supported in both the on and off modes.
Regular and hover switch interaction states
**A: Regular state:** The default state of the component.
**B: Hover state:** The state when the cursor is positioned over the switch.
For more information, see [Interaction States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-interaction-states).

### Focus state

The focus state indicates which component is currently in
focus.
Unfocused and focused switch states
**A: Unfocused state:** The switch is not in focus and
does not display a focus indicator.
**B: Focused state:** The switch displays an additional
border around the track to indicate focus.
For more information, see [Focus States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-focus-states).

## Behavior and Interaction

The switch toggles between on and off when the user clicks or taps it. Visual feedback updates immediately to reflect the new state. The component supports interaction through mouse, touch, and keyboard.

### Turning a switch on or off

A switch toggles between on and off states through user interaction. The component supports multiple interaction methods:

- **Clicking:** Single click toggles the state.
- **Dragging:** Hold and drag the handle to transition between states.
- **Tapping (on touch devices):** Tap to toggle the state.

When toggled, the switch updates its visual appearance with a new color, icon, and handle position. A focus indicator appears during keyboard or interaction focus.

Turning switch on

**Note:** Hover states are not supported on touch devices. For more information, see [tap gesture](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/gestures#tap-press-and-release) and [drag gesture](<https://www.sap.com/design-system/fiori-design-web/foundations/interaction/gestures" \l "drag-tap-and-hold-move-and-release>).

### Tooltips

Provide a tooltip when no label is available to give context for the switch. The label identifies what the switch controls and the effect of toggling it.

Switch with tooltip

## Responsiveness

The switch does not adapt responsively, but it supports two content density modes depending on the device:

- Compact (mouse and keyboard input)
- Cozy (touch input)

Switch in compact and cozy modes

For more information, see [Content Density](https://www.sap.com/design-system/fiori-design-web/foundations/visual/cozy-compact).

## Accessibility

SAP follows international standards, such as WCAG and WAI-ARIA, and strives to make our business solutions accessible and inclusive.

For more information, see [Accessibility in SAP Fiori](https://www.sap.com/design-system/fiori-design-web/discover/sap-design-system/product-standards/accessibility-in-sap-fiori) and the [Accessibility Design Tools Handbook](https://www.sap.com/documents/2023/11/bc210d8b-977e-0010-bca6-c68f7e60039b.html).

### Keyboard navigation

The following keyboard combinations are supported by the SAPUI5 Switch component.

**Table (col-width-30-70)**

Key Combination

**Tab**

**Shift \+ Tab**

**Spacebar or Enter/Return**

### Screen reader support

For additional details on screen reader support and Accessible Rich Internet Applications (ARIA), see the [UI5 Screen Reader Support](https://ui5.sap.com/#/topic/33fae3482358438e93daea5232527093) and [WAI-ARIA Authoring](https://www.w3.org/TR/wai-aria-1.2/).

## Content

### Localization

The switch component supports both left-to-right (LTR) and right-to-left (RTL) reading directions.

Switch in left-to-right mode

### Wrapping and Truncation

By default, label text wraps automatically. Use truncation only when space is limited. Apply a hybrid approach when needed: allow the label to wrap for up to N lines, then truncate any remaining text. Keep labels concise, and reserve truncation for edge cases when no other option is available.

For more information, see [Wrapping & Truncation](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/wrapping-and-truncation).

#### Label on top

For top labels, when the text wraps, the switch is pushed down by the additional lines. The number of wrapped lines depends on the label’s length.

Switch with top label wrapping

#### Label and optional text

By default, the optional text wraps. Avoid truncation and keep both the label and optional text short and concise.

Switch with wrapping and truncation of optional text

#### Label to the side

When a side label cannot fit horizontally, the switch moves below the label. The text wraps by default.

Switch with side label repositioning

## Framework Comparison Overview

There are no differences between SAPUI5 and SAP Web Components regarding thе component's behaviors and framework-specific patterns.

---

## switch-web-component

+------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------+
+--------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------+---------x----------+
## This page has been deprecated and is no longer available.
This page was deprecated with guideline version **1.145**.
#### Reason for deprecation
The guidelines for the SAP Web Component and the SAPUI5 component have been merged. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).
#### Looking for the latest information?
Visit the page below for the unified guideline with the most recent updates.
[Switch](https://www.sap.com/design-system/fiori-design-web/ui-elements/switch/)

---

