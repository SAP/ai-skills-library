# SAP Fiori Foundations: Interaction

## Keyboard Support

# Keyboard Support

## Intro

Every application and UI component must be fully operable using the keyboard.

This foundation concept defines the global principles and interaction models for keyboard navigation, selection, activation, and text interaction across SAP experiences.

It defines a consistent, predictable baseline for keyboard behavior across components and layouts, so designs remain accessible, efficient, and scalable.

Detailed keyboard behaviors and interaction patterns are documented in the referenced Figma frames.

## General Concepts

Certain concepts and shared mechanisms apply across all keyboard interactions and UI components. These include:

- UI element states relevant to keyboard interaction
- The role and intent of modifier keys
- Browser and platform context affecting keyboard behavior
- General principles for mapping keys to interaction intent

These concepts form the basis for all keyboard interaction patterns in this guideline.

For more information, see [General Concepts](https://www.figma.com/design/zy0CLKKHfLwjGvldHQwa3q/-Keyboard-Support--Specification--WIP-?node-id=5303-100616\&t=OiyQceFFCqekDYn6-4) in the Keyboard design specification.

## Design Principles

The following core principles guide the design of keyboard interactions across SAP experiences:

- **Predictability and robustness**, ensuring consistent and stable keyboard behavior
- **Immediate reversibility**, allowing users to easily undo or adjust keyboard actions
- **Discoverability**, enabling users to learn and understand available keyboard interactions
- **Efficiency**, supporting fast and effective interaction for both novice and expert users

These principles underpin all keyboard interaction patterns described in this guideline.

For more information, see [Design Principles](https://www.figma.com/design/zy0CLKKHfLwjGvldHQwa3q/-Keyboard-Support--Specification--WIP-?node-id=861-2659\&t=OiyQceFFCqekDYn6-4) in the Keyboard design specification.

## Navigation

Keyboard navigation defines how focus moves between components and items, independent of selection or activation behavior. It includes:

- **Navigation between components**, defining how focus moves across distinct UI areas
- **Skip navigation**, enabling users to bypass repeated content and reach key areas efficiently
- **One-dimensional item navigation**, used for linear structures such as lists or rows
- **Two-dimensional item navigation**, used for spatial layouts with horizontal and vertical relationships

Navigation behavior is derived from the structural layout of the UI and must remain predictable and consistent across components.

For more information, see [Navigation](https://www.figma.com/design/zy0CLKKHfLwjGvldHQwa3q/-Keyboard-Support--Specification--WIP-?node-id=5303-53820\&t=OiyQceFFCqekDYn6-4) in the Keyboard design specification.

## Selection

Selection behavior defines how users select one or multiple items using the keyboard. Selection includes:

- **Single selection**, where only one item can be selected at a time
- **Multi-selection**, allowing multiple items to be selected within a one-dimensional structure
- **Block selection**, allowing rectangular selection ranges in two-dimensional structures
- **Selection in drop-down lists and suggestion lists**, where users choose options from a predefined set

Selection behavior depends on the structure and selection capabilities of the UI. It must remain predictable and clearly distinguishable from navigation and activation.

For more information, see [Selection](https://www.figma.com/design/zy0CLKKHfLwjGvldHQwa3q/-Keyboard-Support--Specification--WIP-?node-id=5303-53826\&t=OiyQceFFCqekDYn6-4) in the Keyboard design specification.

## Action

Action patterns define how users trigger operations with the keyboard. We focus on patterns commonly used across SAP components and contexts:

- **Triggering actions on item level**, for example activating the currently focused item
- **Opening and closing interaction surfaces**, including context menus
- **Opening and closing assistance surfaces**, including drop-down lists and value help

These action patterns must remain consistent and clearly distinguishable from navigation and selection behavior.

For more information, see [Action](https://www.figma.com/design/zy0CLKKHfLwjGvldHQwa3q/-Keyboard-Support--Specification--WIP-?node-id=5303-53832\&t=OiyQceFFCqekDYn6-4) in the Keyboard design specification.

## Drag and Drop

Keyboard drag-and-drop provides an accessible alternative to pointer-based interaction. It covers:

- Initiating drag operations
- Moving items
- Dropping items
- Canceling drag operations

For more information, see [Drag and Drop](https://www.figma.com/design/zy0CLKKHfLwjGvldHQwa3q/-Keyboard-Support--Specification--WIP-?node-id=5369-52609\&t=OiyQceFFCqekDYn6-4) in the Keyboard design specification.

## Text

Text interaction covers keyboard behavior for entering, navigating, and modifying text, depending on the type and structure of the text content. It includes:

- **Text editing**, covering basic text input and modification
- **One-dimensional text editing**, such as linear text fields or single-line inputs
- **Two-dimensional text editing**, such as multi-line or structured text areas
- **Auto-complete**, supporting assisted text entry through suggestions

Text interaction behavior is distinct from navigation and selection and applies only within explicit text editing contexts.

For more information, see [Text](https://www.figma.com/design/zy0CLKKHfLwjGvldHQwa3q/-Keyboard-Support--Specification--WIP-?node-id=5303-53838\&t=OiyQceFFCqekDYn6-4) in the Keyboard design specification.

## Shortcuts

Optional keyboard shortcuts give users a faster path for common actions while remaining consistent with global keyboard behavior. The shortcut definition covers:

- **Types of shortcuts**, describing different categories and usage contexts
- **Access keys**, enabling direct access to specific UI elements
- **Default button behavior**, defining how primary actions are triggered
- **Recommended shortcuts for Fiori**, providing a standardized set of commonly used shortcuts

Shortcuts must be consistent and discoverable, and must never conflict with shortcuts reserved by the platform or browser.

For more information, see [Shortcuts](https://www.figma.com/design/zy0CLKKHfLwjGvldHQwa3q/-Keyboard-Support--Specification--WIP-?node-id=5303-53844\&t=OiyQceFFCqekDYn6-4) in the Keyboard design specification.

---

## Overview

# Interaction Design Foundations - Overview

## Intro

The interaction design foundations define how the user interface should behave when users interact with it to complete specific tasks and achieve their goals. Interaction occurs through input devices such as a mouse, keyboard, gestures, or voice commands, and output devices like screens or screen readers.

These foundations are standardized across the SAP Design System and cannot be modified by individual teams. They should serve as a baseline when designing components, patterns, and floorplans, where applicable.

We will continue to build out the foundation guidelines on an ongoing basis.


**Foundations (available)**
The following guidelines are currently available:
following topics:
- [Cursors](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/cursors)
- [Drag and Drop](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/drag-and-drop-overview)
- [Gestures](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/gestures)
- [Keyboard Support](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/keyboard-support)
- [Motion Design](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/motion-design-overview)
- [Screen Reader](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/screen-reader)
- [States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/interaction-design-foundations-states)
- [Timing](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/interaction-design-foundations-timing)
- [Wrapping and Truncation](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/wrapping-and-truncation)
Read on for a short summary of each one.
**Columns (external_only)**

**Foundations**
The following guidelines are currently available:
- [Cursors](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/cursors)
- [Drag and Drop](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/drag-and-drop-overview)
- [Gestures](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/gestures)
- [Motion Design](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/motion-design-overview)
- [States](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/interaction-design-foundations-states)
- [Timing](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/interaction-design-foundations-timing)
- [Wrapping and Truncation](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/wrapping-and-truncation)
Read on for a short summary of each one.
## Cursors

Cursors are graphical elements that show the current position in the software interface. The cursor’s visual representation changes, depending on where it is placed. This indicates which mouse interactions are available in the context.

For more information, see [Cursors](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/cursors).

## Drag and Drop

Drag and drop is an interaction that lets users reorder, resize, move elements, and transfer data with clear real-time feedback.

We categorize drag and drop into four main use cases:

- **Reorder:** Change the order of items within components, like list items.
- **Resize**: Adjust component sizes, such as dialog boxes or table columns.
- **Move**: Shift components to new positions, including dialogs or slider values.
- **Data Transfer**: Move data between components or applications, like dragging items between lists or uploading files.

For more information, see:

- [Drag and Drop Overview](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/drag-and-drop-overview)
- [Reorder](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/drag-and-drop/reorder)
- [Resize](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/drag-and-drop/resize)
- [Move](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/drag-and-drop/move)
- [Data Transfer](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/drag-and-drop/data-transfer)

## Gestures

Gestures are touch-based interactions that use natural hand movements to let users navigate, manipulate, and engage with digital interfaces.

Each gesture – such as swipe, tap, double tap, long press, or rotate – expresses specific intentions. Gestures assist with navigation and tasks, or enable users to adjust the size, position, or orientation of elements on the screen.

For more information, see [Gestures](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/gestures).

## Motion Design

Motion design brings interfaces to life through the use of animated visual elements, helping users navigate SAP applications more intuitively and efficiently.

By providing clear feedback and highlighting changes with subtle animations, motion design enhances user focus, simplifies complex tasks, and creates a polished, modern experience that encourages user adoption.

For more information, see [Motion Design](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/motion-deisgn-overview).

## States

States define the appearance and behavior of a UI element based on user interactions or system status. They influence aspects such as interactivity, visibility, and the semantic meaning of a component. Applying the correct state – or combination of states – helps users identify available options and understand where their input is needed.

UI elements can have different types of states, which may appear individually or combined:

- [Component State](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-component-states)
- [Focus State](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-focus-states)
- [Interaction State](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-interaction-states)
- [Selection State](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-selection-states)
- [Value State](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-value-states)

For more information, see [States Overview](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/interaction-design-foundations-states) and [State Combinations](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-state-combinations).

## Timing

Timing in interaction design shapes how users experience transitions, feedback, and system responsiveness. The right timing helps users notice changes without unnecessary delays, balancing clarity with efficiency. Factors like component size, complexity, and user intent all influence how long a component should appear, disappear, or respond.

We distinguish between four timing groups – fast, normal, slow, and very slow. Each group has distinct response times, feedback, and states, and applies to different types of components.

For more information, see [Timing](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/timing).

## Wrapping and Truncation

Wrapping and truncation determine how text behaves when its length exceeds the available space. This responsive behavior is consistent across all devices and form factors. Various controls utilize wrapping and/or truncation to manage text display.

For more information, see [Wrapping and Truncation](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/wrapping-and-truncation).

---

## Timing

# Timing

## Intro

Timing refers to how long a component appears or disappears on screen, as well as any intentional delay between user input and the system response. The speed should be slow enough for users to notice changes, but fast enough to avoid unnecessary waiting.

## General Principles

Generally, timing correlates with component size. The following sections explain how durations differ for small and large components.

### Small Components

Small components usually contain less content and carry less visual weight, so users can process updates and changes quickly. Shorter transition times work well here—quick transitions help keep interactions brisk, reduce disruption, and let users stay focused on the main content.

### Large Components

Large components often present more information, have greater visual prominence, and can cause more noticeable changes to the layout. Use longer transitions for these components. This gives users time to notice and understand the change, support cognitive processing, and integrate new information smoothly without feeling rushed or disrupted.

### What to Consider

- **Complexity and detail:** More complex or detailed components may need more time for users to absorb information.
- **Visibility and noticeability:** More visually dominant components attract attention, so longer durations can help users understand the change and its purpose.
- **Impact on the overall interface:** Large components have a greater potential to disrupt flow, so longer transitions help maintain a smooth experience.
- **User focus and engagement:** Transition timing can help direct user attention and ensure important information isn’t missed.

## User Intent

Timing is directly related to the user’s intent and expectations. Well-timed transitions guide focus and provide feedback from the system to the user.

### Enter and Exit

When a component enters (appears on the screen), a slightly slower transition helps users notice the change, understand the context, and prepare for interaction. By contrast, components often exit more quickly to reduce the delay and maintain a responsive feel.

- **User attention and orientation:** Longer entry transitions give users time to notice and get used to new elements, which aids comprehension. Quick exits remove clutter efficiently and let users focus on what comes next.
- **Cognitive load:** Slower entries give users time to process new information, reducing cognitive load. Fast exits minimize cognitive load by clearing unnecessary elements quickly.
- **Expectations and feedback**: Longer entry transitions signal new content, aligning with user expectations. Fast exits provide immediate feedback and confirm task completion.
- **Emotional and aesthetic appeal**: Smooth transitions improve aesthetics and contribute to a more positive user experience. Quick exits create a dynamic, responsive feel.

### Reveal Hidden Content

When a user hovers over an item for 300 to 500 milliseconds, this often shows intent to open the item or display hidden content. Revealing hidden content too quickly can cause accidental activations and confuse users, especially during casual cursor movement. On the other hand, waiting too long can make the interface feel unresponsive and interrupt the user’s workflow.

## Timing Groups

You can group components by how long they take to appear on screen or respond to user input:

- **Fast**: Up to 100 milliseconds
- **Normal**: 100 to 1,000 milliseconds
- **Slow**: 1 to 3 seconds
- **Very slow**: More than 3 seconds

Note: 1 second = 1,000 milliseconds.

### Fast (up to 100 milliseconds)

Interactions with components should feel immediate and seamless for users. This creates a sense of direct manipulation and responsiveness.

- **Response time**: Immediate or near-instantaneous (less than 100 milliseconds)
- **Feedback**: Immediate visual feedback
- **State updates**: Update immediately with no noticeable delay
- **Examples**: Changes to the button state, checkboxes and radio buttons, dialogs

*Change in the button state on hover – example of a fast interaction (up to 100 milliseconds display time)*

An example of fast interaction timing is how a button responds on hover:

**A. Entry:** When the user moves the mouse pointer over the button, the interaction state changes from regular to hover, giving a visual indication that the component is interactive.
**B. Exit:** When the user moves the mouse away from the button area, the state returns to regular.
**C. Display time:** Each change in state should happen within 100 milliseconds.

### Normal (100 to 1,000 milliseconds)

Components in this group handle slightly more complex operations.

- **Response time**: Expect 100 to 1,000 milliseconds
- **Feedback:** Perceived as fluid and responsive, acceptable for most interactions
- **State updates:** There may be a brief delay due to more complex data processing or content changes
- **Examples:** Tooltips, popovers, delay after the last keystroke to optimize search performance

*Tooltip display – example of a normal interaction (100 to 1,000 milliseconds display time)*

An example of normal interaction timing is tooltip behavior:

**A. Entry:** The standard time to display a tooltip with a mouse is 500 milliseconds. This prevents flickering or accidental activation when users move the cursor quickly. The same delay applies when showing a tooltip via keyboard. For touch interactions, tooltips appear instantly with no delay.
**B. Exit:** When triggered by hovering, a tooltip disappears 500 milliseconds after the cursor leaves the element. The same 500 millisecond delay applies when dismissed via keyboard. Tooltips aren’t focusable. On touch devices, the tooltip disappears immediately after the user taps outside the element.

Note: When displaying tooltips in sequence, use a 200 millisecond delay between tooltips. This means the previous tooltip disappears and the new one appears after the delay.

### Slow (1-3 seconds)

Components in this category are typically larger or more resource intensive. They include complex data visualizations, transitions that involve multiple components, or major layout changes that need more processing. Some components are designed to stay visible longer, not because they’re slow to respond, but because they provide important information. For example, message toasts use a longer display time on purpose, so users have enough time to read and process the message without interrupting their workflow.

- **Response time**: 1 to 3 seconds (1,000 to 3,000 milliseconds)
- **Feedback**: Clear feedback or transition effects to keep users engaged
- **State updates**: Clearly noticeable delay
- **Examples**: Message toast (minimum display time), busy indicator, card loading, [placeholder loading](https://www.sap.com/design-system/fiori-design-web/ui-elements/placeholder-loading/)

*Message toast – example of a slow interaction (3,000 milliseconds default display time)*

An example of slow interaction timing is message toast behavior:

- **Entry:** The message toast should appear quickly after the triggering action to provide clear feedback.
- **Minimum display time**: By default, the toast stays visible for 3,000 milliseconds before the close animation starts. For longer messages, you can extend the display time.
- **Exit:** By default, the close animation takes 1,000 milliseconds to complete. If no animation is needed, you can set this to zero.

### Very Slow (more than 3 seconds)

Response delays over 3 seconds can disrupt user flow and may lead to frustration or abandonment if you don’t handle them well. If delays can’t be avoided, provide visual feedback to reassure users. Use elements like content placeholders or progress indicators.

In some cases, time-related components – like message toasts – are meant to remain visible for long periods by design. This helps ensure users have enough time to read and process important information. Longer display times are acceptable when providing informative feedback without interrupting the user workflow.

- **Response time:** More than 3 seconds (over 3,000 milliseconds)
- **Feedback:** Clearly show users that the interaction may take a while
- **State updates:** May involve large operations or loading significant amounts of data
- **Examples:** Repetitive placeholders, busy indicators, progress indicators, AI-generated content, authentication processes

*Busy indicator – example of a slow or very slow interaction (1-3 seconds display time)*

#### Minimum and Maximum Display Times

The recommended minimum display time is 500 milliseconds. This helps prevent flickering. Adjust this duration as needed to fit your specific use case.

If a process takes more than 10 seconds, show a more detailed progress animation, such as a placeholder animation.

An example of very slow interaction timing is the busy indicator:

- **Entry**: Only use a busy indicator for system operations that take 1,000 milliseconds or more. For faster operations, don’t show a busy indicator. If you need the busy indicator to appear instantly, set the delay time to 0 milliseconds.
- **Minimum display time**: Set a minimum display time of 500 milliseconds to prevent flickering. Adjust this duration if your use case requires it.
- **Maximum display time**: If a process takes more than 10 seconds, show more detailed progress, such as a placeholder animation.

**Metadata**

Title

Breadcrumbs

Description
appear or disappear from the screen, as well as any
intentional delay between user input and system response.

---

