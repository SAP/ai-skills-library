# SAP Fiori Foundations: Best Practices

## Ui Elements > Title Hierarchy Guidance

# Title Hierarchy Guidance

## Intro

When designing and building web apps, organizing and managing headings is very important. A clear and consistent heading hierarchy, expressed visually through title styles and structurally through semantic heading levels, helps users scan and understand pages quickly while also supporting efficient navigation for assistive technologies. By establishing clear guidelines for using title styles alongside appropriate semantic heading levels, teams can create layouts that are intuitive, adaptable to different interactions and states, and easy to navigate.

These guidelines focus on content structure and heading hierarchy, not on implementation specifics. They cover the visual use of title styles and the semantic heading levels that determine how titles are announced by screen readers.

This illustrates the hierarchical arrangement of heading levels and the styling of titles on the object page as an example.

## Usage

Do
Consider the following best practices for usage:
- **Assign semantic tags.** Use semantic tags based on
the content’s importance and structure.
- **Adapt visual styles.** Allow visual styling to change
based on branding and design needs while maintaining
semantic integrity, making sure the app remains
accessible.
- **Follow accessibility guidelines.** Use ARIA levels
consistently to help screen readers understand the
hierarchy of content.
- **Use heading sizes appropriately.** Align heading size
choices with their defined usage purposes (for example,
use Header 6 for small, nested group headers).
- **Sequential order.** Follow sequential heading orders
without skipping levels to ensure content structure
remains clear.
levels match the semantic HTML tags used, without causing
confusion for screen readers.

## Layout and Structure – General Guidance

This outlines the structure of the components, specifying areas, sections with typography, iconography in context, and other details.

## Ensuring Logical Flow

- **Hierarchy update:** When you add more content, adjust the headings to maintain a clear order, ensuring that the visible headings reflect the importance of the content.

* **Consistency in updates:** Ensure that changes align with the original heading order and integrate smoothly into the user's experience.

## Visual Style and Semantic Hierarchy

It's important to understand the difference between the visual appearance of titles and their role in organizing content. Tags help establish content order for accessibility and screen readers, while titles can be styled differently to fit branding and design preferences. Separating these aspects allows developers to use tags based on content importance, while design adapts to achieve their goals. This ensures that apps remain easy to use and visually appealing, following good design principles while maintaining flexibility.

Additional Examples:

- Custom Object Page:

- Flexible Column Layout:

- Dialog in Combination with Panel:

---

## Ui Elements

**Design System Hero**

# Best Practices – UI Elements

## Formatting

+----------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------+
Tiles (plain)
+----------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------+
[Formatting Data – Overview](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/formatting/formatting-data-overview)
Use locale‑ready formatting rules for times, dates, numbers, measurements, and comma‑separated lists.
+----------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------+
[Formatting Dates](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/formatting/formatting-dates)
Use SAPUI5 to format dates consistently across locales.
+----------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------+
[Formatting Numbers](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/formatting/formatting-numbers)
Format numbers according to international rules using SAPUI5.
+----------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------+
[Formatting Time](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/formatting/formatting-time)
Format times correctly across locales using SAPUI5.
+----------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------+
[Units of Measurement](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/formatting/units-of-measurement)
Use standard unit rules for abbreviations, spacing, and pluralization.
+----------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------+
[Removing Leading and Trailing White Space](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/formatting/leading-trailing-blank-removal)
Trim blanks when copying and pasting text into input controls.

## Component Usage

+---------------------------------------------------------------------------------x---------------------------------------------------------------------------------+
Tiles (plain)
+---------------------------------------------------------------------------------x---------------------------------------------------------------------------------+
[Busy States](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/busy-handling)
Signal work in progress while reducing interruptions.
+---------------------------------------------------------------------------------x---------------------------------------------------------------------------------+
[Collaboration](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/collaboration)
Add SAP Jam tiles, share menu actions, and social feeds to your app.
+---------------------------------------------------------------------------------x---------------------------------------------------------------------------------+
[Table Overview](https://www.sap.com/design-system/fiori-design-web/v1-136/foundations/best-practices/ui-elements/tables/table-overview)
Choose the right table for your use case scenario.
+---------------------------------------------------------------------------------x---------------------------------------------------------------------------------+
[Table Personalization Overview](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/tables/overview-table-personalization)
Choose the right personalization pattern to adjust columns, sorting, grouping, and filters.
+---------------------------------------------------------------------------------x---------------------------------------------------------------------------------+
[Title Hierarchy](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/title-hierarchy-guidance)
Create clear and accessible heading hierarchies using title styles and semantic heading levels.
+---------------------------------------------------------------------------------x---------------------------------------------------------------------------------+
[UI Element States](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/ui-element-states)
Use appropriate state combinations to signal options and highlight where attention is needed.
+---------------------------------------------------------------------------------x---------------------------------------------------------------------------------+
[Using Semantic and Industry Colors](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/how-to-use-semantic-colors)
Apply semantic colors for universal value states and industry colors for domain-specific contexts.
+---------------------------------------------------------------------------------x---------------------------------------------------------------------------------+
[Using Tooltips](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/using-tooltips)
Learn how to use tooltips for unlabeled elements.
+---------------------------------------------------------------------------------x---------------------------------------------------------------------------------+
[Which Selection Control Should I Use?](https://www.sap.com/design-system/fiori-design-web/foundations/best-practices/ui-elements/which-selection-control-to-use)
Choose the best selection control for your use case.

**Metadata**

Title

Breadcrumbs
Elements

---

