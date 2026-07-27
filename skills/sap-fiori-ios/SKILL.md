---
name: sap-fiori-ios
description: SAP Fiori for iOS Design Skill — Converts Figma designs from the Fiori iOS UI Kit into SwiftUI prototypes with animations and interactions. Use this skill when a designer provides a Figma node ID or component name and wants working SwiftUI code, when asking which Fiori iOS component to use, when mapping Figma variants to SwiftUI, or when adding animations and state transitions to iOS prototypes. Triggers on: Fiori iOS, SwiftUI, iOS prototype, Figma to iOS, FioriButton, FioriTheme, animation, interaction, SAP 72, preferredFioriColor, ObjectItem, FioriSwiftUI.
---

# SAP Fiori for iOS — Design Skill

## Figma UI Kit

**File key:** `1450853598524410675`
**Community URL:** `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`

### How to read a component from Figma
```
get_figma_data(fileKey: "1450853598524410675", nodeId: "<nodeId>", depth: 3)
```

### Known Page Node IDs (depth=1 from file root)
| Page | Contents |
|------|----------|
| Cover | File cover |
| 🎨 Foundations | Colors, typography, spacing, elevation |
| 🔘 Buttons | FioriButton all variants |
| 🗂 Cards | Card, KPI Card, Timeline Card |
| 📋 Lists | ObjectItem, SectionHeader, KeyValueItem |
| 🗺 Navigation | TabBar, NavigationBar, SideBar |
| 📝 Forms | TextFieldFormView, NoteFormView, SwitchFormView |
| 📊 Charts | All chart types |
| 🔔 Notifications | Banners, toasts, badges |
| 📅 Pickers | DateTimePicker, DurationPicker |
| 📈 KPI | KPIItem, KPIProgressItem, KPIHeader |

---

## Core Rule: NEVER hardcode hex values

Always use Fiori color tokens. The API is:

```swift
// Dynamic color (adapts to Light / Dark automatically)
Color.preferredColor(.primaryLabel)

// In a view modifier context
.foregroundStyle(Color.preferredColor(.tintColor))

// Force a specific scheme
Color.preferredColor(.tintColor, background: .darkConstant)
```

See [references/foundations/colors.md](references/foundations/colors.md) and [references/colors.md](references/colors.md) for the full token table.

---

## Figma Variant → SwiftUI Mapping

### FioriButton

| Figma Variant Property | Figma Value | SwiftUI |
|------------------------|-------------|---------|
| Type | Primary | `.fioriPrimaryButtonStyle` |
| Type | Secondary | `.fioriSecondaryButtonStyle` |
| Type | Tertiary | `.fioriTertiaryButtonStyle` |
| Type | Destructive | `.fioriDestructiveButtonStyle` |
| Type | Menu | `.fioriMenuButtonStyle` |
| State | Default | (no modifier) |
| State | Pressed | `.disabled(false)` + tap gesture |
| State | Disabled | `.disabled(true)` |

```swift
// Primary button
FioriButton { _ in Text("Continue") }
    .fioriButtonStyle(.fioriPrimaryButtonStyle)

// Secondary
FioriButton { _ in Text("Cancel") }
    .fioriButtonStyle(.fioriSecondaryButtonStyle)

// Full width
FioriButton { _ in Text("Submit") }
    .fioriButtonStyle(.fioriPrimaryButtonStyle)
    .frame(maxWidth: .infinity)
```

### Typography

