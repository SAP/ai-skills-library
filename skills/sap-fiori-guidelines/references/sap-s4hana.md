# SAP S/4HANA Design Guidelines

Specific design guidance for SAP S/4HANA applications.

## Ai Assisted Error Explanation

# AI-Assisted Error Explanation

## Intro

AI-assisted error explanation helps users understand and resolve the errors or warnings that they encounter when working on an object page in an application developed with SAP Fiori Elements.

Issue explanation

## When to Use

Use AI-assisted error explanation in workflows where the user encounters errors or warnings via the [message popover](https://www.sap.com/design-system/fiori-design-web/ui-elements/message-popover/) on an [object page](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/), and requires more details, and recommendations for resolving them.

Do
Use AI-assisted error explanation
- To provide users with a more detailed explanation for the errors or warnings that they encounter in
workflows on the [object page](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/object-page/)
- To recommend how to resolve the error or warning
- To speed up the users’ workflow
- To explain simple errors that the user may already know
how to resolve

## Anatomy

AI-assisted error explanation extends the dialog component to enable new AI-specific interactions.

*Structure of AI assisted error explanation dialog*

1. **Dialog Container**
2. **Short description of the error**
3. **Understanding the Issue** – an AI-generated explanation of the error
4. **“Show more” button –** For progressive disclosure of a lengthy description.
5. **Resolving the issue –** AI-generated recommendations on resolving the issue
6. **AI Notice** 
7. **Feedback icons**
8. **Footer –** with *Copy All* and *Close* buttons

## Behavior & Interaction

When the user encounters an error or warning on the object page in edit mode, it appears in the message popover. The user can navigate to the message and trigger an AI-generated explanation with the *Explain* button.

Message popover with ‘Explain’ button

### During Generation

**Busy indicator:** The *Issue Explanation* dialog shows a busy indicator to inform the user that AI is generating the explanation.

Generating an error explanation (generation)

### After generation

When generation is complete, the error explanation text is displayed in the dialog. The text headings ensure easy readability, and consistency. The user can share the explanation with the *Copy All* button.

Generation of error explanation completed

## Responsive Behavior

The AI-assisted error explanation builds on the foundation of the dialog and its responsive behavior. For more on the responsive behavior of the AI-assisted error explanation dialog, see [Dialog](https://www.sap.com/design-system/fiori-design-web/ui-elements/dialog/#responsiveness).

---

## Navigation Menu

# Navigation Menu

## Intro

The navigation menu is always a click away and provides users with quick access from one work area to another. To optimize their navigation flows, users can personalize the menu with their most used spaces and their favorite S/4HANA Public Cloud apps.

**> **Information:** **

All references to “My Home” in this article relate to the [SAP S/4HANA product home page](https://www.sap.com/design-system/fiori-design-web/discover/sap-products/sap-s4hana-only/s4hana-product-home-page-my-home), which displays *My Home* on its interface.

*Navigation menu*

## When to Use

Do
Use the navigation menu:
- To give users direct access to all S/4HANA Cloud spaces
and apps
- To let users organize and access apps with favorites,
folder creation, and pinned spaces
## Anatomy

Anatomy of the navigation menu

All items below are mandatory and cannot be replaced:

1. **The hamburger toggle button:** Located in the shell bar and available from every space, it opens and closes the navigation menu.
2. **My Home:** Navigates to the SAP S/4HANA product home page.
3. **Favorite Apps section:** Users can add their favorite apps to this section and create folders in it for better organization. The *Add Apps* item navigates to the *App Finder*.
4. **My Spaces section:** Provides access to authorized spaces. Users can pin their favorite spaces in this section.
5. **All Spaces:** Opens *All Spaces* where users can pin specific spaces.

Adding favorite apps from the App Finder

Pinning and unpinning spaces from the All Spaces menu

## Behavior & Interaction

### Open/Close the Navigation Menu

Clicking the hamburger menu, alternately:

- Opens the navigation menu as a popover
- Closes the menu

Selecting a menu item or clicking outside the menu also closes the navigation menu.

### Expand/Collapse Menu Sections

Clicking a submenu indicator alternately expands and collapses the section.

### Navigation Interactions

- Right clicking an item opens the corresponding app or space in a new tab.
- Clicking a space item navigates to the space.
- Clicking a space submenu indicator expands the menu of subspaces.

*Right clicking an app or space shows the menu item for opening it in a new tab*

---

## S4Hana Product Home Page My Home

# My Home in SAP S/4HANA Cloud Public Edition

## Intro

My Home in SAP S/4HANA Cloud Public Edition is the entry point to **apps**, and offers access to:

1. **Tasks** and **situations**
2. **News** feed
3. **Pages**
4. Analytical **insights**
5. SAP **Business AI** recommendations

Additionally, its users benefit from enhanced personalization features for content and layout.

My Home in SAP S/4HANA Cloud Public Edition is based on launchpad [spaces](https://www.sap.com/design-system/fiori-design-web/foundations/integration-and-services/sap-fiori-launchpad/sap-fiori-launchpad-spaces) and runs best with the [Horizon theme](https://www.sap.com/design-system/fiori-design-web/foundations/visual/theming), although it supports other SAP and custom themes. A key user must activate My Home in SAP S/4HANA Cloud Public Edition.

## Components

Components in My Home in SAP S/4HANA Cloud Public Edition

My Home in SAP S/4HANA Cloud Public Edition is the leftmost option in the top-level [shell bar](https://main--builder-prospect--sapudex.hlx.page/design-system/fiori-design-web/ui-elements/shell-bar/) navigation and provides the following sections and content:

1. The salutation bar with specific actions
2. *[To Dos](https://www.sap.com/design-system/fiori-design-web/discover/sap-products/sap-s4hana-only/s4hana-product-home-page-my-home#to-dos)* for tasks and situations
3. *[News](https://sap.com/design-system/fiori-design-web/discover/sap-products/sap-s4hana-only/s4hana-product-home-page-my-home#news)* for user-relevant news and other updates
4. *[Pages](https://sap.com/design-system/fiori-design-web/discover/sap-products/sap-s4hana-only/s4hana-product-home-page-my-home#pages)* for a maximum of 8 pages displayed as tiles
5. *[Apps](https://sap.com/design-system/fiori-design-web/discover/sap-products/sap-s4hana-only/s4hana-product-home-page-my-home#apps)* for the user’s favorite apps, most used apps, recently used apps, and apps recommended by SAP Business AI
6. *[Insights Tiles](https://sap.com/design-system/fiori-design-web/discover/sap-products/sap-s4hana-only/s4hana-product-home-page-my-home#insights-tiles)* for tiles with analytical information
7. *[Insights Cards](https://sap.com/design-system/fiori-design-web/discover/sap-products/sap-s4hana-only/s4hana-product-home-page-my-home#insights-cards)* for cards from overview pages and list-report-based apps
8. A section menu shows actions for each section, including an action to open the *My Home Settings* dialog. From the dialog, users access personalization options for the section, and for the [layout for My Home](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/8a60279e8d2041b5ad8d3455fab0f3ef.html#layout-for-my-home) and the [visibility of its sections](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/8a60279e8d2041b5ad8d3455fab0f3ef.html#sections-in-the-my-home-in-sap-s/4hana-cloud-public-edition-entry-page).

For more information on user workflows for personalization, see the [My Home in SAP S/4HANA Cloud Public Edition](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/8a60279e8d2041b5ad8d3455fab0f3ef.html) documentation in the SAP Help Portal.

### To Dos

My Home - ‘To-Dos’ section

The *To Dos* section includes tabs for:

1. **Situations** from the My Situations app
2. **Tasks** from the Task Center

Each tab displays the tasks or situations as [cards.](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/overview-page-card/) They are arranged in a row according to their **priority**, from high to low.

> **Information:** The *To Dos* section is available only if the My Inbo&#x78;*,* Task Center, or My Situations app is assigned to the user. The
tabs shown in the section correspond to the assigned apps.

### News

My Home - ‘News’ section

A **carousel** lets users navigate through the news feed. Users can personalize their news feed in the Manage News app, available in the section menu.

> **Information:** The news feed is available only if a key user has activated it.

When users click an item in the carousel, a dialog opens to display the details.

My Home - news dialog

### Pages

My Home - ‘Pages’ section

The **Pages section** shows a **maximum of 8** favorite pages represented as tiles. Users define the pages to show or hide in the *Pages* tab of *My Home Settings.* See [Pages](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/80614a515a6e4bb1a4a18378c344a067.html).

> **Information:** A key user can assign custom colors and icons to the pages.

### Apps

My Home - ‘Apps’ section

The *Apps* section includes a **Favorites** **(1)** tab, with apps that the users have added from the ***Most Used*** **(2)**, ***Recently Used*** **(3)**, or ***Recommended*** **(4)** tabs.

**App groups (5)** are displayed as colored folders and contain the apps that the users add to them. See [Apps](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4fc8d03390c342da8a60f8ee387bca1a/f3fb03713b4748c69f7bc3ca708da97c.html).

> **Information:** Apps are shown on the *Most Used* and *Recently Used* tabs only if the user allows app tracking in the *My Home Settings* dialog:
- *Most Used* displays the apps used in the last 30 days, ordered from the most to least used.
- *Recently Used* displays up to 30 activities, ordered from most to least recently used.
Apps recommended by SAP Business AI are based on the user's business role. Users can hide the tab in the *My Home* *Settings* dialog.

### Insights

#### Insights Tiles

My Home - ‘Insights Tiles’ section

The *Insights Tiles* section contains [tiles](https://www.sap.com/design-system/fiori-design-web/ui-elements/tile/) with analytical information, such as charts or KPIs. All tiles are displayed in one row.

#### Insights Cards

My Home - ‘Insights Cards’ section

1. The *Insights Cards* section contains a **maximum of 10** [cards](https://www.sap.com/design-system/fiori-design-web/page-types/floorplans/overview-page-ovp/overview-page-card/)
2. An **overflow menu** for each card with card-specific actions

## Responsiveness

My Home in SAP S/4HANA Cloud Public Edition is responsive and can be used on tablets and phones.

---

