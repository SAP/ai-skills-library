# Filter Form Cell — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIFilterFormCell`, SwiftUI `FilterFormView`

## What is it?

A filter form cell is used to filter one or more values under a filter category. It presents a label and a row of tappable filter buttons. Commonly used in the filter pattern for sorting and grouping.

---

## When to Use

**Do:**
- Use for **short text** filter values
- Use when the number of values is **fewer than 8**

**Don't:**
- Use when text is too long or there are **8 or more values** — use a list picker instead for easier interaction

---

## Anatomy

```
A. Label: "Status"
B. [ Open ] [ Closed ] [ In Review ] [ Pending ]
```

**A. Label** — describes the filter or sort category.

**B. Filter Buttons** — the selectable options. Selected state shows a blue checkmark highlight.

---

## Behavior & Interaction

- Tap a button to select → button highlights with a blue checkmark
- Tap again to deselect
- Supports **single selection** and **multi-selection** depending on the use case
- Can start with a default selection or all buttons unselected

---

## Adaptive Design

- Supported in both compact and regular widths
- On iPad, filter form cells may appear inside a **popover modal**

---

## Variations

### Single Selection
Only one value can be selected at a time within the category (e.g. sort order: Ascending / Descending).

### Multi-Selection
Multiple values can be selected simultaneously (e.g. status: Open, In Review, Pending).

---

## SwiftUI Code Examples

### Single selection filter
```swift
import FioriSwiftUICore

@State private var selectedStatus: String? = nil
let statusOptions = ["Open", "In Review", "Closed"]

FilterFormView(
    title: { Text("Status") },
    options: statusOptions.map { AttributedString($0) },
    selectedIndices: Binding(
        get: { selectedStatus.flatMap { statusOptions.firstIndex(of: $0) }.map { [$0] } ?? [] },
        set: { indices in selectedStatus = indices.first.map { statusOptions[$0] } }
    ),
    allowsMultipleSelection: false
)
```

### Multi-selection filter
```swift
@State private var selectedPriorities: Set<Int> = []
let priorityOptions = ["Low", "Medium", "High", "Critical"]

FilterFormView(
    title: { Text("Priority") },
    options: priorityOptions.map { AttributedString($0) },
    selectedIndices: Binding(
        get: { Array(selectedPriorities) },
        set: { selectedPriorities = Set($0) }
    ),
    allowsMultipleSelection: true
)
```

### With default selection
```swift
// Start with "Open" pre-selected
@State private var selectedIndices: [Int] = [0]

FilterFormView(
    title: { Text("Status") },
    options: ["Open", "In Review", "Closed"].map { AttributedString($0) },
    selectedIndices: $selectedIndices,
    allowsMultipleSelection: false
)
```

### Inside a filter sheet (full pattern)
```swift
NavigationStack {
    Form {
        Section {
            FilterFormView(
                title: { Text("Status") },
                options: ["Open", "In Review", "Closed", "Rejected"].map { AttributedString($0) },
                selectedIndices: $selectedStatusIndices,
                allowsMultipleSelection: true
            )
        }

        Section {
            FilterFormView(
                title: { Text("Priority") },
                options: ["Low", "Medium", "High"].map { AttributedString($0) },
                selectedIndices: $selectedPriorityIndices,
                allowsMultipleSelection: false
            )
        }
    }
    .navigationTitle("Filter")
    .navigationBarTitleDisplayMode(.inline)
    .toolbar {
        ToolbarItem(placement: .cancellationAction) {
            FioriButton { _ in Text("Cancel") }
                .fioriButtonStyle(FioriTertiaryButtonStyle())
                .onTapGesture { dismiss() }
        }
        ToolbarItem(placement: .destructiveAction) {
            FioriButton { _ in Text("Reset") }
                .fioriButtonStyle(FioriTertiaryButtonStyle())
                .onTapGesture { resetFilters() }
        }
    }
    .safeAreaInset(edge: .bottom) {
        FioriButton { _ in Text("Apply") }
            .fioriButtonStyle(FioriPrimaryButtonStyle())
            .frame(maxWidth: .infinity)
            .padding(16)
            .background(.regularMaterial)
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Selection | Single | `allowsMultipleSelection: false` |
| Selection | Multi | `allowsMultipleSelection: true` |
| Default | Selected | `selectedIndices` pre-populated |
| Default | All unselected | `selectedIndices: []` |
| Value count | < 8 | `FilterFormView` |
| Value count | ≥ 8 | Use `ListPickerItem` instead |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Keep option labels short — they must fit as buttons on a single row
- Use single selection for mutually exclusive options (sort direction, time range)
- Use multi-selection when multiple values in a category can apply simultaneously
- Switch to a list picker when there are 8 or more values

**Don't:**
- Use for long option labels — they won't fit in the button layout
- Use when there are 8 or more options — use `ListPickerItem` instead
- Use as a navigation control — this is a filter/selection input only

---

## Related Components

- [filter-feedback-bar.md](filter-feedback-bar.md) — displays active filters above a list
- [forms.md](forms.md) — other form input cells