| Figma Text Style | SwiftUI |
|-----------------|---------|
| extraLargeTitle | `.fiori(forTextStyle: .extraLargeTitle)` |
| extraLargeTitle2 | `.fiori(forTextStyle: .extraLargeTitle2)` |
| largeTitle | `.fiori(forTextStyle: .largeTitle)` |
| title1 | `.fiori(forTextStyle: .title1)` |
| title2 | `.fiori(forTextStyle: .title2)` |
| title3 | `.fiori(forTextStyle: .title3)` |
| headline | `.fiori(forTextStyle: .headline)` |
| body | `.fiori(forTextStyle: .body)` |
| callout | `.fiori(forTextStyle: .callout)` |
| subheadline | `.fiori(forTextStyle: .subheadline)` |
| footnote | `.fiori(forTextStyle: .footnote)` |
| caption1 | `.fiori(forTextStyle: .caption1)` |
| caption2 | `.fiori(forTextStyle: .caption2)` |
| KPI | `.fiori(forTextStyle: .KPI)` |
| largeKPI | `.fiori(forTextStyle: .largeKPI)` |

```swift
Text("Hello")
    .font(.fiori(forTextStyle: .headline))

Text("42")
    .font(.fiori(fixedSize: 36, weight: .light))  // fixed KPI number
```

### Navigation

| Figma Component | SwiftUI Equivalent |
|----------------|--------------------|
| TabBar | `TabView` + `.tabItem {}` |
| NavigationBar | `NavigationStack` + `.navigationTitle()` + `.toolbar {}` |
| SideBar | `NavigationSplitView` with `SidebarListStyle` |
| BackButton | Automatic in `NavigationStack` |

### Cards

| Figma Variant | SwiftUI |
|--------------|---------|
| Card / Default | `CardView {}` or custom VStack in card style |
| Card / Highlighted | Add `.overlay(RoundedRectangle.stroke(Color.preferredFioriColor(forStyle: .tintColor)))` |
| KPI Card | `_KPIItem` or custom card with `.fiori(forTextStyle: .KPI)` |

### List / ObjectItem

| Figma Property | SwiftUI |
|---------------|---------|
| ObjectItem / 1-line | `ObjectItem(title: Text(""), footnote: nil)` |
| ObjectItem / 2-line | `ObjectItem(title: Text(""), subtitle: Text(""))` |
| ObjectItem / 3-line | `ObjectItem(title: Text(""), subtitle: Text(""), footnote: Text(""))` |
| ObjectItem / with icon | Add `detailImage: Image(...)` |

### Forms

| Figma Variant | SwiftUI Component |
|--------------|-------------------|
| TextField | `TextFieldFormView(title: Text(""), text: $value)` |
| NoteField | `NoteFormView(title: Text(""), text: $value)` |
| KeyValue | `KeyValueFormView(keyText: Text(""), value: Text(""))` |
| Switch | `SwitchFormView(title: Text(""), isOn: $value)` |
| DateTimePicker | `_DateTimePicker(...)` |

---

## Animation Specs

| Interaction | Animation |
|-------------|-----------|
| Button tap press | `.scaleEffect(0.97)` with `.spring(response: 0.2, dampingFraction: 0.8)` |
| View appear | `.opacity(0→1)` + `.offset(y: 8→0)` with `.easeOut(duration: 0.25)` |
| Sheet present | System default `.sheet()` — do not override |
| List row tap | `.opacity` feedback with `duration: 0.15` |
| Navigation push | System default — do not override |
| Toggle switch | System default `.toggle()` — let SwiftUI handle |
| Loading/skeleton | `.opacity(0.3...1.0)` repeating with `.easeInOut(duration: 0.9)` |
| Error shake | `.offset(x: -6...6)` sequence, 3 cycles, `duration: 0.07` each |

```swift
// Standard button press feedback
struct FioriButtonPress: ViewModifier {
    @State private var isPressed = false
    func body(content: Content) -> some View {
        content
            .scaleEffect(isPressed ? 0.97 : 1.0)
            .animation(.spring(response: 0.2, dampingFraction: 0.8), value: isPressed)
            .simultaneousGesture(DragGesture(minimumDistance: 0)
                .onChanged { _ in isPressed = true }
                .onEnded { _ in isPressed = false })
    }
}
```

---

## FioriTheme Setup

