# Data Table — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIDataTable`, SwiftUI `DataTable`

## What is it?

A data table is a grid of labeled columns and rows used to present numbers, text, or images. It supports horizontal scrolling with a sticky header row and optional sticky first column. On compact screens, the data table converts to a list report by default.

---

## When to Use

**Do:**
- Use when users need to **compare multiple attributes** across items in a large data set
- Use in compact screen sizes with horizontal scrolling and sticky headers enabled

**Don't:**
- Use in preview views (cards, object header, etc.)
- Use when users don't need to compare multiple attributes — use a list (`ObjectItem`) instead

---

## Anatomy

```
A. Header Row  (sticky — always visible during scroll)
┌──────────────┬───────────────┬───────────────┬───────────────┐
│ B/C. Col 1 ↕│    Column 2   │    Column 3   │    Column 4   │
├──────────────┼───────────────┼───────────────┼───────────────┤
│  Row 1 data  │               │               │               │
├──────────────┼───────────────┼───────────────┼───────────────┤
│  Row 2 data  │               │               │               │
└──────────────┴───────────────┴───────────────┴───────────────┘
 ↑ C. Persistent column (optional — sticks left during horizontal scroll)
```

### A. Header Row
Always at the top. Contains column labels. **Sticky** — remains visible during vertical scroll.

### B. Rows of Data
Each row = one data instance. Each column = one attribute of that instance.

### C. Persistent Column (optional)
The leftmost column can be set to stick to the left during horizontal scrolling, keeping row identity visible.

---

## Behavior & Interaction

### Multi-Selection (Bulk Actions)
The data table supports multi-row selection. Selected rows expose a toolbar with further actions (delete, export, approve, etc.).

```swift
DataTable(model: model)
    .onSelectionChange { selectedRows in
        selectedRows // Set<Int> of selected row indices
    }
```

### Add a Data Row
A "+" button in the navigation bar or inline cell triggers adding a new row. The added row appears following the current sort order (e.g. newest-first if sorted by timestamp). The table scrolls to the new row and briefly highlights its background, which then fades.

```swift
.toolbar {
    ToolbarItem(placement: .primaryAction) {
        FioriButton { _ in Image(systemName: "plus").accessibilityLabel("Add row") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .onTapGesture { addNewRow() }
    }
}
```

### Edit a Data Row
Two edit modes:

**Drill-down edit** — tap a row to navigate to an object detail page, edit there, save.

**In-line edit** — triggered by an "Edit" button in the navigation bar. Allows editing multiple cells without leaving the table.

In-line edit behavior:
- Tap any editable cell to begin editing — active cell shows highlighted stroke and text background
- Tap "Done" in nav bar to save and exit edit mode
- **Invalid entry** — cell highlighted red, banner with error message appears
- **Deselect invalid cell** — error remains visible with red underline, banner persists

Supported in-line edit data types: **text, duration, time, date, list picker**

**Read-only cells** — displayed with grey background. Tapping shows a `ToastMessage` indicating the cell is read-only.

```swift
// Inline edit mode toggle
@State private var isEditing = false

NavigationStack {
    DataTable(model: model, isEditing: $isEditing)
        .navigationTitle("Invoices")
        .toolbar {
            ToolbarItem(placement: .primaryAction) {
                FioriButton { _ in Text(isEditing ? "Done" : "Edit") }
                    .fioriButtonStyle(FioriTertiaryButtonStyle())
                    .onTapGesture { isEditing.toggle() }
            }
        }
}
```

---

## Adaptive Design

| Size class | Default behavior |
|-----------|-----------------|
| Regular (iPad) | Full data table with horizontal scroll |
| Compact (iPhone) | **Converted to list report** by default |

To override and show the data table on compact (with horizontal scroll):

```swift
DataTable(model: model)
    .allowsHorizontalScrolling(true)  // enable on compact
```

---

## SwiftUI Code Examples

### Basic DataTable
```swift
import FioriSwiftUICore

let model = TableModel(
    headerData: [
        DataTableItem(text: "Invoice #", textAlignment: .leading),
        DataTableItem(text: "Vendor", textAlignment: .leading),
        DataTableItem(text: "Amount", textAlignment: .trailing),
        DataTableItem(text: "Due Date", textAlignment: .center),
        DataTableItem(text: "Status", textAlignment: .center)
    ],
    rowData: invoices.map { invoice in [
        DataTableItem(text: invoice.number),
        DataTableItem(text: invoice.vendor),
        DataTableItem(text: invoice.amount, textAlignment: .trailing),
        DataTableItem(text: invoice.dueDate, textAlignment: .center),
        DataTableItem(text: invoice.status, textAlignment: .center)
    ]},
    isFirstColumnSticky: true
)

DataTable(model: model)
```

### With multi-selection and bulk actions
```swift
@State private var selectedRows: Set<Int> = []
@State private var showBulkActions = false

DataTable(model: model)
    .onSelectionChange { selected in
        selectedRows = selected
        showBulkActions = !selected.isEmpty
    }
    .toolbar {
        if showBulkActions {
            ToolbarItemGroup(placement: .bottomBar) {
                FioriButton { _ in Text("Approve (\(selectedRows.count))") }
                    .fioriButtonStyle(FioriPrimaryButtonStyle())
                FioriButton { _ in Text("Delete") }
                    .fioriButtonStyle(FioriSecondaryButtonStyle())
                    .tint(Color.preferredColor(.negativeLabel))
            }
        }
    }
```

### With sorting
```swift
DataTable(model: model)
    .allowsColumnSorting(true)
```

### Inline edit with validation
```swift
@State private var isEditing = false

DataTable(model: model, isEditing: $isEditing)
    .onCellEdit { rowIndex, columnIndex, newValue in
        // Validate
        if !isValid(newValue, for: columnIndex) {
            return .invalid(message: "Invalid value for this field")
        }
        // Apply
        updateData(row: rowIndex, column: columnIndex, value: newValue)
        return .valid
    }
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Sticky header | Yes | Default — always enabled |
| Sticky column | Yes | `isFirstColumnSticky: true` |
| Sticky column | No | `isFirstColumnSticky: false` (default) |
| Sorting | Yes | `.allowsColumnSorting(true)` |
| Multi-select | Yes | `.onSelectionChange {}` |
| Edit mode | In-line | `isEditing: $isEditing` binding |
| Edit mode | Drill-down | Navigation to detail view |
| Column alignment | Leading | `textAlignment: .leading` |
| Column alignment | Trailing | `textAlignment: .trailing` |
| Column alignment | Center | `textAlignment: .center` |
| Compact behavior | List report | Default |
| Compact behavior | Table | `.allowsHorizontalScrolling(true)` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Set `isFirstColumnSticky: true` for wide tables — keeps row identity visible during horizontal scroll
- Right-align numeric columns
- Enable multi-selection when bulk actions are available
- Show a `ToastMessage` when the user taps a read-only cell
- Show a `BannerMessage` for in-line validation errors
- Scroll to and briefly highlight newly added rows

**Don't:**
- Use data table in preview views (cards, headers)
- Use when comparison across attributes isn't needed — use a list instead
- Add more than 6–7 visible columns without considering progressive disclosure
- Truncate column header labels

---

## Related Components

- [object-cell.md](object-cell.md) — list-based alternative for compact layouts
- [filter-feedback-bar.md](filter-feedback-bar.md) — filtering data table results
- [banner.md](banner.md) — in-line edit validation errors
- [banner.md](banner.md) — read-only cell toast feedback
