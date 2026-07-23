# Search Bar — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUISearchBar`, SwiftUI `SearchableListView`

## What is it?

The search bar locates objects within a large collection. Used in list report and list picker patterns to quickly navigate to an item.

---

## Anatomy

```
[🔍  A. Placeholder text          B. Mic/Scanner  ] [C. Cancel]
```

**A. Placeholder text** — context about what is being searched (e.g. "Search invoices").
**B. Trailing icon** (optional, hidden by default) — microphone (voice search) or barcode scanner.
**C. Cancel button** — returns to default state; cancels the search.
**D. Input text** — the user's typed query.
**E. Clear button** — clears the input field while remaining in search mode.

---

## States

| State | Visual |
|-------|--------|
| Default | Placeholder text shown; no keyboard |
| Active | Keyboard open; cursor in field; Cancel visible |
| Typing | User entering text; Clear button visible |
| Typed | Query entered; results shown in content area |

When the user taps the search bar, it **shifts up and replaces the navigation bar** (nav bar is automatically hidden). Results populate in the content area as the user types.

---

## Entry Points

### Search Icon
Use when search is **not the primary action** on the screen. A search icon is visible; tapping it expands into the full search bar.

### Search within Navigation Bar (Prominent)
Use when search **is the primary action**. The search bar remains permanently visible below the navigation bar.

---

## Trailing Icons (optional)

| Icon | Use for |
|------|---------|
| Microphone | Voice/speech recognition search — no typing required |
| Barcode scanner | Launch scanner to search by barcode without typing |

Both are hidden by default. Add only when relevant to the content being searched.

---

## Adaptive Design

- Supported in compact and regular widths
- Placement and sizing follow global layout margins for each size class

---

## SwiftUI Code Examples

### Standard search bar (prominent — always visible)
```swift
import FioriSwiftUICore

NavigationStack {
    List(filteredInvoices) { invoice in
        ObjectItem { Text(invoice.number) }
            .subtitle: { Text(invoice.vendor) }
    }
    .navigationTitle("Invoices")
    .searchable(
        text: $searchQuery,
        placement: .navigationBarDrawer(displayMode: .always),
        prompt: "Search invoices"
    )
}
```

### Search icon entry point (not always visible)
```swift
NavigationStack {
    List(invoices) { invoice in
        ObjectItem { Text(invoice.number) }
    }
    .navigationTitle("Invoices")
    .searchable(
        text: $searchQuery,
        placement: .navigationBarDrawer,  // collapsed by default
        prompt: "Search invoices"
    )
}
```

### With voice search (microphone)
```swift
// Microphone is provided automatically by the system keyboard
// For a dedicated mic button in the search bar:
.searchable(text: $searchQuery, prompt: "Search products") {
    // Suggestions
    ForEach(suggestions) { suggestion in
        Text(suggestion).searchCompletion(suggestion)
    }
}
// System provides mic in the keyboard — no manual mic needed in most cases
```

### With barcode scanner icon
```swift
NavigationStack {
    List(filteredItems) { item in
        ObjectItem { Text(item.name) }
    }
    .navigationTitle("Products")
    .searchable(text: $searchQuery, prompt: "Search or scan")
    .toolbar {
        ToolbarItem(placement: .primaryAction) {
            FioriButton { _ in
                Image(systemName: "barcode.viewfinder")
                    .accessibilityLabel("Scan barcode")
            }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .onTapGesture { openBarcodeScanner() }
        }
    }
}

// Handle scanner result — populate search field
func handleScanResult(_ code: String) {
    searchQuery = code
}
```

### In a list picker (search to select)
```swift
NavigationStack {
    List(filteredOptions, selection: $selectedOption) { option in
        Text(option.name)
    }
    .navigationTitle("Select Vendor")
    .searchable(
        text: $searchQuery,
        placement: .navigationBarDrawer(displayMode: .always),
        prompt: "Search vendors"
    )
}

var filteredOptions: [Vendor] {
    searchQuery.isEmpty ? allVendors
        : allVendors.filter {
            $0.name.localizedCaseInsensitiveContains(searchQuery)
        }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Entry point | Search icon | `.searchable(placement: .navigationBarDrawer)` |
| Entry point | Prominent (always visible) | `.searchable(placement: .navigationBarDrawer(displayMode: .always))` |
| Trailing icon | Microphone | System keyboard mic (automatic) |
| Trailing icon | Barcode scanner | Custom `ToolbarItem` with scanner button |
| State | Default | No query, no keyboard |
| State | Active | Keyboard open, Cancel visible |
| State | Typing | Clear button visible |
| State | Typed | Results in list |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use "prominent" (always-visible) placement when search is the primary action
- Write descriptive placeholder text (e.g. "Search invoices", not just "Search")
- Filter results in real time as the user types
- Allow Cancel to fully dismiss search and restore the content list

**Don't:**
- Show the search bar below the navigation bar on iPad inline — use `.navigationBarDrawer`
- Use trailing icons (mic, scanner) unless they are genuinely useful for the content type
- Omit placeholder text — users need context about what they're searching

---

## Related Components

- [filter-feedback-bar.md](filter-feedback-bar.md) — active filter chips shown below search
- [list-picker-form-cell.md](list-picker-form-cell.md) — search within a picker's value list
- [navigation-bar.md](navigation-bar.md) — search bar placement within nav bar context
