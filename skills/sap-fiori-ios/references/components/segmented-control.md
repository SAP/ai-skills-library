# Segmented Control — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUISegmentedControl`, SwiftUI `SegmentedControlPicker`

## What is it?

A segmented control is a horizontal bar of two or more mutually exclusive buttons that gives users quick access to specific categories of content. Used for switching between views — not for filtering lists.

---

## When to Use

**Do:**
- Use to switch between views (e.g. map vs. list, day vs. week vs. month)
- Use in a navigation bar, modal, popover, or drawer

**Don't:**
- Use when segments are unrelated to each other
- Use to narrow or filter a list — use a filter instead
- Place more than one segmented control on the same screen

---

## Anatomy

```
[ A. Inactive ] [ B. Active ] [ A. Inactive ]
```

**A. Inactive item** — at least one in the control.
**B. Active item** — exactly one active at a time.

---

## Adaptive Design

Maximum button count depends on presence of a navigation bar title:

| Context | Max buttons |
|---------|------------|
| Compact — with nav title | 5 |
| Compact — without nav title | 4 |
| Regular — with nav title | 5 |

---

## SwiftUI Code Examples

### In a navigation bar (standard placement)
```swift
import FioriSwiftUICore

@State private var selectedSegment = 0

NavigationStack {
    contentView(for: selectedSegment)
        .navigationTitle("Assets")
        .toolbar {
            ToolbarItem(placement: .principal) {
                SegmentedControlPicker(
                    selectedIndex: $selectedSegment,
                    segmentTitles: ["Map", "List", "Grid"]
                )
                .frame(maxWidth: 280)
            }
        }
}
```

### Standalone (modal or popover)
```swift
SegmentedControlPicker(
    selectedIndex: $selectedMode,
    segmentTitles: ["Day", "Week", "Month"]
)
.padding(.horizontal, 16)
```

### Respect max button count
```swift
// ✅ Compact with nav title — max 5
SegmentedControlPicker(
    selectedIndex: $idx,
    segmentTitles: ["A", "B", "C", "D", "E"]
)

// ✅ Compact without nav title — max 4
SegmentedControlPicker(
    selectedIndex: $idx,
    segmentTitles: ["Open", "In Review", "Closed", "All"]
)
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Item | Active | `selectedIndex` matches item index |
| Item | Inactive | All other indices |
| Placement | Nav bar | `ToolbarItem(placement: .principal)` |
| Placement | Modal / popover | Standalone in VStack |
| Max segments | Compact + title | 5 |
| Max segments | Compact, no title | 4 |
| Max segments | Regular + title | 5 |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Keep all segments semantically related
- Use in nav bar, modal, popover, or drawer
- Respect the max button counts per size class and title context
- Use only one segmented control per screen

**Don't:**
- Use to filter a list — use `FilterFeedbackBar` instead
- Mix unrelated segments
- Exceed the maximum segment count

---

## Related Components

- [segmented-control-form-cell.md](segmented-control-form-cell.md) — segmented control inside a form cell
- [dimension-selector.md](dimension-selector.md) — similar pattern for chart/view switching
- [filter-feedback-bar.md](filter-feedback-bar.md) — list filtering
