# SAP Fiori Foundations: Visual

## Colors Overview

**Design System Hero**

# Colors

## Intro

Color brings your screens to life. It communicates importance and association, letting users quickly identify key elements. When you use the theme’s color palette, you help create a clean, lightweight design that stays consistent and coherent across all SAP Fiori applications. Thoughtful use of color enhances visual hierarchy, usability, and accessibility. Colors also reinforce consistency and help users recognize status or visual feedback.

Familiarize yourself with the concepts of color balance and color usage, especially the interplay between primary colors, accent colors, grayscale areas, and semantic colors. For more information, see the colors for each theme:

- [Morning Horizon Colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/morning-horizon)
- [Evening Horizon Colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/evening-horizon)
- [Quartz Light Colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/quartz-light-colors)
- [Quartz Dark Colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/quartz-dark-colors)
- [Belize Colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/colors)

SAP Fiori offers a range of themes out of the box. Each theme meets accessibility standards of at least AA. For each theme, you’ll also find AAA-compliant high contrast options. For more information, see [Theming](https://www.sap.com/design-system/fiori-design-web/foundations/visual/theming).

## The DNA Reference Palette

The DNA reference palette contains nine different hues, each with eleven shades. Pure white and black are also included, covering the entire spectrum.

The colors for each theme are offered through a token hierarchy. This system keeps theming smooth and consistent across the user interface. The DNA reference palette forms the first and base level of this hierarchy – every other color palette is built from it.

Reference colors come from SAP company brand colors. These colors may vary between themes, and you shouldn’t use them directly in the CSS of user interface components. They are technology-agnostic and independent of specific use cases.

## UI Theme Reference Colors

The DNA color palette ensures coherence across SAP and throughout the customer journey. From this palette, we define a set of UI reference colors as the foundation for theming.

UI reference colors derived from the DNA color palette


Theme-specific colors are listed here: [Theming – Reference Colors (Horizon)](https://wiki.one.int.sap/wiki/pages/viewpage.action?pageId=2637292033)
Don’t apply these colors directly to user interface components. Instead, they are mapped to a stable set of parameters for styling the interface.
All colors used in user interface components are listed here: [Semantic Control Parameters (Horizon)](https://wiki.one.int.sap/wiki/pages/viewpage.action?pageId=2650676507)

## Color Contrast

The DNA palette is designed to support simple color contrast rules.

### Decorative Elements

The 7th shade is used against the 1st shade, or the 6th shade is used against white.

Color contrast rule for decorative elements

### Essential Elements

The 8th shade is used against the 1st or 2nd shade, or the 7th shade is used against white.

Color contrast rule for essential elements

### High Contrast

The 9th shade is used against the 1st shade, or the 9th shade is used against white.

Color contrast rule for high contrast


### Learn More
For more detailed best practices, check the full guideline and specification:
- [Theming – Reference Colors (Horizon)](https://wiki.one.int.sap/wiki/pages/viewpage.action?pageId=2637292033)
- [Semantic Control Parameters (Horizon)](https://wiki.one.int.sap/wiki/pages/viewpage.action?pageId=2650676507)

---

## Iconography > Iconography Horizon

# Iconography – Horizon

## Intro

The SAP icons for the Horizon visual themes feature a fresh, friendly, and bold aesthetic. They are designed for consistency in size, stroke, and balance. As a core element of the SAP visual product identity, these icons are optimized for simple and direct user interaction through intuitive, easy-to-understand metaphors.

Each icon is handcrafted and aligned across the various formats required by SAP Fiori applications. Composed of vector graphics, they offer seamless scalability, ensuring a crisp and professional appearance at any size.

*New SAP icon design for the Horizon visual themes*

## When to Use

Do
Use the icons to:
- Provide visual cues that help users navigate complex
interfaces quickly.
- Draw attention to primary actions.
- Save space in tight UI areas like toolbars or tables.
- Improve accessibility by adding a secondary layer of
meaning to color-coded information.

+-----------------------------------------------------------x------------------------------------------------------------+
Top Tips
+-----------------------------------------------------------x------------------------------------------------------------+
- **Accessibility:** Ensure that icons and visual elements are easy for everyone to understand, no matter which
reading direction they use.
- **Consistency:**  Keep icon meaning and visual integrity consistent between LTR and RTL layouts.
- **Localization:** Avoid culture-specific symbols, ensuring they are universally understandable and adaptable to
different languages, regions, and reading directions.
- **Icon metaphors**: Ideally represent a single, clear metaphor. If multiple metaphors are unavoidable, they must not
require different RTL handling. For example, combining a directional arrow with a logo creates conflicts, as arrows
must be flipped in RTL contexts while logos must not. Such combinations cannot be handled safely and increase
development complexity.
- **Icon sets:** If icons are part of a set, ensure as far as possible that similar icons are visually consistent with
each other across all variants and reading directions, so that each set feels cohesive and unified.

## Style

+-----------------------------------------------------------+>-----------------------<+
**Bold**: Strong presence that ensures clarity at small
and large sizes.
*Icon style – examples*
**Fresh**: Modern, clean, and free of unnecessary detail.
**Simple**: Reduced complexity for better readability and
faster recognition.
**Friendly**: Soft curves and approachable proportions.
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------x-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
Use the [Icon Creation Kit](https://www.figma.com/design/QHrbGNCBzNItkhkGLzzng6/Icon-Creation-Kit?node-id=0-1\&t=MrlzfoTBgtijUCtx-1), in combination with the [Icon Creation Guidance](https://wiki.one.int.sap/wiki/spaces/visualcore/pages/2599409981/Iconography\+%E2%80%93\+Icon\+Design\+Guideline\+Horizon), to ensure consistency and compliance when creating new icons.

## Format

We currently support two primary methods for implementing icons:

**SVG (scalable vector graphics)**: SVGs are handled as individual vector files. They offer high-definition rendering at any scale and offer advanced CSS styling options.
**Icon font**: An icon font treats icons as glyphs within a font file. This is a highly efficient way to manage large libraries and allows icons to be styled easily using standard text properties like font size and color.

Both formats are fully integrated into our environment, and you may choose based on the specific needs of your interface. While the system uses **SVG as the default format**, icon fonts are fully supported as well

## Sizing

### Default base size (16px)

The standard size for most general interface elements, such as buttons and input fields, is 16px. This size offers the ideal balance between visibility and spatial efficiency for standard desktop and mobile layouts.

### Small-scale and high-density (Up to12px)

For dense environments (e.g., data tables, checkboxes, or compact switches), smaller sizes are available.

- **Minimum**: We recommend 12px as the absolute minimum size for any icon.
- **Recommendation**: While the SVG library is scalable, avoid reducing icons beyond this point, as it may compromise stroke integrity and make the metaphor difficult to recognize.

### Large-scale and emphasis (Up to 48px)

Icons can be scaled up to create visual hierarchy or provide aesthetic emphasis.

- **Use cases**: Larger sizes are appropriate for avatars, generic tiles, or "highlight" areas.
- **Maximum**: For standard UI components, we recommend a cap of 48px. Beyond this size, icons may begin to feel visually "heavy" relative to the surrounding typography.

Icon scaling

## Grid System

To ensure every icon in the Horizon theme family feels like a cohesive part of the same DNA, we utilize a grid system. This system acts as a blueprint, balancing mathematical precision with visual harmony.

### Types of grids

We distinguish between two layers of alignment: the icon grid and the pixel grid.

- **Icon grid alignment:** Refers to the placement of elements relative to the internal key shapes and orthogonal lines. This ensures visual balance and consistent proportions across different metaphors.
- **Pixel grid alignment**: Refers to the alignment of paths to the actual physical pixels of the screen. This ensures that the icon remains crisp and avoids "anti-aliasing" (blurriness).

*Icon grid alignment (A) and pixel grid alignment (B)*

### Elements of the SAP icon system grid

The grid is a combination of four essential elements that construct one unified form:

1. **Pixel unit grid:** The foundational 1x1 coordinate system that ensures every point of the vector sits on a whole number.
2. **Orthogonal lines:** Vertical, horizontal, and 45° diagonal axes used to maintain structural integrity and consistent angles.
3. **Key shapes:** Standardized geometric templates (circles, squares, and rectangles) that provide a footprint for the icon's primary mass.
4. **Margins**: The "safe zone" around the edges of the 16x16px container that prevents the icon from touching the bounding box.

+----------------------------------------------------------x-----------------------------------------------------------+
+----------------------------------------------------------x-----------------------------------------------------------+
Generally, we try to snap every point perfectly to the pixel unit grid. When technical snapping noticeably harms the
visual result, we prioritize visual appearance over perfect technical alignment.

## Color

### Core color tokens

We categorize our icon colors based on their functional role within the interface:

**A: Interactive icons:** These tokens are used for actionable elements like buttons, navigation items, and clickable tools.

**B: Inverted icons:** Specifically designed for use within contrast statements or dark backgrounds. These tokens ensure the icon remains legible when placed on top of primary brand colors or dark UI surfaces.
**C: Non-interactive icons:** Applied to purely decorative icons that do not trigger an action. These typically have a lower visual weight to distinguish them from clickable elements.
**D: Marker icons:** Used for marker icons (such as the [object marker](https://www.sap.com/design-system/fiori-design-web/ui-elements/object-display-elements/#object-marker) icons).
**E: Rated/unrated content:** Specialized tokens for feedback systems, such as star ratings. These provide a clear visual distinction between active (filled/rated) and inactive (outlined/unrated) states.
**F: Semantic use cases (message and status):** These icons vary in color depending on the functional state of the message or object state (negative, critical, positive, information or neutral).

*Icon color examples*

## Accessibility

Icons must be usable by everyone.

Requirements

- Provide accessible names for all icon-only controls.
- Hide decorative icons from assistive tech.
- Accompany icons that convey meaning with text or labels.
- Ensure sufficient color contrast.

Never assume an icon’s meaning is universally understood.

For more information, see [Accessibility in SAP Fiori](https://www.sap.com/design-system/fiori-design-web/discover/sap-design-system/product-standards/accessibility-in-sap-fiori) and the [Accessibility Design Tools Handbook](https://www.sap.com/documents/2023/11/bc210d8b-977e-0010-bca6-c68f7e60039b.html).

---

## Iconography > Product Launch Icons

**Design System Hero**

# Product Launch Icons

## Intro

Product launch icons help communicate the purpose of the
SAP Business Suite experience, enabling users to
instantly identify products on the suite’s home page and
in the product switch.
Designed to complement the Horizon visual language, these
icons align with the SAP mobile product icons and app
icons to convey a unified brand identity. The balance
between individual icon metaphors, characteristic shapes,
and coherent visual design embraces the SAP design style.
## When to Use

Product launch icons are reserved exclusively for launching products within SAP Business Suite and must not be used for other purposes. They are used on the home page (SAP Start) and in the product switch in the [shell bar](https://www.sap.com/design-system/fiori-design-web/ui-elements/shell-bar/). Per SAP Brand guidelines, product launch icons may be permitted in board-level keynote presentations in exceptional circumstances. Each icon must always be accompanied by its corresponding text label.

## Appearance

Unlike logos, product launch icons are optimized for
clarity at small sizes and designed to work consistently
across the suite, ensuring intuitive navigation and a
cohesive user experience.
To maintain a recognizable identity across web and mobile
platforms, icons must retain core visual features and use
our standard design variables. This ensures the SVGs
automatically support all system themes, including
Horizon, Quartz, Belize, and High-Contrast modes.
## Current Collection

+:---------------------------------------x---------------------------------------:+:-----------------------------------------x------------------------------------------:+:-------------------------------------------x-------------------------------------------:+:--------------------------------------------x--------------------------------------------:+:---------------------------------------------x---------------------------------------------:+
Analytics Cloud                                                                 | Build                                                                                | Business Data Cloud                                                                     | Cloud ERP                                                                                 | Commerce Cloud

+:------------------------------------------x------------------------------------------:+:------------------------------------------x------------------------------------------:+:-----------------------------------------x-----------------------------------------:+:------------------------------------x-------------------------------------:+:--------------------------------------------x--------------------------------------------:+
Concur                                                                                | Customer Experience                                                                   | Datasphere                                                                          | Fieldglass                                                                 | Finance

+:-----------------------------------------------x-----------------------------------------------:+:----------------------------------------------x----------------------------------------------:+:-----------------------------------------x------------------------------------------:+:-------------------------------------------x-------------------------------------------:+:---------------------------------------x----------------------------------------:+
HANA Cloud                                                                                      | Industries                                                                                    | Integration Suite                                                                    | Procurement                                                                             | Sales Cloud

+:-------------------------------------------x--------------------------------------------:+:-------------------------------------------------------x-------------------------------------------------------:+:----------------------------------------x----------------------------------------:+:----------------------------------------x----------------------------------------:+:---------------------------------------------x---------------------------------------------:+
SAP Start                                                                                | Service Cloud                                                                                                   | Signavio                                                                          | SuccessFactors                                                                    | Supply Chain Management

+:----------------------------------------x-----------------------------------------:+:x:+:x:+:x:+:x:+
Sustainability                                                                     |   |   |
## Approach

For product launch icons, we use SAP Fiori icons as a foundation. The best way to start creating product launch icons is to choose an SAP Fiori icon that best represents your app metaphorically, then apply the style. While it's not required to use an icon as a base, product launch icons should follow the same style.

*Product launch icon metamorphosis*

## Anatomy

The product launch icon is composed of three layers,
representing the three-tier architecture.
1. Database layer
2. Logic layer
3. UI layer
The first level is the database layer, which is the base
shape of the app icon. The second layer represents the
logic layer. The UI layer is the third layer of the
product launch icon. For some icons, it is also possible
to use a highlight layer, if needed.
## Specification

*Background layer*
*Second layer*

## Product Icon Creation

To streamline icon creation for new products in SAP Business Suite, refer to the [Figma file](https://www.figma.com/design/03GEXkHM25FT4OwCkwhbCX/Product-Launch-Icons) featuring a usage guide and a product launch icon template with the color variables. To request a new product launch icon or to request access to an existing one, there will be a central request process.

---

## Iconography

**Design System Hero**

# Iconography

## SAP Icons

+---------------------------------------------------------------x----------------------------------------------------------------+
Tiles (plain)
+---------------------------------------------------------------x----------------------------------------------------------------+
[Iconography – Horizon](https://www.sap.com/design-system/fiori-design-web/foundations/visual/iconography/iconography-horizon)
SAP icons for the latest Horizon visual theme.
+---------------------------------------------------------------x----------------------------------------------------------------+
[Iconography – Quartz](https://www.sap.com/design-system/fiori-design-web/foundations/visual/iconography/icons)
SAP icons for the alternative Quartz visual theme.

**Metadata**

Title

Breadcrumbs

---

## Look Feel And Wording

# Visual Design Foundations - Overview

## Intro

Visual design plays a key role in how users perceive and recognize a product. Applying consistent styles reinforces brand identity and helps users feel confident as they interact with your application. Explore the sections below to get an overview of each visual design area and find links to detailed guidance:

- [Design Tokens](https://www.sap.com/design-system/fiori-design-web/foundations/visual/look-feel-and-wording#design-tokens)
- [Theming](https://www.sap.com/design-system/fiori-design-web/foundations/visual/look-feel-and-wording#theming)
- [Colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/look-feel-and-wording#colors)
- [Iconography](https://www.sap.com/design-system/fiori-design-web/foundations/visual/look-feel-and-wording#iconography)
- [Typography](https://www.sap.com/design-system/fiori-design-web/foundations/visual/look-feel-and-wording#typography)
- [UX Illustrations](https://www.sap.com/design-system/fiori-design-web/foundations/visual/look-feel-and-wording#ux-illustrations)
- [Shadows](https://www.sap.com/design-system/fiori-design-web/foundations/visual/look-feel-and-wording#shadows)

## Design Tokens                      |
*At the heart of SAP’s design system* |
SAP provides design tokens for colors, typography, shadows, and metrics in a central repository. These tokens connect directly to SAP themes used across all SAP technologies and platforms. Tokens replace hard-coded values with clear, meaningful names that are easy to map to UI components.

For more information, see [Design Tokens](https://www.sap.com/design-system/fiori-design-web/foundations/visual/design-tokens).

## Theming                     |
*One design, multiple flavors* |
SAP provides multiple application themes, all of which meet accessibility standards, including WCAG levels AA and AAA ([Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/)). The latest SAP theme is Horizon, available in a light mode (Morning Horizon) and a dark mode (Evening Horizon). We also offer dedicated high-contrast themes: High-Contrast Black (HCB) and High-Contrast White (HCW).

For more information, see [Theming](https://www.sap.com/design-system/fiori-design-web/foundations/visual/theming).

## Colors                 |
*The DNA of SAP’s themes* |
Color communicates importance and association, guiding users as they work. By applying the theme color palette, you create user interfaces that are clean, lightweight, and consistent across SAP Fiori applications. Make sure you understand the concepts of color balance and color usage, especially the interplay between primary colors, accent colors, grayscale areas, and semantic colors. For more information, explore the color palettes for each theme:

- [Morning Horizon Colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/morning-horizon) (latest theme)
- [Evening Horizon Colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/evening-horizon) (latest theme)
- [Quartz Light Colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/quartz-light-colors)
- [Quartz Dark Colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/quartz-dark-colors)
- [Belize Colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors/colors)

For more information, see [Colors](https://www.sap.com/design-system/fiori-design-web/foundations/visual/colors-overview).

## Iconography          |
*SAP’s icon font style* |

Learn about the icon styles for each theme family, including general icon semantics, the grid system, line thickness, and corner radius values.
If you need an app icon for your web app in a marketplace, check out the guidelines for creating service icons.
For key products in SAP Business Suite, use the predefined product icons.
- [Iconography – Horizon](https://www.sap.com/design-system/fiori-design-web/foundations/visual/iconography/iconography-horizon) (latest theme)
- [Iconography – Quartz](https://www.sap.com/design-system/fiori-design-web/foundations/visual/iconography/icons)
- [Service Icons](https://www.sap.com/design-system/fiori-design-web/foundations/visual/iconography/service-icons)
- [Product Launch Icons](https://www.sap.com/design-system/fiori-design-web/foundations/visual/iconography/product-launch-icons)

**Default (external_only)**

Learn about the icon styles for each theme family, including general icon semantics, the grid system, line thickness, and corner radius values.
- [Iconography – Horizon](https://www.sap.com/design-system/fiori-design-web/foundations/visual/iconography/iconography-horizon) (latest theme)
- [Iconography – Quartz](https://www.sap.com/design-system/fiori-design-web/foundations/visual/iconography/icons)

## Typography          |
*SAP’s corporate font* |
The “72” font family supports SAP’s visual language and has been crafted to convey trust, friendliness, and a modern look. Enhanced accessibility features also improve readability. “72” is optimized to render flawlessly on all supported devices and platforms. When “72” can’t be used, SAP applications automatically fall back to the next best available font.

For more information, see:

- [Typography – Horizon](https://www.sap.com/design-system/fiori-design-web/foundations/visual/typography/typography-horizon) (latest theme)
- [Typography – Quartz](https://www.sap.com/design-system/fiori-design-web/foundations/visual/typography/typography)

## UX Illustrations             |
*Consistent illustration style* |
UX illustrations simplify complex information, improve comprehension, and boost engagement through visual storytelling. When you use illustrations purposefully, you help create a human-centered experience and make interactions feel more approachable, relatable, and meaningful.

For more information, see [UX illustrations](https://www.sap.com/design-system/fiori-design-web/foundations/visual/ux-illustrations).

## Shadows            |
*Elevation and depth* |
The shadow concept uses a generic approach for depicting depth in applications. Multiple depth levels apply across all container controls, like tiles, menus, dialogs, and more. Each level uses a distinct shadow, making it easy to recognize one level from another and keep a consistent visual hierarchy. The concept also applies to interaction and text shadows, improving the overall user experience and readability.

For more information, see [Shadow Concept](https://www.sap.com/design-system/fiori-design-web/foundations/visual/shadow-concept).

---

## Shadow Concept

**Design System Hero**

# Shadow Concept

## Intro

The shadow concept offers a standard way to show depth in applications. It defines several depth levels that apply to all container components, such as tiles, menus, dialogs, and other elements. Each depth level uses a unique shadow, so you can easily distinguish one layer from another. This helps create a consistent visual hierarchy.

The shadow concept also covers interaction shadows and text shadows, which improve the user experience and make text easier to read. These shadows come with the component.

*The four content shadow levels in the Horizon theme*

## Content Shadow Levels

You’ll find examples for each shadow level below, shown in four different theming variants. These examples illustrate the visual layering hierarchy of container components in the UI.

### Content Shadow Level 0

The examples below show content **shadow level 0 on the overview page**.

+-------------x-------------+
**Carousel (full-width)**

(In order: Morning Horizon, Evening Horizon, High-Contrast Black, High-Contrast White)

### Content Shadow Levels 1 and 2

The examples below show a **combination of content shadow levels 1 and 2**.

Content shadow **level 1** is used by the following components:
- [Action sheet](https://wiki.one.int.sap/wiki/pages/viewpage.action?pageId=2030860737)
- [Floating footer](https://wiki.one.int.sap/wiki/pages/viewpage.action?pageId=2051281967)
- [Menu](https://wiki.one.int.sap/wiki/pages/viewpage.action?pageId=2061501144)

**Columns (external_only)**
Content shadow level 1 is used by the following
components:
- Action sheet
- Floating footer
- Menu

+-------------x-------------+
**Carousel (full-width)**

(In order: Morning Horizon, Evening Horizon, High-Contrast Black, High-Contrast White)

### Content Shadow Level 3


The example below shows the **level 3 shadow styling for a [dialog](https://wiki.one.int.sap/wiki/pages/viewpage.action?pageId=2033847432)**.

**Default (external_only)**

The example below shows the **level 3 shadow styling for a dialog**.

+-------------x-------------+
**Carousel (full-width)**

(In order: Morning Horizon, Evening Horizon, High-Contrast Black, High-Contrast White)


### Learn More
For more detailed best practices, check the full [shadow concept specification](https://wiki.one.int.sap/wiki/pages/viewpage.action?pageId=2697902969).

---

## Typography > Typography Horizon

# Typography – Horizon

## Intro

SAP applications use SAP’s proprietary typeface **72**, with a fallback to sans-serif system fonts if 72 can’t be loaded.

Designing 72 from the ground up made it possible to meet SAP Fiori’s typographic requirements, including:

- **Legibility enhancements:** Optimize for screen use.
- **Font styles:** Support a robust typographic hierarchy.
- **Brand voice:** Be credible and humane.
- **Character set:** Accommodate complex content.
- **Language support:** Support Windows Glyph List.
- **Accessibility:** Improve character recognition.

## Typography with 72

“**72**” replaces the default system fonts to improve the typographic system for SAP applications. The design has been meticulously crafted to portray a look and feel that is more trustworthy, friendly and modern, communicating the visual language of SAP. The metrics have been optimized to ensure compatibility with the corresponding fallback fonts such as Arial. Improvements of the individual characters have been made to enhance legibility and ensure better accessibility recognition. With all these enhancements, along with the humanist influences within the fine details, 72 greatly improves the legibility of SAP applications.

*72, a bespoke typeface created for SAP*

## Language Support and Fallback to System Fonts

Language coverage is one of the most important requirements of a typeface, depending on the number of countries in which your applications need to be available. Beyond the languages the font supports, fallback solutions need to be considered. If the defined fonts cannot be displayed when an application initially loads, fallback fonts are defined in the style sheet. Defining a fallback to sans-serif system fonts that are readily available on every user’s device is a simple solution for loading applications in any language. The font stack that is used within the CSS includes 72 with a fallback to system fonts such as Arial and Helvetica in combination, or Roboto for Android.

Here is an example of how theme parameters are used to specify font stacks. Notice that there are two versions of the 72 font; the first is a smaller subset to help improve performance and the second is the full version:

**sapFontFamily**: “72”, “72full”, Arial, Helvetica, sans-serif;

The fallback system fonts also have the advantage of zero loading time, ensuring that there is always a consistent font available that works with the fresh, clean, and minimalist SAP visual style. The font stacks used come with a full Unicode solution when special characters are needed. System fonts are available for all the languages that SAP products need to support. 72 is integrated into the control set, making customization easy. The font stacks can also be modified to achieve a custom result.

## Accessibility

Optimized for screen consumption, 72’s design enhancements increase legibility, readability and ultimately, accessibility. A wider apex and open counters help with character recognition at smaller sizes. Differentiation of character details, such as the number “1” and the lower case “l” versus the capital “I”, makes the characters easier to distinguish and improves the overall reading experience.

*Example of improved accessibility features*

## Headlines and Font Styles for UI Controls

- **Headlines 1 to 6:** Titles are defined in several sizes and styles that help to visually identify the context of application pages or grouped content within the user interface. Examples of headlines include the page title, object header title, list, form, table, chart, timeline, and feed titles. Headlines generally use the 72 Bold font weight by default and 72 Black for the key titles in the Horizon theme, but this is flexible depending on the control component or product application context.
- **Small text**: Used for exceptional use cases within controls, such as time stamps or a unit of measurement. We do not recommend using small text size as the main UI text size within controls.
- **Medium text:** Default text size used in controls, such as buttons, inputs, tables, or a tree.
- **Large text**: Stand-out text controls, such as titles within standard list items.
- **Key performance indicators or custom display sizes:** KPI numbers or custom display text sizes may have individually-specified sizes and font weights depending on the control component or application context. Consider visual accessibility and the typographic hierarchy before choosing any custom size or font weight. Light font weights are recommended only for large sizes that are clearly visible and should never be used for small textual information or labeling. If a UI is specially designed to be visible on very large displays from far away, consider emphasizing key information using a bold font weight.

These recommended sizes and weights are offered by default. However, SAP product lines have the flexibility to define their own type scale.

### Header Scale

<https://www.sap.com/design-system/live-examples/_Foundations/Typography/Typography_SE_HeaderScale.html>

### UI Control Text Sizes

<https://www.sap.com/design-system/live-examples/_Foundations/Typography/Typography_SE_TextSizes.html>

## 72 Font Styles

### Additional Styles
SAP can now benefit from the additional font styles that
have been added to 72, such as 72 Semibold Duplex. These
font styles help to expand the possibilities of how to
best visualize the information hierarchy within products
and websites.
### 72 Semibold Duplex
72 Semibold Duplex also enables additional accessibility
improvements by providing a visual weight distinction to
the regular font weight without any visual jump in the
width of the letters. This helps bring more interactive
affordance to the text used for general actions and also
helps bring a more consistent weight when paired with the
new stronger weight of the icon style for the Horizon
theme.
## Line Heights

In general, **no line height is applied to text,** since the line height affects the padding and leads to misaligned content.
If a more generous line height is required for long continuous text, a consistent line height of 1.5 is recommended:

- **Normal line height**: This is the default auto line height used in bread and butter controls (such as buttons, inputs, lists, and tables with no wrapping text).
- **1.5 line-height**: Line height recommended by WCAG accessibility guidelines for long continuous or wrapped text (for example, text area or feed list item).

---

## Typography Overview

**Design System Hero**

# Typography

SAP applications use SAP’s proprietary typeface 72, with a fallback to a sans-serif system font if 72 can’t be loaded.

+--------------------------------------------------------------x--------------------------------------------------------------+
Tiles (plain)
+--------------------------------------------------------------x--------------------------------------------------------------+
[Typography – Horizon](https://www.sap.com/design-system/fiori-design-web/foundations/visual/typography/typography-horizon)
Typographic system with the Horizon visual theme.
+--------------------------------------------------------------x--------------------------------------------------------------+
[Typography – Quartz](https://www.sap.com/design-system/fiori-design-web/foundations/visual/typography/typography)
Typographic system with the Quartz visual theme.

**Metadata**

Title

Breadcrumbs

---

