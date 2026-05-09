# SAP Fiori Foundations: Integration And Services

## Sap Fiori Launchpad > Enterprise Search

# Enterprise Search

## Intro

The SAP Fiori launchpad offers an enterprise search function that searches across all apps and business objects, such as materials, customers, and maintenance
plans. The search icon is displayed in the [shell bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/shell-bar/) of the launchpad and is always readily available at the top of the screen.
*Search icon in the shell bar*

Default (col-1)

When pressing the search icon in the shell bar, the search field and the type selector appear.

> **Information, Col-1:** Some customers may not yet have business objects enabled for search. In this case, the UI adapts accordingly to
search for apps only. In particular, the type selector is not visible and the filter functionality is more limited.

Default (col-1)

After entering a search term, users can trigger the search by pressing ENTER, by clicking the magnifier icon, or by selecting one of the
suggestions. A search for *All* can be achieved by pressing ENTER in an empty search field or by using the \* query.
If the search field is left empty, clicking the search icon closes the search field.

Default (col-2)

*Search field in the shell bar*

Section Metadata

style

## Type Selection

The search can be restricted to objects of a particular
type.
*Type selection using dropdown*
This can be done before the search is triggered, either
by using the type selector or by typing the object type
into the search field and selecting the respective
suggestion.
To filter a result list by object type, users can select
the type tabs or the respective section in the filter
panel.
## Suggestions

When the user starts typing in the search field, suggestions appear. There are 3 main
suggestion types:
*Search suggestions*
- Type suggestions switch the type selector (for example, *Search In: Sales Orders*).
- App suggestions launch the app (for example, *App Create Leave Request*).
- Term suggestions execute a search with the respective terms (for example, *SAP Walldorf*)
## Result List

The result list is a ranked list of all matching items.
Different object types can have different
representations.
Apps are shown as tiles and can be launched.
Business objects are summarized in a few lines. Pressing
the title link of an object shows a full-screen
representation of that object, such as an object page or
a document viewer. If additional summary attributes area
available, clicking the down arrow :slim-arrow-down: on
the right will show them. This will also reveal
navigation shortcuts to apps that can handle the business
object.
The tabs at the top of the result list allow users to
filter by object type. The tabs are sorted by the number
of hits – categories with most hits appear first.
If the results have been limited to a certain object
type, additional actions appear in the upper right-hand
corner. Here, users can change the sort order, or switch
to a table representation with the option to show or hide
specific columns.
## Personalized Search

