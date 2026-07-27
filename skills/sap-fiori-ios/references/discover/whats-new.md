# What's New — SAP Fiori for iOS

> SAP Fiori for iOS | Discover

Release history for the SAP Design System portal and SAP BTP SDK for iOS.

---

## Portal Update — New SAP Design System Portal

The SAP Fiori Design Guidelines are now the all-encompassing **SAP Design System Guidelines** at `sap.com/design-system`. The old URL (`experience.sap.com/fiori-design`) redirects to the new portal during a transitional period.

---

## SAP BTP SDK for iOS 26.4

### List Picker Form Cell
Read-only state added: selected values shown inline, chevron removed, non-interactive. No word limit on displayed values — long or multi-select values may cause extended cell heights; use a custom summary view if needed.
→ [../components/list-picker-form-cell.md](../components/list-picker-form-cell.md)

### Switch Form Cell
Read-only state added: text label replaces visual switch (default "On/Off", fully customizable). Cell height and padding consistent with active state.
→ [../components/switch-form-cell.md](../components/switch-form-cell.md)

---

## SAP BTP SDK for iOS 26.1

### Adaptive Apps
Best practices for designing adaptive apps. New usage patterns article maps use cases to containers across size classes.
→ [../foundations/adaptive-layout.md](../foundations/adaptive-layout.md)

### AI User Feedback
Inline AI user feedback now available as a standalone reusable component.
→ [../in-app-ai-design/patterns/ai-user-feedback.md](../in-app-ai-design/patterns/ai-user-feedback.md)

### Step Progress Indicator
Step node width is now flexible with a minimum value, allowing the indicator to fill screen width when there are fewer steps.
→ [../components/step-progress-indicator.md](../components/step-progress-indicator.md)

---

## SAP BTP SDK for iOS 25.11

### Actionable Text Weight
Actionable text (hyperlinks, buttons) updated to **semibold** weight to meet accessibility requirements. Affects: banner, button form cell, key value table view cell, header cell, multi-message handling.

### AI Handoff *(New Pattern)*
Common use cases for Joule vs embedded AI, best practice tips, and handoff example flows.
→ [../in-app-ai-design/patterns/ai-handoff.md](../in-app-ai-design/patterns/ai-handoff.md)

### AI Insights *(New Pattern)*
Standardized way to display AI-generated summaries, analyses, or suggestions.
→ [../in-app-ai-design/patterns/ai-insights.md](../in-app-ai-design/patterns/ai-insights.md)

### App Icons
Updated guidance for Liquid Glass aesthetic; new naming convention section; Apple Icon Composer section.
→ [../foundations/app-icon.md](../foundations/app-icon.md)

### Attachment Form Cell
Loading indicator feedback during upload; updated per-file error handling.
→ [../components/attachment-form-cell.md](../components/attachment-form-cell.md)

### Card System
Horizontal card variants added. New flex-item component for flexible card main header configuration (tags, status info labels outside/between/below title and subtitle).
→ [../components/cards.md](../components/cards.md)

### Text Inputs
Label color updated to black for typing state; right-side padding for character counters removed; real-time counter color changed to gray at limit. Affects: text field form cell, key value form cell.
→ [../components/text-inputs.md](../components/text-inputs.md)

### Single-User Onboarding
New splash screen guidance (logo-only). Skip Passcode for optional passcode setups. Change Passcode enhanced with Remove Passcode support.
→ [../patterns/single-user-onboarding.md](../patterns/single-user-onboarding.md)

### Toolbar
Overflow interaction updated: tapping overflow opens a menu with text-only action buttons.
→ [../components/toolbar.md](../components/toolbar.md)

---

## SAP BTP SDK for iOS 25.8

### AI Writing Assistant *(New Pattern)*
Edits text in input fields via prompts in a panel.
→ [../in-app-ai-design/patterns/ai-writing-assistant.md](../in-app-ai-design/patterns/ai-writing-assistant.md)

### AI User Feedback *(New Pattern)*
Positive/negative feedback on embedded AI, component-level to page-level.
→ [../in-app-ai-design/patterns/ai-user-feedback.md](../in-app-ai-design/patterns/ai-user-feedback.md)

### Modals and Sheets *(New Guidelines)*
Full coverage: full-screen modals, non-modal sheets, action sheets, popovers, form sheets.
→ [../components/modals.md](../components/modals.md), [../components/sheets.md](../components/sheets.md)

### Picker
Date range picker now supported as a picker form cell.
→ [../components/pickers.md](../components/pickers.md)

### Text Inputs
Currency support: ISO code in input label, currency symbol after editing, localized formatting.
→ [../components/text-inputs.md](../components/text-inputs.md)

### Deprecated: Card Types
Removed in SDK 25.12. Use [Cards](../components/cards.md) instead.

### Deprecated: Empty State View
Removed in SDK 25.12. Use [Illustrated Message](../components/illustrated-message.md) instead.

---

## SAP BTP SDK for iOS 25.4

### Adaptive Layout *(Updated Guidelines)*
Size classes, layout basics, multi-column layouts, adaptive apps for large screens.
→ [../foundations/adaptive-layout.md](../foundations/adaptive-layout.md)

### AI Notice
Available as helper text beneath form cells; interactive (standalone) or non-interactive (with page-level banner) depending on number of AI fields.
→ [../in-app-ai-design/patterns/ai-notice.md](../in-app-ai-design/patterns/ai-notice.md)

### Attachment Form Cell
Optional confirmation dialog added for the "Delete" action in the previewer.
→ [../components/attachment-form-cell.md](../components/attachment-form-cell.md)

### Card Header
Right accessory in main header now has two slots for custom components. Right accessory in extended header has one custom component slot.
→ [../components/cards.md](../components/cards.md)

### Filter Feedback
Stepper, slider, and list picker added as new form cells in the filter feedback pattern.
→ [../components/filter-feedback-bar.md](../components/filter-feedback-bar.md)

### Progress Indicators *(New Guidelines)*
Activity indicator and progress & processing indicators added as separate guideline articles.
→ [../components/activity-indicator.md](../components/activity-indicator.md), [../components/progress-and-processing-indicator.md](../components/progress-and-processing-indicator.md)

---

## SAP BTP SDK for iOS 24.12

### Elevation *(New)*
Full elevation article covering shadow levels and material effects.
→ [../foundations/elevation.md](../foundations/elevation.md)

### Chart Colors
Updated ordered and semantic chart colors to align with web.
→ [../foundations/colors.md](../foundations/colors.md)

### Avatars
Grouped layout and top/bottom labels added to avatar stack.
→ [../components/avatars.md](../components/avatars.md)

### Document Scanner
Automatic and manual mode, border detection, multi-page scanning and editing.
→ [../patterns/document-scanner.md](../patterns/document-scanner.md)

### Multi-Message Handling *(New)*
Banner overview of multiple messages with detail view link.
→ [../components/multi-message-handling.md](../components/multi-message-handling.md)

### Object Cell
More flexibility: swappable nested elements mirroring cards (rating control, label button, avatar stack, overflow button).
→ [../components/object-cell.md](../components/object-cell.md)

### Rating Control
Half stars for read-only; optional leading/trailing text; enhanced read-only star sizes; small editable/disabled removed for accessibility.
→ [../components/rating-control.md](../components/rating-control.md)

### Step Progress Indicator
Icon nodes added as alternative to numeric nodes.
→ [../components/step-progress-indicator.md](../components/step-progress-indicator.md)
