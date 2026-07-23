# Dimension Selector — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIDimensionSelector`, SwiftUI `DimensionSelector`

## What is it?

A dimension selector is a horizontal bar of two or more mutually exclusive buttons. It allows users to switch between different measures, views, or chart ranges. Only one item can be active at a time; tapping an active item deselects it.

---

## When to Use

**Do:**
- Use for switching between views or charts (e.g. chart time range: Day / Week / Month / Year)
- Place in a chart, navigation bar, modal, or popover
- Ensure all dimensions are related to each other

**Don't:**
- Use when dimensions are unrelated
- Use to narrow or filter a list — use `FilterFeedbackBar` / `SortFilter` instead
- Use more than one dimension selector on the same screen

---

## Anatomy

```
[ Inactive ] [ Active ] [ Inactive ] [ Inactive ]
```

**A. Inactive selector item** — at least one must exist
**B. Active selector item** — exactly one active at a time; tapping an active item deselects it

---

## Adaptive Design

| Size class | Max recommended buttons |
|-----------|------------------------|
| Compact (iPhone) | 5 |
| Regular (iPad) | 7 |

Wider buttons are easier to tap — keep the count within these limits.

---

## SwiftUI Code Examples

### Basic dimension selector
```swift
import FioriSwiftUICore

@State private var selectedIndex = 0
let dimensions = ["Day", "Week", "Month", "Quarter", "Year"]

DimensionSelector(
    selectedIndex: $selectedIndex,
    titles: dimensions
)
```

### Chart time range filter (typical use case)
```swift
@State private var selectedRange = 0
let ranges = ["1W", "1M", "3M", "6M", "1Y"]

VStack(spacing: 12) {
    DimensionSelector(
        selectedIndex: $selectedRange,
        titles: ranges
    )
    .padding(.horizontal, 16)

    ChartView(model: chartModel(for: ranges[selectedRange]))
        .frame(height: 220)
}
```

### In a navigation bar
```swift
NavigationStack {
    RevenueChartView(dimension: dimensions[selectedIndex])
        .navigationTitle("Revenue")
        .toolbar {
            ToolbarItem(placement: .principal) {
                DimensionSelector(
                    selectedIndex: $selectedIndex,
                    titles: ["Month", "Quarter", "Year"]
                )
                .frame(maxWidth: 280)
            }
        }
}
```

### View switcher (non-chart use case)
```swift
@State private var viewMode = 0

VStack(spacing: 0) {
    DimensionSelector(
        selectedIndex: $viewMode,
        titles: ["Map", "List", "Calendar"]
    )
    .padding(16)

    Divider()

    switch viewMode {
    case 0: MapView()
    case 1: ListReportView()
    default: CalendarView(selection: $selectedDate, calendar: .current)
    }
}
```

### Deselectable behavior
```swift
// Tapping the active item deselects it (selectedIndex becomes nil)
@State private var selectedIndex: Int? = 0

DimensionSelector(
    selectedIndex: $selectedIndex,
    titles: dimensions
)
// When nil, show default / unfiltered content
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Items | 2–5 (compact) | `titles` array, max 5 |
| Items | 2–7 (regular) | `titles` array, max 7 |
| State / Item | Active | `selectedIndex` matches item index |
| State / Item | Inactive | All other indices |
| Placement | Below nav bar | `VStack` with chart/content below |
| Placement | In nav bar | `ToolbarItem(placement: .principal)` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Keep all dimensions semantically related (e.g. all time ranges, all view modes)
- Respect the max button counts: 5 compact / 7 regular
- Respond to selection immediately — update chart or view on tap
- Place only one dimension selector per screen

**Don't:**
- Use as a filter for narrowing lists — use `FilterFeedbackBar` instead
- Mix unrelated options in the same selector
- Place two dimension selectors on the same screen

---

## Related Components

- [filter-feedback-bar.md](filter-feedback-bar.md) — list filtering
- [charts.md](../patterns/charts.md) — chart views paired with dimension selectors