```swift
// AppDelegate — call at launch
import FioriThemeManager

func application(_ application: UIApplication,
                 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    ThemeManager.shared.setPaletteVersion(.v8)  // pin to current Fiori Next palette
    Font.registerFioriFonts()                   // register SAP 72 typeface
    return true
}

// To override individual tokens:
ThemeManager.shared.setHexColor("FF6000", for: .tintColor, variant: .light)
ThemeManager.shared.reset()  // clear all overrides
```

---

## Quick Start SwiftUI Template

```swift
import SwiftUI
import FioriSwiftUICore
import FioriThemeManager

struct FioriScreenTemplate: View {
    var body: some View {
        NavigationStack {
            List {
                ObjectItem {
                    Text("Invoice #1234")
                } subtitle: {
                    Text("SAP SE")
                } footnote: {
                    Text("Due: 30 Jan 2026")
                } detailImage: {
                    Image(systemName: "doc.text")
                }
            }
            .navigationTitle("My Items")
            .toolbar {
                ToolbarItem(placement: .primaryAction) {
                    FioriButton { _ in Image(systemName: "plus") }
                        .fioriButtonStyle(FioriPrimaryButtonStyle())
                }
            }
        }
    }
}
```

---

## File Directory

> **All content lives under `references/`.** When reading any file, always use the full path from the skill root as listed below. Never guess a path — look it up here first.

### Foundations — `references/foundations/`
| Topic | File |
|-------|------|
| Colors & tokens | [references/foundations/colors.md](references/foundations/colors.md) |
| Typography (SAP 72) | [references/foundations/typography.md](references/foundations/typography.md) |
| Theming & FioriTheme | [references/foundations/theming.md](references/foundations/theming.md) |
| Design tokens | [references/foundations/design-tokens.md](references/foundations/design-tokens.md) |
| Accessibility | [references/foundations/accessibility.md](references/foundations/accessibility.md) |
| Adaptive layout | [references/foundations/adaptive-layout.md](references/foundations/adaptive-layout.md) |
| Animation | [references/foundations/animation.md](references/foundations/animation.md) |
| Elevation & shadows | [references/foundations/elevation.md](references/foundations/elevation.md) |
| Iconography | [references/foundations/iconography.md](references/foundations/iconography.md) |
| App icon | [references/foundations/app-icon.md](references/foundations/app-icon.md) |
| App Store appearance | [references/foundations/app-store-appearance.md](references/foundations/app-store-appearance.md) |
| Time & date formats | [references/foundations/time-and-date-formats.md](references/foundations/time-and-date-formats.md) |

