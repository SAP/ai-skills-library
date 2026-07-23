# Segmented Control Form Cell — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUISegmentedControlFormCell`, SwiftUI `SegmentedControlPicker`

## What is it?

A segmented control form cell allows a user to quickly select from a small set of values. Used in create/edit patterns and occasionally in filter patterns. For more than 3 values or long labels, use a list picker or filter form cell instead.

---

## When to Use

**Do:**
- Use when value texts are **short and concise**
- Use for 2–3 mutually exclusive or multi-select values in a form context

**Don't:**
- Use if values are long and would need truncation — use list picker or filter form cell instead
- Use for more than 3 values — switch to list picker or filter form cell

**Strongly recommended:** Always have a **default selection** — it signals to the user that the buttons are tappable.

---

## Anatomy

```
A. Label          B. Buttons
"Priority"    [ Low ] [ Medium ] [ High ]    ← single-line buttons

— or —

"Priority"                                   ← stacked
[ Low ] [ Medium ] [ High ]
```

**A. Label** — describes the selection's intent.
**B. Buttons** — selected / unselected state. Highly recommended to have a default selection.

---

## Variations

Four variations based on two axes: **layout** (single-line vs. stacked) and **control type** (buttons vs. segmented):

| Variation | Layout | Selection | Use when |
|-----------|--------|-----------|---------|
| Single-line buttons | Label + buttons on same line | Single or multi | Values are short |
| Stacked buttons | Label above, buttons below | Single or multi | Values are too long for single-line |
| Single-line segmented | Label + segmented on same line | Single only | Mutually exclusive, short labels |
| Stacked segmented | Label above, segmented below | Single only | Mutually exclusive, longer labels |

**Buttons** support single and multi-selection.
**Segmented** is always **single selection / mutually exclusive** only.

---

## Adaptive Design

On regular width (iPad), the segmented control form cell may appear in a form sheet, popover, or full-screen modal.

---

## SwiftUI Code Examples

### Single-line segmented (single selection — mutually exclusive)
```swift
import FioriSwiftUICore

@State private var selectedPriority = 0
let priorities = ["Low", "Medium", "High"]

SegmentedControlPicker(
    title: { Text("Priority") },
    selectedIndex: $selectedPriority,
    segmentTitles: priorities
)
```

### Stacked segmented (longer labels, single selection)
```swift
@State private var selectedApprovalType = 0
let approvalTypes = ["Automatic", "Manual Review", "Requires Escalation"]

SegmentedControlPicker(
    title: { Text("Approval Type") },
    selectedIndex: $selectedApprovalType,
    segmentTitles: approvalTypes,
    isStacked: true  // label above, segmented control below
)
```

### Button variation with multi-selection
```swift
@State private var selectedDays: Set<Int> = [1]  // default: Monday
let weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]

SegmentedControlPicker(
    title: { Text("Repeat On") },
    selectedIndices: $selectedDays,
    segmentTitles: weekdays,
    allowsMultipleSelection: true
)
```

### With default selection (always recommended)
```swift
// ✅ Pre-select a value so user knows buttons are tappable
@State private var selectedStatus = 0  // default: "Active"
let statuses = ["Active", "Inactive", "Archived"]

SegmentedControlPicker(
    title: { Text("Status") },
    selectedIndex: $selectedStatus,
    segmentTitles: statuses
)

// ❌ No default — user may not realize the control is interactive
@State private var selectedStatus: Int? = nil
```

### Inside a form
```swift
Form {
    Section("Invoice Details") {
        TextFieldFormView(title: { Text("Vendor") }, text: $vendor)

        // Segmented — mutually exclusive, single selection
        SegmentedControlPicker(
            title: { Text("Payment Method") },
            selectedIndex: $paymentMethodIndex,
            segmentTitles: ["Bank Transfer", "Credit Card", "Check"]
        )

        // Stacked buttons — multi-selection
        SegmentedControlPicker(
            title: { Text("Notification") },
            selectedIndices: $notificationOptions,
            segmentTitles: ["Email", "SMS", "Push"],
            allowsMultipleSelection: true,
            isStacked: true
        )
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Variation | Single-line buttons | Default layout, `allowsMultipleSelection` optional |
| Variation | Stacked buttons | `isStacked: true`, `allowsMultipleSelection` optional |
| Variation | Single-line segmented | Default layout, `allowsMultipleSelection: false` (default) |
| Variation | Stacked segmented | `isStacked: true`, `allowsMultipleSelection: false` |
| Selection | Single | `selectedIndex: $int` binding |
| Selection | Multi | `selectedIndices: $set` binding + `allowsMultipleSelection: true` |
| Default | Yes (recommended) | Pre-populate `selectedIndex` / `selectedIndices` |
| Default | None | `selectedIndex` starts at `-1` or `nil` (avoid) |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Always provide a default selection — it signals interactivity
- Use stacked variation when labels are too long for a single line (never truncate)
- Use buttons for multi-selection; use segmented only for single/mutually-exclusive selection
- Switch to list picker or filter form cell when there are more than 3 values or labels are long

**Don't:**
- Truncate button or segment labels — use stacked layout or a different component instead
- Use segmented variation for multi-selection — it only supports single selection
- Leave all buttons unselected without a clear reason

---

## Related Components

- [filter-form-cell.md](filter-form-cell.md) — alternative for up to 8 options in a filter context
- [list-picker-form-cell.md](list-picker-form-cell.md) — alternative for more than 8 options or long labels
- [forms.md](forms.md) — other form input cells
