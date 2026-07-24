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

## Reference Files

| File | Contents |
|------|----------|
| [references/foundations/colors.md](references/foundations/colors.md) | All color tokens — Light / Dark / Elevated / Contrast |
| [references/foundations/typography.md](references/foundations/typography.md) | SAP 72 font styles and weights |
| [references/foundations/theming.md](references/foundations/theming.md) | FioriTheme setup and customization |
| [references/foundations/accessibility.md](references/foundations/accessibility.md) | WCAG, VoiceOver, Dynamic Type |
| [references/foundations/adaptive-layout.md](references/foundations/adaptive-layout.md) | iPad, size classes, split view |
| [references/foundations/elevation.md](references/foundations/elevation.md) | Shadows and visual hierarchy |
| [references/foundations/design-tokens.md](references/foundations/design-tokens.md) | Token hierarchy explained |
| [references/foundations/iconography.md](references/foundations/iconography.md) | SF Symbols + SAP icons |
| [references/components/buttons.md](references/components/buttons.md) | FioriButton all variants |
| [references/components/navigation-bar.md](references/components/navigation-bar.md) | NavigationStack, toolbar |
| [references/components/tab-bar.md](references/components/tab-bar.md) | TabView patterns |
| [references/components/sidebar.md](references/components/sidebar.md) | NavigationSplitView |
| [references/components/cards.md](references/components/cards.md) | Card components |
| [references/components/object-cell.md](references/components/object-cell.md) | ObjectItem / list rows |
| [references/components/object-header.md](references/components/object-header.md) | Detail screen header |
| [references/components/text-inputs.md](references/components/text-inputs.md) | Form input components |
| [references/components/calendar.md](references/components/calendar.md) | Calendar — month, week, expandable, date selection |
| [references/components/data-table.md](references/components/data-table.md) | DataTable |
| [references/components/kpi-header.md](references/components/kpi-header.md) | KPIItem, KPIProgressItem, KPIHeader |
| [references/patterns/charts.md](references/patterns/charts.md) | All FioriCharts types |
| [references/components/contact-cell.md](references/components/contact-cell.md) | ContactItem |
| [references/components/profile-header.md](references/components/profile-header.md) | ProfileHeader |
| [references/components/timeline-view.md](references/components/timeline-view.md) | TimelineItem, TimelineMarker |
| [references/components/step-progress-indicator.md](references/components/step-progress-indicator.md) | StepProgressIndicator |
| [references/components/banner.md](references/components/banner.md) | BannerMessage, ToastMessage |
| [references/components/illustrated-message.md](references/components/illustrated-message.md) | Empty / error states |
| [references/components/activity-indicator.md](references/components/activity-indicator.md) | Loading, skeleton, progress |
| [references/components/rating-control.md](references/components/rating-control.md) | RatingControl |
| [references/components/avatars.md](references/components/avatars.md) | Avatars, AvatarStack |
| [references/components/filter-feedback-bar.md](references/components/filter-feedback-bar.md) | FilterFeedbackBar, SortFilter |
| [references/components/signature-capture.md](references/components/signature-capture.md) | SignatureView |
| [references/patterns/single-user-onboarding.md](references/patterns/single-user-onboarding.md) | WelcomeScreen, ActivationScreen, EULA, Consent |
| [references/colors.md](references/colors.md) | Quick color token lookup |