### Components — `references/components/`
| Topic | File |
|-------|------|
| Activity indicator / loading | [references/components/activity-indicator.md](references/components/activity-indicator.md) |
| Attachment form cell | [references/components/attachment-form-cell.md](references/components/attachment-form-cell.md) |
| Avatars | [references/components/avatars.md](references/components/avatars.md) |
| Avatars & images | [references/components/avatars-and-images.md](references/components/avatars-and-images.md) |
| Banner | [references/components/banner.md](references/components/banner.md) |
| Button form cell | [references/components/button-form-cell.md](references/components/button-form-cell.md) |
| Buttons (FioriButton) | [references/components/buttons.md](references/components/buttons.md) |
| Calendar | [references/components/calendar.md](references/components/calendar.md) |
| Cards | [references/components/cards.md](references/components/cards.md) |
| Chart header | [references/components/chart-header.md](references/components/chart-header.md) |
| Checkout indicator | [references/components/checkout-indicator.md](references/components/checkout-indicator.md) |
| Collection view | [references/components/collection-view.md](references/components/collection-view.md) |
| Contact cell | [references/components/contact-cell.md](references/components/contact-cell.md) |
| Data table | [references/components/data-table.md](references/components/data-table.md) |
| Dimension selector | [references/components/dimension-selector.md](references/components/dimension-selector.md) |
| Empty state view | [references/components/empty-state-view.md](references/components/empty-state-view.md) |
| Error handling | [references/components/error-handling.md](references/components/error-handling.md) |
| Feedback indicators | [references/components/feedback-indicators.md](references/components/feedback-indicators.md) |
| Filter feedback bar | [references/components/filter-feedback-bar.md](references/components/filter-feedback-bar.md) |
| Filter form cell | [references/components/filter-form-cell.md](references/components/filter-form-cell.md) |
| Hierarchy view | [references/components/hierarchy-view.md](references/components/hierarchy-view.md) |
| Illustrated message (empty/error states) | [references/components/illustrated-message.md](references/components/illustrated-message.md) |
| Info view | [references/components/info-view.md](references/components/info-view.md) |
| Inline signature form cell | [references/components/inline-signature-form-cell.md](references/components/inline-signature-form-cell.md) |
| Inline validation | [references/components/inline-validation.md](references/components/inline-validation.md) |
| Key-value table view cell | [references/components/key-value-table-view-cell.md](references/components/key-value-table-view-cell.md) |
| KPI header / KPIItem / KPIProgressItem | [references/components/kpi-header.md](references/components/kpi-header.md) |
| KPIs (overview) | [references/components/kpis.md](references/components/kpis.md) |
| Linear progress indicator | [references/components/linear-progress-indicator.md](references/components/linear-progress-indicator.md) |
| List picker form cell | [references/components/list-picker-form-cell.md](references/components/list-picker-form-cell.md) |
| Modals | [references/components/modals.md](references/components/modals.md) |
| Multi-message handling | [references/components/multi-message-handling.md](references/components/multi-message-handling.md) |
| Navigation bar | [references/components/navigation-bar.md](references/components/navigation-bar.md) |
| Object cell (ObjectItem / list rows) | [references/components/object-cell.md](references/components/object-cell.md) |
| Object header | [references/components/object-header.md](references/components/object-header.md) |
| Offline | [references/components/offline.md](references/components/offline.md) |
| Order picker form cell | [references/components/order-picker-form-cell.md](references/components/order-picker-form-cell.md) |
| Pickers | [references/components/pickers.md](references/components/pickers.md) |
| Preview table view | [references/components/preview-table-view.md](references/components/preview-table-view.md) |
| Profile header | [references/components/profile-header.md](references/components/profile-header.md) |
| Progress & processing indicator | [references/components/progress-and-processing-indicator.md](references/components/progress-and-processing-indicator.md) |
| Rating control | [references/components/rating-control.md](references/components/rating-control.md) |
| Rating control form cell | [references/components/rating-control-form-cell.md](references/components/rating-control-form-cell.md) |
| Search bar | [references/components/search-bar.md](references/components/search-bar.md) |
| Search to select | [references/components/search-to-select.md](references/components/search-to-select.md) |
| Segmented control | [references/components/segmented-control.md](references/components/segmented-control.md) |
| Segmented control form cell | [references/components/segmented-control-form-cell.md](references/components/segmented-control-form-cell.md) |
| Sheets | [references/components/sheets.md](references/components/sheets.md) |
| Sibling navigation | [references/components/sibling-navigation.md](references/components/sibling-navigation.md) |
| Sidebar (NavigationSplitView) | [references/components/sidebar.md](references/components/sidebar.md) |
| Signature capture | [references/components/signature-capture.md](references/components/signature-capture.md) |
| Skeleton loading | [references/components/skeleton-loading.md](references/components/skeleton-loading.md) |
| Slider form cell | [references/components/slider-form-cell.md](references/components/slider-form-cell.md) |
| Standard table view cell | [references/components/standard-table-view-cell.md](references/components/standard-table-view-cell.md) |
| Status info label | [references/components/status-info-label.md](references/components/status-info-label.md) |
| Step progress indicator | [references/components/step-progress-indicator.md](references/components/step-progress-indicator.md) |
| Stepper form cell | [references/components/stepper-form-cell.md](references/components/stepper-form-cell.md) |
| Switch form cell | [references/components/switch-form-cell.md](references/components/switch-form-cell.md) |
| Tab bar | [references/components/tab-bar.md](references/components/tab-bar.md) |
| Tags | [references/components/tags.md](references/components/tags.md) |
| Text inputs (forms) | [references/components/text-inputs.md](references/components/text-inputs.md) |
| Timeline preview | [references/components/timeline-preview.md](references/components/timeline-preview.md) |
| Timeline view | [references/components/timeline-view.md](references/components/timeline-view.md) |
| Toast message | [references/components/toast-message.md](references/components/toast-message.md) |
| Toolbar | [references/components/toolbar.md](references/components/toolbar.md) |
| Widgets | [references/components/widgets.md](references/components/widgets.md) |

