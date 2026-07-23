# Multi-Message Handling — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Feedback
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIBannerMultiMessageViewController`, `FUIBannerMessageView`, SwiftUI `BannerMultiMessageSheet`

## What is it?

Multi-message handling provides an overview of multiple messages — showing the type and number of messages — along with an action link to open a detail view. The detail view opens as a bottom sheet on compact screens and a popover on regular screens.

---

## When to Use

**Do:**
- Use only when there is **more than one message**

**Don't:**
- Use when there is only one message — show a regular `BannerMessage` instead

**Top tips:**
- Keep the overview banner text short, concise, and informational
- Show the **total number** and **types** of messages
- Show the overview banner with icon and color of the **highest urgency** message — not lower-priority messages
- Use the optional filter only when there are multiple categories or more messages than the user can handle without one
- Customize filter categories to match user needs

---

## Anatomy

```
Overview Banner (in BannerMessage):
┌───────────────────────────────────────────────┐
│ [!] 3 messages require attention   [View All] │
└───────────────────────────────────────────────┘

Detail View (bottom sheet / popover):
┌───────────────────────────────────────────────┐
│ A. Header: "Messages (3)"           [✕ Close] │
│───────────────────────────────────────────────│
│ B. Filter (optional): [All] [Error] [Warning] │
│───────────────────────────────────────────────│
│ C. Header Cell: Errors (2)         [Clear All]│
│   D. Banner: "Invoice #1 — field X missing →" │
│   D. Banner: "Order #5 — amount invalid    →" │
│───────────────────────────────────────────────│
│ C. Header Cell: Warnings (1)       [Clear All]│
│   D. Banner: "Supplier #3 — address incomplete"│
└───────────────────────────────────────────────┘
```

### A. Header
Title, total message count, and a button to collapse the detail view.

### B. Filter (optional)
Dimension selector to filter by message type. Use only when there are multiple categories or a high message volume. The "All" option always shows all messages.

### C. Header Cell (optional)
Per-category header showing the message count and an optional "Clear" button to dismiss all messages of that type.

### D. Banner
Individual message detail. The link in the banner navigates to the screen location (table cell, form cell) related to the message.

---

## Behavior & Interaction

### Opening the Detail View
Tapping the "View All" (or similar) action link in the overview banner opens the detail view:
- **Compact** — bottom sheet modal (draggable handle to expand/minimize)
- **Regular** — popover

When the detail view opens on compact, the **overview banner automatically folds**. It reappears when the detail view is collapsed.

### Closing the Detail View
- Tap the "Close" (✕) icon in the header, OR
- Tap anywhere outside the modal or popover

### Filtering
Tap a filter chip to show only that message type. Tap "All" to show all messages. Implemented using a `DimensionSelector` (see [dimension-selector.md](dimension-selector.md)).

### Navigating to the Error
Tapping the link in a banner navigates to the exact screen location related to that message (e.g. the form field with the error).

### Clearing Messages
- **Single message** — tap its "Close" button, or swipe left (compact)
- **All of one type** — tap the "Clear" button in the category header cell

---

## Adaptive Design

| Size class | Detail view presentation |
|-----------|-------------------------|
| Compact (iPhone) | Bottom sheet — draggable to expand/minimize |
| Regular (iPad) | Popover |

---

## SwiftUI Code Examples

### Overview banner + multi-message sheet
```swift
import FioriSwiftUICore

@State private var showMultiMessageSheet = false
@State private var messages: [BannerMessage] = systemMessages

// Overview banner — shows highest-urgency icon and color
if !messages.isEmpty {
    BannerMessage {
        Text("\(messages.count) messages require attention")
    } icon: {
        // Use icon/color of highest-urgency message
        Image(systemName: "exclamationmark.triangle.fill")
            .foregroundStyle(Color.preferredColor(.negativeLabel))
    } action: {
        FioriButton { _ in Text("View All") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .onTapGesture { showMultiMessageSheet = true }
    }
    .sheet(isPresented: $showMultiMessageSheet) {
        BannerMultiMessageSheet(messages: $messages)
    }
}
```

### BannerMultiMessageSheet with filter categories
```swift
@State private var showSheet = false
@State private var messages: [FioriBannerMessage] = [
    FioriBannerMessage(
        title: "Invoice #1234 — Amount field is required",
        type: .negative,
        navigateTo: { navigateTo(.invoice("1234")) }
    ),
    FioriBannerMessage(
        title: "Order #5678 — Delivery date is in the past",
        type: .critical,
        navigateTo: { navigateTo(.order("5678")) }
    ),
    FioriBannerMessage(
        title: "Supplier #9 — Address incomplete",
        type: .critical,
        navigateTo: { navigateTo(.supplier("9")) }
    )
]

BannerMultiMessageSheet(messages: $messages)
    .presentationDetents([.medium, .large])
    .presentationDragIndicator(.visible)
```

### Adaptive presentation (sheet on compact, popover on regular)
```swift
@Environment(\.horizontalSizeClass) var hSizeClass
@State private var showMessages = false
@State private var popoverAnchor: CGRect = .zero

Button("View \(messages.count) Messages") {
    showMessages = true
}
.sheet(isPresented: $showMessages.projectedValue,
       isPresented: hSizeClass == .compact) {
    BannerMultiMessageSheet(messages: $messages)
        .presentationDetents([.medium, .large])
}
.popover(isPresented: $showMessages.projectedValue,
         isPresented: hSizeClass != .compact) {
    BannerMultiMessageSheet(messages: $messages)
        .frame(width: 375, height: 500)
}
```

### Clearing messages
```swift
// Clear single message
messages.removeAll { $0.id == messageToRemove.id }

// Clear all of one type
messages.removeAll { $0.type == .negative }

// After clearing, if only one message remains, switch to single BannerMessage
if messages.count == 1 {
    showMultiMessageSheet = false
    showSingleBanner = true
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Screen | Compact | `.sheet` with `BannerMultiMessageSheet` |
| Screen | Regular | `.popover` with `BannerMultiMessageSheet` |
| Filter | Yes | `DimensionSelector` inside sheet |
| Filter | No | Omit filter row |
| Header cell | Yes | Per-category section with clear action |
| Message type | Error | `.negativeLabel` color |
| Message type | Warning | `.criticalLabel` color |
| Message type | Info | `.informativeLabel` color |
| Overview banner | Highest urgency | Icon + color = highest severity present |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Show the highest-urgency message type's icon and color in the overview banner
- Include the total count and message types in the overview banner text
- Auto-fold the overview banner when the detail sheet opens on compact
- Add a filter only when there are multiple categories or a high volume of messages
- Allow navigation from individual banners to the related screen location
- Switch back to a single `BannerMessage` when only one message remains

**Don't:**
- Use multi-message handling for a single message
- Show lower-priority message styling in the overview banner if higher-priority messages exist
- Add a filter when all messages are the same type
- Overuse filter categories — only add ones that match actual user mental models

---

## Related Components

- [banner.md](banner.md) — single-message banner (used for overview and individual messages)
- [dimension-selector.md](dimension-selector.md) — filter bar inside the detail view
- [illustrated-message.md](illustrated-message.md) — empty state when all messages are cleared
