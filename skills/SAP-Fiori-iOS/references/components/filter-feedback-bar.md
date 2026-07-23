# Filter Feedback Bar — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIFilterFeedbackControl`, SwiftUI `FilterFeedbackBar`

## What is it?

The filter feedback bar is a horizontal scrollable bar that appears above a list of content. It uses interactive buttons to communicate which filters are currently applied and allows users to quickly apply frequently used filters. Typically used in list report or work list floorplans.

---

## When to Use

**Do:**
- Use when there are frequently used filter options that benefit from one-tap access

**Don't:**
- Use when there are many filters or filters with complex names — show the count as feedback in a filter button instead

---

## Anatomy

The filter feedback bar sits:
1. Below the navigation bar
2. Below the search bar (if present)
3. Directly above the content area

```
NavBar
──────────────────────────────────────────
SearchBar (if present)
──────────────────────────────────────────
[Sort ▼] [● Active Filter] [Inactive] [Inactive] →   ← Filter Feedback Bar
──────────────────────────────────────────
List content
```

### Filter Button Types

**A. Active Filter Buttons**
Currently selected filters (and non-default sort). Always placed **left of inactive filter buttons**.

**B. Inactive Filter Buttons**
Unselected fast filters. Remain visible in the bar. Users cannot customize which buttons appear — the app defines them.

### Filter Sheet

Opens when a filter button with a downward chevron is tapped. Used for complex filter interactions.

| Part | Contents |
|------|----------|
| A. Navigation Bar | Sheet-level controls: "Cancel" and "Reset" |
| B. Component Area | Filter form cells, sliders, calendars, etc. |
| C. Toolbar | "Apply" button — always visible, even when scrolled |

---

## Button Variants

Four filter button types — must be used consistently across the entire bar:

| Type | When to use |
|------|-------------|
| Default button | Standard filter, no icon |
| Default button + chevron (▾) | Standard filter that opens a filter sheet |
| Descriptive icon button | Filter with a recognizable icon |
| Descriptive icon button + chevron (▾) | Icon filter that opens a filter sheet |

**Consistency rule:** If any button in the bar uses a descriptive icon, **all** buttons must use descriptive icons. Default and icon buttons cannot be mixed in the same bar.

---

## Behavior & Interaction

### Horizontal Scrolling
Users scroll the bar horizontally to reveal off-screen buttons. If a sort button is present, filter buttons slide beneath it when scrolling.

### Applying Fast Filters
Tap an inactive filter button → filter is applied to the list → button becomes active. Active buttons move to the left.

### Removing Filters
- Tap an active button → deselects and removes the filter
- From a filter sheet: tap "Reset" then "Apply"
- **Fast filter buttons remain in the bar even when inactive**
- Filters applied from the filter modal (not originally in the bar) **disappear from the bar when deactivated**

### Filter Sheet (complex filters)
Tap any button with a chevron (▾) → bottom sheet appears with a richer filter interface (form cells, sliders, calendar, etc.). Tap "Apply" in the toolbar to apply; "Reset" to clear; "Cancel" to dismiss without changes.

### Filter Modal
Filters applied from the full filter modal appear as **active buttons on the left side** of the bar (right of sort, if present), and disappear when deactivated.

---

## Variations

### Filter Feedback Bar with Predefined Buttons
Buttons are always visible — active or inactive. Defined by the app, not customizable by users. Shows the most frequently used filters for fast access.

### Filter Feedback Bar without Predefined Buttons
Hidden by default. Only appears after the user:
- Applies a filter from the filter modal, OR
- Changes the sort option (non-default sort only — the **default sort never appears**)

---

## SwiftUI Code Examples

### Basic FilterFeedbackBar
```swift
import FioriSwiftUICore

@State private var filterItems: [FilterFeedbackBarItem] = [
    FilterFeedbackBarItem(
        title: AttributedString("Status"),
        isSelected: false
    ),
    FilterFeedbackBarItem(
        title: AttributedString("Open"),
        isSelected: true  // active — shown left
    ),
    FilterFeedbackBarItem(
        title: AttributedString("High Priority"),
        isSelected: true
    ),
    FilterFeedbackBarItem(
        title: AttributedString("Due This Week"),
        isSelected: false
    )
]

FilterFeedbackBar(items: $filterItems) { tappedItem in
    if tappedItem.isSelected {
        // Deactivate
        if let index = filterItems.firstIndex(where: { $0.id == tappedItem.id }) {
            filterItems[index].isSelected = false
        }
        removeFilter(tappedItem)
    } else {
        // Activate
        if let index = filterItems.firstIndex(where: { $0.id == tappedItem.id }) {
            filterItems[index].isSelected = true
        }
        applyFilter(tappedItem)
    }
}
```

