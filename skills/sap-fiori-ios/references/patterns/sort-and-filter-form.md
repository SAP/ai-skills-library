# Sort & Filter Form — Pattern Guide

> SAP Fiori for iOS | Patterns
> Development reference: Create and Filter Patterns SDK

## What is it?

The sort and filter form enables advanced filtering of large datasets. Opens as a full-screen modal (compact) or popover (regular). Requires the user to tap a results button to apply — results are not updated live.

---

## When to Use

**Do:**
- Use for large, complex filters with many options
- Put sort options first, then filter options (most important/frequent on top)
- Group related filters together
- Keep the form short and uncluttered

**Don't:**
- Use for contextual live filtering — use Filter Feedback Bar instead
- Put everything into filters — important top-level choices belong upfront

---

## Anatomy

```
A. Navigation Bar
   Title: "Filter"
   Subtitle: "<content type> <N filtered> of <N total>"
   [B. Cancel]              [C. Reset]

D. Sort Section
   (filter form cell — single, or order picker — multi-criteria)

D. Filter Sections
   (various form cell controls)

E. Action Toolbar: [Show <N> <results>]  ← always visible
```

**A. Title + subtitle** — subtitle auto-adapts to content type (e.g. "Orders 12 of 54"); sort does not affect count.
**B. Cancel** — closes without applying filters.
**C. Reset** — resets all settings to initial state.
**D. Sort always first**, then filter components; sort always has a preselected default.
**E. Results button** — "Show N results" label; always visible (not hidden on scroll).

---

## Trigger

- Primary: filter text button in the navigation bar
- Secondary (if no nav bar space): filter button in the toolbar
- After applying: filter button shows the count of active filters

---

## Form Control Selection

| Filter type | Component |
|-------------|-----------|
| Toggle on/off | Switch form cell |
| Increment/decrement value | Stepper form cell |
| Continuous range | Slider (single) or Range Slider |
| Up to 8 text options, short labels | Filter form cell (single/multi) |
| Up to 3 short values | Segmented control form cell |
| More than 8 values, or dynamic | List picker (single/multi) |
| Date/time or duration | Picker |
| Sort by one criterion | Filter form cell (single selection) |
| Sort by multiple criteria + direction | Order picker form cell |

---

## Sort Rules

- Sort section always comes **before** filter sections
- Sort must always have a **preselected default value**
- Popular sort options: alphabet, date, rating
- Single criterion → filter form cell (single selection)
- Multiple criteria + direction → order picker form cell

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

@State private var showFilter = false
@State private var sortIndex = 0
@State private var selectedStatuses: Set<Int> = []
@State private var priceRange: ClosedRange<Double> = 0...10000
@State private var fromDate = Date()
@State private var isUrgentOnly = false

let sortOptions = ["Date (Newest)", "Amount (High to Low)", "Vendor (A–Z)"]
let statusOptions = ["Open", "In Review", "Approved", "Rejected"]

// Filter button in nav bar shows active count
.toolbar {
    ToolbarItem(placement: .primaryAction) {
        FioriButton { _ in
            HStack(spacing: 4) {
                Image(systemName: "line.3.horizontal.decrease.circle")
                if activeFilterCount > 0 {
                    Text("\(activeFilterCount)")
                        .font(.fiori(forTextStyle: .caption2))
                }
            }
            .accessibilityLabel("Filter — \(activeFilterCount) active")
        }
        .fioriButtonStyle(FioriTertiaryButtonStyle())
        .onTapGesture { showFilter = true }
    }
}

// Filter form — compact: full-screen, regular: popover
.fullScreenCover(isPresented: $showFilter) {  // compact
    NavigationStack {
        List {
            // D. Sort (always first, always preselected)
            Section("Sort") {
                FilterFormView(
                    title: { Text("Sort By") },
                    options: sortOptions.map { AttributedString($0) },
                    selectedIndices: Binding(
                        get: { [sortIndex] },
                        set: { sortIndex = $0.first ?? 0 }
                    ),
                    allowsMultipleSelection: false
                )
            }

            // D. Filters
            Section("Status") {
                FilterFormView(
                    title: { Text("Status") },
                    options: statusOptions.map { AttributedString($0) },
                    selectedIndices: Binding(
                        get: { Array(selectedStatuses) },
                        set: { selectedStatuses = Set($0) }
                    ),
                    allowsMultipleSelection: true
                )
            }

            Section("Amount") {
                FioriSlider(
                    title: { Text("Price Range") },
                    lowerValue: Binding(get: { priceRange.lowerBound },
                                       set: { priceRange = $0...priceRange.upperBound }),
                    upperValue: Binding(get: { priceRange.upperBound },
                                       set: { priceRange = priceRange.lowerBound...$0 }),
                    range: 0...50000, step: 500, decimalPlaces: 0
                )
            }

            Section("Options") {
                SwitchView(title: { Text("Urgent Only") }, isOn: $isUrgentOnly)
            }
        }
        .navigationTitle("Filter")
        .navigationBarTitleDisplayMode(.inline)
        .toolbar {
            ToolbarItem(placement: .cancellationAction) {
                FioriButton { _ in Text("Cancel") }
                    .fioriButtonStyle(FioriTertiaryButtonStyle())
                    .onTapGesture { showFilter = false }
            }
            ToolbarItem(placement: .destructiveAction) {
                FioriButton { _ in Text("Reset") }
                    .fioriButtonStyle(FioriTertiaryButtonStyle())
                    .onTapGesture { resetFilters() }
            }
        }
        .safeAreaInset(edge: .bottom) {
            // E. Always-visible results button
            FioriButton { _ in Text("Show \(filteredCount) Results") }
                .fioriButtonStyle(FioriPrimaryButtonStyle())
                .frame(maxWidth: .infinity)
                .padding(16)
                .background(.regularMaterial)
                .onTapGesture { applyFilters(); showFilter = false }
        }
    }
}
```

---

## Adaptive Design

| Size class | Presentation |
|-----------|-------------|
| Compact (iPhone) | Full-screen modal |
| Regular (iPad) | Popover |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Always place sort before filters
- Always preselect a default sort value
- Keep the Results button always visible (sticky at bottom)
- Show active filter count on the filter button
- Group related filters in sections
- Auto-adapt subtitle to the filtered content type

**Don't:**
- Use for live/contextual filtering (use Filter Feedback Bar)
- Allow the Results button to scroll out of view
- Skip the active filter count indicator on the filter button

---

## Related Patterns

- [sort-and-filter-overview.md](sort-and-filter-overview.md)
- [quick-sort.md](quick-sort.md)
- [../components/filter-feedback-bar.md](../components/filter-feedback-bar.md)
