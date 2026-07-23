# Order Picker Form Cell — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIOrderPickerFormCell`

## What is it?

Order picker form cells are used for sorting with multiple criteria where **both the sort direction and the sequence (priority) of criteria matter**. Each criterion can be independently toggled, reordered, and given a sort direction.

---

## Anatomy

```
A. Header: "Sort By"
──────────────────────────────────────────────────────
B. ✓ Due Date        Ascending ↕   ⠿   ← highest priority
C. ✓ Vendor Name     Descending ↕  ⠿
C.   Amount                        ⠿   ← unchecked = inactive
C.   Status                        ⠿   ← lowest priority
──────────────────────────────────────────────────────
```

### A. Order Picker Header
Contains the form label.

### B. Criterion Cell (higher priority)
The topmost cell is the highest priority in the sort sequence.

### C. Criterion Cell (lower priority)
Cells lower in the list have lower sort priority. Each criterion cell contains a label; selected criteria also show a checkmark.

### D. Order Direction Label
Shows the current sort direction for that criterion (e.g. Ascending / Descending). Tapping it toggles the direction.

### E. Drag Handle (⠿)
Dragging moves the criterion cell to reorder priority.

---

## Touch Areas — Three Distinct Zones

| Zone | Tap target | Action |
|------|-----------|--------|
| Left area (label → direction label or drag handle) | Wide row area | Toggles checkmark (select/deselect criterion) |
| Direction label word | Small tap area | Toggles sort direction (Ascending ↔ Descending) |
| Drag handle icon | Handle area | Drag to reorder criteria |

---

## Behavior

### Text Wrapping
By default text is **truncated**. The component can be configured to **wrap all text** when labels are long.

### Selection
- Tapping the main row area toggles the criterion on/off (checkmark)
- An unchecked criterion is inactive — it has no effect on sorting
- Tapping the direction label toggles Ascending ↔ Descending independently for each criterion

### Reordering
Drag the handle (⠿) to move a criterion up or down, changing its priority in the sort sequence. The topmost selected criterion is the primary sort key.

### Priority
Sort is applied top-to-bottom among checked criteria. Unchecked criteria are ignored.

---

## Presentation / Modality

Order picker form cells can be used in:
- **Form panel** — inline within a form or settings sheet
- **Bottom sheet** — presented as a resizable modal

In both compact and regular widths, the order picker is placed in **its own section**, separate from other form cells.

---

## SwiftUI Code Examples

### Basic order picker
```swift
import FioriSwiftUICore

struct SortCriterion: Identifiable {
    let id: String
    var label: String
    var isSelected: Bool
    var isAscending: Bool
}

@State private var criteria: [SortCriterion] = [
    SortCriterion(id: "dueDate",    label: "Due Date",     isSelected: true,  isAscending: true),
    SortCriterion(id: "vendor",     label: "Vendor Name",  isSelected: true,  isAscending: false),
    SortCriterion(id: "amount",     label: "Amount",       isSelected: false, isAscending: true),
    SortCriterion(id: "status",     label: "Status",       isSelected: false, isAscending: true)
]

Form {
    Section("Sort By") {
        ForEach($criteria) { $criterion in
            HStack {
                // Toggle checkmark — main row tap area
                Button {
                    criterion.isSelected.toggle()
                } label: {
                    HStack {
                        Image(systemName: criterion.isSelected
                              ? "checkmark" : "")
                            .foregroundStyle(Color.preferredColor(.tintColor))
                            .frame(width: 20)

                        Text(criterion.label)
                            .font(.fiori(forTextStyle: .body))
                            .foregroundStyle(Color.preferredColor(.primaryLabel))
                            .lineLimit(1)  // truncated by default

                        Spacer()
                    }
                }
                .buttonStyle(.plain)

                // Direction toggle — separate tap area
                if criterion.isSelected {
                    Button {
                        criterion.isAscending.toggle()
                    } label: {
                        Text(criterion.isAscending ? "Ascending" : "Descending")
                            .font(.fiori(forTextStyle: .subheadline))
                            .foregroundStyle(Color.preferredColor(.tintColor))
                    }
                    .buttonStyle(.plain)
                }

                // Drag handle
                Image(systemName: "line.3.horizontal")
                    .foregroundStyle(Color.preferredColor(.tertiaryLabel))
                    .padding(.leading, 8)
            }
            .padding(.vertical, 4)
        }
        .onMove { from, to in
            criteria.move(fromOffsets: from, toOffset: to)
        }
    }
}
.environment(\.editMode, .constant(.active))  // enables drag reorder
```

