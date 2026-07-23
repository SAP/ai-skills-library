# Search to Select — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUISearchToSelectView`, `FUISearchToSelectViewController`

## What is it?

Search to select is a control for searching and selecting **multiple items** from a large collection of values. It combines a search field with a suggestion list and selected item chips.

---

## When to Use

**Do:**
- Use to choose one or more items from a large set

**Don't:**
- Use the local search component (standard search bar) to find and select multiple values — use search to select instead

---

## Anatomy

```
Navigation bar
──────────────────────────────────────────
A. [Search field: "Type to search…"]
──────────────────────────────────────────
[Select All] (optional)
B. Suggestion list / results list:
   ○ Item A
   ✓ Item B (selected)
   ○ Item C
   ...
```

**A. Search field** — below the navigation bar.

**B. Suggestion list** — sits below the search field. Can show:
- Recommended items immediately available for selection (suggestions)
- If no suggestions: full list sorted alphabetically

**C. Select All button** (optional) — selects all values in the current list.

---

## Presentation

Can be presented as:
- **Push navigation** — navigates into the selection screen
- **Modal sheet** — overlays the current screen

Choose based on the use case context.

---

## Selection

### Option 1 — Select from suggestion list
User selects multiple items directly from the suggestion/full list. Selected items are shown with a checkmark and accumulate in the search field area.

### Option 2 — Search then select
1. User types a query → results list appears
2. User taps an item → item is selected and appears in the search field
3. App **automatically navigates back** to the default screen after selection
4. The selected state is visible for **>1 second** before auto-navigation

---

## Removing a Selected Item

Two ways to remove:
1. **Delete from the search input field** — tap the × on the item chip in the search field
2. **Deselect from the list below** — tap the selected item in the suggestion/results list to deselect

---

## SwiftUI Code Examples

### Basic search to select (push navigation)
```swift
import FioriSwiftUICore

@State private var selectedVendors: Set<String> = []
@State private var searchQuery = ""

NavigationStack {
    SearchListPickerItem(
        query: $searchQuery,
        items: filteredVendors,
        selectedItems: $selectedVendors,
        id: \.self
    ) { vendor in
        Text(vendor)
    }
    .navigationTitle("Select Vendors")
    .toolbar {
        ToolbarItem(placement: .confirmationAction) {
            FioriButton { _ in Text("Apply") }
                .fioriButtonStyle(FioriTertiaryButtonStyle())
                .onTapGesture { applySelection(); dismiss() }
        }
        ToolbarItem(placement: .cancellationAction) {
            FioriButton { _ in Text("Cancel") }
                .fioriButtonStyle(FioriTertiaryButtonStyle())
                .onTapGesture { dismiss() }
        }
    }
}

var filteredVendors: [String] {
    searchQuery.isEmpty ? allVendors
        : allVendors.filter { $0.localizedCaseInsensitiveContains(searchQuery) }
}
```

### As a modal sheet
```swift
@State private var showSearchToSelect = false
@State private var selectedItems: Set<String> = []

FioriButton { _ in Text("Add Assignees") }
    .fioriButtonStyle(FioriSecondaryButtonStyle())
    .onTapGesture { showSearchToSelect = true }
    .sheet(isPresented: $showSearchToSelect) {
        NavigationStack {
            SearchListPickerItem(
                query: $searchQuery,
                items: filteredItems,
                selectedItems: $selectedItems,
                id: \.self
            ) { item in Text(item) }
            .navigationTitle("Select Assignees")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    FioriButton { _ in Text("Cancel") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { showSearchToSelect = false }
                }
                ToolbarItem(placement: .confirmationAction) {
                    FioriButton { _ in Text("Apply") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture {
                            applySelection()
                            showSearchToSelect = false
                        }
                }
            }
        }
        .presentationDetents([.medium, .large])
    }
```

### With Select All + deselect from list
```swift
VStack(spacing: 0) {
    // Optional Select All
    Button("Select All") {
        selectedItems = Set(allItems)
    }
    .foregroundStyle(Color.preferredColor(.tintColor))
    .frame(maxWidth: .infinity, alignment: .leading)
    .padding(.horizontal, 16)
    .padding(.vertical, 8)

    Divider()

    List(filteredItems, id: \.self) { item in
        Button {
            if selectedItems.contains(item) {
                selectedItems.remove(item)  // deselect from list
            } else {
                selectedItems.insert(item)
            }
        } label: {
            HStack {
                Text(item)
                    .foregroundStyle(Color.preferredColor(.primaryLabel))
                Spacer()
                if selectedItems.contains(item) {
                    Image(systemName: "checkmark")
                        .foregroundStyle(Color.preferredColor(.tintColor))
                }
            }
        }
        .buttonStyle(.plain)
    }
}
```

### Auto-navigate back after single-item selection (Option 2 behavior)
```swift
func selectItem(_ item: String) {
    selectedItems.insert(item)
    searchQuery = ""

    // Visible for >1s before navigating back
    DispatchQueue.main.asyncAfter(deadline: .now() + 1.1) {
        dismiss()
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Presentation | Push | `NavigationStack` push |
| Presentation | Modal | `.sheet` + `NavigationStack` inside |
| Suggestion list | With suggestions | Pre-populate list with recommended items |
| Suggestion list | Alphabetical (no suggestions) | Sort `allItems` alphabetically |
| Select All | Yes | Button that sets `selectedItems = Set(allItems)` |
| Select All | No | Omit |
| Remove | From search field | Remove chip from `selectedItems` |
| Remove | From list | Tap item to deselect |
| Auto-navigate | Yes (single select) | `asyncAfter(>1s)` then `dismiss()` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use for selecting multiple items from a large collection
- Show a brief selected state (>1s) before auto-navigating after single-item selection
- Allow removal both from the search field chips and by deselecting in the list
- Provide Select All when selecting the entire list is a common operation

**Don't:**
- Use standard search bar for multi-value selection — use search to select
- Auto-navigate immediately (0ms) after selection — the user needs to see the selected state briefly

---

## Related Components

- [search-bar.md](search-bar.md) — single-focus search without multi-select
- [list-picker-form-cell.md](list-picker-form-cell.md) — multi-select from a list via a form cell
- [filter-feedback-bar.md](filter-feedback-bar.md) — displaying selected values as filter chips