### Patterns — `references/patterns/`
| Topic | File |
|-------|------|
| Authentication overview | [references/patterns/authentication-overview.md](references/patterns/authentication-overview.md) |
| Barcode scanner | [references/patterns/barcode-scanner.md](references/patterns/barcode-scanner.md) |
| Basic authentication | [references/patterns/basic-authentication.md](references/patterns/basic-authentication.md) |
| Biometric authentication | [references/patterns/biometric-authentication.md](references/patterns/biometric-authentication.md) |
| Chart content table view cell | [references/patterns/chart-content-table-view-cell.md](references/patterns/chart-content-table-view-cell.md) |
| Chart types | [references/patterns/chart-types.md](references/patterns/chart-types.md) |
| Charts (FioriCharts) | [references/patterns/charts.md](references/patterns/charts.md) |
| Consent forms | [references/patterns/consent-forms.md](references/patterns/consent-forms.md) |
| Create & edit | [references/patterns/create-and-edit.md](references/patterns/create-and-edit.md) |
| Document scanner | [references/patterns/document-scanner.md](references/patterns/document-scanner.md) |
| Hierarchy | [references/patterns/hierarchy.md](references/patterns/hierarchy.md) |
| Map | [references/patterns/map.md](references/patterns/map.md) |
| Modality | [references/patterns/modality.md](references/patterns/modality.md) |
| Multi-user onboarding | [references/patterns/multi-user-onboarding.md](references/patterns/multi-user-onboarding.md) |
| Navigation | [references/patterns/navigation.md](references/patterns/navigation.md) |
| OCR scanner | [references/patterns/ocr-scanner.md](references/patterns/ocr-scanner.md) |
| QR code scanner | [references/patterns/qr-code-scanner.md](references/patterns/qr-code-scanner.md) |
| Quick sort | [references/patterns/quick-sort.md](references/patterns/quick-sort.md) |
| Rich text document | [references/patterns/rich-text-document.md](references/patterns/rich-text-document.md) |
| Search | [references/patterns/search.md](references/patterns/search.md) |
| Single-user onboarding | [references/patterns/single-user-onboarding.md](references/patterns/single-user-onboarding.md) |
| Sort & filter (form) | [references/patterns/sort-and-filter-form.md](references/patterns/sort-and-filter-form.md) |
| Sort & filter (overview) | [references/patterns/sort-and-filter-overview.md](references/patterns/sort-and-filter-overview.md) |
| What's new | [references/patterns/whats-new.md](references/patterns/whats-new.md) |

### Page Types — `references/page-types/`
| Topic | File |
|-------|------|
| List report page | [references/page-types/list-report-page.md](references/page-types/list-report-page.md) |
| Object details page | [references/page-types/object-details-page.md](references/page-types/object-details-page.md) |
| Overview page | [references/page-types/overview-page.md](references/page-types/overview-page.md) |
| Profile & settings page | [references/page-types/profile-and-settings-page.md](references/page-types/profile-and-settings-page.md) |