### In a bottom sheet (sort filter pattern)
```swift
@State private var showSortSheet = false
@State private var criteria = defaultCriteria

FioriButton { _ in
    Label("Sort", systemImage: "arrow.up.arrow.down")
}
.fioriButtonStyle(FioriTertiaryButtonStyle())
.onTapGesture { showSortSheet = true }
.sheet(isPresented: $showSortSheet) {
    NavigationStack {
        Form {
            // Order picker in its own section
            Section("Sort By") {
                ForEach($criteria) { $criterion in
                    OrderCriterionRow(criterion: $criterion)
                }
                .onMove { from, to in
                    criteria.move(fromOffsets: from, toOffset: to)
                }
            }
        }
        .environment(\.editMode, .constant(.active))
        .navigationTitle("Sort")
        .navigationBarTitleDisplayMode(.inline)
        .toolbar {
            ToolbarItem(placement: .cancellationAction) {
                FioriButton { _ in Text("Cancel") }
                    .fioriButtonStyle(FioriTertiaryButtonStyle())
                    .onTapGesture {
                        criteria = defaultCriteria  // discard
                        showSortSheet = false
                    }
            }
            ToolbarItem(placement: .confirmationAction) {
                FioriButton { _ in Text("Apply") }
                    .fioriButtonStyle(FioriTertiaryButtonStyle())
                    .onTapGesture {
                        applySort(criteria)
                        showSortSheet = false
                    }
            }
        }
    }
    .presentationDetents([.medium, .large])
    .presentationDragIndicator(.visible)
}
```

### With text wrapping enabled
```swift
ForEach($criteria) { $criterion in
    HStack {
        Text(criterion.label)
            .font(.fiori(forTextStyle: .body))
            .lineLimit(nil)  // wrap instead of truncate
            .fixedSize(horizontal: false, vertical: true)
        // ...
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Criterion state | Selected (✓) | `isSelected: true` |
| Criterion state | Unselected | `isSelected: false` — no checkmark, no direction label |
| Direction | Ascending | `isAscending: true` |
| Direction | Descending | `isAscending: false` |
| Text | Truncated (default) | `.lineLimit(1)` |
| Text | Wrapped | `.lineLimit(nil)` |
| Container | Form panel | Inline `Form` section |
| Container | Bottom sheet | `.sheet` + `.presentationDetents([.medium, .large])` |
| Priority | Higher | Top position in list |
| Priority | Lower | Lower position in list |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Place in its own `Section` — separate from other form cells
- Apply sort top-to-bottom among checked criteria only
- Keep labels short by default — truncation is the default behavior
- Allow text wrapping when criterion labels are long and truncation would lose meaning
- Always provide "Cancel" and "Apply" when used in a sheet

**Don't:**
- Use for single-criterion sorting — use a simpler sort button or segmented control
- Mix order picker rows with other form cell types in the same section
- Apply sort order immediately on change — wait for explicit "Apply"

---

## Related Components

- [filter-feedback-bar.md](filter-feedback-bar.md) — displaying the active sort in the feedback bar
- [list-picker-form-cell.md](list-picker-form-cell.md) — selecting values to filter by
- [forms.md](forms.md) — other form input cells
