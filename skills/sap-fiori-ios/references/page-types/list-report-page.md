# List Report Page — Page Type Guide

> SAP Fiori for iOS | Page Types
> Development reference: `FUIListFloorplan`, `sap.f.SemanticPage`

## What is it?

A list report displays a large list of items of the **same object type** and lets users search, sort, filter, group, and act on them. Navigate to it from an overview or object screen; tap a line item to drill down to its object page.

**Do not use** when the list contains different object types (e.g. mixed people profiles and tasks).

---

## Anatomy

```
A. Navigation Bar
   ← Back (title of prev screen)   "Tasks (100)"   [Filter] [Edit] [Add]

B. Search Bar
   [🔍 Search tasks…]

C. Filter Feedback Bar (optional)
   [Status: Open ✕] [Due: This Week ✕]

D. Content Area
   [ Object Cell ]  or  [ Data Table ]
   [ Object Cell ]
   ...

E. Toolbar (optional — overflow from nav bar)
   [Share]  [Assign]  [Export]
```

---

## Content Guidelines

### A. Navigation Bar

**Back button:** Use the previous screen's title (not "Back"). Chevron + title.

**Screen title:** `<Object Type> (<count>)` — e.g. "Tasks (100)". Count updates when filters are applied to show filtered/total (e.g. "Tasks (12 of 100)").

**Button rules:**
- Edit (if present) → right side; other buttons to its left
- No Edit → Filter on the right
- Compact: min 1, max **2** icons in nav bar; overflow to toolbar
- Regular: min 1, max **3** icons in nav bar

### B. Search Bar
Between nav bar and content. Can be always visible or hidden until the user pulls down. See [search-bar.md](../components/search-bar.md).

### C. Filter Feedback Bar (optional)
Show when:
- Frequently used filters exist (always visible for quick access)
- After filters/sort/grouping are applied (shows active filters as removable chips)

### D. Content Area

**Object cells:** All key information visible in the cell. Regular width — balance information, avoid large empty areas. Tap → drill down to object details.

**Data table:** Use when comparison of multiple attributes is needed.

**Empty state:** When filters produce no results, show appropriate placeholder/illustrated message.

### E. Toolbar (optional)
For additional list-level actions that don't fit in the nav bar. Both nav bar and toolbar buttons affect the **whole list**, not individual items.

---

## List Actions

| Action | Placement | Effect |
|--------|-----------|--------|
| **Filter** | Nav bar (right if no Edit) | Sort, group, filter the list |
| **Edit** | Nav bar (right) | Activates multi-selection for group actions (Delete, etc.) |
| **Add** | Nav bar | Adds a new item of the same type |
| **Share** | Nav bar or toolbar | Share list via email / supported channels |
| Other actions | Toolbar | Any action affecting the whole list |

---

## Line Item Actions (swipe)

Directly impact the individual item, not the whole list.

- Max **3 quick actions** via swipe
- More than 3 → include "More" button → opens action sheet
- Use text or icon+label; consistent color coding

```swift
ObjectItem { Text(invoice.number) }
    .swipeActions(edge: .trailing, allowsFullSwipe: false) {
        Button(role: .destructive) { delete(invoice) } label: {
            Label("Delete", systemImage: "trash")
        }
        Button { approve(invoice) } label: {
            Label("Approve", systemImage: "checkmark.circle")
        }
        .tint(Color.preferredColor(.positiveLabel))
    }
```

---

## Filtering Behavior

When filters/sort applied:
- Filter feedback bar appears with active filter chips
- Screen title updates: "Tasks (12 of 100)"
- Tap a chip to remove that filter

## Grouping Behavior

When grouping applied:
- Group titles + item count appear
- Does NOT change the screen title counter (only filters do)
- Filter feedback bar reflects that grouping is active

---

## Full Code Example

