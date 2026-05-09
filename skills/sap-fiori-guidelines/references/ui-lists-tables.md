# SAP Fiori UI Elements: Lists Tables

This reference covers the following UI components:

- [Analytical Table Alv](#analytical-table-alv)
- [Grid List](#grid-list)
- [Grid Table](#grid-table)
- [Responsive Table](#responsive-table)
- [Upload Set With Table Plugin](#upload-set-with-table-plugin)

---

## analytical-table-alv

An analytical table\ contains a set of data that is structured in rows and columns. It provides several powerful possibilities for working with the data, including advanced grouping and aggregations.

In contrast to other tables, the analytical data binding used by the analytical table allows an aggregated number to be shown automatically in a cell. This means that a number in such a summarized cell is a total sum of several lines in the database.

## Usage

### Use the analytical table (ALV) if:
- The cell level and the spatial relationship between cells
are more important than the line item. Examples include
spreadsheet analyses and waterfall charts. Note that an
analytical table is not fully responsive. It is only
available for desktops and tablets, so you will need to
take an adaptive approach by offering an additional UI for
smartphones.
- You have to work on more than 1,000 rows. In this case,
the analytical table is easier to handle. In contrast to
the responsive table, the architecture of the analytical
table is optimized for handling large numbers of items.
Note that an analytical table is not fully responsive. It
is only available for desktops and tablets, so you will
need to take an adaptive approach by offering an additional
UI for smartphones.
- Comparing items is a major use case. In this case, an
analytical table might be more appropriate than a
responsive table. In the analytical table, each cell
contains only one data point. In contrast, the responsive
table is more flexible regarding line items, including the
ability to add more data points per cell and also the
pop-in function. Both make comparisons more difficult. Note
that an analytical table is not fully responsive. It is
only available for desktops and tablets, so you will need
to take an adaptive approach by offering an additional UI
for smartphones.
## Responsiveness

The analytical table is available for desktops and tablets, but not in smartphone sizes. It supports touch interaction devices, but is not optimized for small screens. If you use an analytical table, you need to take an [adaptive approach](https://www.sap.com/design-system/fiori-design-web/discover/sap-design-system/vision-and-mission/responsiveness-adaptiveness#adaptive-approach) by offering an additional UI for smartphones.

You could create a fallback by using a [responsive table](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/). However, a completely different solution, such as showing [charts](https://www.sap.com/design-system/fiori-design-web/ui-elements/chart/) in a read-only case, might be more suitable.

*Analytical table (ALV) shown on a desktop*

## Components

An analytical table does not consist of other elements. However, it is common to use a [toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/) above the analytical table.

The toolbar can contain entry points for the [view settings dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/view-settings-dialog/) and the [table personalization dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-personalization-dialog/) or for the [p13n dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/p13n-dialog-popup/), as well as for view switches in the form of a [segmented button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/), and [buttons](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/) for *Add*, *Edit*, and other actions.

## Behavior and Interaction

An analytical table is quite restricted in terms of its content, although it provides powerful features for working with the content.

### Table Level

#### Scroll
An analytical table allows horizontal and vertical
scrolling (sap.ui.table.AnalyticalTable, property:
navigationMode, value: Scrollbar).
You can add any number of line items to the analytical
table, which is known as “lazy loading”.
To prevent adverse side effects when scrolling
vertically, all line items must have the same height
(sap.ui.table.AnalyticalTable, property: rowHeight).
The analytical table is optimized to allow faster
scrolling within the first 1000 items.
#### Select

Selection for an analytical table depends on the chosen selection mode. The following options are available:

**No selection**: Items cannot be selected. (property:
selectionMode = None)
*Analytical table without item selection*

**Single selection**: One item in the analytical table
can be selected. A row selector column is shown.
(property: selectionMode = Single)

Default (col-1)

- **Multiple selection**: One or more items can be selected. The analytical table provides a column with checkboxes on the left-hand side.
Clicking a checkbox toggles the state of the corresponding row from deselected to selected and back. The **Shift** key can be used to select a range. For multiple selection, you can choose between two variants.
- Multi-toggle mode (property: selectionMode = MultiToggle)
- Multi-selection plug-in (sap.ui.table.plugins.MultiSelectionPlugin)
- These variants behave differently when the user selects more items than are currently loaded in the front end.
#### Multi-toggle
- In multi-toggle mode, you can offer a *Select All* checkbox to the left of the column header (property: enableSelectAll). Selecting this
checkbox selects or deselects all items that are currently loaded in the front end (keyboard: **Ctrl\+A**). All other items are not
selected/deselected. If the application data is stored in the back end, scrolling down further can reveal additional unselected items. The
same can happen with range selections if not all items in the selected range have been loaded to the front end.
#### Multi-selection plug-in
- If you use this plug-in instead of the multi-toggle selection mode, the behavior for range selection and *Select All* changes:
- By default, a dedicated *Deselect All* button replaces the *Select All* checkbox. There is no default UI element for selecting all items.
- You can set a limit for the number of items that can be selected (sap.ui.table.plugins.MultiSelectionPlugin, property: limit). This limit
has the following effect:
- The range that can be selected using the **Shift** key is limited to the specified number of items (default = 200). The table
automatically scrolls back to the last selected item and a message can appear (sap.ui.table.plugins.MultiSelectionPlugin, property:
enableNotification). Users can select more items by selecting additional ranges (the specified limit applies each time).
- If the selection limit is set to 0, a *Select All* checkbox is shown. There is also no limit on the number of items that can be
selected in a range. All selected items are loaded, which can lead to performance issues for large data sets. (Keyboard: **Ctrl\+A**)
- If selected items are not already available in the front end, they are loaded automatically by the plug-in and set as selected.

> **Information, Col-1:** When setting a limit for the number of items that can be selected, keep the following boundaries in mind:
- The performance of your service: How many items can be loaded at once in a reasonable time? Does this also apply if
an end-user shows all available columns?
- The “minimum limit”: Internally, the analytcial table loads blocks of items as the user scrolls down. Because this
block size (sap.ui.table.AnalyticalTable, property: threshold) is usually also based on the performance of the service,
it should be safe to assume that the minimum selection limit is twice this size. In this case, loading the data would
take as long as scrolling down and loading exactly one more block. Nevertheless, we recommend using larger limits if
your service allows.

Default (col-2)

*Analytical table with multiple selection*
*Using the multi-selection plug-in with a limit*

Section Metadata

style

##### Selection Behavior

An item can be selected in different ways, depending on the configuration of the analytical table (sap.ui.table.Table, property: selectionBehavior):

- *Row*: An item is selected by clicking the checkbox or the row. Use this option for multi-selection tables if clicking a row or a cell is not used for anything else.
- *RowSelector*: An item is selected only by clicking the checkbox in the selector cell. Use this option if clicking the row (or a cell inside the row) is used for something else, such as navigation.
- *RowOnly*: An item is selected only by clicking the row, and not using checkboxes in the selector cells. Use this for single-selection tables if clicking a row or a cell is not used for another purpose, such as navigation.

#### Compact, Cozy, and Condensed

Like all SAP Fiori controls, the analytical table is shown in compact mode on a desktop and in cozy mode on tablets.
*Analytical table in compact mode*
For desktop devices, you can fit even more rows onto the screen by using the condensed mode together with the compact mode. This renders less white space
for each item.
*Analytical table in condensed mode - More items on the same screen real estate*
Note that the condensed content density must always be set in addition to the compact mode. Do not use the condensed mode on its own. Do not mix condensed
with cozy. Doing so could lead to unpredictable or unwanted results, such as cozy-sized controls in condensed-sized containers, missing padding, and so
on.
Note that neither compact mode nor condensed mode support touch interaction. Even on a desktop with a touch screen, users will have difficulty selecting
rows or using controls inside the cells with their fingers.
For more information on cozy and compact modes, see [content density](https://www.sap.com/design-system/fiori-design-web/foundations/visual/cozy-compact).
### Column Header

The column header provides the label for the corresponding column and access to the column
header menu.
Columns are resized as follows:
*Opening the column header menu on touch devices*
- **Mouse interaction:** The user drags the separator line between two columns
(sap.ui.table.AnalyticalColumn, property: Resizable). Double-clicking the line optimizes
the column according to the length of the data currently visible and the label of the
column header (sap.ui.table.AnalyticalColumn, property: Autoresizable).
- **Touch interaction:** The user clicks the column header to reveal two buttons: one to
show the column header menu and one for resizing. The user drags the latter to resize the
column.
- **Keyboard interaction:** Users can increase the width of the focused column header with **Shift\+Right** and decrease it with **Shift\+Left**.
When the user resizes a column, the adaptation of the column width depends on how the
column widths are set:
- If column widths are set in pixel-based units (px, em, rem), the resized column is
adapted and subsequent columns are moved accordingly. The width of all other columns is not
affected.
If all the columns together do not use up the full width of the table control, empty
space is added. If all the columns together exceed the width of the table control, a
scrollbar appears.
- If all column widths are set as percentages or “auto”, resizing one column automatically
resizes one or more other columns. Resizing can also affect the position of the resized
column. This option utilizes the full width of the table and ensures that no white space is
added. A scrollbar appears only if all or most of the columns become to narrow. To avoid
the side effect of undersized columns, you can set a minimum width per column. However,
this minimum width is only taken into account if columns are resized automatically. End
users can still reduce the column width to below the defined minimum (sap.ui.table.Column,
properties: width, minWidth).
Users can rearrange columns by dragging the column header to another position
(sap.ui.table.AnalyticalTable, property: enableColumnReordering). Keyboard interaction: **Ctrl\+Left** and **Ctrl\+Right** move the focused column header one position in the corresponding direction.
#### Column Header Menu
*Column header menu*
For each column, a menu can contain the following menu
items (sap.ui.table.AnalyticalColumnMenu, property:
Visible):
- *Sort Ascending/Descending*
(sap.ui.table.AnalyticalColumn, property:
showSortMenuEntries)
- Free text filter (sap.ui.table.AnalyticalColumn,
property: showFilterMenuEntries)
- *Group*
- Totals
- *Freeze* from the first to the last specified column
(sap.ui.table.AnalyticalTable, property:
enableColumnFreeze)
For each column, the menu can be replaced by an
app-specific menu.
#### Sort
*Sort settings in column header menu*
The column header menu can provide two sort options
(sap.ui.table.AnalyticalColumn, properties: sortProperty,
showSortMenuEntry):
- *Sort Ascending*
- *Sort Descending*
The user selects one of these options to sort the
corresponding column accordingly
(sap.ui.table.AnalyticalColumn, properties: sorted,
sortOrder, sortProperty).
#### Filter
*Free text filter in column header menu*
The column header menu can provide a search field for entering free text (sap.ui.table.AnalyticalColumn, properties: filterProperty,
showFilterMenuEntries).
If the user enters a term in the input field and triggers the search by pressing ENTER when the focus is on the filter input field,
the analytical table is filtered by the corresponding column and value (sap.ui.table.AnalyticalTable, properties: filtered,
filterProperty, filterValue, filterOperator, sap.ui.table.AnalyticalColumn, property: filterType).
Note that the filter may return zero results, in which case, the table might be empty.
General recommendations for filtering:
- If filtering is a main use case, choose the [filter bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/filter-bar/) or any other filtering UI over the built-in free text filter.
- Only use the free text filter if filtering is a secondary use case and if the filter bar is too heavy.
#### Group
*Group setting in column header menu*
The column header menu can provide the option to group by
this column (sap.ui.table.AnalyticalColumn, property:
sortProperty).
One group collects all items with the same value within
the corresponding column.
If line items are grouped in a column, every group is
provided with a collapsible or expandable group header
(sap.ui.table.AnalyticalColumn, property: grouped). The
header text consists of the column name and the value for
the corresponding group (sap.ui.table.AnalyticalColumn,
property: groupHeaderFormatter). Several grouping levels
are possible.
The corresponding column can be hidden to avoid
duplicates (sap.ui.table.AnalyticalColumn, property:
showIfGrouped). Exercise caution when using this option
since hiding the column changes the table layout and may
lead to confusion.

#### Aggregation
The column header menu can provide the option to show or
hide aggregation totals for this column.
Intermediate aggregations are shown at group level for
the corresponding columns if the group contains more than
one line item (sap.ui.table.AnalyticalColumn, property:
summed).
The overall aggregation is shown in a row at the bottom
of the analytical table when the column contains values
for a single unit of measure.
When the column contains values for **more than one** unit of measure, a *Show Details*
link is displayed in a row at the bottom of the table, for example, when the column
contains multiple currencies.
The *Show Details* link opens a popover that lists the totals for each unit of measure.
#### Freeze Columns
*Freeze setting in column header menu*
The column header menu can provide the option to freeze columns
(sap.ui.table.AnalyticalTable, property: enableColumnFreeze). Selecting *Freeze* freezes all
columns up to the one in which the operation was triggered (sap.ui.table.AnalyticalTable,
property: fixedColumnCount).
When *Freeze* is triggered, the menu item changes to *Unfreeze* for the corresponding column.
### Line Item Level
*Line item*
A line item contains a set of cells and provides options
for selecting the item.
To prevent adverse side effects when scrolling
vertically, all line items must have the same height.
(sap.ui.table.**AnalyticalTable**, property: rowHeight)
#### Drag and Drop
*Drag and drop*
One or several items can be moved to other UI elements
using drag and drop operations
(sap.ui.table.AnalyticalTable, aggregation:
dragDropConfig). While being dragged, the items are shown
as ghost elements on the mouse cursor.
Drop targets can be on items, between items, or both
(sap.ui.core.dnd.DropPosition). On a drop target, the
mouse cursor changes to either a “copy”, “link”, “move”,
or “none” cursor. “None” indicates that the dragged item
cannot be dropped in the current position
(sap.ui.core.dnd.DropEffect).
Drag and drop is only available on supporting browsers.
### Cell Level
*Cell*
A cell provides one data point.
It can contain one of the following controls to display this data point:
- [Text](https://www.sap.com/design-system/fiori-design-web/ui-elements/text/)
- [Label](https://www.sap.com/design-system/fiori-design-web/ui-elements/label/)
- Object status
- [Icon](https://www.sap.com/design-system/fiori-design-web/foundations/visual/iconography/icons)
- [Button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/)
- [Input](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/)
- [Date picker](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-picker/)
- [Select](https://www.sap.com/design-system/fiori-design-web/ui-elements/select/)
- [Combo box](https://www.sap.com/design-system/fiori-design-web/ui-elements/combo-box/)
- The following micro charts in size XS: [Bullet](https://www.sap.com/design-system/fiori-design-web/ui-elements/bullet-micro-chart/), [comparison](https://www.sap.com/design-system/fiori-design-web/ui-elements/comparison-micro-chart/), [stacked bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/stacked-bar-micro-chart/)
- [Multi-combo box](https://www.sap.com/design-system/fiori-design-web/ui-elements/multi-combobox/)
- [Multi-input field](https://www.sap.com/design-system/fiori-design-web/ui-elements/multiinput/)
- [Checkbox](https://www.sap.com/design-system/fiori-design-web/ui-elements/checkbox/)
- [Link](https://www.sap.com/design-system/fiori-design-web/ui-elements/link/)
- [Currency](https://www.sap.com/design-system/fiori-design-web/ui-elements/currency/)
- [Rating indicator](https://www.sap.com/design-system/fiori-design-web/ui-elements/rating-indicator/)
- [Progress indicator](https://www.sap.com/design-system/fiori-design-web/ui-elements/progress-indicator/)
While it is technically possible to also use other controls, doing so could lead to issues with alignment, condensed mode, screen reader support, and keyboard support.
If you use text, use only single-line text to keep the same row height. Truncate if necessary as this prevents adverse side effects when scrolling vertically (sap.m.Text, property: wrapping, value: false). Do not wrap.
#### Context Menu
*Analytical table with context menu*
You can attach a context menu (sap.m.Menu) to a table. The context menu gives users an alternative way to
modify the focused elements by giving them access to context-specific functions.
When opened, the context menu gets the row and column context, except for special columns (such as the
selection column) or special rows (like group headers). Context menus can be implemented for a specific table,
row, or cell (not recommended for editable cells).
By default, the analytical table provides a context menu on the group headers (for example, *Expand*, *Collapse*, …). Otherwise, no default context menus are provided.
Context menus are opened by right-clicking (desktop), long press (mobile), the **context menu key**, or **Shift\+F10**.
Be aware that using the context menu overrides the browser context menu, which can no longer be opened.
If a control inside a table is the “click target”, and the control also provides a context menu, the control
context menu “wins”.
## Guidelines

### Data Density vs. Complexity

The analytical table can be used to display and work with large amounts of data. Unfortunately, the analytical table has a high data density and therefore conveys an immediate feeling of complexity.

Only show tables with a lot of data as a last resort. To make the data easier to read, you should instead try the following:

- Break down the data into manageable chunks and allow the user to navigate or drill down between them.
- Use charts with drilldown functionality until the amount of data is more manageable.

Try to avoid horizontal scrolling in the default delivery.

Try to minimize the number of columns, especially if there is a large number of rows.

### Table Title

Implement the table title by using a [title](https://www.sap.com/design-system/fiori-design-web/ui-elements/title/) control in a [toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/).

Use a table title only if the title of the table is not indicated in the surrounding area.

Do not use a table title if it simply repeats text that is already above the table. For example:

- A pricing conditions table is the only control on a tab labeled *Pricing Conditions*.
- A section or subsection on an object page contains only one table.

Use a table title if you need the item count, [table toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/), or [variant management](https://www.sap.com/design-system/fiori-design-web/ui-elements/variant-management/). To avoid repeating text, feel free to use generic text as a table title, such as *Items*.
Exception: If the surrounding area contains the table title, and both the item count and toolbar can be added to the surrounding area, no additional table title is needed.
Example: An object page (sub-)section contains only one table. In this case, add the item count and the table toolbar to the (sub-)section header.

If you use a table title, show either a title for the table, with or without [variant management](https://www.sap.com/design-system/fiori-design-web/ui-elements/variant-management/), or an item count in the following format:

*Items (2,534)*.

The item count in the table title includes all the visible items that a user can reach by scrolling or expanding groups. Group headers are not included.

Remove the item count in the table title if there are zero items.

> **Hint:** Assistive technologies (such as screen readers) use the title to create a hierarchical site map for faster
navigation. In addition, screen readers use the title as the label for the table.
If you don’t use a title (for example, to avoid repetition), make sure that the table is connected to another
meaningful on-screen text that can be used as a label for assistive technologies. You can do this using the method
addAriaLabelledBy.

### Selection

#### Single Selection
For single-selection list-detail scenarios within the [flexible column layout](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout/), do not show an additional “navigated” indicator.
#### Multiple Selection
- We strongly recommend using the multi-selection plug-in. This ensures that all items selected using *Select All* or as part of a range are included – even if some items were not initially loaded in the front end. This is not the case if you use the multi-toggle option.
- Do not limit the range selection for the multi-selection plug-in unless you have to.
- If the dataset is small and/or completely available in the front-end, set the limit property to 0 to enable the *Select All* option and allow users to select any range.
- If you have a large dataset, set a limit on the number of selected items to avoid performance issues. Also bear in mind that some actions won’t be helpful if the dataset is too big (for example, a delete operation on 2
million database entries).
- When setting a limit, also display the corresponding message when the user selects more items at once than the limit allows (sap.ui.table.plugins.MultiSelectionPlugin, property: enableNotification).
- In multiple selection mode (multi toggle), do not show
checkboxes in the first data column in the default
delivery to avoid confusion.
*Do not add checkboxes to the first column*

- Never disable the selection checkbox. If an action can’t be performed on a specific item, inform the user after the corresponding action has been triggered. For more information, see [Enabling/Disabling Actions](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/processing-multiple-items#enablingdisabling-actions).
### Loading Data

To indicate that the table is currently loading items, use the [busy state](https://www.sap.com/design-system/fiori-design-web/ui-elements/busy-state/) (sap.ui.table.AnalyticalTable, property: busy). Do not show any items or text. As soon as the data is loaded, remove the busy state and show all items.

Default (col-1)

### Errors and Warnings

Default (col-1)

To indicate that the table contains items with errors or warnings, show a [message strip](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-strip/) above the table. On the [message strip](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-strip/), provide information about errors or warnings. When issues are solved or when new issues appear, update the [message strip](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-strip/) accordingly.
To indicate an error in a single row, see [Item States](https://www.sap.com/design-system/fiori-design-web/ui-elements/analytical-table-alv/#item-states) below.
For details on displaying errors, warnings, and other messages, see [Message Handling](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/messaging).

> **Hint, Col-1:** The sap.m.plugins.DataStateIndicator displays a message strip above the table, which shows binding-related messages.

Default (col-2)

*Table containing errors and warnings*

Section Metadata

style

### Columns – Best Practices

Minimize the number of columns. Avoid the need to scroll horizontally in the default delivery.

By default, the analytical table assigns the same width to each column. We recommend overwriting this default to provide optimal space for your content (sap.ui.table.AnalyticalColumn, property: width).

If you define the column width in pixels or rems, resizing a column affects only the width of this specific column. Reducing the size of the browser window results in a scrollbar. If the user resizes a column, and the total width of all columns exceeds the table width, a scrollbar appears. If the columns do not take up the full table width, white space appears to the right of the last column.

If you define the column width as a percentage, resizing one column affects the width of several or all columns. Reducing the size of the browser window truncates the texts. This ensures that the columns fill up all the available space. A scrollbar appears only if width of all the columns still exceeds the table width after the automatic width adjustments. To avoid the side effect of undersized columns, you can set a minimum width per column. However, this this minimum width is only taken into account if columns are automatically resized. End users can still reduce the column width to below the defined minimum (sap.ui.table.Column, properties: width, minWidth).

If you set the column width to “auto”, the behavior is the same as for “percentage”. However, unlike “percentage”, “auto” distributes the columns equally.

To decide on how to set the column width (pixel/rem/em vs. percent/auto), keep the following in mind:

- For tables with only 2 to 3 columns, use pixel-based units. This ensures that the values in the columns are not spread over the whole screen on wide screens, which improves the readability of the line items.
- For tables with many columns, where a horizontal scrollbar is usually needed, use pixel based units. This avoids unintended side effects when resizing columns.
- For all other tables, use whatever fits your case better.

Be cautious when mixing columns with pixel-based and percentage-based widths. While this can be helpful in some cases, it can also cause even more side effects when resizing a column. If you are using percentage-based widths for one or more columns, consider not allowing end users to resize columns at all.

Optimize the column width for its     | Don't                                                                           | Don't
initial visible content, including    |
the column header texts. If this is   | \ | 
not possible (for example, if showing | *Don't truncate the initial visible content In the default delivery*            | *Never wrap texts*
the full texts would result in        |
extremely wide columns), let the      |
texts truncate. End users can change  |
the width of the column to read the   |
full text, as needed.                 |
Maintain a constant column width and  |
avoid adjusting it automatically when |
the content changes.                  |
Always keep to one line of text. Do   |
not wrap.                             |
### Column Headers – Best Practices

For each column, provide a label in the column header. In the default delivery, do not truncate the column header texts. Only let the text truncate if showing the full text would make the column too wide. Never wrap the text.

### Content Alignment

For alignment of cell content, follow the guidelines below.

Left-align: text, IDs, phone numbers, URLs, passwords,
and email addresses.

Right-align: numbers, except IDs, to ensure comparability
of numbers and amounts.

Right-align amounts with currencies to the cell and align
their respective decimal points.
This ensures that amounts with different currencies are
shown correctly, regardless of whether the currencies
have 0, 2, or 3 decimals.
For aligning to the decimal point, use the
sap.ui.uinified.Currency control.
Right-align dates and times.
This ensures comparability for most formats and locales.

Left-align status information.
*Left-align status information*

Center-align icons.

Left-align micro charts.
*XS micro charts in condensed mode*

### Content Formatting

#### Key Identifier

Use a bold label or an emphasized link as the key
identifier of an item. In the default delivery, show the
key identifier in the first column.

For strings with IDs, show the ID together with the
corresponding description in one column whenever
possible. Description fields are hidden by default, so
the dialog remains clear, and key users can switch among
ID only, description only, or a combined display at any
time. Use a text arrangement if the metadata supports it,
ensuring consistent sorting, filtering, and grouping.
Only use separate ID and description columns if no text
arrangement can be provided, because users cannot combine
them later.
*If displayed as a link, use only the string as the link, not the ID*
*If displayed as a link, use the whole text as the link*

#### Truncation
*Optimize column width for typical content, not all content*
Avoid truncation of typical content in the default
delivery (sap.ui.table.AnalyticalColumn, property:
width). However, since the columns are resizable, do not
worry too much if truncation occurs as columns can still
be enlarged if necessary.
To prevent adverse side effects when scrolling
vertically, all line items must also have the same
height. If you need to decide between truncation and
different row heights, choose truncation. Do not wrap.
#### Number of Links
*Emphasized links, links, subtle links, and text*
Are there too many links? Use subtle links to avoid a
wall of links. Standard links are also emphasized more if
they are surrounded by subtle links.
For example, a financial table consists of several
columns with summarized cells. A summarized cell shows
the total sum of several database entries. Each sum
should be a link to a report that shows details about
which database entries produce the total sum. The line
item identifier should also be a link that provides more
detail about the line item itself. Use a standard or
emphasized link for the item identifier, and subtle links
for the summarized cells.
#### Missing Value
*Leave empty fields blank*
If there is no value for a cell, leave it blank. Do not
display text as *N/A*.
#### Numbering Items
*Add a separate column for the item number*
In terms of numbering items:
- If the item number is more like an ID with regard to
its description, use ID formatting as described above.
- In all other cases, use a separate column for the item
number.
#### Status
*Semantic colors on text*
For status information, use semantic colors on the foreground elements.
For status information on text, use an [object status](https://www.sap.com/design-system/fiori-design-web/ui-elements/object-display-elements/).
#### Micro Charts
*Micro charts in an analytical table*
Use only the following micro charts: [Bullet](https://www.sap.com/design-system/fiori-design-web/ui-elements/bullet-micro-chart/), [comparison](https://www.sap.com/design-system/fiori-design-web/ui-elements/comparison-micro-chart/), [stacked bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/stacked-bar-micro-chart/). When using micro charts, use them in size XS.
#### Empty Tables
*Provide meaningful instructions*
Avoid empty analytical tables. If necessary, provide instructions on how to fill the analytical table with data (sap.ui.table.AnalyticalTable, properties: noDataText, showNoData).
Examples:
- If a table is initially empty, provide at least a basic text:
*No items available.*
Overwrite this whenever a hint can be provided on how to fill the table with data.
- If a table is used together with a [filter bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/filter-bar/) (as in the [list report](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/)), and is initially empty, use the following text:
*To start, set the relevant filters.*
- If a table is used together with a filter bar and the filter does not return results, use the following text:
*No data found. Try adjusting the filter settings.*
Adapt the texts above if:
- The standard text is not precise enough for your use case (for example, a search is also offered, or only the search is offered).
- The standard text is misleading (for example, if the data is filled based on a list-detail pattern instead of filter settings).
#### Invalid State
*Analytical table with invalid data*
To show an invalid state of the analytical table within the [list report floorplan](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/),
show an overlay on the analytical table and the corresponding toolbar (sap.ui.table.AnalyticalTable, property: showOverlay). The overlay
prevents user interactions.
Use this within the list report floorplan if filter settings have been changed but the analytical table has not yet been updated.
### Item States

To show that an item has been modified, for example, within the global edit flow, add the string *(Modified)* in an additional column with the label *Editing Status*.
*A modified item*
In the default delivery, add a column directly behind the key identifier.
To show that a modified item contains an error, for example, within the global edit flow, add
the string *Contains errors* in the *Editing Status* column and highlight the row accordingly. This string replaces the *Modified*
string. A row with errors should be highlighted in all use cases – for example when the field
is visible in the row in edit mode.
To show that an item is locked, add a transparent-style button with the corresponding icon and the text *Locked by [name]* in the *Editing Status* column.
*A locked item*

To show that an item is in [draft](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/draft-handling) state, add a transparent-style button with the text *Draft* in the *Editing Status* column.
*Item in draft state*

Show only one state at a time.

### Numbers and Units

Show the unit of measurement in one of the following ways:

The number and unit are in the same cell. Do this if
sorting, filtering, or grouping by the unit of
measurement are not needed.
For amounts, use a currency control to display the
concatenated string.
The number and unit are in separate columns. Do this if
sorting, filtering, or grouping by the unit of
measurement are a common use case.
Note that this column can be hidden or moved
independently of the column containing the corresponding
number. Therefore, be sure to have clear labels for both
columns to communicate the dependency.
If the unit of measurement is the same for all rows, show
the unit of measurement in the column header. Otherwise,
show the unit of measurement within the row.
### Drag and Drop

Drag and drop is “invisible” on the UI: users can’t see where dragging is available and where it isn’t. In addition, there is no generic keyboard interaction. Drag and drop is also
not available on all browsers. For these reasons, provide it only in addition to existing (and visible) UI elements that fulfill the same purpose. For example, offer ([toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/)) [buttons](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/) for moving or for copying and pasting items. These are keyboard operable and available on all browsers.

Do not use drag and drop for rearranging items in the
analytical table. The analytical table is mainly used for
grouping items and for calculating the totals per group
and column. Moving items to another group also means that
a value of the dropped item changes: because grouping is
based on values in a column, the dropped item needs to
take on the value of the target group for the
corresponding column.
Example:
A table is grouped by availability. An item is moved from
the group “Not Available” to the group “In Stock”. In
this case, the moved item needs to change its
availability to “In Stock” to match the target group.
Because changing the value in this way doesn’t make
sense, rearranging items is not permitted in analytical
tables.
### Context Menu

Use the context menu only to give users a quick way of accessing functions that are already available elsewhere (for example, as buttons in the toolbar). Don’t just offer actions in the context menu itself, as users might not realize that these actions are available at all.

The context menu can be triggered for the table, row, or cell. However, we do not recommend using context menus for cells: because the content of a cell is a different touch target than the cell itself, opening a cell context menu via touch is quite hard, even in cozy mode.

Do not combine context menus with condensed mode: editable controls fill the entire space inside a cell. Because of this, context menus cannot be opened at all with touch or mouse interaction.

### Actions

For guidelines on how to use actions, see the corresponding guidelines for the grid table:

[Grid Table – Actions](https://www.sap.com/design-system/fiori-design-web/ui-elements/grid-table/#actions)

Technically, the analytical table is based on the grid table and shares many of the rendering behaviors.

### Editable Content

Default (col-1)

For editable content, only use the following controls, and only one control per cell:
- [Button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/)
- [Input](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/)
- [Date picker](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-picker/),
- [Select](https://www.sap.com/design-system/fiori-design-web/ui-elements/select/)
- [Combo box](https://www.sap.com/design-system/fiori-design-web/ui-elements/combo-box/)
- [Multi-combo box](https://www.sap.com/design-system/fiori-design-web/ui-elements/multi-combobox/)
- [Multi-input field](https://www.sap.com/design-system/fiori-design-web/ui-elements/multiinput/)
- [Checkbox](https://www.sap.com/design-system/fiori-design-web/ui-elements/checkbox/)
- [Rating indicator](https://www.sap.com/design-system/fiori-design-web/ui-elements/rating-indicator/)
Only these controls are optimized for all viewing modes of the analytical table.
If you need edit mode, change your text controls, such as label, text, link, object status, icons, and currencies, to editable controls as soon as you switch to edit mode, but not before. You can do this by exchanging the
controls, for example, from sap.m.Text to sap.m.Input.
For mass editing items:
- Provide multiselection.
- Provide an *Edit* button.
- If several items are selected, clicking the *Edit* button opens a [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog/) in which the user edits the corresponding fields for all selected items.
This is similar to mass editing in the split-screen layout floorplan.

> **Warning, Col-1:** Do not offer editing for summarized cells. A summarized cell shows the total sum of several database entries.
Changing the total sum does not make sense since it is unclear how this sum is divided between the different database
entries.

Default (col-2)

*Interactive controls – Inline*

Section Metadata

style

### View Settings

There are several ways to show *Sort*, *Filter*, and/or *Group* settings:
*Column header menu with view settings*
- Column header menu: In all cases, show the corresponding settings in the column header menu.
- [View settings dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/view-settings-dialog/): Simple and more
flexible with regard to filter settings. No advantage for sorting. Allows the user to ungroup grouped columns.tables with a
medium amount of items.
- [Table personalization dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-personalization-dialog/):
Provides complex options for sorting items by several levels and allows the user to ungroup grouped columns. It also provides a
query-builder-like approach for filter settings. The complexity of the options is also its downside. Use the table
personalization dialog for tables with a large number of items.
- If filtering is a main use case, use the filter bar. In this case, avoid offering additional filter settings on the table. If
you do, the filter settings on the table work only on the result set provided by the filter bar.
Always be careful when synchronizing the settings in the dialog with the settings from the column header menu.
Trigger the dialogs in one of the following ways:
- **View settings dialog**: Provide several buttons, one for each of these view settings. Each button opens the view settings
dialog on the corresponding page.
- **Table personalization dialog**: Provide a settings button, which opens the table personalization dialog containing all pages.
Use only the view settings you really need. For example, do not offer grouping if it does not support your use case.
Persist the view settings. When a user reopens the app,
show the analytical table with the same sort, filter,
group, and aggregation settings as last defined by this
user.
#### Sort

Always sort the table in a meaningful way when it first
loads. In most cases, this means sorting by the column
that identifies the row. This is usually the first column
in the default delivery.
*Column, sorted descending*
To display the current sort state, an icon is shown in
the column header of the last sorted column. This icon
indicates the sort direction
(sap.ui.table.AnalyticalColumn, properties: sorted,
sortOrder, sortProperty).
For the default sort setting, sort by the column that
identifies the row, which is usually the first column in
default delivery. Use a meaningful sort order, such as
alphabetical order for text, numeric order for numbers,
or chronological order for dates.
The descending sort order         | \ | 
must always be the exact          | *Object status sorted ascending, with neutral status last*            | *Object status sorted descending, with neutral status first*
reverse of the ascending sort     |                                                                       |
order.                            |                                                                       |
For each column, provide a        |                                                                       |
meaningful sort order. For        |                                                                       |
example:                          |                                                                       |
- Sort text alphabetically        |                                                                       |
- Sort numbers by their value     |                                                                       |
- Sort status information by      |                                                                       |
the severity of the status:     |                                                                       |
- Ascending: Sort status        |                                                                       |
information from positive to  |                                                                       |
negative, with neutral last.  |                                                                       |
- Descending: Sort status       |                                                                       |
information from negative to  |                                                                       |
positive, with neutral first. |                                                                       |
- - Ascending with different        | \ | 
values per severity level: Sort | *Object status sorted ascending and alphabetically, from positive to negative with neutral last*            | *Object status sorted descending and alphabetically, from negative to positive with neutral first*
status information from         |                                                                                                             |
positive to negative, with      |                                                                                                             |
neutral last. Sort different    |                                                                                                             |
values within a severity level  |                                                                                                             |
(semantic color)                |                                                                                                             |
alphabetically.                 |                                                                                                             |
- Descending with different       |                                                                                                             |
values per severity level: Sort |                                                                                                             |
status information from         |                                                                                                             |
negative to positive, with      |                                                                                                             |
neutral first. Sort different   |                                                                                                             |
values within a severity level  |                                                                                                             |
(semantic color)                |                                                                                                             |
alphabetically.                 |                                                                                                             |
#### Filter

To display the current filter state, an icon is shown in
the column header of the filtered column
(sap.ui.table.AnalyticalColumn, properties: filtered,
filterProperty, filterValue, filterOperator,
defaultFilterOperator, filterType).
#### Group

To display the current group state, group headers are
shown. Show the following text in the group header
(sap.ui.table.AnalyticalColumn, properties: grouped,
showIfGrouped, groupHeaderFormatter):
*[Label of the grouped column]: [Grouping value]*
If there is no grouping value, show the following text:
*[Label of the grouped column]: (Not Available)*
This is the case if you have a group of items that don’t
have a value for the grouped column.
Set the property collapseRecursive to “false” to keep
subgroups expanded even after collapsing and expanding
the parent group.
On non-touch devices, right-clicking a group header opens
the group header menu. On touch devices, the same menu is
opened by using the menu icon on the right side of a group
header.
*Group header on touch devices*
The group header menu provides several options:
- *Show/Hide*: Shows or hides the column in the table
layout, although it is grouped.
- *Ungroup*: When the user ungroups a column, the
corresponding group headers disappear. If the column was
hidden, it is shown again as a separate column.
- *Ungroup All*: The columns are shown again.
- *Move Up*: Rearranges the grouping levels hierarchy by
moving the selected group above the group that is one
level higher up in the hierarchy.
- *Move Down*: Rearranges the grouping levels hierarchy by
moving the selected group below the group that is one
level lower down in the hierarchy.
- *Collapse Level*: Collapses all groups on the
corresponding grouping level.
- *Collapse All*: All groups are collapsed.
In general:

- Offer grouping for objects and attributes that are shared by multiple elements in the table.
- Avoid grouping for measures or element properties that often occur only once in a data set and would lead to groups of one.
- Don’t use grouping to display hierarchical data structures. Groups define properties to cluster existing entries but are not an entry on their own. To present hierarchical data, use the [tree table](https://www.sap.com/design-system/fiori-design-web/ui-elements/tree-table/).
- If appropriate, offer reasonable grouping by default, but do not exaggerate. As a rule of thumb, use up to three group levels.
- Provide more space for the first column. Grouping needs an indent per group level. Extra space in the first column prevents truncated text.

#### Aggregate

Default (col-1)

To display the current aggregation state, the total sum of the corresponding column is shown at the bottom of the
table.
If items are grouped, an intermediate sum is shown:
- At the bottom of each group if the group is expanded.
- In the group header if the group is collapsed.
(sap.ui.table.AnalyticalColumn, property: summed)
When aggregating amounts with different units of measurement, show an asterisk (\*) in the aggregation rows.

Default (col-1)

When sorting an aggregated column, only the leaf nodes of a group are included by default. If each measure column currently displays a single unit of measurement, the order of the groups can also be
affected.
For example:
Let’s assume that table items are grouped by *Country/Region* and aggregated by *Total Net Amount.* If you sort the *Total Net Amount* column in descending order, the largest total net amount is shown first.

> **Warning, Col-1:** Only enable sorting by totals if each column has a single unit of measurement. This prevents inconsistencies in the
sorting behavior, which depends on user settings, such as filter settings or the columns currently displayed.

> **Hint, Col-1:** To allow sorting by totals, the following conditions must be met:
1. For each measure column, multiple units must not occur in the displayed data, regardless of whether or not totals
are shown.
2. The autoExpandMode of the AnalyticalBinding must be set to Sequential. Note that the default is Bundled.

Default (col-1)

In general:
- Offer aggregation on measures, but not on objects or attributes.
- Avoid aggregations on the first three columns for the default delivery. As soon as grouping is used together with
aggregations, collapsing a group shows the aggregation on the group header. This conflicts with the group name.
- Where appropriate, offer reasonable aggregation by default.

Default (col-2)

*Aggregation and groups*

Section Metadata

style

### Personalization

Only offer personalization if you need more columns than a tablet screen can display at any one time, which is usually five.

Persist the column layout. When a user reopens the app, show the analytical table with the same column layout settings as last defined by this user.

#### Add, Remove, and Rearrange Columns

To add, remove, or rearrange columns, use one of the following:

- The [table personalization dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-personalization-dialog/): It offers some simple settings for column layout. Use this if you have only a few columns to choose from and/or you use the [view settings dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/view-settings-dialog/).
- The [p13n dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/p13n-dialog-popup/): Besides various complex view settings, it also provides settings for column layout. Use this if you have a large number of columns to choose from and/or you use this dialog anyway for view settings.

In both cases, trigger the dialog via the settings button in the [table toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/). As short cut, use **CTRL+COMMA**.

You can also use drag and drop to rearrange columns (sap.ui.table.Table, property: enableColumnReordering). If you allow rearranging via drag and drop as well as via a dialog, keep both places in sync.

#### Resize Columns

Resizing columns works differently on touch and non-touch devices.

- Non-touch devices: Drag and drop the column separator on the right side of the column. Double-clicking the column separator optimizes the width of the column for the data currently loaded into the front end, which is usually about 100 rows.
- Touch devices: Clicking the column header reveals two buttons: one for opening the column header menu, another one for resizing the column. Drag and drop this second button to resize the column.

#### Freeze Columns
*Frozen column*
For freezing columns, offer the setting in the column header
menu (sap.ui.table.AnalyticalTable, property:
enableColumnFreeze).
Selecting *Freeze* on a column freezes all columns from the
first one to the one where *Freeze* is selected. On this column, the menu entry changes from *Freeze* to *Unfreeze*.
#### Highlight Items
*Highlighted items*
To show that an item needs attention, you can display a highlight indicator in front of the item. The highlight indicator can be used to indicate:
- A semantic state, such as red or orange for an error or warning. In this case, use [semantic colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/colors#semantic-colors).
- Additional information, such as blue to highlight newly added items. In this case, use [semantic colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/colors#semantic-colors).
- Industry-specific or process-specific states, such as “out of stock” or “excess of inventory”. In this case, use [indication colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/colors#indication-colors).
Be aware that the highlight is just an indication. It does not tell users exactly what is wrong. Make sure that you provide this information within the table row, ideally in the same color.
For details on the use of highlight colors, see [How To Use Semantic Colors / Industry-Specific Colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/how-to-use-semantic-colors).
(sap.ui.table.AnalyticalTable, aggregation: rowSettingsTemplate)
### Tables in Object Pages

In the [object page](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/), you can use a [responsive table](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/#tables-in-object-pages) or [grid](https://www.sap.com/design-system/fiori-design-web/ui-elements/grid-table/) table and offer navigation to a list report with the previously mentioned tables. We advise using analytical and [tree tables](https://www.sap.com/design-system/fiori-design-web/ui-elements/tree-table/) in tab mode.

For more information on the use of tables within the object page, see the [Tables](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#tables) section of the *Object Page* article.

### Export to Spreadsheet

On the [table toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/), apps can provide a [menu button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/#menu-button1) for exporting table data to a spreadsheet. For the export, use the [export to spreadsheet](https://www.sap.com/design-system/fiori-design-web/ui-elements/export-to-spreadsheet/) function.
*'Export to Spreadsheet' menu button*

## Properties

sap.ui.table.AnalyticalTable

The following additional properties are available for the analytical table:

- The property: width defines the width of the analytical table.
- The property: rowHeight defines the height of each row in the analytical table. Since the height required is calculated automatically by the analytical table, this property is only needed rarely.
- The property: columnHeaderHeight defines the height of the column headers. Since the height required is calculated automatically by the analytical table, this property is only needed rarely.
- The property: columnHeaderVisible can be used to hide the column headers. Always show the column headers.
- The property: showColumnVisibilityMenu provides an additional entry in the column header menu that allows columns to be shown or hidden. In SAP Fiori, columns are shown and hidden via the table personalization dialog or via the table personalization dialog. Do not use this property.
- The property: columnVisibilityMenuSorter is used for sorting the columns inside the column header menu if showing and hiding columns is provided in the menu. In SAP Fiori, columns are shown and hidden via the table personalization dialog or via the table personalization dialog. Do not use this property.
- The property: visibleRowCount defines the height of the analytical table. Show as many rows as fit on the screen.
- The property: visibleRowCountMode defines whether the height of the analytical table is fixed or automatically calculated based on the space provided by the underlying container. For automatic calculation, make sure that all rows have the same height.
- The property: minimumAutoRowCount defines the minimum number of rows that must be shown if the property: visibleRowCountMode is set to “auto”. Show at least three to five rows.
- The property: firstVisibleRow defines the first row shown in the visible area of the analytical table. The analytical table is scrolled accordingly.
- The property: allowColumnReordering is deprecated. Use the property: enableColumnReordering instead.
- The property: editable does not have a visible effect. Please do not use it.
- The property: threshold is used for optimizing lazy loading of items. In most cases, the default value is appropriate.
- The property: enableGrouping is experimental and does not have a meaningful effect on the analytical table. Do not use it.
- The property: sumOnTop shows additional aggregation values on the group header, even if the group is expanded. Do not use it.
- The property: enableCustomFilter changes the filter entry in the column header menu from an edit box to *Filter…*. Selecting this entry throws an event that apps can react to, for example, by opening a dialog. In general, you should choose the built-in filter over your own implementation. Specifically, keep filtering via the column header menu simple, while offering more advanced options via the table personalization dialog.
- The property: enableBusyIndicator has not yet been fully implemented. Do not use it.
- The property: title adds a line of text on top of the analytical table. Do not use it. To add a title to the table, use a toolbar.
- The property: footer adds a short text at the bottom of the table.
- The property: Busy sets the analytical table to busy state. While in busy state, the whole table cannot be used and items cannot be read due to an overlay.
- The property: Tooltip does not have an effect. Do not use it.
- The property: alternateRowColors displays the rows with alternating background colors (“banded rows”). Do not use it.

sap.ui.table.AnalyticalColumn

The following additional properties are available for the analytical column:

- The property: leadingProperty is used for data binding.
- The property: inResult is used for data binding.
- The property: visible defines whether a column is shown or hidden.
- The property: name defines the name shown in the column header menu for showing and hiding columns. In SAP Fiori, columns are shown and hidden via the table personalization dialog or via the table personalization dialog. Please do not use this property.
- The property: headerSpan defines whether one column header is used for one or several columns. To prevent adverse side effects, always use one column header for only one single column. Please do not use this property.
- The property: Tooltip does not have an effect. Please do not use it.

## Resources

#### Elements and Controls                                                                                                                  | #### Implementation                                                                                            | #### Visual Design
- [Bullet Micro Chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/bullet-micro-chart/) (guidelines)                     | - [Analytical Table](https://ui5.sap.com/#/api/sap.ui.table.AnalyticalTable) (SAPUI5 API reference)            | - [Analytical Table](https://wiki.one.int.sap/wiki/pages/viewpage.action?pageId=2698915566) (visual design specification)
- [Comparison Micro Chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/comparison-micro-chart/) (guidelines)             | - [Analytical Column](https://ui5.sap.com/#/api/sap.ui.table.AnalyticalColumn) (SAPUI5 API reference)          | - [Table](https://wiki.one.int.sap/wiki/pages/viewpage.action?pageId=2848852795) (visual design specification)
- Feed List Item (guidelines)                                                | - [Analytical Column Menu](https://ui5.sap.com/#/api/sap.ui.table.AnalyticalColumnMenu) (SAPUI5 API reference)
- [Grid Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/grid-table/) (guidelines)                                     |
- [Link](https://www.sap.com/design-system/fiori-design-web/ui-elements/link/) (guidelines)                                                 |
- List Report Floorplan (guidelines)                                          |
- [Multi-Input Field](https://www.sap.com/design-system/fiori-design-web/ui-elements/multiinput/) (guidelines)                              |
- [Responsive Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/) (guidelines)                         |
- [Stacked Bar Micro Chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/stacked-bar-micro-chart/) (guidelines)           |
- [Table Personalization Dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-personalization-dialog/) (guidelines) |
- [Table Toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/) (guidelines)                                   |
- [Tree Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/tree-table/) (guidelines)                                     |
- [Variant Management](https://www.sap.com/design-system/fiori-design-web/ui-elements/variant-management/) (guidelines)                     |
- [View Settings Dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/view-settings-dialog/) (guidelines)                 |
#### Elements and Controls                                                                                                                  | #### Implementation
- [Bullet Micro Chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/bullet-micro-chart/) (guidelines)                     | - [Analytical Table](https://ui5.sap.com/#/api/sap.ui.table.AnalyticalTable) (SAPUI5 API reference)
- [Comparison Micro Chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/comparison-micro-chart/) (guidelines)             | - [Analytical Column](https://ui5.sap.com/#/api/sap.ui.table.AnalyticalColumn) (SAPUI5 API reference)
- Feed List Item (guidelines)                                                | - [Analytical Column Menu](https://ui5.sap.com/#/api/sap.ui.table.AnalyticalColumnMenu) (SAPUI5 API reference)
- [Grid Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/grid-table/) (guidelines)                                     |
- [Link](https://www.sap.com/design-system/fiori-design-web/ui-elements/link/) (guidelines)                                                 |
- List Report Floorplan (guidelines)                                          |
- [Multi-Input Field](https://www.sap.com/design-system/fiori-design-web/ui-elements/multiinput/) (guidelines)                              |
- [Responsive Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/) (guidelines)                         |
- [Stacked Bar Micro Chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/stacked-bar-micro-chart/) (guidelines)           |
- [Table Personalization Dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-personalization-dialog/) (guidelines) |
- [Table Toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/) (guidelines)                                   |
- [Tree Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/tree-table/) (guidelines)                                     |
- [Variant Management](https://www.sap.com/design-system/fiori-design-web/ui-elements/variant-management/) (guidelines)                     |
- [View Settings Dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/view-settings-dialog/) (guidelines)                 |

---

## grid-list

The grid list displays a set of items. Whereas the [list](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/list-overview/) and the [responsive table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/) display the items in rows, the grid list displays the items as rectangular boxes on a grid. This makes it ideal for displaying visual content, such as [images](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/image/), [charts](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/), or [object cards](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/cards/#object-card).

*Grid list*

## When to Use

### Use the grid list if:

- You want to display a set of homogeneous items.
- The rectangular format of the items is better suited to your content than [tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) or [lists](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/list-overview/).
- The focus is on complete items, not cells.
- Your items mimic the format of existing objects (such as business cards).
- Users need to sort, group, or filter the items.

### Don’t use the grid list if:

- Your content isn’t suitable for a card-like format. If you need to display a lot of detail or if your content is very text-heavy, use a [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) instead.
- You expect to show more than 1.000 items. For better performance, use the [grid table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/) or [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/) instead.
- You need an overview of a large amount of data. In this case, consider using a [chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/).
- You only need the grid-style layout. In this case, use a layout container, such as the [flexible grid](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/flexible-grid/).

## Components

*Grid list components*
1. [Title bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#1-title-bar) or toolbar
2. [Filter infobar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#2-filter-infobar-optional) (optional)
3. [Items](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#3-items)
4. [*More* button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#more-button-optional) (optional)
5. [Footer](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#footer-optional) (optional)
### 1. Title Bar

Default (col-1)

The title bar contains the [title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/title/) of the grid list and an item counter.
Instead of a a title bar, you can use a [toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/). The toolbar can have the following elements:
- [Title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/title/) and an [item counter](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/#title) or [a selection and item counter](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/#title)
- [Variant management](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/)
- [Actions](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement), such as *Add* or *Edit*.
- A [segmented button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/#segmented-button) for switching views
- A button to open a [view settings dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/view-settings-dialog/)
*Title bar*
*Toolbar instead of title bar*

> **Guideline, Col-2:** - Use a [title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/title/) if you need a counter, [toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/) actions, or [variant management](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/). To avoid repeating text, you can also use a generic title text, such as *Items*.
- Don’t show the title bar at all if all these elements are already available nearby ([title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/title/), counter, [variant management](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/), [toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/)).
Example: An [object page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/) section contains only one grid list. In this case, add the item count and the [toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/) to the section header.
- For the item count, apply the following:
- Use the format: [Title] ([count])
Example: *Items (234)*
- Include all the items that a user can reach by scrolling, except group headers.
- Remove the item count if no items are displayed.
- For the selection and item count, apply the following:
- Use the format: [Title] (S*elected: [count of selected items] of [item count]*)
Example: *Items (Selected: 22 of 234)*
- Include all the items that a user can reach by scrolling, except group headers.
- Remove the selection and item count if no items are selected.
- If you are using a *More* button, don’t show a count on the title bar. Show the count below the *More* button instead.
- Keep the title bar sticky (`sap.f.GridList`, property: `sticky`).

> **Hint, Col-2:** Assistive technologies (such as screen readers) use the title to create a hierarchical site map for faster navigation. In addition,
screen readers use the title as the label for the table.
If you don’t use a title (for example, to avoid repetition), make sure that the table is connected to another meaningful on-screen text
that can be used as a label for assistive technologies. You can do this using the method `addAriaLabelledBy`.

Section Metadata

style

### 2. Filter Infobar (Optional)

Default (col-1)

The filter [infobar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/infobar/) shows information on the filter settings.
*Filter infobar*

> **Guideline, Col-2:** Display the filter infobar when the grid list is filtered.

Section Metadata

style

### 3. Items

Default (col-1)

A grid list item can contain any content. This can include single controls or a combination of controls (for example, using layout containers).
A grid list can contain different item types. For example:
- Sales orders and purchase orders
- Items in display mode and single items in edit mode
You can [highlight items](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#highlighting-items) and show an [item state](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#item-states) (such as “unread” or “locked”).
*Example of a grid list item*

> **Guideline, Col-2:** - Ensure that items can be identified. For example, add a title and subtitle.
- If the item has an ID and a description, use the title for the description and the subtitle for the ID.
- Avoid truncation. Use wrapping instead.
- Since no specific item templates are available, we recommend following the guidelines for [object cards](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/cards/#object-card).

Section Metadata

style

*Another example of a grid list item*
#### Highlighting Items

Default (col-1)

To show that an item needs attention, you can display a highlight indicator to the left of the item.
(`sap.m.ListItemBase`, property: `highlight`)
*Highlighted item*

> **Guideline, Col-2:** - Use highlighting to indicate:
- A  value state, such as red for an error or orange for a warning. In this case, use [semantic colors](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/visual/colors/colors#semantic-colors).
- Additional information, such as blue to highlight newly added items. In this case, use [semantic colors](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/visual/colors/colors#semantic-colors).
- Industry- / process-specific states, such as “Out of Stock” or “Excess of Inventory”. In this case, use [indication colors](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/visual/colors/colors#indication-colors).
- Provide information within the item to explain why it is highlighted, ideally in the same color. The highlight is just a visual cue. It doesn’t tell users *why* the item has been highlighted.
- For more details on the usage of highlight colors, see [How To Use Semantic Colors / Industry-Specific Colors](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/visual/how-to-use-semantic-colors).

Section Metadata

style

#### Item States

Show the different item states as follows:

**State** | **How to Display**
Unread    | Shows most content in bold.
`sap.f.GridList `property: `showUnread`
```
sap.f.GridListItem
```
property: `unread`
*Unread item next to a read item*
> **Guideline:** - Show only one state at a time.
- For detailed guidelines on the different states, see the [item state guidelines for the responsive table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/#item-states).

[Modified](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/manage-objects-with-the-global-flow) | Add the string *(Modified)* near the item identifier.
*A modified item*
Error | Add the string *(Contains errors)* near the item identifier.
```                                                          | *An item with an error*
sap.m.ObjectStatus
```
Property: `state`
Value: `sap.ui.core.ValueState.Error`
Highlight the item accordingly
```
sap.f.GridListItem
```
property: `highlight`
Locked | Add a transparent [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) with the corresponding icon and the text *Locked by [Name]* near the item identifier.
Clicking the [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) opens a [quick view](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/quickview/) of the person. | *A locked item*

[Draft](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/draft-handling) | Add a transparent [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) with the text *Draft* near the item identifier.
Clicking the [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) opens a [popover](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/popover/) showing the timestamp of the last change. | *An item in a draft state*

### “More” Button (Optional)

The [*More* button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#more-button) loads more items. The count below the button indicates the items displayed and the total number of items.
*'More' button*
### Footer (Optional)

You can use the footer to display additional static information relating to the content.
*Grid list footer*

## Behavior and Interaction

This section covers the following topics:

*Grid List:*                                                                                                                                               | *Grid List Items:*                                                                                                                                         | - [Add Items](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/#add-items)
| - [Busy State](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/#loading-data)
- [Loading Items](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#loading-items)             | - [Selecting Items](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#selecting-items)         | - [Context Menu](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/#context-menu)
- [Drag and Drop](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#drag-and-drop)             | - [Clickable Items](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#clickable-items)         | - [Empty Grid Lists](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/#empty-tables)
- [Keyboard Navigation](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#keyboard-navigation) | - [Actions](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#actions)                         | - [Enabling/Disabling Actions](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/processing-multiple-items#enablingdisabling-actions)
- [Errors and Warnings](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#errors-and-warnings) | - [Export to Spreadsheet](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/#export-to-spreadsheet)
| - [Grid List in Object Pages](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/#tables-in-object-pages)
| - [Paste](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/#paste)
| - [View Settings](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/#view-settings-sort-filter-and-group)

### Loading Items

Default (col-1)

You can load the grid list in “growing” mode.
In “growing” mode, only a limited number of items are loaded when the grid list is initially displayed. Additional items are only loaded (and rendered) on request. This request can be triggered either by [scrolling](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#scroll) (preferred) or by clicking the [*More* button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#more-button).

> **Guideline, Col-2:** - To optimize performance, we recommend showing no more than 200 items at once in the grid list.
- For larger datasets (200 to 1,000 items), use the “growing” mechanism to limit the number of displayed items (property: `growing`), and make sure that users can filter the data.
- Ideally, use [scrolling](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#scroll) to load more items instead of the *More* button (property: `growingScrollToLoad`).
- Use the [*More* button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#more-button) only if content is shown below the grid list.

> **Warning, Col-2:** The 200 and 1,000 item limits given here are only recommendations. For a specific app context, the number of
manageable items might be far higher or lower.
The actual limits depend on your concrete scenario, including:
- The number of items in the grid list
- The number of displayed data points inside the items
- The complexity of the data points (for example, simple text vs. complex charts)
- Other elements on the page (for example, multiple pages in a flexible column layout, or several tables/elements
with more complex rendering on one page)
- The browser being used

Section Metadata

style

#### Scroll

Default (col-1)

The height of the grid list is defined by the number of items it contains.
The grid list is scrolled together with the page and doesn’t have its own scroll container. When the user scrolls
through the page, the title bar and filter infobar can stick to the top of the surrounding layout container
(`sap.f.GridList`, property:`sticky`).
*Sticky toolbar*

> **Information, Col-2:** The “sticky” feature comes with some limitations:
- It isn’t available on all browsers.
- Certain layout containers suppress the sticky behavior, such as the grid layout. The same happens if the grid list
is placed within the object page.

Section Metadata

style

#### “More” Button

Default (col-1)

The *More* button is the default implementation when growing is switched on (property: `growing` = `true`).
*'More' button with loaded/total items*

> **Guideline, Col-2:** - Only use the *More* button if your page contains content below the grid list.
- Below the *More* text, show the number of items already loaded and (if possible) the total number items.
- Don’t show an item count on the title bar. Use the count on the *More* button instead.

Section Metadata

style

### Drag and Drop
Default (col-1)

The grid list offers the same drag and drop features as the [responsive table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/#drag-and-drop1).
However, because the items in the grid list are rearranged after an item is dropped, it isn’t always clear where the item will finally be placed.

> **Guideline, Col-2:** When dropping items from outside the grid list, adapt the size of the drop indicator to match the target layout of the item.
```
sap.f.dnd.GridDropInfo
```
Property: `dropIndicatorSize`
In addition, see the corresponding guidelines for the [responsive table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/#drag-and-drop1).

Section Metadata

style

### Keyboard Navigation

The grid list supports the following keyboard navigation options:

- **Arrow keys**: Navigate between items in all directions
- **Page Up** / **Page Down**: Skip several rows
- **Home**: Move the focus to the first item
- **End**: Move the focus to the last item

### Selecting Items

Default (col-1)

A grid list offers the same [selection modes as the responsive table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/#select)
(`sap.f.GridList` / `sap.m.ListBase`, property: `mode`).
Exception: A *Select All* checkbox isn’t provided. Users can only select/deselect all items with the keyboard shortcut (**CTRL\+A**).
*An unselected and a selected item in "multi-selection" mode*
*A selected item in "single select master" mode*

> **Guideline, Col-2:** - For all single selection modes, make sure that one item is initially selected. Otherwise, the user can’t return to the initial state. A selected item can only be deselected by selecting another item.
- For single-selection list-detail scenarios within the [flexible column layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout/), use the mode “single select master”. Don’t show an additional “navigated” indicator.
- Avoid the mode “single select left”. It removes the option to click somewhere on the item to select it. Use “single select left” only if you really need two different click areas; a small selection area, and the rest of the item for something else.
- Never disable the selection checkbox (multiple selection) or radio button (single selection). If an action can’t be performed on a specific item, inform the user after the corresponding action has been triggered. For more information, see [Enabling/Disabling Actions](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/processing-multiple-items#enablingdisabling-actions).
- If selecting/deselecting all items is important for your app, add a *Select All* [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) to the [toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/). Change the [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) text to *Deselect All* if all items are selected.

Section Metadata

style

### Clickable Items

Default (col-1)

The whole item can be clickable. You can define the action triggered by the click, such as opening a [dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/dialog/) (`sap.f.GridListItem`, property: `type`, value: `sap.m.ListType.Active` or s`ap.m.ListType.DetailAndActive`).
Active elements don’t have a visual indicator and therefore can’t be differentiated from non-active elements.
Clicks on interactive controls within the item are handled by the interactive control and don’t trigger the event for the item as a whole.

> **Guideline, Col-2:** - Don’t use the “Active” list item type for navigation, to switch the item to an edit state, or to delete the item.
- You can combine clickable items with [edit](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#action-edit) and [delete](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#action-delete) actions, but not with [navigation](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#action-navigation).
- Don’t combine clickable items with single selection. “Active” uses the whole item as a clickable area and therefore can’t be used together with a grid list in “single select master” mode.

Section Metadata

style

### Actions

Default (col-1)

You can offer actions for the entire grid list, [single items](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#actions-on-single-items), and [multiple items](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#actions-on-multiple-items).

> **Guideline, Col-2:** If an action is independent of the selection, show it on the [toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/) of the grid list. Examples of such actions are *Add* or *Edit* (in the sense of changing all items to edit mode), *Sort*, *Filter*, and *Group*.
To indicate if an action is available, follow the guidelines for [enabling/disabling actions](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/processing-multiple-items#enablingdisabling-actions).

Section Metadata

style

Default (col-1)

#### Actions on Single Items
You can offer actions for single items either on the toolbar or within the item.
[Delete](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#action-delete), [navigation](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#action-navigation), and [edit](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#action-edit) actions for single items are supported by the grid list control (see below).

> **Guideline, Col-2:** - Offer only one or two actions within the item. In this case, show the action trigger near the content to which it belongs.
- Use a button, unless the action trigger belongs to a link. Hide the action if it doesn’t apply to an item.
- If you offer [delete](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#action-delete), [navigation](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#action-navigation), or [edit](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#action-edit) actions for single items, always offer them at item level.

Section Metadata

style

##### *Delete:*

Default (col-1)

Use the “Delete” mode of the grid list (`sap.m.ListBase`, property: `mode`, value: `sap.m.ListMode.Delete`).
This places a *Delete* button ( :decline: ) in the top right area of the item.
*'Delete' button*

> **Guideline, Col-2:** - Don’t use the “Delete” mode if users typically need to delete multiple items.
- The “Delete” mode can’t be used with the “single select” or “multi select” selection modes.

Section Metadata

style

##### *Navigation:*

Default (col-1)

Use the “Navigation” item type (`sap.m.ListItemBase`, property: `type`, value: `sap.m.ListType.Navigation`).
This places a navigation indicator ( :slim-arrow-right: ) in the top right area of the item, and the entire item
becomes clickable.
By contrast, clicking an interactive control within an item doesn’t trigger the navigation event. Instead, the
corresponding control handles the click event.
*Navigation indicator*

> **Guideline, Col-2:** - Use the navigation action to navigate to a new page containing item details. In rare cases, you can also use the navigation action for the [category navigation](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/category-navigation/) pattern without navigating to another page.
- You can’t use the navigation action together with “[edit](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#action-edit)” or in combination with [click events for the entire item](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#clickable-items) (“Active”).

Section Metadata

style

##### *Edit*:

Default (col-1)

Use the “Detail” list item type (`sap.f.GridListItem`, property: `type`, value: `sap.m.ListType.Detail`).
This places an *Edit* icon ( :edit: ) in the top right area of the item. Clicking the button triggers the edit event.
Use this event to switch the corresponding item to edit mode.
*Edit button*

> **Guideline, Col-2:** If an edit mode is needed, change your text controls ([labels](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/label/), [text](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/text/), and [links](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/link/)) to [input fields](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/input-field/) or other appropriate editable controls as soon as you switch to edit mode, but not before. You can do this by changing the control or, in more complex cases, by exchanging the whole item.
You can’t use the “Edit” list item type together with the “[navigation](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#action-navigation)” list item type or in combination with click events for the entire item (“Active”).

Section Metadata

style

#### Actions on Multiple Items

Default (col-1)

To trigger actions for multiple items:
- Use a multi-selection grid list.
(`sap.f.GridList`, property: `mode`, value: `sap.m.ListMode.MultiSelect`)
- Offer the corresponding actions on the [toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/) of the grid list.
- Keep the [toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/) sticky.
(`sap.f.GridList, property: sticky`)

> **Guideline, Col-2:** - Don’t offer actions for multiple items if you expect the grid list to usually have fewer than 10 items.
- For mass editing scenarios, provide an *Edit* button. When the user clicks this button, open a dialog for editing the corresponding fields for all selected items. For more information, see [Mass Edit](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/mass-editing).
- In rare cases, you can also offer the corresponding actions in the [footer toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/footer-toolbar/). Do this only for [finalizing actions](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement#workflow) and if the grid list is the only area on the screen to which actions can be applied.

Section Metadata

style

### Errors and Warnings

Default (col-1)

Error handling must be implemented by the app team.
For details on displaying errors, warnings, and other messages, see [Message Handling](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/messaging).
*Grid list with errors*

> **Guideline, Col-2:** If the **grid list** contains items with errors or warnings, show a corresponding [message strip](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/message-strip/) above the grid list:
- On the message strip, provide information about errors or warnings.
- When issues are solved or when new issues appear, update the message strip accordingly.
Use [item states](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/grid-list/#item-states) to indicate errors and warnings for **single items**.

> **Hint, Col-2:** `sap.m.plugins.DataStateIndicator` displays a message strip above the table, which shows binding-related messages.

Section Metadata

style

## Responsiveness

Default (col-1)

The responsiveness of the grid list results from the underlying grid, which is defined by rows and columns. Columns
can have a minimum and maximum size or a fixed size. Whenever an additional column fits on the screen, it is added.
If a column no longer fits on the screen, it is removed. Items are re-layouted accordingly.
You can also define different configurations for the underlying grid using breakpoints (for example, based on the
device types).
### Predefined Layouts
To define the grid layout and behavior, you can use one of the predefined layouts:
- **Grid box layout**: Adds a variable number of columns, depending on the available screen width. Columns have
either a fixed width or can “breathe” slightly. All rows have the same height and all items are the same size.
- **Responsive column layout**: The number of columns depends on breakpoints (4 columns for size S, 8 for size M, 12
for size ML and L, 16 for size XL, 20 for size XXL and XXXL). The width of the columns grows or shrinks with the
available screen space until the next breakpoint is reached. The row height of the grid is determined by the height
of the highest item in the row. The number of rows and columns taken up by an item can differ.
### Custom Grid
Alternatively, you can define your own grid. This gives you much greater flexibility to influence both the layout and
the (responsive) behavior of the grid.
The underlying grid defines the available space per item. The width can differ according to the width of the screen
(“breathing”) or be fixed. The height can differ according to the content of the item or be fixed.
Items can use one ore more grid cells. Items can also be different sizes (for example, to allow for varying text
lengths/wrapping in different items).

> **Guideline, Col-2:** When defining a custom grid:
- We recommend letting items “breathe” to make better use of the available screen space.
- Make sure that the item adapts to the resulting width/height. For example:
- Re-layout the item content.
- Hide less important information.
- Re-size content, such as [images](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/image/) or [charts](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/).
When designing an item,
- Use the grid list item as starting point and make sure that the content adapts responsively to a changing item width / height.
- Don’t use other list items. They aren’t responsive enough.
- Use responsive content. For example, use controls that wrap text and configure them accordingly.

Section Metadata

style

## Examples

*Size S*           | *Size M*
*Size L*

## Properties

### sap.f.GridList

The following additional properties are available for the grid list:

- `inset` adds a margin on all sides of the grid list.
- `headerText` is a simple way to set the title for the grid list. However, this excludes the following:
  - A separate toolbar
  - Variant management
- `headerDesign` affects the appearance of the header if the theme supports it. Leave the default value as it is.
- `footerText` adds a small additional row below the table footer or last item. This row can contain text only. Don’t use this property.
- `width` defines the width of the whole grid list.
- `includeItemInSelection` uses a click on the whole item to select the corresponding item if the grid list is in a selection mode. This competes with other settings like “Navigation” or “Active” and therefore shouldn’t be used in combination with these two settings.
- `enableBusyIndicator` automatically shows a busy indicator while data is loaded. (In contrast to the `busy` property, where the application can control when the grid list is set to busy state)
- `modeAnimationOn` has no effect. Don’t use it.
- `showSeparators` has no effect. Don’t use it..
- `swipeDirection` has no effect. Don’t use it..
- `rememberSelections` should be set to “false” so that selections are reset or “forgotten” when the user applies, for example, a filter or sort to the table. Only change this behavior by setting the flag to “true” for exceptional cases.
- `busy` sets the grid list to a busy state. While in the busy state, the entire grid list can’t be used and items can’t be read due to an overlay.
- `busyIndicatorDelay` defines how long a busy state is shown after the grid list has been set to this state. Use the default value.
- `visible` shows the grid list (`true`) or hides it (`false`).
- `tooltip` provides a tooltip for the whole grid list. Don’t use it.

### sap.f.GridListItem

The following additional properties are available for `sap.m.ColumnListItem`:

- `selected` allows an item to be selected programmatically.
- `counter` shows a number on the right side of an item. This is used to show the number of subitems, for example.
- Don’t use the `busy` property.
- Don’t the `busyIndicatorDelay` property.
- `visible` shows or hides the item.
- `tooltip` adds a tooltip to a whole item. The tooltip is only shown on mouse interaction. It won’t work on tablets or smartphones. Don’t use it.

## Top Tips

- Use the grid list only if the content is suitable for a rectangular format.
- Ensure that items can be identified.
- Keep your grid and your items responsive. Consider allowing cards of different sizes to avoid content truncation.
- In your card design, either mimic existing objects like business cards or follow the guidelines for [object cards](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/cards/#object-card).

---

## grid-table

A grid table contains a set of data that is structured in rows and columns. It allows users to scroll in both directions and is optimized for handling large numbers of rows and columns.

## Usage

### Use the grid table if:
- The cell level and the spatial relationship between cells are more important than the line item. Examples include spreadsheet analyses and
waterfall charts. Note that a grid table is not fully responsive. It is only available for desktops and tablets, so you will need to take an adaptive
approach by offering an additional UI for smartphones.
- You need a table to display large amounts of complex data. The grid table can handle higher volumes more efficiently than the responsive table.
- - The focus is on working on line items, not on cells. The **responsive table** is optimized for displaying complete items on all devices, such as file browsing and a list of documents you want to act on, like purchase orders and purchase requisitions.
The responsive table can handle around 200 items when data is of average complexity — more items when data is less complex and fewer when data is
more complex. If your scenario exceeds these data limits, use the grid table. Factors that influence the exact limit include:
- You want to have only one implementation for all devices. However, make sure you adapt the responsive table design to offer the best solution for the tasks performed on mobile devices. Sometimes, a solution without a table is more useful and usable.
- - The number of loaded rows in the table
- The number of displayed columns
- The complexity of the cell content (for example, simple text vs. complex charts)
- Other elements on the page (for example, multiple pages in a flexible column layout, or several tables/elements with more complex rendering on
the page)
- The browser used
- Comparing items is a major use case. In this case, a grid table might be more appropriate than a responsive table. In the grid table, each cell
contains only one data point. In contrast, the responsive table is more flexible regarding line items, including the ability to add more data points
per cell and also the pop-in function. Both make comparisons more difficult.
- You’re going to implement inline creation and the sequence in which the items are created is important – the grid table creates new items at the
bottom of the table.
- Your use case is for tasks performed on a desktop or tablet device. The grid table is not [fully responsive](https://www.sap.com/design-system/fiori-design-web/ui-elements/grid-table/#responsiveness).
## Responsiveness

A grid table is not fully responsive, but available for only desktops and tablets, and it supports touch interactions. For mobile use cases, you need to:​

- Create a new Fiori application with reduced complexity, not an exact match of the desktop application.​
- With the new application, address the most important use cases for users in a mobile context. The responsive controls ([responsive table](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/), [list](https://www.sap.com/design-system/fiori-design-web/ui-elements/list-overview/) or [tree](https://www.sap.com/design-system/fiori-design-web/ui-elements/tree/),) or a relevant control for your use case (for example a [chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/chart/) or the [category navigation](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/category-navigation/) pattern) may suffice.

Or, you could create a fallback by using a [responsive table](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/), but a completely different solution, such as showing [charts](https://www.sap.com/design-system/fiori-design-web/ui-elements/chart-toolbar/) in a read-only case, might be more appropriate.

*Grid table shown on a desktop*

## Layout

1. *Select All* – The *Select All* checkbox selects or deselects all items.
2. Column header – The column header allows the user to resize and
rearrange columns. It also provides access to a menu with column-specific
commands.
3. Selector cells – The selector cells allow the user to select one or more
items.
4. Items – The collection of items, or rows, occupies the main part of the
grid table.
## Components

A grid table does not consist of other elements. However, it is common to use a [toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/) above the grid table.

The toolbar can contain entry points for the [view settings dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/view-settings-dialog/) and the [table personalization](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-personalization-dialog/) **[dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-personalization-dialog/)** or for the [p13n dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/p13n-dialog-popup/), as well as view switches in the form of a [segmented button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/), and [buttons](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/) for *Add*, *Edit*, and other actions.

## Behavior and Interaction

A grid table is quite restricted in terms of its content.

### Table Level

#### Scroll

A grid table allows horizontal and vertical scrolling (sap.ui.table.Table, property: navigationMode, value:
Scrollbar).
You can add any number of line items to the grid table, which uses “lazy loading”.
To prevent adverse side effects when scrolling vertically, all line items must have the same height
(sap.ui.table.Table, property: rowHeight).
The grid table is optimized to allow faster scrolling within the first 1000 items.

#### Select

##### Selection Mode

Selection for a grid table depends on the chosen selection mode. The following options are available:

**No selection**: Items cannot be selected. (property:
selectionMode = None)
*A non-selection grid table*

**Single selection**: One item in the grid table can be
selected. A row selector column is shown. (property:
selectionMode = Single)

Columns
**Multiple selection**: One or more items can be selected. The grid table
provides a column with checkboxes on the left-hand side. Clicking a checkbox
toggles the state of the corresponding row from deselected to selected and back.
The **Shift** key can be used to select a range.
For multiple selection, you can choose between two variants.
*Using the multi-selection plug-in with a limit*
- Multi-toggle mode (property: selectionMode = MultiToggle)
- Multi-selection plug-in (sap.ui.table.plugins.MultiSelectionPlugin)
These variants behave differently when the user selects more items than are
currently loaded in the front end.
#### Multi-toggle

In multi-toggle mode, you can offer a *Select All* checkbox to the left of the column header (property: enableSelectAll). Selecting this checkbox selects or deselects all items that are currently loaded in the front end (keyboard: **CTRL+A**). All other items are not selected/deselected. If the application data is stored in the back end, scrolling down further can reveal additional unselected items. The same can happen with range selections if not all items in the selected range have been loaded to the front end.

##### Multi-selection plug-in

If you use this plug-in instead of the multi-toggle selection mode, the behavior for range selection and *Select All* changes:

- By default, a dedicated *Deselect All* button replaces the *Select All* checkbox. There is no default UI element for selecting all items.
- You can set a limit for the number of items that can be selected (sap.ui.table.plugins.MultiSelectionPlugin, property: limit). This limit has the following effect:
  - The range that can be selected using the **Shift** key is limited to the specified number of items (default = 200). The table automatically scrolls back to the last selected item and you can display a corresponding message (sap.ui.table.plugins.MultiSelectionPlugin, property: enableNotification). Users can select more items by selecting additional ranges (the specified limit applies each time).
  - If the selection limit is set to 0, a *Select All* checkbox is shown. There is also no limit on the number of items that can be selected in a range. All selected items are loaded, which can lead to performance issues for large data sets. (Keyboard: **CTRL+A**)
- If selected items are not already available in the front end, they are loaded automatically by the plug-in and set as selected.

> **Information, Col-1:** When setting a limit for the number of items that can be selected, keep the following boundaries in mind:
- The performance of your service: How many items can be loaded at once in a reasonable time? Does this also apply if
an end-user shows all available columns?
- The “minimum limit”: Internally, the grid table loads blocks of items as the user scrolls down. Because this block
size (sap.ui.table.Table, property: threshold) is usually also based on the performance of the service, it should be
safe to assume that the minimum selection limit is twice this size. In this case, loading the data would take as long
as scrolling down and loading exactly one more block. Nevertheless, we recommend using larger limits if your service
allows.

##### Selection Behavior

An item can be selected in different ways, depending on the configuration of the grid table (sap.ui.table.Table, property: selectionBehavior):

- *Row*: An item is selected by clicking the checkbox or the row. Use this option for multi-selection grid tables if clicking a row or a cell is not used for anything else.
- *RowSelector*: An item is selected only by clicking the checkbox in the selector cell. Use this option if clicking the row (or a cell inside the row) is used for something else, such as navigation.
- *RowOnly*: An item is selected only by clicking the row, and not using checkboxes in the selector cells. Use this for single-selection grid tables if clicking a row or a cell is not used for another purpose, such as navigation.

#### Compact, Cozy, and Condensed

Like all SAP Fiori controls, the grid table is shown in compact mode on a desktop and in cozy mode on tablets.

For a desktop, you can also display even more rows on the same screen height by adding the condensed mode in addition to the compact mode. This renders less white space for each item.

Note that the condensed content density has always to be set in addition to compact. Do not use condensed on its own. Do not mix condensed with cozy. Doing so could lead to unpredictable and / or unwanted results, e.g. cozy sized controls in condensed sized containers, missing paddings, etc.

Note that neither compact mode nor condensed mode can be interacted with via touch. Even on a desktop with a touch screen, users will have difficulty selecting rows or using controls inside the cells when using their fingers.

Furthermore, condensed mode is not available for Internet Explorer 9. If condensed mode is to be used, please provide a fallback.

For more information on cozy and compact modes, see [content density](https://www.sap.com/design-system/fiori-design-web/foundations/visual/cozy-compact).

### Column Header

The column header provides the label for the corresponding column and access to the
column header menu.
*Column header*
Columns are resized as follows:
- **Mouse interaction:** The user drags the separator line between two columns
(sap.ui.table.Column, property: Resizable). Double-clicking the line optimizes the
column according to the length of the currently visible data and the label of the column
header (sap.ui.table.Column, property: Autoresizable).
- **Touch interaction:** The user taps the column header to reveal two buttons – one to
show the column header menu, and one for resizing. The user drags the latter to resize
the column.
- **Keyboard interaction:** The width of the focused column header can be increased via **Shift\+Right** and decreased via **Shift\+Left**.
After resizing a column, the adaptation of the column widths depends on how the column
width is set:
- If column widths are set in pixel-based units (px, em, rem), the corresponding column
is adapted and the columns that follow are moved accordingly. The width of all other
columns is not affected.
If all the columns together take up less width than the table control, an empty space
is added. In case all columns together take up more width than the table control, a
scrollbar appears. (sap.ui.table.Column, property: width)
- If all column widths are set in percentage or “auto”, resizing one column might also
lead to the automatic resizing of some or all other columns. The position of the resized
column might also be affected. This is done to ensure that the whole table width is used
and no white space is added. A scrollbar appears only if all or most of the columns
shrink significantly. To avoid the side effect of undersized columns, a minimum width
can be set per column. Please be aware that this minimum width is only taken into
account if columns are automatically resized. End users are still able to reduce the
column width below the provided minimum. (sap.ui.table.Column, properties: width,
minWidth)
Columns can be rearranged by dragging the column header to another position
(sap.ui.table.Table, property: enableColumnReordering). Keyboard: the focused column
header can be moved by one position in the corresponding direction via **Ctrl\+Left** / **Ctrl\+Right**.
#### Column Header Menu

For each column, a menu can contain the following menu items
(sap.ui.table.ColumnMenu, property: visible):
*Column header menu*
- *Sort Ascending/Descending* (sap.ui.table.Column, property: showSortMenuEntries)
- Free text filter (sap.ui.table.Column, property: showFilterMenuEntries)
- *Freeze* from the first to the last specified column (sap.ui.table.Table,
property: enableColumnFreeze)
For each column, the menu can be replaced by an app-specific menu.
#### Sort

The column header menu can provide two sort options
(sap.ui.table. Column, properties: sortProperty,
showSortMenuEntry):
- *Sort Ascending*
- *Sort Descending*
The user selects one of these options to sort the
corresponding column accordingly (sap.ui.table. Column,
properties: sorted, sortOrder, sortProperty).
#### Filter

The column header menu can provide a search field for entering free text (sap.ui.table.Column, properties: filterProperty,
showFilterMenuEntries).
*Free text filter in column header menu*
If the user enters a term in the input field and triggers the search by pressing Enter when the focus is on the filter input field,
the grid table is filtered by the corresponding column and value (sap.ui.table.Table, properties: filtered, filterProperty,
filterValue, filterOperator, sap.ui.table.Column, property: filterType).
Note that the filter may return zero results, in which case, the table might be empty.
General recommendations for filtering:
- If filtering is a main use case, choose the [filter bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/filter-bar/) or any other filtering UI over the built-in free text filter.
- Only use the free text filter if filtering is a secondary use case and if the filter bar is too heavy.
#### Freeze Columns

The column header menu can provide the option to freeze columns (sap.ui.table.Table,
property: enableColumnFreeze). Selecting *Freeze* freezes all columns up to the one in which
the operation was triggered (sap.ui.table. Table, property: fixedColumnCount).
When *Freeze* is triggered, the menu item changes to *Unfreeze* for the corresponding column.
### Line Item Level

A line item contains a set of cells and provides options
for selecting the item.
*Line item*
To prevent adverse side effects when scrolling
vertically, all line items must have the same height
(sap.ui.table.Table, property: rowHeight).
#### Drag and Drop

One or several items can be repositioned within a table
or moved to other UI elements using drag and drop
operations (sap.ui.table.Table, aggregation:
dragDropConfig). While being dragged, the items are shown
as ghost elements on the mouse cursor.
Drop targets can be on items, between items, or both
(sap.ui.core.dnd.DropPosition). On a drop target, the
mouse cursor changes to either a “copy”, “link”, “move”,
or “none” cursor. “None” indicates that the dragged item
cannot be dropped in the current position
(sap.ui.core.dnd.DropEffect).
Drag and drop is only available on supporting browsers.
#### Context Menu

You can attach a context menu (sap.m.Menu) to a table. The
context menu gives users an alternative way to modify the focused
elements by giving them access to context-specific functions.
When opened, the context menu gets the row and column context,
except for special columns (such as the selection column) or
special rows. Context menus can be implemented for a specific
table, row, or cell (not recommended for editable cells).
Context menus are opened by right-clicking (desktop), long press
(mobile), the **context menu key**, or **Shift\+F10**.
Be aware that using the context menu overrides the browser
context menu, which can no longer be opened.
If a control inside a table is the “click target”, and the
control also provides a context menu, the control context menu
“wins”.
### Cell Level

A cell provides one data point and can contain one of the following controls:
- [Button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-126/ui-elements/button/)
- [Checkbox](https://www.sap.com/design-system/fiori-design-web/ui-elements/checkbox/)
- [Combo box](https://www.sap.com/design-system/fiori-design-web/ui-elements/combo-box/)
- [Currency](https://www.sap.com/design-system/fiori-design-web/ui-elements/currency/)
- [Date picker](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-picker/)
- [Icon](https://www.sap.com/design-system/fiori-design-web/foundations/visual/iconography/icons)
- [Input](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/)
- [Label](https://www.sap.com/design-system/fiori-design-web/ui-elements/label/)
- [Link](https://www.sap.com/design-system/fiori-design-web/ui-elements/link/)
- The following micro charts size XS: [Bullet](https://www.sap.com/design-system/fiori-design-web/ui-elements/bullet-micro-chart/), [comparison](https://www.sap.com/design-system/fiori-design-web/ui-elements/comparison-micro-chart/), [stacked bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/stacked-bar-micro-chart/)
- [Multi-combo box](https://www.sap.com/design-system/fiori-design-web/ui-elements/multi-combobox/)
- [Multi-input field](https://www.sap.com/design-system/fiori-design-web/ui-elements/multiinput/)
- Object status
- [Progress indicator](https://www.sap.com/design-system/fiori-design-web/ui-elements/progress-indicator/)
- [Rating Indicator](https://www.sap.com/design-system/fiori-design-web/ui-elements/rating-indicator/)
- [Select](https://www.sap.com/design-system/fiori-design-web/ui-elements/select/)
- [Text](https://www.sap.com/design-system/fiori-design-web/ui-elements/text/)
Use only single-line text to keep the same row height. Truncate it if necessary to prevent adverse side effects with vertical scrolling (sap.m.Text, property: wrapping, value: false). Do not wrap.
We recommend against using other controls to prevent issues with alignment, condensed mode, screen reader support, and keyboard support.
## Guidelines

### Data Density vs. Complexity

The grid table can be used to display large amounts of data. Unfortunately, the grid table has a high data density and therefore conveys an immediate feeling of complexity.

Only show tables with a lot of data as a last resort. Try the following instead:

- Break down the data into manageable chunks and allow the user to navigate or drill down between them.
- Use charts with drilldown functionality until the amount of data is more manageable.

Try to avoid horizontal scrolling in the default delivery.

Try to minimize the number of columns, especially if there is a large number of rows.

### Table Title

Implement the table title by using a [title](https://www.sap.com/design-system/fiori-design-web/ui-elements/title/) control in a [toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/).

Use a table title only if the title of the table is not indicated in the surrounding area.

Do not use a table title if it simply repeats text that is already above the table. For example:

- A pricing conditions table is the only control on a tab labeled *Pricing Conditions*.
- A section or subsection on an object page contains only one table.

Use a table title if you need the item count, [table toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/), or [variant management](https://www.sap.com/design-system/fiori-design-web/ui-elements/variant-management/). To avoid repeating text, feel free to use generic text as a table title, such as *Items*.
Exception: If the surrounding area contains the table title, and both the item count and toolbar can be added to the surrounding area, no additional table title is needed.
Example: An object page (sub-)section contains only one table. In this case, add the item count and the table toolbar to the (sub-)section header.

If you use a table title, show either a title for the table, with or without [variant management](https://www.sap.com/design-system/fiori-design-web/ui-elements/variant-management/), or an item count in the following format:

*Items (2,534)*.

The item count in the table title includes all the visible items that a user can reach by scrolling.

Remove the item count in the table title if there are zero items.

> **Hint:** Assistive technologies (such as screen readers) use the title to create a hierarchical site map for faster
navigation. In addition, screen readers use the title as the label for the table.
If you don’t use a title (for example, to avoid repetition), make sure that the table is connected to another
meaningful on-screen text that can be used as a label for assistive technologies. You can do this using the method
addAriaLabelledBy.

### Selection

#### Single Selection

For single-selection list-detail scenarios within the [flexible column layout](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout/), do not show an additional “navigated” indicator.

#### Multiple Selection

- We strongly recommend using the multi-selection plug-in. This ensures that all items selected using *Select All* or as part of a range are included – even if some items were not initially loaded in the front end. This is not the case if you use the multi-toggle option.
- Do not limit the range selection for the multi-selection plug-in unless you have to.
  - If the dataset is small and/or completely available in the front-end, set the limit property to 0 to enable the *Select All* option and allow users to select any range.
  - If you have a large dataset, set a limit on the number of selected items to avoid performance issues. Also bear in mind that some actions won’t be helpful if the dataset is too big (for example, a delete operation on 2 million database entries).
- If you set a limit, also display the corresponding message when the user selects more items at once than the limit allows (sap.ui.table.plugins.MultiSelectionPlugin, property: enableNotification).

> **Information:** When setting a limit for the number of items that can be selected, keep the following boundaries in mind:
- The performance of your service: How many items can be loaded at once in a reasonable time? Does this also apply if
an end-user shows all available columns?
- The “minimum limit”: Internally, the grid table loads blocks of items as the user scrolls down. Because this block
size is usually also based on the performance of the service, it should be safe to assume that the minimum selection
limit is twice this size. In this case, loading the data would take as long as scrolling down and loading exactly one
more block. Nevertheless, we recommend using larger limits if your service allows.

- In multiple selection mode (multi toggle), do not show
checkboxes in the first data column in the default
delivery to avoid confusion.
*Do not add checkboxes to the first data column in the default delivery*

- Never disable the selection checkbox. If an action can’t be performed on a specific item, inform the user after the corresponding action has been triggered. For more information, see [Enabling/Disabling Actions](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/processing-multiple-items#enablingdisabling-actions).

### Loading Data

To indicate that the table is currently loading items, use the busy state.
(sap.ui.table.Table, property: busy). Do not show any items or text. As soon as the data is
loaded, remove the busy state and show all items.

### Errors and Warnings

Default (col-1)

To indicate that the table contains items with errors or warnings, show a [message strip](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-strip/) above the table. On the [message strip](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-strip/), provide information about errors or warnings. When issues are solved or when new issues appear, update the [message strip](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-strip/) accordingly.
To indicate an error in a single row, see [Item States](https://www.sap.com/design-system/fiori-design-web/ui-elements/grid-table/#item-states) below.
For details on displaying errors, warnings, and other messages, see [Message Handling](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/messaging).

> **Hint, Col-1:** The sap.m.plugins.DataStateIndicator displays a message strip above the table, which shows binding-related messages.

Default (col-2)

*Table containing errors and warnings*

Section Metadata

style

### Columns – Best Practices

Minimize the number of columns. Avoid the need to scroll horizontally in the default delivery.

The grid table assigns the same width to each column by default. It is recommended that you overwrite this default to provide optimal space for your content (sap.ui.table.Column, property: width).

If you define the column width in pixels or rems, resizing a column affects only the width of this specific column. Reducing the browser window size results in a scrollbar. After resizing a column, a scrollbar appears if the width of the table is not enough to show all columns. If the columns use less space than available, white space appears on the right side of the last column.

If you define the column width as a percentage, resizing one column affects the width of several or all columns. Text becomes truncated when the browser window size is reduced. This is done to make sure that all columns together fill the space of the table. A scrollbar appears only in case the automatic change of the column widths is not enough for showing all columns. To avoid the side effect of undersized columns, a minimum width can be set per column. Please be aware that this minimum width is only taken into account if columns are automatically resized. End users are still able to reduce the column width below the provided minimum.

If you define the column width as “auto”, the behavior is the same as for “percentage”. In contrast to percentage, “auto” distributes the columns equally.

To decide on how to set the column width (pixel / rem / em vs. percent / auto), keep the following in mind:

- For tables with only 2 to 3 columns, use pixel-based units. This ensures that on wide screens the values in the columns are not spread over the whole screen, which improves the readability of line items.
- For tables with many columns, where a horizontal scrollbar is usually needed, use pixel-based units. This avoids unintended side effects when resizing columns.
- For all other tables, use whatever fits your case better.

Be cautious with mixing columns with pixel-based and percentage-based widths. While this can be helpful in some cases, it could also cause even more unexpected side effects when resizing a column. When using percentage-based widths for one or more columns, think of the possibility to not allow end users to resize columns at all.

Optimize the column width for its     | Don't                                                                          | Don't
initial visible content, including    |
the column header texts. If this is   |
not possible (for example, if showing |
the full texts would result in        | *Don't truncate the initial visible content in the default delivery*           | *Never wrap texts*
extremely wide columns), let the      |
texts truncate. End users can change  |
the width of the column to read the   |
full text, as needed.                 |
Maintain a constant column width and  |
avoid adjusting it automatically when |
the content changes.                  |
Always keep to one line of text. Do   |
not wrap.                             |
### Column Headers – Best Practices

For each column, provide a label in the column header. In the default delivery, do not truncate the column header texts. Only let the text truncate if showing the full text would make the column too wide. Never wrap the text.

### Content Alignment

For alignment of cell content, follow the guidelines below.

Left-align the following: text, IDs, phone numbers, URLs,
passwords, and email addresses.
*Left-alignment of text*

Right-align numbers (except IDs).
This ensures comparability of numbers and amounts.

Right-align amounts with currencies to the cell and align
them in terms of their respective decimal points.
*Alignment to decimal point*
This ensures that amounts with different currencies are
shown correctly, whether these currencies have 0, 2, or 3
decimals.
For aligning to the decimal point, use the
sap.ui.uinified.Currency control.
Right-align dates and times.        |
This ensures comparability for most | *Right-alignment of dates*
formats and locales.                |
Left-align status information.
*Left-align status information*

Center-align icons.

Left-align micro charts.
*XS micro charts in condensed mode*

### Content Formatting

#### Locale Settings

Be locale-aware: show dates, times, numbers, and so on in
the format corresponding to the user’s locale settings.
#### Key Identifier

Use a bold label or an emphasized link as the key
identifier of an item. In the default delivery, show the
key identifier in the first column.

For strings with IDs, show the ID together with the
corresponding description whenever possible. Description
fields are hidden by default, so the dialog remains
clear, and key users can switch among ID only,
description only, or a combined display at any time. Use
a text arrangement if the metadata supports it, ensuring
consistent sorting, filtering, and grouping. Only use
separate ID and description columns if no text
arrangement can be provided because the user cannot
combine them later.
*Text and ID in one column – Sorting and filtering is available for either the text or the ID, but not for both*
*Text and ID in one column - If displaying a link, show the whole string as the link (text and ID)*

#### Truncation
Avoid truncation of typical content in the default
delivery (sap.ui.table.Column, property: width). However,
since the columns are resizable, do not worry too much if
truncation occurs as columns can still be enlarged if
necessary.
To prevent adverse side effects when scrolling
vertically, all line items must also have the same
height. If you need to decide between truncation and
different row heights, choose truncation. Do not wrap.
#### Number of Links
Are there too many links? Use subtle links to avoid a
wall of links. Standard links are also emphasized more if
they are surrounded by subtle links.
#### Missing Value
If there is no value for a cell, leave it blank. Do not
display text as *N/A*.
#### Numbering Items
In terms of numbering items:
- If the item number is more like an ID with regard to
its description, use ID formatting as described above.
- In all other cases, use a separate column for the item
number.
#### Status
For status information, use semantic colors on the foreground elements.
For status information on text, use an [object status](https://www.sap.com/design-system/fiori-design-web/ui-elements/object-display-elements/).
#### Micro Charts
Use only the following micro charts: [Bullet](https://www.sap.com/design-system/fiori-design-web/ui-elements/bullet-micro-chart/), [comparison](https://www.sap.com/design-system/fiori-design-web/ui-elements/comparison-micro-chart/), [stacked bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/stacked-bar-micro-chart/). When using micro charts, use them in size XS.

#### Empty Tables
Avoid empty grid tables. If necessary, provide instructions on how to fill the grid table with data (sap.ui.table.Table, properties: noDataText, showNoData).
Examples:
- If a table is initially empty, provide at least a basic text:
*No items available.*
Overwrite this whenever a hint can be provided on how to fill the table with data.
- If a table is used together with a [filter bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/filter-bar/) (as in the [list report](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/)), and is initially empty, use the following text:
*To start, set the relevant filters.*
- If a table is used together with a filter bar and the filter does not return results, use the following text:
*No data found. Try adjusting the filter settings.*
Adapt the texts above if:
- The standard text is not precise enough for your use case (for example, a search is also offered, or only the search is offered).
- The standard text is misleading (for example, if the data is filled based on a list-detail pattern instead of filter settings).
#### Invalid State
To show an invalid state of the grid table within the [list report floorplan](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/), show an overlay on the grid table and the corresponding toolbar (sap.ui.table.Table, property: showOverlay). The overlay prevents user interactions.
Use this within the list report floorplan if filter settings have been changed but the grid table is has not yet been updated.
### Item States

To show that an item has been modified, for example, within the global edit flow, add the string *Modified* in an additional column with the label *Editing Status*.
In the default delivery, add a column directly behind the key identifier.

To show that a modified item contains an error, for example, within the global edit flow, add
the string *Contains errors* in the *Editing Status* column and highlight the row accordingly. This string replaces the *Modified* string.
*A modified item with an error*
A row with errors should be highlighted in all use cases – for example when the field is
visible in the row in edit mode.
To show that an item is locked, add a transparent-style button with the corresponding icon and the text *Locked by [name]* in the *Editing Status* column.
*A locked item*

To show that an item is in [draft](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/draft-handling) state, add a transparent-style button with the text *Draft* in the *Editing Status* column.
*Item in draft state*

Show only one state at a time.

### Numbers and Units

Show the unit of measurement in one of the following ways:

#### Number and Unit in Same Cell
The number and the unit are in the same cell. Do this if sorting and filtering by the unit of measurement are not needed.
For amounts, use a [currency](https://www.sap.com/design-system/fiori-design-web/ui-elements/currency/) control to display the concatenated string.
#### Number and Unit in Separate Columns
The number and unit are in separate columns. Do this if
sorting and filtering by the unit of measurement are a
common use case.
Note that this column can be hidden or moved
independently of the column containing the corresponding
number. Therefore, be sure to have clear labels for both
columns to communicate the dependency.
Show the unit of measurment on the column header, if the
unit of measurement is the same for all rows. If not,
show the unit of measurement within the row.
### Drag and Drop

If you offer drag and drop for rearranging items within
the table, use drop targets that are between items
(sap.ui.core.dnd.DropPosition.Between). This provides
better feedback on where the item will be inserted. Show
the “move” mouse cursor
(sap.ui.core.dnd.DropEffect.Move).
Do not combine rearranging items and sorting. If you
really need to do so, make sure that there is a dedicated
sort criterion for the user-defined sort order, and only
offer options for rearranging items if this sort order is
set.
Drag and drop is “invisible” on the UI: users can’t see where dragging is available and where it isn’t. In addition, there is no generic keyboard interaction. Drag and drop is also
not available on all browsers. For these reasons, provide it only in addition to existing (and visible) UI elements that fulfill the same purpose. For example, offer ([toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/)) [buttons](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/) for moving or for copying and pasting items. These are keyboard operable and available on all browsers.
*Use drag and drop only in addition to existing visible UI elements*

### Context Menu

Use the context menu only as a quick way of accessing functions that are already available elsewhere (for example, as buttons in the toolbar). Don’t just offer actions in the context menu itself, as users might not realize that these actions are available at all.

The context menu can be triggered for the table, row, or cell. However, we do not recommend using context menus for cells: because the content of a cell is a different touch target than the cell itself, opening a cell context menu via touch is quite hard, even in cozy mode.

Do not combine context menus with condensed mode: editable controls fill the entire space inside a cell. Because of this, context menus cannot be opened at all with touch or mouse interaction.

### Actions

You can offer actions for table items in three places: in the table toolbar, inline in a table cell, or per row in a dedicated actions column.

#### Recommendations

Place actions in the **table toolbar** when:

- Actions apply to the entire table or to all items.
- Actions apply to the selected items.

Place actions inline in a **table cell** when:

- The action directly modifies the data in that cell.
- The action depends on the cell content and can vary for each item.

Use a **dedicated actions column** when:

- Actions apply to the entire item.
- Actions depend on the state of the individual item.
- Users prefer to act item by item.

#### Toolbar Actions

Toolbar actions apply to the entire table, to all items, or to the selected items. For selection-based actions, the table must support multi-selection. To trigger actions on multiple items, use a mutli-selection grid table (sap.ui.table.Table, property: selectionMode, value: MultiToggle). Actions in the toolbar can be enabled or disabled based on the selection.

If the use case requires both multi-selection and item-level processing, you can also show the same actions inline or in an actions column.

#### Inline Actions

If an action only affects a single data point in the table, it can be placed inside the table cell for each item. The action can depend on the status of the data (for example, adding or replacing an assignee). Use inline actions with care, since they increase table complexity and size.

#### Row Actions in "Actions" Column

Actions that are applied to a table row can be placed in a dedicated "actions" column. In the grid table, the actions column is provided by the RowAction element. It’s rendered as the last column and remains visible when users scroll horizontally.

If the navigation indicator is used, it is always shown as the last action in the actions column. Additional row actions can be added before it. When multiple row actions are added, they are automatically moved into the overflow, while the navigation indicator always remains visible.

> **Information:** Header for "Actions" Column
When you offer a dedicated column for row actions, you don’t need to show a visible column header label. According to
WCAG, it’s sufficient to provide an accessible name for the column header so assistive technologies can announce it.
On the row level, actions are self-explanatory. This guidance has been validated by internal and external
accessibility experts.

You can also create a custom actions column by placing actions in a separate column. Use this approach only in exceptional cases and implement it with care. **If you use the default actions column, any additional custom actions column must include a visible column header label**.

#### Navigation Action

As mentioned above, the navigation action can be part of the actions column. Alternatively, you can render cell content as a link that triggers navigation.

**Multi-selection in a list-detail scenario:**
When you use a multi-selection table in a list-detail scenario, it can be unclear which item was last opened (for example, which item is currently shown in the second column of a [flexible column layout](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout/)). In this case, you can display a "navigated" indicator to show which item is currently open.

#### Single Cell

To trigger actions on a single cell, create the corresponding click event. Do not use the cell click event if the cell contains interactive controls, such as links.

#### Add Items

For adding items, place an *Add* or *Create* text [button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/) on the [table toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/).

- Use *Create* if the [button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/) adds a brand new item that doesn’t yet exist on the database.
- Use *Add* if the item already exists and is merely added or assigned to the current object.

Show new items as the first item of the table, with a visual highlight at the beginning of the row.

Enable the shortcut **Ctrl+Enter** (and ideally **Enter** in addition) to trigger the *Add* or *Create* button.

There are three options for adding an item. In order of priority (most recommended first), these are:

1. **Add the item inline**. Create an empty, editable row as the first item of the table. Show the *Save* [button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/) on the [table toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/). This option is recommended for simple scenarios with just a few columns and no option to hide columns.
2. **Open a [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog/)** for larger tables with up to 8 editable columns. Save the new item at [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog/) level.
3. **Navigate to a new page**. This behavior should only be used for very complex scenarios that cannot be handled by a [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog/) (for example, tables with more than 8 columns). When the user presses *Save* in the [footer toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/footer-toolbar/) of the create page, navigate back to the table.

Depending on the flow, an item can be in one of three different states:

- **New**: The item was just created inline and is in edit mode (for example, after pressing the *Create* [button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/)). It is highlighted with a visual indicator (information state).
- **Recent**: The item was just created and is in read-only mode (for example, if *Create* leads to a [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog/), and *Save* was triggered within the [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog/)). In this case, keep the item highlighted and display it as the first item of the table. Ignore current sort and filter criteria to keep the item visible.
- **Added**: The item has been fully added. It follows the sort and filter settings and also loses the visual highlight. This state is used after:
  - Inline creation: After *Save* was triggered on the [table toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/) or at page level.
  - Create with [dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog/): A table showing one or several items with the state “Recent” gets updated (for example, after sorting or filtering, or when the browser is refreshed).

In the context of [draft handling,](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/draft-handling) new items are not saved at table level, but rather with the entire draft.

For more details, see the guidelines for [managing objects](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/manage-objects) (including subarticles).

### Editable Content

For editable content, only use the following controls, and only one control per cell:
- [Button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/)
- [Input](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/)
- [Date picker](https://www.sap.com/design-system/fiori-design-web/ui-elements/date-picker/),
- [Select](https://www.sap.com/design-system/fiori-design-web/ui-elements/select/)
- [Combo box](https://www.sap.com/design-system/fiori-design-web/ui-elements/combo-box/)
- [Multi-combo box](https://www.sap.com/design-system/fiori-design-web/ui-elements/multi-combobox/)
- [Multi-input field](https://www.sap.com/design-system/fiori-design-web/ui-elements/multiinput/)
- [Checkbox](https://www.sap.com/design-system/fiori-design-web/ui-elements/checkbox/)
- [Rating Indicator](https://www.sap.com/design-system/fiori-design-web/ui-elements/rating-indicator/)
Only these controls are optimized for all viewing modes of the grid table.
If you need edit mode, change your text controls, such as label, text, link, object status, icons, and currencies, to editable controls as soon as you switch to edit
mode, but not before. You can do this by exchanging the controls, for example, from sap.m.Text to sap.m.Input.
For mass editing items:
- Provide multiselection.
- Provide an *Edit* button.
- If several items are selected, clicking the *Edit* button opens a dialog in which the user edits the corresponding fields for all selected items.
For more information, see [Mass Editing](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/mass-editing).
### View Settings

There are several ways to show *Sort* and/or *Filter* settings:
- Column header menu: In all cases, show the corresponding settings in the column header menu.
- [View settings dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/view-settings-dialog/): Simple and more flexible with regard to filter settings. No advantage for sorting.
- [Table personalization dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-personalization-dialog/):
Provides complex options for sorting items by several levels. It also provides a query-builder-like approach for filter
settings. The complexity of the options is also its downside. Use the table personalization dialog for tables with a large
number of items.
- If filtering is a main use case, use the filter bar. In this case, avoid offering additional filter settings on the table. If
you do, the filter settings on the grid table work only on the result set provided by the filter bar.
*Table toolbar with trigger for table personalization dialog*
Always be careful when synchronizing the settings in the dialog with the settings from the column header menu.
Trigger the dialogs in one of the following ways:
- **View settings dialog**: Provide several buttons, one for each of these view settings. Each button opens the view settings
dialog on the corresponding page.
- **P13nDialog**: Provide a settings button, which opens the table personalization dialog containing all pages.
Use only the view settings you really need.
Persist the user settings: When reopening the app, show
the grid table with the same sort and filter settings as
last defined by this user.
#### Sort

Always sort the table in a meaningful way when it first
loads. In most cases, this means sorting by the column
that identifies the row. This is usually the first column
in the default delivery.
To display the current sort state, an icon is shown in
the column header of the most recently sorted column.
This icon indicates the sort direction
(sap.ui.table.Column, properties: sorted, sortOrder,
sortProperty).
For the default sort settings, sort by the column that
identifies the row, which is usually the first column in
default delivery.
The descending sort order         |  |
must always be the exact          |                                                                      |
reverse of the ascending sort     | *Object status sorted ascending, with neutral status last*           | *Object status sorted descending, with neutral status first*
order. For each column,           |                                                                      |
provide a meaningful sort         |                                                                      |
order. For example:               |                                                                      |
- Sort text alphabetically        |                                                                      |
- Sort numbers by their value     |                                                                      |
- Sort status information by      |                                                                      |
the severity of the status:     |                                                                      |
- Ascending: Sort status        |                                                                      |
information from positive to  |                                                                      |
negative, with neutral last.  |                                                                      |
- Descending: Sort status       |                                                                      |
information from negative to  |                                                                      |
positive, with neutral first. |                                                                      |
- - Ascending with different        |  |
values per severity level: Sort |                                                                                                            |
status information from         | *Object status sorted ascending and alphabetically, from positive to negative with neutral last*           | *Object status sorted descending and alphabetically, from negative to positive with neutral first*
positive to negative, with      |                                                                                                            |
neutral last. Sort different    |                                                                                                            |
values within a severity level  |                                                                                                            |
(semantic color)                |                                                                                                            |
alphabetically.                 |                                                                                                            |
- Descending with different       |                                                                                                            |
values per severity level: Sort |                                                                                                            |
status information from         |                                                                                                            |
negative to positive, with      |                                                                                                            |
neutral first. Sort different   |                                                                                                            |
values within a severity level  |                                                                                                            |
(semantic color)                |                                                                                                            |
alphabetically.                 |                                                                                                            |
#### Filter

To display the current filter state, an icon is shown in
the column header of the filtered column
(sap.ui.table.Column, properties: filtered,
filterProperty, filterValue, filterOperator,
defaultFilterOperator, filterType).
### Personalization

Only offer personalization if you need more columns than those that fit on a tablet screen, which is usually five, to fulfill 80% of your main use cases.

Persist the column layout. When a user reopens the app, show the grid table with the same column layout settings as last defined by this user.

#### Add, Remove, and Rearrange Columns

To add, remove, or rearrange columns, use one of the following:

- The [table personalization dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-personalization-dialog/): It offers some simple settings for column layout. Use this if you have only a few columns to choose from and/or you use the [view settings dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/view-settings-dialog/).
- The [p13n dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/p13n-dialog-popup/): Besides various complex view settings, it also provides settings for column layout. Use this if you have a large number of columns to choose from and/or you use this dialog anyway for view settings.

In both cases, trigger the dialog via the settings button in the [table toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/). As short cut, use **Ctrl+comma**.

You can also use drag and drop to rearrange columns (sap.ui.table.Table, property: enableColumnReordering). If you allow rearranging via drag and drop as well as via a dialog, keep both places in sync.

#### Resize Columns

Resizing columns works differently on touch and non-touch devices.

- Non-touch devices: Drag and drop the column separator on the right side of the column. Double-clicking the column separator optimizes the width of the column to the data currently loaded into the front end, which is usually about 100 rows.
- Touch devices: Clicking the column header reveals two buttons: one for opening the column header menu, another one for resizing the column. Drag and drop this second button to resize the column.

#### Freeze Columns
To freeze columns, offer the setting in the column header menu
(sap.ui.table.Table, property: enableColumnFreeze). Selecing *Freeze*
on a column freezes all columns from the first one to the one
where *Freeze* is selected. On this column, the menu entry changes from *Freeze* to *Unfreeze*.
#### Highlight Items
To show that an item needs attention, a highlight indicator can be shown in front of the item. The highlight indicator can be used to indicate:
- A semantic state, such as red or orange for an error or warning. In this case, use [semantic colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/colors#semantic-colors).
- Additional information, such as blue to highlight newly added items. In this case, use [semantic colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/colors#semantic-colors).
- Industry-specific or process-specific states, such as “out of stock” or “excess of inventory”. In this case, use [indication colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/colors#indication-colors).
Be aware that the highlight is just an indication. It does not tell users exactly what is wrong. Make sure that you provide this information within the table row, ideally in the same color.
For details on the use of highlight colors, see [How To Use Semantic Colors / Industry-Specific Colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/how-to-use-semantic-colors).
(sap.ui.table.Table, aggregation: rowSettingsTemplate)
### Tables in Object Pages

In the object page, you can use a [responsive table](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/#tables-in-object-pages) or grid table and offer navigation to a [list report](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/) with the table types mentioned above. In the [object page](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/), we advise using the [analytical](https://www.sap.com/design-system/fiori-design-web/ui-elements/analytical-table-alv/) and [tree tables](https://www.sap.com/design-system/fiori-design-web/ui-elements/tree-table/) in tab mode.

For more information on the use of tables within the object page, see the [Tables](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#tables) section of the *Object Page* article.

### Export to Spreadsheet

On the [table toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/), apps can provide a [menu button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/#menu-button1) for exporting table data to a spreadsheet. For the export, use the [export to spreadsheet](https://www.sap.com/design-system/fiori-design-web/ui-elements/export-to-spreadsheet/) function.
*'Export to Spreadsheet' menu button*

### Paste

The browser paste function can be used to paste data from the clipboard to the table if the focus is on an editable control within the table. The browser paste is triggered with the Ctrl + V keyboard shortcut, the table toolbar action, or actions in either the browser context menu or the table generic context menu.

The pasting of a new row or cell follows the [grid table inline creation](https://www.sap.com/design-system/fiori-design-web/ui-elements/grid-table/#use-the-grid-table-if) paradigm, where new items are created at the bottom of the table. The same happens when the data is pasted and a cell is unselected or focused.

##### Note

Pasting via the browser context menu is unavailable if the table has its own context menu because table context menu takes precedence over the browser context menu.

#### Paste (Overwrite)

Pasting overwrites data present in the table **only** when a cell with data is selected prior to pasting. When a single cell is selected, all the data in the clipboard is pasted into the table, extending from that cell. The paste will overwrite the data contained in those additional cells, too.

##### Note

If a user has selected multiple cells to overwrite, but the focus is placed outside of the selection, pasting will follow the guidelines for [inline creation](https://www.sap.com/design-system/fiori-design-web/ui-elements/grid-table/#use-the-grid-table-if) as above. This can happen, for example, when the user uses the arrow keys on the keyboard to move the focus.

#### Clipboard Selection Behaviour

If the clipboard has larger data set than the range selected for the paste, only the cells contained within the selection are updated.

On the other hand, if the clipboard has a dataset too small to fill all the cells selected for the paste, the pasted data updates only the selected cells for which there is data.

#### Read-Only

The paste action does not update read-only cells, even if there is data in the clipboard corresponding to those cells, but does update surrounding write cells.

##### Example

If the clipboard contains a range of four columns, and that data is pasted into a table, where column 2 is read-only, only the cells in column 1, 3, and 4 are updated.

## Properties

sap.ui.table.Table

The following additional properties are available for the grid table:

- The property: width defines the width of the grid table.
- The property: rowHeight defines the height of each row in the grid table. Since the height required is calculated automatically by the grid table, this property is only needed rarely.
- The property: columnHeaderHeight defines the height of the column headers. Since the height required is calculated automatically by the grid table, this property is only needed rarely.
- The property: columnHeaderVisible can be used to hide the column headers. Always show the column headers.
- The property: showColumnVisibilityMenu provides an additional entry in the column header menu that allows columns to be shown or hidden. In SAP Fiori, columns are shown and hidden via the table personalization dialog or via the table personalization dialog. Do not use this property.
- The property: visibleRowCount defines the height of the grid table. Show as many rows as fit on the screen.
- The property: visibleRowCountMode defines whether the height of the grid table is fixed or automatically calculated based on the space provided by the underlying container. For automatic calculation, make sure that all rows have the same height.
- The property: minAutoRowCount defines the minimum number of rows that must be shown if the property: visibleRowCountMode is set to “auto”. Show at least three to five rows.
- The property: firstVisibleRow defines the first row shown in the visible area of the grid table. The grid table is scrolled accordingly.
- The property: allowColumnReordering is deprecated. Do not use it. Use the property: enableColumnReordering instead.
- The property: editable does not have a visible effect. Do not use it.
- The property: enableCustomFilter changes the filter entry in the column header menu from an edit box to *Filter…*. Selecting this entry throws an event to which apps can react, for example, by opening a dialog. In general, you should choose the built-in filter over your own implementation. Specifically, keep filtering via the column header menu simple, while offering more advanced options via the table personalization dialog.
- The property: enableBusyIndicator has not yet been fully implemented. Do not use it.
- The property: title adds a line of text on top of the grid table. Do not use this. To add a title to the table, use a toolbar.
- The property: footer adds a short text at the bottom of the table.
- The property: Busy sets the grid table to busy state. While in busy state, the whole table cannot be used and items cannot be read due to an overlay.
- The property: Tooltip does not have an effect. Do not use it.
- The property: alternateRowColors displays the rows with alternating background colors (“banded rows”). Do not use it.

sap.ui.table.Column

The following additional properties are available for the column:

- The property: visible defines whether a column is shown or hidden.
- The property: name defines the name shown in the column header menu for showing and hiding columns. In SAP Fiori, columns are shown and hidden via the table personalization dialog or via the table personalization dialog. Do not use this property.
- The property: headerSpan defines whether one column header is used for one or several columns. To prevent adverse side effects, always use one column header for only one single column. Do not use this property.
- The property: Tooltip does not have an effect. Do not use it.

sap.ui.table.Column

The following additional properties are available for the column:

- The property: visible defines whether a column is shown or hidden.
- The property: name defines the name shown in the column header menu for showing and hiding columns. In SAP Fiori, columns are shown and hidden via the table personalization dialog or via the table personalization dialog. Do not use this property.
- The property: headerSpan defines whether one column header is used for one or several columns. To prevent adverse side effects, always use one column header for only one single column. Do not use this property.
- The property: Tooltip does not have an effect. Do not use it.

## Resources

Want to dive deeper? Follow the links below to find out more about related controls, the SAPUI5 implementation, and the visual design.

#### Elements and Controls                                                                                                                                | #### Implementation                                                                       | #### Visual Design
- [Analytical Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/analytical-table-alv/) (guidelines)                                   | - [Column](https://ui5.sap.com/#/api/sap.ui.table.Column) (SAPUI5 API reference)          | - [Tables](https://wiki.one.int.sap/wiki/pages/viewpage.action?pageId=2848852795) (visual design specification)
- [Bullet Micro Chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/bullet-micro-chart/) (guidelines)                                   | - [Column Menu](https://ui5.sap.com/#/api/sap.ui.table.ColumnMenu) (SAPUI5 API reference)
- [Comparison Micro Chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/comparison-micro-chart/) (guidelines)                           | - [Grid Table](https://ui5.sap.com/#/api/sap.ui.table.Table) (SAPUI5 API reference)
- [Feed List Item](https://www.sap.com/design-system/fiori-design-web/ui-elements/feedinput/) (guidelines)                                                | - [Grid Table](https://ui5.sap.com/#/entity/sap.ui.table.Table) (SAPUI5 samples)
- [Link](https://www.sap.com/design-system/fiori-design-web/ui-elements/link/) (guidelines)                                                               |
- [List Report Floorplan](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/) (guidelines) |
- [Multi-Input Field](https://www.sap.com/design-system/fiori-design-web/ui-elements/multiinput/) (guidelines)                                            |
- [Responsive Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/) (guidelines)                                       |
- [Stacked Bar Micro Chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/stacked-bar-micro-chart/)                                      |
- [Table Personalization Dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-personalization-dialog/) (guidelines)               |
- [Table Toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/) (guidelines)                                                 |
- [Tree Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/tree-table/) (guidelines)                                                   |
- [Variant Management](https://www.sap.com/design-system/fiori-design-web/ui-elements/variant-management/) (guidelines)                                   |
- [View Settings Dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/view-settings-dialog/) (guidelines)                               |
#### Elements and Controls                                                                                                                                | #### Implementation
- [Analytical Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/analytical-table-alv/) (guidelines)                                   | - [Column](https://ui5.sap.com/#/api/sap.ui.table.Column) (SAPUI5 API reference)
- [Bullet Micro Chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/bullet-micro-chart/) (guidelines)                                   | - [Column Menu](https://ui5.sap.com/#/api/sap.ui.table.ColumnMenu) (SAPUI5 API reference)
- [Comparison Micro Chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/comparison-micro-chart/) (guidelines)                           | - [Grid Table](https://ui5.sap.com/#/api/sap.ui.table.Table) (SAPUI5 API reference)
- [Feed List Item](https://www.sap.com/design-system/fiori-design-web/ui-elements/feedinput/) (guidelines)                                                | - [Grid Table](https://ui5.sap.com/#/entity/sap.ui.table.Table) (SAPUI5 samples)
- [Link](https://www.sap.com/design-system/fiori-design-web/ui-elements/link/) (guidelines)                                                               |
- [List Report Floorplan](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/) (guidelines) |
- [Multi-Input Field](https://www.sap.com/design-system/fiori-design-web/ui-elements/multiinput/) (guidelines)                                            |
- [Responsive Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/) (guidelines)                                       |
- [Stacked Bar Micro Chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/stacked-bar-micro-chart/)                                      |
- [Table Personalization Dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-personalization-dialog/) (guidelines)               |
- [Table Toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/) (guidelines)                                                 |
- [Tree Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/tree-table/) (guidelines)                                                   |
- [Variant Management](https://www.sap.com/design-system/fiori-design-web/ui-elements/variant-management/) (guidelines)                                   |
- [View Settings Dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/view-settings-dialog/) (guidelines)                               |

---

## responsive-table

The responsive table contains a set of line items and is fully responsive. Depending on the scenario, users can also navigate from the line items to further details.

A line item contains several data points sorted into columns. A data point refers to a unit of information, such as a number, a text, a unit of measurement, and so on, which can be used to form the content of a [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview), [form](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/form/) or other control. One data point is usually displayed by a control, such as a [text](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/text/), [object status](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/object-display-elements/#-object-status), or [input field](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/input-field/). A control can display more than one data point, for example, by concatenating text.

In contrast to traditional tables, a “cell” of the responsive table is not limited to displaying only one control, and therefore a single cell can present far more than one data point.

*Responsive table*

## Usage

### Use the responsive table if:

- You need a table to display a moderate amount of data. When your data is of average complexity, the responsive table can handle up to 200 items. However, more complex data lowers the limit, and less complex data raises it. Note that the limit is not on the number of items in the database or in the filtered results, but the volume of data **loaded at any point**. Factors that influence the exact limit include:
  - The number of loaded rows in the table
  - The number of displayed columns
  - The complexity of the cell content (for example, simple text vs. complex charts)
  - Other elements on the page (for example, multiple pages in a flexible column layout, or several tables/elements with more complex rendering on the page)
  - The browser used
- For loading large amounts of complex data, use a [grid table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/) instead, as it can handle higher volumes more efficiently.
- You need to use various controls inside a line item, such as [micro charts](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/micro-chart/). By contrast, the [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/) supports only a very limited set of controls.
- The focus is on line items, not on cells. The responsive table is optimized for viewing complete items on all devices.
- Selecting one or more items is a main use case and details are needed to choose the correct item.
- Line items are independent of each other and no operation across columns is needed.
- You want a single implementation for all devices. As its name suggests, the table is responsive and adjusts its appearance to the screen size so you can use it on all devices. However, make sure you adapt the responsive table design to offer the best solution for the tasks performed on mobile devices. Sometimes, a solution without a table is more useful and usable.

### Do not use the responsive table if:

- The main use case is to select one item from a very small number of items, without viewing additional details. In this case, a [select](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/select/) or [combo box](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/combo-box/) might be more appropriate.
- The main use case is to select one item from several items, with the possibility of viewing only a few details per item. In this case, a [list](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/list-overview/) might be more appropriate. Pay attention to the layout of the [list item](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/list-overview/#list-item-variants) to ensure that it has a pleasant appearance.
- The cell level and the spatial relationship between cells is more important than the line item. In this case, use the [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/) or [grid table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/). Examples include spreadsheet analyses and waterfall charts. Note that neither the analytical table nor the grid table are fully responsive. Both are only available for desktops and tablets, so you will need to take an adaptive approach by offering an additional UI for smartphones.
- You expect users to work with large amounts of complex data. Use the [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/) or [grid table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/) instead; they are optimized for those cases.
  Note that the analytical table and the grid table are not fully responsive, but available only for desktops and tablets, so you will need to take an [adaptive approach](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/discover/sap-design-system/vision-and-mission/responsiveness-adaptiveness#adaptive-approach) by offering an additional UI for smartphones.
- Comparing items is a major use case. In this case, the [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/) or [grid table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/) might be more appropriate because each cell contains only one data point. In contrast, the responsive table offers greater flexibility within line items, including the ability to add more data points per cell and the pop-in function. Both make comparisons more difficult. Note that neither the analytical table nor the grid table are fully responsive. Both are only available for desktops and tablets, so you will need to take an adaptive approach by offering an additional UI for smartphones.
- Data needs to be structured in a hierarchical manner. In this case, a [tree table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tree-table/) might be more appropriate. Although the [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/) can have several grouping levels, it is not as flexible when nodes at several levels contain child nodes. Note that the analytical table isn’t fully responsive and is only available for desktops and tablets, so you will need to take an adaptive approach by offering an additional UI for smartphones.
- You need an overview of a large amount of data. In this case, use a [chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/).
- You just need it for layout reasons. In this case, use a layout container such as a horizontal layout or a vertical layout instead.
- You need read-only or editable field-value pairs. In this case, use a [form](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/form/) instead. The responsive table is not optimized for form-like input navigation.

Don't
*Don't use a responsive table as a form*
See the [table overview](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) to decide which SAP Fiori table is most suitable for your needs.

## Responsiveness

The responsive table is optimized for viewing one line item at a time with no scrolling or only vertical scrolling, irrespective of the display width.

On smartphones, only the most important data remains in the one-column or two-column table, while all other data is moved to the space between two item rows, known as the “pop-in area”.

In this area, data for the corresponding cell is provided as a label/value pair. The label is defined by the column header, and the value is taken from the corresponding cell. Labels can be displayed next to the value or above the value.

Within the pop-in area, the label/value pairs can be displayed in the following ways (sap.m.Table, property: PopinLayout):

- Block: Label/value pairs are listed one below the other.
- GridSmall: Label/value pairs are displayed next to each other in equally spaced grid cells. An additional column is shown for each 13 rem of available width (208 px with default browser settings). If the number of grid cells exceeds the available width, the grid cells wrap. On S size, this layout transforms automatically to a block layout.
- GridLarge: The display logic is the same as for GridSmall,, but grid columns come with a larger minimum width (26 rem instead of 13 rem).

In all layouts, you can show the labels next to or above (recommended) the corresponding data.

The responsive table uses all the available space, and does not provide any padding. If there is space around the table, it comes from the spacing defined for the surrounding layout container.

> **Information:** The GridSmall and GridLarge layouts are not available in all browsers. If the chosen layout is not available, it is
automatically changed to Block layout.

*Responsive table displayed on a smartphone (size S)*

*Responsive table displayed in compact mode on a desktop computer (size L)*

The responsive behavior is optional. If it is not used, the responsive table minimizes all visible columns until they are no longer readable. The priority level assigned to columns also impacts the display of the responsive table. For more information on the priority levels, see: [Smart Table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/smart-table/#show-details-hide-details)

There are two ways to configure responsiveness: auto pop-in mode and manual pop-in mode (sap.m.Table, property: autoPopinMode).

The **auto pop-in mode** ensures responsiveness automatically and is sufficient in most cases. You can still influence the behavior per column, but only to a limited extent.

The **manual mode** is more flexible, but needs are more configuration. This configuration becomes more cumbersome when table columns can be shown/hidden or re-ordered. On the other hand, only the manual mode allows you to:

- Let more than one column stay in the tabular layout
- Move more than one column into the pop-in area at once

In both modes, the responsive table ensures that at least one column always remains in the table layout.

### Auto Pop-In Mode

The auto pop-in mode handles responsiveness automatically. You can optimize this to a certain extent by adapting the behavior per column.

Columns have a minimum width. As soon as the width of all the visible columns exceeds the table width, the right-most column moves to the pop-in area. The default minimum width per column is 8 rem. You can change this value for each column (sap.m.Column, property: autoPopinWidth).

To further influence the behavior, you can assign columns a priority. Low-priority columns move to the pop-in area first (right-most low priority column first), medium-priority columns next, and high-priority columns last. The default priority is “none”, which is handled like the “medium” priority (sap.m.Column, property: importance).Instead of moving columns to the pop-in area, you can also hide columns of one or more priority levels (property: hiddenInPopin).

In auto pop-in mode, all other pop-in-related column settings are ignored.

### Manual Pop-In Mode

The manual pop-in mode allows more flexibility but also requires more effort if you want it to work in a meaningful way. You also need to invest additional effort if table columns can be shown/hidden or re-ordered.

You need to configure each column manually. Depending on the width of the table (in pixels), the column needs to know which of the following responses is required:

- Stay in the table layout (in auto pop-in mode, only one column stays in the table layout).
- Move to the pop-in area (sap.m.Column, with the properties: demandPopin, minScreenWidth, popinHAlign, popinDisplay).
- Hide

By default, the table width is assumed to be the screen width. If the table does not use the full width of the screen, app developers must configure the table accordingly (sap.m.Table, property: contextualWidth).

Because you configure the pop-in response for each column individually, you can also handle more than one column at a given breakpoint. This allows you to move several columns to the pop-in area at once, which isn’t possible in auto pop-in mode

Each of the three device types has a predefined value for the screen width. However, you will get better results if you offer more breakpoints by using pixel values instead of the predefined values.

For the smallest screen width, keep the following information in the table layout:

- The identifier of the line item
- The key attribute

### Example for Block Layout

A typical responsive table.
*A typical responsive table*

Hide the information column for a width smaller than 570
px.
*Hiding the information column*

Move the column “vendor” to the pop-in area for a width
smaller than 460 px (sap.m.Column, properties:
demandPopin, minScreenWidth).

Move the column “limit” to the pop-in area for a width
smaller than 350 px (sap.m.Column, properties:
demandPopin, minScreenWidth).

Move the column “price” to the pop-in area for a width
smaller than 270 px (sap.m.Column, properties:
demandPopin, minScreenWidth).

If you still need to support smaller screens, values can
be moved below the corresponding labels inside the pop-in
area. In these examples, this happens for a width smaller
than 220 px (sap.m.Column, property: popinDisplay).
### Example for GridLarge Layout

A more complex responsive table.
*A more complex responsive table (full screen without pop-in content)*

In this example, the *Average Occupancy Rate* and *Available In*
columns move to the pop-in area if the screen width is less than
1900 pixels.

If the width is less than 1500 pixels, the *Average Stay* column moves to the pop-in area.
*GridLarge layout - 'Average Stay' column moves to the pop-in area*

If the width is less than 1100 pixels, the *Description*
column moves to the pop-in area. Since all four columns
in the pop-in area do not fit into one row, the pop-in
content wraps.
If the width is reduced even further, the *Details*
column moves to the pop-in area. On this narrow screen,
only one column fits into one pop-in row, so it looks
exactly like the block layout.
## Layout
The optional **title bar** consists of the title of the responsive table, an item counter, [variant management](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/), and the [toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/).
The **filter infobar** appears when the responsive table is filtered, and shows information on the filter settings.
The **column header** shows the label for each column. In addition, it allows the user to resize the column.
The collection of **items**, or rows, occupies the main part of the responsive table.
You can add aggregation information (such as totals) on the **table footer**.
A ***More*** **button** can be shown if you do not want all items to be loaded at the start (known as “lazy loading”). Ideally, you should use scrolling to load more items instead of choosing the *More* button.
## Components

The title bar contains the title of the responsive table, an item counter, [variant management](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/), and the [toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/).
The toolbar can contain entry points for the view settings dialog and the [table personalization dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-personalization-dialog/), as well as view switches in the form of a [segmented button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/), and [buttons](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) for *Add*, *Edit*, and other actions.
Beneath the toolbar, display a filter infobar (which itself is a special toolbar) if the responsive table is filtered.
To format within items, apply the guidelines for formatting data. Controls commonly used inside items are the object identifier and the object number. For more information about these controls, see [object display components](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/object-display-elements/).
You can use the table footer to display additional static information relating to the table content.
The *More* button loads more items to the front end if not all items have yet been loaded.
## Behavior and Interaction

The responsive table is quite flexible with regard to its content.

### Table Level

#### Scroll
The height of the table is defined by the number of items it contains. It does not have a scroll container on its own, but is scrolled together with the app (in contrast to the [grid table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/) and the [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/)).
If the table works in [“growing” mode](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/responsive-table/#load-items), it only loads a few items at first. Additional items are only loaded (and rendered) on request. The “request” can either be triggered by scrolling (preferred), or by clicking the *More* button.
Default (col-1)

When the user scrolls, the [title bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/), column headers, and filter infobar can stick to the top of the surrounding layout container (sap.m.Table, property: sticky).

> **Information, Col-1:** The “sticky” feature comes with some limitations:
- It is not available on all browsers. In non-supporting browsers, the corresponding areas ([title bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/), column headers, filter infobar) are not fixed on top of the surrounding layout container while scrolling.
- Certain layout containers suppress the sticky behavior, such as the grid layout. The same happens if the table is placed within the [object page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/).
- If focus is set to a fixed column header, the table is automatically scrolled to top.

Default (col-2)

*Sticky table title and sticky column header*

Section Metadata

style

#### Merge Duplicates
To simulate the behavior of row spanning, you can merge cells of consecutive rows inside one or more columns
automatically if they contain the same value (`sap.m.Column`, properties: `mergeDuplicates`, `mergeFunctionName`).
Use the merge feature if you expect the column to contain duplicate entries, and it makes sense to group them. In
the example screenshot, the *Supplier*, *Product*, and *Dimensions* columns reflect a hierarchical structure:
Suppliers have products, which in turn have dimensions. Because suppliers typically have multiple products,
merging duplicate entries for the supplier column makes the table easier to read. Note, however, that when the
user sorts the table by another field, the hierarchy changes and the merged items are regrouped accordingly.
Do not use the merge feature:
- If duplicate entries are not part of the design. If consecutive table rows happen to have the same values at
runtime, this alone isn’t a valid reason to group them.
- If the corresponding column can contain blank cells. Otherwise, it is cumbersome to differentiate between blank
values and merged values.
#### Select
A responsive table can have one of the following selection modes (`sap.m.Table`/ `sap.m.ListBase`, property: `mode`):                                                                                                                                                                                                                                                                       | *Responsive table without selectable items*
- **None**: Items cannot be selected (`sap.m.ListMode.None`).
Note: Line items can still use the `sap.m.ListType` “navigation”, which allows click handling for specific line items. Only use this option if the click triggers navigation to a corresponding details page.
- **Single select master**: One item in the responsive table can be selected. Items are selected by clicking the whole row. The single select master mode has no obvious
visual cues, such as checkboxes or radio buttons. It only provides a light blue background for the selected state. Because of this, it can barely be differentiated from
tables without selection (mode: `None`). Single select master is the preferred mode for single selection (`sap.m.ListMode.SingleSelectMaster`).
- **Single select left**: One item in the responsive table can be selected. For this, the responsive table provides radio buttons on the left side of each line item. This mode is not recommended (`sap.m.ListMode.SingleSelectLeft`).
- **Multi select**: Users can select one or more items using the checkboxes on the left of each line item. The **Shift** key can be used to select a range. Users can (de)select all items using the *Select All* checkbox to the left of the column header (or **CTRL\+A**). *Select All* should (de)select all items that the user can reach by scrolling. (sap.m.ListMode.MultiSelect).
Another multi select variant is to not provide a *Select All* option, but just a *Clear All* check box in the same place (property: `multiSelectMode`, value: `ClearAll`).
Keyboard: If the focus is on a row, the **space bar** selects the corresponding item.
*Multi select with 'Select All' checkbox*
*Multi select with 'Clear All' button*

#### Group
When items are grouped, a group header is displayed. The
group header is not interactive.
#### Show Aggregations
Show aggregations (such as totals) on the table footer (`sap.m.Column`, aggregation: `footer`).                                                                                                                                                                                                                   | *Table footer displays aggregated total*
Don’t show aggregations in [“growing” mode](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/responsive-table/#load-items). In “growing” mode it isn’t clear which values are being aggregated; only the items currently loaded in the front end, or all items.
Default (col-1)

#### Load Items
When the responsive table fits the general requirements for your use case, always consider ways to reduce the amount of **data loaded** in the responsive table with, for example, filters, graphics, aggregation of information, and navigation. Keep in mind you should use it only to display [moderate amounts of data](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/responsive-table/#use-the-responsive-table-if), including factors like number of items and content complexity.
To show more than 100 items, use the “growing” mode (`sap.m.Table`/ `sap.m.ListBase`, properties: `growing`, `growingThreshold`, `growingScrollToLoad`, `growingTriggerText`). The “growing” mode allows the user to load only the first few items. Additional items are only loaded (and rendered) on request, which improves [performance](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/#design-for-performance). You decide whether the user triggers the request by scrolling (preferred) or by clicking the *More* button.
If you use the *More* button, show the number of items already loaded and the total number items below the *More* text, if possible.
Do not show aggregations in “growing” mode. Also, do not display an item count on the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/) if “growing” mode is used. Use the count on the *More* button instead.

> **Guideline, Col-1:** If you expect users to work with large amounts of data, use the [grid table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/) because it is optimized for handling large data sets.
The growing mode will only help to reduce the amount of data loaded at once but the [limits to the overall amount of data](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/ui-elements/responsive-table/#use-the-responsive-table-if) still apply.

Default (col-2)

*Load on scroll*

Section Metadata

style

### Column Header Level

The column header provides the label for the corresponding column. It also handles the functionality for resizing columns.

#### Resizing Columns

Default (col-1)

If you implement column resizing, users can resize the columns as follows:
- **Mouse interaction**: The user drags the separator line between two columns. Double-clicking the line optimizes the column width based on the length of the
currently visible data and the label of the column header.
- **Touch interaction**: As for mouse interaction, but with a larger target touch area.
- **Keyboard interaction**: When the focus is on the column header, **Shift\+Right** increases the width of the focused column. **Shift\+Left** decreases the width.
When a column is resized, the other columns can keep their original width or adapt their width. This depends on the column width settings:
- If column widths are set in pixel-based units (px, em, rem), the resized column is adapted and the columns that follow are moved accordingly. The width of all the
other columns is not affected. If the visible columns don’t use the full width of the table control, empty space is added. If the visible columns exceed the width
of the table control, one or more columns move to the pop-in area.
- If all column widths are set as a percentage or as “auto”, resizing one column might also result in automatic resizing of some or all other columns. The position
of the resized column might also be affected. This ensures that the full table width is used and no white space is added.

> **Hint, Col-1:** To enable resizable columns, implement the plugin:
`sap.m.plugins.ColumnResizer`.

Default (col-2)

*Resizing a column*

Section Metadata

style

### Line Item Level

#### Delete Single Item Rows
To delete single item rows, use the table in the mode “delete” (sap.m.Table/ sap.m.ListBase,
property: mode, value: sap.m.ListMode.Delete). This adds *Delete* buttons to each line item.
Clicking this button triggers the deletion of the corresponding line item. (Keyboard: If the
focus is on the row itself, the **Delete** key can be used to trigger the *Delete* button.)
Do not use this mode if deleting multiple lines at once is the preferred use case.
Delete is a mode of the responsive table and therefore cannot be used together with single
selection or multiselection.
#### Highlight an Item
To highlight an item, use the “highlight” indicator
(sap.m.ColumnListItem, properties: highlight).
#### Navigate
To allow navigation from a line item, use an item with the type “navigation” (sap.m.ColumnListItem/ sap.m.ListItemBase, property: type, value: sap.m.ListType.Navigation). This creates an indicator at the end of the
line (“>”) and the entire line item becomes clickable (keyboard: if the focus is on the row itself, the **Enter** key triggers navigation). If the user clicks on the line, navigate to a new page containing line item details. In rare cases, you can also use the navigation mode for [category navigation](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/category-navigation/), without navigating to another page.
By contrast, clicking an interactive control within a line item does not trigger the navigation event. Instead, the corresponding control handles the click event.
If no navigation is possible, set sap.m.ListType to “inactive”.
“Navigation” is a list item type and therefore cannot be used together with “edit”, or in combination with click events for the entire item (“active”).
#### Indicate Navigated Item
When multi-selection is used in a list-detail scenario, it is not clear which item was last opened (for example, which item is currently shown in the second column of a [flexible column layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout/)). In this case only (multi-selection table with navigable items), you can display a **“navigated” indicator** to mark the item that is currently open (sap.m.ColumnListItem, property: navigated).

#### Edit Line Items

To allow editing for a line item, set sap.m.ListType to
“detail” within the corresponding item
(sap.m.ColumnListItem/ sap.m.ListItemBase, property: type,
value: sap.m.ListType.Detail or
sap.m.ListType.DetailAndActive). This will create an *Edit*
button at the end of the line. Clicking the button triggers
the edit event (keyboard: If the focus is on the row
itself, the **F2** key triggers the *Edit* button). Use
this event to switch the corresponding line item to edit
mode.
Edit is a list item type and therefore cannot be used
together with “navigation” or in combination with click
events for the entire item (“active”).
#### Click an Item

Items as a whole can be clickable. An event is fired by
clicking on the item (anywhere where there is no
interactive control inside the item). Apps can react on
the event, for example, by opening a dialog
(sap.m.ColumnListItem/ sap.m.ListItemBase, property:
type, value: sap.m.ListType.Active or
sap.m.ListType.DetailAndActive).
Active elements do not have a visual indication and can
therefore not be differentiated from non-active elements.
Active is a list item type and can therefore not be used
together with “navigation” or “edit”. In addition,
“active” uses the whole item as a clickable area and
therefore cannot be used together with a single-selection
table.
#### Drag and Drop

One or several items can be repositioned within a table
or moved to other UI elements using drag and drop
operations (sap.m.ListBase, aggregation: dragDropConfig).
While being dragged, the items are shown as ghost
elements on the mouse cursor.
Drop targets can be on items, between items, or both
(sap.ui.core.dnd.DropPosition). On a drop target, the
mouse cursor changes to either a “copy”, “link”, “move”,
or “none” cursor. “None” indicates that the dragged item
cannot be dropped in the current position
(sap.ui.core.dnd.DropEffect).
Drag and drop is only available on supporting browsers.
#### Context Menu

You can attach a context menu (sap.m.Menu) to a table. The
context menu gives users an alternative way to modify the
focused elements by giving them access to context-specific
functions.
When opened, the context menu gets the row and column
context, except for special columns (such as the selection
column). Context menus can be implemented for a specific
table or row.
Context menus are opened by right-clicking (desktop), long
press (mobile), the context menu key, or **Shift\+F10**.
Be aware that using the context menu overrides the browser
context menu, which can no longer be opened.
If a control inside a table is the “click target”, and the
control also provides a context menu, the control context
menu “wins”.
### Cell Level

#### Showing Information

In contrast to traditional tables (such as the [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/) or the [tree table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tree-table/)), a cell can contain more than just one line of text.
*Several lines of text within one cell*

#### Add Controls

Alongside textual elements, you can also add any control to a table cell, such as input fields, microcharts, buttons, and so on.

*Controls inside cells*

A cell can contain more than one control and more than
one data point.
*Several controls per cell*
With the *View Settings* dialog, users can sort, filter,
and group by each of these data points.
You can also have different controls in different rows in
the same column. This could be the case if one item is
locked, but another item is in edit mode, for example.

## Guidelines

### Responsiveness

In most cases, the auto pop-in mode is sufficient. If you need to optimize further, first try to adapt the columns to influence the automatic behavior (sap.m.Column, properties: autoPopinWidth, importance). For example, set the priority for the two or three most important columns to “High” (identifying column, key attribute).

While the pop-in layouts GridLarge and GridSmall make better use of the available width, they also only look good with content that is specifically designed for these pop-in layouts. If you have text-only tables with only one value per column, use the Block layout (sap.m.Table, property: popinLayout).

Place the column header labels in the pop-in area above the corresponding values (sap.m.Column, property: popinDisplay, value: Block). This avoids alignment issues with different content. Be aware that the labels get top-aligned with the adjacent content.
Only place the label next to the corresponding value under the following conditions (sap.m.Column, property: popinDisplay, value: Inline):

- The values are text-only (no input fields, icons, images, micro charts, and so on)
- The available space is at least the double the width of size S.

This avoids truncation or “over-wrapping” of the labels and content.

If a column does not have a column header text (for example, if it always contains the same button with its own label), do not show the header text as a label in the pop-in area either (sap.m.Column, property: popinDisplay, value: withoutHeader). If you forget this setting, you will see an empty space followed by a colon (“:”).

> **Information:** The GridSmall and GridLarge layouts are not available in all browsers. If the chosen layout is not available, it is
automatically changed to Block layout.

### Table Title

Implement the table title by using a [title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/title/) control in a [toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/).

Use a table title only if the title of the table is not already shown nearby. Do not use a table title if it simply repeats text that is already above the table. For example:

- A pricing conditions table is the only control on a tab labeled *Pricing Conditions*.
- A section or subsection on an object page contains only one table.

Use a table title if you need the item count, [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/), or [variant management](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/). To avoid repeating text, feel free to use generic text as a table title, such as *Items*.
Exception: If the surrounding area contains the table title, and both the item count and toolbar can be added to the surrounding area, no additional table title is needed.
Example: An object page (sub-)section contains only one table. In this case, add the item count and the table toolbar to the (sub-)section header.

> **Hint:** Assistive technologies (such as screen readers) use the title to create a hierarchical site map for faster
navigation. In addition, screen readers use the title as the label for the table.
If you don’t use a title (for example, to avoid repetition), make sure that the table is connected to another
meaningful on-screen text that can be used as a label for assistive technologies. You can do this using the method
addAriaLabelledBy.

If you use a table title, show either a title for the table, with or without [variant management](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/), or an item count in the following format:*Items (2,534)*
The item count in the table title includes all the visible items that a user can reach by scrolling. Group headers are not included.
Remove the item count in the table title if there are zero items. Do not use an item count together with “growing” mode.
If possible, keep the title bar sticky (sap.m.Table, property: sticky).

### Selection

For single selection cases, use the selection mode “single select master”. This is the recommended single-selection mode for list-detail scenarios within the [flexible column layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-96/page-types/page-layouts/flexible-column-layout/). If you use it there, do not show a “navigated” indicator.
In rare cases, you can also use the click area for the row for another purpose (for example, to open dialogs). As a result, the click area cannot be used for selecting the row. In these cases
only, use the “single select left” selection mode to offer a radio button as an additional click area for each row. To avoid confusion, make sure that the first data column does not contain radio
buttons in the default delivery.
For all single selection modes, make sure that one item is initially selected. Otherwise, the user cannot return to the initial state. A selected item can only be deselected by selecting another
item.
In multiple selection mode:
*Multiple selection - Don't show checkboxes in the first column in the default delivery*
- Prefer *Select All* over *Clear All*
- Use *Clear All* only for tables with a large number of items (more than recommended above), where loading all items to select them would harm performance.
- To avoid confusion, don’t show checkboxes in the first data column in the default delivery.
- Make sure that the *Select All* checkbox (de)selects all items the user can reach by scrolling. This is only possible if all items are rendered.
- Never disable the selection checkbox. If an action can’t be performed on a specific item, inform the user after the corresponding action has been triggered. For more information, see [Enabling/Disabling Actions](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-96/ui-elements/responsive-table/#enablingdisabling-actions).
*Use the selection mode "single select left" if clicking the row is used for something else (such as
navigation)*
Do
*Use the selection mode "single select master" in all other single selection cases*

> **Hint:** *Select All* is only applied to items that have already been loaded to the front-end server. All other items are not
(de)selected before they are loaded, such as items added via lazy loading with growingScrollToLoad. This conflicts with the
guideline that all items the user can reach by scrolling must be (de)selected.
To process all items, listen to the selectionChange event and to its selectAll flag. This indicates whether the *Select All*
checkbox was triggered. As soon as an action is triggered, process the items accordingly. Depending on the number of items,
consider processing them in the back end.

#### Selection Reset


When selection is enabled, make sure that selected items
are reset or “forgotten” each time the user refreshes the
table, for example, after applying a filter or sort.
(property: remember`Selections`, value: False).
Only for exceptional cases should you change this
behavior by setting the flag to “true”.
### Loading Data

To indicate that the table is currently loading items, use the [busy state](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/busy-state/).
(sap.m.Table, property: busy). Do not show any items or text. As soon as the data is loaded, remove the busy state and show
all items.

### Errors and Warnings

Default (col-1)

To indicate that the table contains items with errors or warnings, show a [message strip](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/message-strip/) above the table. On the [message strip](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/message-strip/), provide information on errors or warnings. When issues are solved or when new issues appear, update the [message strip](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/message-strip/) accordingly.
To indicate an error in a single row, see [Item States](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/#item-states) below.
For details on displaying errors, warnings, and other messages, see [Message Handling](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/messaging).

> **Hint, Col-1:** The sap.m.plugins.DataStateIndicator displays a message strip above the table, which shows binding-related messages.

Default (col-2)

*Table containing errors*

Section Metadata

style

### Columns – Best Practices

Minimize the number of columns:
- On a smartphone, use only one or two columns, depending on the content.
- On a tablet or desktop, use three to five columns if the responsive table is shown within the [flexible column layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout/). Use about eight columns if using the full screen width, depending on the content.
If the responsive table does not fit into the width provided:
*Do not distribute just a few columns across the full width*
- Hide columns to reduce the width of the table.
- Use pop-in areas to show the whole content by increasing the height of the line items (sap.m.Column, properties: demandPopin, minScreenWidth).
At the smallest size, keep the following information in the table layout:
- The column that identifies the line item.
- The column that contains the key attribute.
*Use a fixed column width instead*
If both of these do not fit into the width provided, keep just the column with the line item identifier in the tabular layout.
The responsive table assigns the same width to each column by default. In doing so, it uses all the available space. We recommend overwriting this default to provide optimal space for your content (sap.m.Column, property: width).
Especially for tables with just a few columns, we recommend assigning a fixed width to each column and to disabling automatic distribution of the remaining available space (property: fixedLayout, value: Strict). In this case, the rest of the table is filled with empty space.
Optimize the column width for its initial content (sap.m.Column, property: width). If the content is dynamic, optimize the column width for typical content.
When defining the column width, consider the implications when a column is resized:
- If you define the column width in pixels or rem, resizing a column only affects the width of that particular column.
- If the table isn’t wide enough to show all the columns after a column has been resized, one or more of follow-on columns move into the pop-in area.
- If the columns don’t use up the available space, white space appears to the right of the last column (property: fixedLayout, value: strict).
- If only one column remains, and the width of this column exceeds the width of the table itself, the width of the column is reduced to the width of the table.
- If you define the column width as a percentage, resizing one column affects the width of several or all columns. Text wraps more when the browser window size is reduced. This ensures that all columns together make use of the full table width.
- If you define the column width as “auto”, the behavior is the same as for “percentage”. However, unlike “percentage”, “auto” distributes the columns equally.
- Be cautious of mixing columns with pixel-based and percentage-based widths. While this can be helpful in some cases, it could also cause even more unexpected side effects when columns are resized. If you are using percentage-based widths for one or more columns, consider not allowing end users to resize columns at all.
If you need more columns than those that fit on a tablet screen (usually five) to fulfill 80% of your main use cases, offer an option to add, remove, and rearrange columns via the [table personalization dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-personalization-dialog/). Before doing so, try to reduce the number of columns, for example, by using several lines per column or by utilizing the pop-in function. See the [cheat sheet](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/responsive-table-content-formatting-cheat-sheet/) for an example.
### Column Headers – Best Practices

Within the column header, provide a label for each column (sap.m.Column, aggregation: header). The column header label is reused as a label in the pop-in area.

**Exception:** If the column does not pop in, no column header label is needed as long as at least one column still has a column header label.

To keep the column headers readable, wrap or truncate the texts as follows:

- If columns are **not resizable**, use controls that **wrap** and support wrapping with hyphenation, such as [text](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/text/) (with wrapping and hyphenation enabled). Do not use controls that truncate.
- If columns are **resizable**, use controls that **truncate**.

Keep column headers sticky.

Do
*Wrap column headers if columns are not resizable*

Column headers (sap.m.Column, aggregation: header) usually contain [links](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/link/) or text-based controls.

Column headers can also contain other kinds of SAP Fiori controls. However, the column header cannot be aligned vertically, making it difficult to use many controls in the column header. Using other kinds of controls also creates problems with pop-in behavior and could thus lead to accessibility issues. Therefore, exercise caution when using them in a column header.

*Accepted: Link as column header text (rarely used)*

If a column cell contains several fields, use an umbrella term in the column header (such as *Address* for fields like *Street*, *ZIP Code*, and *City*).

For text and ID fields, use a generic label (for example, *Employee* for *Name* and *ID*).

If none of these are possible, separate the labels with “/” (for example, *Name / Status*).

For boolean values, such as checkboxes, find a descriptive text for the column header.

### Horizontal Content Alignment

For alignment of cell content, follow the guidelines below (sap.m.Column, properties: halgin, valign, sap.m.ColumnListItem, property: VAlign). Align the column header horizontally according to the content of the cell.

**Exception:** Secondary information in a column always follows the alignment of the main information.

#### Left-Align

Left-align: Text, IDs, phone numbers, URLs, passwords,
and email addresses.
*Left-align text*

Left-align: [Status information](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/object-display-elements/#-object-status)
*Left-align status information*

#### Right-Align

Right-align: Dates and times (to ensure comparability for
most formats and locales)
*Right-align dates*

Right-align: Numbers and amounts, except IDs, to ensure
figures are comparable
*Right-align numbers*

#### Center-Align

Center-align: [Icons](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/icontabbar/), [images,](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/image/) and [avatars](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/avatar/)
Keep the column name for center-aligned columns as short as possible to avoid excessive white space between columns. Alternatively, you can leave the column header empty on the visual UI, and use the invisible text control to provide information on the column content for screen reader listeners.
Align buttons with the content hierarchically
Always place buttons directly next to their content. Do
not add an additional column for buttons. If you have
more than one button, display them next to each other.
Order the buttons based on importance. The most important
button is on the left, the least important on the right.
If there is not enough space to display them all in one
line, move the buttons from the right onto the next line
one by one. Do not use more than two buttons per line
item.
### Vertical Content Alignment

Top-align where possible to facilitate reading the content on one line.

Do not use top-alignment if it results in a peculiar layout. This usually happens when controls that need more vertical space are combined with text-only controls, such as input fields. In this case, try center-alignment instead and fine tune it until the layout fits.

Do
*Use top-alignment where possible*

### Content Formatting

The responsive table provides flexibility, including multi-line cells, by enabling every control to be put into a cell.

As a key identifier of an item, use an **object identifier**. Show the key identifier in the first column. For more information, see [object display components](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/object-display-elements/).
If the table width is small, do not hide this column or move it to the pop-in area.

Strings with IDs: If the responsive table contains more
single-line data, show the ID in brackets after the
corresponding string.
This minimizes the line height.
*If displayed as a link, use the whole text as the link*

Strings with IDs: If line height is already large, show the ID below the corresponding string. Use the [object identifier](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/object-display-elements/) to do so.
*For items with a large line height, place the ID below the corresponding string*
*Is displayed as a link, use only the first line as the link*

If there is more than one key identifier (for example, *First Name* and *Last Name*), display these columns first and show the values in bold text.
*Several key identifiers*

For status information, use semantic colors on the foreground elements.
For status information on text: If the status is actionable, add a transparent icon button next to the text.

Avoid truncation. Use controls that wrap the text and support hyphenation.

For example, use [text](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/text/).

Do
*Wrap text*

For editable content, use [input fields](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/input-field/)
and other interactive controls within the table cells. If you need to offer edit mode, change your text controls (labels, text, and links, to
input fields or other appropriate controls) as soon as you switch to edit mode, but not before.
You can do this by changing the control or, in more complex cases, by exchanging the whole responsive table.
If there is no value for a cell, leave it blank. Do not
display text as *N/A*.
*Leave empty fields blank*

#### Numbering Items
- If the item number has four digits/letters or less and is
equally important as the corresponding description,
concatenate the item number with the description and show
it in one column.
- If the item number has five digits/letters or more, or if
it is more important than the corresponding description,
for example, when no description is available, use a
separate column for the item number.
- If the item number is more like an ID in regards to its
description, use ID formatting, like *Description (ID)*.
#### Flag and Favorite
Place the [flag or favorite](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/flag-and-favorite/) marker in the first column (in the default delivery). To change the settings, users need to drill down into the object itself.

#### Empty Tables
Try not to display an empty responsive table. If there is no way around this, provide instructions on how to fill the table with data (sap.m.Table/ sap.m.ListBase, properties: showNoData, noDataText).
Examples:
- If a table is initially empty, provide at least a basic text:
*No items available.*
Overwrite this whenever a hint can be provided on how to fill the table with data.
- If a table is used together with a [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/) (as in the [list report](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/)), and is initially empty, use the following text:
*To start, set the relevant filters.*
- If a table is used together with a filter bar and the filter does not return results, use the following text:
*No data found. Try adjusting the filter settings.*
Adapt the texts above if:
- The standard text is not precise enough for your use case (for example, a search is also offered, or only the search is offered).
- The standard text is misleading (for example, if the data is filled based on a list-detail pattern instead of filter settings).
Remove the item count in the table title if there are zero items.
#### **Displaying Boolean Values**
If a column contains Boolean values, such as “Yes” or
“No”, show a read-only checkbox next to the texts.
The supplementary checkbox makes it easier for users to
see at a glance which items are “true” (checked) and
which are “false” (unchecked).
Developer Hint
Use sap.m.checkbox with the Horizon theme and set the
editable property to “false” to get the read-only
variant. Add the checkbox next to the existing text
value. The text itself should remain unchanged.
### Item States

To show that an item is unread, use the corresponding
flag (sap.m.Table, property: showUnread,
sap.m.ColumnListItem/ sap.m.ListItemBase, property:
unread). This shows most of the content in bold font.
To show that an item has been modified, for example,
within the global edit flow, add the string *(Modified)*
at the bottom of the column that identifies the line
item.
To show that a modified item contains an error (for example, within the global edit flow), add the string *(Contains errors)*
at the bottom of the column that identifies the line item. To do this, use an object status control with the error state (sap.m.ObjectStatus, property: state,
value: sap.ui.core.ValueState.Error).
In addition, highlight the row accordingly (sap.m.ListItemBase, property: highlight). A row with errors should be highlighted in all use cases – for example when
the field is visible in the row in edit mode.
To show that an item is locked, use a transparent button with the corresponding icon and the text *Locked by [Name]* at the bottom of the identifying column. The user can click the button to open a [quick view](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/quickview/) of the person.
*A locked item*

To show that an item is in a [draft](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/draft-handling) state, use a transparent-style button with the text *Draft* at the bottom of the identifying column. The user can click the button to open a [popover](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/popover/) showing the timestamp of the last change.
*Item in draft state*

Show only one state at any one time.

#### Highlight Items
To show that an item needs attention, you can show a highlight indicator next to the item. The highlight indicator can indicate:
- A  value state, such as red or orange for an error or warning. In this case, use [semantic colors](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/visual/colors/colors#semantic-colors).
- Additional information, such as blue to highlight newly added items. In this case, use [semantic colors](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/visual/colors/colors#semantic-colors).
- Industry-specific or process-specific states, such as “out of stock” or “excess of inventory”. In this case, use [indication colors](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/visual/colors/colors#indication-colors).
Be aware that the highlight is just an indication. It doesn’t tell users exactly what is wrong. Make sure that you provide this information within the table row, ideally in the same color.
For details on the use of highlight colors, see [How To Use Semantic Colors / Industry-Specific Colors](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/visual/how-to-use-semantic-colors).
(sap.m.ListItemBase, property: highlight)
### Numbers and Units

If the following conditions all apply, show the unit of measurement in the column header:

- The unit of measurement is the same for all rows
- A single cell contains only one amount with the unit of measurement
- The column header does not scroll away

In all other cases, show the unit of measurement together with the corresponding amount within the row.

Show the unit of measurement in the same column as the corresponding amount.

For numbers with units, show the correct formatting by
using the object number control.
*Object number*

For the most important number with its unit, show the
correct formatting by using the object number control and
the emphasized flag.
**Exception:** If all numbers are of equal importance,
emphasize none of them.
If the table width is narrow, do not hide this column or
move it to the pop-in area.
**Exception:** If the column containing the object
identifier and the column containing the key attribute do
not fit together on the screen, move the column
containing the key attribute to the pop-in area.
### Drag and Drop

Drag and drop is “invisible” on the UI: users can’t see where dragging is available and where it isn’t. In addition there is no generic keyboard interaction. Drag and drop is also not available on all browsers. For these reasons,
provide it only in addition to existing (and visible) UI elements that fulfill the same purpose and provide the corresponding keyboard support. For example, offer ([toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/)) [buttons](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) for moving or for copying and pasting items. These are keyboard operable and available on all browsers.
*Use drag and drop only in addition to existing visible UI elements*
Currently, there is no keyboard support for drag and drop.
If you offer drag and drop for rearranging items within
the table, use drop targets that are between items
(sap.ui.core.dnd.DropPosition.Between). This provides
better feedback on where the item will be inserted. Show
the “move” mouse cursor
(sap.ui.core.dnd.DropEffect.Move).
Do not combine rearranging items and sorting. If you
really need to do so, make sure that there is a dedicated
sort criterion for the user-defined sort order, and only
offer options for rearranging items if this sort order is
set.
When combining rearranging items with grouping, be aware
that moving items to another group also means that a
value of the dropped item changes: because grouping is
based on values in a column, the dropped item needs to
take on the value of the target group for the
corresponding column. If this is not wanted, do not allow
users to rearrange items in grouped tables.
Example:
A table is grouped by availability. An item is moved from
the group “Not Available” to the group “In Stock”. In
this case, the moved item needs to change its
availability to “In Stock” to match the target group. If
changing the value doesn’t make sense, only allow users
to rearrange the items within the same group, or don’t
allow rearranging at all.
### Context Menu

Use the context menu only to give users a quick way of accessing functions that are already available elsewhere (for example, as buttons in the toolbar).

Don’t just offer actions in the context menu itself, as users might not realize that these actions are available at all.

The context menu can be triggered for the whole table or per row.

### Actions

You can offer actions for table items in three places: in the table toolbar, inline in a table cell, or on row level in a dedicated column.

#### Recommendations

Place actions in the **table toolbar** when:

- Actions apply to the table itself (for example, change the table's state).
- Actions apply to all items in the table, independent of item selection (for example, approve all items in the table).
- Actions apply to selected items only. Based on the selected items, an action can also be enabled or disabled, depending on whether the selected items support the action.

Place actions inline in a **table cell** when:

- Actions only and directly affect the data shown in the cell.
- Actions depend directly on the content of the cell (for example, “Add” for an empty cell, but "Edit" for a filled cell).

Place actions at row level in a **dedicated actions** column when:

- Actions affect the entire line item.
- Actions depend directly on the state of the item (for example, the lifecycle of a document)
- The items in the table can support different actions.
- The user wants to take action item by item rather than selecting multiple items.

You can offer the same action at the row level in the actions column and in the toolbar as a selection-based action. This lets users work item by item or on the selected items.

To trigger actions on **multiple items**, use a multi-selection table (sap.m.Table, property: mode, value: sap.m.ListMode.MultiSelect), and offer the corresponding actions on the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/). Keep the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/) sticky (sap.m.Table, property: sticky).

> **Information:** Header for "Actions" Column
When you offer a dedicated column for row actions, you don’t need to show a visible column header label. According to
WCAG, it’s sufficient to provide an accessible name for the column header so assistive technologies can announce it.
On the row level, actions are self-explanatory. This guidance has been validated by internal and external
accessibility experts.

The following actions on **single items** must always be in-line:

Delete: Use “Delete” table mode (sap.m.Table/ sap.m.ListBase, property: mode, value: sap.m.ListMode.Delete). This places a *Delete* [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) at the end of each row. |
*Delete button*
Navigation: Use the “Navigation” column list item type (sap.m.ColumnListItem/ sap.m.ListItemBase,
property: type, value: sap.m.ListType.Navigation). This places a *Navigation* indicator at the end of each row.
*Navigation indicator*
Use this to navigate to a new page containing line item details. In rare cases, you can also use this
for navigation within the table without navigating to another page.
Edit: Use the “Detail” column list item type (sap.m.ColumnListItem/ sap.m.ListItemBase,
property: type, value: sap.m.ListType.Detail). This places an *Edit* icon at the end of each row.
*Edit button*

From these three actions (delete, navigation, and edit), you can combine delete and edit, or delete and navigation.

Edit and navigation cannot be combined.

To trigger actions that are independent of the selection, show the actions on the table toolbar. Examples of such actions are add, edit (in the sense of changing the whole table to edit mode), sort, filter, group (or view settings), and table personalization.

To trigger a default action on the whole line item, use the “Active” or “DetailAndActive” column list item type (sap.m.ColumnListItem/ sap.m.ListItemBase, property: type, value: sap.m.ListType.Active).

Active items trigger an event when clicked, which can be handled by apps (for example, to open a dialog). Clicks on interactive controls within the item do not trigger the event, but are handled by the interactive control. Do not use this for navigation, to switch the line item to an edit state, or to delete the item.

Active can be combined with edit and delete, but not with navigation. Do not combine active with single selection.

For information on enabling and disabling actions, see [Enabling/Disabling Actions](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/processing-multiple-items#enablingdisabling-actions).

#### Add Items

For adding items, place an *Add* or *Create* text [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) on the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/).

- Use *Create* if the [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) adds a brand new item that doesn’t yet exist on the database.
- Use *Add* if the item already exists and is merely added or assigned to the current object.

Show new items as the first item of the table, with a visual highlight at the beginning of the row.

Enable the shortcut **Ctrl+Enter** (and ideally **Enter** in addition) to trigger the *Add* or *Create* button.

There are three options for adding an item. In order of priority (most recommended first), these are:

1. **Add the item inline**. Create an empty, editable row as the first item of the table. Show the *Save* [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) on the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/). This option is recommended for simple scenarios with just a few columns and no option to hide columns.
2. **Open a [dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/dialog/)** for larger tables with up to 8 editable columns. Save the new item at the [dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/dialog/) level.
3. **Navigate to a new page**. This behavior should only be used for very complex scenarios that cannot be handled by a [dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/dialog/) (for example, tables with more than 8 columns). When the user presses *Save* in the [footer toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/footer-toolbar/) of the create page, navigate back to the table.

Depending on the flow, an item can be in one of three different states:

- **New**: The item was just created inline and is in edit mode (for example, after pressing the *Create* [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/)). It is highlighted with a visual indicator (information state).
- **Recent**: The item was just created and is in read-only mode (for example, if *Create* leads to a [dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/dialog/), and *Save* was triggered within the [dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/dialog/)). In this case, keep the item highlighted and display it as the first item of the table. Ignore current sort, filter and grouping criteria to keep the item visible.
- **Added**: The item has been fully added. It follows the sort, filter, and grouping settings and also loses the visual highlight. This state is used after:
  - Inline creation: After *Save* was triggered on the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/) or at page level
  - Create with [dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/dialog/): A table showing one or several items with the state “Recent” gets updated (for example, after sorting, filtering, or grouping, or when the browser is refreshed).

In the context of the [draft handling](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/draft-handling) new items are not saved on table level, but rather with the entire draft.

For more details, see the guidelines for [managing objects](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/manage-objects) (including subarticles).

*Add button in table toolbar*           | *New item as first row in edit mode*           | *Saved new item, still highlighted, still the first item*

### Editable Content

For editable content, use input fields and any other interactive controls within the table cells that meet your input needs.

All SAPUI5 controls can be used.

If you need edit mode, change your text controls, such as label, text, and link, to input fields, or other appropriate controls as soon as you switch to edit mode, but not before.

You can do this by exchanging the control or, in more complex cases, by exchanging the entire responsive table.

For mass editing items:

- Provide multiselection (sap.m.Table/ sap.m.ListBase, property: mode, value: sap.m.ListMode.MultiSelect).
- Provide an *Edit* button.
- If several items are selected, choosing the *Edit* button opens a dialog in which the user edits the corresponding fields for all selected items.

For details, see [mass editing](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/mass-editing).

### View Settings: Sort, Filter, Group

Sort, filter, and/or group settings are handled in the [view settings dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/view-settings-dialog/). This dialog can provide any combination of these three settings, including just one setting, such as sort only.
- If sorting, filtering, and/or grouping are a common use case in your app, offer one, two, or all three of the corresponding features in one or more view settings dialogs. Note: Do not offer
these features if the table is expected to have only a small number of entries (up to 20 in most cases).
- If filtering is a main use case, do not offer filtering in the view settings dialog. Use the [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/) instead.
To trigger the view settings dialog, provide several [buttons](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/), one for each of these view settings. Each button opens a view settings dialog that contains only the relevant page.
You should always use only the view settings you really need. For example, do not offer grouping if it does not support your use case well.
Using the view settings dialog allows you to define several sort, filter, and/or group settings per column. Therefore, you can sort, filter, and/or group a column with several data points
independently by each data point.
#### Sort

Always sort the table in a        |  |
meaningful way when it first      |                                                                      |
loads. In most cases, this        | *Object status sorted ascending, with neutral status last*           | *Object status sorted descending, with neutral status first*
means sorting by the column       |                                                                      |
that identifies the row. This     |                                                                      |
is usually the first column       |                                                                      |
in the default delivery. Use      |                                                                      |
the primary data point from       |                                                                      |
this column.                      |                                                                      |
If you offer sorting, offer       |                                                                      |
it for each data point. In        |                                                                      |
other words, allow sorting by     |                                                                      |
both the primary and              |                                                                      |
secondary information in a        |                                                                      |
column. Allow sorting in both     |                                                                      |
directions, ascending and         |                                                                      |
descending. The descending        |                                                                      |
sort order must always be the     |                                                                      |
exact reverse of the              |                                                                      |
ascending sort order.             |                                                                      |
For each data point, provide      |                                                                      |
a meaningful sort order. For      |                                                                      |
example:                          |                                                                      |
- Sort text alphabetically        |                                                                      |
- Sort numbers by their value     |                                                                      |
- Sort status information by      |                                                                      |
the severity of the status:     |                                                                      |
- Ascending: Sort status        |                                                                      |
information from positive to  |                                                                      |
negative, with neutral last.  |                                                                      |
- Descending: Sort status       |                                                                      |
information from negative to  |                                                                      |
positive, with neutral first. |                                                                      |
- - Ascending with different        |  |
values per severity level: Sort |                                                                                                            |
status information from         | *Object status sorted ascending and alphabetically, from positive to negative with neutral last*           | *Object status sorted descending and alphabetically, from negative to positive with neutral first*
positive to negative, with      |                                                                                                            |
neutral last. Sort different    |                                                                                                            |
values within a severity level  |                                                                                                            |
(semantic color)                |                                                                                                            |
alphabetically.                 |                                                                                                            |
- Descending with different       |                                                                                                            |
values per severity level: Sort |                                                                                                            |
status information from         |                                                                                                            |
negative to positive, with      |                                                                                                            |
neutral first. Sort different   |                                                                                                            |
values within a severity level  |                                                                                                            |
(semantic color)                |                                                                                                            |
alphabetically.                 |                                                                                                            |
#### Filter

Default (col-1)

To display the current filter state, use the [infobar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/infobar/) below the table title. Clicking the infobar opens the view settings dialog on the filter page.
Show the infobar only if the filter settings are not shown somewhere else. For example, do not show the infobar for settings taken in the filter bar or in a [select](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/select/) placed in the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/).
If the infobar is shown, provide an option to reset all corresponding filters on the infobar.
Keep the infobar sticky (sap.m.Table, property: sticky).

> **Hint, Col-1:** To display the current filter settings on the infobar, consider using the [list formatter](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/formatting/formatting-data-overview#commaseparated-lists) (sap.ui.core.format.ListFormat).

Default (col-2)

*Filtered table*

Section Metadata

style

#### Group

To display the current group state, group headers are
shown.
*Grouped table*
On the group header, show the following text
(sap.m.GroupHeaderListItem, property: title):
*[Label of the grouped column]: [Grouping Value]*
Do not use several values on the group header.
If there is no grouping value, show the following text:
*[Label of the grouped column]: (Not Available)*
*Grouped table, with missing grouping value*
This is the case if you have a group of items that don’t
have a value for the grouped column.
In general:

- Don’t use groups to display hierarchical data structures. A group is not an entity in the data structure but represents a set of properties all members of the group have in common. For hierarchical data, use the [tree table](https://www.sap.com/design-system/fiori-design-web/ui-elements/tree-table/) instead.
- Persist the view settings. When a user reopens the app, show the responsive table with the same sort, filter, and group settings as last defined by this user.

### Personalization: Add, Remove, Rearrange Columns

To enable users to add, remove, or rearrange columns, use the [table personalization dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-personalization-dialog/). Trigger the dialog via a [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) in the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/). Add the shortcut **Ctrl+Comma**.

Offer personalization if you need more columns than those that fit on a tablet screen, which is usually five, to fulfill 80% of your main use cases. Before doing so, try to reduce the number of columns, for example, by using several lines per column or by utilizing the pop-in function. See the [cheat sheet](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/responsive-table-content-formatting-cheat-sheet/) for an example.

If all columns are hidden, the table shows a corresponding “no data” text.

*View settings and table personalization icons*

Persist the column layout settings. When a user reopens the app, show the responsive table with the same column layout as last defined by this user.

### Tables in Object Pages

For more information on the use of tables within the object page, see the [Tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/#tables) section of the *Object Page* article.

### Export to Spreadsheet

On the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/), apps can provide a [menu button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/#menu-button1) for exporting table data to a spreadsheet. For the export, use the [export to spreadsheet](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/export-to-spreadsheet/) function.
*'Export to Spreadsheet' menu button*

### Paste

To paste data from the clipboard to the table, the browser functionality for paste can be used (**Ctrl+V** or browser context menu).

- If the focus is on row level, the app has to take the data from the clipboard and add it to the corresponding controls within the table.
- If the focus is on an editable control within the table, the control gets the data automatically.

Pasting via context menu does not work if a custom context menu is used.

## Properties

sap.m.Table

The following additional properties are available for the responsive table:

- The property: **fixedLayout** defines the algorithm the control uses to define column width. Setting it to “false” would perform automatic calculations for the column width, based on the longest non-breakable content. You should always set it to “true” for performance reasons. Exceptions are permissible if the table has only a few columns for a large width and fewer than 10 rows are displayed.
- The property: **backgroundDesign** defines the background on which items are rendered. Use the default value.
- The property: **showOverlay** provides an overlay on the whole table, which prevents use of the responsive table. This is used within the list report floorplan to mark the table as outdated after filter settings have been changed but the new filter settings have not yet been applied. Do not use it in other cases.
- The property: **inset** adds a margin on all sides of the responsive table.
- The property: **headerText** is a simple way to set the table title if you just need a title. However, do not use any of the following:
  - A separate toolbar
  - variantManagement
  - headerToolbar aggregation
- The property: **headerDesign** affects the appearance of the header if the theme supports it. Leave the default value as it is.
- The property: **footerText** adds a small additional row below the table footer or last item. This row can contain text only. Do not use this property.
- The property: **width** defines the width of the whole table.
- The property: **includeItemInSelection** uses a click on the whole line item to select the corresponding item if the responsive table is in a selection mode. This competes with other settings like “Navigation” or “Active” and should therefore not be used.
- The property: **enableBusyIndicator** automatically shows a busy indicator while data is loaded. (In contrast to the property: busy, where the application can control when the table is set to busy state)
- The property: **modeAnimationOn** does not have any effect. Do not use it.
- The property: **showSeparators** allows you to show all, none, or some separators. The default setting, which is to show all separators, is to be used.
- The property: **swipeDirection** allows you to define the direction in which to swipe if additional actions are hidden behind a table row. This works only on touch devices. Do not use this property.
- The property: **rememberSelections** should be set to “false” so that selections are reset or “forgotten” when the user applies, for example, a filter or sort to the table. Only change this behavior by setting the flag to “true” for exceptional cases.

* The property: **busy** sets the table to a busy state. While in busy state, the whole table cannot be used and items cannot be read due to an overlay.
* The property: **busyIndicatorDelay** defines the time after which a busy state is shown after the responsive table has been set to this state. Use the default value.
* The property: **visible** shows the table (“true”) or hides it (“false”).
* The property: **tooltip** does not have an effect. Do not use it.
* The property: **alternateRowColors** displays the rows with alternating background colors (“banded rows”). Do not use it.

sap.m.Column

The following additional properties are available for sap.m.Column:

- The property: **width** defines the width of the column in all units allowed by HTML, such as em, rem, %, and px.
- The property: **styleClass** is used if you need to change the visual design of a column. Do not use this, but use the default style instead.
- The property: **visible** shows or hides the column.
- The property: **tooltip** does not have an effect. Do not use it.

sap.m.ColumnListItem

The following additional properties are available for sap.m.ColumnListItem:

- The property: **selected** allows an item to be selected programmatically.
- The property: **counter** does not have any effect. Do not use it.
- Do not use the property: **busy**.
- Do not use the property: **busyIndicatorDelay**.
- The property: **visible** shows or hides the item.
- The property: **tooltip** adds a tooltip to a whole row. The tooltip is only shown on mouse interaction. It will not work on tablets or smartphones. Do not use it.

## Resources


#### Elements and Controls                                                                                                                                               | #### Implementation                                                                         | #### Visual Design
- [Analytical Table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/) (guidelines)                     | - [Responsive Table](https://ui5.sap.com/#/entity/sap.m.Table) (SAPUI5 samples)             | - [Responsive Table](https://wiki.one.int.sap/wiki/display/visualcore/ResponsiveTable\+%28Horizon%29\+-\+Specification) (visual design specification)
- Feed List Item (guidelines)                                                | - [Column](https://ui5.sap.com/#/entity/sap.m.Column) (SAPUI5 samples)
- [Footer Toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/footer-toolbar/) (guidelines)                             | - [Column List Item](https://ui5.sap.com/#/entity/sap.m.ColumnListItem) (SAPUI5 samples)
- [Grid Table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/) (guidelines)                                     | - [Responsive Table](https://ui5.sap.com/#/api/sap.m.Table) (SAPUI5 API reference)
- Object Identifier (guidelines)                                      | - [Column](https://ui5.sap.com/#/api/sap.m.Column) (SAPUI5 API reference)
- Object Number (guidelines)                                                | - [Column List Item](https://ui5.sap.com/#/api/sap.m.ColumnListItem) (SAPUI5 API reference)
- [Table Personalization Dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-personalization-dialog/) (guidelines) |
- [Table Toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/) (guidelines)                                   |
- [Tree Table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tree-table/) (guidelines)                                     |
- [Variant Management](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/) (guidelines)                     |
- [View Settings Dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/view-settings-dialog/) (guidelines)                 |
**Columns (external_only)**

#### Elements and Controls                                                                                                                                               | #### Implementation
- [Analytical Table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/) (guidelines)                     | - [Responsive Table](https://ui5.sap.com/#/entity/sap.m.Table) (SAPUI5 samples)
- Feed List Item (guidelines)                                                | - [Column](https://ui5.sap.com/#/entity/sap.m.Column) (SAPUI5 samples)
- [Footer Toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/footer-toolbar/) (guidelines)                             | - [Column List Item](https://ui5.sap.com/#/entity/sap.m.ColumnListItem) (SAPUI5 samples)
- [Grid Table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/) (guidelines)                                     | - [Responsive Table](https://ui5.sap.com/#/api/sap.m.Table) (SAPUI5 API reference)
- Object Identifier (guidelines)                                      | - [Column](https://ui5.sap.com/#/api/sap.m.Column) (SAPUI5 API reference)
- Object Number (guidelines)                                                | - [Column List Item](https://ui5.sap.com/#/api/sap.m.ColumnListItem) (SAPUI5 API reference)
- [Table Personalization Dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-personalization-dialog/) (guidelines) |
- [Table Toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/) (guidelines)                                   |
- [Tree Table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tree-table/) (guidelines)                                     |
- [Variant Management](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/) (guidelines)                     |
- [View Settings Dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/view-settings-dialog/) (guidelines)                 |

---

## upload-set-with-table-plugin

The upload set with table plugin allows users to upload a single file, multiple files, or a directory of files from a device (desktop, tablet, or phone) to an SAP Fiori app.

Despite its name, the upload set with table plugin is not limited to upload scenarios. You can also use it for cases where users can only download files uploaded by other users, due to the context or access rights.

The successor to the upload set control, the upload set with table plugin is enhanced with new features. While the upload set control was designed for the list UI control, the upload set with table plugin was designed to work with the table control.

This plugin can be connected to tables, such as the [grid table](https://www.sap.com/design-system/fiori-design-web/ui-elements/grid-table/), the [responsive table](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/), or the Meta Driven Controls (MDC) table.

**> **Information:** **

For more information, see:
- [MDC table](https://sapui5.hana.ondemand.com/#/entity/sap.ui.mdc.Table) (SAPUI5 samples)
- [MDC table](https://sapui5.hana.ondemand.com/#/api/sap.ui.mdc.valuehelp.content.MDCTable) (SAPUI5 API reference)

*Upload set plugin in a responsive table*

## When to Use

Do
Use the upload set with table plugin:
- To show uploaded files in a table row that can be modified.
- To allow users to add or remove several files, and to change the  | - Instead, use the `sap.ui.unified.FileUploader` control.
file names
- To replace an older or deprecated control:
- `sap.ca.ui.FileUpload`
- `sap.m.UploadCollection` (deprecated since SAPUI5 version 1.88.
- `sap.m.upload.UploadSet`
## Upload Actions

The plugin offers the following upload actions:
- *Upload* for uploading files from the local file system
- *Upload from Cloud* for uploading files from the
connected cloud workspace account
### Additional Actions
Additionally, you can provide an action to:
- Download a file
- Rename a file
- Add a URL: The URL is used to create the file
**> **Hint:** **

You implement the additional actions with the following public APIs:
- [Download a file](https://sapui5.hana.ondemand.com/#/api/sap.m.plugins.UploadSetwithTable%23methods/download)
- [Rename a file](https://sapui5.hana.ondemand.com/#/api/sap.m.plugins.UploadSetwithTable%23methods/renameItem)
- [<u>Upload a file without content</u>](https://sapui5.hana.ondemand.com/#/api/sap.m.plugins.UploadSetwithTable%23methods/uploadItemWithoutFile)
- [<u>Upload a file via a URL</u>](https://sapui5.hana.ondemand.com/#/api/sap.m.plugins.UploadSetwithTable%23methods/uploadItemViaUrl)

## File Preview

Users can preview uploaded files with a specialized file preview dialog control that displays the file content.
The plugin supports the preview for only specific file types listed in the [FilePreviewDialog](https://sapui5.hana.ondemand.com/#/api/sap.m.upload.FilePreviewDialog) (SAP UI5 API reference).

## Behavior and Interaction

### Uploading Files

The users drop files onto the table area or they click the *OK* button in the file selection dialog.

Depending on the working mode that the application development team uses for the upload set, the user experience differs slightly:

- With the **default** working mode, instant upload, the files are uploaded immediately.
- With the working mode, manual upload with item validation, a dialog is displayed with the files that the users selected. In the dialog, users can confirm or cancel the upload and:
  - Browse for additional files to upload
  - Select the type for the documents that they are uploading
  - Delete the items selected for upload

If some users are allowed only to download the files that others have uploaded, you can disable the upload option.

The upload set with table plugin allows you to use a custom uploader, unlike the deprecated upload collection control,

**> **Hint:** **

You implement the additional actions with the following public APIs:
- The default working mode is instant upload.
- For manual upload, where the users trigger the upload explicitly and with item validation callback, configure the `itemValidationHandler`. The selected files are uploaded only after a promise from the callback is resolved.
- The Boolean property, `uploadEnabled `controls whether or not users can upload files.

#### Empty State

If the table is empty, the plugin provides an [illustrated message](https://www.sap.com/design-system/fiori-design-web/ui-elements/illustrated-message/) that tells the users to upload files by dragging and dropping them into a large zone in the table area or by using the *Upload* button.

*Table with an empty state*

#### Drag and Drop

To start the upload, users can select one or more files from their computer and drag them onto the table’s drop area. The same process is used as the one for the *Upload* button.

*Dragging a file into a table*

### Previewing Files

To preview files, users click the file name of the attachment. The preview opens in a dialog.

When necessary, on mobile devices, a dialog opens where users can select an app that supports the respective file type, such as \*.doc or \*.pptx.

**> **Hint:** **

The API openFilePreview integration or configuration is essential for previewing files. For example, the openFilePreview API is invoked when the file name is
clicked.
For more information, see the [openFilePreview](https://sapui5.hana.ondemand.com/#/api/sap.m.plugins.UploadSetwithTable%23methods/openFilePreview) API reference.

### Renaming Files

The *Rename* action works identically on desktop and mobile devices.
The action is enabled when the user selects an entry from the table.
It opens the *Rename Document* dialog.
### Adding a URL

The users can upload a file using a URL, rather than a
file. The URL is then used to create the file.
*Add a URL dialog*

**> **Hint:** **

- The API `uploadItemViaUrl` returns a promise that initiates an upload when it is resolved.

---