### With sort button
```swift
@State private var sortItem = FilterFeedbackBarItem(
    title: AttributedString("Due Date ↑"),
    isSelected: true,  // non-default sort — shown active
    accessoryIcon: Image(systemName: "arrow.up")
)

// Sort button always appears leftmost
var allItems: [FilterFeedbackBarItem] {
    var items = filterItems
    if sortItem.isSelected {
        items.insert(sortItem, at: 0)
    }
    return items
}

FilterFeedbackBar(items: .constant(allItems)) { tappedItem in
    handleTap(tappedItem)
}
```

### Button with chevron → opens filter sheet
```swift
@State private var showDateFilterSheet = false

FilterFeedbackBar(items: $filterItems) { tappedItem in
    if tappedItem.title == AttributedString("Due Date") {
        showDateFilterSheet = true  // open sheet for complex filter
    } else {
        toggleFilter(tappedItem)
    }
}
.sheet(isPresented: $showDateFilterSheet) {
    NavigationStack {
        DateRangeFilterSheet(selection: $dateRange)
            .navigationTitle("Due Date")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    FioriButton { _ in Text("Cancel") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { showDateFilterSheet = false }
                }
                ToolbarItem(placement: .destructiveAction) {
                    FioriButton { _ in Text("Reset") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { resetDateFilter() }
                }
            }
    }
    .safeAreaInset(edge: .bottom) {
        // Toolbar always visible
        FioriButton { _ in Text("Apply") }
            .fioriButtonStyle(FioriPrimaryButtonStyle())
            .frame(maxWidth: .infinity)
            .padding(16)
            .background(.regularMaterial)
    }
}
```

### Full list report pattern
```swift
struct InvoiceListReport: View {
    @State private var filterItems: [FilterFeedbackBarItem] = predefinedFilters
    @State private var showFilterModal = false

    var body: some View {
        NavigationStack {
            VStack(spacing: 0) {
                // Search bar
                // (handled by .searchable modifier)

                // Filter feedback bar
                if !filterItems.isEmpty {
                    FilterFeedbackBar(items: $filterItems) { item in
                        toggleFilter(item)
                    }
                    Divider()
                }

                // Content list
                List(filteredInvoices) { invoice in
                    ObjectItem {
                        Text(invoice.number)
                    } subtitle: {
                        Text(invoice.vendor)
                    } status: {
                        Text(invoice.status)
                            .foregroundStyle(Color.preferredColor(.secondaryLabel))
                    }
                }
            }
            .navigationTitle("Invoices")
            .searchable(text: $searchQuery)
            .toolbar {
                ToolbarItem(placement: .primaryAction) {
                    FioriButton { _ in
                        Image(systemName: "line.3.horizontal.decrease.circle")
                            .accessibilityLabel("Filter")
                    }
                    .fioriButtonStyle(FioriTertiaryButtonStyle())
                    .onTapGesture { showFilterModal = true }
                }
            }
            .sheet(isPresented: $showFilterModal) {
                SortFilterSheet(model: $filterModel, onApply: applyFilters)
            }
        }
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Button type | Default | `FilterFeedbackBarItem(title:)` |
| Button type | Default + chevron | Add `accessoryIcon: Image(systemName: "chevron.down")` |
| Button type | Icon | `FilterFeedbackBarItem(title:, icon:)` |
| Button type | Icon + chevron | Icon item + `accessoryIcon` |
| State | Active | `isSelected: true` |
| State | Inactive | `isSelected: false` |
| Sort | Non-default | Active item, leftmost position |
| Sort | Default | Not shown in bar |
| Sheet | Yes | `.sheet {}` with NavigationStack + Apply toolbar |
| Bar | With predefined buttons | `filterItems` always populated |
| Bar | Without predefined buttons | `filterItems` empty until filter/sort applied |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Keep active buttons to the left of inactive buttons
- Use consistent button types — all default OR all icon, never mixed
- Keep predefined filter buttons visible even when inactive
- Show default sort only when it has been changed to a non-default value
- Provide a "Reset" and "Apply" in the filter sheet — the Apply button must always be visible
- Make filters from the modal disappear from the bar when deactivated

**Don't:**
- Mix default and icon filter buttons in the same bar
- Show a filter feedback bar when filters are too complex or have long names — use a count in the filter button instead
- Allow users to customize which fast filters appear in the bar
- Show the default sort option in the bar

---

## Related Components

- [object-item.md](object-item.md) — list rows filtered by this component
- [data-table.md](data-table.md) — table filtered by this component
- [forms.md](forms.md) — form cells used inside the filter sheet
- [dimension-selector.md](dimension-selector.md) — related selection pattern
