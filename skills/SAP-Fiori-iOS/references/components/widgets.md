# Widgets — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIKPIView`, `FUIKPIUnitItem`, `FUIKPIProgressView`, `FUITimelinePreviewView`, `FUIObjectCell`, `FUIObjectCollectionViewCell`

## What is it?

Widgets display key information in a glanceable format on the user's device (home screen, lock screen, Today view). Starting with iOS 17, widgets can include interactive buttons and toggles.

---

## When to Use

**Do:**
- Use only SAP icons and SDK components for visual consistency with the app
- Use **16pt margins** for text content; **8pt margins** for images and glyphs
- Use SAP icons or SF Symbols in the header (not the app logo)
- Show the logo only if your app curates content

**Don't:**
- Put the logo in the widget header
- Repeat information or expand content just to fill medium/large widget space

---

## Anatomy

```
A. Header
   Left accessory (icon, optional) | Title | Right accessory (logo/tag/counter)
   — or — KPI | Image | Customized | Empty state | Authentication

B. Body
   Table view (object cells) | Chart card (line, bar, multi-bar)

C. Footer
   Buttons (1–2 symbols or labels) | Label

D. Background
   Default | Customized | Image
```

---

## Variations

### KPI View
Uses `KPIItem` / `KPIHeader` components. Displays numeric values (dates, amounts, counts).

### Table View
Uses `ObjectItem` components. Displays object image + headline + subtitle.

### Chart View
Uses chart card components. Line and donut charts recommended — avoid overcrowding.

---

## Behavior & Interaction

### Interactive Widgets (iOS 17+)
Buttons and toggles trigger app functionality without launching the app. On locked devices, interactions require authentication.

### Pressed State (Content)
Selecting a row or column changes its background color — immediate feedback.

### Pressed State (Button)
Button state changes to pressed on tap.

### Processing State
After a button tap, the button expands to full width, shows a circular indicator, and label changes to present-continuous tense + "…" (e.g. "Approving…").

### Success State
Auto-transitions from processing when complete — indicator becomes a success icon. List advances to the next item if more exist.

### Fail State
Processing button reverts to its default state.

### Navigation
- **Tap widget** → opens app to the corresponding page (list report, etc.)
- **Tap row/column** → opens app to the specific object's detail page

### Empty State
Show a clear message: what's happening, why, and what to do.

---

## SwiftUI Code Examples (WidgetKit)

### KPI widget
```swift
import WidgetKit
import SwiftUI
import FioriSwiftUICore

struct KPIWidgetView: View {
    let entry: KPIEntry

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            // Header
            HStack {
                Image(systemName: "chart.bar")
                    .foregroundStyle(Color.preferredColor(.tintColor))
                Text("Revenue")
                    .font(.fiori(forTextStyle: .subheadline, weight: .semibold))
                    .foregroundStyle(Color.preferredColor(.primaryLabel))
            }
            .padding(.horizontal, 16)  // 16pt text margin
            .padding(.top, 16)

            // KPI value
            VStack(alignment: .leading, spacing: 4) {
                Text("$1.4M")
                    .font(.fiori(forTextStyle: .largeKPI, weight: .light))
                    .foregroundStyle(Color.preferredColor(.primaryLabel))
                Text("Revenue YTD")
                    .font(.fiori(forTextStyle: .footnote))
                    .foregroundStyle(Color.preferredColor(.secondaryLabel))
            }
            .padding(.horizontal, 16)
            Spacer()
        }
        .widgetBackground(Color.preferredColor(.primaryBackground))
    }
}
```

### Table view widget (object cells)
```swift
struct TableWidgetView: View {
    let entry: TableEntry

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            // Header — 16pt margin
            Text("Open Orders")
                .font(.fiori(forTextStyle: .subheadline, weight: .semibold))
                .padding(.horizontal, 16)
                .padding(.vertical, 8)

            Divider()

            // Object rows
            ForEach(entry.orders.prefix(3)) { order in
                HStack(spacing: 12) {
                    // Image — 8pt margin
                    RoundedRectangle(cornerRadius: 6)
                        .fill(Color.preferredColor(.secondaryBackground))
                        .frame(width: 36, height: 36)
                        .padding(.leading, 8)

                    VStack(alignment: .leading, spacing: 2) {
                        Text(order.title)
                            .font(.fiori(forTextStyle: .footnote, weight: .semibold))
                            .lineLimit(1)
                        Text(order.subtitle)
                            .font(.fiori(forTextStyle: .caption2))
                            .foregroundStyle(Color.preferredColor(.secondaryLabel))
                            .lineLimit(1)
                    }
                    Spacer()
                }
                .padding(.vertical, 6)
                .padding(.trailing, 16)
            }
        }
    }
}
```

### Interactive approval widget (iOS 17+)
```swift
struct ApprovalWidgetView: View {
    let entry: ApprovalEntry

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text(entry.requestTitle)
                .font(.fiori(forTextStyle: .subheadline))
                .padding(.horizontal, 16)

            // Interactive buttons (iOS 17+)
            HStack {
                Button(intent: RejectIntent(id: entry.id)) {
                    Text("Reject")
                        .foregroundStyle(Color.preferredColor(.negativeLabel))
                }
                .buttonStyle(.bordered)

                Button(intent: ApproveIntent(id: entry.id)) {
                    Text("Approve")
                }
                .buttonStyle(.borderedProminent)
            }
            .padding(.horizontal, 16)
        }
    }
}
```

### Empty state
```swift
if entry.items.isEmpty {
    VStack(spacing: 8) {
        Image(systemName: "checkmark.circle")
            .font(.system(size: 32))
            .foregroundStyle(Color.preferredColor(.positiveLabel))
        Text("All caught up")
            .font(.fiori(forTextStyle: .footnote))
            .foregroundStyle(Color.preferredColor(.secondaryLabel))
        Text("No pending approvals")
            .font(.fiori(forTextStyle: .caption2))
            .foregroundStyle(Color.preferredColor(.tertiaryLabel))
    }
    .multilineTextAlignment(.center)
}
```

---

## Margin Guidelines

| Content type | Margin |
|-------------|--------|
| Text | 16pt |
| Images and glyphs | 8pt |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use SAP icons or SF Symbols in widget headers
- Apply 16pt margins for text, 8pt for images/glyphs
- Show logo only when your app curates content
- Use line and donut charts — avoid complex multi-series charts
- Provide meaningful empty states

**Don't:**
- Put the app logo in the header (unless content-curating app)
- Pad content just to fill widget space
- Use more than simple charts (line, bar, donut)

---

## Related Components

- [kpis.md](kpis.md) — KPI components used in widgets
- [object-cell.md](object-cell.md) — object cells in table view widgets
- [charts.md](charts.md) — chart types for chart view widgets
