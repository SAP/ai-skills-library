# Quick Sort — Pattern Guide

> SAP Fiori for iOS | Patterns
> Related: [sort-and-filter-overview.md](sort-and-filter-overview.md)

## What is it?

Quick sort is a contextual sort pattern for changing sort criteria without filtering. Available as a direct menu (icon in nav bar) or submenu (within overflow menu). Works at component level (cards, preview tables) or full-screen (list reports).

**No filtering is possible with quick sort — use Sort & Filter Form for filtering.**

---

## Anatomy

### Menu (direct access)
```
A. Sort icon → opens menu
B. Menu with sort criteria
   C. ✓ Selected criterion (checkmark when active)
   D. Sort Criteria (max 5 — avoid scrolling)
```

### Submenu (in overflow menu)
```
A. … Overflow → opens overflow menu
B. "Sort By" entry (with chevron E.) → opens submenu
G. Submenu Title: "Sort By" / current criterion as subtitle
B. Submenu with sort criteria
   C. ✓ Selected criterion
```

**Max 5 sort criteria** — avoid scroll in the menu.

---

## Behavior

### After selecting a criterion:
1. Menu/submenu closes
2. Component sorts by new criterion
3. **Toast message** confirms the new sort (e.g. "Sorted by Date")

### Checkmark
Only visible on the currently active criterion.

---

## Adaptive Design

Both compact and regular use native iOS menu/submenu.

| Behavior | Compact (iPhone) | Regular (iPad) |
|----------|-----------------|----------------|
| Submenu opens | On top of menu | Next to menu (side-by-side) |
| Menu entry chevron | Left side | Right side |
| Submenu header | Shows menu entry info | No header — criteria only |

---

## SwiftUI Code Example

### Quick sort as direct menu (nav bar)
```swift
import FioriSwiftUICore

@State private var sortCriterion = "Date"
let sortOptions = ["Date", "Amount", "Vendor", "Status"]

.toolbar {
    ToolbarItem(placement: .primaryAction) {
        Menu {
            ForEach(sortOptions, id: \.self) { option in
                Button {
                    sortCriterion = option
                    showSortToast = true
                    autoDismissToast()
                } label: {
                    HStack {
                        Text(option)
                        if sortCriterion == option {
                            Image(systemName: "checkmark")  // C. Checkmark
                        }
                    }
                }
            }
        } label: {
            Image(systemName: "arrow.up.arrow.down")
                .accessibilityLabel("Sort")
        }
    }
}
.overlay(alignment: .bottom) {
    if showSortToast {
        ToastMessage { Text("Sorted by \(sortCriterion)") }
            .padding(.bottom, 24)
    }
}
```

### Quick sort as submenu (in overflow menu)
```swift
Menu {
    // Other actions
    Button("Share") { share() }
    Button("Archive") { archive() }

    // G. Sort submenu
    Menu("Sort By") {  // submenu title
        ForEach(sortOptions, id: \.self) { option in
            Button {
                sortCriterion = option
                showSortToast = true
            } label: {
                HStack {
                    Text(option)
                    if sortCriterion == option {
                        Image(systemName: "checkmark")
                    }
                }
            }
        }
    }
} label: {
    Image(systemName: "ellipsis.circle")
        .accessibilityLabel("More actions")
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Show a toast message confirming the new sort criterion
- Limit to max 5 sort criteria in the menu
- Show a checkmark on the currently active criterion
- Use direct menu when sort is a primary action; submenu when sort is secondary

**Don't:**
- Use quick sort for filtering — use Sort & Filter Form or Filter Feedback Bar
- Add more than 5 sort criteria (causes scrolling in the menu)

---

## Related Patterns

- [sort-and-filter-overview.md](sort-and-filter-overview.md)
- [sort-and-filter-form.md](sort-and-filter-form.md)
