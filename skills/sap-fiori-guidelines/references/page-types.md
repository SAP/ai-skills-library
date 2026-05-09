# SAP Fiori Page Types and Floorplans

## Floorplans > Analytical List Page > Usage

> **Information:** This floorplan is implemented with [SAP Fiori Elements](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements).
To explore the design capabilities of SAP Fiori elements for OData V4 and experiment with their behavior, see [Analytical List Report](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/floorplanListReport/analyticalListReport) in the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## Intro

*Analytical list page*

The analytical list page (ALP) offers a unique way to analyze data step by step from different perspectives, to investigate a root cause through drilldown, and to act on transactional content. All this can be done seamlessly within one page. The purpose of the analytical list page is to identify interesting areas within datasets or significant single instances using data visualization and business intelligence.

Visualizations help users to recognize facts and situations, and reduce the number of interaction steps needed to gain insights or to identify significant single instances. Chart visualization increases the joy of use, and enables users to spot relevant data more quickly.

The main target group are users who work on transactional content. They benefit from fully transparent business object data and direct access to business actions. In addition, they have access to analytical views and functions without having to switch between systems. These include KPIs, a visual filter where filter values are enriched by measures and visualizations, and a combined table/chart view with drill-in capabilities (hybrid view). Users can interact with the chart to dig deep into the data. The visualization enables them to identify spikes, deviations and abnormalities more quickly, and to take appropriate action right away.

## Usage

### Use the analytical list page if:

- Users need to extract key information to understand the current situation or identify a root cause. The way the data is presented is crucial for giving them the insights they need to take the right action.
- Users need a way to analyze data step by step from different perspectives, investigate a root cause through drilldown, and act on transactional content within one page.
- In addition to the filtered dataset, users need to see the impact of their filter settings in a chart (visual filter).
- Users need to switch between integrated chart and table views (hybrid view).
- Users need to see the impact of their action on a key performance indicator (KPI).
- Users need to find and act on relevant items out of a large set of items by searching, filtering, sorting, grouping, drilling down, and slicing and dicing.

### Do not use the analytical list page if:

- Drilldown is rarely used, not used at all, or is only needed after navigating to another page, rather than as free or flexible drilldown within the page itself. In this case, a [list report](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/) might be sufficient for your use case.
- Users need different visualizations for the entire dataset (for example, as a [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) or [chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/smart-chart/)), but don’t need to work with both visualizations on the same page (for example, in a reporting scenario). In this case, a list report might be sufficient.
- Users need to find and act on relevant items from within a large set of items by searching, filtering, sorting, and grouping, without using drilldown or “slice and dice”. In this case, consider using a [list report](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/).
- Users need to work with multiple views of the same content, for example on items that are “Open”, “In Process”, or “Completed”. They want to be able to switch views using tabs, segmented buttons, or a select control. In this case, consider using a [list report](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/).
- Users need to see or edit a single item with all its details. Use the [object page floorplan](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/) instead.
- Users need to find a specific item, and the item or an identifying data point is known to the user (such as a code). In this case, use the [initial page floorplan](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/initial-page-floorplan/).
- Users need to work through a comparably small set of items, one by one. In this case, use the [worklist floorplan](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/work-list/).
- Users have a trivial use case that does require the use of a chart, but that do not involve identifying a root cause, analyzing data, or drilldown. Instead, use a [list report](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/) with a table/chart switch.

## Structure

This section describes the basic layout of the analytical list page, as well as the different layout variants.

### Basic Layout