This feature allows the system to track the user’s search behavior in order to personalize and improve future rankings for search results. Algorithms analyze the user’s behaviors and interests, and adapt accordingly to support the user by focusing on context-relevant information.
Users can switch the personalized search on or off in the [User Menu](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/launchpad#user-menu) under *Settings* -> *[User Profiling](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/services#user-profiling-in-settings-dialog).* They can also delete collected data with the *Clear My History* button.
"Settings" dialog*
Some of these features might not be available to the user, depending on the system configuration.
## Filters

A filter icon in the top left-hand corner offers additional options for filtering the search results. When the user clicks the icon, a filter panel appears on the left-hand side. In this panel the user can change the object type, which may also be depicted as a hierarchy (depending on the system configuration).

Once the results have been limited to a certain object type, thus ensuring a homogeneous result set, result-specific filters are offered. Only meaningful filters are included. For example, if all results are for the same country, the country filter is not shown.

Up to 5 one-click options are available for each filter. You can show the selection options in a list, or visualize them in a bar chart or pie chart. Multiple selection is supported for all visualizations.

Once the filter panel has been closed, the applied filters are visible in an [infobar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/infobar/) above the result list. On the right of the infobar, all filters can be cleared without reopening the filter panel.

#### Filter Panel

Carousel (full-width)

## Advanced Filters

Default (col-1)

In addition to the the one-click filters, the user can set more filters by choosing *Show More* or *Show All Filters*.
This opens a filter dialog with a list of all the available filters on the left. The details for the selected filter
show on the right.
The available options depend on the data type of the filter (text-based, numeric, date) and the configuration. For
most filters, a list of filter conditions is shown, similar to the filter panel. For texts, this list can be filtered
and sorted. For numbers and dates, the user can add custom ranges. There is also an option to enter variable
conditions: Instead of picking items from a list, the user can specify advanced conditions like *begins with*.

Default (col-2)

#### Dialog for setting all available filters

Carousel (full-width, col-2)

*Infobar for displaying filters defined by the user*

Section Metadata

style

## Configuration

Default (col-1)

Users can switch the personalized search on or off, depending on the configuration.

> **Information, Col-2:** Users can access their individual settings via *[User Menu](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/launchpad#user-menu)* > S *ettings* > *[User Profiling](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/services#user-profiling-in-settings-dialog)* > *Personalized Search*.
System-wide configuration for the personalized search is done in the [Configure Personalized Search](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps\('F2800'\)/S11) app.

Section Metadata

style

Default (col-1)

Development teams can fine-tune the search for the business objects they are responsible for.

> **Information, Col-2:** In **search models**\, you can configure:
- Which attributes are searched in (including associations to other objects)
- Which attributes are displayed and in which order
- Which attributes are displayed as filters in the filter pane
- The importance of each attribute (for a proper search ranking)
- The semantics of each attribute (to select the proper matching/fuzzy algorithms)
Using **SAP Fiori launchpad intents** you can configure:
- What happens when the user clicks the title
- What actions are listed in expanded result list items
In the ***Define Synonyms*** **app**, you can configure the synonyms to be applied to each search.
In the ***Fine-Tune Ranking*** **app**, you can configure ranking factors and their influence.
*Examples:*
“products that are in stock are more important than others”
“new documents are more important”
“sales orders created by my team are more important”

Section Metadata

style

## Creation of Search Models

The display and behavior of the enterprise search is based on search models. Apply the following rules when creating search models.
- Implement the title of a search result as a **link to the [object page](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/page-types/floorplans/object-page/)** or an equivalent full screen representation of that particular business object.
- **Align** the title, subtitle, and object type with the corresponding object page. Displaying objects consistently makes them easier to scan.
- To help users recognize objects quickly, use **images** whenever they are available. However, don’t display indistinctive images or placeholder images.
- Include relevant **attributes** in the object preview. They can help users to distinguish between objects and answer common questions up front (such as a contact phone number).
- Do not show unimportant attributes or attributes that aren’t shown on the corresponding object page.
Hint: When choosing attributes, focus on attributes that are important during productive use. These can differ from attributes that seem most important during development. For example,
master data attributes like “Created On” and “Created By” would not normally be relevant for the preview.
- Use consistent attribute labels that are either identical or aligned (for example, “Team Type” vs. “Type” in the “Team” section of the object page).
- Align the attribute content, especially the display order of “text (ID)” attributes.
- Make **visible fields searchable** (note that this may not be possible for all fields due to technical constraints).
- Include **facets** only if they are meaningful as filter criteria. Otherwise, avoid them.
For example, a facet for an ID would not make sense – each ID would return a single result, rather than a set of results.

---

## Sap Fiori Launchpad

**Design System Hero**

# SAP Fiori Launchpad

## Overview

+----------------------------------------------------------------------x-----------------------------------------------------------------------+
Tiles (plain)
+----------------------------------------------------------------------x-----------------------------------------------------------------------+
[SAP Fiori Launchpad](https://www.sap.com/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/launchpad)
Learn about the key components of SAP Fiori Launchpad.

## Home Page and Spaces

+--------------------------------------------------------------------------x---------------------------------------------------------------------------+
Tiles (plain)
+--------------------------------------------------------------------------x---------------------------------------------------------------------------+
[Home Page](https://www.sap.com/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/home-page)
Explore the layout and features of the SAP Fiori launchpad home page.
+--------------------------------------------------------------------------x---------------------------------------------------------------------------+
[Spaces](https://www.sap.com/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/sap-fiori-launchpad-spaces)
Use spaces to structure the most relevant apps for users with a certain business role.
+--------------------------------------------------------------------------x---------------------------------------------------------------------------+
["My Home"](https://www.sap.com/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/sap-fiori-launchpad-my-home)
Discover how the “My Home” space enables personalized app access and organization.

## Enterprise Search

+-------------------------------------------------------------------------x--------------------------------------------------------------------------+
Tiles (plain)
+-------------------------------------------------------------------------x--------------------------------------------------------------------------+
[Enterprise Search](https://www.sap.com/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/enterprise-search)
Learn about search features, personalization options, and best practices for effective results.

## Services

+---------------------------------------------------------------------x----------------------------------------------------------------------+
Tiles (plain)
+---------------------------------------------------------------------x----------------------------------------------------------------------+
[Launchpad Services](https://www.sap.com/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/services)
Get to know essential launchpad services that support personalization, navigation, and user assistance.
+---------------------------------------------------------------------x----------------------------------------------------------------------+
[App Finder](https://www.sap.com/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/app-finder)
Understand how the app finder organizes and provides access to all available apps.

**Metadata**

Title

Breadcrumbs
Launchpad

---

