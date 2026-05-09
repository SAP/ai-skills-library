---
name: sap-fiori-guidelines
description: SAP Fiori design guidelines for building enterprise applications. Use this skill when designing, building, or reviewing SAP Fiori applications, implementing SAPUI5 or UI5 Web Components, working with SAP enterprise UX patterns, or needing guidance on buttons, forms, tables, object pages, list reports, navigation, messaging, colors, typography, accessibility, AI/Joule integration, or any SAP Fiori UI element. Triggers on mentions of Fiori, SAPUI5, UI5, SAP UX, SAP design system, or enterprise application design following SAP standards.
---

# SAP Fiori Design Guidelines

Comprehensive guidance for designing and building SAP Fiori applications following official SAP design system standards.

## When to Use This Skill

- Designing or building SAP Fiori applications
- Implementing SAPUI5 or UI5 Web Components
- Following SAP enterprise UX patterns
- Choosing UI elements for SAP applications
- Implementing navigation, messaging, or data visualization
- Ensuring accessibility and inclusive design
- Applying colors, typography, or visual styling
- Designing AI-powered features, Joule integration, or guided prompts

## Core Principles

SAP Fiori is built on five principles:

1. **Role-based** - Designed for specific user roles and tasks
2. **Adaptive** - Works across devices and screen sizes  
3. **Coherent** - Consistent experience across all SAP applications
4. **Simple** - Focused on essential tasks, reduces complexity
5. **Delightful** - Engaging and intuitive user experience

## Technology Options

| Technology | Use Case |
|------------|----------|
| SAPUI5 | Full SAP Fiori applications, SAP BTP, S/4HANA |
| UI5 Web Components | Framework-agnostic, React/Vue/Angular integration |
| SAP Fiori Elements | Metadata-driven apps with OData services |

## Reference Documentation

Read the appropriate reference file based on your task:

### UI Elements

| Reference | Contents |
|-----------|----------|
| `references/ui-actions.md` | Buttons, links, toggle buttons, menu buttons |
| `references/ui-inputs.md` | Input fields, selects, checkboxes, radio buttons, sliders, date/time pickers, filter bar |
| `references/ui-containers.md` | Panels, cards, dialogs, popovers, toolbars, forms, shell bar, user menu, notification center |
| `references/ui-display.md` | Avatars, progress indicators, busy indicators, illustrated messages |
| `references/ui-lists-tables.md` | Responsive tables, grid tables, analytical tables, grid lists, lists |
| `references/ui-navigation.md` | Icon tab bar, segmented button, side navigation, shell search |
| `references/ui-messages.md` | Message strips, message strip web component |
| `references/ui-ai.md` | AI button, AI notice, AI writing assistant, AI acknowledgment, guided prompts, quick prompts, regenerate, home page banner |
| `references/ui-upload.md` | Upload set with table plugin |

### Page Types & Floorplans

| Reference | Contents |
|-----------|----------|
| `references/page-types.md` | Object page, list report, analytical list page, overview page, dynamic page layout, page header |

### Foundations

| Reference | Contents |
|-----------|----------|
| `references/foundations-visual.md` | Colors, typography, iconography, theming, content density |
| `references/foundations-interaction.md` | States, cursors, screen reader support |
| `references/foundations-writing-and-wording.md` | UX writing, UI text guidelines |
| `references/foundations-best-practices.md` | Navigation, messaging, object handling, action placement |
| `references/foundations-ai-and-joule-design.md` | AI design patterns, Joule assistant, situation handling, AI guidelines |
| `references/foundations-integration-and-services.md` | Fiori launchpad, integration patterns |

### SAP Fiori Elements & S/4HANA

| Reference | Contents |
|-----------|----------|
| `references/fiori-elements.md` | Smart templates, list report, object page, table features, AI input assistance |
| `references/sap-s4hana.md` | S/4HANA specific design: navigation menu, product home page, AI error explanation |

## Quick Reference

### Button Types and Usage

| Type | Usage |
|------|-------|
| Emphasized | Primary action - **one per page/dialog** |
| Default/Ghost | Secondary actions |
| Transparent | Toolbar actions, low emphasis |
| Accept (green) | Positive semantic actions (Approve, Accept) |
| Reject (red) | Negative semantic actions (Reject, Delete) |

### Semantic Colors

| Color | Meaning | Usage |
|-------|---------|-------|
| Neutral | Default state | Regular UI elements |
| Positive (Green) | Success, good status | Approval, completion |
| Critical (Orange) | Warning | Needs attention |
| Negative (Red) | Error, bad status | Rejection, errors |
| Information (Blue) | Informational highlight | Neutral information |

### Message Types

| Type | Usage |
|------|-------|
| Error | Prevents task completion, requires user action |
| Warning | Potential issue, user can proceed |
| Success | Confirms completed action |
| Information | Neutral information |

### Navigation Patterns

| Pattern | When to Use |
|---------|-------------|
| Drill-down | Navigate to object details with back navigation |
| Full-screen | Replace current view entirely |
| Flexible Column Layout | Master-detail views in columns |
| Dialog/Popover | Temporary overlay for quick tasks |

### AI Components

| Component | When to Use |
|-----------|-------------|
| AI Button | Trigger AI-powered actions |
| AI Acknowledgment | Show AI contribution transparency |
| Guided Prompts | Help users formulate AI requests |
| Quick Prompts | Provide predefined AI interaction shortcuts |
| Regenerate | Allow users to request new AI-generated content |
| AI Writing Assistant | Inline AI text assistance |
| Local AI Notice | Inform users about on-device AI processing |

## Implementation Checklist

When building a Fiori application:

- [ ] Single emphasized button per page/dialog
- [ ] Proper semantic colors for status indication
- [ ] Message handling with Message Popover
- [ ] Accessible labels and ARIA attributes
- [ ] Responsive layout for different screen sizes
- [ ] Consistent navigation patterns
- [ ] Form validation with value states
- [ ] Loading indicators for async operations
- [ ] AI features follow Joule design patterns where applicable

## Key Guidelines

### Buttons
- Use text buttons for primary, secondary, and semantic actions
- Icon-only buttons only for universally recognized metaphors
- Always provide tooltips for icon buttons
- Button text: imperative verb (Save, Edit, Create)

### Forms
- Group related fields logically
- Use proper field labels (always visible)
- Show validation errors with value states
- Provide clear error messages

### Tables
- Use responsive table for most cases
- Grid table for complex data analysis
- Analytical table for aggregation needs
- Always provide column headers

### Messages
- Message Popover for multiple messages
- Message Box only for interrupting errors
- Toast for transient success confirmations
- Inline validation for form fields

### AI Integration
- Use AI Button for AI-triggered actions
- Show AI Acknowledgment for transparency
- Provide Guided Prompts to help users interact with AI
- Always include Local AI Notice when processing happens on-device
- Follow responsible AI principles in all AI-powered features

## External Resources

- SAP Fiori Design Guidelines: https://experience.sap.com/fiori-design-web/
- SAPUI5 SDK: https://ui5.sap.com/
- UI5 Web Components: https://sap.github.io/ui5-webcomponents/

---

When implementing specific components, always read the relevant reference file for detailed guidance and examples.