The [shell bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/shell-bar/) is above the analytical list page. The page itself uses the [dynamic page layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/) and has two main areas:
1. **[Analytical list page header](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/#analytical-list-page-header)**:
The page header is the filter area. Users can expand and collapse the header using the [expand/collapse header icon](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#expandcollapse-header-feature).
2. **[Analytical list page content area](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/#analytical-list-page-content-area)**:
The content area shows the content for the chosen filters.
All elements are described in more detail in the [Components](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/#components) section below.
### Layout Variants

The layout of the analytical list page is quite flexible. The display is determined by the header and content views chosen by the user.

- In the expanded page header, users can switch between the [visual filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/visual-filter-bar/) and the [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/) using the [filter type switch](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/page-types/floorplans/analytical-list-page/#filter-type-switch).
- In the content area, users can switch between a [hybrid view](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/#hybrid-view) (chart and table), a [chart-only view](#chart-only-view), or a [table-only view](#table-only-view) using the view switch.

**The analytical list page always offers all of the above layout options.** You cannot restrict the available views at app level. For example, you can’t offer only a visual filter (with no option to show the standard filter bar). Likewise, you can’t show only a table view (with no option to display the hybrid or chart views).

> **Information:** SAP Fiori elements for OData V4 uses the [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/) and SAP Fiori elements for OData V2 uses the [smart filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/smart-filter-bar-annotations/).

## Responsiveness

The analytical list page is responsive, except for the [KPIs](https://main--builder-prospect-prod--sapudex.aem.page/design-system/fiori-design-web/v1-136/page-types/floorplans/analytical-list-page/usage-edited#kpi-tags-and-cards). Apps with one or more KPIs are not supported on screen sizes smaller than size L (desktop).

Likewise, the analytical list page is only fully supported in the flexible column layout if no KPIs are used. If you use the analytical list page with KPIs within the flexible column layout, the column should have at least size M.

### Size S
On size S, the analytical list page supports both the chart-only and table-only views. The table-only view supports only the [responsive table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/). If no responsive table is available, the chart-only view is displayed without a view switch toggle.
KPIs are not supported on size S.
*Chart-only view - Size S*          | *Table-only view - Size S*          | *Chart-only view - Size M*          | *Table-only view - Size M*
## Components

### Analytical List Page Header

The page header can be expanded and collapsed on click. Different content is shown in the expanded and collapsed states. For more information about the basic behavior of the header, see [Dynamic Page Header](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#dynamic-page-header).

#### Collapsed Header

*Collapsed analytical list page header*

The collapsed page header contains the following elements:
- [Variant management](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/#variant-management) (serves as page variant) (mandatory)
- [Key performance indicator tags](https://main--builder-prospect-prod--sapudex.aem.page/design-system/fiori-design-web/v1-136/page-types/floorplans/analytical-list-page/usage-edited#kpi-tags-and-cards) (=KPI tags) (optional)
- [Key performance indicator cards](https://main--builder-prospect-prod--sapudex.aem.page/design-system/fiori-design-web/v1-136/page-types/floorplans/analytical-list-page/usage-edited#kpi-tags-and-cards) (=KPI cards) (optional)
- [Filter dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/#filter-dialog) via the *Adapt Filters* *(x)* link. Visible only in live mode. (mandatory)
- [Header toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/header-toolbar/) with global actions (optional)
- Summary of applied filters as follows:
- Either *1 filter active:* or *\<n> filters active:*, where “n” stands for the number of applied filters.
- A comma-separated list of the currently applied filters for up to five filters. If there are more, an ellipsis (…) shows at the end of the string.
Or, if no filters have been applied, the summary text is: *No filters active*
#### Expanded Header

Initially when the app is launched the header is expanded by default. The expanded page header contains the following elements:
- [Variant management](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/#variant-management) (serves as page variant) (mandatory)
- [Key performance indicator tags](https://main--builder-prospect-prod--sapudex.aem.page/design-system/fiori-design-web/v1-136/page-types/floorplans/analytical-list-page/usage-edited#kpi-tags-and-cards) (=KPI tags) (optional)
- [Key performance indicator cards](https://main--builder-prospect-prod--sapudex.aem.page/design-system/fiori-design-web/v1-136/page-types/floorplans/analytical-list-page/usage-edited#kpi-tags-and-cards) (=KPI cards) (optional)
- [Filter dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/#filter-dialog) via the *Adapt Filters* *(x)* link (mandatory)
- [Header toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/header-toolbar/) with global actions (optional)
- [Filter area](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/#filter-area-visual-filter-bar-and-filter-bar), including the [visual filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/#visual-filter-bar) and [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/) (mandatory)
- [Filter type switch](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/#filter-type-switch) ( :filter-fields: \| :filter-analytics: ) (mandatory)
### Analytical List Page Content Area

The [analytical list page content area](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/#analytical-list-page-content-area) contains the following elements:
- View switch ( :chart-table-view: \| :vertical-bar-chart: \| :table-view: )

- [Hybrid view](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/#hybrid-view): View with one chart, chart toolbar, one table, and a table toolbar
*Hybrid view*

- [Chart-only view](#chart-only-view): View with one chart and a chart toolbar
*Chart-only view*

- [Table-only view](#table-only-view): View with one table and a table toolbar
*Table-only view*

## Analytical List Page Header

### Variant Management

Variant management in the analytical list page allows users to save a page variant whenever there are changes in the underlying structures
of the filter/content area. Variant management for the page is handled by the standard SAPUI5 page [variant management](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/).
Currently, the page variant captures the following states across the page:
- Filter view switch state: Visual filter bar or filter bar
- Filter set: The filters set in the visual filter bar and filter bar
- Filter selections: Selected values in the visual filter bar and filter bar
- Content view switch state: hybrid view :chart-table-view: , chart-only view :vertical-bar-chart: , or table-only view :table-view:
- Chart and table configurations, such as measures and dimensions used, sort order, or grouping
- Chart drill-down state, based on the current selections (slice & dice)
- Table entry switch state: *Hide* ( :hide: ) or *Show* ( :show: ) selected table records

### KPI Tags and Cards

Use a KPI tag (=key performance indicator tag) if you would like to show a KPI related to the task in hand. The KPI value changes only if an action is executed on the transactional content. For example, the user needs to know the effect of releasing sales orders on a related
KPI, or the effect of posting an accounting document on certain financial KPIs.
*4 KPI tags including KPI labels, KPI values, KPI color, and criticality indicator*
You can display **a maximum of three** KPIs. Clicking a KPI tag opens a [KPI card](https://main--builder-prospect-prod--sapudex.aem.page/design-system/fiori-design-web/v1-136/page-types/floorplans/analytical-list-page/usage-edited#kpi-card) that displays more details on the KPI.
The KPI tags and corresponding KPI cards are **independent of the filter area**. This means that KPI tags do not react to filters set in the visual filter bar and filter bar.
A KPI tag has four components:
- KPI label
- KPI value
- KPI color and criticality indicator
#### KPI Label
The KPI label is an abbreviation of the complete KPI title. It is formed using the first three letters of the first three words of
the KPI title.
Examples: *AMR* for *Actual Monthly Revenue*, *TAR* for *Total Advertising Revenue*, or *LPC* for *Landing Page Conversation Rates*
If there is only one word in the KPI title, the first three letters of the word are displayed. Example: *CON* for *Contracts*
If the KPI title has only two words, only the first letters of these two words are displayed. Examples: *AC* for *Actual Costs*, *SG* for *Sales Growth*
#### KPI Value
The KPI value is displayed using a semantic color and a
scaling factor. Relative values are shown with a
percentage sign and one decimal place.
Examples: 0.3%, 82.9%
Absolute values are shown without decimal places, a
currency, or a unit of measure.
Examples: 2K, 75K, 30M, 14B
#### KPI Color and Criticality Indicator
The color of the KPI value is based on the thresholds
defined for the particular KPI in the annotation. The KPI
tag also uses a line to indicate the criticality. The
color of the line is the same as that of the KPI value.
#### KPI Card

Clicking the KPI tag opens the [analytical card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-card/), which displays more information about the current value of the KPI, the KPI target, the deviation from the target, and how the KPI has evolved over time.
*KPI card*

### Filter Area: Visual Filter Bar and Filter Bar

Default (col-1)

The filter area allows users to filter the result set, which feeds the main content area. The analytical list page comes with two filter types: compact filters in the [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/), and the [visual filter bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/visual-filter-bar/). Always **design both** visual filters and compact filters ([filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/)) for your app. **We recommend setting the visual filter bar as the default,** but this is no longer mandatory. You can opt to use the (compact) [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/) as the default if your app has the required parameter values, if your main use case involves date ranges, or if your users often need to combine multiple filters in different ways.
Currently, any visual filter configured in the visual filter bar must always be displayed as a compact filter in the [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/) as well. By contrast, a filter configured as a compact filter in the filter bar may or may not be configured for display as a visual filter. This means that it’s possible to have a smaller set of visual filters and a larger set of compact filters.
Both filter types supports two different modes: **live update** and **manual update**. Use the **live update mode** for both filter types **as the default** whenever possible. Apply the same mode to both filter types: the [visual filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/visual-filter-bar/) and the [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/). For example, if you use the live update mode in the visual filter bar, you should also use the live update mode for the filter bar.

> **Information, Col-1:** SAP Fiori elements for OData V4 uses the [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/) and SAP Fiori elements for OData V2 uses the [smart filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/smart-filter-bar-annotations/).

Default (col-2)

*Visual filter bar*
*Filter bar*

Section Metadata

style

### Filter Type Switch

Users can toggle between the compact filters :filter-fields: ([filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/)) and :filter-analytics: ([visual filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/visual-filter-bar/)) in the upper-right area of the page header. The filter type switch is a core feature of the analytical list page and is **mandatory**. The switch is only displayed when the page header is expanded. Once the header collapses, it disappears.
*Filter type switch*

#### Carrying Forward Filter Selections

*Visual Filter to Compact Filter*

Any values selected in the visual filters are always carried forward to the corresponding compact filters.

*Compact Filter to Visual Filter*

Filter dimensions that are part of a visual filter are synced to the visual filter. If the dimension value(s) chosen in the compact filter are part of a visual filter, they are shown as selected chart dimensions in the visual filter (single or multiple selections).

Filter dimensions that are not part of the visual filter, parameter values, and interval-based dimensions are applied to the filter query and the content is refreshed.

To show complex conditions, click the link for the number of selected items at the top of the visual filter.

### Visual Filter Bar

The visual filter bar combines measures or item counts with filter values. The visual filter bar becomes more powerful if you match measures to the filter dimension instead of just item counts. Use the visual filter bar if you would like to give the user a condensed overview of the data in the dataset. Chart visualization increases the joy of use, and enables users to spot relevant data more quickly.

#### Chart Types in the Visual Filter Bar

Currently, the visual filter bar supports three [interactive chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/interactive-chart/) types:

- [Interactive donut chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/interactive-donut-chart/)
- [Interactive line chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/interactive-line-chart/)
- [Interactive bar chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/interactive-bar-chart/)

These interactive charts are also referred to as *visual filters.*

#### Interactive Donut Chart                                                                                                                        |
The [interactive donut chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/interactive-donut-chart/) | *Interactive donut chart*           | *Interactive donut chart with semantic colors*
in the visual filter bar is used for non-time-related data (for example, categories) and displays only the top or bottom two values. The rest are   |
aggregated into the “Other” section.                                                                                                                |
#### Interactive Line Chart                                                                                                                                                                                                                                                                                                                                                       |
The [interactive line chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/interactive-line-chart/) is used **exclusively** for displaying **time series data**, and can show a maximum of six data points. Always show the first or last six data points (for example, last six days, last six months, first six days, and so on). | *Interactive line chart*           | *Interactive line chart with semantic colors*

#### Interactive Bar Chart                                                                                                                      |
The [interactive bar chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/interactive-bar-chart/) | *Interactive bar chart*           | *Interactive bar chart with semantic colors*
can be used for non-time-related data (for example, categories) and has a maximum of three filter values. These filter values show the top      |
three or bottom three entries.                                                                                                                  |
#### Using Interactive Charts

The interactive charts come with the following features and rules:

- **Minimum number of interactive charts**: Show at least three visual filters and try to use different chart types.
- **Filter title:**
  - Use the following naming convention for the filter title, using title case:
[Measure Name] by [Dimension Name]
    *Examples:*
Project Costs by Project
Sales Volume by Commodity
  - For an item count, use the following naming convention for the filter title, using title case:
Number of [Dimension]
    *Examples:*
Number of Products
    Number of Contracts by Month
  - Note that for some use cases, it might be appropriate to replace “Number” with a different expression. Bear in mind that the space for displaying the filter title is limited. If the measure and/or dimension names are longer than the predefined space, the text will be truncated. 
*Filter title with truncation*

- **Filter-to-filter dependencies:** Ideally, the filters depend on each other. By selecting one or several chart data points, users can perform a quick analysis of the dataset.
  Examples: Supplier with the lowest supplier performance this year, product with the highest sales volume in March in the EMEA region
- **Adding additional filter values:** All charts have a maximum number of filter values that can be displayed within the chart itself. More filter values can be selected using the [value help](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/value-help-dialog/) or the select popover.
- **Selected values:** Any data point or segment that is selected in the visual filter’s interactive charts will remain selected even when the user changes the measure, chart type, or sort order in any of the charts. If a selected record falls outside the top/bottom three records being displayed, the number of selected records is shown in parentheses at the top right of the chart.
- **Semantic colouring**: All interactive charts support semantic colors to indicate the criticality of filter values.
- **How to design a visual filter:** To design a visual filter, choose a meaningful measure out of the dataset and match it to a filter dimension. If no measures or no meaningful measures are available, use an item count instead. Have a look at the [visual filter bar article](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/visual-filter-bar/) for more information.

### Filter Dialog

In the filter dialog, the user can switch between the visual filter bar and the compact filters using a toggle button, and also manage the filters. For more about the standard filter dialog, see [Filter Bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/#filter-dialog). Visual filters are explained in more detail below.

#### Filter Dialog for Visual Filters

The filter dialog is launched by clicking the *Adapt Filters ([number of applied filters])* link in the page header area. In the filter dialog for visual filters, the user can choose which filter fields are shown in the visual filter bar, and make the following changes:

- Add visual filters
- Delete visual filters
- Hide visual filters in the visual filter bar
- Search for visual filters
- Change the sort order :sort-descending: of each visual filter
- Change the chart type :horizontal-bar-chart-2: of each visual filter
- Switch to other measures :measure: in the visual filter display

## Analytical List Page Content Area

The content area shows different visualizations of the selected data. In the hybrid view, users can interact with both the chart and table visualizations at the same time. In addition, the analytical list page supports a chart-only view and a table-only view. The analytical list page **always** comes with **all three views**. Offering additional views or even tabs would add too much complexity, and is neither supported nor recommended.

Check out the following sections for more details on the hybrid view, chart-only view, and table-only view.

#### Hybrid View

The hybrid view uses both chart and table visualizations at the same time. It enables users to analyze data step by step from
different perspectives. Users can interact with both the chart and the table, and drill down through either the [smart chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/smart-chart/)
or table entries to investigate a root cause. They can also act directly on transactional content. In the initial view of the
chart, **visualize the most important aspects of the whole dataset** in the chart.
**Example:** The view shows all the suppliers the user is responsible for, organized by value. By drilling down the material to
the plant with the highest/lowest volume, the user can see if materials need to be shifted from one plant to another. The
corresponding transactional data is shown in an analytical table below the chart, which might also offer an action for shifting
the material.
#### Chart-Only View

The chart-only view enables users to analyze data step by step from different perspectives, and to investigate a root cause through drilldown,
without direct access to transactional content. The [smart chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/smart-chart/)
control provides the chart visualization in the chart-only and hybrid views: it is used to display the dataset as a chart. The smart chart
drilldown functionality provides a convenient way to analyze the dataset. In addition, the smart chart offers detailed information on the chart
data and a breadcrumb that shows the drilldown path. Ensure that you **show the most important aspects of the dataset** in the chart.
This mode is perfect for applications with analytical data that can easily be represented visually using charts, but doesn’t need to be linked to
the transactional dataset.
#### Table-Only View

The table view provides access to transactional content. The user can act on single or multiple objects, and navigate to the object details or to other applications.
Depending on the use case, you can opt to use either the [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/) or the [responsive table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/).
Snapping or scrolling is not available for desktop-focused tables, such as the [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/). Scrolling is only available when the responsive table is used. The pin is enabled by default. The table entries are loaded using lazy loading.
Users can apply filters at table level using the *Settings* button (:action-settings: ). For analytical tables, filtering is also available at column level. For more information, see [Analytical Table (ALV) – Filter](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/#filter).
## Behavior and Interaction

The expand/collapse header and pin/unpin header features work as in the [dynamic page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#behavior-and-interaction).

### Initial Focus

When the analytical list page is loaded, set the initial focus as follows:

- If the compact filter is visible by default, set the focus on the first filter field (for live update mode) or on the *Go* button (for manual update mode).
- If the header contains empty mandatory fields, set the focus on the first empty mandatory field.
- If the visual filter bar is visible by default, set the focus on the first chart container.
- If the header is collapsed (visual or compact filter), set the focus on the first chart data point or the first table row (depending on the selected view).

### Open and View the KPI Card via the KPI Tag

Clicking a KPI tag opens the KPI card, which shows the details for the particular KPI.

### Select Filters in the Visual Filter

Unlike [micro charts](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/micro-chart/), the visual filter charts are interactive. In live search mode, selecting a filter value triggers data filtering in the content area. Both single and multiple selection are supported.

To select a filter value, the user clicks on a value in the chart. The filter can be removed by either clicking on the value help link, or by clicking on the same value in the chart again. The user can [select](https://www.sap.com/design-system/fiori-design-web/ui-elements/visual-filter-bar/#selecting-filters) more filter values using the [value help](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/value-help-dialog/) or select popover.

Any data point that is selected in a chart still remains selected when the user selects a data point in another chart. Filter values react on each other. If a selected record falls outside the top/bottom three records being displayed, the number of selected records is shown in parentheses at the top right of the chart.

### Switch Views: Hybrid, Chart-Only, and Table-Only

Users can switch between the hybrid view, chart-only view, and table-only view.

If the user selects values and then switches the view, the selection remains intact. See the table below for more details.

Table

Switch

Hybrid view to table view

Hybrid view to chart view

Chart view to hybrid view
selections are displayed

Table view to hybrid view

### Show/Hide Table Entries in Hybrid View and Table View

The table toolbar for the analytical list page offers a *Show* :show: and *Hide* :hide: table entries feature as a toggle switch in the hybrid and table views:

- If the ***Show*** **icon** is active, the table shows all items. These include highlighted entries (where values are selected in the chart) and non-highlighted entries.
- If the ***Hide*** **icon** is active, the table shows only items that are selected in the chart.

For example, if the user selects *SAP’s Sales Revenue for 2012* as *Customer* in the chart, all records relating to *SAP’s Sales Revenue for 2012* are highlighted (but not selected) in the table. Note that the record is still highlighted even if *Customer* not displayed as a column in the table. If the table rows are grouped, the entire grouping is highlighted, even if only one record within the grouped set is affected by the chart selection. All values that are not selected in the chart are “hidden” and are not shown in this table mode.

## Guidelines

#### Show the filter dimension with one measure in the visual filter, not multiple measures

Filter dimensions in the compact filters ([filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/)) have **exactly one** representation in the visual filter bar.
Do not show the same filter dimension with two or more different measures at the same time in the visual filter bar. The example shows the filter Dimension *Year* with two different measures *Revenue* and *Quantity*. Showing the filter dimension *Year* twice is not in sync with the compact filter, where it is shown only once. Furthermore, matching between the two filter types will not work.

If the use case requires you to show a dimension with different measures, consider using an [overview page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page/) instead.

Do
*For each dimension display exactly one representation in the visual filter bar.*

### 
### Tips for Design Gates

#### Filter Area

- Always configure both a visual filter bar and a compact filter bar.
- It is preferable to use the visual filter as the default, but not mandatory. Consider using the compact filter bar as the default if:
  - Parameter values are required
  - Data range selection is the main use case
  - Users often need a large set of filters
- Use the live search as the default for both filter types (except when parameter values are required).
- Every visual filter must have a corresponding compact filter, but not all compact filters need a corresponding visual filter.
- Filter dimensions in the compact filter bar have exactly one representation in the visual filter.

#### Visual Filter Bar

- Always use a line chart to show a time series. Do not use a line chart to show categories; use a bar chart instead.
- If you expect the user to work with a large number of datasets, consider using the bar chart.
- If your scenario involves filtering a small number of datasets by parts of a whole, consider using the donut chart.
- If your scenario involves filtering 200 or more filter values, consider using value help. For filtering less than 200 values, we recommend using the select popover.
- Use the following naming convention for the filter title, using title case: [Measure Name] by [Dimension Name] in [Scaling Factor] [Unit of Measure]. For example, *Project Costs by Project in K EUR, Sales Volume by Commodity in M PC.*
- **It is mandatory** that all visual filters are connected and react to each other. If a user interacts with a certain visual filter, the others must react to the selection.

#### Hybrid View / Chart-Only View

- Show the most important aspects of the dataset in the main chart.

#### Tabs

- Do not use tabs in the analytical list page.

## Resources


#### Elements and Controls                                                                                                                                     | #### Implementation
- [Visual Filter Bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/visual-filter-bar/) (guidelines)             | - SAP Fiori Elements Feature Map (internal)
- [Analytical Card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-card/) (guidelines)                 | - Analytical List Page (developer guide)
- [Interactive Charts](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/interactive-chart/) (guidelines)            |
- [Interactive Bar Chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/interactive-bar-chart/) (guidelines)     |
- [Interactive Donut Chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/interactive-donut-chart/) (guidelines) |
- [Interactive Line Chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/interactive-line-chart/) (guidelines)                                |
- [Value Help Dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/value-help-dialog/) (guidelines)                                          |
- [Smart Chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/smart-chart/) (guidelines)                         |
- [Smart Table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/smart-table/) (guidelines)                         |
- [Analytical Table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/) (guidelines)           |
- [Responsive Table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/) (guidelines)               |
**Columns (external_only)**

#### Elements and Controls                                                                                                                                     | #### Implementation
- [Visual Filter Bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/visual-filter-bar/) (guidelines)             | - SAP Fiori Elements Feature Map (internal)
- [Analytical Card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-card/) (guidelines)                 | - Analytical List Page (developer guide)
- [Interactive Charts](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/interactive-chart/) (guidelines)            |
- [Interactive Bar Chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/interactive-bar-chart/) (guidelines)     |
- [Interactive Donut Chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/interactive-donut-chart/) (guidelines) |
- [Interactive Line Chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/interactive-line-chart/) (guidelines)                                |
- [Value Help Dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/value-help-dialog/) (guidelines)                                          |
- [Smart Chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/smart-chart/) (guidelines)                         |
- [Smart Table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/smart-table/) (guidelines)                         |
- [Analytical Table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/) (guidelines)           |
- [Responsive Table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/) (guidelines)               |

---

## Floorplans > List Report Floorplan Sap Fiori Element > Usage

> **Information:** This floorplan is available with [SAP Fiori Elements](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements).
For more information, see the topics for the list report [header](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/list-report/list-report-header-sap-fiori-elements) and [content area](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/list-report/list-report-content-area-fiori-elements) in the *SAP Fiori Elements* section.
To explore the design capabilities of SAP Fiori elements for OData V4 and experiment with their behavior, see [List Report Page](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/floorplanListReport/simpleListReport) in the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## Intro

With a list report, users can view and work with a large set of items. This floorplan offers powerful features for finding and acting on relevant items. It is often used as an entry point for navigating to the item details, which are usually shown on an [object page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/).

*List report*

## When to Use

### Use the list report floorplan if:

- Users need to find and act on relevant items within a large set of items by searching, filtering, sorting, and grouping.
- You want to let users display the whole dataset using different visualizations (for example, as a table or as a chart), but no interactions are required between these visualizations. An example use case might be reporting.
- Users need to work with multiple views of the same content, for example on items that are “Open”, “In Process”, or “Completed”. You want to let users switch views using tabs, segmented buttons, or a select control.
- Drilldown is rarely or never used, or is only available via navigation to another page, and not as free or flexible drilldown within the page itself.
- Users work on different kinds of items.

### Do not use the list report floorplan if:

- Users need to see or edit one item with all its details. Use the [object page floorplan](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/) instead.
- Users need to find one specific item, and the item or an identifying data point is known to the user (such as a code). Use the [initial page floorplan](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/initial-page-floorplan/) instead.
- Users need to work through a comparably small set of items, one by one. Use the [worklist floorplan](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/work-list/) instead.
- Users need to extract knowledge or insights from data, either to better understand the current situation, or to identify the root cause for a certain value. Use the [analytical list page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/) instead.
- Charts are not only used for visualization. Users need to switch between integrated chart and table views (hybrid view). Use the [analytical list page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/) instead.
- Users need to see the impact of their action on a KPI. Use the [analytical list page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/) instead.
- Users need to see not only the result, but also the impact of their filter settings directly in a chart representation. Use the [analytical list page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/) instead.

## Components

The list report is a full screen floorplan. It can also be used in [flexible column layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout/), where it is usually displayed in the first column.

The list report page is based on the [dynamic page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/), and is divided into a header area and a content area, as defined by the dynamic page layout.

*Schematic visualization of a list report*

- The **dynamic page header (1)** contains the header title **(2)** and the expandable/collapsible header content (5).
  - The **header title (2)** is part of the header area and should display a **[title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/title/)** or **[variant](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/) (3)** for the whole page (mandatory), filter information (if the header is collapsed), and a [header toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/header-toolbar/) **(4)** with global actions, such as *Share* (optional).
  - The **header content (5)** is used to display the [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/) or the smart filter bar (mandatory).
  - The **[header features](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#header-features) (6)** allow users to expand/collapse the header **(6a)** (mandatory) and pin/unpin the header area **(6b)**.
- The **content area (7)** is used to display:
  - A table/chart title, textual [icon tab bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/icontabbar/#text-only), or select **(8)** (optional)
  - One [table/chart toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/) **(9)** per tab
  - One or multiple [tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) and/or [charts](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/) **(10)**. You can use any kind of table. If you use a chart, you can display the chart on its own (without a table) or as an additional view for an existing table (switchable).
- The **footer toolbar (11)**: If needed, use a [footer toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/footer-toolbar/) to display the [messaging button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/message-popover/) and finalizing actions.

## Behavior and Interaction

### Initial Focus

When the list report is loaded, set the initial focus as follows:

- If the header is expanded, set the focus on the first filter field (live update mode) or on the *Go* button (manual update mode).
- If the header contains empty mandatory fields, set the focus on the first empty mandatory field.
- If the header is collapsed, set the focus on the first table row.

### Standard Naming Conventions

For all objects, follow the standard conventions for action buttons, the object name, and the title in the shell bar. For more information see:

- [Object Handling – Naming Guidelines](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/manage-objects#naming-guidelines)
- [Launchpad Shell Bar – Page Title and Navigation Menu](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/shell-bar/#page-title-and-navigation-menu)

### Header Title

#### Variant Management

[Variant management](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/) is optional. If you use variants, we recommend using one variant management control for the whole page. Use the variants to save and restore all settings for [filters](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/), selected [tabs](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/icontabbar/), all [tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview), and all [charts](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/).
In some specific cases, you might need to add a second variant at control level. This can be the case when the user needs to change the view settings of a list independently of the page filters. However, the default is to use a single variant management control for the entire page.
Users can choose a default variant, which is selected every time the app is started.
Allow users to choose whether a variant should be executed automatically as soon as it has been selected. Not executing a variant automatically allows the user to add or remove [filters](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/) before the dataset is updated. Provide this option only if the filter bar is in manual update mode. For live updates, this option is not required.
If [variant management](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/) is not needed, show a [title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/title/) that describes the current view instead.
#### Filter Information

Display the summary of filters currently applied only if the header content is collapsed. Use the
following text:
- Either *1 filter active:* or *\<n> filters active:*, where “n” stands for the number of applied filters.
- A comma-separated list of the currently applied filters for up to five filters. If there are more, an
ellipsis (…) shows at the end of the string.
If no filters have been applied, the summary text is: *No filters active*
#### Header Toolbar

Use the header toolbar for non-finalizing global actions, such as *Share*. *Share* opens an [action sheet](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/action-sheet/), which features *Save as Tile* (if the [SAP Fiori launchpad](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/launchpad) is available), *Send Email*, and *Share in SAP Jam* (if SAP Jam is available). Show the *Share* [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) only if it makes sense for your application.
If the content area contains a [grid table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/), an [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/), a [tree table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tree-table/), or any other content with its own scrollbar, display a *Show Filters* / *Hide Filters* [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) for expanding and collapsing the header content.
In addition, offer any other global, non-finalizing actions needed. Hide actions that cannot be used at all (for example, because of access rights). To save space on the [header toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/header-toolbar/), group similar actions using a [menu button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/#menu-button1).
For more information on global actions, see the guidelines for the [header toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/header-toolbar/).
### Header Content

#### Search

The [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/) can contain a [search field](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/search/) (optional). If you use the search field, the content shows only items that match both the search terms and the filter criteria.
The search generally searches across all available columns of the table, regardless of whether or not they are visible. In rare cases, some columns might not be included due to technical constraints. If the search does not apply to multiple columns, do not offer the search field.
#### Filters
Filters are applied to all content, including all [tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) and [charts](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/). To improve performance, consider providing mandatory filter fields and/or default settings for filters.
If the list report loads automatically when the page loads, **ensure that mandatory filter fields always have default values** to avoid error messages.
The [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/) offers two different update modes:
- The live update mode (recommended) triggers filtering immediately whenever a filter setting is changed. If the [search field](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/search/) is used, the search is triggered together with all filter settings with every letter typed.
- The manual update mode displays a *Go* [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/), which triggers the filtering. If the [search field](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/search/) is used, the search is executed together with all filters as soon as the *Go* button is pressed.
Make sure that all [tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) and [charts](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/) in the content area are in a busy state until the new data is available. Also ensure that the content is grayed out as soon as the filter settings do not correspond to the content shown (any table, property: showOverlay). This is usually the case if the content is not yet updated and the *Go* button needs to be triggered.
Use the manual update mode only if you run into performance problems while loading the [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) data.
Regardless of the update mode, make sure that the [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/) and the visible content match: The [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/) must always describe the items that are shown in the content area.
#### Header Content - Expand / Collapse Behavior

Carousel (full-width)

The header content collapses when the user scrolls down the page (except for desktop-centric tables), and expands again when the user scrolls back up (“snap on scroll”). Users can pin the header content to keep it visible. For more information, see [Dynamic Page – Expand/Collapse Header](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#expandcollapse-header-feature).

Exception: The “Snap on scroll” and “pin header” features are not provided if the main content area contains desktop-centric tables ([grid tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/), [analytical tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/), [tree tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tree-table/)) or any other content with its own scrollbar. In these [cases](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#special-case-no-page-scrolling-possible), users need to expand and collapse the header content manually using the *Show Filters / Hide Filters* button.

When starting the application, expand the header content if no query was fired (and the table is therefore empty). Otherwise, collapse the header content.

### Content Area

#### General Layout

There are three basic list report layouts: *simple content*, *multiple views*, and *multiple content*. These are described in more detail below.

*Simple Content*

In most cases, the content consists of just a [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/) and a [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview). If needed, provide an option to switch between the [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) and a corresponding [chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/) view.

*Multiple Views*
For more complex scenarios, provide multiple views of the same content. Multiple views involve one or more of the following:
- Showing the same [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview), but with different columns.
- Showing the same [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) in different pre-filtered states. These states are usually based on a status column, for example, items that are *Open*, *In Process*, or *Closed*. Make sure that the corresponding filter is not offered on the [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/).
- Differentiating between the items displayed in the content in some other fundamental way.
There are two options for switching between different views:
The first option is to replace the table [title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/title/) with a content switch. Use this approach if all views share the same sort and group states, as well as the same actions.
The content switch can be:
- A [segmented button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) for up to three views
- A [select control](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/select/) for more than three views, or if the number of views changes dynamically
If you have both a [table title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/title/) and a content switch, display the [table title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/title/) first, then the content switch. Place both on the left side of the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/). Since the content switch is placed on the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/), the same actions are shown for all views.
If you are using the content switch together with [charts](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/), ensure that the [chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/) also reacts to the content switch. This can be done by:
- Filtering the data that influences the display of the [chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/)
- Changing the measures and/or dimensions (for example, *View by Country/Region*, *View by Customer*, …)
The second option for switching views is to show each view in a tab container of the [icon tab bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/icontabbar/). Use this approach if all views show different states of the same data (sort states, group states, as well as item selection). Using tabs also allows you to offer different actions on the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/) for each view.
*Multiple Content*
To support even more complex use cases, a list report floorplan can also contain multiple [tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) that display different kinds of objects. The [filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/) settings are applied to all of these [tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) in parallel. For example, a customer overview list report might display different [tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) for invoices, deliveries, and overdue payments. All of these [tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) can be filtered for a specific customer and a specific date.
Display each [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) inside a tab container of an [icon tab bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/icontabbar/). This also allows you to offer different actions on the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/) for each [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview).
#### Icon Tab Bar
Use the text-only version of the [icon tab bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/icontabbar/). Display the number of items shown in the respective [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) on each tab (sap.m.IconTabFilter, property: count).

#### Table Toolbar
Display at least a table [title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/title/) (ideally with an item count) and icon-only [buttons](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) for sorting, grouping, and column settings. Do not offer additional filter settings on the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/). For sort and group, show a [view settings dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/view-settings-dialog/) with just the corresponding features enabled. For column settings, show the [table personalization dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-personalization-dialog/). If you need more extensive functionality (for example, grouping or sorting on several levels, tables with more than 20 columns), use the [P13n-Dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/p13n-dialog-popup/) with just the corresponding feature enabled.
If alternative visualizations are provided (such as [charts](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/)), offer an additional view switch on the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/). Triggering the switch replaces the current visualization with another one. If a [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) and [chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/) need to be shown in parallel, offer a switch for the combined view.
In rare cases, you can offer an additional layout [variant](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/) on the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/). The layout variant stores view settings like the column order and the sort and group settings. If you use a layout variant, do not store the [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) settings in the filter variant. Offer this additional layout [variant](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/) only if there is a strong use case for switching filter and layout variants independently. If there is no strong use case, or you are unsure, do not use a layout [variant](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/) at all.
*Toolbar with a table title and layout variant*
*Toolbar with additional actions*

In addition, offer any other actions needed. Disable selection-dependent actions (such as *Delete*) if no items are selected, or if the action cannot be applied to the selected items. Always enable selection-independent actions (such as *Add*). To save space on the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/), group similar actions using a [menu button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/#menu-button1). For example: | Do
- *Release* and *Release with Conditions*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | ---
- *Add Contact* and *Replace Contact*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
- *Edit Account* and *Edit Title*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
For more information on table/chart actions, see the guidelines for the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/), the [chart toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart-toolbar/), and for [managing objects](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/manage-objects).                                                       | *Table without the filter icon*
Don't
*Table with a filter option*
#### Table

If there are no items to display, use the “no data” text of the corresponding [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview). Explain why the table is empty, and what the user needs to do to display items.

Examples:

- After starting the app, no filters are applied:
  *To start, set the relevant filters.*
- The filter was executed, but no items were found. This can also happen if the list report was opened by a related app, and the filter criteria were transferred automatically:
  *No data found. Try adjusting the filter settings.*

If you are using a responsive table, always enable “[scroll](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/#scroll) to load” behavior.

#### Sticky Behavior

The icon tab bar, table/chart toolbar, and column headers of all table types must be “sticky”. This means that they stay fixed on top when the user scrolls down the page.

#### Navigation

There are three types of navigation at item level in the list report floorplan:

- **Line item navigation**: If applicable, allow navigation to a detail view (usually an [object page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/)) at line item level. Show a navigation indicator (chevron icon) for each line item that provides a detail view. In a [list](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/list-overview/), [tree](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tree/), or [responsive table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/), clicking the line item triggers the navigation.
  In a [grid table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/), [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/), or [tree table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tree-table/), clicking the navigation indicator triggers the navigation.
  Another option is to use a [link](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/link/) as the identifier for the line item. This [link](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/link/) triggers the navigation. Use this only if the navigation indicator is being used for a different target.
  Only show navigation indicators for target pages the user is authorized to access.
- **Drilldown navigation**: If a line item contains aggregated data, allow navigation to a view that contains details for the aggregated amount. This is usually another list report. In this case, use a [link](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/link/) to display the aggregated amount. If the [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) contains many columns with [links](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/link/), use the [link](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/link/) options to provide different levels of highlighting.
  In [charts](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/), offer the drilldown navigation [link](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/link/) in the popover for the chart element. In this case, also navigate to the corresponding list report to show the details.
- **Cross navigation**: If a line item contains cross-references to other entities, such as people or business objects, use a [link](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/link/) to display the corresponding data point in the [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/overview-table-personalization). Triggering the [link](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/link/) opens a [quick view](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/quickview/). Typically, the [quick view](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/quickview/) displays basic details of the referenced object and a navigation [link](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/link/) to another page (usually an [object page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/)) or another app that shows the object details.

> **Information:** **SAP Fiori Elements – Navigation to Classic UIs** If you need to navigate to classic UIs for create, display, or edit actions, see [Integration of Classic SAP UIs (SAP Fiori Elements List Report)](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/discover/sap-products/sap-s/4hana-only/integration-of-classic-sap-uis-sap-fiori-elements-list-report). This article describes which UI elements and navigation flows to use in different scenarios.

#### Working Modes

When the user edits a list item in a filtered list, the changed item might no longer match the filter criteria. For this use case, there are two alternative working modes:

- **Worklist mode**
- Users want to see a direct system reaction to their changes. Items that don’t match the current filters
- vanish immediately. This mode applies to about 80% of all use cases.
- **Continuous working mode**
- The user still needs the edited item, even though it no longer matches the filter criteria. The item stays in the list until the next filtering process is triggered. The item is marked, and a system message informs the user about the filter mismatch. This mode applies to about 20% of all use cases.

The app developer can choose the appropriate working mode for the app use case.

#### Footer Toolbar
Use the [footer toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/footer-toolbar/) to display the [messaging button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/message-popover/) and finalizing actions. Only use the [footer toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/footer-toolbar/) if finalizing actions for the whole page and/or the [message popover](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/message-popover/) are available.
Always show the [footer toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/footer-toolbar/) in edit mode.
Hide actions that cannot be used at all (for example, if the user doesn’t have authorization). To save space on the [footer toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/footer-toolbar/), group similar actions using a [menu button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/#menu-button1).
For more information on finalizing actions, see the guidelines for the [footer toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/footer-toolbar/).
## Actions

*Places for actions in the list report*

(1) Global actions in the header toolbar
(2) Table actions in the table toolbar
(3) Line item actions
(4) Finalizing actions in the footer toolbar

### 1. Global Actions

Place actions that affect the entire page in the [header toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/header-toolbar/) in the header title (1). These include the following standard actions:

- *Show Filters* / *Hide Filters*: This [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) expands and collapses the header content. Show this [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) only if the list report contains a [grid table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/), [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/), or [tree table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tree-table/).
- *Share*: This [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) opens an [action sheet](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/action-sheet/) that contains actions like *Save as Tile* (if the [SAP Fiori Launchpad](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/launchpad) is available), *Send Email*, and *Share in SAP Jam* (if SAP Jam is available). Show the *Share* [button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/) only if it makes sense for your application.

Hide actions that cannot be used at all (for example, because the user has no authorization). To save space on the [header toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/header-toolbar/), group similar actions using a [menu button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/#menu-button1).

Do not place actions that finalize the current process (“finalizing actions”) on the [header toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/header-toolbar/) of the header title, even if they affect the entire page.

For more information on global actions, see the guidelines for the [header toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/header-toolbar/).

### 2. Table/Chart Actions

Place actions that affect the content of a [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) or [chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/) in the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/) (2).

> **Information:** When you use the [list](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/list-overview/), [tree](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tree/), or [responsive table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/), actions on the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/) move up out of the visible screen area when the user scrolls down.

If you are using an [icon tab bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/icontabbar/), be aware that each tab contains its own table toolbar.

#### When to Enable, Disable, or Hide Actions

Indicate whether an action is available. Some actions are always available (such as *Create* for new objects). Other actions are only relevant if items have been selected (for example, *Edit* at item level, *Remove*, object-specific actions, or actions that change the status of an item).

*Enable* the following actions:

- All *Add/Create* actions, unless the user needs to specify where in the table the new item should be added.
- *Edit* actions that switch the entire table to edit mode (independent of the selected items).
  If the user triggers the *Edit* button, replace it with *Save* and *Cancel* buttons (see [Editing the Whole Table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/#option-2-editing-the-whole-table)).
- Item-dependent actions that can be applied to some or all of the selected items.

*Disable* the following actions:

- Item-dependent actions when no items have been selected.
- *Add/Create* actions where the user needs to specify the insert position in the table, but either no item has been selected, or more than one item has been selected.

*Hide* actions that cannot be used at all (for example, because the user has no authorization).

For more information, also see [UI Element States – Control States](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/ui-element-states#control-states).

**Partial Processing**

Enable the user to apply the changes to as many of the selected items as possible.

If an action can’t be applied to all selected items, show a warning message **before** executing the action:

- Indicate the number of selected items that can’t be processed (out of the total number of selected items).
- Give a reason why the action can’t be applied to these items.
- Let the user choose whether to apply the action to the remaining items anyway or cancel the action.

[See an example here](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/#guidelines).

Note: In some scenarios, you might not be able to identify whether an action can be applied to all selected items before executing it. If the system is unable to apply the action to all items, show a message after executing the action.

##### Sort, Group, Personalization

Decide if you need to provide a sorting, grouping or personalization for your use case. If you offer more than one of these actions, offer them as single actions. We recommend keeping them in the following order: *[Sort](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/#sort-filter-and-group-generic), [Group](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/#sort-filter-and-group-generic), [Personalization](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-46/ui-elements/table-bar/#personalization-generic).*

##### Add/Create Items Using a Dialog

You can let users add or create new items at list report level using a dialog. This approach is recommended for cases where there are fewer than 8 required fields. Display the action in the table toolbar.

You can use this option for both draft and non-draft scenarios.

##### More Information

For more information on table and chart actions, see the guidelines for the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/), [chart toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart-toolbar/), and for [managing objects](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/manage-objects).

### 3. Line Item Actions

In rare cases, actions that affect a single item can be placed directly inside the line item. Use this only for specific, frequently used tasks (3). If the same action can also be applied to several items at once, feel free to also place it on the [table toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/table-bar/). Nevertheless, if you do so, reconsider whether you really need to offer the action at line item level. Examples of line item actions include:

- *Start/Stop* (a batch job)
- *Approve* (an item)
- *Assign* (an item)

Do not disable line item actions. If an action cannot be used, hide it. This can be the case if the user has no authorization or the line item is in the wrong state.

### 4. Finalizing Actions

Place actions that trigger the end of a process and affect the entire page in the [footer toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/footer-toolbar/) (4).

Examples:

- *Save*
- *Cancel*
- *Submit*

Please be aware: Even if you are using the [icon tab bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/icontabbar/), there is only one [footer toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/footer-toolbar/) for all tabs.

Hide actions that cannot be used at all (for example, because the user has no authorization).

For more information on finalizing actions, see the guidelines for the [footer toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/footer-toolbar/).

## Responsiveness

In general, the list report floorplan is responsive. However, there are exceptions if the following controls are used:

- [Grid table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/), [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/), and [tree table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tree-table/) are supported on **desktop and tablet devices only** so you cannot use them for mobile use cases.

Instead, take an [adaptive approach](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/discover/sap-design-system/vision-and-mission/responsiveness-adaptiveness#adaptive-approach):

- - Create a new Fiori application with reduced complexity, not an exact match of the desktop application.
  - With the new application, address the most important use cases for users in a mobile context. The responsive controls ([responsive table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/), [list](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/list-overview/) or [tree](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tree/),) or a relevant control for your use case (for example a [chart](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/) or the [category navigation](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/category-navigation/) pattern) may suffice.
- [Smart table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/smart-table/): The smart table is a wrapper around the different existing [table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview) controls. If a [grid table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/), [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/), or [tree table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tree-table/) is used inside the smart table, you will run into the limitation mentioned above.

For more details, see the respective guideline articles.

*List report - Size L*           | *List report - Size M*           | *List report - Size S*

## Examples

The examples below show variants of the list report with the most commonly-used controls. You can also see the manual update mode (with a “Go” button) and the live update mode (no “Go” button).

Carousel (full-width)

## Top Tips

- Avoid loading list report page without any data, even if there are no mandatory filters.
- Use only one [key identifier](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/object-display-elements/#object-identifier) in the table.
- If you are using the [icon tab bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/icontabbar/), place it beneath the filters.
- In the icon tab bar, use text labels only (without icons).
- Choose [selection controls](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/which-selection-control-to-use) that best fit your use case.
- Make sure that columns in the table are [aligned correctly](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/responsive-table/responsive-table-content-formatting-cheat-sheet/).
- Ensure that mandatory [filter](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/#filters) fields always have default values.
- Avoid using variant management for tables. Use the page variant instead.
- Always enable [actions](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/#when-to-enable-disable-or-hide-actions) like *Add, Create* or *Edit*. Once *Edit* is triggered, replace it with *Save* and *Cancel*.
- Never place finalizing actions in the header toolbar, even if they affect the whole page.
- When using the icon tab bar, be aware that each tab contains its own table toolbar.

---

## Floorplans > Object Page > Usage

> **Information:** This floorplan is available with [SAP Fiori elements](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements).
For information on the default settings and other options for the SAP Fiori element implementation, see the topics for the object page [overview](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-overview-sap-fiori-elements), [header](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements), [content area](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements), and [footer bar](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-footer-bar-sap-fiori-elements) in the *SAP Fiori Elements Framework* section.
To explore the design capabilities of SAP Fiori elements for OData V4 and experiment with their behavior, see [Object Page](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/floorplanObjectPage/simpleObjectPage) in the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## Intro

The object page floorplan is used to display and categorize all relevant information about an object. Categorized content can be accessed quickly using anchor or tab navigation, and users can switch from display to edit mode to change the content. To create a new object, users can switch to create mode.

The object page floorplan comes with a flexible, responsive layout and a [dynamic page header](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/) that can be adapted to display simple and complex business objects. This allows you to adjust the layout to a wide range of use cases.

*Object page floorplan*

> **Warning:** - Always build the object page using the **dynamic page header** and not the former object page header. Using the old object page header creates issues that can’t be fixed retrospectively. Using the dynamic
header will also ensure consistency across all floorplans and provide greater flexibility. For details, see the [Header](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#header) section below.
- **Do not use the current implementation of the “page variant” feature** in SAP Fiori elements. This feature is technically available for object pages, but we are still working on the final design.

## When to Use

### Use the object page floorplan if:

- Users need to display, create, or edit an object.
- Users need to get an overview of an object and interact with different parts of the object.
- You need to structure your content into **different sections**.
- You have a page with one section and editable header content.

Table

### Do not use the object page floorplan if:

- Users need to edit several items at the same time.
- Users need to find relevant items without knowing the exact item details.
- Users need to be guided through a series of steps when a new object is created.
- The creation process for a new object is not linear, but can have different paths, depending
on the information selected.
- Users need to find one specific item, where the item or an identifying data point is known to
the user (such as a code identified by a scanner).
- Users need a way to analyze data step by step from different perspectives. They need to drill
down to investigate a root cause and act on transactional content within one page.
- Users need to interact with interdependent chart and table views (rather than using charts
for visualization only).
- Your content can be shown in just **one section** and you don’t have editable header content.

## Components

The object page consists of the following elements:

- Dynamic page header (mandatory)
- Navigation bar (optional)
- Content area (mandatory)

The image below provides an overview of the object page components.

Default

*Schematic visualization of the object page*

1. Dynamic page header
2. Navigation bar
3. Content area
4. Shell bar
5. Breadcrumbs
6. Global actions
7. Header content
8. Footer toolbar

The following sections explain these components in more detail.

### Dynamic Page Header (mandatory)

The dynamic page header contains key information about the object and provides the user with the necessary context. The header initially expands in display mode. It also contains global actions for the object, such as *Edit* or *Delete*.

The header consists of the following elements:
1. Breadcrumbs (optional)
2. Title (mandatory)
3. Subtitle (optional)
4. Header content (optional)
5. Object marker (optional)
6. [Header toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/header-toolbar/) with global actions (optional)
7. Visual indicator for [header features](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#header-features) (mandatory if the header can be collapsed and expanded)
If the object page is used in the [flexible column layout](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout/), it can also contain layout actions.

Please note:

- To display images and placeholders in the header, use the [avatar](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar/) control.
- The subtitle is now below the title. (In the former object page header, it was next to the title.)

For more information, see the [Dynamic Page Header](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#header-title) section for the dynamic page layout.

> **Warning:** Always build the object page using the **dynamic page header** and not the former object page header. Using the old object page header creates issues that can’t be fixed retrospectively. Using the dynamic header will also
ensure consistency across all floorplans and provide greater flexibility. For details, see the [Header](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#header-content-optional) section below.

> **Hint:** To use the dynamic page header in SAP Fiori elements, set the class “objectPageHeaderType” to “Dynamic”.

### Breadcrumbs

A breadcrumb is displayed above the object title. Limit the breadcrumb to the drilldown levels within the object page.

### Header Content (optional)

The header content displays app-specific contextual information. You build the content using containers, called facets.

The facets are arranged inline, with a left float. Each facet adapts its size to the content and makes optimal use of the space without truncating the texts. If the facets do not all fit on one line, those on the right wrap to the line below.

The header content is hidden by scrolling down the page or clicking the collapse indicator.

There are several types of header facets for different kinds of data. The facets must be implemented by the app team for standalone object pages. For SAP Fiori elements, they are predefined.

The following header facets are available:

- [Form (dataset)](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#form-facet-dataset)
- [Plain text](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#plain-text-facet)
- [Image](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#image-facet)
- [Key value](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#key-value-facet)
- [Micro chart](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#micro-chart-facet)
- [Progress indicator](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#progress-indicator-facet)
- [Rating indicator](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#rating-indicator-facet)

Default (col-1)

#### Form Facet (Dataset)
You can use the form facet to display datasets.
A form facet consists of:
1. Title (optional)
2. Label-text pair (no more than 5 in a group)
- The labels can be invisible, but need to have a text for accessibility purposes.
- The labels can be icons, but need to have a text for accessibility purposes.
- Each text can hold a link.

> **Hint, Col-1:** For **non-SAP Fiori element object pages** only:
For each label-value pair in the form header facet, use a *sap.m.Label* and a sap.m.Text or sap.m.Link, nested within an sap.m.HBox.

Default (col-2)

*Header facet - Form facets*

Section Metadata

style

Default (col-1)

#### Plain Text Facet
You can use the plain text facet to display a continuous text in the header.
A plain text facet consists of:
1. Title (optional)
2. Text
You can have links inline in the continuous text. They can navigate to another page or open a [quick view](https://www.sap.com/design-system/fiori-design-web/ui-elements/quickview/). The text can contain more than one link, with different actions.
The default width of the facet is 320 px. The width of the facet doesn’t adapt to its content, but when the headline is broader than the facet width, the header wraps. You can also set a specific width to make optimal use of the given space.

> **Hint, Col-1:** For **non-SAP Fiori element object pages** only:
To set the width of the plain text facet, nest the text within an sap.m.HBox and set the property:width of the
sap.m.HBox.

Default (col-2)

*Header facet - Plain text facet with default width*
*Header facet - Plain text facet with custom width*

Section Metadata

style

Default (col-1)

#### Image Facet
You can use the image facet to show a picture of the object or a user profile. The header can have either one image
facet or no image facet. The position of the image facet is fixed to the left. The image can have a press event. The
default press event enlarges the image. When the header collapses, the image facet moves to the left of the title and
becomes smaller.

> **Guideline, Col-1:** Always use the [avatar control](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar/) for the image in the header. This applies to both expanded and collapsed images.

Default (col-2)

*Header facet – Image facet specification*

Section Metadata

style

Default (col-1)

#### Key Value Facet
You can use the key value facet to highlight important data or KPIs.
A key value facet contains:
1. Title (mandatory)
2. Text or number in a larger font size
If the key value facet is used with a text, such as a status, you can also display an icon to the right of the text.
This icon must only be used as a visual cue for the text it relates to, and not to add more information.

> **Hint, Col-1:** For **non-SAP Fiori element object pages** only:
Larger value texts are now possible following the introduction of new properties for the [object status](https://www.sap.com/design-system/fiori-design-web/ui-elements/object-display-elements/#object-status) and [object number](https://www.sap.com/design-system/fiori-design-web/ui-elements/object-display-elements/#object-number1).

Default (col-2)

*Header facet – Key value facets with KPIs and a status*

Section Metadata

style

Default (col-1)

#### Micro Chart Facet
A micro chart facet consists of:
1. Title (mandatory)
2. Subtitle (optional)
3. Micro chart (mandatory)
4. Footer text (optional)
To display the unit used in the micro chart, use the footer.
The following micro charts can be used in the micro chart facet:
- [Bullet chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/bullet-micro-chart/)
- [Column chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/column-micro-chart/)
- [Line micro chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/line-micro-chart/)
- [Comparison chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/comparison-micro-chart/)
- [Delta chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/delta-micro-chart/)
- [Harvey ball chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/harvey-ball-micro-chart/)
- [Radial chart](https://www.sap.com/design-system/fiori-design-web/ui-elements/radial-micro-chart/)
The micro chart facet can have a click event on the chart itself. This can lead to a page with a bigger chart or open
a quick view, for example.
For more information, see [Micro Charts](https://www.sap.com/design-system/fiori-design-web/ui-elements/micro-chart/).

Default (col-2)

*Header facet – Micro chart facets*

Section Metadata

style

Default (col-1)

#### Progress Indicator Facet
A progress indicator facet consists of:
1. Title (mandatory)
2. Subtitle (optional)
3. Progress indicator
4. Footer text (optional)
For more information, see [Progress Indicator](https://www.sap.com/design-system/fiori-design-web/ui-elements/progress-indicator/).

Default (col-2)

*Header facet - Progress indicator facet*

Section Metadata

style

#### Rating Indicator Facet
You can use the [rating indicator](https://www.sap.com/design-system/fiori-design-web/ui-elements/rating-indicator/)
facet to display a single rating value or an aggregated rating (such as an average rating for a product). The facet
structure is slightly different in each case.
*Single rating value:*
The single rating consists of:
1. Title (mandatory)
2. Subtitle (optional): Displays supplementary texts
3. Rating indicator
*Aggregated rating:*
The aggregated rating consists of:
1. Title (mandatory)
2. Subtitle (optional): Indicates the amount of data being
aggregated.
3. Rating indicator
4. Footer text (mandatory): Displays the exact aggregation
value. Use the format “\<average rating> out of \<maximum
rating>”. For the average rating, use the exact value with
one decimal place.
> **Guideline, Col-1:** We recommend the following property settings when using the rating indicator in header facets:
- Show 5 symbols as the default.
- Use the *Favorite* icon as the symbol.
- Display half-stars to represent decimal values.

Section Metadata

style

### Navigation Bar

You can only have several sections in the object page layout and there are two ways to structure it:

- [Anchor bar navigation (default)](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#anchor-bar-navigation)
- [Tab bar navigation](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#tab-bar-navigation)

### Anchor Bar Navigation

The anchor bar is the default navigation control for the object page. It consists of a series of anchor links, which are arranged horizontally at the top of the page. The anchors represent sections or subsections of the page. Clicking a link makes the screen scroll to the corresponding section of the page and the anchor bar remains visible.

Use tab bar navigation if your page covers different topics that each have complex content, such as long tables or lists.

Default

*Object page – Anchor bar navigation*

Default (col-1)

1. Active anchor
2. Inactive anchor
3. Subsection dropdown
4. Subsection
5. Subsection dropdown indicator
6. Overflow carousel button
7. Overflow menu button
8. Overflow menu dropdown
9. Section (hover) in overflow menu
10. Section in overflow menu
11. Subsection in overflow menu

> **Hint, Col-2:** Make sure that the `UpperCaseAnchorBar` property is disabled and that you enter the anchor bar labels in **title case** (for example: *Contact Information*).

Section Metadata

style

#### Overflow

If there are more anchors than the screen can accommodate, the remaining anchors move into an overflow menu. The overflow button on the right of the navigation bar (:overflow:) opens a hierarchical dropdown list of all sections and subsections. When the user scrolls down the page, the anchor links scroll horizontally to ensure that the active anchor is always visible.

You might also see a small right arrow on the anchor bar. This arrow allows you to scroll horizontally to reveal any hidden content, and only appears when you hover over the overflow menu. In the meantime, this arrow has been replaced by the overflow menu button, but is still supported technically for legacy reasons.

#### Responsiveness

On small screens, the anchor bar becomes a dropdown list. The text field of the dropdown list shows the section currently selected. Clicking the dropdown menu opens a hierarchical list with all the sections and subsections of the page.

#### Behavior and Interaction

Table

**Click / Select:**

Anchor link
section (not to the title).

Arrow next to section anchor with several subsections

Item in the overflow list
or subsection (not to the title).

Keyboard left and right arrows

Fade area to the left or right of the anchor bar
only). The overflow arrow button is always visible in
cozy mode.

Overflow scroll button (right arrow)
are hidden in the overflow into view.

Overflow menu button (:overflow:)
sections and subsections of the page.

### Tab Bar Navigation

As an alternative to the anchor bar, you can also use the tab bar for navigation. The tab bar works in a similar way to the [icon tab bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/icontabbar/#responsiveness), but is not the same control. The tab bar navigation for the object page is a variant of the anchor bar, and is handled by the object page floorplan.

The tabs are a series of links arranged horizontally at the top of the page which link to subpages. Clicking a link displays the corresponding subpage below and the tabs remain visible.

Use tab bar navigation if your page covers different topics that each have complex content, such as long tables or lists.

Default

*Object page – Tab navigation*

1. Anchor/tab bar navigation
2. First section
3. Second section

If you set the tab bar property (`useIconTabBar` = “true”), the navigation bar displays tabs instead of anchors. The object page only supports text-only tabs; icon tabs and icon/text tabs are not available. The object page sections and subsections are reflected in the tab navigation: sections of the object page become the tabs, and subsections become the internal content of the tab. The tabs can have an item counter, which is displayed in parentheses next to the title of the tab.

On small screens, the tab bar uses the same horizontal carousel overflow pattern as the icon tab bar. This differs from the dropdown approach used for the anchor bar.

If the content of a section contains a control, for example a table, then we recommend to always display it, even if the control title and tab title are identical. This makes it easier for the user to orientate themselves.

#### Subnavigation

To make it easier to reach specific content on a long tab page, tabs can have subnavigation. Subnavigation is optional, but the default state is set to “true” and a dropdown arrow is shown next to the tab. Clicking on the dropdown arrow displays a dropdown menu with the subsection anchors for that tab. Applications can decide which tabs are enabled for anchor subnavigation by setting their property to “true”.

### Content Area

The object page content consists of sections and subsections arranged in a column layout.

#### Sections
Sections are containers for subsections. They provide the
basic structure for navigation and are directly reflected
in the navigation bar.
The first section doesn’t have a title.
2. Toolbar with actions (optional)
All the following sections consist of:
4. Mixable related content (optional)
1. Title with item counter (counter is optional)
2. Subsections
If the subsection contains a table or a chart and the title is the
Sections cannot contain controls.
If a section contains only one subsection, the title of
the subsection is used as the name of the section. In
this case, there is no subsection submenu in the anchor
bar.
content. App developers can specify which content is shown initially,
Sections can only contain subsections, not content.
Because of this, the object page only provides toolbars
for local actions at the subsection level.
> **Guideline:** If a section contains a control, like a table or a chart, and the title of the control is the same as the section
title, then the section title can be hidden so that this title is only displayed once. This avoids unnecessary
redundancies.
We recommend the same for subsection titles.

#### Responsiveness
The content blocks in a subsection display in a row. The
width of the row depends on the column layout for the
respective screen size. If there is not enough space to
display a content block, it wraps to the line below.
> **Hint:** For **non-SAP Fiori element object pages** only:
The content of the dynamic page header, navigation bar, (sub)section titles, and subsections must be vertically aligned. To achieve this, apply the `sapUxAPObjectPageSubSectionAlignContent` CSS class to the content of the subsections and set the `width` property to “auto”.

#### Forms within the Object Page

Form columns can be displayed with the standard number of columns or more to allow application teams to efficiently handle information density.

**> **Guideline:** **

We recommend you optimize the information density of forms on:
- Extra large screens that allow the display of 6 columns, if short titles are used.
- Large and medium screen that allow the display of more columns between the breakpoints for the screens.

For guidance on layout columns and content density for form content in the object page, see [Responsiveness](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#responsiveness-2).

Forms are located within subsections. They follow the column design of the object page, whereby each form group is arranged into a column. The title of the form is given by the subsection header. To improve access to the different forms we recommend always using one subsection per form, rather than placing multiple forms into one subsection.

To add actions, use the subsection header. For actions at the group level, use a group header. To prevent confusion, we recommend inserting actions only in one place, depending on the use case.

Use top-aligned labels for form fields. Top-aligned labels are known to reduce completion times and are the best approach for forms requiring localization or long labels. Using top-aligned labels also prevents issues with the spacing between the label and form field, which can occur with left- and right-aligned labels.

You can enable users to show and hide forms, groups or label-value field pairs using the *Show More / Show Less* toggle button.

SAP Fiori elements provide an option to show or hide fields on small screen devices based on their importance.

> **Hint:** You can set the importance of a field using the `UI.Importance` annotation type (`"High"`, `"Medium"`, or `"Low"`), the fields are shown or hidden depending on the screen size. If you do not specify the `UI.Importance` annotation, the default is set to `"High"` and the field is shown on all device types.

#### Blocks
Layout blocks allow content to be aligned within the columns as follows:
- Layout 1: Occupies the maximum available horizontal space of one column.
- Layout 2: Occupies the horizontal space of only two columns. If there is only one column available, it occupies one column.
- Layout 3: Occupies the horizontal space of three columns. If there is only one column available, it occupies one column. If there are only two columns available, it occupies two columns.
To show and hide blocks, you can use a *Show More* / *Show Less* toggle button. Do not use the [panel](https://www.sap.com/design-system/fiori-design-web/ui-elements/panel/) container in the object page content area.
#### **Tables**

When a section or subsection contains one table and no other content, remove the redundant table title so the section or subsection title serves as the table title. In the subsection, also reduce the vertical space.

Grid tables in sections must have at least 4 rows, and the maximum number of rows visible will depend on the window size. To prevent any need for the user to scroll to access the horizontal scrollbar, keep the table within the screen size limitations. This may not be possible in all use cases, for example, if the table contains a large data volume, then you must use two scrollbars.

In an object page with anchor bars, use no more than 4 grid tables to prevent cognitive overload. (Consider using different sections between multiple tables to ease the burden, except for table comparison use cases.) To include more than 4 grid tables, place them in individual tabs.

To embed analytical tables or tree tables in an object page, use an object page with tabs and place each table in its own tab. If you are using a scrollable object page without tabs, use responsive or grid tables instead, and offer navigation to another page with the respective table type.

Depending on the number of table items, use one of the following loading behaviors:

Table

**Number of Table Items:**

Up to 20

Up to 100

More than 50-100 but less than 200

More than 200 or tab approach is unsuitable

If a table is expected to have more than 20 items, use one of the 3 options below for long tables.

For all three options, we recommend **providing a search**, and if feasible, **sorting and filtering for the table** in the object page. **Avoid grouping.**

*1. Lazy Loading Behavior (“More” button)*

If you expect up to 100 items, use the [*More* button](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/#layout) of the responsive table. The initial number of items shown depends on the height of the rows. We recommend initially showing 10 items, but not more than 20. If there is more than one table in the object page, only use this option for tables with up to 50 expected items.

*2. Tab Navigation*

If you expect to have more than 50 to 100 items, but fewer than 200, using the object page with tab navigation instead of anchor navigation also solves the problems associated with long tables. To enable the scroll-to-load behavior, the table must be the only or last element within a tab.

*3. Navigation to Another Page*
For tables with more than 200 items, or when the tab
approach is unsuitable, restrict the size of the table in
the object page to a reasonable number of items. We
recommend showing a preview of only 10 items, but not
more than 20. This can be achieved using predefined
filters and/or by sorting the table. If necessary, you
can also set a fixed number of items (such as the top
10). To enable the user to work with the entire table,
offer navigation to a separate page, such as a list
report, subobject page, or dynamic page with the
respective table type. To do this, place a right-aligned
link below the table with the label *Show All (x)*, where
x represents the total number of items in the table.
#### Representation of Child Pages

In object pages with drilldown navigation, child pages are represented in two ways:

- Breadcrumbs: A breadcrumb is displayed above the object title. Limit the breadcrumb to the drilldown levels within the object page.
- Paging buttons: Up and down arrows in the [layout action area](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#header-title) allow the user to navigate between subitems without going back to the original list.

### Footer Toolbar

The footer toolbar is used for closing and finalizing actions in:

- Edit and create mode, for example, *Save*, *Post*, *Accept*, *Reject*, and *Activate*
- Display mode, for example, *Approve, Accept,* and *Reject*

## Behavior and Interaction

The basic layout of the object page in terms of header, navigation, and content remains the same in all modes (display, edit, create).

### Initial Focus

When the object page is loaded, set the initial focus as follows:

- If the object page is in edit mode, set the focus on the first empty mandatory field.
- If there are no mandatory fields, set the focus on the first editable element or first action.

### Edit

The object page can contain a mixture of editable and read-only content.

Use the same content layout for both display and edit mode – content should not change location when the user switches between display and edit modes.

For global and local editing guidelines, see [Object Handling (Create, Edit, Delete)](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/manage-objects).

There are two ways of editing header content depending on whether you’re implementing Global Edit or Partial Edit, both of which are explained below.

#### Editing header content in Global Edit mode

Because the header snaps on scroll, there are no editable forms in the header itself, so if you’re dealing with editable header content, a temporary “Header” section is generated above all the other sections of the page where the header content can be edited. The same principle applies if your object page only has one section and there is editable content in the header, except a temporary navigation bar should be generated as well. Any changes made to the header are not reflected until the user saves them.

When there is editable content in the header, the title bar information and all editable fields from the header container move from the header to the temporary “Header” section and non-editable content displays as read-only. You can leave out header content that doesn’t make sense in edit mode (for example, aggregated values that are calculated from several sources, KPIs, or micro charts). If only a few fields in the header are editable, and they match an existing section, they are moved to that section. In this case, no editable header section appears. The header container in edit mode can also contain independent facets that are not included in the header content in display mode which provide information to assist editing.

**> **Guideline:** **

The temporary “Header” section for editing header content requires manual implementation for freestyle applications.
Consider whether it’s better to place editable content in the object page sections instead of in the header.

> **Hint:** The temporary “Header” section described comes out of the box with SAP Fiori elements. With freestyle applications,
it needs to be implemented manually.

#### Editing header content in Partial Edit mode

The user can edit the header content separately by pressing the *Edit Header* button.

If there are only a few elements to edit, the partial edit triggers a dialog.

If there are too many elements to fit in a dialog, the partial edit triggers a subpage. The subpage contains all editable information from the header. However, it differs from the “Header” section in global edit mode in that it has no action buttons in the toolbar, no navigation, and no breadcrumbs.

#### Create and edit subobjects

The following options are available for creating or editing subobjects:

- Navigation to a subobject page
- Inline create or inline edit in a [table](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/#add-items)
- Dialog containing the fields of the object

To enable users to create subobjects inline, offer an *Add* or *Create* button on the table toolbar. Clicking the button creates a row at the top of the table. Pressing **Ctrl+Enter** has the same effect.

If the subobject has less than 8 fields, use a dialog or the inline create/edit option (no separate page for the subobject). Exceptions can apply if additional content for the subobject is available but not part of the edit process, or if other apps need to offer deep links to the subobject page.

#### Edit Actions in Display Mode (freestyle apps only)

The standard flow is to switch to edit mode for edit and delete actions. However, in some cases, it can be helpful to offer certain edit actions in display mode as well.

You can offer edit actions in display mode if:

- Switching to edit mode would inconvenience the user. This is especially true if the change is small and quick, and switching to edit mode would take longer than making the change.
- The change does not impact a critical flow or result in technical inconsistencies.

*Examples:* Adding a comment, uploading a file

Do not offer edit actions in display mode if:

- The change has a critical impact on business data/follow-on processes.
- The change requires a finalizing action.

*Example:* Deleting a sales order item would affect the entire sales order and dependent data.

When offering delete actions in display mode, always show a delete confirmation dialog. For more information, see:

- [Delete Objects – Object Page](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/delete-objects#delete-from-object-page)
- [Delete Objects – Top Tips](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/delete-objects#top-tips)

#### Unsaved Changes
If [draft handling](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/draft-handling)
has been implemented, documents are automatically saved as draft versions in the background. An editing icon to the right of the object title
indicates that a draft version exists. In other words, either the current user or another user has made changes, but not yet actively saved the
document (“unsaved changes”). Do not show the editing icon for unsaved changes if draft handling is not supported.
Selecting the editing icon invokes a popover with more information about the unsaved changes. This normally states:
- Who made the changes
- When the last changes were made
The popover closes when the user clicks outside the popover or clicks the :decline: (*Close)* icon.
### Create

Create mode is similar to edit mode, except that the user creates a new object and defines a title for it. Until the new object title is known, display the placeholder text “New ” (for example, *New Purchase Order*). Replace the placeholder text with the actual name or ID of the new object as soon as this has been entered or generated.

Consider using the [wizard floorplan](https://www.sap.com/design-system/fiori-design-web/ui-elements/wizard/) instead of the object page floorpan if:

- You need to guide the user through a series of steps when a new object is created.
- You need a progressive disclosure approach for the creation process.
- The creation process is not linear, but can have different paths, depending on the information selected.
- The user is not familiar with the creation task.

### Loading Behavior
The object page loads in a “growing” mode. This means that the object page loads section by section to show users some content before the whole
page is loaded. Scrolling down the page triggers loading for the sections below. Hidden items in sections are only loaded (and rendered) by
clicking the *Show More* button for the section.
If loading takes a long time, a busy indicator is shown on top of the section or item until the content is loaded and visible.
SAP Fiori elements uses a skeleton template with generic placeholders. For more information, see [Placeholder Loading](https://www.sap.com/design-system/fiori-design-web/ui-elements/placeholder-loading/).
## Message Handling

### In Display Mode
The following controls can provide messages to users in the object page in display mode:
1. Generic tag
2. Message strip
3. Object status
#### Generic Tag
The [generic tag](https://www.sap.com/design-system/fiori-design-web/ui-elements/generic-tag/) displays KPIs and [situations](https://www.sap.com/design-system/fiori-design-web/discover/sap-products/sap-s4hana-only/situation-handling).
#### Message Strip

You can place a [message strip](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-strip/) in the header or in a section in the content area:
- **Header**
Show the message strip in the header if the information relates to the whole object.
Place the message strip between the object page title and the header content. When the header is collapsed, it remains visible.
*Object page with message strip in a section*
- **Content area section**
Show the message strip in the content area section if the information relates to a specific section.
Place the message strip at the top of the section above the section title.
Use a single message strip with a single message per area. Do not stack several message strips together.
A message strip can display:
- A call to action, such as a task that the user must perform
- Temporary information that the user needs to know
- An issue that is not related to a form field
- The object status if the object status control is too small to convey the information.
- For a brief status text, use the [object status](https://www.sap.com/design-system/fiori-design-web/ui-elements/object-display-elements/#object-status) control.
If you decide to display both the message strip and the object status control, they should not repeat the same information.
- Brief guidance on how to use or read the page.
If the object page requires multiple hints for the user, consider using [SAP Companion](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/web-assistant) instead.
#### Object Status
The [object status](https://www.sap.com/design-system/fiori-design-web/ui-elements/object-display-elements/#object-status) displays a brief description of the object status.
### In Edit Mode

In edit mode, use the [message popover](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-popover/) to help validate forms and tables as a single object.

## Responsiveness

The object page floorplan is responsive and supports all SAP Fiori screen sizes: small (S), medium (M), large (L), and extra large (XL).

For standard columns provided by the form, see the [Form / Simple Form](https://www.sap.com/design-system/fiori-design-web/ui-elements/form/#responsiveness).

### SAP Fiori Elements: Extended Columns Feature

SAP Fiori elements, by default, provide reduced content density for form content:

- Small: 1 column
- Medium: 3 columns
- Large: 4 columns
- Extra large: 6 columns

### Use

- For general content or for forms that contain longer text/label value pairs, use the **standard column distribution** provided in [Form / Simple Form.](https://www.sap.com/design-system/fiori-design-web/ui-elements/form/#responsiveness)
- For forms that contain short text/label value pairs in SAP Fiori elements, use the **extended column feature** to improve information density.

### Extra Large Screens

#### Responsiveness of Form Content

For size XL, we recommend using the full 6 columns for forms with a lot of content. This gives you greater flexibility when you organize the form content and the groups

**> **Guideline:** **

- **Use the default balanced option** to spread the content of the form group or groups evenly across a maximum of 4 columns.
- **Use the extended column option** to spread the content of your form and group or groups evenly across 6 columns.

*XL screen extended (up to 6 columns)*

### Large Screens

#### Content Density of Forms with Large Screens

Forms on an L screen have 3 columns by default. You can increase the number to as many as 4.

**> **Guideline:** **

- **Use the default balanced option** to spread the content of your form group or groups evenly across a maximum of 3 columns.
- **Use the extended option** to spread the content of your forms and group or groups evenly across 4 columns.

*Large Screen Extended (4 columns)*

### Medium Screens

#### Content Density of Forms with Medium Screens

Forms on an M screen have 2 columns by default. You can increase the number to 3.

**> **Guideline:** **

- **Use the default balanced option:** to spread the content of your form group or groups equally across 2 columns.
- **Use the extended option:** to spread the content of your forms and group or groups equally across 3 columns.

*Medium screen extended (3 columns)*

### Small Screens

Forms on an S screen (smartphone or small desktop screens) have one column by default.

*Small screen with form content (1 column default)*

## Guidelines

### Dynamic Page Header

Use the header to set the context. Ensure that it is clearly structured and contains only essential information. Too much information impedes the main purpose of providing clear context.

> **Hint:** **How to achieve a small header:**
- The header container is always optional. If there is no important data to be displayed, you can omit it. In this
case, only the header title bar is shown.
- Omit the image if it is not necessary. It is generally the tallest element in a header container.
- Use a light theme to reduce the emphasis on the header if it doesn’t contain much information.
- Consider moving information from the header into a general information section.

### Actions

Arrange the actions in the header toolbar with care, and consider what matters most to the user:

- Highlight actions that are common or most important.
- Differentiate between secondary and generic actions.
- Use either a text button or an icon for an action, but not both.
- Use icons only for generic actions (such as :action: for *Share*). For all business actions, use text buttons.
- Place the most important actions on the left (actions go into the overflow from right to left).
- Establish a coherent visual approach.

For more information, see [Action Placement](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement).

### Image Facet

If you intend to use images in the object header, consider the following:

- How will the user manage the images?
- How will the system block people without permission from editing images?
- How will these images be reflected in other floorplans if they are part of the object?
- If there are a large number of items, how would a user be able to manage images without having to navigate from page to page?
- Will the organization be able to manage the images?

### Tab Navigation

If you have a complex object page, use the tab navigation approach. This can be useful when a complex object page has performance issues in a flat view, or in response to a specific user preference.

### Content Area

- Avoid using the object page as a universal container for masses of information. Use the object page in accordance with the SAP Fiori principles: role-based, coherent, simple, and adaptive.
- Give your users quick and easy access to the information they need to complete their task(s). Use a progressive disclosure strategy to keep your interface clean. You can always provide additional information on request.
- Only present your users with information that makes sense for their industry, role, activity, and task.

### Dynamic Side Content

You can offer [dynamic side content](https://www.sap.com/design-system/fiori-design-web/ui-elements/dynamic-side-content/) alongside the object page under the following conditions:

- Use the side panel only for contextual content. Do not place finalizing or global actions in the side panel. This is because opening the side panel occupies the whole right side of the screen. There is no way to show it only below the header and anchor bar.
- Do not place object information in the side panel. This information should always be in the content area of the object page.

### Standard Naming Conventions

For all objects, follow the standard conventions for action buttons, the object name, and the title in the shell bar. For more information, see:

- [Object Handling – Naming Guidelines](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/manage-objects#naming-guidelines)
- [Launchpad Shell Bar – Page Title and Navigation Menu](https://www.sap.com/design-system/fiori-design-web/ui-elements/shell-bar/#page-title-and-navigation-menu).

## Resources

#### Elements and Controls                                                                                                                                                                                        | #### Implementation                                                                                                                                                        | #### Visual Design
- [Dynamic Page – Header](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#header-title) (guidelines)                                                              | - [Object Page Floorplan](https://ui5.sap.com/#/entity/sap.uxap.HeaderFacetPattern) (SAPUI5 samples)                                                                       | - [Visual Design](https://wiki.one.int.sap/wiki/pages/viewpage.action?pageId=2697896853) (visual design specification)
- [Action Placement](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement) (guidelines)                                                                 | - List Report and Object Page (developer guide)
- [Form / Simple Form](https://www.sap.com/design-system/fiori-design-web/ui-elements/form/) (guidelines)                                                                                                         | - SAP Fiori Elements Feature Map (internal)
- [SAP Fiori Elements – Object Page Header](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements) (guidelines)             |
- [SAP Fiori Elements – Object Page Content Area](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements) (guidelines) |
- [SAP Fiori Elements – Object Page Footer Bar](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-footer-bar-sap-fiori-elements) (guidelines)     |
#### Elements and Controls                                                                                                                                                                                        | #### Implementation
- [Dynamic Page – Header](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#header-title) (guidelines)                                                              | - [Object Page Floorplan](https://ui5.sap.com/#/entity/sap.uxap.HeaderFacetPattern) (SAPUI5 samples)
- [Action Placement](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement) (guidelines)                                                                 | - List Report and Object Page (developer guide)
- [Form / Simple Form](https://www.sap.com/design-system/fiori-design-web/ui-elements/form/) (guidelines)                                                                                                         |
- [SAP Fiori Elements – Object Page Header](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements) (guidelines)             |
- [SAP Fiori Elements – Object Page Content Area](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements) (guidelines) |
- [SAP Fiori Elements – Object Page Footer Bar](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-footer-bar-sap-fiori-elements) (guidelines)     |

---

## Floorplans > Overview Page > Usage

> **Information:** This floorplan is implemented with [SAP Fiori Elements](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements).
To explore the design capabilities of SAP Fiori elements for OData V4 and experiment with their behavior, see [Overview Page](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/floorplanOverviewPage/overviewPage) in the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## Intro

#### View, Filter, and Take Immediate Action
The overview page (OVP) is a data-driven SAP Fiori app type and floorplan that provides all the information a user needs in a single page, based on the user’s specific domain or role. It
allows the user to focus on the most important tasks, and view, filter, and react to information quickly.
- Content from different sources shows side by side – no
Each task or topic is represented by a card (or content container). The overview page acts as a UI framework for organizing multiple cards on a single page.
- Information can be visualized on cards in different
The overview page is based on [SAP Fiori elements](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/smart-templates)
technology, and uses annotated views of app data, meaning that the app content can be tailored to the domain or role. Different types of card allow you to visualize information in an
attractive and efficient way.
*Overview page*

## When to Use

### Use the overview page if:
- You want to provide an entry-level view of content related to a **specific domain or role**.
- Users needs to filter and react to **information from at least two different applications** to complete their role-specific tasks.
- You want to offer **different information formats** (such as charts, lists, and tables) on a single page.
- You plan to have **at least three cards**. These cards should not all be of the same type.

Default (col-1)

#### SAP Fiori Launchpad Home Page, Overview Page, and Object Page
The [launchpad home page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/home-page) contains **all of a user’s favorite apps** and offers access to them via [tiles](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tile/). This covers all the roles that a user might have, such as employee, manager, production worker, or quality manager.
An overview page focuses on the **key tasks for a specific role**, and contains only the most frequently-used apps for that role. The overview page uses cards, which display more (preview) information than tiles because of their size, properties, and interaction areas. One card type also allows users to perform simple actions. Cards represent an entry-level view of application content.

Default (col-2)

#### Launchpad Home Page vs. Overview Page

Table (col-2)

Launchpad Home Page

Framework (given)

“Birds-eye” view

Single point of entry

One SAP Fiori launchpad per user

Access to all the user’s favourite applications

Uses tiles

No actions

Section Metadata

style

Default (col-1)

The overview page is always role-based. The user sees a heterogeneous set of information related to a specific business context and the tasks associated with a specific role. This is not the case with the [object page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/), which contains homogenous, object-based information.

Default (col-2)

#### Overview Page vs. Object Page

Table (col-2)

Overview Page

Role-based

“Street-level” view

Heterogeneous information

Section Metadata

style

#### Role-Specific Overview Pages
As you can see in the picture, the overall content scope
(shown in gray) becomes more focused with each
interaction step. An overview page brings together
information from different sources that support a
specific task or information need. Only provide an
overview app for a role if it makes sense to do so.
If a role or user has several main tasks that each
require a specific set of information, the role or user
might also have multiple overview apps. For example, one
overview app could be used to reflect the user’s role as
manager, with information for managing team performance
reviews. Another overview app could be used to track
quality issues and other relevant information pertaining
to the machines that the user is responsible for in the
role of quality manager.
## Components

The basic structure and appearance of the overview page is governed by the [dynamic page layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#components), and is divided into a header area and a content area.
This enables you to use variant management, text, and a smart filter bar in the upper part of the screen (dynamic page header). The content of the overview page is presented using [cards](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/overview-page-card/).
Two different [layouts](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page/#overview-page-layout) are available, which determine the size and position of the cards: [fixed card layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/overview-page-fixed-card-layout/) and [resizable card layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/resizable-card-layout-overview-page/).
### Dynamic Page

The [dynamic page header](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#dynamic-page-header) comprises the header title and expandable/collapsible header content. Three different header variants are available for overview pages.

In the overview page, the header content is used for the [smart filter bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/filter-bar/) with the live update mode (variant 1 and variant 2): the results are updated immediately whenever the user changes a filter field. As a result, there is no *Go* button for the filter bar.

Users can expand/collapse and pin the header content with the two icon buttons below the smart filter bar:

1. [Expand/collapse header](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#expandcollapse-header-feature): :slim-arrow-down: or :slim-arrow-up:
2. [Pin/unpin header content](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#pinning-the-header-content): :pushpin-off:

#### Filter Summary

#### Dynamic Page Variants for the Overview Page

The header title (either text or variant management) is mandatory, while the header content (smart filter bar) is optional. Variant 3 shows only a text in the header title.

Table
Variant 1          | Variant 2        | Variant 3

Dynamic page header | Yes                | Yes              | Yes

Header title        | Variant Management | Text             | Text

Header content      | Smart Filter Bar   | Smart Filter Bar | –

Page content        | Cards              | Cards            | Cards

Accordion

Variant 1 – Variant Management and Smart Filter Bar
(default)
*Dynamic page variant 1 – Expanded mode*

Variant 2– Text in the Header Title and Smart Filter Bar
*Dynamic page variant 2 – Expanded mode*

Variant 3 – Text in the Header Title
*Dynamic page variant 3 – Expanded/collapsed mode*

### Overview Page Layout

*Fixed card layout*

The overview page layout describes the position, size, and characteristics of cards in the content area below the dynamic page header.

There are two layout variants:

- [Fixed card layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/overview-page-fixed-card-layout/)
- [Resizable card layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/resizable-card-layout-overview-page/)

Only place [cards](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/overview-page-card/) on the overview page. Never add [tiles](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tile/).

#### Fixed Card Layout vs. Resizable Card Layout

Table

Fixed Card Layout

Fixed card width and predefined height

Users can’t influence the card size

Predefined static card characteristics
different levels of detail)

Lower implementation effort – defined card patterns

Self-contained cards

Fast overview and navigation

Cards can be swapped

Maximum of 5 card columns (letterboxing)

### Personalized Selection of Cards

Users can also hide cards. The corresponding setting is in the [user actions menu](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/launchpad#user-menu) under *Manage Cards*. A dialog appears on the overview page, and lists the different card names. Users can opt to show or hide the cards using a [switch control](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/switch/). *Restore* reinstates the default setup. The personalized setup stays until the user next changes it.

Each overview page app has its own *Manage Cards* setting. Users who work with several overview pages can personalize the cards shown for each one.

*Overview page – 'Manage Cards' dialog after initial loading*          |
## Behavior and Interaction

As for any other SAP Fiori app, users open overview page apps by selecting a tile on the [SAP Fiori launchpad home page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/home-page), or by bookmarking the direct link in a browser. From the overview page the user decides which issues need attention, and navigates via cards to the relevant SAP Fiori apps. In addition, users can also access the [navigation menu](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/shell-bar/#navigation-menu) in the shell bar, which allows fast and easy navigation to other apps. The overview page supports navigation to both SAP Fiori and non-SAP Fiori apps. For SAP Fiori apps, it uses intent-based navigation. Non-SAP Fiori apps open in a new browser window.

In the screen flow, always position the overview page app between the SAP Fiori launchpad home page and the SAP Fiori app. The overview page doesn’t replace the SAP Fiori launchpad home page. Never start overview page apps from another SAP Fiori app.

The picture below illustrates the complete interaction flow:
SAP Fiori launchpad home page ➝ SAP Fiori overview app ➝ SAP Fiori app or non-SAP Fiori app

*Overview page – Interaction flow*

#### Initial Focus

When the overview page is loaded, set the initial focus as follows:

- If no cards are loaded, and the filter bar is in manual mode, set the focus on the *Go* button or on the first filter field.
- If no cards are loaded, the filter bar is in manual mode, and a mandatory field is still empty, set the focus on the mandatory field.
- When all cards are loaded, set the focus either on the first card or the header of the first card.

#### Dedicated Floorplan

While other floorplans like the list report and object page can be combined in a single app, there is a **1:1 relationship between the overview page floorplan and the corresponding overview app**. The overview page floorplan is never combined with other floorplans. Because of this, the terms “overview page floorplan” and “overview (page) app” are often used synonymously.

## Cards

*Overview page – Different card types (selection)*

Cards are containers for app content, and represent an entry-level view of the most pertinent app data for a given topic or issue. The overview page can contain several cards that reference the same underlying application. However, each card must bring added value to the user, and not just repeat information already offered on another card.

Cards can display different types of content. They can show a chart, a list, a table, informative text, or a combination of two elements. Cards can also vary in size, depending on the selected [layout](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/overview-page/#overview-page-layout). However, cards never have editable fields.

When designing cards, make sure that you define and format the texts on all the cards consistently. Check the [UI text guidelines for the overview page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/overview-page-ui-text-guidelines) for details.

For more information about the [cards](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/overview-page-card/) and [card types](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/overview-page-card/#card-types) available for the overview page, see the dedicated topics:

- [Analytical Card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-card/)
- [List Card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/cards/overview-page-list-cards/)
- [Bar Chart List Card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/cards/overview-page-list-cards/#bar-chart-list-card)
- [Link List Card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/cards/overview-page-list-cards/#link-list-card)
- [Table Card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/cards/overview-page-table-card/)
- [Stack Card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/cards/overview-page-stack-card-quick-view-card/)
- [Custom Card](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/cards/overview-page-custom-cards/)

> **Information:** Please note that the [integration cards](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/cards/) cannot be consumed by the overview page.

## Responsiveness

The overview page is fully responsive and can accommodate typical laptop screens as well as larger desktop monitors. The responsive behavior differs for the two layout types – [fixed card layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/overview-page-fixed-card-layout/#responsiveness) and the [resizable card layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/resizable-card-layout-overview-page/#responsiveness).

Both feature responsive (collapsible) “columns” of cards that can scale all the way down to tablet or phone screen sizes. For more information on each card type, follow the respective links.

## Top Tips

Before you start designing an overview page, familiarize yourself with following best practices to optimize the user experience. They reflect the basic findings of multiple usability tests across different scenarios and user groups.

- **Make a conscious decision on the number of cards:** Show only cards that really support the specific role context or task.
- **Accentuate the most important information:** Semantic colors in texts, charts, attract more attention. The same applies to larger cards.
- **Offer a well-balanced mixture of card types**: Diversity makes it easy to recognize, select, and read information.
- **Define a deliberate card order:** Users assume that bigger cards and cards at the top of the page are more important than others.
- **Group similar topics:** Users assume that related cards will be shown next to each other.
- **Choose easy-to-read and actionable texts**: If the user needs to take action, use the active voice (for example “Reorder Soon” when stocks are running low).
- **Be semantically consistent:** Users expect crucial terms like “Urgent” or “Out of Stock” to be highlighted with semantic colors.

---

## Page Layouts > Dynamic Page Layout > Usage

## Intro

The dynamic page is the foundation for all pages in SAP Fiori. It is a generic layout control designed to support various floorplans and use cases. As a result, the content of both the header and the page can vary. Depending on your use case, you can either use one of the [predefined floorplans](https://www.sap.com/design-system/fiori-design-web/page-types/when-to-use-which-floorplan) or create your own layout.

One part of the dynamic page header (1) is collapsible, which helps users to focus on the actual page content (2), while ensuring that important header information and actions are readily available. The dynamic page also includes an optional footer toolbar (3) for closing or finalizing actions that impact the whole page.

Carousel (full-width)

All SAP Fiori floorplans use the dynamic page, or are visually aligned to look the same. For detailed guidance, see the corresponding floorplan articles.
The following floorplans use the dynamic page:
- [Object page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/#components)
- [Analytical list page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/#basic-layout)
- [List report](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/#components)
- [Overview page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page/#dynamic-page)
- [Wizard](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/wizard/)
- [Worklist](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/work-list/#components)
## When to Use

### Use the dynamic page if:

- You want to build a freestyle application that uses the foundation layout components for SAP Fiori pages, such as the [dynamic page header](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#dynamic-page-header) and the [footer toolbar](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#footer-toolbar). Also see the related [semantic page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/semantic-page/).
- You want to build a simple [object page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/#navigation-bar-optional) with only one section.
- You want to represent your application in full screen. Also the combination within the [flexible column layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/page-types/page-layouts/dynamic-page-layout/#Combining) is possible.

### Do not use the dynamic page if:

- You are planning to use [SAP Fiori elements](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/smart-templates), such as the [list report](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/), [analytical list page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/), [overview page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page/), or [object page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/). These floorplans already incorporate the dynamic page.
- You want to implement an [initial page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/initial-page-floorplan/) or an [object page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/#navigation-bar-optional) floorplan with complex content and several sections. These floorplans only use the dynamic page header.
- You only need to display a small amount of information. In this case, use a [dialog](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/dialog/) instead. If you can’t avoid using the dynamic page, use [letterboxing](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/letter-boxing/) to mitigate the issue.

### Dynamic Page vs. Semantic Page

The dynamic page is a skeleton structure that comes with empty content containers (page header, page content) and built-in responsive behavior.

This basic structure can be “filled” with content elements in three ways:

- **Automatically**: If you are using an [SAP Fiori element floorplan](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/smart-templates), the content of the dynamic page is provided out of the box.
- **Via the semantic page (recommended for freestyle apps)**: If you are creating a floorplan from scratch, you can use the [semantic page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/semantic-page/) (`sap.f.semanticPage`) to create a freestyle page. The semantic page is a separate control that comes with built-in logic for adding predefined content elements to the page, such as a title, global actions, and a footer toolbar. Using the semantic page significantly reduces the development effort for app teams, and ensures that the header and footer content is structured consistently.
  Note that in this case, the app developer uses only the semantic page control (which already embeds the dynamic page), and not the dynamic page control itself.
- **Manually**: Technically, it’s possible to build the dynamic page from scratch. However, implementing the dynamic page manually is a significant development effort! Only consider this option in exceptional cases (for example, if you have special requirements for a freestyle app that cannot be implemented using the preconfigured semantic page control).

## Components

Like all layouts, the dynamic page is below the [shell bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/shell-bar/) of the SAP Fiori launchpad, which is always at the very top. The dynamic page consists of the following areas:

1. [Dynamic page header](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#dynamic-page-header), comprising the header title (1a) and the expandable/collapsible header content (1b)
2. Title
3. Subtitle/summary
4. Key information / KPI
5. Global actions
6. [Header features](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#header-features) to expand/collapse (6a) and pin/unpin (6b) the header
7. Page content (differs depending on the use case and floorplan)
8. [Footer toolbar](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#footer-toolbar) with finalizing actions

Carousel (full-width)

### Dynamic Page Header

The dynamic [page header](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/page-header/) contains the [header title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/page-types/page-layouts/dynamic-page-layout/#header-title) (mandatory) and the [header content](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/page-types/page-layouts/dynamic-page-layout/#header-content) (optional).

#### Header Title

*Dynamic page - Header title example*

The header title bar (`sap.f.DynamicPageTitle`) always contains one of the following elements:

*Mandatory Elements*

- **Title** (1): The title is located on the left of the header title bar, and is always visible. The title can contain one of the following components:
  - [Title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/title/) (text)
  - [Link](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/link/)
  - [Variant management](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/)
  - [Input field](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/which-selection-control-to-use) (for the [initial page)](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/initial-page-floorplan/)

*Optional Elements*

- **Subtitle/summary** (2)
  Placement: Always below the title. The subtitle is often used to summarize the most important information in the collapsed header content. For example, if the header area contains a filter (as in a [list report](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/), [analytical list page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/), or [overview page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page/)), the subtitle can be used to display the “Filtered By” information.
- **Breadcrumb** (3)
  Placement: Above the title. Depending on the floorplan and use case, you can add [breadcrumb](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/breadcrumb/) navigation. The breadcrumb is located above the header title, and is primarily used to display the hierarchy of subpages within an object page.
  Note that in the [flexible column layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout/), the breadcrumb is only available in full screen mode, and only if just one column is visible.
- **Key information** (4)
  Placement: In the middle area, but left-aligned. Floorplans can also contain key information, such as text, mini facets, and KPI tags.
  Note that currently, KPI tags are only used within the [analytical list page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/) and [worklist](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/work-list/) floorplans.
- **Global actions** (5)
  Placement: Global actions for the entire floorplan appear on the right-hand side of the header title bar. Always offer the actions as [buttons](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/button/), visualized either as text or icons. For more information, see [Header Toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/header-toolbar/#business-actions). In the collapsed mode, the header title offers the same actions as in the expanded mode and keeps them actionable.
- **Layout actions** (6)
  Placement: Typical layout actions are the *Close*, *Full Screen*, or *Exit Full Screen* icons, which are mainly offered by the [flexible column layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout/). Depending on the screen size, the layout actions are placed either on the very right of the global actions toolbar, separated by a divider line, or above the global actions (see more in the [Responsiveness](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/page-types/page-layouts/dynamic-page-layout/#responsiveness) section). Note that the dynamic page only provides the area for the layout actions. The **navigation actions themselves are defined separately** (for example, using the [semantic page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/semantic-page/)).

> **Guideline:** - Do not remove or disable the actions within the global action toolbar when the header content is collapsed.
- In the [flexible column layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout/), ensure that the icons for the *Close* or *Full Screen* / *Exit Full Screen* actions always stay on the very right. Their position then remains stable, even if other actions are added (such as the [paging buttons](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/header-toolbar/#paging-layout) :slim-arrow-up: and :slim-arrow-down: ). The *Close* and *Full Screen* / *Exit Full Screen* actions must never move into the overflow.

#### Header Content

*Dynamic page - Header content example*

The optional header content (`sap.f.DynamicPageHeader`) is located below the header title. You can place any components in the header content area (1) as long as they follow the guidelines for the respective floorplan.

When the dynamic page header collapses, the header content area is hidden. If there is no header content, the header content area is hidden automatically. In the latter case, the header title is not interactive ([snap on scroll](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#snap-on-scroll) or [snap on click](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#snap-on-click)) and there is no [expand/collapse header](#clicking-the-expandcollapse-header-button) feature.

### Header Features

*Dynamic page - Header features*

The header features (3) allow users to control the visibility of [header content](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#header-content) using two icon buttons at bottom of the header content area:

1. [Expand/collapse header](#clicking-the-expandcollapse-header-button): :slim-arrow-down: or :slim-arrow-up:
2. [Pin/unpin header content](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#pinning-the-header-content): :pushpin-off:

### Footer Toolbar

*Dynamic page - Footer toolbar*

The [footer toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/footer-toolbar/) (`sap.m.Toolbar`) is an optional part of the dynamic page. You can use it to offer closing or finalizing actions.

### Combining the Dynamic Page with the Flexible Column Layout

The layout of the dynamic page is responsive and optimized for use within a [flexible column layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout/). Each column (1, 2, 3) can contain its own dynamic page with a different floorplan, depending on the use case.

*Dynamic page inside the flexible column layout*

## Behavior and Interaction

### Initial Focus

The dynamic page itself doesn’t set an initial focus. The initial focus depends on the floorplan that is using the dynamic page and the specific app use case.

### Dynamic Page Header                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |  |
The dynamic page header supports three optional interaction patterns that can be combined. To show more of the actual page content, the header content can collapse or expand using defined triggers ([snap on scroll](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#snap-on-scroll) and [snap on click](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#snap-on-click)). In addition, users can fix the header content while scrolling through the page content with the [pin feature](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#pinning-the-header-content). The combined usage of all three patterns is recommended and activated by default. | *Dynamic page - Snap on scroll*          | *Dynamic page - Snap on click*           | *Dynamic page - Pin/unpin*

#### Starting in Expanded or Collapsed Mode

By default, the header content is initially expanded. In certain cases, it can also make sense to deviate from the default and allow the header to appear in collapsed mode when initiating the app. However, the idea is to always expand the header content when the application starts without a query (and the content area is therefore empty).

#### Snap on Scroll

Scrolling is the typical trigger for collapsing the header content. When the user scrolls down the page, the header content scrolls away. The header title switches to collapsed mode and stays fixed. When the user scrolls up the page, the header content expands again.

Note that this interaction pattern works only in combination with an expandable/collapsible header content. It can be combined with [snap on click](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#snap-on-click), but does not have to be.

Carousel (full-width)

#### Snap on Click

The snap on click pattern is another way of expanding and collapsing the [header content](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/page-types/page-layouts/dynamic-page-layout/#header-content). The user can collapse the header without scrolling, and expand it again even when it has been collapsed by scrolling down. Two interaction variants are offered, which always appear in combination: clicking the header title and clicking the *Expand Header / Collapse Header* icon button in the header features area.

Again, the interaction pattern works only in combination with expandable/collapsible header content. It can be combined with [snap on scroll](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#snap-on-scroll), but does not have to be.

##### Clicking the Header Title

The user can expand and collapse the header content by clicking anywhere on the header title bar that has no active elements (such as links or active buttons). When using a mouse, the cursor changes from an arrow to a hand to support the user’s interaction. In addition, a hover effect is visible on the header title and on the *Expand Header / Collapse Header* icon button in the header area. If the header is expanded and the user clicks the title bar, the header content collapses, and vice versa.

Carousel (full-width)

##### Clicking the Expand/Collapse Header Button

The expand/collapse header feature is a small icon button directly below the header, which is also used to expand or collapse the header content. When the pin is active, the expand/collapse header button is still available and overrules the pin. The icon buttons for expanding and collapsing the header are an alternative to [clicking on the header title bar](#clicking-the-header-title), which might not have much clickable space. They also support [keyboard actions](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#keyboard-interaction).

Carousel (full-width)

#### Pinning the Header Content

Activating the pin feature keeps the header expanded while the user scrolls through the page content. This mode remains fixed until the user clicks the pin icon again or triggers [snap on click](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#snap-on-click). This feature is optional and can be switched off if it is not useful for your application.

The expand/collapse header button remains visible when the pin is activated. Clicking the *Collapse Header* icon overrules the pin, collapses the header, and switches the pin button off. Do not offer the pin feature for floorplans without scrollbars (see [special case](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#special-case-no-page-scrolling-possible) below), or if there is no header content.

In the smartphone version, the pin action is not provided, as the pinned header would take up too much screen real estate. The same applies whenever the dynamic page header would occupy more than 60% of the screen, regardless of the device type. Overruling the pin feature keeps the focus on the content.

Note that this interaction works only in combination with expandable/collapsible header content. The pin button is available as soon as [snap on scroll](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#snap-on-scroll) (or [snap on click](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#snap-on-click)) is activated.

Carousel (full-width)

#### Special Case: No Page Scrolling Possible

The following special case applies for pages containing desktop-centric tables, such as the [analytical table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/), [grid table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/), or [tree table](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tree-table/).

Because these tables use up all of the available screen space, there should not be a vertical scroll function, and hence no [snap on scroll](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#snap-on-scroll). In this special case, an explicit interaction via the expand/collapse header button is required to expand or collapse the content area. The [pin feature](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#pinning-the-header-content) is obsolete and is not provided.

This exceptional case also applies to [chart containers](https://sapui5nightly.int.sap.eu2.hana.ondemand.com/#/sample/sap.suite.ui.commons.sample.ChartContainerCustomIconsOneChart/preview) that use up all the available screen space in a similar way to desktop-centric tables.

#### Keyboard Interaction

Default (col-1)

The dynamic page header expands automatically as soon as keyboard actions like tabbing or group jumps (F6) bring the
content of the dynamic page header into focus.
The dynamic page header collapses as soon as the keyboard focus leaves the dynamic page header content area.

Table (col-2)

Key(s)

**Tab**
bar. The dynamic page header expands automatically. If
the focus is inside the header content area, move the
focus to the next UI element within the header.
If the focus is on the last UI element within the header
content area (expand/collapse header feature), leave the
header. Collapse the header content.

**Shift\+Tab**

**F6**
focus to the header title bar. Expand the header content.
If the focus is within the header content, move the focus
out of the header and collapse the header content.

**Shift\+F6**

Section Metadata

style

## Responsiveness

The dynamic page offers considerable freedom and flexibility. In addition, the dynamic page header and the footer toolbar are designed to adapt automatically to small, medium, and large screen sizes.

The **title** (`sap.m.Title`) and **subtitle** (`sap.m.Text`) on the left truncate in collapsed mode to save vertical space, and wrap in expanded mode to offer the full text. This behavior needs to come from the respective controls for the [title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/title/) and [subtitle](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/text/). Overall, we recommend showing a maximum of 2 lines of text in collapsed mode. This prevents a disproportionate header height, especially on mobile devices if no [summary line](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#summary-line) is used. The 2 lines can either be a combined title and subtitle, or a longer wrapping title. For more information, see [wrapping and truncating text](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/wrapping-and-truncating-text).

**Key information,** such as a **KPI** (middle area, left aligned), stays as long as possible before it moves into the overflow.

**Global actions** stay as long as possible. If there is no key information, the title and the global actions automatically get more space. The toolbar follows the standard [toolbar overflow](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/toolbar-overview/) guidelines, and adds the available buttons to the [overflow menu](https://sapui5nightly.int.sap.eu2.hana.ondemand.com/#/entity/sap.m.OverflowToolbar/samples) from right to left.

**Layout actions:** The dynamic page offers a specific area for layout actions, which reacts to the predefined breakpoint of 1280 px:

- Less than 1280 px: Navigation actions are placed in a separate row above the global actions.
- 1280 px or more: Navigation actions are placed to the right of the global actions on the same line.

This breakpoint corresponds to the page width and not to the window width. Therefore it doesn’t matter whether the page is used in the [flexible column layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout/), on a desktop device, or on a mobile device.

[Letterboxing](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/page-layouts/letter-boxing/) limits the width of the content area to 1280 px. This prevents the app content from becoming too “stretched” on wide screens, and optimizes readability. Letterboxing can be used together with the dynamic page if the use case requires it. However, most business apps offer so much content that the page is typically shown across the entire screen, without letterboxing.

#### Size L

Carousel (full-width)

#### Size M

Carousel (full-width, col-1)

#### Size S

Carousel (full-width, col-2)

Section Metadata

style

Default (col-1)

#### Summary Line
To save vertical space on smartphones, you can opt to display a smaller summary line instead of the collapsed header. The header
content scrolls away as soon as the user scrolls up the page. The header converts to a summary line, which shows only the [title](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#header-title)
and an arrow icon button on the very right of the screen. Tapping the summary line also expands and collapses the whole header. The
rest of the page stays in the same position.

> **Guideline, Col-1:** Use the summary line to help users to focus on the page content.

Default (col-2)

*Size S with summary line*

Section Metadata

style

## Examples

The dynamic page is a generic control. The content of both the header and the page differs from floorplan to floorplan. Here are some examples showing the most frequently-used variants for each type of floorplan. For detailed guidance, see the corresponding floorplan guidelines ([analytical list page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/), [overview page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/overview-page/), [list report](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/), [worklist](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/work-list/#dpiwlf), [initial page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/initial-page-floorplan/), [object page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/), [wizard](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/wizard/)).

#### Floorplan Examples

Carousel (full-width)

## Top Tips

- Always use a [header title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/page-types/page-layouts/dynamic-page-layout/#header-title) – either as a text or link, or by including variant management. For the [initial page floorplan](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/initial-page-floorplan/), use an input field.
- Use the [header title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/page-types/page-layouts/dynamic-page-layout/#header-title) and [header content](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/page-types/page-layouts/dynamic-page-layout/#header-content) to provide the most relevant information and actions for your use case.
- Only use KPI tags within the [analytical list page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/) and [worklist](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/work-list/) floorplans.
- Do not remove or disable the [actions](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/page-types/page-layouts/dynamic-page-layout/#header-title) within the global action toolbar when the header content is collapsed.
- Make sure that the [layout actions](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/page-types/page-layouts/dynamic-page-layout/#header-title) in the flexible column layout are displayed correctly and never get hidden in the overflow.
- Start your application in [expanded mode](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#starting-in-expanded-or-collapsed-mode) if users need further content or adjustment options to get started.
- Offer the [pin feature](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#pinning-the-header-content) whenever users may need to fix the header content while scrolling through the page content.
- Activate the [summary line](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#summary-line) on smartphones to help users focus on the page content.

---

## Page Layouts > Dynamic Page Web Component > Index

# Dynamic Page Layout
#### ui5-dynamic-page

Usage

**Metadata**

**Title**

**Breadcrumbs**

Description
dynamic behavior, a content area, and an optional
floating footer.

**uiElementsTechnology**

**designOwner**

**elementType**

**uiElementsStatus**

---

## Page Layouts > Dynamic Page Web Component > Usage

## Intro

The dynamic page is a generic layout control designed to support various floorplans and use cases.

Dynamic page

## When to Use

Do
Use the dynamic page if:
- You want to build a freestyle application that uses dynamic page layout components for SAP Fiori pages, such as the [dynamic page header](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-web-component#dynamic-page-header) and the footer [toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/toolbar-web-component/).
- You want to build a simple [object page](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/) with only one section.
- You want to use a full screen layout.
- You want to use dynamic pages in a [flexible column layout](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout-web-component/).
**Top Tips**

- Always use a header title – either as a text or link, or by including variant management.
- Use the header title and header content to provide the most relevant information and actions for your use case.
- Don’t remove or disable the actions within the global action toolbar when the header content is collapsed.
- Make sure that the layout actions in the [flexible column layout](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout-web-component/) are displayed correctly and never get hidden in the overflow.
- Start your application in [expanded mode](<https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout-web-component/" \l "starting-in-expanded-or-collapsed-mode>) if users need further content or adjustment options to get started.
- Offer the [pin feature](<https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout-web-component/" \l "pinning-the-header-content>) whenever users may need to fix the header content while scrolling through the page content.
- Don’t offer the pin feature for size S screens. This saves vertical space.
- Activate the [summary line](<https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout-web-component/" \l "summary-line>) on size S screens to help users focus on the page content.

## Anatomy

*Anatomy of the dynamic page*

+--------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------+
Requirements
+--------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------+
The dynamic page consists of a title, a header with dynamic behavior, a content area, and an optional floating footer.
1. **Dynamic page header**: Comprises the header title (a) and expandable/collapsible header content (b).
a. **Header title**: The title area contains a mandatory title element, along with optional elements such as breadcrumbs, subtitle/summary,
content, KPIs, and actions.
b. **Expandable/collapsible header content**: An area that can hold any components, depending on the use case. This content is hidden when the dynamic header collapses.
2. ***Expand Header*** **and** ***Pin Header*****buttons:** Buttons used to expand or collapse the header, and to pin or unpin the expanded header.
3. **Content area:** The content of the dynamic page.
4. **Optional:****Footer area:** A footer toolbar is used for finalizing page actions.
+--------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------+

## Types

### Freestyle Dynamic Page

In the freestyle dynamic page, any component can be
placed in the title and header content areas.
*Example of a freestyle dynamic page*

### Combining the Dynamic Page with the Flexible Column Layout

The dynamic page can be combined with the [flexible column layout](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout-web-component/).
For example, each column can contain its own dynamic page with a different floorplan, depending on the use case.

**> **Guideline:** **

In the flexible column layout, ensure that the icons for the *Close* or *Full Screen* / *Exit Full Screen* actions always stay on the very right.
Their position then remains stable, even if other actions are added (such as the paging buttons :slim-arrow-up: and :slim-arrow-down: ). The *Close* and *Full Screen* / *Exit Full Screen* actions must never move into the overflow.

### Dynamic Page for Floorplans

Many SAP Fiori floorplans use the dynamic page, or are
visually aligned to look the same (for example, overview
page, list report, worklist, object page, wizard).

## Behavior & Interaction

### Dynamic Page Header

The dynamic [page header](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/page-header/) supports three optional interaction patterns that can be combined. With [snap on scroll](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout-web-component/#snap-on-scroll) or [snap on click](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout-web-component/#snap-on-click), the header content can be collapsed or expanded. In addition, the header content can be fixed with the [pin feature](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout-web-component/#pinning-the-header-content).

By default, all three interaction patterns are combined and activated.

*Dynamic page header can be snapped | *Dynamic page header can be snapped | *The header content can be pinned*
on scroll*                          | on click*
### Starting in Expanded or Collapsed Mode

The dynamic header has both expanded and collapsed modes. By default, the header content is initially expanded.

You can opt to display the header in collapsed mode when the app is opened, deviating from the default. However, the idea is to always expand the header content when the application starts without a query.

*Dynamic page – expanded mode*

### Snap on Scroll

When the user scrolls down the page, the header content scrolls away. The header title switches to collapsed mode and stays fixed. When the user scrolls up the page, the header content expands again.

+-------------x-------------+
**Carousel (full-width)**

### Snap on Click

The snap on click pattern is another way of expanding and collapsing the header content. The user can collapse the header without scrolling, and expand it again even when it has been collapsed by scrolling down. This interaction only works in combination with expandable/collapsible header content.

There are two click options. Users can:

- Click the header title area
- Click the *Expand Header* icon button

This interaction pattern can be combined with [snap on scroll](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout-web-component/#snap-on-scroll).

#### Clicking the Header Title Area

The user can expand and collapse the header content by clicking anywhere on the header title area that has no active elements (like links or active buttons).

+-------------x-------------+
**Carousel (full-width)**

#### Clicking the Expand Header Button

The *Expand Header* icon button directly below the header can also be used to expand or collapse the header content.

+-------------x-------------+
**Carousel (full-width)**

### Pinning the Header Content

Activating the pin feature keeps the header expanded while the user scrolls through the page content. This interaction works only in combination with expandable/collapsible header content.

Dynamic page header with pin feature activated

## Responsive Behavior

### Responsiveness

The dynamic page is designed to adapt automatically to small, medium, and large screen sizes.

##### Dynamic Page in Sizes S, M, L, and XL

+-------------x-------------+
**Carousel (full-width)**

**> **Guideline:** **

On small screens, the *Pin Header* action is not provided, as the pinned header would take up too much screen real estate.

### Summary Line

To save vertical space on small screens, the dynamic page
header offers a smaller summary line instead of the
collapsed header.

The header content scrolls away as soon as the user
scrolls up the page.
The header converts to a summary line, which shows only
the title and an arrow icon button on the right of the
screen.

Tapping the summary line also expands and collapses the
whole header. The rest of the page stays in the same
position.
## Wrapping and Truncation

The dynamic page offers considerable freedom and flexibility.

### Global Actions

- Global actions stay as long as possible.
- If there is no key information, the title and the global
actions automatically get more space. The toolbar follows
the standard toolbar overflow guidelines.
### Title and Subtitle

- The title and subtitle wrap in expanded mode to offer the full text. This behavior needs to come from the respective controls for the title and subtitle.
- The title and subtitle truncate in collapsed mode to save vertical space.

Wrapping and truncation of the title and subtitle

### Layout Actions

The placement of navigation actions depends on the screen size:

- Less than 1280 px: Navigation actions are placed in a separate row above the global actions.
- 1280 px or more: Navigation actions are placed to the right of the global actions on the same line.

##### Example: Positioning of Layout Actions

+-------------x-------------+
**Carousel (full-width)**

---

## Page Layouts > Page Header > Index

# Page Header
####

Usage

**Metadata**

**Title**

**Breadcrumbs**

Description
tone, and adapts flexibly to varied app scenarios.

**uiElementsTechnology**
**designOwner**

**elementType**

**uiElementsStatus**

---

## Page Layouts > Page Header > Usage

## Intro

The page header is a crucial component of any application interface, serving as the first point of interaction for users. A well-designed header not only enhances navigation but also sets the tone for the entire user experience. This guideline is based on the dynamic page header, which offers a flexible structure and interaction capabilities to support a variety of application scenarios.

*Page header*

## When to Use

Do
Apply the page header guidance for the following page
types:
- Object list (list report)
- Analytical list
- Object page
- Guided process (wizard)
- Create page
- Overview
- Dashboard
## Anatomy

### Page header areas

1. **Header title**: The title area hosts the mandatory page title and the common, but optional elements – breadcrumbs, subtitle/summary, key information, and actions. When the header collapses, the title area remains visible, with the page title and actions always persistent. The contents can adapt between expanded and collapsed modes (for example, a list report can show the filter summary in the subtitle when collapsed).
2. **Header content**: A collapsible area which can hold any structured or unstructured content. The entire content is hidden when the header is collapsed.

*Anatomy of page header areas*

### Page header elements

1. **Title**: A title describes the purpose and/or the contents of the page.
2. **Breadcrumbs (optional)**: A breadcrumb is a type of secondary navigation that indicates the position of a page within the application hierarchy.
3. **Key information (optional)**: Key information is a dedicated section that showcases essential indicators of the page contents, such as KPIs or object status.
4. **Global actions (optional)**: Actions relevant for the entire page appear on the right-hand side of the header title bar. For more information, see [header toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/header-toolbar/).
5. **Layout actions (optional)**: Typical layout actions are the *Close*, *Full Screen*, or *Exit Full Screen* icons, which are mainly used when a page is presented in a [flexible column layout](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/flexible-column-layout/).
6. **Header feature (optional)**: Controls to expand/collapse and pin/unpin the header content. These controls are hidden if the header content area isn’t used.
7. **Header content (optional)**: The content varies based on the use case and floorplan. This area is used to display contextual information about the object or filters relevant to the page content. It’s hidden when the header is collapsed.
8. **Subtitle/summary (optional)**: A subtitle is a secondary text that supports the main title. It can also be used to display summarized header content, such as applied filters, when the header is collapsed.

*Elements of a page header*

## Behavior and Interaction

Since the page header is part of the dynamic page layout, it follows the same interaction patterns.

For more details on page header behavior and interactions, see the [dynamic page layout](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/).

### Expand and collapse

The page header supports expanded and collapsed modes. In the expanded mode, users can see more page-level information in the header. In the collapsed state, the header content area is hidden and the title shrinks, freeing vertical space for the page content. The page-level messages remain visible until the user dismisses them manually.

+-------------x-------------+
**Carousel (full-width)**

### Pin

Activating the pin feature keeps the header expanded while the user scrolls through the page content. This interaction works only in combination with expandable/collapsible header content.

To save vertical space, don’t offer the pin feature for size S screens.

*Dynamic page header with pin feature activated*

**> **Guideline:** **

To save vertical space, don’t offer the pin feature for size S screens.

## Responsive Behavior

The page header adapts automatically to all screen sizes based on the [responsive spacing system](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/spacing). For more details on page header responsiveness, see the [dynamic page layout](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/).

### Title and subtitle

The title and subtitle truncate in collapsed mode to save vertical space and wrap in expanded mode to show the full text. This behavior is provided by the respective controls. We recommend a maximum of two lines in collapsed mode to avoid an oversized header, especially on mobile when no summary line is present. Those two lines can be either a title with a subtitle, or a single longer title that wraps to two lines.

The title has the highest priority for space allocation. Elements that share the same horizontal space, such as key information and actions, move to overflow before the title wraps or truncates.

For more information, see [Wrapping and Truncation](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/wrapping-and-truncation).

*Title and subtitle wrap in expanded mode and truncate in collapsed mode*

### Key information

Key information, such as a generic tag or KPI (middle
area, left-aligned), remains visible as long as possible
before moving into the overflow. If no key information is
present, the title and global actions automatically
receive more space.
**> **Guideline:** **

Be mindful of the space available for key information. To avoid excessive truncation or wrapping of the page title
and to prevent key information from being hidden in overflow, use header content if multiple indicators need to be
displayed.

### Global actions

Global actions also remain visible as space allows.
The toolbar follows standard overflow behavior, moving actions into the overflow menu from right to left.
For more information, see [Toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/toolbar-overview/).
### Layout actions

The placement of layout actions depends on the page width:

- **Screen size S, M**: Layout actions appear in a separate row above the global actions.
- **Screen size L, XL or more**: Layout actions appear to the right of the global actions on the same line.

This breakpoint is based on the page width, not the window width, and applies regardless of whether the page is used in the flexible column layout, on desktop, or on mobile.

*Size L: Layout actions next to global actions*

*Size S: Layout actions above global actions*

## Best Practices

### Title

Every application page must have a visible title in the page header that describes its topic and purpose.

Make the title concise. Remove non-essential words to improve scannability and to avoid excessive wrapping or truncation when space is limited.

If using an object name or ID as the title, ensure it’s identifiable. Add the type before the name/ID to help the user identify the object, if needed. Use the format "Object type: \<Object name/ID>".  For example, "Order: A100201".

There are two types of title in page header:

**A. Static:** A simple, static text [title](https://www.sap.com/design-system/fiori-design-web/ui-elements/title/) in the page header.
**B. Dynamic:** A title that contains dynamic elements, such as variant management.

*Page title types*

#### Accessibility requirements

Every page must have a single static \<h1> heading that describes its topic and purpose. Dynamic elements – such as variant management components or input fields – don’t qualify, because their labels change, and assistive technologies can’t rely on them to identify the page.

The \<h1> can be visible or visually hidden, but it must always be present in the DOM. If a visible heading suits the design, add a simple text title (\<h1>) alongside the dynamic element. If a visible heading doesn’t fit, insert an \<h1> at the top of the page using a screen-reader-only technique. The heading won’t appear on screen but remains fully accessible to assistive technologies.

### Page-level avatar

You can add a page-level avatar to the page header title area or header content area.

Use a size S avatar before the page title and subtitle in the title area. In the header content area, pick the size based on the other elements.

Use only one avatar per header in expanded and collapsed modes.

For more information, see [Avatar](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar/).

*Page-level avatar in collapsed mode*

### Global actions

The global actions toolbar located in the page header contains actions that are valid for the entire page, except for the closing and finalizing actions that end the current process.

- Use text buttons for all business specific actions.
- Use icon buttons for all generic actions, such as *Favorite*, *Flag*, *Share*, and paging.
- Use no more than one primary button to highlight the most important action for the page.
- Since space is limited, try grouping related actions using menu buttons.
- Use an overflow toolbar if there are multiple global actions. This activates the overflow when there isn't enough space. The app team can decide which actions can move into the overflow and which actions are so important that they should never move into the overflow.

For more information, see [Toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/toolbar-overview/).

*Global actions in the page header*

### Page-level breadcrumbs

Presenting the current page in breadcrumbs is optional but must be consistent across all pages within a product.

In applications with a fixed hierarchy, use static breadcrumbs. These breadcrumbs always display the current page location the same way, regardless of how the user arrives there.

Consistent presentation of breadcrumbs throughout the product helps users orient themselves and sets clear expectations. Breadcrumbs should consistently start from the same hierarchy level to improve usability.

#### Breadcrumb patterns

Use the breadcrumb patterns described below for each navigation level.
Note: Underscore indicates a navigable link.

**Table (col-width-50-50)**

**Use Case**

On **home page**

**Multiple tab pages on the home page**

**Navigation item (L1)** in the side navigation menu is **navigational**
<u>Home</u> / Current page (L1 item)
On a **navigation subitem (L2) landing page:**
<u>Home</u> / <u>L1 item</u> / Current page (L2 item)
Drilling down to the **subsequent child page:**
<u>Home</u> / <u>L1 item</u> / <u>L2 item</u> / Current page
*Breadcrumb examples when L1 is navigational*

**Navigation item (L1)** in the side navigation menu is **not navigational**
<u>Home</u> / L1 item: Current page (L2 item)
Drilling down **from L2 landing page to an object:**
<u>Home</u> / <u>L1 item: L2 item</u> / Current page (object)
*Breadcrumb examples when L1 is not navigational*

#### "Back to" link

You can include an additional link before the breadcrumbs for quick access to
a previously visited page that isn’t part of the current hierarchy.
*Breadcrumb example with an extra “Back to” link*
Use a descriptive label like *Back to Project XYZ* to specify the destination.
If you need a persistent back button that functions like the browser back
button but can’t depend on the browser’s back button, use the back button in
the shell bar.
### Header content

Depending on the use case, the header can include various elements such as filters, charts, or forms. See [Use Cases and Page Types](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/page-header/#use-cases-and-page-types).

If no extra header content is required, use a single, static header without expand/collapse functionality.

*No header content, without expand/collapse feature*

## Use Cases and Page Types

The page header can display different elements based on the use cases or page types. The following are some of the common use cases.

### List report (object list)

A list report page enables users to view and manage a large collection of items. Users can locate and interact with relevant items using the search and filter options in the page header. It often serves as an entry point for navigating to item details, which are typically displayed on an object page.

#### Recommended page title syntax

Use the object type in plural form as the page title (for example, *Purchase Orders*). If variant management is used, provide a meaningful, descriptive label for the default view, such as *Active Orders*.

**Mandatory elements**
- Title (text, variant Management, or both)
- Subtitle (show filter summary when the header is
collapsed)
- Header content (search, filter or smart filter bar)
- Header features (pin, expand/collapse)

For more information, see [List Report Floorplan](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/).

*Example of a list report page header with a filter bar*

### Analytical list page

An analytical list page enables users to analyze large datasets, identify root causes, and take action on transactional content. It helps users find interesting areas within datasets or significant individual instances through data visualization and business intelligence. A [visual filter bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/visual-filter-bar/), consisting of a set of interactive charts, offers a unique way to filter large datasets via visualization and is included in the page header.

#### Recommended page title syntax

Use the object type in plural form as the page title (for example, *Suppliers*). If variant management is used as the page title, provide a meaningful, descriptive label for the default view, such as *Active Suppliers*.

**Mandatory Elements**
- Title (text, variant management, or both)
- Subtitle (show filter summary when the header is
collapsed)
- Header contents (visual filter bar, filter bar)
- Header feature (pin, expand/collapse)

For more information, see [Analytical List Page Floorplan](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/).

*Example of an analytical list page header with a visual filter bar and filter toggle*

### Object page

The object page displays and organizes all relevant information about an object. It can be in display or edit mode. The page header provides context to help the user identify the object shown and the actions they can take.

#### Recommended page title syntax

Use the object name or object ID directly as the page title. If the object name or ID is unclear, append the object type in front to provide the context (for example, *Order Item: 019204X*), or use the subtitle for context.

**Mandatory Elements**
- Title (text)
- Subtitle
- Key information
- Global actions
- Header content (form, text, avatar, key value, micro
chart, progress indicator, rating indicator)

For more information, see [Object Page Floorplan](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/).

*Example of an object page header with context information*

### Wizard page

A wizard page assists users in completing lengthy or complex tasks by dividing them into sections and guiding them step-by-step. It includes two types of screens: walkthrough screens and a summary screen. A progress bar, which can be either in anchor or tab mode, is located just below the page header to help users follow their progress. When an anchor bar is used, the summary page appears as a separate screen. With a tab bar, the summary is usually the final step. Typically, use a wizard page for tasks with 3 to 8 steps.

#### Recommended page title syntax

If the wizard page is used to create new object, use the format, New \<Object Type>, as the page title. For example, New Customer. If the wizard page is used to walk users through a complex process, use the process name as the page title. For example, Check Out.

If the wizard page is used to create a new object, use the format "*New \<Object Type>*" as the page title (for example, *New Customer*). If the wizard page is used to walk users through a complex process, use the process name as the page title (for example, *Check Out*).

**Mandatory Elements**
- Title (text)
- Progress bar
- Global actions

For more information, see [Wizard Floorplan](https://www.sap.com/design-system/fiori-design-web/ui-elements/wizard/).

*Example of a wizard page header with a progress bar*

### Create Page

A "create" page is an object page in create mode.

#### Recommended page title syntax

Use the format “*New \<Object Type>*” as the page title (for example, *New Customer*). This page title can be replaced with the actual object name or object ID as soon as it is entered or generated.

**Mandatory Elements**
- Title (text)
- Subtitle
- Key information (draft/version switcher)
- Global actions

For more information, see [Object Page Floorplan](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/).

*Example of a page header for a "create" object page*

---

