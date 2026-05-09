# SAP Fiori UI Elements: Display

This reference covers the following UI components:

- [Avatar](#avatar)
- [Avatar Group](#avatar-group)
- [Avatar Group Web Component](#avatar-group-web-component)
- [Avatar Web Component](#avatar-web-component)

---

## avatar

+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
Message Strip (information)
+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
This guideline now covers both SAPUI5 and SAP Web Components. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).

## Intro

Avatars are visual representations of users, products, or business entities, helping people quickly identify them within an application. Users can be shown with their own photos or initials, while products can be depicted with representative images or logos.

Examples of a user image, user initials, and standard user placeholder icon

### Component availability

This component is available in the following libraries:

+-----------x------------+-------------------------------------------------------------x-------------------------------------------------------------+----------------x-----------------+
Library                | Technical Name                                                                                                            | Identifier
+-----------x------------+---------------------------------------------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit        | [sap.m.Avatar](https://ui5.sap.com/#/entity/sap.m.Avatar)                                                                 | :badge, info, large, _, SAPUI5:
+-----------x------------+-------------------------------------------------------------x-------------------------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components     | [ui5-avatar](https://ui5.github.io/webcomponents/components/Avatar/)                                                      | Components:
+-----------x------------+-------------------------------------------------------------x-------------------------------------------------------------+----------------x-----------------+
SAP Web UI Kit (Figma) | [Avatar](https://www.figma.com/design/SILcWzK5uFghKun9jx6D7c/SAP-Web-UI-Kit?m=auto\&node-id=2-1354\&t=F9pseQ9DaDQ8KiI1-1) | :badge, info, large, _, Figma:

**Table (external_only)**
+----------------x-----------------+----------------------------------------------x----------------------------------------------+----------------x-----------------+
Library                          | Technical Name                                                                              | Identifier
+----------------x-----------------+---------------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit                  | [sap.m.Avatar](https://ui5.sap.com/#/entity/sap.m.Avatar)                                   | :badge, info, large, _, SAPUI5:
+----------------x-----------------+----------------------------------------------x----------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components               | [ui5-avatar](https://ui5.github.io/webcomponents/components/Avatar/)                        | Components:
+----------------x-----------------+----------------------------------------------x----------------------------------------------+----------------x-----------------+
SAP Fiori for Web UI Kit (Figma) | [Avatar](https://www.figma.com/community/file/1494295794601744471/sap-fiori-for-web-ui-kit) | :badge, info, large, _, Figma:

## When to Use

+------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------+
When To Use
+------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------+
Do
Use the avatar to:
- Display user photos, initials, or placeholders for personal identification.
- Show standardized images for business content such as products, parts, logos, or campaign visuals.
- Represent concepts or entities with icons when images aren’t available.
- Present images with transparent backgrounds when needed for clarity or design fit.
- Provide placeholder images when no other source image is available.
- Apply avatars consistently in places like lists, cards, and headers to create familiarity and a uniform visual pattern across the interface.
+------------------------------------------------------------------------------------------x------------------------------------------------------------------------------------------+
Don't
Don’t use the avatar to:
- Display pictures in a sequence, such as a slideshow or carousel. Instead, use the [carousel](https://www.sap.com/design-system/fiori-design-web/ui-elements/carousel/) component.
- Display an interactive icon. Instead, use the [button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/) with an icon inside.

+-----------------------------------------------------------------------------------x-----------------------------------------------------------------------------------+
Top Tips
+-----------------------------------------------------------------------------------x-----------------------------------------------------------------------------------+
- Use a circle for people and a square for product or business-related images.
- Use the predefined sizes. If you need a custom size, follow [these guidelines](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar/#custom-size).
- For product icons, replace the default icon with a more suitable icon for your use case.
- Provide a clear alternative text for the avatar image.
- For interactive avatars and badges, provide both a tooltip and an alternative text.
- Avoid unnecessarily large files.
- Avoid badges on avatars smaller than size S.
- Don’t attach actions to icons in the avatar.

## Anatomy

1. **Avatar:** Main avatar component with different display options. See [Types](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar/#types).
2. **Border (optional):** An avatar can have a very subtle border.
3. **Badge (optional):** Displays a visual indication of the action triggered when clicking the avatar.

## Types

### Content types

Avatars represent people, products, or business objects, and can display a photo, initials, or a placeholder icon.

**A:** User photo or business image
**B:** User’s initials
**C:** Placeholder icon

Avatar types

#### Images

Use images for avatars when representing people or business content. Avatars can display either user or business images.

The avatar component can be configured in various shapes. For more information on the shape types and their usage, see the [Shape Types](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar/#shape-types) section.

Optimize high-resolution images to avoid unnecessarily large files. Large image files can severely impede page performance.

The examples below show square avatars for business content.

*Examples of business images*

#### Initials

The initials stand for the first and last name of a person – for example, JD for Jane Doe, or MvV for Marjolein van Veen. The order of the initials depends on the language – for example, first name before last name in English.

Initials can have up to three alphabetical characters (A-Z, a-z). If more than 3 initials are required for longer names (such as Anna María Agustí Suárez), the gender-neutral placeholder icon is displayed instead. The placeholder is also used if the three letters don’t fit into the circle (for example, WWW).

User initials with 1, 2, and 3 characters

#### Placeholder icons

Placeholder icons are used for both user and business images when no other image is available:

- The default placeholder for a **user** is a gender-neutral person icon inside a circle.
- The default placeholder for **other images** is a neutral product icon inside a square.

Default person and product placeholders

You can specify your own default placeholder icon for business images. Always replace the default product icon if there is a more suitable icon for your use case and industry.

Product placeholders with custom icons

#### Background color

The background color is set to blue by default. However, to add more visual variety to the UI, you can change the background color using one of the following options:

- **Avatar colors:** You can specify one of 10 different avatar colors as the placeholder background color.
- **Random color:** The component automatically picks a random color from the avatar color palette.

All avatar colors can be [themed](https://www.sap.com/design-system/fiori-design-web/foundations/visual/theming).

User initials in all 10 accent colors

For images in the **content area**, use the background color “placeholder” to keep the primary focus on the text. This approach ensures that image content plays a secondary role.

Image and placeholder icon with background color “placeholder”

You can use **images with transparent backgrounds** to display descriptive illustrations and visuals.

Images with transparent backgrounds

You can use the avatar component to display **icons** as non-interactive elements. To do this, apply the background color “placeholder”.

Don’t use icons as images. Icons are usually part of an [icon font](https://www.sap.com/design-system/fiori-design-web/foundations/visual/iconography/icons#sap-icon-font).

Don’t apply actions to icons. If you want to place an action on the icon, use the [button](https://www.sap.com/design-system/fiori-design-web/ui-elements/button/) with an icon inside instead.

Icon examples with background color “placeholder”

### Interaction types

From an interaction standpoint, an avatar can be one of two types:

- **Interactive:** Focusable and pressable. Interactive avatars can display a badge.
- **Non-interactive:** Not focusable and not pressable.

Users can press or click an interactive avatar to trigger an action.

Interactive avatar (A) and non-interactive avatar (B)

If the avatar is interactive, you can display a badge with an icon. The badge signals that the avatar is interactive, and the icon indicates the action that will be triggered. This is especially useful for images.

Avoid badges on avatars smaller than size S to preserve visibility. Always include a tooltip that describes the action.

Avatars with badges for zoom in (left), edit (center), and change picture (right)

### Shape types

The avatar component can be configured to display in various shape types, including circular or square, to best represent different types of entities.

Use a circle for people and a square for product or business-related images. Circles emphasize individuality and work best for people, while squares convey structure and are better suited for products, companies, or other business objects. This distinction helps users quickly recognize whether content represents a person or a business.

In general, the avatar component is typically used in a circular or square shape. Custom shapes can be defined using CSS classes.

Avatar shapes

### Size types

#### Predefined sizes

The avatar component is available in a set of predefined sizes to ensure a consistent appearance across the user interface.

Predefined sizes: XS, S, M, L, XL

The table below outlines when to use each avatar size.

**Table (col-width-20-80)**

Size

**XS**

**S**

**M**

**L**

**XL**

#### Custom sizes

If your use case requires it, you can also set a custom size.

When using a custom avatar size with initials or icons:

- Ensure that the font size is consistent with the size of the component itself.
- If your custom size is between two predefined sizes, use the font size corresponding to the smaller predefined size.

Example: If your avatar is 5.5 rem (between sizes L and XL), use the font size for size L (2 rem).

### Scale types

You can specify how the original image fits into the avatar:

- **Cover** **(default)** – The size of the image is scaled up to completely cover the avatar area. As a result, parts of the image may be outside the avatar shape. Use the “cover” fit type if the focal point is in the center of the image.
- **Contain** – The image is scaled down to fit into the component area. The entire image is displayed, but it might not completely fill the shape. In this case, the avatar displays a default background color. The image itself is always centered inside the shape. Use the “contain” fit type for images that need to be displayed in full.

Avatar scale types: cover scale type (A) and contain scale type (B)

## States

### Component states

The avatar component supports three component states: enabled, disabled, and hidde&#x6E;*.*

Avatar component states: enabled (A) and disabled (B)

For more information, see [Component States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-component-states).

### Interaction states

The avatar component supports four interaction states: regular, hover, down, and down-hover.

**A: Regular**
**B: Hover**
**C: Down:** This state is sometimes described as an “active” or “active/toggled” state.
**D: Down-Hover:** A combination of the down and hover states.

Avatar interaction states

For more information, see [Interaction States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-interaction-states).

:badge, info, large, _, SAPUI5 only:

The SAPUI5 avatar component also supports an active/toggled state, which inherits the styling of the standard button. The active/toggled state changes the visual appearance of the avatar even if the focus is changed to another component.

Avatar active/toggled state

### Value states

Badges on avatars can display value states to indicate status. Each state uses a distinct color and icon to help users quickly understand the context:

**A: Negative:** Indicates an error or issue that requires attention or resolution.
**B: Critical:** Signals a warning or something that needs caution or a follow-up action.
**C:** **Positive:** Shows success or confirmation that an action has been completed.
**D:** **Information:** Provides neutral information or context without implying an issue.
**E:** **None:** No value state is shown. When the avatar has no image, the badge can display a camera icon to prompt the user to change a picture.

Badge value states

For more information, see [Value States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-value-states).

## Behavior and Interaction

### Focus

After a user clicks an interactive avatar, it receives focus. The pressed state is active while the mouse button is down.

Avatar mouse interaction – hover, press or click

### Fallback icon

You can set a fallback icon to appear when the avatar can’t display its intended content. This icon shows up automatically in cases where the image source is incorrect or unavailable, or when the avatar is too small to display the initials properly.

Fallback icon with product icon (A), person icon (B), and custom fallback icon (C)

### Tooltip :badge, info, large, _, SAPUI5 only:

When adding a badge to the avatar component, always pair it with a tooltip that explains the action. This ensures users understand its purpose and avoids any confusion.

The badge’s tooltip is displayed when the user hovers the mouse pointer over the badge.

When using interactive avatars, always include both a tooltip and an alternative text to [support screen reader users](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar/#screen-reader-support).

Interactive avatar with a tooltip

## Responsiveness

The avatar adapts to different layouts using five predefined sizes optimized for each device type.

Use the predefined sizes to match the surrounding layout density – from compact table items to spacious app headers – ensuring a consistent visual rhythm across your application.

For a full overview of available sizes and their recommended use cases, see [Size Types](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar/#size-types).

## Accessibility

SAP follows international standards, such as WCAG and WAI-ARIA, and strives to make our business solutions accessible and inclusive.

For more information, see [Accessibility in SAP Fiori](https://www.sap.com/design-system/fiori-design-web/discover/sap-design-system/product-standards/accessibility-in-sap-fiori) and the [Accessibility Design Tools Handbook](https://www.sap.com/documents/2023/11/bc210d8b-977e-0010-bca6-c68f7e60039b.html).

### Keyboard navigation

The following keyboard combinations are supported by the SAPUI5 Avatar component.

**Table (col-width-30-70)**

Key Combination

**Tab**
focused.

**Shift \+ Tab**

**Enter/ Return** or **Spacebar** or screen tap gesture

**Shift \+ F10**
focused element.

### Screen reader support

Provide concise alt text that describes what the **avatar** represents.

Add clear alternative text to every **avatar image** so it’s announced by screen readers and shown when the image isn’t available or can’t be displayed.

When the avatar is just used for decorative purpose (e.g avatar username is displayed in text beside the avatar), the aria role for the avatar should be ‘presentation’ so that it’s ignored by accessibility tools to avoid repetitive information for screen reader user.

For an **interactive avatar or badge**, provide a tooltip and an alternative text to indicate the available action.

For details on screen reader support and Accessible Rich Internet Applications (ARIA), see [UI5 Screen Reader Support](https://ui5.sap.com/#/topic/33fae3482358438e93daea5232527093) and [WAI-ARIA Authoring](https://www.w3.org/TR/wai-aria-1.2/).

## Content

### Localization

#### Initials

Some languages don’t build on an alphabet, or don’t use initials at all. In such cases, the gender-neutral person icon is displayed instead.

#### Reading direction

For right-to-left languages, such as Arabic or Hebrew, the position of the avatar badge is mirrored. This way, badge placement aligns naturally with the reading direction.

Left-to-right avatar badges

## Framework Comparison

Some behaviors differ between frameworks due to implementation specifics. The table below summarizes the differences between SAPUI5 and SAP Web Components and lists the framework-specific patterns.

**Table (col-width-50-20-30)**
+--------------------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------------------+-------x-------+---------x----------+
Feature                                                                                                                                                                                                                                                                     | SAPUI5        | SAP Web Components
+--------------------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------------------+---------------+---------x----------+
The avatar’s **active/toggled** state adopts the standard button styling and remains visible even when it loses focus. For more information, see the [Interaction Types](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar/#interaction-types) section. | Available     | Not Available
+--------------------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------------------+---------------+---------x----------+
**Tooltip** explanations for avatar badges clarify the badge’s action and reduce user confusion. For more information, see the [Tooltip](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar/#tooltip) section.                                           | Available     | In Progress

**\**

---

## avatar-group

+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
Message Strip (information)
+---------------------------------------------------------------------------------------------------------------x---------------------------------------------------------------------------------------------------------------+
This guideline now covers both SAPUI5 and SAP Web Components. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).

## Intro

The avatar group is a visual element that displays several [avatars](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar/) together, indicating that more than one person or business entity is associated with an item. It’s typically used to represent a group of people who belong together – for example, members of a project team or department.

*Avatar group*

### Component availability

The avatar group component is available in the following libraries:

+-----------x------------+--------------------------------------------------------------x---------------------------------------------------------------+----------------x-----------------+
Library                | Technical Name                                                                                                               | Identifier
+-----------x------------+------------------------------------------------------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit        | [sap.f.AvatarGroup](https://ui5.sap.com/#/entity/sap.f.AvatarGroup)                                                          | :badge, info, large, _, SAPUI5:
+-----------x------------+--------------------------------------------------------------x---------------------------------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components     | [ui5-avatar-group](https://ui5.github.io/webcomponents/components/AvatarGroup/)                                              | Components:
+-----------x------------+--------------------------------------------------------------x---------------------------------------------------------------+----------------x-----------------+
SAP Web UI Kit (Figma) | [Avatar Group](https://www.figma.com/design/SILcWzK5uFghKun9jx6D7c/SAP-Web-UI-Kit?node-id=99561-12600\&t=6sUenuuJ9nsczZBi-4) | :badge, info, large, _, Figma:

**Table (external_only)**
+----------------x-----------------+----------------------------------------x----------------------------------------+----------------x-----------------+
Library                          | Technical Name                                                                  | Identifier
+----------------x-----------------+---------------------------------------------------------------------------------+----------------x-----------------+
SAPUI5 Demo Kit                  | [sap.f.AvatarGroup](https://ui5.sap.com/#/entity/sap.f.AvatarGroup)             | :badge, info, large, _, SAPUI5:
+----------------x-----------------+----------------------------------------x----------------------------------------+----------------x-----------------+
| :badge, info, large, _, SAP Web
SAP Web Components               | [ui5-avatar-group](https://ui5.github.io/webcomponents/components/AvatarGroup/) | Components:
+----------------x-----------------+----------------------------------------x----------------------------------------+----------------x-----------------+
SAP Fiori for Web UI Kit (Figma) | [Avatar Group](https://www.figma.com/community/file/1494295794601744471)        | :badge, info, large, _, Figma:

## When to Use

+----------------------------------------------------------------------x----------------------------------------------------------------------+
When To Use
+----------------------------------------------------------------------x----------------------------------------------------------------------+
Do
Use the avatar group to:
- Display a group of at least two people.
- Display several people who share something in common, such as a project or a team.
+----------------------------------------------------------------------x----------------------------------------------------------------------+
Don't
Don’t use the avatar group to:
- Display a gallery of simple images. Use the [carousel](https://www.sap.com/design-system/fiori-design-web/ui-elements/carousel/) instead.
- Display a single [avatar](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar/).
- Show visual content other than avatars.
- Show unrelated media or content types.

+------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------+
Top Tips
+------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------+
- Always display avatar groups horizontally.
- Use the [group](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar-group/#group-type--focus-on-the-sum-of-people) type when it’s more important to show the avatar group as a whole.
- Use the [individual](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar-group/#individual-type--focus-on-each-person) type when users need to focus on each person in the avatar group.
- Use the avatar group to display at least two avatars.
- Use size S by default for most layouts. Use sizes M or L only when avatars are key to the page.

## Anatomy

The avatar group component consists of the following elements:
1. **Avatar group:** Container that displays multiple avatars side by side.
2. **Overflow button:** Button that appears automatically if there isn’t
enough space to show all avatars.
3. **Avatar:** Visual representation of a person, shown as an image, initials, or icon.
## Types

### Display types

The avatar group offers two display types: [Group](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar-group/#group-type--focus-on-the-sum-of-people) and [Individual](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar-group/#individual-type--focus-on-each-person).

In both cases, the order of the avatars can be defined flexibly – for example, alphabetical, history-based, or random.

Avatar groups support multiple variants, including avatars that show images, initials, or icons. These elements can also be combined in different ways to suit your needs.

**Note:** The avatar group reuses the avatar component and its logic. If a person’s image is not available, the person’s initials are displayed. If there are more than three initials or the language system doesn’t support initials, the avatar displays a gender-neutral person icon.

#### Group type – focus on the sum of people

Use the group type when it’s more important to show the group as a whole. This type displays avatars with partial overlap to save space. It’s commonly used in cards, org charts, or when representing large groups (100+ people).

This is the **default** type.

*Group type*

#### Individual type – focus on each person

Use the individual type when users need to focus on each person in the group. Avatars are shown side by side without overlapping. This type works well for smaller groups like project teams or department members, where users may want to view details about individuals (for example, via a business card).

*Individual type*

**> **Guideline:** **

- Always provide a clear [<u>label</u>](https://www.sap.com/design-system/fiori-design-web/ui-elements/label/) or description for either type of avatar group.
- Always display avatar groups horizontally.
- The avatar group must contain at least two avatars.
- Once you’ve decided on the avatar order that best fits your use case (for example, alphabetical), use it consistently within your app.

### Size types

The avatar group supports the different sizes of the [avatar](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar/) component.

**A:** Size XS
**B:** Size S
**C:** Size M
**D:** Size L
**E:** Size XL

*Avatar group sizes*

### Scale types

You can specify how the original image fits into every avatar in the group:

- **Cover** (default): The size of the image is scaled up to completely cover the avatar area. As a result, parts of the image may be outside the avatar shape. Use the “cover” fit type if the focal point is in the center of the image.
- **Contain**: The image is scaled down to fit into the component area. The entire image is displayed but might not fully fill the shape. In this case, the avatar displays a default background color. The image itself is always centered inside the shape. Use the “contain” fit type for images that need to be displayed in full.

Scale types “cover” (left) and “contain” (right)

## States

### Component states

The avatar group component supports the following component states: enabled, disabled, and hidden.

*Avatar group component states: enabled (top), disabled (bottom)*

For more information, see [Component States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-component-states).

### Interaction states

The avatar group component supports the following interaction states: regular, hover and down.

*“Regular” interaction state for avatar group (group and individual type)*

*“Hover” interaction state for avatar group (group and individual type)*

*“Down” interaction state for avatar group (group and individual type)*

For more information, see [Interaction States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-interaction-states).


Currently, some interaction states are not showing correctly in the SAPUI5 and SAP Web Component implementations.
This is being addressed.
This guideline describes the correct design.

### Focus state

Clicking an avatar group (**type: group**) or selecting it via keyboard activates its focus state, visualized with a solid line around the avatar group.

*Focused (left) and unfocused (right) avatar group (type: group)*

Clicking an individual avatar within avatar group (**type: individual**) or selecting it via keyboard activates its focus state, visualized with a solid line surrounding the individual avatar.

*Focused (left) and unfocused (right) avatar group (type: individual)*

For more information, see [Focus States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/interaction-design-foundations-states#focus-state).

## Behavior and Interaction

### Mouse interaction

#### Type: group

In group mode, the entire avatar group acts as one interactive area.

Moving the cursor over the avatar group triggers the **hover state**.

*Hover state of an avatar group (type: group)*

While the user holds down the left mouse button, the entire avatar group displays the **down state** and receives focus.

*Down state of an avatar group (type: group)*

On release, an overview of all avatars appears, including those in the overflow. By default, the full avatar group opens in a [popover](https://www.sap.com/design-system/fiori-design-web/ui-elements/popover/), but app teams can also display it on a details page.

When the popover opens, the avatar group returns to its default state, and the focus state moves to the first avatar in the popover.

*A popover appears after releasing the avatar group*

Clicking outside the popover closes it and returns the avatar group to its **regular state**.

*Regular state of an avatar group (type: group)*

#### Type: individual

Each avatar and the overflow avatar respond individually to user interaction. When the type is set to "Individual," hovering over an avatar only applies the **hover state** to that specific avatar, not to the entire avatar group.

*Hover state of an avatar group (type: individual)*

While the user holds down the left mouse button, the selected avatar within the group displays the **down state** and receives focus.

*Down state of an avatar group (type: individual)*

Releasing the avatar triggers the action. A [popover](https://www.sap.com/design-system/fiori-design-web/ui-elements/popover/) appears, displaying additional information about the avatar. The content of the popover depends on the information that needs to be shown about the person.

*A popover appears after releasing the avatar*

Clicking outside the popover closes it, and the avatar group stays in its **regular state**.

*Regular state of an avatar group (type: individual)*

#### Overflow button

While the user holds down the left mouse button, the overflow button displays the **down state** and receives focus.

*Down state of the overflow button in the avatar group (type: individual)*

On a release, a [<u>popover</u>](https://www.sap.com/design-system/fiori-design-web/v1-139/ui-elements/popover/) appears, displaying all avatars in the group, including those in the overflow. The overflow button returns to its default state, and the focus state moves to the first avatar in the popover.

*A popover appears after releasing the overflow button*

Clicking outside the popover closes it, and the avatar group stays in its **regular state**.

#### Overflow (popover) content

When users interact with the overflow shape, they expect information about the “overflowed” avatars. By default, an overview of all “overflowed” avatars is displayed directly in a [<u>popover</u>](https://www.sap.com/design-system/fiori-design-web/ui-elements/popover/). **Adapt the content in the popover** to your individual app needs. We recommend displaying additional information for each avatar.

*Minimum version of the overflow popover (left), popover with context-specific information (right)*

#### Interacting with avatars in the overflow popover

When an avatar is in the [overflow popover](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar-group/#overflow-popover-content), the user should have access to the same detailed information as for avatars displayed in the visible group outside the overflow. Choosing the avatar either triggers navigation within the popover or navigation to another page (for example, with a person’s profile).

*Navigation from the overflow button to the overflow popover and avatar details*

**> **Guideline:** **

- If the group has fewer than 100 avatars, try to show all of them in the popover. This is the minimum visualization for overflowed avatars.
- Recommended: Provide primary or secondary information in the overflow popover to offer additional value to the user. Carefully select which
details should be primary and which should be secondary for display in the avatars, based on your user research findings.
- If you have more than 100 “overflowed” avatars, we recommend navigating to another page that displays all avatars properly. For example, you
can display them in a [<u>grid list</u>](https://www.sap.com/design-system/fiori-design-web/ui-elements/grid-list/) together with primary or
even secondary information. Ensure that the avatars in the list display in the same order as in the avatar group control on the page before.

### Touch enablement

On touch devices, users interact with the avatar group using a [single finger tap gesture](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/gestures#tap-press-and-release), mirroring mouse click behavior but without hover states.

### Tooltip :badge, info, large, _, SAPUI5 Only:

When enabled, the tooltip helps clarify the purpose or identity of each avatar. It appears on hover and provides additional context without interrupting the user experience.

When users hover over an avatar in an individual-type avatar group, a tooltip appears showing the person's name.

*Interactive avatar group (type: individual) with a tooltip*

When users hover over a group-type avatar group, a tooltip appears showing the name of the entire group.

*Interactive avatar group (type: group) with a tooltip*

## Responsiveness

### Overflow button

The avatar group is responsive. If there isn’t sufficient space to display all the avatars in a group, the overflow button appears and one or more avatars move into the overflow popover. The circular overflow button indicates the exact number of avatars that can’t be displayed on the screen. The size of the overflow button supports up to 3 symbols before truncation.

If the number no longer fits within the overflow shape, the shape expands to accommodate it.

You can also define a custom overflow to display the full avatar group on a separate page. This is recommended if you have a large number of avatars.

*Avatar group with overflow button*

## Accessibility

SAP follows international standards, such as WCAG and WAI-ARIA, and strives to make our business solutions accessible and inclusive.

For more information, see [Accessibility in SAP Fiori](https://www.sap.com/design-system/fiori-design-web/discover/sap-design-system/product-standards/accessibility-in-sap-fiori) and the [Accessibility Design Tools Handbook](https://www.sap.com/documents/2023/11/bc210d8b-977e-0010-bca6-c68f7e60039b.html).

### Keyboard navigation

The following keyboard combinations are supported by the SAPUI5 Avatar Group component.

**Table (col-width-30-70)**

Key combination

**Tab**
interactive element.

**Shift \+ Tab**

**Enter/ Return** or **Spacebar** or screen tap gesture
available.

**Shift \+ F10**
focused element.

### Screen reader support

For additional details on screen reader support and Accessible Rich Internet Applications (ARIA), see [<u>UI5 Screen Reader Support</u>](https://openui5nightly.hana.ondemand.com/topic/33fae3482358438e93daea5232527093) and [<u>WAI-ARIA Authoring</u>](https://www.w3.org/TR/wai-aria-1.2/).

## Content

### Localization

The avatar group supports left-to-right (LTR) and right-to-left (RTL) reading directions.

*Avatar group – left-to-right*

## Framework Comparison

Some behaviors differ between frameworks due to implementation specifics. The table below summarizes the differences between SAPUI5 and SAP Web Components and lists the framework-specific patterns.

**Table (col-width-50-20-30)**
+----------------------------------------------------------x----------------------------------------------------------+-------x-------+---------x----------+
Feature                                                                                                             | SAPUI5        | SAP Web Components
+----------------------------------------------------------x----------------------------------------------------------+---------------+---------x----------+
**Tooltips** can be used to help users identify avatars or                                                          | Available
understand their purpose. For more information, see the [Tooltip](#tooltip-badge-info-large-_-sapui5-only) section. |               | In progress

**\**

---

## avatar-group-web-component

+------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------+
+--------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------+---------x----------+
## This page has been deprecated and is no longer available.
This page was deprecated with guideline version **1.142**.
#### Reason for deprecation
The guidelines for the SAP Web Component and the SAPUI5 component have been merged. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).
#### Looking for the latest information?
Visit the page below for the unified guideline with the most recent updates.
[Avatar Group](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar-group/)

---

## avatar-web-component

+------------------------------------------------------------------------------------------------------------------------------------x-------------------------------------------------------------------------------------------------------------------------------------+
+--------------------------------------------------------------------------------------------------------------------------x--------------------------------------------------------------------------------------------------------------------------+---------x----------+
## This page has been deprecated and is no longer available.
This page was deprecated with guideline version **1.142**.
#### Reason for deprecation
The guidelines for the SAP Web Component and the SAPUI5 component have been merged. [Learn more](https://www.sap.com/design-system/fiori-design-web/discover/get-started/ui-elements-sap-design-system#transition-to-unified-component-guidelines).
#### Looking for the latest information?
Visit the page below for the unified guideline with the most recent updates.
[Avatar](https://www.sap.com/design-system/fiori-design-web/ui-elements/avatar/)

---

