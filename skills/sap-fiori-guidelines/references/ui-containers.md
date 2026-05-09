# SAP Fiori UI Elements: Containers

This reference covers the following UI components:

- [Cards](#cards)
- [Filter Bar](#filter-bar)
- [Notification Center](#notification-center)
- [P13N Dialog Popup](#p13n-dialog-popup)
- [Popover](#popover)
- [Popover Web Component](#popover-web-component)
- [Responsive Popover Web Component](#responsive-popover-web-component)
- [Shell Bar](#shell-bar)
- [Smart Filter Bar Annotations](#smart-filter-bar-annotations)
- [Table Bar](#table-bar)
- [User Menu](#user-menu)

---

## cards

A card represents an app or page. It can be used to launch the app or navigate to the page content. Integration cards are a way of making application content available to end users in a consistent manner.

Integration cards are similar to the cards on the [overview page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page/). However, unlike the overview page cards, integration cards can be used in different host environments.

A card can show details about a single app or page, or contain related information from multiple sources. An app or page can also be represented by several cards, which each focus on a different aspect of the content.

*Card examples*

## When to Use

You can offer cards on the SAP Fiori launchpad or embed them in other controls.

Offer a card if:

- You want to give users easy access to an app or page that is relevant for a business task.
- You want to show a KPI or a preview of the most important content for the task.
- You want to let users complete a simple action right away, without navigating to the underlying app.

## Card Anatomy

A card comprises a [header](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/cards/#header) and a [content area](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/cards/#content-area), which are separated by a divider line. Both components are inside a card container, which includes the background and the border.
### Header
The header shows what the card is about. There are two variants: the [default header](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/cards/#default-header) and the [numeric header](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/cards/#numeric-header).
#### Default Header
The default header shows the basic information about the card and has the following components:
1. The **title** is mandatory and represents the “point of view” of the card. Titles longer than three lines are truncated with an ellipsis (…).
2. Optional: You can use a **subtitle** to qualify the title or explain the context. Subtitles that exceed two lines are truncated.
3. Optional: You can use an **[avatar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/avatar/)** to provide a visual hint on the card header (for example, an image, icon, or initials).
4. If the content area contains multiple items, a **counter** is added to the header. It shows how many items are visible on the card in
relation to the total number of relevant items (for example, “6 of 12”).
#### Numeric Header
Use the numeric header if you need to display numeric
information.
1. Mandatory title
2. You can add a subtitle with additional qualifying
information (optional).
3. If you specify a currency or unit of measurement, it
also appears in the subtitle row. If you provide both a
subtitle and a unit of measurement, the display format is: **\<subtitle text> \| \<unit of measurement>**.
4. In additional to the general information, you can
configure the visualization for a numeric value, such as a
KPI.
5. If required, you can also show up to two additional
indicators that relate to the main KPI.
6. If required, you can display more information about the
numeric value directly below it (for example, the period
for which a KPI applies).
> **Guideline:** Ensure that the card title is short, clear and precise.
Provide all the information required to interpret the numeric value (specific description, currency or unit of
measurement, relevant period).
- For currencies and standard units of measurement, use the dedicated `unitOfMeasurement` property. The unit then
appears consistently in the subtitle line. If the value is a simple count (such as the number of open tasks), a
precise title/subtitle text is usually sufficient.
- If the value applies to a period, use the footer area (5) to specify the period.

### Content Area

The content area is reserved for showing information from the underlying source(s). Cards can represent different types of content, with several visualization options. This depends on which card type is used.

> **Guideline:** In the card content area, show the most relevant data for the task at hand.

## Card Types

The card type defines how content is presented (for example, as a list or table). The embedded controls govern the layout, navigation, and interaction in the card content area.

The following card types are available:

- [List card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/cards/#list-card)
- [Analytical card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/cards/#analytical-card)
- [Table card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/cards/#table-card)
- [Object card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/cards/#object-card)
- [Timeline card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/cards/#timeline-card)
- [Calendar card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/cards/#calendar-card)
- [Component card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/cards/#component-card)

### List Card
The list card can display multiple list items of various
types.
### Analytical Card
The analytical card visualizes analytics data. It can
contain a line chart, bar chart, or donut chart.
### Table Card
The table card displays multiple items in a table view.

### Object Card
You can use this card type to display information about
an object in groups. Each group can contain as many items
as needed.
### Timeline Card
The timeline card displays time-related content in
chronological order.
### Calendar Card
The [calendar card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/calendar-card/) shows the schedule for a single entity (typically a person) for a selected day.

### Component Card

The component card allows you to display a SAPUI5 component as content. This gives you significant flexibility in configuring the content.

## Behavior and Interaction

Default (col-1)

### Card Header
The whole header is clickable and is the navigation area for opening the underlying source. Clicking the header opens
the app or page that relates to the card.
### Card Content
The content area can have several click areas with different purposes. They depend on the control used and the
structure of the content.

> **Guideline, Col-1:** Always provide meaningful navigation targets. Ensure that the navigation target supports the information flow that
starts on the card.

Default (col-2)

*Card interaction*

Section Metadata

style

## Responsiveness

The responsive behavior for integration cards depends on the container control of the host environment (for example, SAP Fiori launchpad). The size of the card adapts dynamically to the size of the container.

## Top Tips

- Cards introduce users to the content in the underlying source. Make sure that your card focuses on the most relevant content.
- Use cards if supportive visualizations and meaningful navigations are helpful for users.
- Don’t use individual branding.
- Avoid unnecessary white space on the card.

---

## filter-bar

The filter bar lets users set criteria to limit the data loaded and displayed in a table. It is part of the [list report](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/) and the [overview page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page/), and is also available as an alternative layout to the visual filter bar in the [analytical list page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/#layout-variants).

It is made up of input controls that filter objects according to various criteria, such as status or date. Users can [adapt](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/filter-bar/#adapt-filters-dialog) the filter bar, for example, by showing and hiding input controls or changing their order. They can also store the current set of filter criteria in a [view](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/).

The filter bar is displayed in the header area of a [list report](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/), [overview page,](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page/) or [analytical list page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/). Because these floorplans are based on the [dynamic page layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/), the expand and collapse header functions are available.

## When to Use

The filter bar is always part of the list report and overview page.

Do not use the filter bar:

- In a table in an object page section. Use the filter in the *[View Settings](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/view-settings-dialog/)* dialog instead.
- In a wizard.
- In a simple list. Use the [search](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/search/) instead.

## Filter Bar Components

### Expanded Filter Bar

The expanded filter bar consists of:

1. Views (optional)
2. Basic [search](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/search/) field (optional)
3. [Filter input controls](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/filter-bar/#filter-input-controls)
4. *Go* button (only for [manual update mode](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/filter-bar/#behavior-and-interaction))
5. [*Adapt Filters* button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/filter-bar/#adapt-filters-dialog)

*Expanded filter bar*

[Views](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/) **(1)** store the settings for the filter bar, including the values of filter input controls, the fields visible in the filter bar, and their order.

You can also use the filter bar without view management. In this case, display a page title instead.

If the [basic search field](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/search/) **(2)** is available, it is displayed first. It allows users to filter the results with a given keyword. Unlike the other input control fields, the basic search field has a placeholder text instead of a label.

The [filter input controls](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/filter-bar/#filter-input-controls) **(3)** are arranged in a horizontal, linear layout, with a label above them. An asterisk next to the filter label indicates the filter is mandatory.

If the browser window size is reduced or filter input controls exceed the available width, they wrap to the next line. The height of the expanded filter bar is not limited and adjusts to accommodate the visible filters. The size of the widest input control is inherited by all other filters to ensure visual cohesion.

The *Go* button **(4)** triggers the search for the manual update mode. Alternatively, you can offer the live update mode where the table results are updated each time the user changes an input control value. For more information, see [Behavior and Interaction](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/filter-bar/#behavior-and-interaction).

In most cases, only a subset of all available filters is visible in the filter bar. Users can control the visibility and order of the filters and assign values to them in the [*Adapt Filter* s dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/filter-bar/#adapt-filters-dialog) **(5)**.

Next to *Adapt Filters*, the number of active filters is displayed in parentheses. A filter is active when a value is assigned to it either in the filter bar or the *Adapt Filters* dialog. **Note** that a filter can be active, but not visible in the filter bar.

### Collapsed Filter Bar

The collapsed filter bar takes up very little space, leaving most of the screen to display the results.

*Collapsed filter bar*

It shows a summary of the filters currently applied:

- Either *1 filter active:* or *\<n> filters active:*, where “n” stands for the number of applied filters.
- A comma-separated list of the currently applied filters for up to five filters. If there are more, an ellipsis (…) shows at the end of the string.

If no filters have been applied, the summary text is: *No filters active*

### “Adapt Filters” Dialog

Users can manage all the available filters in the *Adapt Filters* dialog, including their visibility and order in the filter bar and the values of filters both visible and not visible in the filter bar.

*Adapt Filters dialog - list view, hidden values*
The *Adapt Filters* dialog consists of:
1. Select control and search
2. *Show Values*/*Hide Values* toggle
3. List or group view
4. Mandatory and optional filters
5. Footer bar buttons
6. Arrows to move the filter up and down
7. Active filter with assigned value
When opened, the dialog displays all the available filters in the *Hide Values* view with the *List* view.
The selected filters are visible in the filter bar and displayed in the same order as in the filter bar.
#### Searching and Displaying Filters in the Dialog
To find filters **(1)**, users can search for them by name or use the select control to limit the filters displayed
in the dialog to certain filter types, such as visible, active, or mandatory.
Mandatory filters have an asterisk next to their label **(4)**. They must have values for the search to return results. Users can set the values either in the filter bar or the *Adapt Filters* dialog.
In the dialog, when a mandatory filter has:
- No value assigned, its checkbox is automatically selected and cannot be deselected.
- A value assigned, the users can deselect it to remove the filter from the filter bar.
In the dialog, users can display the filters:
- With or without the filter values **(2)**.
When the values are hidden, a visual indicator **(7)** flags the active filters.
- In the list or group view **(3)**.
The group view shows the filters according to group. The first group is called *Basic* and contains the filters for
the standard view that you design to ship with the app. You can design additional views to ship with the app, but no
additional groups are created for these views.
#### Displaying Filters in the Filter Bar
All the views in the dialog allow users to select filters to be visible in the filter bar.
In the *Hide Values* view with the *List view*, users can reorder the selected filters with the arrows **(6)**.
In the *Adapt Filters* footer bar **(5)**:
- *OK* applies changes and closes the dialog.
- *Cancel* closes the dialog without applying changes.
#### Resetting Filters
In the header area, *Reset* **(8)** (optional) restores the selected filters and filter values to the ones in the
current view. Before the filters are reset, the user gets a warning because the reset applies immediately to the
filter bar, even though the dialog stays open. Clicking *Cancel* in the footer bar does not reverse the reset action.
### Filter Input Controls

To prevent unnecessary complexity in the filter bar, pick the simplest input control that works for your use case, as recommended below:

Table

For

A predefined list for single or multiple selection

Temporal information

[Multi-input fields](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/multiinput/)

For a comprehensive overview of when to use which input field, see [Which Selection Control Should I Use?](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/which-selection-control-to-use)

Use the [value help control](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/value-help-dialog/) only as a last resort. It is especially beneficial if you want to offer an advanced function for selecting single or multiple items either inline (by entering text) or by means of a dialog.

> **Hint:** For development information, see [Data Types](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/smart-filter-bar-annotations/#data-types) for the smart filter bar.

For more information on the selection controls, see:

- [Input](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/input-field/)
- [Select](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/select/)
- [Combo box](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/combo-box/)
- [Multi-combo box](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/multi-combobox/)
- [Multi-input](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/multiinput/)
- [Value help](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/value-help-dialog/)
- [Date picker](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/date-picker/)
- [Date range selection](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/date-range-selection/)
- [Date/time picker](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/datetime-picker/)
- [Rating indicator](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/rating-indicator/)

## Behavior and Interaction

In the **live update mode**, the search results are updated each time the user changes the value of an input control or the search field. A *Go* button is not necessary.

As the user types in the search field, the search is triggered with the entry of each character. The table is updated with the results that match all the filter values and include the search term.

In the **manual update mode**, the search results are updated only when the users click *Go* or press **Enter** on their keyboard.

For **both update modes**, when selection is enabled for the table, make sure the update resets or “forgets” previously selected table items by asking the application developers to set the table property [rememberSelections](https://main--builder-prospect--sapudex.aem.page/design-system/fiori-design-web/v1-142/ui-elements/responsive-table/#properties) to “false.”

## Responsiveness

The name of the view or title is always visible.

The filter area (basic search field, input controls, optional *Go* button, *Adapt Filters* dialog) varies:

- Desktop: Expanded or collapsed by default
- Tablet: Collapsed by default
- Phone: Not displayed. Accessible through filter dialog.

## Examples

Carousel (full-width)

## Top Tips

### Filter Bar

Always provide a set of predefined default filters to deliver with the app (*Basic* group in the *[Apply Filters](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/filter-bar/#adapt-filters-dialog)* dialog). Include filters that are:

- Mandatory / crucial for the use case
- Frequently used
- Vital for reducing the number of items in the list

Users can set filters from the *Basic* group not to display in the filter bar, but cannot remove them from the *Adapt Filters* dialog.

### Filter Input Controls

- Use the basic search field to provide a keyword search. Do not show a search field in the table toolbar.
- Pick the simplest selection control that works for your use case. See [When to Use which Selection Control?](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/which-selection-control-to-use)
- For temporal filters, use the [date picker](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/date-picker/) or [date range selector](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/date-range-selection/).
- To help the user enter a valid value for [multi-input fields](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/multiinput/), enable suggestions.

### Preset Filter Values

- Provide meaningful default values for as many filters as possible to prevent unnecessary data from loading. This is particularly important when the application has large data sets.
  **Example:**
  A default value for date ranges should reflect the time frame the user would normally apply.
- For list reports and overview pages, preset values for mandatory filters to prevent error messages when the page loads.

### Update Mode

- Whenever possible, use the live update mode because it is more convenient for the user.
- Consider the manual update mode only in cases where:
  - The volume of unfiltered data to load would be excessively high.
  - The users need to enter multiple filter values to display results they can work with.

---

## notification-center


## Intro

Notifications serve as real-time alerts, providing users with information about significant events, updates, or changes in business processes, workflows, or data. Notifications ensure users remain informed and can take timely action or make decisions without disrupting ongoing tasks.

Notifications are temporary, one-way messages triggered by an event. Users can read, act on, dismiss, or simply ignore them; engagement is optional. Once sent, the notification content remains and cannot be changed or retracted, so notifications might become outdated.

Users can access notifications by clicking the bell icon :bell: in the top-right corner of the screen.

Open notifications panel


The notification experience is available as a ready-to-run plugin (front end and backend) that can be integrated into products. For more information, see the Technology Guidelines Business Notifications TG47.

## When to Use

Notifications should be well-instrumented to provide value to users. Using notifications effectively involves timing them to provide value without being intrusive. An excessive number of notifications can frustrate users, diminishing their effectiveness. Notifications should be brief and concise, conveying specific information or prompting an action.

In a nutshell, a notification should be:

- Clear on its purpose (e.g., update, reminder, or alert)
- Concise and to the point
- Relevant and useful for the user
- Well-timed
- Personalized, where possible
- Action-oriented, with a clear call to action
- Transparent on importance (ensure that you use the importance indicator consistently across your product)
- Well-paced (avoid overwhelming users with too many messages in a short time span)

### Notification Scenarios

Here are some scenarios where using notifications can be beneficial:

- **Reminders**:
  For upcoming events, appointments, deadlines, payments, or tasks that require the user's attention or action.
- **Alerts**:
  For urgent information, such as business critical alerts.
- **Updates**:
  Significant changes to something the user is interested in, such as status updates or workflow progress.

> **Guideline:** - Always consider the user's perspective and the context in which they're receiving the notification.
- Aim to provide value and relevance without overwhelming or interrupting the user.
- Consider grouping notifications for similar event types. If the number of notifications reaches a certain threshold
and the event is not business-critical, grouping notifications reduces the overall the number of notifications.

While these experiences might seem similar initially, they each serve a different purpose, follow different lifecycles, and require distinct features
and interactions to coexist effectively. These experiences may use notifications to inform users of news and updates but will reside within their own
contexts.
Notifications integrate events and updates from various sources in one place. Please also consider the <u>Product Standard for UX Consistency 024</u>.

## Anatomy – Notification Panel

+-------------------------------------------------------------------------------x-------------------------------------------------------------------------------+:-----------------------------------:+
1. **Notification panel title**
2. **Notification panel actions**
*Anatomy of the notification panel*
- ***Clear All***: Removes all notifications
- ***Sort***:
- By date (default)
- By importance
- **Notification settings:** Link to all notification settings
3. **Notification list**: Contains notification group and notification list items (scrolling area).
4. **Notification group item**: Collapsible group that contains notification list items when expanded. The group title is displayed in bold if it contains
one or more notification list item that has not been read.
5. **Notification list item**: See below.
6. **Notification panel**: A [popover](https://www.sap.com/design-system/fiori-design-web/ui-elements/popover/) is used as a base for the notification panel.
## Anatomy – Notification List Item

+----------------------------------------------------------------x----------------------------------------------------------------+---------------------------------------+
1. **Avatar**:  You can use an additional avatar to give a notification more context. Only display avatars when they help users
to distinguish notification items.
2. **Status indicator:** You can use this visual indicator to display the following states:
- Positive
- Negative
- Critical
3. **Title**: Initially displays a maximum of 2 lines.
4. **Action**: Unsubscribe and legacy actions.
5. **Delete**: Removes the notification item from the list.
6. **Description**: Initially displays a maximum of 2 lines.
7. **More / Less**: If the title or description exceeds two lines, a *More* link allows the user to display the truncated text.
8. **Timestamp**
9. **Importance indicator**: Important notifications can be marked with an importance indicator.
10. **Source information**: Indicates the business domain or process that triggered the notification. This can be beneficial
for products with a broader scope.
## Behavior and Interaction

### Scrolling

The notification group titles remain fixed at the top of the scroll container as you scroll. When you reach the next group, the title at the top of the container changes to the title of this group.

Notification panel – scrolling

### Clear All

The *Clear All* button removes all notifications that are currently in the panel. The user is prompted to confirm the action.

Notification panel – ‘Clear All’ button

### Sorting

The notification panel offers two sort options:

- **By Date** (default):  Newest to oldest
- **By Importance**: Notifications with importance indicators are grouped in an “Important” group. This group is displayed at the top of the panel and sorted by newest to oldest. The remaining notifications are grouped under “Other” below the “Important” group. They are sorted by creation date in descending order.

Notification panel – sorting by date or importance

### Expand / Collapse Notification Group

Users can expand and collapse notification groups using the chevron to the left of the notification group title.

Expanded and collapsed notification groups

### Unread / Read

The title of the notification item is **bold**, indicating that it hasn't been clicked. When the user clicks the notification, the title's font weight changes from **bold** to normal.

Unread and read notification items

### Unsubscribe Action

The overflow button :overflow: allows the user to access the *Unsubscribe* option for this specific notification type. We do not recommend adding further actions.

'Unsubscribe’ action for a notification item

### Delete

Clicking *Delete* :decline1: removes the notification item.

### More / Less

The title and description for a notification item are each limited to two lines. Longer texts are truncated. To view the full text, the user can click *More*. Clicking *Less* shows the truncated text again. 

'More’ and ‘Less’ buttons for a notification item

### Banner Fly-In

Users can set certain notifications to fly in from the right as banners while using the product. These notifications appear for five seconds before sliding away. Users can interact with them if necessary. Clicking the *Dismiss* button :decline1: removes the notification, but it remains listed in the notification panel.

Banner fly-in

### Bell Interaction

The counter above the bell icon :bell: shows the number of new notifications received since the user last opened the notification panel. Clicking the bell icon resets the counter to zero and the badge is hidden.

Desktop: If the notification count is 1000 or more, the counter shows +999.

Mobile: If the notification count is 100 or more, the counter shows +99.

Bell interaction

## Responsiveness

The notification panel is fully responsive.

*Size S*

## Content

To ensure clear and actionable notifications across products, follow the standard conventions for message structure, tone, terminology, and information placement.

For more information, see [UX Writing for Notifications](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/ux-writing-for-notifications).

---

## p13n-dialog-popup

The P13n dialog control tabs allow users to personalize table and smart chart attributes.

**Table Personalization Tabs**

- **[Columns](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/p13n-dialog-popup/#columns)**: Visibility and order of columns
- **[Sort](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/p13n-dialog-popup/#sort)**: Sort criteria for table items
- **[Filter](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/p13n-dialog-popup/#filter)**: Filter criteria for table items
- **[Group](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/p13n-dialog-popup/#group)**: Grouping table items by specific attributes

The tabs can be shown in any combination, as required by the use case.

The P13n dialog is intended for complex [tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/) that have a large number of columns and require complex queries for sorting, grouping, and filtering.
For simple tables, see the [view settings dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/view-settings-dialog/) and [table personalization dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-personalization-dialog/).

**[Smart Chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/smart-chart/) Personalization Tabs**

In addition to the *Sort* and *Filter* tabs, the P13n dialog for smart charts can include the *[Chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/p13n-dialog-popup/#chart)* tab to allow users to set the visibility of chart dimensions and measures.

The P13n dialog is opened using the corresponding buttons on the right-hand side of the table or chart toolbar, as shown below.

#### Dialog buttons within the toolbar

Carousel (full-width)

## Usage

### Use the P13n dialog if:

- Users can personalize more than \~20 columns.
- You need multiple personalization functions (columns, sorting, filtering, grouping, …)
- You are using the [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/).
- Complex queries have to be built for the table.

### Do not use the P13n dialog if:

- Users can personalize fewer than \~20 columns.
- You only need a simple feature to show/hide columns.

## Responsiveness

The P13n dialog is available for all display sizes. For sizes L/XL (desktop) and M (tablet), it shows as a centered dialog. For size S (smartphones), it displays as a full screen dialog.

*Size S – Columns* | *Size M*    | *Size L*

## Components

The P13n dialog can include the following tabs, separately or combined, as required by the use case:

- Sort
- Filter
- Columns (available only for tables)
- Group (available only for tables)
- Chart (available only for the Smart Chart)

App developers can add more tabs manually.

## Behavior and Interaction

### Sort

Default (col-1)

On the *Sort* tab, the user can specify the sort criteria and sort order (ascending or descending).
Each entry has two input fields:
- One for choosing the sort column in a table or the sort dimension or measure in a smart chart
- The second for choosing the sort order.
Users can enter multiple sort criteria. Once a sort criterion is entered, a new line appears for entering another
one.
The order of the sort criteria reflects the order in which they are applied to the table or smart chart.

> **Information, Col-1:** - The new P13n panels from the SmartTable (*Columns*, *Sort*, *Group*) are now available for freestyle application development.
- Using the sort feature for column headers replaces ALL sort options in the dialog!

Default (col-2)

*Sort settings in the P13n dialog*

Section Metadata

style

### Filter

Carousel (full-width)

The Filter tab allows users to filter the table or chart information according to specific criteria.

Once a filter criterion is entered, a new line appears for entering another one. Users can remove filters by clicking the :decline: (Remove Filter) icon at the end of each filter item.

#### Filter Criterion

In the first input field, the user selects the column (for tables) or the dimension/measure (for charts) to be filtered. Any column or dimension/measure can be selected, including columns and dimensions/measures that are not currently visible.

#### Define Conditions

The second field is an input field which calls a [Value Help Dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/value-help-dialog/) when the user clicks the selection icon (value help icon) in the input field.

The first input field in the value help dialog contains the operator that is applied to the filter value (such as greater than or not before).

To include or exclude filter criteria, the user selects the relevant operator from the Include or Exclude section of the dropdown list. For example, equal to to include a value, or not equal to to exclude it.

If individual filter criteria have Boolean values, the operator is always “equal to” and the operator dropdown is disabled.

##### Available Operators

*String (Text)*         | *Number*                | *Date*         | *Boolean (true/false)*
- between               | - between               | - between      | - equal to
- contains              | - equal to              | - equal to     |
- equal to              | - greater than          | - after        |
- begins with           | - greater than or equal | - on or after  |
- ends with             |   to                    | - before       |
- greater than          | - less than             | - before or on |
- greater than or equal | - less than or equal to |                |
to                    |                         |                |
- less than             |                         |                |
- less than or equal to |                         |                |
#### Value

The second field in the value help dialog contains the value by which the selected column is filtered. The kind of input field that is provided depends on the data type of the selected column and the selected operator. For example, the value field for fixed or Boolean values could be a dropdown list, an input field with suggestions, or a date picker. You can also offer two or even more fields if the use case requires it.

The above mentioned guidance for filtering is applied to both the table and chart personalization.

> **Information:** If there is a filter bar, use the filter bar functionality and deactivate the filter feature of the P13n dialog.

### Columns

The *Columns* tab allows users to change the visible
table columns and the order in which they are displayed.
*Column settings in the P13n dialog*
The available columns are shown as list items with
checkboxes. The checkboxes for the columns that are
currently being displayed are selected.
*Hide (All) Unselected* toggles the display between all
columns and only those that are currently selected.
#### Show/Hide
To show or hide a column, users select or deselect the
column checkbox.
#### Reorder
To change the order of the columns, users focus on a list
item and use the buttons on the right-hand side of the
table toolbar to move it up or down. The order of the
columns from top to bottom corresponds to the order on
the table from left to right.
#### Search
The search field in the table toolbar enables users to
find a specific column more quickly. Matching columns are
displayed as soon as the user starts to type.
#### Filters Icon

When both description cells and selected cells are available on the column tab, a *Filters* icon replaces the  *Hide (All) Unselected*
toggle. Selecting the icon opens a popover where users can show or hide content,
such as description cells and unselected items, to adjust the view to their needs.
descriptions

> **Information:** The new P13n panels from the SmartTable (*Columns*, *Sort*, *Group*) are now available for freestyle application development.

### Group

The *Group* tab allows users to group the table data.
In the select control, they can select a grouping criterion from a list of all available columns.
For [analytical tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/),
users can define more complex grouping scenarios. Once a grouping criterion is entered, a new line appears for entering another one. In
addition, the *Show Field As Column* checkbox allows users to decide whether or not to display the corresponding column.
The grouped table shows the individual values for the selected field as the group headers. Expanding the group shows all the corresponding
table items.
If you have defined multiple groups, the grouped table shows the individual values for the first selected field. Expanding the groups shows
the subgroups and items in an expandable hierarchy.
> **Information:** The new P13n panels from the SmartTable (*Columns*, *Sort*, *Group*) are now available for freestyle application development.

> **Warning:** Only columns marked as visible on the *Columns* tab can be used for grouping!

### Chart

Columns
The *Chart* tab allows users to set the visibility of chart dimensions and measures and to change the order in
which they are displayed.
*Chart settings in the P13n dialog*
Users can add dimensions and measures with the select control or remove them by clicking the :decline: (*Remove dimension/measure*) icon at the end of each chart item.
They can enter multiple dimensions and measures. Once a dimension or measure is entered, a new line appears for
entering another one.
The order of the entered dimensions and measures reflects the order in which they are applied to the chart.
#### Dimensions
Each entry has two select controls: one for choosing the dimension, and one for choosing the layout option. The
dialog is adapted to the currently selected chart type and shows layout options that work on the selected chart
type.
#### Measures
In the select control, the user can select a needed measure from a list of all available measures.
#### Reorder
To change the order of the dimensions and measures, users focus on the list item and use the buttons on the
right-hand side of the table toolbar to move it up or down or by dragging the dimension/measure to the desired
location.
> **Warning, Col-1:** Users can select or change a chart type via the Smart Charts toolbar!

## Resources


#### Elements and Controls                                                                                                                                                                                    | #### Implementation                                                                                            | #### Visual Design
- [Table Personalization Overview](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/overview-table-personalization) (guidelines) | - [P13n Dialog](https://ui5.sap.com/#/entity/sap.m.p13n.Popup/sample/sap.m.sample.p13n.Popup) (SAPUI5 samples) | - Table Personalization (visual design specification)
- [View Settings Dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/view-settings-dialog/) (guidelines)                                                      | - [P13n Dialog](https://ui5.sap.com/#/api/sap.m.p13n.Popup) (SAPUI5 API reference)
- [Table Personalization Dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-personalization-dialog/) (guidelines)                                      |
**Columns (external_only)**

#### Elements and Controls                                                                                                                                                                                    | #### Implementation
- [Table Personalization Overview](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/overview-table-personalization) (guidelines) | - [P13n Dialog](https://ui5.sap.com/#/entity/sap.m.p13n.Popup/sample/sap.m.sample.p13n.Popup) (SAPUI5 samples)
- [View Settings Dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/view-settings-dialog/) (guidelines)                                                      | - [P13n Dialog](https://ui5.sap.com/#/api/sap.m.p13n.Popup) (SAPUI5 API reference)
- [Table Personalization Dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-personalization-dialog/) (guidelines)                                      |

---

## popover

+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
Message Strip (information)
+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
This guideline now covers both SAPUI5 and SAP Web Components. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).

## Intro

The popover is a small overlay window that appears on top of an existing UI element. It displays additional information for an object in a compact way and without leaving the page. The popover can contain various UI elements such as fields, tables, images, and charts. It can also include actions in the footer.

Popover

### Component availability

This component is available in the following libraries:

+-----------x------------+-------------------------------------------------x-------------------------------------------------+----------------x-----------------+
Library                | Technical Name                                                                                    | Identifier
+-----------x------------+---------------------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit        | [sap.m.Popover](https://ui5.sap.com/#/entity/sap.m.Popover)                                       | :badge, info, large, _, SAPUI5:
+-----------x------------+-------------------------------------------------x-------------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components     | [ui5-popover](https://ui5.github.io/webcomponents/components/Popover/)                            | Components:
+-----------x------------+-------------------------------------------------x-------------------------------------------------+----------------x-----------------+
SAP Web UI Kit (Figma) | [Popover](https://www.figma.com/design/SILcWzK5uFghKun9jx6D7c/SAP-Web-UI-Kit?node-id=153790-1130) | :badge, info, large, _, Figma:

**Table (external_only)**
+----------------x-----------------+----------------------------------------------x-----------------------------------------------+----------------x-----------------+
Library                          | Technical Name                                                                               | Identifier
+----------------x-----------------+----------------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit                  | [sap.m.Popover](https://ui5.sap.com/#/entity/sap.m.Popover)                                  | :badge, info, large, _, SAPUI5:
+----------------x-----------------+----------------------------------------------x-----------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components               | [ui5-popover](https://ui5.github.io/webcomponents/components/Popover/)                       | Components:
+----------------x-----------------+----------------------------------------------x-----------------------------------------------+----------------x-----------------+
SAP Fiori for Web UI Kit (Figma) | [Popover](https://www.figma.com/community/file/1494295794601744471/sap-fiori-for-web-ui-kit) | :badge, info, large, _, Figma:

## When to Use

+-------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------+
When To Use
+-------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------+
Do
Use the popover to:
- Define a custom structure when the [quick view](https://www.sap.com/design-system/fiori-design-web/ui-elements/quickview/) component does not meet the requirements.
- Show UI elements that are not supported by the [quick view](https://www.sap.com/design-system/fiori-design-web/ui-elements/quickview/) component.
- Display lightweight, contextual content.
- Show details for a list item, contact information, or a short preview without leaving the current view.
- Let users stay in context while viewing or editing related information.
- Present content that is directly related to a specific UI element.
- Provide quick, non-disruptive actions without navigating away.
+-------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------+
Don't
Don’t use a popover to:
- Display content that is better suited for a [quick view](https://www.sap.com/design-system/fiori-design-web/ui-elements/quickview/) component.
- Display object details in a list-detail layout (these details belong in the dedicated details area).
- Display content that requires full user focus or involves complex interaction.
- Interrupt the user's flow by requiring explicit input or confirmation. Instead, use a [dialog.](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog/)
- Create modal behavior where the background is not interactive. Instead, use a [dialog.](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog/)
- Provide information that is not directly related to a specific UI element.
- Present content that takes up more than one-third of the phone screen. Use a responsive popover instead.
- Show large or scroll-heavy content.

+------------------------------------------------------------x------------------------------------------------------------+
Top Tips
+------------------------------------------------------------x------------------------------------------------------------+
- Include a header or footer when the popover needs a title or action. Leave them out if the content is clarified by
the context provided by the triggering element, is clear on its own, or doesn't require any action.
- Place the popover directly beside its trigger element, keeping the trigger visible so the relationship is obvious.
- Ensure the popover can be dismissed based on your scenario: by clicking outside of it, re-clicking its trigger, or by
selecting an action within it, and make sure user focus returns to the trigger element afterward.
- Use popovers for navigation flows when showing nested details.
- Consider using responsive popovers for larger screens where full-screen display and touch interactions are supported.

## Anatomy

1. **Header (optional):** Contains a title and a back button when navigation is available.
2. **Content area:** Can contain any component.
3. **Resize handle (optional):** The resize handle is visible when the popover is resizable.
4. **Footer (optional):** Contains one or more actions.
5. **Arrow (optional):** Visually connects the popover to its trigger element.

Anatomy of a popover

**> **Information:** **

You can define a fixed height for the popover. If the content exceeds that height, a scrollbar appears automatically.

## Types

### Popover with or without header and footer

The popover can include a header, a footer, or both. A header and footer are useful if you need to contextualize the information with a title or add any actions to the footer (A). In contrast, a popover without a header or footer is ideal for simple content that is already clarified by the surrounding context provided by the triggering element, is inherently clear, and doesn't require a title or additional actions (B).

Examples of popovers with a header and footer, and without either

### Popover with a custom header

A popover with a custom header is useful when the standard header doesn't meet specific application requirements. You can place any component inside a custom header, such as adding an alternative way to dismiss the popover using a *Close* button at the end of the header (A). Additionally, you can use a header that provides back navigation to a previous page. In this scenario, you might also include options for additional actions at the end of the header (B).

Examples of a popover with custom headers

### Popover with a subheader

The popover can include an additional subheader that may contain any component (A). It is also possible to use the popover without a main header, having only the subheader instead (B).

Popover with both a header and a subheader, and another with only a subheader

## States

The popover doesn’t have its own states. When the popover opens, focus moves to the first interactive element within it. Initial focus can be configured to land on a specific element.

### Focus State

The focus state determines which component receives the user input
when using an input device, for example, a keyboard.
A popover with both focused and unfocused buttons
**A. Focus state:** Appears with a visible outline around the
interactive element, for example, a button.
**B. Unfocused state:** Applies to all elements that are not focused.
For more information, see [Focus States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-focus-states).

## Behavior and Interaction

### Opening a popover

A popover opens when users click the element that triggers it, such as a link or button. The popover then positions itself next to the trigger element, ensuring the trigger element remains visible and accessible. This behavior is typically designed to maintain context for the user, allowing users to still see that element and click it again if needed.

Hovering over the trigger element displays the hover state before opening the popover (A). Clicking the trigger opens the popover (B).

Opening a popover when clicking a button

### Closing a popover

The popover can be dismissed as follows: by clicking outside its boundaries (A), by clicking the trigger element again (B), or by selecting an action within the popover (C). When the popover closes, focus returns to its trigger element.

Closing a popover by clicking outside of it, on the trigger element, or by clicking a “Cancel” button

### Navigation flow

The popover supports a navigation flow when additional details or nested content are needed for a selected item.

Clicking the trigger element (A) opens the popover as an overlay (B), displaying the content within while keeping the trigger visible.

Opening a popover and selecting an item

The selected item (B) reveals its detailed view (C) with a back arrow button in the header. The content area provides contextually relevant information. Clicking on the back arrow (C) returns to the full list view (D), allowing users to select a different item.

Clicking on the back arrow button, the popover displays the full list again

### Resizing a popover :badge, info, large, _, SAPUI5 only:

A popover can be resizable, depending on the implementation. When resizing is enabled, a handle, such as one in the bottom-right corner, appears, allowing the user to drag and adjust the popover’s dimensions.

Resizing a popover

## Responsiveness

The popover behaves differently on mobile phones than on tablet and desktop devices.

**Desktop and tablet devices:** Opens as a standard-sized popover.
**Mobile phones:** Opens as a full-screen dialog. This behavior applies to both portrait and landscape orientations.
**Touch devices:** Touch interactions work similarly to mouse interactions: [tap gestures](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/gestures#tap-press-and-release) open and close the popover, while [drag gestures](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/gestures#drag-tap-and-hold-move-and-release) resize it.

Responsive popover on a mobile phone

## Accessibility

SAP follows international standards, such as WCAG and WAI-ARIA, and strives to make our business solutions accessible and inclusive.

For more information, see [Accessibility in SAP Fiori](https://www.sap.com/design-system/fiori-design-web/discover/sap-design-system/product-standards/accessibility-in-sap-fiori) and the [Accessibility Design Tools Handbook](https://www.sap.com/documents/2023/11/bc210d8b-977e-0010-bca6-c68f7e60039b.html).

### Keyboard Navigation

The following keyboard combinations are supported by the SAPUI5 Popover component.

**Table (col-width-30-70)**

Key Combination

**Tab**
element, it moves to the first one, staying inside the popup.

**Shift \+ Tab**

**Escape**
By default, the focus goes to the **Cancel** button, if available.

### Screen Reader Support

For additional details on screen reader support and Accessible Rich Internet Applications (ARIA), see [UI5 Screen Reader Support](https://ui5.sap.com/#/topic/33fae3482358438e93daea5232527093) and [WAI-ARIA Authoring](https://www.w3.org/TR/wai-aria-1.2/).

## Content

### Localization

Popover supports both left-to-right (LTR) and right-to-left (RTL) reading directions. The layout automatically mirrors to match the language direction.

Left-to-right text directions

## Features

### Placement

A popover can appear without an arrow (A) or with an arrow (pointing left, right, top, or bottom) to visually connect to the trigger element (B).

Arrow placement options

### Resize handle positioning

The resize handle is always positioned on the opposite side of the arrow to maintain usability and prevent visual interference. When the arrow is centered on any side of the popover, the handle appears in the opposite corner. The exact placement (up/down or left/right) depends on the initial position of the arrow, ensuring optimal interaction space and clear visual separation between the arrow and the resize handle.

The arrow is positioned at the left (A) and top (B), with the resize handle appearing on the opposite side

### Modal behavior

Modal behavior determines whether clicking outside the popover closes it or leaves it open. If modal behavior is disabled, clicking anywhere outside the popover automatically closes it. If enabled, outside clicks are ignored, and the popover remains open. In this case, it can only be dismissed via an available action within the popover or by activating a trigger element, such as a button or link.

## Framework Comparison

Some behaviors differ between frameworks due to implementation specifics. The table below summarizes the differences between SAPUI5 and SAP Web Components and lists the framework-specific patterns.

**Table (col-width-50-20-30)**

Feature                                                                                                                                                           | SAPUI5    | SAP Web Components

A popover can be made resizable by displaying a handle in the bottom-right corner, allowing its dimensions to be adjusted dynamically. For more                   | Available | Not available
information, see [Resizing a popover](https://www.sap.com/design-system/fiori-design-web/ui-elements/popover/#resizing-a-popover-badge-info-large-_-sapui5-only). |

---

## popover-web-component

+------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------+
+--------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------+---------x----------+
## This page has been deprecated and is no longer available.
This page was deprecated with guideline version **1.142**.
#### Reason for deprecation
The guidelines for the SAP Web Component and the SAPUI5 component have been merged. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).
#### Looking for the latest information?
Visit the page below for the unified guideline with the most recent updates.
[Popover](https://www.sap.com/design-system/fiori-design-web/ui-elements/popover/)

---

## responsive-popover-web-component

+------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------+
+--------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------+---------x----------+
## This page has been deprecated and is no longer available.
This page was deprecated with guideline version **1.142**.
#### Reason for deprecation
The guidelines for the SAP Web Component and the SAPUI5 component have been merged. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).
#### Looking for the latest information?
Visit the page below for the unified guideline with the most recent updates.
[Popover](https://www.sap.com/design-system/fiori-design-web/ui-elements/popover/)

---

## shell-bar


## Intro

The shell bar is a universal header at the top of all screens. It offers both global functions (like search, notifications, and user profile) and elements that are specific to the product context.

*Shell bar*

## Anatomy

*Anatomy of the shell bar*

1. **Side navigation**: Allows users to open or close, as well as expand or collapse, the side navigation menu.
2. **Back**: Enables users to return to the previous page or state within the application.
3. **Branding element (mandatory)**: The branding element consists of two parts:
   a. **SAP logo**: Indicates that the product is part of the SAP product family.
   b. **Product identifier**: Unique name that helps the user understand the specific context within the SAP portfolio.
   When selecting the branding element, the user navigates to the product home page. The home page is the primary or initial page users encounter when accessing the product.
4. **Additional context area**: Contains specific elements applicable to the entire product. Elements can be positioned within two containers: one aligned to the left and the other to the right. You can prioritize these elements to ensure that higher-priority elements remain visible longer than lower-priority elements as the available space decreases.
5. **Search**: A search input field or button that expands the search bar, enabling users to search within the product or across multiple products. We recommend expanding the search field by default.

6. **Joule:** Launches SAP’s AI assistant, Joule.
7. **Notifications**: Displays [notifications](https://www.sap.com/design-system/fiori-design-web/ui-elements/notification-center/).
8. **Additional actions**: A section for further actions that are defined by the product.
9. **Help (mandatory):** Provides access to integrated help functionality.
10. **Profile (mandatory)**: Provides access to the [user menu](https://www.sap.com/design-system/fiori-design-web/ui-elements/user-menu/).

11. **Product switch**: Offers access to other products.

### Back Button

**Avoid using a** ***Back*** **button in the shell bar**; use the browser's *Back* button instead. Only use the shell bar *Back* button if you can’t rely on the browser *Back* button due to technical limitations.

Only show the shell bar *Back* button if back navigation within the product is possible. Hide the *Back* button if there is no back history (for example, upon initial launch or when deep linking).

### Additional Actions

Only add actions to the shell bar if users need to access them **frequently**. Don’t replicate shell bar actions in other areas of the product, such as the [user menu](https://www.sap.com/design-system/fiori-design-web/ui-elements/user-menu/) or side navigation.


## Responsiveness

The shell bar is fully responsive. When space is limited, it collapses or hides elements in the following order:

1. The **search field** collapses first to keep other content visible.
2. Next, **additional shell actions** move to an overflow menu. The user menu and product switch icon remain in place.
3. Then, **additional context elements** are hidden based on priority: the lowest-priority element hides first, and the highest-priority last. Elements in the additional context area don’t have automatic overflow behavior. However, when an additional context element is hidden, it’s possible to listen for these events and adjust how the component is represented – for example, by switching to a minified version.
4. The **product identifier** part of the branding element is hidden.
5. If there isn’t enough space to show both the highest-priority context element and the search icon, the **search** function also moves to the overflow menu.

### Example

The example below shows how elements are collapsed or hidden as the screen width is reduced:

- **Size XL**: All elements are visible, and the search field is expanded.
- **Size L**: The search field is collapsed, all other elements are still visible.
- **Size M**: The additional shell actions have moved to the overflow menu. In addition, 2 of 4 elements in the additional context area are now hidden (lowest-priority elements).
- **Size S**: The product identifier in the branding element is now hidden.
- Only the top-priority element in the context area remains.

*Shell bar – responsive behavior*

### Badge Overflow

#### One badge

If a **single action** with a badge moves into the overflow menu, the counter is also shown on the overflow button.

*Badge overflow – single action*

#### More than one badge

If multiple **actions** with a badge move into the overflow menu, only the attention indicator is shown on the overflow button.

Badge overflow – multiple actions

## Additional Context Examples

### Trial System

A trial system is a temporary setup that allows users to test and evaluate a product or service before making a commitment to purchase or implement it. It provides a hands-on experience, enabling users to explore features, assess performance, and determine if it meets their needs.

To indicate a trial system, use the [tag web component](https://sap.github.io/ui5-webcomponents/nightly/components/Tag/) with color scheme 7 from set 2. In addition, you can also show the remaining days.

Trial system

### Multiple Productive Systems

To differentiate between multiple productive systems for the same product, use the [tag web component](https://sap.github.io/ui5-webcomponents/nightly/components/Tag/). We recommend using color scheme 10 from set 2.

Multiple productive systems

### Non-Productive Systems

To differentiate between multiple non-productive systems for the same product (for non-admins), use the [tag web component](https://sap.github.io/ui5-webcomponents/nightly/components/Tag/). We recommend using color scheme 8 from set 2.

Non-productive systems

---

## smart-filter-bar-annotations

+------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------+
+-------------------------------------------------------------------------------x--------------------------------------------------------------------------------+---------x----------+
## This page has been deprecated and is no longer available.
This page was deprecated with guideline version **1.145**.
#### Reason for deprecation
The smart filter bar control is now maintained but no longer enhanced so no further versions of the guidelines will be published.
#### Looking for the latest information?
Visit the last version of the guidelines for [Smart Filter Bar.](https://www.sap.com/design-system/fiori-design-web/ui-elements/smart-filter-bar-annotations/)

---

## table-bar

The table toolbar always appears above the table. Use it for key actions that affect the entire table and for actions that apply to selected items.

*Table toolbar*

## When to Use

+--------------------------------------x--------------------------------------+
When To Use
+--------------------------------------x--------------------------------------+
Do
Use the table when you need to:
- Show a table title.
- Control table settings or views and adjust how much information is shown.
- Apply the same action to selected items.
- Switch between different tables.
+--------------------------------------x--------------------------------------+
Don't
Don’t use the table toolbar if:
- The table is used for selection only.
- You want to show all actions within each row.

**Top Tips**

- Include only the actions and content your users really need.
- Keep the predefined order for action groups.
- Don’t move main actions into the overflow.

## Anatomy

*Anatomy of the table toolbar*

1. **Title**: The table title.
2. **Search**: A search field or an action that opens the search field.
3. **Actions**: Actions that apply to the table or to selected rows. Related actions appear in one group.
4. **Separators:** Separators divide action groups. Each visible group begins with a separator, even if the group contains a single action. Only the first group after the search field must not show a separator.

## Responsiveness

To enable responsiveness, use the [overflow toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/toolbar-overview/) control. For more information, see [Toolbar Overview – Responsiveness](https://www.sap.com/design-system/fiori-design-web/ui-elements/toolbar-overview/#responsiveness).

## Features

### Title and additions

#### Title

A title gives a short, meaningful summary of the content, often in one word. Use the [title](https://www.sap.com/design-system/fiori-design-web/ui-elements/title/) component to display it.

Use a toolbar title if you need the table toolbar, and the title of the [table](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) is not displayed nearby. To prevent redundancy when another title already provides context, use a generic label for the table title, such as *Items*.

#### Item
You can add an item counter after the title. The counter shows the number of items displayed in the table in parentheses, for example, *(37)*. Remove the counter when no items are shown.

*Title with item counter in the table toolbar*

### Variant management

In tables, a variant stores all the settings that define the table view, such as the column layout, column visibility, sorting, filter settings, and grouping. The [variant management](https://www.sap.com/design-system/fiori-design-web/ui-elements/variant-management/) component enables users to load, save, and change variants. In most cases, variant management replaces the title.

*Variant management in the table toolbar*

*Title with variant management*

**> **Guideline:** **

If you need both a title and variant management, place the variant management component directly after the title.
Insert a separator between the title and variant management.
Using both often leads to truncation issues, so this pattern isn’t recommended.

### Content switch

To switch between different predefined views, use a [select](https://www.sap.com/design-system/fiori-design-web/ui-elements/select/) or a segmented button. The content switch replaces the title and the variant management component. In the rare case that the content switch is shown together with a title, the content switch follows the title.

A predefined view contains settings for sorting, filtering, grouping, column layout, and column visibility. Nevertheless, in most cases, the content switch is just used for different filter settings like *All*, *Mine*, and *Others*. In this case, make sure that the content switch doesn’t interfere with other filter settings. For example, remove the corresponding filter from the [filter bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/filter-bar/). If possible, include an item counter per view.

Another common pattern for content switches are views like *By X*, and *By Y,* which are usually defined using group settings.

Use the segmented button and the select control as follows:

- For a limited set of views (2-3), use the segmented button for desktop and tablet devices. Replace it with a select if there is not enough screen space.
- If the number of views can change or is larger than 3, use the select control.

For more information, see [multiple views](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/#content-area) for list reports.

*Segmented button with an item counter*

*Segmented text button to switch content*

*Select control to switch content*

### Search

The search field can be especially useful for tables with a large number of items. Avoid using the search if you have a filter bar or text filters per column. The search field can't be moved into the overflow menu.

For more information, see [Search](https://www.sap.com/design-system/fiori-design-web/ui-elements/search/).

**> **Guideline:** **

Use a search field only if there is no other way to search within the table (for example, if there is no additional
filter bar).

**> **Hint:** **

Although the search field isn’t a group, you can offer it as a group technically to add specific search components.

### Action groups and custom actions

To maintain continuity and consistency across table types, organize related actions into generic action groups so similar operations appear together. Surface only the actions users need. Follow the predefined group order.

When you create a table toolbar, identify the actions your table needs to offer and place them in the defined groups. Use the recommended slots to add application-specific actions within a group without disrupting overall stability and consistency. In metadata-driven components, the toolbar is predefined, and the slots act as insertion points where developers can add custom actions.

You won’t need every action shown in the examples. Use the subset that applies and order and group them accordingly.

Overview of table toolbar groups

**1. Finalizing actions**
**2. Business actions**
**3. Modification actions**
**4. Personalization**
**5. Share**
**6. Export**
**7. View actions**
**8. End slot**

**> **Guideline:** **

- Only disable an action if it can’t be applied to any of the selected items, or if the number of selected items
doesn’t match the action. For example, disable *Compare* if only one item is selected.
- If the items are still available after an action is applied, keep them selected.

Only use **finalizing actions**, such as *Save* or *Cancel*,
when the table is editable. Place them in the first position
in the table toolbar. Semantic actions behave like
finalizing actions, though you can also treat them as
business actions. Add custom actions between the primary
action and the negative action. The primary action doesn’t
have to be *Save*, as shown in this example.
**> **Guideline:** **

If there’s no other primary action on the page, you can use an emphasized button for the finalizing action. Otherwise, highlight the
most important button in the table toolbar with the ghost button style.
See also:
- [Button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/)
- [Action Placement](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement)

**Business actions**, such as *Edit* or *Delete*, are transactional actions that operate on the underlying business object, not just the table. These actions are
business-specific or modify items in the table. Add custom actions at the beginning or end of the group.
Business actions group
In most cases, pair *Delete* with *Create* and *Remove* with *Add*.
*Create*, *Delete*, *Add*, and *Remove* must never move into the overflow.
See also: [Object Handling (Create, Edit, Delete)](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/manage-objects).
There are several options for **editing a table**:
- Edit a single row:
Place an icon-only *Edit* button at the end of the row. When users click it, trigger the edit event and switch the row to edit mode.
- Mass editing:
Allows users to simultaneously change multiple objects that share the same editable properties.
More information: [Mass Editing](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/mass-editing)
- Edit the whole table:
To let users edit a whole table, use a text-only *Edit* button. When the user triggers the edit action, switch the table to edit mode. In edit mode, don't show the *Edit* button and add the finalizing actions *Save* and *Cancel* instead. Remove any actions that are meaningless in edit mode. Keep the view settings available.
*Table in display mode with 'Edit' as the most important action*

*Table in edit mode*

**Modification actions**, such as *Copy* or *Paste*, are
clipboard actions or actions that change the order or
content in the table. The up and down arrows are for
moving items, not for pagination, and are only available
on trees.  Add custom actions at the beginning or the end
of the group.
**Personalization** action&#x73;**,** such as *Sort* or *Filter*, change the arrangement and personalization of the table at the row level. The first set covers collapsing and expanding groups or rows. The rest are typical personalization actions, often shown as a single settings icon.
Add custom actions before the expand and collapse actions and before the settings actions.
Use the [table personalization dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-personalization-dialog/) or the [P13n Dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/p13n-dialog-popup/) for personalization actions.
For more information, see [Table Personalization](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/overview-table-personalization).
Depending on the responsive behavior, some data can appear in the pop-in area. Users can switch between a reduced data set and the full data set using the *Show Less per Row / Show More per Row* [segmented button](https://www.sap.com/design-system/fiori-design-web/ui-elements/segmented-button/).

For more information, see [Smart Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/smart-table/#show-details-hide-details).

*'Show More per Row' function to show all data in the pop-in area*

*'Show Less per Row' function to reduce data in the pop-in area*

**> **Guideline:** **

- Offer column settings when you need more columns than fit on a tablet screen (usually five) to cover about 80% of your main use cases. Before you add column settings, try reducing the number of columns, for example
by using multiple lines per column or the pop‑in feature.
- Don't provide sorting, filtering, and grouping actions if you expect the table to have only a small number of entries (up to 20 in most cases).
- If filtering in a list report is a main use case, don't offer filtering on the table toolbar. Use the [filter bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/filter-bar/) instead.
- When users reopen the app and [variant management](https://www.sap.com/design-system/fiori-design-web/ui-elements/variant-management/) isn't being used, show the table with the same column settings they last defined.

**Share** sends content to others. This can include
sending content to another application or adding a tile
to the home page.
Place the general *Share* action at the end of the group.
Add custom actions only before it.
**Export** converts table contents into an external
format, such as Microsoft Excel.
Export group
The common *Export* action must be placed at the end of
the group. Add custom actions only before it.
**View actions**, such as the full screen action and the view switch, change the presentation of the entire table. Place the full screen action and the view switch at the end of the group. Add custom actions only before them.
To let users show the table in full screen, display the *Maximize* button. Let users exit full screen with the *Minimize* button.
View switches allow the user to switch between different [chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/chart/) types and different controls for displaying items (for example [list](https://www.sap.com/design-system/fiori-design-web/ui-elements/list-overview/), [responsive table](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/), [grid list](https://www.sap.com/design-system/fiori-design-web/ui-elements/grid-list/)).
Use a [segmented button](https://www.sap.com/design-system/fiori-design-web/ui-elements/segmented-button/) with icons and sort the options in order of importance. The currently used view is highlighted.
**> **Guideline:** **

Full Screen
- Use the *Maximize* and *Minimize* buttons only when truly needed.
- We recommend offering them in [object pages](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/) that contain multiple grid tables in one tab.
- Don't use the *Maximize* and *Minimize* buttons:
- In [list reports](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/), [worklists](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/work-list/), [analytical list pages,](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/) and [initial pages](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/initial-page-floorplan/).
- For [responsive tables with a *More* button](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/#load-items).
- If the table is in a [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog/) or [popover](https://www.sap.com/design-system/fiori-design-web/ui-elements/popover/).
View Switch
- Provide the view switch when a [chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/chart/) relies on subtle color differences or gradients. That lets users with visual impairments switch to the [table](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) view.
- Define the number of chart types and switches with care. Offer only chart types that meaningfully visualize the data and help users. Ideally, provide no more than three visualization types.

The **End** slot offers space to add additional custom actions, such as pagination.

---

## user-menu


## Intro

The user menu provides access to user-specific settings and information. It is accessed by clicking on the user profile icon within the shell bar, represented by an avatar.

*User menu*

## Anatomy

The user menu popover comprises of the following SAP Web Components:
1. **Popover:** Holds all the content of the user menu.
The popover represents the user currently signed in and contains the following information:
2. **Avatar:** A visual element with the user's profile picture. If no profile picture is
available, the avatar displays the user's initials. Editing the avatar/profile picture is
optional.
3. **Title:** A UI element that displays the user's first and last name.
4. **Subtitle 1:** Shows the unique identifier of the signed-in user, such as an email address or username.
5. **Subtitle 2:** Can display additional details about the user, such as their job role or position.
6. **Additional Information:** An extra line intended to present supplementary details. This
information is not displayed within the Accounts panel.
7. **"Manage Account" button:** If the product's user profile is managed outside the product
itself as a central profile, this button navigates the user to the appropriate experience.
Don’t display this button if no central profile is available.
8. **"Manage Accounts" icon button:** Links to the experience where accounts can be managed.
9. **"Accounts" panel:** If the product supports multiple accounts, this panel lists other
accounts the user can sign into.
10. **User menu items:** Displays list items that provide access to standard options, such as *Settings*, *Legal Information*, or *About*. If necessary, you can also include product-specific options that are related to the user.
11. **Submenu:** If necessary, you can add a second-level menu.
12. **"Sign Out":** Procedure to exit the product in a secure manner.
## Interaction

### Scrolling

When scrolling, the title snaps into place at the top.

Scrolling – title snaps to the top

### Account Switch

Selecting another account under *Other Accounts* signs the user into the selected account and switches the view from the original account to the new one.

Switching to another account

## Responsiveness

The user menu opens in full screen on Size S for touch-enabled devices.

User menu responsiveness – Size S (touch)

---