### Joule — `references/joule/`
| Topic | File |
|-------|------|
| Get started | [references/joule/get-started.md](references/joule/get-started.md) |
| AI handoff | [references/joule/ai-handoff.md](references/joule/ai-handoff.md) |
| What's new | [references/joule/whats-new.md](references/joule/whats-new.md) |
| Colors | [references/joule/foundations/colors.md](references/joule/foundations/colors.md) |
| Layout | [references/joule/foundations/layout.md](references/joule/foundations/layout.md) |
| Carousel | [references/joule/components/carousel.md](references/joule/components/carousel.md) |
| Illustrated message | [references/joule/components/illustrated-message.md](references/joule/components/illustrated-message.md) |
| Input field | [references/joule/components/input-field.md](references/joule/components/input-field.md) |
| Joule panel | [references/joule/components/joule-panel.md](references/joule/components/joule-panel.md) |
| Likert scale | [references/joule/components/likert-scale.md](references/joule/components/likert-scale.md) |
| List card | [references/joule/components/list-card.md](references/joule/components/list-card.md) |
| Media | [references/joule/components/media.md](references/joule/components/media.md) |
| Menu selection | [references/joule/components/menu-selection.md](references/joule/components/menu-selection.md) |
| Object card | [references/joule/components/object-card.md](references/joule/components/object-card.md) |
| Quick replies | [references/joule/components/quick-replies.md](references/joule/components/quick-replies.md) |
| Response actions | [references/joule/components/response-actions.md](references/joule/components/response-actions.md) |
| Text messages | [references/joule/components/text-messages.md](references/joule/components/text-messages.md) |
| Timestamp | [references/joule/components/timestamp.md](references/joule/components/timestamp.md) |
| AI notice | [references/joule/patterns/ai-notice.md](references/joule/patterns/ai-notice.md) |
| Attachment by prompt | [references/joule/patterns/attachment-by-prompt.md](references/joule/patterns/attachment-by-prompt.md) |
| Confirmation | [references/joule/patterns/confirmation.md](references/joule/patterns/confirmation.md) |
| Conversations list | [references/joule/patterns/conversations-list.md](references/joule/patterns/conversations-list.md) |
| Detail view | [references/joule/patterns/detail-view.md](references/joule/patterns/detail-view.md) |
| Dictation | [references/joule/patterns/dictation.md](references/joule/patterns/dictation.md) |
| Entry point | [references/joule/patterns/entry-point.md](references/joule/patterns/entry-point.md) |
| Error handling | [references/joule/patterns/error-handling.md](references/joule/patterns/error-handling.md) |
| Feedback | [references/joule/patterns/feedback.md](references/joule/patterns/feedback.md) |
| Initial loading | [references/joule/patterns/initial-loading.md](references/joule/patterns/initial-loading.md) |
| Modes | [references/joule/patterns/modes.md](references/joule/patterns/modes.md) |
| Outbound navigation | [references/joule/patterns/outbound-navigation.md](references/joule/patterns/outbound-navigation.md) |
| Persistent attachment | [references/joule/patterns/persistent-attachment.md](references/joule/patterns/persistent-attachment.md) |
| Response loading | [references/joule/patterns/response-loading.md](references/joule/patterns/response-loading.md) |
| Transparency & explainability | [references/joule/patterns/transparency-and-explainability.md](references/joule/patterns/transparency-and-explainability.md) |
| Typeahead | [references/joule/patterns/typeahead.md](references/joule/patterns/typeahead.md) |
| Welcome screen | [references/joule/patterns/welcome-screen.md](references/joule/patterns/welcome-screen.md) |