```swift
import FioriSwiftUICore

struct InvoiceListReport: View {
    @State private var searchQuery = ""
    @State private var showFilter = false
    @State private var isEditing = false
    @State private var selectedItems: Set<String> = []
    @State private var filterItems: [FilterFeedbackBarItem] = []

    var filteredInvoices: [Invoice] { /* filter + search logic */ }
    var title: String {
        filterItems.isEmpty
            ? "Invoices (\(allInvoices.count))"
            : "Invoices (\(filteredInvoices.count) of \(allInvoices.count))"
    }

    var body: some View {
        NavigationStack {
            VStack(spacing: 0) {
                // C. Filter feedback bar
                if !filterItems.isEmpty || isFiltered {
                    FilterFeedbackBar(items: $filterItems) { item in
                        toggleFilter(item)
                    }
                    Divider()
                }

                // D. Content area
                if filteredInvoices.isEmpty {
                    ContentUnavailableView.search(text: searchQuery)
                } else {
                    List(filteredInvoices, selection: isEditing ? $selectedItems : nil) { invoice in
                        NavigationLink(destination: InvoiceDetailView(invoice: invoice)) {
                            ObjectItem {
                                Text(invoice.number)
                            } subtitle: {
                                Text(invoice.vendor)
                            } footnote: {
                                Text("Due: \(invoice.dueDate)")
                            } status: {
                                Text(invoice.status)
                                    .foregroundStyle(invoice.isOverdue
                                        ? Color.preferredColor(.negativeLabel)
                                        : Color.preferredColor(.secondaryLabel))
                            }
                        }
                        .swipeActions(edge: .trailing) {
                            Button(role: .destructive) { delete(invoice) } label: {
                                Label("Delete", systemImage: "trash")
                            }
                            Button { approve(invoice) } label: {
                                Label("Approve", systemImage: "checkmark.circle")
                            }
                            .tint(Color.preferredColor(.positiveLabel))
                        }
                    }
                    .environment(\.editMode, isEditing ? .constant(.active) : .constant(.inactive))
                }
            }
            .navigationTitle(title)
            .navigationBarTitleDisplayMode(.large)
            .searchable(
                text: $searchQuery,
                placement: .navigationBarDrawer,
                prompt: "Search invoices"
            )
            .toolbar {
                // A. Nav bar buttons — max 2 (compact), 3 (regular)
                ToolbarItemGroup(placement: .primaryAction) {
                    // Filter (right-most when no Edit)
                    FioriButton { _ in
                        HStack(spacing: 4) {
                            Image(systemName: "line.3.horizontal.decrease.circle")
                            if activeFilterCount > 0 {
                                Text("\(activeFilterCount)")
                                    .font(.fiori(forTextStyle: .caption2))
                            }
                        }
                        .accessibilityLabel("Filter")
                    }
                    .fioriButtonStyle(FioriTertiaryButtonStyle())
                    .onTapGesture { showFilter = true }

                    // Edit
                    FioriButton { _ in Text(isEditing ? "Done" : "Edit") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { isEditing.toggle(); selectedItems.removeAll() }
                }

                ToolbarItem(placement: .navigationBarLeading) {
                    // Add (left of Edit group on some layouts)
                    if !isEditing {
                        FioriButton { _ in Image(systemName: "plus").accessibilityLabel("Add invoice") }
                            .fioriButtonStyle(FioriTertiaryButtonStyle())
                    }
                }
            }
            // E. Toolbar for group actions in edit mode
            .toolbar {
                if isEditing && !selectedItems.isEmpty {
                    ToolbarItemGroup(placement: .bottomBar) {
                        Spacer()
                        FioriButton { _ in Text("Delete (\(selectedItems.count))") }
                            .fioriButtonStyle(FioriSecondaryButtonStyle())
                            .tint(Color.preferredColor(.negativeLabel))
                    }
                }
            }
            .sheet(isPresented: $showFilter) {
                SortFilterFormView(onApply: applyFilters, onReset: resetFilters)
            }
        }
    }
}
```

---

## Navigating to Object Details

- Default: tap line item → push navigation to object detail page
- Exception: if there are no further details and the primary action is editing → open modal in edit mode

---

## Adaptive Design

- Both compact and regular width supported
- Same vertical structure across widths; cells expand horizontally
- Regular: add description field; apply readable margins (max ~672pt content width)

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use only for single object type lists
- Use previous screen's title for the Back button label
- Update the title counter when filters are applied (N of Total)
- Keep nav/toolbar actions as list-level (not item-level)
- Show illustrated message / empty state when no results match filters

**Don't:**
- Mix object types in the same list report
- Put more than 3 swipe actions per item (add "More" button instead)
- Use generic "Back" as the back button label
- Put item-specific actions in the nav bar or toolbar

---

## Related Components / Patterns

- [../components/object-cell.md](../components/object-cell.md)
- [../components/filter-feedback-bar.md](../components/filter-feedback-bar.md)
- [../components/search-bar.md](../components/search-bar.md)
- [../components/data-table.md](../components/data-table.md)
- [../patterns/sort-and-filter-form.md](../patterns/sort-and-filter-form.md)
- [object-details-page.md](object-details-page.md)
