# SAP Fiori Elements

SAP Fiori Elements provides predefined templates for common app patterns.

## Contents

- [Ai Features > Ai Input Assistance](#ai-input-assistance)
- [Analytical List Page Overview Page Sap Fiori Elements 2](#analytical-list-page-overview-page-sap-fiori-elements-2)
- [List Report > List Report Content Area Fiori Elements](#list-report-content-area-fiori-elements)
- [List Report > List Report Header Sap Fiori Elements](#list-report-header-sap-fiori-elements)
- [List Report > Worklist Sap Fiori Elements](#worklist-sap-fiori-elements)
- [Object Page > Object Page Content Area Sap Fiori Elements](#object-page-content-area-sap-fiori-elements)
- [Object Page > Object Page Footer Bar Sap Fiori Elements](#object-page-footer-bar-sap-fiori-elements)
- [Object Page > Object Page Header Sap Fiori Elements](#object-page-header-sap-fiori-elements)
- [Object Page > Object Page Overview Sap Fiori Elements](#object-page-overview-sap-fiori-elements)
- [Smart Templates](#smart-templates)
- [Tables And Lists > List Sap Fiori Elements](#list-sap-fiori-elements)
- [Tables And Lists > Table Features Sap Fiori Elements](#table-features-sap-fiori-elements)
- [Tables And Lists > Table Rows Sap Fiori Elements 2](#table-rows-sap-fiori-elements-2)
- [Tables And Lists > Table Types Sap Fiori Elements](#table-types-sap-fiori-elements)
- [Tables And Lists > Tables Toolbar](#tables-toolbar)

---

## Ai Input Assistance

# AI Input Assistance

## Intro

AI input assistance eases data entry for a new or existing object by recommending values for the input fields, based on previous input or business data. The intelligent suggestions are displayed as recommended values in the input fields for users to accept or to reject.

After the user rejects a recommended value, the AI input assistance doesn’t recommend it again until the user ends the “object session,” by saving and closing the object. Instead, it recommends other available values.

All values rejected in one object session become available for recommendation again in the next session after the user reopens the closed object or opens another object to create or edit it.

AI input assistance is available in applications developed with SAP Fiori elements for OData V4.

*Input field with grouped recommendations and autocomplete suggestions*

## When to Use

Do
Use the AI input assistance in workflows where the user
enters data in input fields on the object page:
- When the user’s intent is unpredictable
- To streamline repetitive or common actions, for
example, creating many objects of the same type
- To enhance and speed up the user’s workflow
- When previously entered data is available to propose
with intelligent recommendations for input fields
**> **Information:** **

Input assistance isn't available for the following fields:
- Fields without value help (except those with a dropdown list)
- Fields with multiple values
- Custom fields
- Fields that have more than one key field in their value help entity. For example, if the field "Plant" has two key
fields, namely "PlantID" and ''RegionID", to uniquely identify a given plant, the field "Plant" must be excluded from
providing recommendations.

## Anatomy

The AI input assistance extends the following components and properties to enable new AI-specific interactions:

- [Input field](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/)
- Input field with [autocomplete suggestions](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/#autocomplete-suggestions) and [grouping](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/#grouping)
- Input field with [tabular suggestions](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/#tabular-autocomplete) and [grouping](https://www.sap.com/design-system/fiori-design-web/ui-elements/input-field/#grouping)
- Unaccepted recommendations [message box](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-box/)

### Input Field

1. **Label**
2. **AI-recommended value** is displayed in placeholder text
3. **Input field** in the information value state

### Grouped Recommendations and Suggestions

1. **Message strip** at the top of the select dropdown displays a message to inform the
user of the AI recommendations
2. **Group header “Recommendations”** followed by the AI-recommended values in the dropdown
3. **Group header “Other”** followed by the remaining items in the dropdown

### Unaccepted Recommendations Message Box

Anatomy of the ‘Unaccepted Recommendations’ dialog

1. **Information icon and header**
2. **Label of each input field** with the value of the unaccepted recommendation
3. **Footer with buttons** for accepting the recommendations, ignoring them, or continuing to edit the object by closing the dialog without acting on the recommendations

## Behavior & Interaction

Recommendations are displayed in empty input fields on an object page in both create and edit modes.

The display of additional recommendations or new recommended values are triggered when the user:

- Scrolls to a new section
- Displays a new tab
- Creates a new table row inline
- Refreshes the object page
- Changes the value of a field that is configured for recommendation update

The user can accept or reject the recommendations:

- Individually via the input field
- As a group in the *Unaccepted Recommendations* dialog

After the user rejects a recommended value, the AI input assistance doesn’t recommend it again until the user ends the “object session,” by saving and closing the object. Instead, it recommends other values, if available.

All values rejected in one object session become available for recommendation in the next session after the user reopens the closed object or opens another one to create or edit it.

### Accepting or Rejecting Recommendations in the Input Field

Input field with recommendations

**A.** The input field displays the recommended value in the information value state and placeholder text. Only one recommended value is visible in the field, although there may be others.

**B.** The user selects the input field, and the dropdown menu is displayed with a message strip that highlights the recommended value or values.

- To accept a recommended value, the user selects it from the dropdown.
- To reject the recommended value, the user selects a different value.

**C.** The input field displays the selected value in a regular state.

### Accepting or Rejecting Recommendations in the “Unaccepted Recommendations” Dialog

The *Unaccepted Recommendations* dialog is displayed after the user selects the create or save action, before acting on all the recommendations for each input field.

In the dialog, the user selects the actions to apply to all the unaccepted recommendations or the action to continue editing the object.

#### Unaccepted Recommendations Dialog

+----------------------------------------x----------------------------------------+
**Table (col-width-20-80)**

Button

*Accept and Create*
the corresponding input fields.
*Accept and Save*
If all the required fields have values, the object is
also created or saved.
If not, the create or save action is blocked. An error is
displayed in the message popover.

*Reject and Create*
the corresponding input fields.
*Reject and Save*
If all the required fields have values, the object is
created or saved.
If not, the create or save action is blocked. An error is
displayed in the message popover.

*Continue Editing*

---

## Analytical List Page Overview Page Sap Fiori Elements 2

# Analytical List Page / Overview Page

+------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------+
+------------------------------------------------------------x-------------------------------------------------------------+-----------------------x-----------------------+
## This page has been deprecated and is no longer available.
This page was deprecated with guideline version **1.142**.
#### Reason for deprecation
It was redundant with information available in other articles.
#### Looking for the latest information?
Visit these pages
- [Analytical List Page](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/analytical-list-page/)
- [Overview Page (OVP)](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/overview-page/)

---

## List Report Content Area Fiori Elements

# List Report – Content Area

**> **Information, External_Only:** **

No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData
V4.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with
their behavior – both standalone and when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).


No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData V4.
For information on the latest release of both versions of SAP Fiori Elements, see: [What's New](https://ui5.sap.com/#/topic/99ac68a5b1c3416ab5c84c99fefa250d) in SAPUI5 documentation.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with their behavior – both standalone and
when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## Intro

The SAP Fiori elements list report template supports the three content area layouts detailed below.

For design information, see [General Layout](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/#general-layout) and the links below.

## Simple Content Layout

The default layout for the content area is the simple content layout and displays the data for one business object in a single table view. It supports:

- Display of one business object in one table, or — with SAP Fiori elements for OData V2 — in one list
- Automatic data loading
- One table toolbar
- Creation of business objects via a dialog
- Creation of cards for the *Insights* section of *My Home* in SAP S/4HANA Cloud, when My Home in SAP S/4HANA Cloud has been enabled. The *Add Card to Insights* option automatically appears in the overflow toolbar of the table in list report. You can turn off this feature.

> **Warning:** - We **strongly recommend against** table-level view management, but it is supported.
- With SAP Fiori elements for OData V4 these restrictions apply for the Insights cards:
- When users navigate from the card in the *Insights* section of the *My Home* page to the list report table, the table
view is similar to its state at card creation, but it does not retain the changes in the position or removal of filter
fields or table columns.
- The formatting of unit of measure fields differs between the Insights card and the list report table.

> **Hint:** For more information on card creation and disabling it, refer application developers to [Creating Cards for the Insights Section of My Home in SAP S/4HANA Cloud](https://sapui5.hana.ondemand.com/#/topic/9b13559ef978405a99e8b624a87daf31).

Columns

*Simple content layout (default)*
## Multiple View Layout

For more complex scenarios, you can turn on the multiple view layout which supports:

- Display of multiple views of a table that shows one business object, for example, each view of the same table can display different prefiltered states
- The segmented button for a maximum of three views or the select control for four or more views
  Note that the SAP Fiori elements framework determines the switch control automatically based on the number of views.
- Display of the count or number of total rows in the view (must be enabled)
- One table toolbar
- Automatic data loading
- Creation of business objects via a dialog with SAP Fiori elements for OData V2
- Creation of cards for the *Insights* section of *My Home* in SAP S/4HANA Cloud, by default when My Home in SAP S/4HANA Cloud has been enabled. You can turn off this feature.

> **Warning:** - We **strongly recommend against** table-level view management, but it is supported.
- With SAP Fiori elements for OData V4 these restrictions apply for the Insights cards:
- When users navigate from the card in the *Insights* section of the *My Home* page to the list report table, the table
view is similar to its state at card creation, but it does not retain the changes in the position or removal of filter
fields or table columns.
- The formatting of unit of measure fields differs between the Insights card and the list report table.

> **Hint:** For more information on card creation and disabling it, refer application developers to [Creating Cards for the Insights Section of My Home in SAP S/4HANA Cloud](https://sapui5.hana.ondemand.com/#/topic/9b13559ef978405a99e8b624a87daf31).

Columns

*Multiple view layout - Segmented button*

## Multiple Content Layout

To support even more complex scenarios, you can turn on the multiple content layout which supports:

- Display of one or more business objects in multiple tables, for example, you can display a customer overview with different tables for invoices, deliveries, and overdue payments. All the tables can be filtered by a specific customer and a specific date
- Text-only icon tab bar to switch among the tabs
- Views with data visualization in either table or chart format with both SAP Fiori elements for OData V2 and V4
- Automatic data loading
- Different toolbars for each view

> **Warning:** - We **strongly recommend against** table-level or chart-level view management, but it is supported.
- Creation of business objects **must** be done in an object page. Doing it via a dialog is not supported
- **Do not** use a mix of responsive and non-responsive tables.

> **Hint:** Application developers may be unfamiliar with the designer term “multiple content layout.”
For more information on implementing this feature, refer the development team to:
- [Defining Multiple Views on a List Report Table – Single Table Mode](https://sapui5.hana.ondemand.com/#/topic/0d390fed360c4c58a0f0619338938de1)
- [Defining Multiple Views on a List Report Table – Multiple Table Mode](https://sapui5.hana.ondemand.com/#/topic/37aeed74e17a42caa2cba3123f0c15fc)

Columns

*Multiple content layout*

---

## List Report Header Sap Fiori Elements

# List Report – Header

**> **Information, External_Only:** **

No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData
V4.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with
their behavior – both standalone and when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).


No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData V4.
For information on the latest release of both versions of SAP Fiori Elements, see: [What's New](https://ui5.sap.com/#/topic/99ac68a5b1c3416ab5c84c99fefa250d) in SAPUI5 documentation.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with their behavior – both standalone and
when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## Intro

The SAP Fiori elements list report template supports the features and settings for the list report header detailed below.

For design information, see the [List Report Floorplan](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/) guidelines and the links below.

> **Warning:** Put all controls for searching and filtering data in the list report filter bar.
**Do not** include the search or filter options that are available in the table header.

## Feature Availability

Table

#### Features

[Page-Level View Management](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/list-report/list-report-header-sap-fiori-elements#page-level-view-management)

[Share Menu](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/list-report/list-report-header-sap-fiori-elements#share-menu)

[Manual Update Mode](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/list-report/list-report-header-sap-fiori-elements#update-mode)

[Live Update Mode](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/list-report/list-report-header-sap-fiori-elements#update-mode)

[Search](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/list-report/list-report-header-sap-fiori-elements#search)

[Filter Bar](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/list-report/list-report-header-sap-fiori-elements#filter-bar)

[Initial State of Header](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/list-report/list-report-header-sap-fiori-elements#initial-state-of-header)
- Expanded on large screens
- Collapsed on medium and small screens when the
application is configured to load the list report data on
app launch

[Pin Button](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/list-report/list-report-header-sap-fiori-elements#pin-button)
list report contains at least one responsive table.

[Editing Status Filter](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/list-report/list-report-header-sap-fiori-elements#editing-status-filter)
You can hide it.

[Input Controls for Filters](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/list-report/list-report-header-sap-fiori-elements#input-controls-for-filters)

[Adapt Filters UI Element](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/list-report/list-report-header-sap-fiori-elements#adapt-filters)
- Default: popover with SAP Fiori elements for OData V4

## Feature Details

### Page-Level View Management

By default, page-level view management is enabled and the header displays a page title.

You can disable it.

> **Guideline:** If you disable page-level view management, you must display a header title.

For more information, see [Header Title](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#header-title).

### Share Menu

By default, the header contains the generic *Share* menu with the global actions *Send Email* and *Save as Tile.* It can also include the:

- *Share in SAP Jam* menu item when SAP Jam integration is configured.
- *Microsoft Teams > As Chat* and *As Card* options when the required settings have been made by the system administrators of SAP S/4HANA or SAP S/4HANA Cloud. This feature is part of collaborative ERP (enterprise resource planning), which integrates the best of SAP S/4HANA or SAP S/4HANA Cloud with Microsoft Teams. It’s not available for all users. When available, the menu item opens a separate window where users can directly share a link to a business application in the SAP S/4HANA or SAP S/4HANA Cloud system with co-workers.

\With SAP Fiori elements for OData V4, you can control the visibility in the *Share* menu of the *Send E-mail* and *Share: Microsoft Teams*.
**Save as Tile**

The tile created opens the list report with the same results shown at the time the tile was saved.

Users can also save a dynamic tile for results shown after the users have filtered for a relative date value, such as today or this year.

For more information, see:

- [Share (Generic)](https://www.sap.com/design-system/fiori-design-web/ui-elements/header-toolbar/#share-generic-4)
- [Collaboration](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/collaboration)

> **Hint:** For more information, refer application developers to:
- [The Share Functionality](https://ui5.sap.com/#/topic/022bf0dcae1d4d90961ebe23d642fca3)
- [Integrating Microsoft Teams](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/257ec7408db6420682462cd1d000e744.html) for SAP S/4HANA Cloud
- [Integration with Microsoft Teams](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/849465e69b7a490a88049fe0b24fb01e.html?version=2023.000) for SAP S/4HANA

### Update Mode

By default, the update mode is manual.

You can enable live update mode instead.

For more information, see [Update Mode](https://www.sap.com/design-system/fiori-design-web/ui-elements/filter-bar/#update-mode).

### Search

By default, the search is disabled.

You can enable it.

The limit for search strings is 1000 characters.

> **Guideline:** Work with the development team to define the searchable properties in the data.

For more information, see [Search](https://www.sap.com/design-system/fiori-design-web/ui-elements/search/).

### Filter Bar

SAP Fiori elements for OData V2 uses the [smart filter bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/smart-filter-bar-annotations/).

SAP Fiori elements for OData V4 uses the [filter bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/filter-bar/).

With SAP Fiori elements for OData V4, you can also show a *Clear* button on the filter bar to let users:

- Remove all filter values
- Reset the value in the *Editing Status* filter to All

> **Warning:** Put all controls for searching and filtering data in the list report filter bar.
**Do not** include the search or filter options that are available in the table header.

### Initial State of Header

The default behavior is shown below:

Table

#### Screen Size | #### Application Starts with Data | #### Application Starts without Data

**S**            | Collapsed                         | Expanded

**M**            | Collapsed                         | Expanded

**L**            | Expanded                          | Expanded

**XL**           | Expanded                          | Expanded

### Pin Button

With SAP Fiori elements for OData V4, the *Pin* :pushpin-off: /*Unpin* :pushpin-on: buttons are displayed under the header when a list report contains at least one responsive table,

The pin option keeps the header collapsed or expanded when the user scrolls.

The grid table and the analytical tables are not scrollable so the *Pin* :pushpin-off: /*Unpin* :pushpin-on: buttons are **not** displayed when the list report contains only these types of table.

For more information see, [Pinning the Header Content](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#pinning-the-header-content).

### Editing Status Filter

By default, the filter is enabled for draft-enabled applications. You can disable it.

The filter is a select control. Its values and corresponding results are as follows:

- *All* (Default value):
  - All saved (or active) versions of the documents for which the current user has no drafts
  - All the users own drafts of unsaved changes to existing documents. The version last saved before the user began editing the draft is not shown in the results.
- *All (Hiding Drafts)*: Only the saved objects.
- *Own Draft*: Drafts that the current user can display or edit.
- *Locked by Another User:* Saved versions that are locked by other users. The current user cannot edit these versions.
- *Unsaved Changes by Another User*: Saved versions that were edited by another user but are no longer locked. The current user can edit and overwrite these versions, and the previous draft will be overwritten.
- *No Changes*: Saved versions with no corresponding draft.

For more information, see [Draft handling](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/draft-handling).

### Input Controls for Filters

You can decide which filter/input controls to use and set the following for them:

- The properties available as a filter criterion
- The labels for the filter fields
- The default filter values
- Mandatory filters: Marked by an asterisk (\*), they always show in the filter bar.
- Type-ahead for values entered
- Value help lists
  By default, a dialog conditions tab is displayed for the value help. Remind application developers to define the right value help options.

> **Hint:** For information on defining the value help, refer application developers to [Field Help](https://ui5.sap.com/sdk/#/topic/a5608eabcc184aee99e1a7d88b28816c).

You can also:

- Decide on the selection controls for the filters
- Restrict the values accepted in the field. By default, the field accepts multiple values.

> **Guideline:** **Date Picker and Date / Time Picker**
By default, filter fields for the date picker (sap.m.DatePicker)and date/time picker (sap.m.DateTimePicker) result in a control that opens a dialog for adding **multiple** dates.
When your use case requires a date/time picker for a **single** value, specify this to the the application developers because it requires explicit configuration.
For more information refer them to: [Configuring Filter Fields](https://ui5.sap.com/#/topic/f5dcb29da3bf4e0091eba3e7ccef4580).

For more information, see:

- [Filter/Input Controls](https://www.sap.com/design-system/fiori-design-web/ui-elements/filter-bar/#filter-input-controls)
- [Selection Controls](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/which-selection-control-to-use)

### Adapt Filters

By default, SAP Fiori elements for OData V2 uses the *Adapt Filters* dialog and SAP Fiori elements for OData V4 uses the *Adapt Filters* popover.

You can configure the following:

- Filters that are initially visible in the expanded filter bar. When you set filters to be visible by default, they are displayed under the Basic group in the dialog.
- Additional groups for the filters
- Show input fields: Visible by default. You can hide the *Hide value/Show value* button.

Users can add additional fields through views.

The *OK* and *Cancel* buttons are displayed when the application team or the user has chosen manual [update mode](https://www.sap.com/design-system/fiori-design-web/ui-elements/filter-bar/#update-mode) for the filter bar.

By default, the *Reset* button is displayed, you cannot change this.

For more information, see: [Adapt Filters](https://www.sap.com/design-system/fiori-design-web/ui-elements/smart-filter-bar-annotations/#filter-dialog).

---

## Worklist Sap Fiori Elements

# Worklist

**> **Information, External_Only:** **

No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData
V4.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with
their behavior – both standalone and when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).


No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData V4.
For information on the latest release of both versions of SAP Fiori Elements, see: [What's New](https://ui5.sap.com/#/topic/99ac68a5b1c3416ab5c84c99fefa250d) in SAPUI5 documentation.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with their behavior – both standalone and
when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## Intro

With SAP Fiori elements, the worklist is a simplified list report without a filter bar and shares many features and settings with the list report that are described in the SAP Fiori elements list report articles.

The worklist features and settings that differ from those in the list report are detailed below.

For design information, see the [Worklist Floorplan](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/work-list/) guidelines and the links below.

## Feature Availability

Table

#### Worklist-Specific Features

View Management Not Enabled

Page-Level View Management

Header Title

Filter Bar

Table Title

Table Behavior

Search

Personalization Actions Enabled: *Sort, Filter, Group,* and *Column Settings*

Export to Spreadsheet

---

## Object Page Content Area Sap Fiori Elements

# Object Page – Content Area

**> **Information, External_Only:** **

No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData
V4.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with
their behavior – both standalone and when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).


No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData V4.
For information on the latest release of both versions of SAP Fiori Elements, see: [What's New](https://ui5.sap.com/#/topic/99ac68a5b1c3416ab5c84c99fefa250d) in SAPUI5 documentation.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with their behavior – both standalone and
when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## Intro

The SAP Fiori elements object page template supports the features and settings for the object page content area detailed below.

For design information, see the [Object Page Floorplan](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/) guidelines and the links below.

> **Warning:** **Always** build the object page using the [dynamic page header](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/#dynamic-page-header-mandatory).
Set the [shellbar page title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/shell-bar/#page-title) to the name of the business object shown in the object page to indicate the user’s position in the system.
**Do not** use the current implementation of the “page view management” feature in SAP Fiori elements. This feature is technically available for object pages, but we are still working on the final design.

## Feature Availability

Table

#### Content Area

[Draft Object Validation](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#draft-object-validation)
Users can trigger the validation by pressing the Enter key while their cursor is in a field on the object or subobject page.

[Navigation Bar: Anchor Bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#navigation-bar)

[Navigation Bar: Tab Bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#navigation-bar)

[Sections and Subsections](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#sections-and-subsections)

[Reuse Components as Sections](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#reuse-components-as-sections)

#### Subsections

Link
With SAP Fiori elements for OData V4, you can display an [icon or image with the link](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/link/#link-with-icon).
With SAP Fiori elements for OData V2, the default link shows the text and ID. You can remove the text or the ID.

[Contact Facets](https://sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#contact-facets)

[Tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#tables)

[Charts](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#charts)

[Views for Tables and Charts](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#views-for-tables-and-charts)

[Address](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#address)

Display of Related Properties Together
The properties can also display as links.

[Forms](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#forms)
The number of columns in a form depends on the screen size. With SAP Fiori elements for OData V2 you can change the number of columns for an extra large screen size.

[Text Control](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#text-control)
You can:
- Change the maximum
- Enable growing mode
- Show users the number of characters allowed in the text area

[File Upload](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#file-upload)

[Dynamic Side Content](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#dynamic-side-content)

#### Subsection Behavior

[Subsection Starts Loading After the Object Page Elements Are Loaded](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#subsection-loading-behavior)

[Adjustment of the Width for Content Display in a Subsection](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#width-for-content-display-in-a-subsection)

#### Content Visibility

[Visible Sections, Subsections, Quickviews, and Tables](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#sections-subsections-quickviews-and-tables)

[Hiding Section, Subsection, Quickview and Table Content](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#sections-subsections-quickviews-and-tables)

[User-Controlled Visibility with *Show More/Show Less*](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#usercontrolled-visibility)

[Visible Smart Form Fields](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-content-area-sap-fiori-elements#visibility-of-smart-form-fields)

\
## Content Area

### Draft Object Validation

By default, data validation for the object page happens only when the users save the object so they enter data without interruption.

They can trigger data validation by pressing the **Enter** key while their cursor is in a field on the object or subobject page.

For more information, see: [Form Field Validation](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/form-field-validation/)

### Navigation Bar

By default, the anchor bar is generated when the object page has **more than one** section.

It lets users navigate to the individual content area sections.

You can:

- Hide the anchor bar when you only have one section.
- Replace it with a tab bar.

**With extensions**, you can replace the buttons with another type of control.

If there is no Anchor Bar, but there is editable information in the header, the first temporary section in the Object Page which controls the header content will have a section title called ‘Header’.

For more information, see:

- [Navigation Bar](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/?external#navigation-bar)
- [Anchor Bar Navigation](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#anchor-bar-navigation)
- [Tab Bar Navigation](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/?external#tab-bar-navigation)

### Sections and Subsections

You can add sections and subsections to the content area.

Sections contain only subsections. You build the subsection content with tables, charts, and forms.

When the object page uses:

- Tab bar navigation, the section title isn’t displayed in the content area
- Anchor bar navigation, only the title of the first section is hidden in the content area, unless the first section contains a table

> **Guideline:** When you assign a section or subsection title, do not use a comma (,) in it because commas serve as delimiters in SAP
Fiori elements.

#### Section and Subsection Titles

To minimize both the number of titles displayed and redundancies among the title values:

- When a section or subsection contains a single table or chart control, only the control title is displayed, but its value is replaced by the section or subsection title.
- For sections or subsections that contain a single text area, with SAP Fiori elements for OData V4, application teams can enable an option to display the section or subsection title instead of the text area label when the object page is in display mode. With the option enabled, the label is only displayed in edit mode if the field is mandatory.

For more information, see: [Sections and Subsections](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/#sections).

### Reuse Components as Sections

You can embed a reuse component as a section in the object page.

> **Warning:** A reuse component that is used in an SAP Fiori elements-based application cannot be used in a freestyle application.
Consult the development team on the requirements for the reuse component.

## Subsections

### Contact Facets

With both versions of SAP Fiori elements, in subsections, you can include a link that users can click to see additional information in a quickview.

For applications with Microsoft Team integration, the contact card and the quick view card both display options for starting a Microsoft Teams audio call, video call, or chat with the contact.

For more information, see:

- [Smart Link](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/smart-link/)
- [Quick View](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/quickview/)
- [Quick View Examples](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/quickview/#quick-view-examples)

### Tables

You can include a table in a subsection.

When a table is the only content in a subsection, the subsection title is not displayed. Instead, the title of the table shows the value assigned to the subsection title.

For more information on SAP Fiori elements capabilities for tables, see the articles under SAP Fiori Elements: Table, starting with [Table Types](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-types-sap-fiori-elements).

### Charts

You can include a single chart facet in a subsection.

In the chart, you can:

- Display measures, their aggregation calculations, and dimensions to categorize the measures.
- Add custom actions to the toolbar for a chart and define whether they are enabled at all times or only after the user selects part of the chart for the action.
- Allow users to personalize the chart settings

When a chart is the only content in a subsection, the subsection title is not displayed. Instead the title of the chart shows the value assigned to the subsection title.

#### SAP Fiori Elements for OData V2

Charts are only supported for business objects or services that are **not draft enabled** or are **read-only**.

#### SAP Fiori Elements for OData V4

You can define a chart for a draft-enabled business object. The chart only displays active data, not data entered into an unsaved draft record.

For more information, see [Chart (VizFrame)](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/chart/).

For more information on chart options, see Chart.

> **Hint:** For more information, refer application developers to [Configuring Charts](https://ui5.sap.com/#/topic/653ed0f4f0d743dbb33ace4f68886c4e).

### Views for Tables and Charts

You can turn on views for:

- All the tables and charts on the page
- Individual tables and charts

For more information, see [Views (Variant Management)](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/variant-management/).

### Address

You can add one or more address fields:

- As a separate subsection
- As part of a field group within a subsection
- To a quick view with smart link navigation

For more information, see:

- [Quick View](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/quickview/)
- [Quick View Examples](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/quickview/#quick-view-examples)

### Display of Related Properties Together

You can display two related properties side-by-side and
with a single label in display mode.
*Related properties as links*
For example, the label *Date Time* can display with the
properties date and time side-by-side, even when they are
distinct properties in the back end.
You can separate the values with a delimiter such as a
slash (/) or a hyphen (-).
In edit mode, the fields can be edited separately.
#### Related Properties as Links
The related properties can also display as links.
> **Hint:** Application developers call the related properties semantically connected fields. For more information on this
feature, you can refer them to [Grouping of Fields](https://ui5.sap.com/#/topic/cb1748ea9b984251addc03718d98df35).

### Forms

You can add action buttons to the toolbar for a form contained in a subsection.

With SAP Fiori elements for OData V4, you can also add an action next to the form header.

The action types can be:

- Actions that occur in the system while the user stays on the object page.
- Actions that navigate to a different application, for example, when the user can open a purchase requisition from a specific purchase order.

#### Conditional Enablement of Navigation Buttons

You can enable buttons that navigate the user to another page or application based on the value of a specific field with SAP Fiori elements for OData V4. To achieve this with SAP Fiori elements for OData V2 requires extensions.

For example, you can enable the *Generate Purchase Order* button only for sales orders with the completed status.

> **Guideline:** Implement this feature only when the way to enable the button is obvious to end users.

#### Columns in a Form

To optimize horizontal onscreen space, the number of columns in a form depends on the screen size, as shown in the table below.

With SAP Fiori elements for OData V2, you change the number of columns for the extra large screen size to 4.

Table (col-width-30-70)

#### Screen Size

Small

Medium

Large

Extra large

#### Groups in a Form

You can group fields in a form and assign a name to the group.

Note that the group name is displayed **only** when a group contains fields.

#### User-Controlled Load of Fields with Low Importance

To improve the performance on application startup, you can prevent form fields with **low** importance from loading until the user clicks *Show Details* with SAP Fiori element for OData V4.

After the user clicks the button, the fields are loaded and the *Hide Details* button is displayed.

#### Text Control

By default, with SAP Fiori elements for OData V4, in edit mode, the default length of the text control allows for the entry of four lines of text.

You can:

- Set a maximum number of lines for the text control that’s greater than four.
- Enable growing mode: The length of the text control on first load allows for four lines. After the user has entered that number of lines, the length grows by one line at a time until it reaches the maximum number. A scrollbar is displayed next to the text entry area.
- Display below the text area the number of characters allowed in it. As the users enter text, the number decreases to show how many characters remain.

A notification is displayed if the users try to enter text beyond the limit.

In display mode, the text is truncated to 100 characters and a *More* link allows the user to display the full text. Alternatively, you can set the full text to display in a popover when the the user clicks *More*.

#### File Upload

With SAP Fiori elements for OData V4, users can upload a file to an object page property and delete the file.

For example, the sales order object can have a property for a contract and users can upload the contract file to the property.

The application developers can define the file size and types allowed for upload.

### Dynamic Side Content

You can display additional content to the right of an object page subsection. Consult with the development team on doing this with a standard extension.

With this feature, the subsection toolbar contains a *Show Details/Hide Details* action for users to control the display of the dynamic side content. By default, the side content is hidden. You can show it instead. You can also rename the action to make it meaningful to the end user.

> **Guideline:** - Do not use tables in the side content panel.
- Do not add content that may introduce a horizontal scroll bar to the dynamic side content.
- For the best view of the dynamic side content, set it to display in 50% of the screen.

For more information, see:

- [Dynamic Side Content](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/dynamic-side-content/)
- Object Page: [Dynamic Side Content](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/#dynamic-side-content)

> **Hint:** For more information, see [Adding Dynamic Side Content to Object Page Sections](https://ui5.sap.com/#/topic/8e01a463d3984bfa8b23c2270d40e38c).

## Subsection Behavior

### Subsection Loading Behavior

By default, the subsection starts loading after the main object page elements are loaded.

You can change the loading behavior to load the subsection after the header data is loaded.

**Example**

When the subsection contains a table or chart and you want to allow the user to filter in the header before subsection data loads.

### Width for Content Display in a Subsection

When you mix content — such as forms and tables — in one subsection, you can adjust the width allotted to each content type to display a table next to a form.

## Content Visibility

### Sections, Subsections, Quickviews, and Tables

By default, the object page displays these components.

You can set the entire components or selected content in the components to be displayed or hidden in the content area, according to the object’s state. For example, you can hide the Delivery section in a Sales Order until the order has a status where the delivery is planned.

### User-Controlled Visibility

You can enable the *Show More/Show Less* button in the bottom right corner of a section to let users control the display of subsection content.

- When the subsection is hidden, *Show More* is displayed.
- When the subsection shows, the *Show Less* link is displayed.

### Visibility of Smart Form Fields

By default, all smart form fields have the high importance setting and show on all screen sizes.

You can lower the level of importance for the fields to hide them on smaller screens.

According to the importance assigned to the field, it is displayed as follows:

- High (default): On all (small, medium, and large) screen sizes.
- Medium: On large and medium screens only.
- Low: On large screens only

For more information, see [Responsiveness](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/#responsiveness2).

---

## Object Page Footer Bar Sap Fiori Elements

# Object Page – Footer Bar

**> **Information, External_Only:** **

No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData
V4.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with
their behavior – both standalone and when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).


No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData V4.
For information on the latest release of both versions of SAP Fiori Elements, see: [What's New](https://ui5.sap.com/#/topic/99ac68a5b1c3416ab5c84c99fefa250d) in SAPUI5 documentation.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with their behavior – both standalone and
when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## Intro

The SAP Fiori elements object page template supports the features and settings for the object page footer detailed below.

For design information, see the [Object Page Floorplan](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/) guidelines and the links below.

> **Warning:** **Always** build the object page using the [dynamic page header](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/#dynamic-page-header-mandatory).
Set the [shellbar page title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/shell-bar/#page-title) to the name of the business object shown in the object page to indicate the user’s position in the system.
**Do not** use the current implementation of the “page view management” feature in SAP Fiori elements. This feature is technically available for object pages, but we are still working on the final design.

## Feature Availability

Table

#### Footer Bar Actions

[Finalizing Actions](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-footer-bar-sap-fiori-elements#finalizing-actions)

Create

[Save](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-footer-bar-sap-fiori-elements#save)

[Close on Save](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-footer-bar-sap-fiori-elements#save)

[Save and Edit](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-footer-bar-sap-fiori-elements#save-and-edit)
elements for OData V2 only

[Save and Next](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-footer-bar-sap-fiori-elements#save-and-next)

[Apply](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-footer-bar-sap-fiori-elements#apply)
applications only

[Message Popover Button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-footer-bar-sap-fiori-elements#message-popover-button)

[Discard Draft](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-footer-bar-sap-fiori-elements#discard-draft)

[Cancel](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-footer-bar-sap-fiori-elements#cancel)
handling

[Enabling / Disabling of Actions](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-footer-bar-sap-fiori-elements#enabling-disabling-of-actions)

[Keyboard Shortcuts for Actions](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-footer-bar-sap-fiori-elements#keyboard-shortcuts-for-actions)

## Footer Bar Actions

In create and edit modes, the footer bar appears at the bottom of the screen.

### Finalizing Actions

You can add finalizing actions to the footer bar.

A message toast is displayed when an operation is successful.

Finalizing actions complete the work on the current screen, by permanently changing the object state. You can also set them to navigate away from the object page.

Note that developers may call these actions determining actions.

> **Guideline:** Replace the generic placeholder text in the message toast with text that’s meaningful to the user.

For more information, see:

- Footer Toolbar
- [Action Placement: Guidelines for the Footer Toolbar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement#guidelines-for-the-footer-toolbar)
- [Footer Toolbar Examples of Action Placement](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement#footer-toolbar-examples-of-action-placement)

### Save

The action is displayed by default in edit mode.

After saving, the user stays on the object page for applications both with and without draft handling enabled.

You can enable users to automatically navigate back to the list report when they save with SAP Fiori elements for OData V2. To do this, ask your development team to add close logic to the *Save* action.

### Save and Edit

You can enable this action in non-draft applications with SAP Fiori elements for OData V2.

With the *Save and Edit* action, users save current changes and stay on the object page to continue editing.

### Save and Next

This action is enabled with SAP Fiori elements for OData V2 when the [direct edit](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#direct-edit) feature is enabled in the corresponding list report.

With the *Save and Next* action, users save current changes and navigate to the next editable object in the list report.

After they click *Save and Next* for the last editable object in the list report, they return to the list report.

### Apply

You can enable this action in the footer bar of a **subobject** page in draft-enabled applications.

With the *Apply* action, users conclude the create or edit activity, save the draft, and navigate one step up in the object hierarchy to the object page.

Similarly, when the subobject page is open in flexible column layout with three column layout, clicking *Apply* now closes the column where the subobject is displayed and returns the user to the object page.

### Message Popover Button

Turned on by default, the button is only visible when messages are present and allows the user to open the message popover. The color of the message button reflects the most crtical message level.

The message popover displays the count of error messages.

Messages without a criticality level are treated as information messages.

With SAP Fiori elements for OData V2, the messages in the message popover are grouped by section and table so users can easily locate where they need to take action.

For more information, see:

- [Message Popover Button](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/message-popover/#message-button)
- Message Popover

### Discard Draft

Displayed by default in edit mode for applications **with** draft-handling, this action button lets the users leave the object page without saving the changes they’ve made in a draft version of the object.

### Cancel

Displayed by default in edit mode for applications **without** draft-handling this action button lets users leave the object page without saving changes they’ve made to the object.

### Enabling / Disabling of Actions

You can enable or disable footer bar actions according to certain conditions. For example, to prevent users from archiving a sales order that is still being processed, you can enable the *Archive* action only for sales orders with the status Delivered or Cancelled.

Note that even if you disable all footer bar actions, the footer bar still appears onscreen for the display of the [message popover](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-footer-bar-sap-fiori-elements#message-popover-button), described above.

### Keyboard Shortcuts for Actions

Keyboard shortcuts are available for basic operations.

You can also enable custom shortcuts for application-defined actions.

> **Hint:** For more information, refer application developers to [Keyboard Shortcuts](https://ui5.sap.com/#/topic/0cd318c83ec5473d9a091c1782d03c21).

---

## Object Page Header Sap Fiori Elements

**Design System Hero**

# Object Page – Header

**> **Information, External_Only:** **

No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData
V4.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with
their behavior – both standalone and when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).


No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData V4.
For information on the latest release of both versions of SAP Fiori Elements, see: [What's New](https://ui5.sap.com/#/topic/99ac68a5b1c3416ab5c84c99fefa250d) in SAPUI5 documentation.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with their behavior – both standalone and
when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## Intro

The SAP Fiori elements object page template supports the features and settings for the object page header detailed below.

For design information, see the [Object Page Floorplan](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/) guidelines and the links below.

**> **Warning:** **

**Always** build the object page using the [dynamic page header](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#dynamic-page-header-mandatory).
Set the [shellbar page title](https://www.sap.com/design-system/fiori-design-web/ui-elements/shell-bar/#page-title) to the name of the business object shown in the object page to indicate the user’s position in the system.
**Do not** use the current implementation of the “page variant” feature in SAP Fiori elements. This feature is technically available for object pages, but we are still working on the final design.

## Feature Availability

**Table**

#### Behavior and Interaction

[Expanded State](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#collapsedexpanded-state)

[Collapsed State](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#collapsedexpanded-state)
With SAP Fiori elements for OData V2, on mobile phone
screens, the object page displays a summary line instead
of the collapsed header.

[Header Content Display in Display Mode](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#display-of-header-content)

[Header Content Display in Edit and Create Modes](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#display-of-header-content)
- The first dynamic section in the content area, the
header section, displays all the fields in the header
that can be rendered in a form — both editable and
uneditable fields.
- UI elements in the header that cannot be rendered in a
form, such as micro charts, are not shown.

[Header Content Visible](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#header-content-visibility)

[Header Content Hidden](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#header-content-visibility)

[Header Field Editability](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#header-field-editability)
- Not editable with SAP Fiori elements for OData V2
- Editable with SAP Fiori elements for OData V4
You can change the default.

[Highlighting Values Based on Criticality](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#highlighting-values-based-on-criticality)

#### Components

Dynamic Page Header

[Title](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#title)

[Menu for Saved Version / Draft](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#menu-for-saved-version-draft)

[Breadcrumbs](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#breadcrumbs)

Subtitle

[Object Marker](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#object-marker)

[Image](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#image)

[Paging Buttons on the First Object Page](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#paging-buttons)

[Paging Buttons on the First Subobject Page](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#paging-buttons)

Toolbar

#### Toolbar Actions

[Edit and Delete](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#edit-and-delete)
You can turn one or both actions off.

[Copy](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#copy)

[Related Apps Menu Button](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#related-apps-menu-button)
With SAP Fiori elements for OData V4, you can change the
button name to *Open in…*

[Generic Actions](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#generic-actions)
turned off for drafts.

[Application-Specific Actions](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#applicationspecific-actions)

[Conditional Enablement of Navigation Buttons](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#conditional-enablement-of-navigation-buttons)
Requires an extension with SAP Fiori elements for OData
V2

[Order of Toolbar Actions](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#order-of-toolbar-actions)
You can change the default order.

[Grouping Actions in a Menu Button](https://main--builder-prospect-prod--sapudex.aem.page/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#grouping-actions-in-a-menu-button)

#### Additional Content (Optional)

[Message Strip](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#message-strip)
a whole, such as the object status

[Simple Header Facets](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#simple-header-facets)

[Plain Text Facets](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#plain-text-facets)

[Contact Facets](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#contact-facets)

[Micro Chart Facets](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#micro-chart-facets)

[Form Facets](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#form-facets)

[Address Facets](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#address-facets)

[Header Field Group](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#header-field-groups)

[Rating Indicator Facets](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#rating-indicator-facets)

[Progress Indicator Facet](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#progress-indicator-facets)

[Key Value Facet](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-header-sap-fiori-elements#key-value-facets)

Link
With SAP Fiori elements for OData V2:
- The default link shows the text and ID. You can remove
the text or the ID from the link.
- You can include a link that navigates to a site
external to the application.

## Behavior and Interaction

### Collapsed/Expanded State

When the object page header contains at least one facet:
- On the initial load of the object page, the header is expanded.
- When the user scrolls down the page, the header collapses.
- The *Expand/Collapse :navigation-down-arrow: :navigation-up-arrow:* button and the *Pin/Unpin :pushpin-off:* button are displayed.
When the object page header contains only a title and a subtitle, the *Expand/Collapse :navigation-down-arrow: :navigation-up-arrow:* button and the *Pin/Unpin :pushpin-off:* button are not displayed.
With SAP Fiori elements for OData V2, when users scroll on a mobile phone screen, the object page optimizes the screen space by displaying a summary
line instead of the collapsed header.
Next to the title, an arrow :navigation-down-arrow: button lets the users expand the header.
For more information, see:
- [Dynamic Page Header (Mandatory)](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#dynamic-page-header-mandatory)
- [Header Toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/header-toolbar/)
- [Header Features](https://www.sap.com/design-system/fiori-design-web/page-types/page-layouts/dynamic-page-layout/#header-features)
### Display of Header Content

In display mode, the header content area displays **all** the header content.

In edit and create modes, when the header is:

- **Editable**
  - The first dynamic section in the content area, the header section, displays all the fields in the header that can be rendered in a form — both editable and uneditable fields.
- The header section is only present in the edit and create modes.
  - The first temporary section will have a section title called “Header” if there is no Anchor Bar available.
  - UI elements in the header that cannot be rendered in a form, such as micro charts, are not shown.
- **Not Editable**, the header is hidden.

Note that, by default, the header is

- Editable with SAP Fiori elements for OData V4
- Not editable with SAP Fiori elements for OData V2

You can ask the application developers to change the default.

For more information, see [Dynamic Page Header (Mandatory)](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#dynamic-page-header-mandatory).

**> **Hint:** **

To change the default for the editability of the header, you can refer the application developers to: [Toggling the Editability of Header Fields](https://ui5.sap.com/#/topic/c8a9a40a5cee4fb4bcdf97d09420de5e).

### Header Content Visibility

By default, header content is visible.

You can set the following header components or selected content, fields, or actions in them to be displayed or hidden, according to the object’s state:

- Entire header facets
- Content, such as fields, in a header facet
- Content in quick views

With Fiori elements for OData V2, you can set:

- The header to be displayed in edit mode.
- Header facets to be visible in edit mode.

**> **Hint:** **

For more information on the features, refer the development team to:
- [Hiding Features Using the UI.Hidden Annotation](https://ui5.sap.com/#/topic/ca00ee45fe344a73998f482cb2e669bb)
- [Adapting the UI: List Report and Object Page](https://ui5.sap.com/#/topic/0d2f1a9ebd2d4a4c906216ded1d33783.html)

### Header Field Editability

By default, in edit mode the header is:

- Not editable with SAP Fiori elements for OData V2
- Editable with SAP Fiori elements for OData V4

You can change the default.

Even when the header is editable, certain fields or facets in the header may not be editable, for example, micro chart facets or text fields marked as `ReadOnly`.

**> **Hint:** **

To change the default for the editability of the header, you can refer the application developers to: [Toggling the Editability of Header Fields](https://ui5.sap.com/#/topic/c8a9a40a5cee4fb4bcdf97d09420de5e).

### Highlighting Values Based on Criticality

You can assign colors and icons to text to indicate the criticality of a field value.

With SAP Fiori elements for OData V4, you can add a quick view to text that’s been set to display in a color to indicate the criticality of its value. The text is displayed underlined as a link so users know the quick view is available.

## Components

### Title

By default, with:

- SAP Fiori elements for OData V2, the title area is empty.
- SAP Fiori elements for OData V4, the title area displays the text: (Unnamed Object).

**> **Guideline:** **

Tell the developers which property to use as the title.

### Menu for Saved Version / Draft

With this menu next to the object page title, users can navigate between the **saved** version of an object and the **draft** version that they’ve created. This is a default feature in applications with draft-handling,

### Breadcrumbs

Breadcrumbs are displayed above the object title.

**> **Guideline:** **

Limit the breadcrumbs to the drilldown levels within the object page.

### Object Marker

The object marker indicates the object is locked by another user in draft-enabled applications.

### Image

The image is an avatar control. By default, it has a square shape.

You can set:

- An image to display instead of the avatar. SAP Fiori elements for OData V4 uses the [lightbox](https://www.sap.com/design-system/fiori-design-web/ui-elements/lightbox/) control to allow a larger view of the image.
- The avatar to a have a circular shape.

When no image is set or found for the avatar, the avatar initials are displayed.

If those are not set or found either, an icon for the avatar is displayed:

- A square avatar for a product
- A circular avatar for a person.

For more information on the logic used for displaying an object, consult the development team and see [Using Images, Initials, and Icons](https://ui5.sap.com/#/topic/5760b638ea274d7aab59e4e434899528).

### Paging Buttons

By default, with **both** SAP Fiori elements for OData V2 and V4, the paging buttons appear in the subobject page of applications that use the dynamic page layout in the following conditions:

- The user has navigated from a table in the object page to the subobject.
- The table in the object page contains at least two items.

With SAP Fiori elements for OData V2, you can:

- Enable the paging buttons to show on the first object page opened from a list report.
- Disable the default display of the paging buttons on the subobject page.

## Toolbar Actions

### Edit and Delete

By default, these actions are displayed when the data in the object page allows them.

You can:

- Set each enabled action to be displayed or hidden based on certain conditions in the back end. For example, you can hide the actions for a sales order that has already been paid.
- Disable the actions.

For more information, see:

- [Object Handling (Create, Edit, Delete)](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/manage-objects)
- [Edit](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#edit)

### Copy

You can place a copy action button in the header to let the user create a new object with the same data as the current object with SAP Fiori elements for OData V2.

You set the label for the button according to your use case. Otherwise, the default label is *Copy*.

In the object page, the *Copy* button is displayed after the *Delete* button.

**> **Hint:** **

Application developers can define a standard copy action button by annotating a function import action (DataFieldForAction) as a *Copy* action. For more information, refer them to: [Enabling Actions in the Object Page Header](https://ui5.sap.com/#/topic/5fe439613f9c4e259015951594c423dc).

### Related Apps Menu Button

You can enable the *Related Apps* menu button. It displays the actions available on the same object in different applications. Users select the action to open the same object in another application.

You can also:

- Hide specific actions in the menu.
- Change the button name to *Open In…* with SAP Fiori elements for OData V4.

### Generic Actions

By default, the Share button is displayed for saved objects and hidden for drafts.

It can include the:

- *Share in SAP Jam* menu item when SAP Jam integration is configured.
- *Microsoft Teams > As Chat* and *As Card* options when the required settings have been made by the system administrators of SAP S/4HANA or SAP S/4HANA Cloud. This feature is part of collaborative ERP (enterprise resource planning), which integrates the best of SAP S/4HANA or SAP S/4HANA Cloud with Microsoft Teams. It’s not available for all users. When available, the menu item opens a separate window where users can directly share a link to a business application in the SAP S/4HANA or SAP S/4HANA Cloud system with co-workers.

\With SAP Fiori elements for OData V4, you can control the visibility in the *Share* menu of the *Send E-mail* and *Share: Microsoft Teams*.
For more information, see:

- [Share (Generic)](https://www.sap.com/design-system/fiori-design-web/ui-elements/header-toolbar/#share-generic-4)
- [Collaboration](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/collaboration)

**> **Hint:** **

For more information, refer application developers to:
- [The Share Functionality](https://ui5.sap.com/#/topic/022bf0dcae1d4d90961ebe23d642fca3)
- [Integrating Microsoft Teams](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/257ec7408db6420682462cd1d000e744.html) for SAP S/4HANA Cloud
- [Integration with Microsoft Teams](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/849465e69b7a490a88049fe0b24fb01e.html?version=2023.000) for SAP S/4HANA

### Application-Specific Actions

You can include the actions required for your use case.

The header toolbar displays application-specific actions to the left of the generic actions.

You can also define custom shortcuts for application-defined action buttons and navigation buttons.

**> **Hint:** **

For more information, refer application developers to [Keyboard Shortcuts](https://ui5.sap.com/#/topic/0cd318c83ec5473d9a091c1782d03c21).

### Conditional Enablement of Navigation Buttons

With SAP Fiori elements for OData V4, you can enable buttons that navigate the user to another page or application based on the value of a specific field.

With SAP Fiori elements for OData V2, this feature requires extensions.

For example, you can enable the Generate Purchase Order button only for sales orders with the completed status.

**> **Guideline:** **

Implement this feature only when the way to enable the button is obvious to end users.

### Order of Toolbar Actions

The default order — left to right — for actions in the object page toolbar is below:

- *Edit*
- *Delete*
- Copy with SAP Fiori elements for OData V2
- Application-specific action buttons
- *Related Apps* menu button
- *Share*

You can rearrange the order, for example, by setting an application-specific action that’s the primary action to the leftmost position on the toolbar.

For more information, see:

- [Action Placement](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement)
- [Header Toolbar](https://www.sap.com/design-system/fiori-design-web/ui-elements/header-toolbar/)

### Grouping Actions in a Menu Button

With SAP Fiori elements for OData V4, you can group together actions with a similar business purpose in a menu button.

Note that when **all the actions** in the menu have one of the following states, the menu button does too:

- Disabled
- Hidden

## Additional Content

### Message Strip

You can add a message strip in the header to provide information related to the object, such as the object status.

The message strip is displayed under the object page title and optional subtitle. When the header is collapsed, the message strip remains visible.

When more than one message is relevant for the object as a whole, the message strip displays the text “*The object contains errors / warnings / information*.”

The user can find the individual messages via the message popover in the footer bar.

For more information, see:

- [Message Strip](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-strip/)
- [Message Popover Button](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-popover/#message-button)

### Simple Header Facets

With SAP Fiori elements for OData V2:

- You can use a simple header facet to show simple data points that align horizontally across the header.
- When form fields contain **no** value, they display the [empty state indicator](https://www.sap.com/design-system/fiori-design-web/ui-elements/form/#empty-state-indicator) (–).

### Plain Text Facets

You can use the plain text facet to display a continuous text in the header.

For more information, see [Plain Text Facet.](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#plain-text-facet)

### Contact Facets

You can enable a quick view for a contact.

For applications with Microsoft Teams integration, the contact card and the quick view card both display options for starting a Microsoft Teams audio call, video call, or chat with the contact.

With SAP Fiori elements for OData V4:

- When a quick view detail contains **no** value, the [empty state indicator](https://www.sap.com/design-system/fiori-design-web/ui-elements/form/#empty-state-indicator) (–) is displayed.
- You can add a quick view to text that’s been set to display in a color to indicate the criticality of its value. The text is displayed underlined as a link, so users know the quick view is available.

For more information, see [Quick View](https://www.sap.com/design-system/fiori-design-web/ui-elements/quickview/).

### Micro Chart Facets

You can display the following micro charts in the header:

- Area micro chart
- Bullet chart
- Radial chart
- Column chart
- Line micro chart
- Harvey ball chart
- Stacked bar chart

For more information, see [Micro Charts](https://www.sap.com/design-system/fiori-design-web/ui-elements/micro-chart/).

### Form Facets

You can add a quick view to the form facet.

For more information, see [Form Facet (Dataset)](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#form-facet-dataset).

**> **Hint:** **

For more information, refer the development team to [Form Facet](https://ui5.sap.com/#/topic/ebe05d52c43241c19aaf79dd5f1c69f1).

### Address Facets

You can display an address such as a shipping address.

**> **Hint:** **

For more information, refer the development team to [Address Facet in the Object Page Header](https://ui5.sap.com/#/topic/0b73cbbeda344d88b5d0f8bea4d4498e).

### Header Field Groups

You can define fields to display together in a facet. For example, for the product object, in the *General Information* section, you can include the fields quantity, weight, and supplier.

### Rating Indicator Facets

You can add a rating indicator to the header. It is read-only in both display and edit modes.

By default, the maximum rating is five stars.

You can:

- Change the maximum rating.
- Specify more descriptive text for the subtitle.

**With extensions**, you can make the rating editable.

#### Display Mode

The rating indicator shows with the:

- Title
- Subtitle with the total number of ratings
- Rating shown with stars: Both the aggregated and non-aggregated single rating types are supported.

#### Edit Mode

The rating indicator moves into the header facet and appears with only the title in edit mode.

For an aggregated rating, the number of ratings is shown in parentheses after the stars.

For more information, see:

- [Rating Indicator Facet](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#rating-indicator-facet)
- [Rating Indicator](https://www.sap.com/design-system/fiori-design-web/ui-elements/rating-indicator/)

### Progress Indicator Facets

You can add a progress indicator facet to the object header.

For more information, see:

- [Progress Indicator Facet](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#progress-indicator-facet)
- [Progress Indicator](https://www.sap.com/design-system/fiori-design-web/ui-elements/progress-indicator/)

### Key Value Facets

You can add a key value facet to highlight important data or KPIs.

For more information, see [Key Value Facet](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/#key-value-facet).

---

## Object Page Overview Sap Fiori Elements

# Object Page – Overview

**> **Information, External_Only:** **

No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData
V4.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with
their behavior – both standalone and when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).


No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData V4.
For information on the latest release of both versions of SAP Fiori Elements, see: [What's New](https://ui5.sap.com/#/topic/99ac68a5b1c3416ab5c84c99fefa250d) in SAPUI5 documentation.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with their behavior – both standalone and
when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## Intro

The SAP Fiori elements object page template supports the features and settings for the overall object page behavior detailed below.

For design information, see the [Object Page Floorplan](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/) guidelines and the links below.

> **Warning:** **Always** build the object page using the [dynamic page header](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/#dynamic-page-header-mandatory).
Set the [shellbar page title](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/shell-bar/#page-title) to the name of the business object shown in the object page to indicate the user’s position in the system.
**Do not** use the current implementation of the “page view management” feature in SAP Fiori elements. This feature is technically available for object pages, but we are still working on the final design.

## Feature Availability

Table (col-width-30-70)

#### Features

Illustrated Message for Unfound Page
See [Illustrated Message](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/illustrated-message/).

[Unsaved Changes Warning](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/v1-124/discover/frameworks/sap-fiori-elements/object-page/object-page-overview-sap-fiori-elements#unsaved-changes-warning)
- Another application without saving changes. You can turn it off.
- The previous page without saving changes.

[Message Toast on Discard](https://main--builder-prospect--sapudex.aem.page/design-system/fiori-design-web/v1-139/discover/frameworks/sap-fiori-elements/object-page/object-page-overview-sap-fiori-elements#message-toast-on-discard)

## Feature Details

### Unsaved Changes Warning

By default, in draft-enabled applications, on the main object page, a message warns users of unsaved changes when the users navigate:

- **Forward** to another application without saving changes in edit mode or without entering data for a new object in create mode.

You can ask the application developers to turn the message off for forward navigation. The draft is kept for the user to return to later.

- **Backward** to the previous page without saving changes in edit mode or the data entered for a new object in create mode.

*Warning for unsaved changes in edit mode*

Depending on whether the object page is in edit or create mode, the message lets the users opt to:

- Save changes in edit mode
- Create the object in create mode
- Keep the draft
- Discard the draft
- Cancel the navigation

> **Information:** The *Warning* message is **not displayed** when the user navigates backward without entering data for a new object in create mode. The object is discarded.

### Message Toast on Discard

When the user makes changes in a draft, then discards it, a message toast is displayed to confirm the successful discard. The message text depends on the action that resulted in the draft, as follows:

Table (col-width-5-95)

#### Action

Create

Edit
“Draft discarded” with SAP Fiori Elements for OData V4

When the user discards a draft without making changes in it, no message toast is displayed.

---

## Smart Templates

# SAP Fiori Elements – Overview

## Intro

The UI-development framework of choice for all projects, the SAP Fiori elements framework:

- Drives UX consistency across applications with common layout and interaction patterns in building blocks that align with SAP's design principles and user-centric approach.
- Offers flexibility to adapt the applications for specific solutions within the framework.
- Speeds development by reducing the frontend code required to build SAP applications.

This article introduces you to the SAP Fiori Elements framework and links to other sources of information about its capabilities so you can optimize your collaboration as an application team.


- To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with their behavior – both standalone and when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).
- For resources on getting started and staying current with SAP Fiori Elements, see: [Find Information and Get Help.](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/find-information-and-get-help)

**> **Information, External_Only:** **

To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with
their behavior – both standalone and when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## SAP Fiori Elements Framework

SAP Fiori Elements Building Blocks

To create SAP Fiori applications, at runtime, the SAP Fiori elements framework generates the UI based on OData service metadata, annotations, and application-specific configurations.

New applications are developed with SAP Fiori elements for OData V4, based on the OData (Open Data Protocol) version 4.

### Building Blocks

Visual layout patterns that range from basic patterns like the field to complex patterns like tables. Building blocks can be used in
standard floorplans, custom pages, or a combination of the two, as best fits your application requirements.
See: [Building Blocks](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/buildingBlocks/buildingBlocks).
### Global Patterns

Non-visual building blocks as common interaction patterns like side effects or draft handling.
See: [Global Patterns.](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/controllerExtensions/editFlow)
### Standard Floorplans

Standard floorplans combine the most common building blocks and patterns in predefined layouts with added optimizations for
component interaction at the floorplan level. They provide for the most efficient application development and can be extended
for use-case-specific deviations.
The most common floorplans are list report and object page with their variations.
Through extension points, these standard floorplans can be adjusted if needed.
See: [Standard Floorplans](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/floorplans)
### Custom Pages

Custom pages flexibly combine building blocks to achieve custom layouts that benefit from the framework capabilities.
Additional SAPUI5 coding can be used to complement the custom layout.
See [Custom Pages](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/customPage).
## Usage

Your use case determines how your project team develops the application with SAP Fiori elements:

- Do the SAP Fiori elements floorplans deliver all the features you need to provide to the users?
- If the SAP Fiori elements floorplans offer a close fit, your project team can explore the extension options to include building blocks or SAPUI5 in a floorplan.
- If your SAP Fiori application requires a custom layout, choose the building blocks and global patterns that developers add to a custom page and retain the benefits of the SAP Fiori elements framework.
- You can combine standard floorplans and custom pages within an application to satisfy the user’s needs.

### Extensions

Although extensions require effort to develop and maintain, they also retain benefits of the SAP Fiori elements framework that save on other efforts. Check out the [extension options for each floorplan](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/controllerExtensions/guidanceControllerExtensions) or explore the [custom layout options with custom pages](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/customPage) in the SAP Fiori Development Portal.

### Placeholder Texts

Some UI texts that the SAP Fiori elements framework provides are generic placeholders. Always replace them with text that is meaningful to your user, for example:

Table (col-width-20-30-50)

Floorplan     | Placeholder Text           | Replacement Text

List Report   | *Create Object*            | *Create Sales Order*

Object Page   | *New Object*               | *New Sales Order*

Overview Page | *Could not perform action* | *Unable to approve*

For more information, see: [Replacing Placeholder Text](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/replacing-placeholder-text).

> **Hint:** For more information about placeholder texts in SAP Fiori elements, see [Replacing Standard UI Texts](https://ui5.sap.com/#/topic/b8cb649973534f08a6047692f8c6830d).

### For Application Developers

SAP Fiori elements is shipped with SAPUI5 and supports both SAP Fiori elements for OData V4 and SAP Fiori elements for OData V2.

- Build new applications with SAP Fiori elements for OData V4.
- Refer to the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction) provides all capabilities for SAP Fiori elements for OData V4.
- For an overview of all available SAPUI5 versions and their maintenance status, see [SAPUI5 Versions Maintenance Status](https://ui5.sap.com/versionoverview.html).

---

## List Sap Fiori Elements

# List

**> **Information, External_Only:** **

No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData
V4.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with
their behavior – both standalone and when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).


No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData V4.
For information on the latest release of both versions of SAP Fiori Elements, see: [What's New](https://ui5.sap.com/#/topic/99ac68a5b1c3416ab5c84c99fefa250d) in SAPUI5 documentation.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with their behavior – both standalone and
when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## Intro

With SAP Fiori elements for OData V2, you can enable the display of a list in the list report with:

- [Standard list items](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/standard-list-item/)
- [Object list items](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/object-list-item/)

With both list item types:

- A chevron icon lets users navigate to the item.
- A navigation row indicator highlights the list item that the user has navigated to.
- You can assign semantic coloring of red, green, or orange to the data points, such as price, based on their values.

---

## Table Features Sap Fiori Elements

# Table Features

**> **Information, External_Only:** **

No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData
V4.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with
their behavior – both standalone and when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).


No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData V4.
For information on the latest release of both versions of SAP Fiori Elements, see: [What's New](https://ui5.sap.com/#/topic/99ac68a5b1c3416ab5c84c99fefa250d) in SAPUI5 documentation.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with their behavior – both standalone and
when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## Intro

The SAP Fiori elements templates support the features and settings for a table detailed below.

For design information see the table guidelines, starting with [Table Overview](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview), and the links within this article.

## Feature Availability

Table

#### Table Settings

Column Header Labels

Asterisk in Labels for Mandatory Fields
in the column header label for mandatory table fields with SAP
Fiori elements for OData V4.

[Tooltips on Column Headers](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#tooltips-on-column-headers)

[Clear All](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#clear-all--select-all)
in both the list report and object page when the selection of
multiple rows is enabled for:
- Grid tables
- Analytical tables
- Tree tables
You can change the default.

[Select All](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#clear-all--select-all)
when the selection of multiple rows is enabled for a
responsive table.
You can change the default.

Sticky Column Header Behavior

[Column Width](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#column-width)
change it.

[Column Importance](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#column-importance-in-responsive-tables)
importance of none, **except** for list report columns for key
fields. These have high importance.
You can change the level of importance.

[Freezing Columns](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#freezing-columns)
for the number of columns that you decide.

[Labels for Multiple Fields in a Column](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#labels-for-multiple-fields-in-a-column)
OData V4

[Ascending Sort Order on a Column](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#sort-order)

[Quick Sort on a Column](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#quick-sort-on-a-column)

[Grouping](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#grouping)
tables

Filters on Aggregation
OData V4.
You can set filters on aggregated measures.

[Number of Table Rows Displayed at Once](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#number-of-table-rows-displayed-at-once)
between optimal user experience and optimal technical
performance.

[No Data Found Message](https://sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#no-data-found-message)
- An illustrated message with generic placeholder text is
displayed with SAP Fiori elements for OData V4. You can add an
action to it. You can change it to a text-only message, as
required.
- Generic placeholder text is displayed with SAP Fiori
Elements for OData V2
Replace the generic text with text that’s meaningful to the
user.

Message Strip above the Table
- List report, object page, and analytical page with SAP Fiori
elements for OData V2
- List report with SAP Fiori elements for OData V4
In the object page, by default, a message strip is displayed
when there are errors in the table.
When there are multiple messages, the one with the highest
severity is displayed.

[Generic Context Menu](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#generic-context-menu)
object page, and analytical list report. It cannot be
deactivated.

[Tree Table Context Menu](https://main--builder-prospect-prod--sapudex.aem.page/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#tree-table-context-menu)

[Order of Nodes in the Tree Table](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#order-of-nodes-in-the-tree-table)
always displays a newly created node as the first in the table
or as the first child below its parent node, even when a sort or
a filter is applied to the table.
You can change the default.

#### List Report and Analytical Page Only

[Number of Table Levels Expanded at Initial Load](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#initial-expansion-of-table-levels)
analytical table.

#### List Report Only

Copy

#### Object Page Only

[Message Strip for Rows with Errors](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#message-strip-for-rows-with-errors)

Rows Displayed in a Grid Table
onscreen space for an object page with:
- Anchor bar navigation and a single section that contains only
a grid table
- Tab bar navigation and a current tab that contains only a grid
table

## Table Settings

### Tooltips on Column Headers

On desktop applications, all table columns display tooltips, based on the text in:

- `Common.QuickInfo`, when it’s visible
- The column label, in all other cases

Tooltips are available only in desktop applications because users must hover their mouse on the column header to see them.

### Clear All / Select All

When the [selection of multiple rows](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#item-selection) is enabled for a table in the list report and object page, the *Clear All*  :clear-all:  checkbox is displayed by default in the selection column header for all tables, but the responsive table. You can change the default.

> **Information:** To select a range of items when the *Clear All*  :clear-all:  checkbox is displayed, users can select an item, press **Shift**, and select others.

Table

#### Table Type  | #### Selection Default   | #### Users Can Select

Grid table       | *Clear All*  :clear-all: | Up to 200 rows by default
Analytical table |                          | We recommend you consult the application
| development team on how changes to the limit
Tree table       |                          | would impact performance.

Responsive table | *Select All*  :border:   | All the rows displayed on the interface, **not all the rows in the table**.
| A message informs users that “Only the first *n*
| of the items you selected were added to the
| selection,” where “*n*” equals the number of
| items loaded on the interface.

> **Warning:** For grid tables, analytical tables, and tree tables, changing the default *Clear All*  :clear-all:  checkbox to the *Select All* :border: checkbox can lead to performance issues because *Select All* :border: loads all the table rows to the frontend.
Always ask the application development team about the impact on performance before you consider such a change.

> **Guideline:** When the object page is in tab bar mode, we recommend enabling the *Clear All*  :clear-all: when the selection of multiple rows is enabled.

### Column Width

The default column width varies according to the column contents:

- Text: can range from 3 to 20 rem
- Image: 5 rem
- Rating or progress indicator: 6.875 rem
- Chart: 20 rem

You can change the width.

You can also ask the application developers to ensure the column width takes into account the contents of both the column and the column header.

> **Hint:** For more information, refer the development team to [Setting the Default Column Width](https://sapui5.hana.ondemand.com/1.88.1/#/topic/a76525362b754354a85981a7389ca7af).

### Column Importance in Responsive Tables

By default:

- Key fields have high importance in list reports.
- Other columns have the importance of none and are handled like columns assigned medium importance.

You can change the level of importance.

The importance assigned to a column determines whether or not the table displays its values onscreen when screen space is limited:

- The values from high importance columns are always displayed onscreen — as columns or in the pop-in area, depending on the screen size.
- The values in columns with low importance are first to be hidden.

When at least one column is hidden, the table toolbar displays the *Show Details* button so users can view the previously hidden columns in the table [pop-in area](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/#responsiveness). After the user clicks *Show Details* to display the column, the action changes to *Hide Details*.

You can also assign an importance to custom columns.

For more information, see:

- [Responsiveness](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/#responsiveness)
- [Auto Popin Mode](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/#auto-pop-in-mode)

### Freezing Columns

You can freeze the first columns of an analytical table, grid table, or tree table so that they always remain visible when the users scroll the table horizontally. You specify the number of columns.

> **Hint:** For more information, refer application developers to [Tables](https://sapui5.hana.ondemand.com/#/topic/c0f6592a592e47f9bb6d09900de47412).

### Labels for Multiple Fields in a Column

By default, with SAP Fiori elements for OData V4, when a column contains a field group with more than one field, the labels for those fields are not displayed.

You can enable the display of a label for each field. The field group label then is displayed as the column title in the header.

### Sort Order

By default, the sort order for a column is ascending.

You can:

- Set the default sort order to descending.
- Define other, customized sort orders.

For more information, see the sort guidelines according to table type:

- [Responsive Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/)
- [Analytical Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/analytical-table-alv/)
- [Grid Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/grid-table/)
- [Tree Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/tree-table/)

### Quick Sort on a Column

Available for any sortable column.

When a column contains a combination of fields, such an ID and a description or a field group, the users can specify a sort and sort order for each field in the column with the quick sort.

### Number of Table Rows Displayed at Once

#### Responsive Table

By default, a responsive table loads the following number of rows at once:

- 20 rows in a list report
- 10 rows in an object page with multiple sections
- 20 rows in an object page that includes one section and one subsection

When more rows exist, the users can click the *More* button at the end of the table to view additional rows.

With SAP Fiori elements for OData V2, you can change the default number.

#### Tree Table, Analytical Table, and Grid Table

By default, when the object page has the default anchor bar navigation or when an object page section contains controls besides the table:

- A tree table or an analytical table displays 10 rows
- A grid table displays 5 rows

When more rows exist, the users can scroll to display them.

With SAP Fiori elements for OData V4, the default number of rows can be changed.

> **Guideline:** Use icon tab bar navigation when you use the grid table because the anchor bar navigation results in the display of
two scroll bars – one for the object page and one for the grid table.

##### Row Display on Scroll

To optimize the display of rows as the users scroll, the grid table, analytical table, and tree table preload a default of 300 table rows from the backend. The application developer can change the default number as required for the use case.

> **Guideline:** Work with the development team to find the best compromise between optimal user experience and optimal technical
performance.

### Grouping

Grouping is available in responsive and analytical tables.

You can define the format of the grouping headers.

For more information, see:

- Analytical Table: [Group](https://www.sap.com/design-system/fiori-design-web/ui-elements/analytical-table-alv/#group)
- Responsive Table: [Group](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/#group)

### No Data Found Message

By default:

- An [illustrated message](https://www.sap.com/design-system/fiori-design-web/ui-elements/illustrated-message/) with generic text is displayed with SAP Fiori elements for OData V4. You can add an action to the illustrated message or you can replace it with a text-only message.
- Generic placeholder text is displayed with SAP Fiori Elements for OData V2.

> **Guideline:** Replace the placeholder text with text that’s meaningful to the user.
For more information, see: [Replacing Placeholder Text](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/replacing-placeholder-text)

### Generic Context Menu

For desktop and mobile applications, a generic context menu is activated and cannot be deactivated for all table types in the list report, object page, and analytical page.

The generic context menu generally behaves like the standard context menu described in the corresponding table articles, linked below.

The context of the generic context menu can be either a single row or multiple selected rows.

*Single row context - a non-selected row is the "click target" so the context menu applies to the non-selected row*

*Multiple row context - one or more selected rows are the "click target " so the context menu applies to all the selected rows*

#### Actions

The following actions are always available on the generic context menu:

- All toolbar actions that become active only after the selection of rows. Developers call them “bounded toolbar actions” or “context-dependent actions.”
- The “open in new tab or window” action. It allows up to 10 items to be opened in separate tabs or windows, depending on the user’s browser settings. As for the standard context menu, if a control inside a row is the “click target”, and that control also provides a context menu, **the control context menu “wins**”.
- *Share to SAP Collaboration Manager* when SAP Collaboration Manager is enabled. This item is displayed when the object page is in read only mode or in edit mode for read only columns.

> **Information:** The *Open in New Tab* or *Open in New Window* action **does not display in the context menu** when the table is configured to navigate to an object page in edit mode.

For information on the standard context menu, see:

- [Context Menu (Responsive Table)](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/)
- [Context Menu (Grid Table)](https://www.sap.com/design-system/fiori-design-web/ui-elements/grid-table/)
- [Context Menu (Analytical Table)](https://www.sap.com/design-system/fiori-design-web/ui-elements/analytical-table-alv/)
- [Context Menu Tree Table](https://www.sap.com/design-system/fiori-design-web/ui-elements/tree-table/)

### Tree Table Context Menu

With SAP Fiori elements for OData V4, the context menu for tree tables contains the actions from the generic context menu, and the actions specific to the tree table for example:

- A bounded *Create* action
- *Move Up* and *Move Down* for reordering nodes within the same hierarchical level
- *Expand All* and *Collapse All*
- *Cut* and *Paste*

#### Bounded Create

The bounded *Create* action is active in the context menu for a single container node or leaf node. The new item is created as a child of the selected node.

When multiple items are selected, it is inactive.

A “bounded action” is one that becomes active only after item selection.

#### Move Up, Move Down

The *Move Up* and *Move Down* actions are active in the context menu for a single container node or leaf node, and the action is relevant for the node.

When the action is not relevant, the menu displays it as inactive. For example, in the context menu for the last node in a container node, the *Move Up* action is active and the *Move Down* action is inactive.

The actions aren’t in the context menu when multiple items are selected.

#### Expand All, Collapse All

The *Expand All* and *Collapse All* actions are active in the context menu for a single container node, and the action is relevant to the node’s current state.

- *Collapse All* closes all the nodes it contains.
- *Expand All displays* all the nodes that the selected node contains down to the lowest level of leaf nodes.

The actions are in an inactive state in the context menu for a:

- Single **leaf node**
- Selection of **more than one node**
- Node that is already collapsed or expanded so the action is irrelevant

#### Paste

The paste action behaves differently, depending on the data structure in the backend table.

For a non-hierarchical data structure, when the users paste to a container node or leaf node at level n, the data is pasted as a child or children to the node at level n+1.

For a hierarchical data structure, when the users paste to:

- A container node at level n, the data is pasted as a child or children to the node at level n+1,
- A leaf node at level n, the leaf node becomes a container at the same level and the data is pasted as a child or children to the node at level n+1

### Order of Nodes in the Tree Table

With SAP Fiori elements for OData V4, by default, a newly created node is always displayed first in the table or as the first child below its parent node, even when a sort or a filter is applied to the table. For example, a node created:

- At the root of the table is displayed **first in the table**
- In a container node is displayed **first in the container node**

Instead, you can enable an option to display new nodes in the order that they were created in the table or parent node. For example, a node created:

- At the root of the table is displayed as the **last in the table**
- In a container node is displayed **last in the container node**

This feature allows users to act directly on the table hierarchy — not just its display — when they:

- Create new table elements
- Reorder nodes from the generic context menu, by moving them up or down in the table or in their parent nodes

> **Information:** - With this feature, a message [strip/toast] informs the user when the filter criteria applied to a table prevents a
new node from being displayed.
- For backend systems on RAP, this feature is unavailable for tree tables in a list report.

> **Hint:** For more information, refer application developers to [Tree Tables](https://sapui5.hana.ondemand.com/#/topic/7cf7a31fd1ee490ab816ecd941bd2f1f).

## List Report and Analytical Page Only

### Initial Expansion of Table Levels

By default, on initial load, the following expandable tables are expanded to this number of levels:

- Responsive table: 1 level
- Tree table: 1 level
- Analytical table: 0 levels

You can change the default value for the tree table and analytical tables.

> **Hint:** For more information, refer the development team to [Initial Expansion Level for Tables in List Reports & Analytical List Pages](https://sapui5.hana.ondemand.com/#/topic/bc05d353d2c44854b1ea228b99e922a2).

### Message Strip for Rows with Errors

When table rows contain errors, a message strip is displayed above the table. It contains a *Filter Items* link that lets users see only the rows with errors. After the users click the link, a *Clear Filter* link replaces it.

## Object Page Only

### Message Strip for Rows with Errors

When table rows contain errors, a message strip is displayed above the table. It contains a *Filter Items* link that lets users see only the rows with errors. After the users click the link, a *Clear Filter* link replaces it.

---

## Table Rows Sap Fiori Elements 2

# Table Rows

**> **Information, External_Only:** **

No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData
V4.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with
their behavior – both standalone and when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).


No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData V4.
For information on the latest release of both versions of SAP Fiori Elements, see: [What's New](https://ui5.sap.com/#/topic/99ac68a5b1c3416ab5c84c99fefa250d) in SAPUI5 documentation.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with their behavior – both standalone and
when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## Intro

The SAP Fiori elements templates support the features and settings for table rows or inline items detailed below.

For design information see the table guidelines, starting with [Table Overview](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview), and the links below.

## Feature Availability

Table

#### Actions

[Empty Row for Data Entry in Create and Edit Modes](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#empty-row-for-data-entry-in-create-and-edit-modes)
tables: the table displays an empty row for data entry.
You can turn it off for edit mode.

Editable Multi-Input Fields

[Inline Actions](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#inline-actions)

[Direct Edit](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#direct-edit)
elements for OData V2

[Conditional Enablement of Navigation Buttons](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#conditional-enablement-of-navigation-buttons)
- Available with SAP Fiori elements for OData V4
- Requires an extension with SAP Fiori elements for OData
V2

[Single Item Selection](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#item-selection)

[Multiple Item Selection](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#item-selection)

[Item Limit for Multiple Selection](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#item-selection)
tree tables. You can change the limit.

[Delete](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#delete)

[Custom Actions](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#custom-actions)

[Messages for Critical Actions](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#messages-for-critical-actions)
meaningful text for the user.

#### Display

[Restrict Field to Read Only in a Table](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#read-only-field)

[Editing Status](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#editing-status)
the responsive table and grid table in a list report.
With SAP Fiori elements for OData V4, it is also
displayed by default in a tree table.

[Rating Indicator](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#rating-indicator)

[Progress Indicator](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#progress-indicator)

[Quick Contact View](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#quick-contact-view)

[Avatar](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#avatar-and-other-images)

[Avatar Tooltip](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#avatar-and-other-images)

[Other Images](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#avatar-and-other-images)

Table Cells with Multiple Values
In edit mode, the multiple values fields are editable in
object page tables.
The cells that displayed multiple values in the table
onscreen are empty when exported to a spreadsheet.

[Highlighting New Line Items](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#highlighting-line-items)
Default with SAP Fiori elements for OData V4 for grid and
responsive tables in draft-enabled applications

[Highlighting Line Items Based on Criticality](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#highlighting-line-items)

#### Responsive Table Only

[Multiple Fields in a Single Column](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#multiple-fields-in-a-single-column)

[Smart Micro Chart](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#smart-micro-chart)

## Actions

### Empty Row for Data Entry in Create and Edit Modes

With this feature, when the object page is in create or edit mode, responsive tables and grid tables display one empty row where the users can enter data for a new subobject.

The empty row:

- Is displayed at the top of the responsive table.
  The toolbar has no *Create* button.
- Is displayed at the end of a grid table.
  The *Create* button in the toolbar scrolls to the empty row at the end of the table and puts the focus on the first editable field.
- Has no inline navigation action to the item via the chevron.
- Cannot be sorted or grouped because it doesn’t exist in the table on the back end.

With SAP Fiori elements for OData V4, you can set the empty row to be deletable.

If the users delete all the empty rows in the table, a new one is added so they can continue data entry.

*An empty row is displayed in the responsive table in create or edit mode*

#### Automatic Creation of a New Empty Row

After users start to enter data in one field in the empty row, a new empty row is added underneath it so they can continue data entry for either one column or one row at a time.

The row with data in one field:

- Is highlighted with a blue line to its left to show it’s a newly created draft
- Displays the navigation chevron
- Can also display an inline delete action
- Displays error messages for [mandatory fields](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#mandatory-fields) without a value.

If users do not enter data in a new empty row, it is removed when the users save.

*After the user starts entering data in the empty row, a new one is displayed*

#### Drafts Saved for Rows

A draft for a once empty row is saved after the users:

- Shift the focus away from the input field in the row with SAP Fiori elements for OData V4
- Have shifted their focus away from the input field in the row and an interval of 20 seconds has passed with SAP Fiori elements for OData V2

#### Enablement Options

In draft-enabled applications, with both versions of SAP Fiori elements, you can enable or disable this feature for:

- An application so the setting applies to all grid tables and responsive tables in all object pages
- A table so it applies only to the table

When settings are made at **both** application and table levels, the table setting takes priority.

Additionally, with SAP Fiori elements for OData V2, you can enable or disable the feature at the object page level. When the settings are made at application, object page, and table levels, the setting at the most granular level takes priority, as follows: table, object page, application.

##### User-Enabled Creation of Empty Rows in Edit Mode

In edit mode, you can turn off the default creation of empty rows for tables whose maintenance mostly requires updating data in existing rows.

If the users want to create additional rows, the *Create* button lets them enable the automatic creation of one empty row.

On first click, the *Create* button creates the empty row. On subsequent clicks, the *Create* button moves the focus to the first editable field in the first empty table row. After the users save their changes, the automatic creation of empty rows is turned off.

#### Additional Settings

When you enable the empty row creation, for the empty row, you can also set:

- [Mandatory fields](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-rows-sap-fiori-elements-2#mandatory-fields)
- Default values to populate fields
- Fields to be read-only at creation time and become editable only after the row is saved

##### Mandatory Fields

In create and edit modes, both versions of SAP Fiori elements guide users in completing the required fields for an empty row, as follows:

- With SAP Fiori elements for OData V4, a red asterisk (\*) is displayed in the column header label for the mandatory fields.
- Both SAP Fiori elements for OData V2 and V4 show an error message strip above the table:
  - When the table does not display mandatory columns. It instructs users to display the columns from the table settings.
  - When mandatory fields are not filled. In addition to the message strip for the table, the mandatory field displays a value state message. “*Enter a value*” is the the placeholder message text.

> **Guideline:** Replace the placeholder text to specify the value to enter with wording more meaningful to the users, for example, “*Enter a delivery date.*”
You can do this in the `i18n` file for the application.
For more information see: [Replacing Placeholder Text (SAP Fiori Elements)](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/replacing-placeholder-text).

### Inline Actions

You can define actions for table rows or inline items. The action types can be:

- Actions that occur in the system while the user stays on the list report screen, for example *Approve* or *Reject*.
- Actions that navigate to a different application, for example, when the user can open a purchase requisition from a specific purchase order in the table.

When a page contains a grid table, an analytical table, or tree table that leads to object or subobject pages, users can navigate to the object or subject page at row level. The *Show Detail* button is not displayed in these tables. Instead, users can click the navigation indicator: :navigation-right-arrow: .

#### Direct Edit

You can enable this action to let users navigate from the table row to the corresponding object page in edit mode with the *Edit* icon :edit: with SAP Fiori elements for OData V2.

This feature is available for responsive and grid tables. When it’s enabled, the object page footer displays the *[Save and Next](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/object-page/object-page-footer-bar-sap-fiori-elements#save-and-next)* button.

For more information, see:

- [Action Placement](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement)
- [UI Text Guidelines for SAP Fiori](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/ui-text-guidelines-for-sap-fiori#word-choice) 
### Conditional Enablement of Navigation Buttons

In list reports and object pages:

- With SAP Fiori elements for OData V4, you can enable buttons that navigate the user to another page or application based on the value of a specific field.
- With SAP Fiori elements for OData V2, this feature requires extensions.

For example, you can enable the Generate Purchase Order button only for sales orders with the completed status.

> **Guideline:** Implement this feature only when the way to enable the button is obvious to end users.

### Item Selection

Both versions of SAP Fiori elements allow you to determine whether users can select:

- One table row for a toolbar action, using a radio button.
- Multiple table rows for a toolbar action, using checkboxes.
  For an object page, you can enable selection of multiple rows for **all the tables** on the page, or for **specific tables only**.
  For an analytical table, grid table, or tree table, ask the development team to use the [Multi-Selection Plugin](https://www.sap.com/design-system/fiori-design-web/ui-elements/analytical-table-alv/#select).

When the selection of multiple rows is enabled for a table, both versions of SAP Fiori elements have the following defaults that you can change:

- Display of either the *Clear All* or *Select All* checkbox in the header of the selection column. The two versions differ in the way they do this.
  For complete information, see: [Clear All / Select All](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/table-features-sap-fiori-elements#clear-all--select-all).
- A limit of 200 rows that the user can select at once for grid tables, analytical tables and tree tables.
  You can change the limit. We recommend you consult the application team on how a change would impact performance.

#### SAP Fiori Elements for OData V2

By default, single selection is enabled for a table. You can enable multiple item selection, known by application developers as multiselect.

#### SAP Fiori Elements for OData V4

With the default auto mode, the application checks whether any table toolbar actions depend on item selection to be enabled. If not:

- In display mode, item selection is not possible.
- In edit mode, when the delete action is enabled, multiple selection is also enabled.

Instead, you can enable one of the following selection modes:

- None:
  - Display mode allows no item selection.
  - Edit mode allows multiple item selection when a *Delete* action is available in the table toolbar.
- Single: Both display and edit modes allow single item selection.
- Multi: Both display and edit modes allow multiple item selection.

> **Warning:** When you enable multiple selection for the **table**, do not enable a delete action in the **table rows**. The application will fail to load when both these features are enabled.
Instead, enable a delete action for the **table**. The delete action is then available in the table toolbar.

For more information, see:

- Responsive Table: [Select](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/#select)
- Analytical Table: [Select](https://www.sap.com/design-system/fiori-design-web/ui-elements/analytical-table-alv/#select)
- Grid Table: [Select](https://www.sap.com/design-system/fiori-design-web/ui-elements/grid-table/#select)
- Tree Table: [Selection Modes](https://www.sap.com/design-system/fiori-design-web/ui-elements/tree/#selection-modes)

> **Hint:** For more information, refer the development team to:
- [Enabling Multiple Selection in Tables](https://ui5.sap.com/#/topic/116b5d82e8c545e2a56e1b51b8b0a9bd)
- [Multi-Selection Plugin](https://www.sap.com/design-system/fiori-design-web/ui-elements/analytical-table-alv/#select)

### Delete

In responsive tables only, you can:

- Display an inline delete action.
- Prevent the deletion of certain rows.

In support of best design practices, SAP Fiori elements **does not** allow you to combine an **inline** delete action with a **central** delete action in the toolbar.

For more information, see [Delete Single Item Rows](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/#delete-single-item-rows).

### Custom Actions

You can define custom inline actions.

Because custom inline actions are grouped, you cannot control their exact display order. However, you can control which columns display the groups.

### Messages for Critical Actions

For actions that you set as critical, you can display one of the following after the user triggers the action:

- A message toast confirmation
- A confirmation message box to check the users want to proceed with specific critical actions

Also, the backend can require a confirmation on some actions. In this case, the confirmation message is always shown in a message box.

> **Guideline:** Replace the generic placeholder text in the messages with text that’s meaningful to the users, as shown in the
example below. You do this by providing the new text to the develoment team for update in the application’s
internationalization (i18n) file for the object type.
Ask the development team whether or not the backend requires confirmations for your use case.

#### Example

Table
**SAP Fiori elements for OData V2**   | **SAP Fiori elements for OData V4**

**Default Text**     | “Do you really want to execute the    | “Do you really want to perform this
action \<Action Label>?”              | action?
\<Action Label> is the label shown on
the button.
**Replacement Text** | “Are you sure you really want to      | “Are you sure you really want to
activate this product?”               | activate this product?”

For more information, see [UI Text Guidelines for SAP Fiori Apps](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/ui-text-guidelines-for-sap-fiori).

## Display

You can include the display features described below in a table row or inline item.

### Read-Only Field

With SAP Fiori elements for OData V4, you can set a field to display as read-only in a table, but set it as editable in another place on the UI.

### Editing Status

By default, for draft-enabled applications, in a list report, the editing status is displayed:

- In the first column of a responsive table
- In a separate column, next to the key column, in a grid table. The column is unlabeled. Users can hide or display it by deselecting or selecting *Edit Status* in the table personalization dialog.

You can also add the semantic key to the status.

The edit status reflects the state of the object or item in the processing cycle. For example, it can give the user information about the state of completion for the item or whether it’s currently available.

- For Unsaved Changes and Locked statuses, a popover displays the full name or technical name of the user who last changed the object when the name is available. “Another user” is displayed when it’s not.
- For Draft, Unsaved Changes and Locked statuses, a popover displays the user who last changed the item and the time of the change.

For more information, see [Tables](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/draft-handling#tables).

### Rating Indicator

You can add an inline, read-only rating indicator and define a maximum rating of up to five stars. By default, five stars is the maximum.

The number of stars displayed depends on the value of a field in the backend. Decimal values are rounded up or down and when the value after the decimal point falls between x.25 and x.74, it is represented by a half star.

**With extensions,** you can enable editing of the rating indicator

For more information, see [Rating Indicator](https://www.sap.com/design-system/fiori-design-web/ui-elements/rating-indicator/).

### Progress Indicator

You can:

- Enable an inline progress indicator to visually represent the level of completion of a project or goal, for example.
- Set the progress measure as a percentage or an absolute number, for example 3 or 8.
- Configure the progress bar to reflect the state of progress with color, based on the criticality of the progress.

For more information, see [Progress Indicator](https://www.sap.com/design-system/fiori-design-web/ui-elements/progress-indicator/).

### Quick Contact View

You can add a quick view to a contact to display key contact details in a popover.

For applications with Microsoft Team integration, the contact quick view card displays options for starting an audio call, video call, or chat in with the contact in Microsoft Teams.

For more information, see [Quickview](https://www.sap.com/design-system/fiori-design-web/ui-elements/quickview/).

Default (col-1)

Default (col-1)

### Avatar and Other Images
You can display an avatar in the row and set a tooltip that displays when the focus is on the avatar.

> **Warning:** Other images are not displayed correctly within the table borders. Only use them with live box mode.

Default (col-1)

For more information, see [Avatar](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar/).

Section Metadata

style

### Highlighting Line Items
By default, with SAP Fiori elements for OData V4, in
draft-enabled applications, a newly created item in draft
status is always highlighted in blue in grid and
responsive tables.
Highlighting of new line items in draft-enabled
applications is available with both SAP Fiori elements for
OData V2 and V4.
You can also define highlighting and icons for line items
based on their criticality.
After a newly created item is saved, it is highlighted
according to the criticality, as follows:
- Green for success (criticality value 3)
- Yellow for warning (criticality value 2)
- Red for error (criticality value 1)
- No highlighting for no criticality (criticality value 0)
## Responsive Table Only

In a responsive table, you can include the display features described below in a table row or inline item.

### Multiple Fields in a Single Column
You can combine multiple IDs, descriptions, and action buttons in a single column in a responsive table.
For example, you can display the following in a single column:
- Company name
- Company ID
- Items in Stock
- Progress Indicator for Items in Stock
- Overall value of the Items
- Multiple Action buttons that allow the user to both:
- Execute an action while staying on the list report page
- Navigate to other objects and applications
The visibility and position in the table of a column that combines multiple fields can be changed.
#### Field Labels
By default, with SAP Fiori elements for OData V4, when a column contains a field group with more than one
field, the labels for those fields are not displayed.
You can enable the display of a label for each field. Then, the field group label is displayed as the column
title in the header.
**Limitation on Export to Spreadsheet**
When users export a table with a column that contains multiple fields to a spreadsheet, only the **first piece of information** displayed in the column is exported.

---

## Table Types Sap Fiori Elements

# Table Types

**> **Information, External_Only:** **

No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData
V4.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with
their behavior – both standalone and when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).


No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData V4.
For information on the latest release of both versions of SAP Fiori Elements, see: [What's New](https://ui5.sap.com/#/topic/99ac68a5b1c3416ab5c84c99fefa250d) in SAPUI5 documentation.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with their behavior – both standalone and
when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## Intro

The SAP Fiori elements templates support the features and settings for the different table types detailed below.

For design information, see the guidelines starting with [Table Overview](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview), and see the links below.

## Feature Availability

\
Table

### Table Type                                                                                                                          | ### Responsive Table (Default) | ### Analytical                                                                                                                                                                                                                                     | ### Grid                                                                                                                                                                                                                                           | ### Tree

#### SAP Fiori Elements for OData Version                                                                                               | #### V2 & V4                   | #### V2 & V4                                                                                                                                                                                                                                       | #### V2                                                                                                                                                                                                                                            | #### V2 & V4

**Devices**

Desktop                                                                                                                                 | **:accept:**                   | **:accept:**                                                                                                                                                                                                                                       | **:accept:**                                                                                                                                                                                                                                       | **:accept:**

Tablet                                                                                                                                  | **:accept:**                   | **:accept:**                                                                                                                                                                                                                                       | **:accept:**                                                                                                                                                                                                                                       | **:accept:**

Phone                                                                                                                                   | **:accept:**                   | **:decline:**                                                                                                                                                                                                                                      | **:decline:**                                                                                                                                                                                                                                      | **:decline:**

**Responsive**\                                                                                                                         | **:accept:**                   | **:decline:**                                                                                                                                                                                                                                      | **:decline:**                                                                                                                                                                                                                                      | **:decline:**
(hide column, popin support)                                                                                                            |                                |                                                                                                                                                                                                                                                    |
**Density Mode**                                                                                                                        |                                | See [Analytical Table: Compact, Cozy, Condensed](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/analytical-table-alv/#compact-cozy-and-condensed).                                                    | See [Grid Table: Compact, Cozy, Condensed](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/grid-table/#compact-cozy-and-condensed).                                                                    | See [Tree Table: Types.](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/tree-table/#types)
See [Content Density](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/visual/cozy-compact). |                                |                                                                                                                                                                                                                                                    |
Compact density                                                                                                                         | **:accept:**                   | **:accept:**                                                                                                                                                                                                                                       | **:accept:**                                                                                                                                                                                                                                       | **:accept:**

Condensed density                                                                                                                       | **:decline:**                  | **:accept:**                                                                                                                                                                                                                                       | **:accept:**                                                                                                                                                                                                                                       | **:accept:**

Cozy density                                                                                                                            | **:accept:**                   | **:accept:**                                                                                                                                                                                                                                       | **:accept:**                                                                                                                                                                                                                                       | **:accept:**

Summarized cell                                                                                                                         | **:decline:**                  | **:accept:**                                                                                                                                                                                                                                       | **:decline:**                                                                                                                                                                                                                                      | **:decline:**

Hierarchical data                                                                                                                       | **:decline:**                  | **:decline:**                                                                                                                                                                                                                                      | **:decline:**                                                                                                                                                                                                                                      | **:accept:**

Large number of rows (> 200)                                                                                                            | :alert:                        | **:accept:**                                                                                                                                                                                                                                       | **:accept:**                                                                                                                                                                                                                                       | **:accept:**

Grouping                                                                                                                                | **:accept:**                   | **:accept:**                                                                                                                                                                                                                                       | **:decline:**                                                                                                                                                                                                                                      | **:decline:**

Freeze columns                                                                                                                          | **:decline:**                  | **:accept:**                                                                                                                                                                                                                                       | **:accept:**                                                                                                                                                                                                                                       | **:accept:**

Horizontal scrolling                                                                                                                    | **:decline:**                  | **:accept:**                                                                                                                                                                                                                                       | **:accept:**                                                                                                                                                                                                                                       | **:accept:**

Merge duplicates                                                                                                                        | **:accept:**                   | **:decline:**                                                                                                                                                                                                                                      | **:decline:**                                                                                                                                                                                                                                      | **:decline:**

Supported Inline Controls                                                                                                               | **All**                        | **Limited**\                                                                                                                                                                                                                                       | **Limited**\                                                                                                                                                                                                                                       | **Limited**
| See [Inline Controls for Non-Responsive Tables](https://www.sap.com/design-system/fiori-design-web/v1-130/discover/frameworks/sap-fiori-elements/tables-and-lists/table-types-sap-fiori-elements#inline-controls-for-non-responsive-tables) below. | See [Inline Controls for Non-Responsive Tables](https://www.sap.com/design-system/fiori-design-web/v1-130/discover/frameworks/sap-fiori-elements/tables-and-lists/table-types-sap-fiori-elements#inline-controls-for-non-responsive-tables) below. | See [Inline Controls for Non-Responsive Tables](https://www.sap.com/design-system/fiori-design-web/v1-130/discover/frameworks/sap-fiori-elements/tables-and-lists/table-types-sap-fiori-elements#inline-controls-for-non-responsive-tables) below.

Row-based                                                                                                                               | **:accept:**                   | **:decline:**                                                                                                                                                                                                                                      | **:decline:**                                                                                                                                                                                                                                      | **:decline:**

Column-based                                                                                                                            | **:decline:**                  | **:accept:**                                                                                                                                                                                                                                       | **:accept:**                                                                                                                                                                                                                                       | **:accept:**

## Inline Controls for Non-Responsive Tables

These inline controls are supported for grid, analytical, and tree tables:

Columns

- Text         | - ComboBox          | Also, the following when they are of
- Label        | - MultiComboBox     | a responsive or very small size:
- ObjectStatus | - CheckBox
- Icon         | - Link              | - StackedBarMicroChart
- Button       | - Currency          | - ComparisonMicroChart
- Input        | - RatingIndicator   | - BulletMicroChart
- DatePicker   | - ProgressIndicator
- Select       |

---

## Tables Toolbar

# Table Toolbar

**> **Information, External_Only:** **

No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData
V4.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with
their behavior – both standalone and when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).


No longer maintained, this article reflects the SAPUI5 version 1.136 release of SAP Fiori Elements for OData V2 and SAP Fiori Elements for OData V4.
For information on the latest release of both versions of SAP Fiori Elements, see: [What's New](https://ui5.sap.com/#/topic/99ac68a5b1c3416ab5c84c99fefa250d) in SAPUI5 documentation.
To explore the design capabilities of SAP Fiori elements for OData V4 and the various options for the building blocks, and to experiment with their behavior – both standalone and
when used in standard floorplans or custom pages, see: the [SAP Fiori Development Portal](https://sapui5.hana.ondemand.com/test-resources/sap/fe/core/fpmExplorer/index.html#/topic/introduction).

## Intro

The SAP Fiori elements templates support the features and settings for the table toolbar detailed below.

For design information, see the guidelines starting with [Table Overview](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/table-overview), and see the links below.

## Feature Availability

Table

#### List Report and Object Page Features

Title
You can hide it.
You can show the table row count next to the title.

Infobar
summarizes the filter criteria applied to the table data. It is displayed below the table toolbar and above the
column headings when at least one filter is set.

Order of Toolbar Actions
with the most frequently-used action and ending with the most seldom-used action, regardless of whether the action
is a custom or standard one.

[Table Personalization Actions](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#table-personalization-actions)

[Show/Hide Details](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#show-hide-details)

[Mass Edit](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#mass-edit)
- In both the list report and object page with SAP Fiori elements for OData V4
- In the list report with SAP Fiori elements for OData V2

[Export](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#export)
- *Export to Spreadsheet* is enabled by default.
- *Export to PDF* is available.
With SAP Fiori elements for OData V2, *Export to Excel* is enabled by default in:
- A list report table
- An object page table **only if** the *Paste* icon is displayed

[Copy to Clipboard](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#copy-to-clipboard)

[Paste from Clipboard](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#paste-from-clipboard)

[Application-Specific Actions](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#applicationspecific-actions)

[Actions Disabled Before Row Selection](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#actions-disabled-until-the-user-selects-a-row)

[Conditional Enablement of Navigation Buttons](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#conditional-enablement-of-navigation-buttons)
Requires an extension with SAP Fiori elements for OData V2

[Grouping Actions in a Menu Button](https://main--builder-prospect-prod--sapudex.aem.page/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#grouping-actions-in-a-menu-button)

[Messages for Critical Actions](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#messages-for-critical-actions)

[Messages for Destructive Actions](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#messages-for-destructive-actions)

[Multiple Views on a Table](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#multiple-views-for-a-table)

#### List Report Only Features

Toolbar Sticky Behavior

[Standard Actions](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#standard-actions): *Create* and *Delete*

Object Creation via an Object Page

[Object Creation via a Dialog](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#via-a-dialog)

[Object Creation with Reference to Another Object](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#via-a-dialog-with-a-reference-to-an-existing-object-of-the-same-type)

[Copy Object](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#copy-object)
You determine the label on the action button.

[Hiding Actions in Multiple Content Layout](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#hiding-actions-in-multiple-content-layout)

Message Strip for the Table

[Add Card to Insights](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#add-card-to-insights)
You can turn it off.

#### Object Page Only Features

[Search](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#search)

[Edit](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#edit)

[Delete](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#delete)

[Subobject Creation via Subobject Page](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#subobject-creation)

[Subobject Creation via Dialog](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#subobject-creation)

[Create Not Visible](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#create-action-visibility)

[Inline Creation](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#inline-creation)

[Prefilling Fields for New Object Creation](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#prefilling-fields-for-a-new-object)

[Full Screen Mode for Table Display](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#full-screen-mode-for-table-display)

[Segmented Button for Switching Table Views](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#content-switch-for-table-views)

[Select Control for Switching Table Views](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#content-switch-for-table-views)

## List Report and Object Page Features

The information below relates to table toolbar actions and settings in **both** the list report and object page floorplans.

### Table Personalization Actions

By default, sort, group and order actions are enabled for the table. They are available in the *Personalization* dialog as tabs. Users open the dialog with the *Settings* icon button.

For specific use cases, you can disable the actions.

Table-level view management is not a prerequisite for personalization.

For more information, see [Table Personalization (Overview)](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/overview-table-personalization).

### Show / Hide Details

The responsive table toolbar displays the *Show Details* action when at least one column is hidden from the screen because of limited onscreen space.

After the user clicks *Show Details*, the the table displays the hidden information in the [pop-in area](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/#responsiveness), and the action changes to *Hide Details*.

The importance assigned to a column determines whether or not the table displays its values onscreen when screen space is limited:

- The values from high importance columns are always displayed onscreen — as columns or in the pop-in area, depending on the screen size.
- The values in columns with low importance are first to be hidden.

By default, in responsive tables:

- Key fields have the importance set to high in list reports.
- Other columns have the importance set to none and are handled like columns assigned medium importance.

You can change the level of importance.

### Mass Edit

You can enable mass edit in responsive tables and grid tables for applications with draft handling in the:

- List report with SAP Fiori elements for OData V2
- List report and object page with SAP Fiori elements for OData V4

#### List Report

Users cannot apply the mass edit to a draft record.

The edit is applied to all the objects selected that don’t return errors or warnings during the update. When they **do** return an error or warning, none of their fields are updated.

#### Object Page

With SAP Fiori elements for OData V4, you can enable the mass edit for a table in the object page. When the object page is in display mode, users can apply the mass edit to the subobjects in a table.

#### Fields Displayed in the Edit Dialog

By default, the *Edit* dialog contains all the table columns that are currently visible and editable.

The application team can define the fields that display in the dialog, by both:

- Including fields in the dialog that **are not** displayed in the table
- Excluding fields from the dialog fields that **are** displayed in the table

> **Hint:** For more information on enabling this feature for an object page table with SAP Fiori elements for OData V4, you can refer application
developers to [Using the Mass Edit Functionality](https://sapui5.hana.ondemand.com/#/topic/965ef5b2895641bc9b6cd44f1bd0eb4d).

### Export

The export action exports the values in a table. When enabled, it is displayed in the table toolbar.

- With SAP Fiori elements for OData V4:
  - *Export to Spreadsheet* is enabled by default.
  - *Export to PDF* is available.
  - By default, a maximum of 1000 rows can be exported. The application development team can change the limit.
  - Columns that contain a [multi-input field](https://www.sap.com/design-system/fiori-design-web/ui-elements/multiinput/) (1:N) are not exported.
- With SAP Fiori elements for OData V2 *Export to Excel* is enabled by default in:
  - A list report table
  - An object page table if the *Paste* icon is available

For more information see [Export to Spreadsheet](https://www.sap.com/design-system/fiori-design-web/ui-elements/export-to-spreadsheet/).

> **Hint:** For more information, refer application developers to:
- [Using the Export Button (SAP Fiori elements for OData V4)](https://sapui5.hana.ondemand.com/sdk/#/topic/4bab6f2043814257974b52d4dafe1dcd)
- [Adapting the UI: List Report and Object Page (SAP Fiori elements for OData V2)](https://sapui5.hana.ondemand.com/sdk/#/topic/0d2f1a9ebd2d4a4c906216ded1d33783)

### Copy and Paste

Users can copy to the clipboard data from other SAP Fiori elements applications or from external applications — such as Microsoft Excel or Microsoft Word — and then, paste the data from the clipboard to tables in SAP Fiori elements applications that are editable.

#### Copy to Clipboard

By default, the *Copy* action is displayed in the table toolbar. This includes tables with the selection type of none with SAP Fiori elements for OData V2.

With it, users can copy multiple rows or ranges of rows and columns to the clipboard.

They can select a range of cells in rows or columns:

- With their mouse, by clicking and holding the mouse button while they select the cells
- With the key combinations, described in [Copying Multiple Rows and Range Selections](https://sapui5.hana.ondemand.com/sdk/#/topic/c0f6592a592e47f9bb6d09900de47412)

#### Paste from Clipboard

The *Paste* action is displayed in the table toolbar if the table supports it.

After users copy data from another SAP Fiori elements application or an external application, they can paste it to:

- **The table**

Users set the focus on the table or select an empty row before pasting the data. One or more new rows are created for the pasted data.

This feature is available only for draft-enabled applications and for tables where inline creation or the insertion of empty rows has been enabled.

- **A cell or range of cells, only in grid and responsive tables**

Users select a cell or cell range within the table and paste the data. If the selected cell or cells are in:

- - Active or draft rows, the pasted data replaces the values in those rows.
  - An empty row, new rows are created for the pasted data.

To paste, they can use the *Paste* action in the toolbar or use a keyboard shortcut (**Ctrl+V** for Microsoft Windows, **Cmd+V** for MacOS).

#### Limitations

- Pasting is supported only for fields that contain a single value, not for complex fields, such as smart links and images.
- If there are validation errors, a dialog displays an error message so the user can take remedial action.
- The greater the number of records copied, the longer the paste operation takes.
- The order of the of the data copied from the spreadsheet can differ from the order in the table in the application after the paste. SAP Fiori elements cannot control this.
- Users cannot paste data into custom columns of tables.
- This feature is not supported for custom tables.

> **Information:** Pasting the data from the clipboard into another SAP Fiori elements table can cause formatting issues because the copy action doesn’t separate the
content of fields that include more than one value, for example, a field with both an amount and a currency or both a value and its description.
Instead, we recommend users [export the data into a spreadsheet](https://www.sap.com/design-system/fiori-design-web/ui-elements/export-to-spreadsheet/)
format that separates multiple values in one field into separate columns, with a single value in each, and then, adjust the format to match the one the
target table.

> **Hint:** For more information, refer application developers to
- [Tables](https://sapui5.hana.ondemand.com/sdk/#/topic/c0f6592a592e47f9bb6d09900de47412)
- [Copying and Pasting from External Applications to Tables](https://ui5.sap.com/#/topic/f6a8fd2812d9442a9bba2f6fb296c42e)

### Application-Specific Actions

You can define these actions and the text displayed on the buttons.

The application team can control when the action button is displayed and enabled.

For application-specific actions, application teams can define custom keyboard shortcuts.

For more information, see:

- [Action Placement](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/action-placement)
- Terminology for Common Actions

> **Hint:** For more information on shortcuts, refer application developers to [Keyboard Shortcuts](https://sapui5.hana.ondemand.com/#/topic/0cd318c83ec5473d9a091c1782d03c21).

### Actions Disabled Until the User Selects a Row

You can set actions in the table toolbar to display as disabled until the user selects one or more table rows for the action.

Note that the development team may call actions that require selection “context-dependent” actions and actions that are enabled without a selection “context-independent” actions.

For more information, see [UI Element States](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/ui-element-states).

### Conditional Enablement of Navigation Buttons

With SAP Fiori elements for OData V4, you can enable buttons that navigate the user to another page or application based on the value of a specific field.

With SAP Fiori elements for OData V2, this feature requires extensions.

For example, you can enable the Generate Purchase Order button only for sales orders with the completed status.

> **Guideline:** Implement this feature only when the way to enable the button is obvious to end users.

### Grouping Actions in a Menu Button

With SAP Fiori elements for OData V4, you can group actions that have a similar business purpose in a menu button.

Note that when **all the actions** in the the menu have one of the following states, the menu button state matches the one:

- Disabled
- Hidden

### Messages for Critical Actions

For actions that you set as critical, you can display one of the following after the user triggers the action:

- A message toast confirmation
- A confirmation message box to ensure the user wants to proceed with specific critical actions

Also, the backend can require a confirmation on some actions. In this case, the confirmation message is always shown in a message box.

> **Guideline:** Overwrite the default message text so it’s meaningful to the users, as shown in the example below. Provide the new
text to the development team. Then, the development team updates it in the application’s internationalization (i18n)
file for the object type.
Ask the development team whether or not the backend requires confirmations for your use case.

#### Example

Table
**SAP Fiori elements for OData V2**   | **SAP Fiori elements for OData V4**

**Default Text**     | “Do you really want to execute the    | “Do you really want to perform this
action \<Action Label>?”              | action?
\<Action Label> is the label shown on
the button.
**Replacement Text** | “Activate this product?”              | “Do you want to activate this
| product?”

For more information, see:

- [Replacing Placeholder Text](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/replacing-placeholder-text)
- [Message Handling](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/messaging)
- [UI Text Guidelines for SAP Fiori Apps](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/ui-text-guidelines-for-sap-fiori)

### Messages for Destructive Actions

By default, a message is displayed for confirmation of an action that will delete or destroy important data.

> **Guideline:** Overwrite the default message text so it’s meaningful to the users, as shown in the example below. Provide the new
text to the development team. Then, the development team updates it in the application’s internationalization (i18n)
file for the object type.
Ask the development team whether or not the backend requires confirmations for your use case.

#### Example

Table
**SAP Fiori elements for OData V2**   | **SAP Fiori elements for OData V4**

**Default Text**     | The default message reuses the title  | “Do you really want to perform this
and the description defined for the   | action?
object in the table.
- In flexible column layout: Delete
object \<title> \<description>?
- For example, “Delete object 12345
(Sales Order)?”
- In full screen mode: Delete object
\<title>?
- For example, “Delete object 12345?”
**Replacement Text** | “Are you sure you really want to      | “Are you sure you really want to
delete this product?”                 | delete this product?”

For more information, see:

- [Message Handling](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/messaging/messaging)
- [UI Text Guidelines for SAP Fiori Apps](https://www.sap.com/design-system/fiori-design-web/foundations/writing-and-wording/ux-writing/ui-text-guidelines-for-sap-fiori)

### Multiple Views for a Table

You can display a table with multiple views, for example, each view of the same table can display different columns or prefiltered states.

For a maximum of three views, a segmented button is displayed. For four or more, the select control is displayed.

With SAP Fiori elements for V4, you can also display the row count for each view next to the view name.

## List Report Only Features

The information below relates **only** to table toolbar actions and settings in the list report floorplan.

### Standard Actions

By default, *Create* and *Delete* are enabled.

You can disable them.

You can also enable or disable the *Delete* button based on conditions specified in the backend.

**Example**

You can disable deletion for a sales order that has already been paid. When a user selects an item that cannot be deleted, the *Delete* button is disabled. In addition, if the user navigates from this item in the list report to the object page, the *Delete* button is hidden.

> **Warning:** In a responsive table, if you put a *Delete* button in the toolbar, do not enable the inline *Delete* for table rows.

### Create Object Actions

By default, the create via the object page feature is enabled. The create action opens the object page in create mode so the user can enter the data. Alternatively, you can enable object creation as described the sections below:

#### Via a Dialog

The action opens a dialog in modal view so the user can enter the data.

With both versions of SAP Fiori elements, you can:

- Include a maximum of eight fields in the dialog
- Enable filter values saved in the filter bar to prefill fields in the dialog. This feature requires an extension with SAP Fiori elements for OData V2.

> **Warning:** When you enable the object creation via a dialog feature, users cannot navigate to an object page in create mode.
Instead, they can navigate to the object page in display mode and switch to edit mode.
Note that when a user clicks *Cancel* in the create dialog, no draft states are maintained.

**> **Hint:** **

For more information, refer application developers to:
- [Enabling Object Creation Using the Dialog in the List Report](https://ui5.sap.com/#/topic/ceb9284b16f64f30865ce999dbd56064)

#### With Default Values That Prefill Fields for the New Object

This feature is available with:

- SAP Fiori elements for OData V2 for applications **without** draft handling
- SAP Fiori elements for OData V4

#### Via a Dialog with a Reference to an Existing Object of the Same Type
*Create from existing object*
With SAP Fiori elements for OData V4, application developers can build a
custom create action via a dialog that lets the user create a new object
with a reference to an existing object of the same type.
The user:
1. Clicks the action button.
You can name the button to suit your use case.
2. Selects the value of the existing object to reference in the dialog.
3. Completes the fields for the new object by selecting one or more
values to copy from the existing one.
4. Completes additional fields for the new object in the object page.
> **Hint:** For more information, refer application developers to:
- [Actions](https://sapui5.hana.ondemand.com/#/topic/cbf16c599f2d4b8796e3702f7d4aae6c)
- [Handling of the preferredmode Parameter](https://sapui5.hana.ondemand.com/#/topic/bfaf3ccf3d6d4735990cc793b21f5529)

### Copy Object

You can place a copy action button in the table toolbar to allow the user to create a new object with the same data as the selected object.

You set the label for the button according to your use case. Otherwise, the default label is *Copy*.

In the toolbar, the *Copy* button is displayed after the *Create* button.

> **Hint:** Application developers can define a standard copy action button by annotating a function import action (DataFieldForAction) as a *Copy* action. For more information, refer them to: [Actions in the List Report](https://sapui5.hana.ondemand.com/#/topic/993e99eae4414b73bc7afef9518c79bf).

### Hiding Actions in Multiple Content Layout

You can hide an action from a toolbar for a specific table when the list report contains multiple views with multiple tables.

For more information, see:

- [Multiple Content Layout](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/list-report/list-report-content-area-fiori-elements#multiple-content-layout)
- [General Layout](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/list-report-floorplan-sap-fiori-element/#general-layout)

### Add Card to Insights

By default, the *Add Card to Insights* option is displayed in the overflow toolbar of list report tables with the single content layouts when My Home in SAP S/4HANA Cloud is enabled.

You can ask the application development team to turn the option off.

For more information, see: [Simple Content Layout](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/list-report/list-report-content-area-fiori-elements#simple-layout-default).

> **Hint:** For more information on card creation and disabling it, refer application developers to [Creating Cards for the Insights Section of My Home in SAP S/4HANA Cloud](https://sapui5.hana.ondemand.com/#/topic/9b13559ef978405a99e8b624a87daf31).

## Object Page Only Features

The information below relates **only** to table toolbar actions and settings in the object page floorplan.

### Search

You can enable a search on the table.

The limit for search strings is 1000 characters.

For more information, see [Search](https://www.sap.com/design-system/fiori-design-web/ui-elements/search/).

### Edit

By default, *Edit* is displayed when the business object shown in the table is editable.

### Delete

By default, *Delete* is displayed in edit mode when the business object shown in the table is deletable.

You can enable or disable the *Delete* action to allow users to delete only in certain conditions.

For example, after the sales items for a Sales Order have shipped, you can hide the *Delete* action for the items. When a user selects an item that cannot be deleted, the *Delete* action is disabled.

When multiple selection is enabled for the table, the *Delete* action is enabled if at least one selected item is deletable.

> **Warning:** In a responsive table, if you put a *Delete* action in the toolbar, do not enable the inline *Delete* for table rows.

### Subobject Creation

By default:

- *Create* is displayed in edit mode when the business object shown in the table is editable. For specific circumstances when the *Create* button is disabled, see [Create Action Visibility](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#create-action-visibility) below.
- The default creation action is via the suboject page — the action opens the subobject page in create mode so the user can enter the data.

You can:

- Enable or disable the *Create* action to allow users to create subobjects only in certain conditions. For example, after a sales order reaches the Delivery is Shipped status, you can hide the *Create Sales Item* action.
- Enable creation of a subobject via a dialog with 8 fields maximum. The action opens a dialog in modal view so the user can enter the data. The dialog must contain all the mandatory fields for the subobject. With SAP Fiori elements for OData V2, you can enable filter values saved in the filter bar to prefill fields in the *Create* dialog.
- Enable inline create for draft-enabled applications in grid and responsive tables with SAP Fiori elements for V4. See [Inline Creation](https://www.sap.com/design-system/fiori-design-web/discover/frameworks/sap-fiori-elements/tables-and-lists/tables-toolbar#inline-creation) below.
- Enable default values to prefill the fields for the new object. This feature is available with SAP Fiori elements for OData V4, and with SAP Fiori elements for OData V2 for applications **without** draft handling.

> **Guideline:** Replace the default dialog title or subobject page title “New Item” to reflect the name of the subobject and to
provide a name for unnamed objects that’s meaningful to the user.

For more information, see:

- [Create Items](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/global-patterns/object-handling/manage-objects-with-the-global-flow#create-items)
- [Add Items](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/#add-items)

### Create Action Visibility

Whether or not the *Create* action is visible in the table toolbar depends on:

- The object page mode.
- Whether the flow is global or local.
- Where the user enters the data for the new subobject — in the subobject page or directly in the table with the inline edit.

Table

**Flow Type**              | **Read Mode for All Tables**      | **Edit Mode for Tables with        | **Edit Mode for Tables with
| Subobject Pages**                  | Inline Edit**

**Global Flow for          | - Navigation indicators           | - Navigation indicators            | - Navigation indicators
Draft-Enabled Applications |   :navigation-right-arrow: are    |   :navigation-right-arrow: are     |   :navigation-right-arrow: are
with Fiori Elements for    |   visible (if required).          |   visible (if required).           |   visible (if required).
OData V2**                 | - *Create* button is not visible. | - *Create* button is visible.      | - *Create* button is visible.

**Local Flow for Non-Draft | - Navigation indicators           | - Navigation indicators            | Not Supported.
Enabled Applications**     |   :navigation-right-arrow: are    |   :navigation-right-arrow: are not
visible (if required).          |   visible.
- *Create* button is visible.     | - *Create* button is not visible.
### Inline Creation

You can enable inline creation of entries for applications with draft handling enabled. The *Create* action is displayed in the table toolbar in edit mode.

The inline creation adds a new row to the table where the users can enter the subobject data.

By default, the new row is highlighted in blue and displayed at the top of the table. The highlighting disappears after the users save the data.

You can:

- Work with the development team to define a custom sort order.
- Enable default values to prefill the fields for the new object.

For more information, see [Add Items](https://www.sap.com/design-system/fiori-design-web/ui-elements/responsive-table/#add-items).

### Prefilling Fields for a New Object

You can turn this on in draft-enabled applications for the default create action via the object page, where the user navigates to another application to enter the data in the new object page.

The new object must be the main object on the object page.

You determine both the fields to prefill and the default values for the fields.

### Full Screen Mode for Table Display

You can enable full screen mode for a table. However, it is generally not recommended.

Users click the *Maximize* action in the toolbar to display to the table in a dialog. They can return to the object page by clicking either the *Minimize* or *Close* action.

For more information on the restrictions for this feature, see [Maximize/Minimize](https://www.sap.com/design-system/fiori-design-web/ui-elements/smart-table/#maximize--minimize).

### Content Switch for Table Views

The number of views defined for a table determines the UI control that lets users [switch the table views](https://www.sap.com/design-system/fiori-design-web/ui-elements/table-bar/#content-switch):

- A [segmented button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/#segmented-button) for a maximum of three views
- A [select control](https://www.sap.com/design-system/fiori-design-web/ui-elements/select/) for four or more views.

By default, the count or number of records in the view is not displayed next to the title of the content switch for table views for performance reasons. Talk to the development team about how displaying the counts impacts performance for your use case.

---