### In-App AI Design — `references/in-app-ai-design/`
| Topic | File |
|-------|------|
| Get started | [references/in-app-ai-design/get-started.md](references/in-app-ai-design/get-started.md) |
| AI UI text | [references/in-app-ai-design/foundations/ai-ui-text.md](references/in-app-ai-design/foundations/ai-ui-text.md) |
| AI buttons | [references/in-app-ai-design/components/ai-buttons.md](references/in-app-ai-design/components/ai-buttons.md) |
| AI progress indicators | [references/in-app-ai-design/components/ai-progress-indicators.md](references/in-app-ai-design/components/ai-progress-indicators.md) |
| AI acknowledgement | [references/in-app-ai-design/patterns/ai-acknowledgement.md](references/in-app-ai-design/patterns/ai-acknowledgement.md) |
| AI handoff | [references/in-app-ai-design/patterns/ai-handoff.md](references/in-app-ai-design/patterns/ai-handoff.md) |
| AI insights | [references/in-app-ai-design/patterns/ai-insights.md](references/in-app-ai-design/patterns/ai-insights.md) |
| AI notice | [references/in-app-ai-design/patterns/ai-notice.md](references/in-app-ai-design/patterns/ai-notice.md) |
| AI user feedback | [references/in-app-ai-design/patterns/ai-user-feedback.md](references/in-app-ai-design/patterns/ai-user-feedback.md) |
| AI writing assistant | [references/in-app-ai-design/patterns/ai-writing-assistant.md](references/in-app-ai-design/patterns/ai-writing-assistant.md) |

### Platform Extensions
| Topic | File |
|-------|------|
| watchOS — get started | [references/watchos/get-started.md](references/watchos/get-started.md) |
| watchOS — colors | [references/watchos/foundations/colors.md](references/watchos/foundations/colors.md) |
| watchOS — design principles | [references/watchos/foundations/design-principles.md](references/watchos/foundations/design-principles.md) |
| watchOS — layout | [references/watchos/foundations/layout.md](references/watchos/foundations/layout.md) |
| watchOS — navigation | [references/watchos/foundations/navigation.md](references/watchos/foundations/navigation.md) |
| watchOS — type system | [references/watchos/foundations/type-system.md](references/watchos/foundations/type-system.md) |
| visionOS — get started | [references/visionos/get-started.md](references/visionos/get-started.md) |
| visionOS — design principles | [references/visionos/foundations/design-principles.md](references/visionos/foundations/design-principles.md) |
| visionOS — design process & tools | [references/visionos/foundations/design-process-and-tools.md](references/visionos/foundations/design-process-and-tools.md) |
| visionOS — spatial UX design | [references/visionos/foundations/spatial-ux-design.md](references/visionos/foundations/spatial-ux-design.md) |
| visionOS — terminology | [references/visionos/foundations/terminology.md](references/visionos/foundations/terminology.md) |
| visionOS — typography | [references/visionos/foundations/typography.md](references/visionos/foundations/typography.md) |
| CarPlay — get started | [references/carplay/get-started.md](references/carplay/get-started.md) |
| CarPlay — design principles | [references/carplay/design-principles.md](references/carplay/design-principles.md) |

### Resources & Discovery
| Topic | File |
|-------|------|
| Color token quick lookup | [references/colors.md](references/colors.md) |
| UI Kit | [references/resources/ui-kit.md](references/resources/ui-kit.md) |
| Joule UI Kit | [references/resources/joule-ui-kit.md](references/resources/joule-ui-kit.md) |
| watchOS UI Kit | [references/resources/watchos-ui-kit.md](references/resources/watchos-ui-kit.md) |
| Mentor app | [references/resources/mentor-app.md](references/resources/mentor-app.md) |
| Get started | [references/discover/get-started.md](references/discover/get-started.md) |
| What's new | [references/discover/whats-new.md](references/discover/whats-new.md) |
| SAP Design System | [references/discover/sap-design-system.md](references/discover/sap-design-system.md) |
| Mobile UX consistency | [references/discover/mobile-ux-consistency.md](references/discover/mobile-ux-consistency.md) |
