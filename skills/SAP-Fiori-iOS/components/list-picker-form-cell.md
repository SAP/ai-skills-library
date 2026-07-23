# List Picker Form Cell — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIListPickerFormCell`, SwiftUI `ListPickerItem`

## What is it?

A list picker allows selection of one or more options from a defined category. Use it when there are **more than 8 values** to choose from, or when the options are dynamic and unpredictable (e.g. loaded from a database).

---

## When to Use

**Do:**
- Use when the size and nature of available options are unknown or dynamic (database data)
- Use when options have a consistent structure (text or object cells)
- Use an asterisk (*) in the label when selection is required
- Use when there are more than 8 values (fewer than 8 → use `FilterFormCell`)

**Don't:**
- Use for boolean options (yes/no, true/false) — use a `Switch` instead
- Use when selection requires complex input (text entry, sliders, multiple simultaneous interactions)

---

## Anatomy

```
A. List Picker Cell (in form)
┌─────────────────────────────────────────┐
│ Label                    Value ›         │
└─────────────────────────────────────────┘
        ↓ tap to open value list

B. Navigation Bar: [Cancel]        [Apply]
E. [Search field]
C. Section Header: "All"  [Select All / Deselect All]
D. Value List:
   ○ Option A
   ✓ Option B          ← checkmark = selected
   ○ Option C
   ...
F. [Anchor Button: 2 Selected ↑]   ← multi-select + modal only
```

### A. List Picker Cell
Label + selected value(s) displayed inline. Tapping navigates into the value list.

### B. Navigation Bar
"Cancel" (discard) and "Apply" (save selection).

### C. Section Header
Describes the grouped values. Provides "Select All / Deselect All" for multi-selection. Visually customizable.

### D. Value List
Items within the category. Checkmark indicates selection.

### E. Search
Recommended when the value list is large.

### F. Anchor Button (optional)
Shows the count of selected items and lets the user quickly jump to the top of the list. **Multi-selection and modal sheet view only.**

---

## Behavior & Interaction

### Select and Apply
1. Tap the list picker cell → navigates to / opens the value list
2. Tap a value → selected (checkmark shown); tap again → deselected
3. Tap "Apply" → selected values saved and displayed in the cell

### Discard Changes
Tap "Cancel" → changes discarded. Consider adding an action sheet confirmation to prevent accidental discard.

### Read-only state
- Helper text optionally indicates read-only
- Disclosure icon (›) hidden
- All selected values surfaced in the cell (wrapping as needed)
- If many long values cause excessive cell height, implement a custom summary view

---

## Variations

### Selection Type

| Type | Use for |
|------|---------|
| Single | One option from the list; values can be grouped by sections |
| Multi | One or more options; "Selected" grouping recommended to minimize scrolling for deselection |

For multi-selection with frequent searching: use the **search to select** pattern.

### Value Type

| Type | When to use |
|------|-------------|
| Text values | Default — most common; long body text goes on a second line; truncate if still too long |
| Object cells | Only when additional information is important for the selection; omit attributes and accessory view; show radio button on the left |

### Selection View (presentation)

| Mode | Behavior |
|------|---------|
| Full view *(default)* | Push transition into a full-screen list |
| Half modal | Resizable sheet — some parent context remains visible; expands to full on scroll or drag |
| Full modal | Full-screen sheet |

---

## SwiftUI Code Examples

### Basic single-selection list picker
```swift
import FioriSwiftUICore

@State private var selectedVendor: String? = nil
let vendors = ["ACME Corp", "SAP SE", "GlobalTech", "InnovateCo", "DataStream"]

ListPickerItem(
    title: { Text("Vendor *") },
    value: { Text(selectedVendor ?? "Select vendor") },
    destination: {
        ListPickerDestination(
            vendors,
            id: \.self,
            selection: $selectedVendor
        ) { vendor in
            Text(vendor)
        }
    }
)
```

### Multi-selection with search
```swift
@State private var selectedCountries: Set<String> = []
@State private var searchQuery = ""

ListPickerItem(
    title: { Text("Countries") },
    value: {
        Text(selectedCountries.isEmpty
             ? "Select countries"
             : selectedCountries.sorted().joined(separator: ", "))
    },
    destination: {
        ListPickerDestination(
            filteredCountries,
            id: \.self,
            selections: $selectedCountries
        ) { country in
            Text(country)
        }
        .searchable(text: $searchQuery)
    },
    allowsMultipleSelection: true
)

var filteredCountries: [String] {
    searchQuery.isEmpty ? allCountries
        : allCountries.filter { $0.localizedCaseInsensitiveContains(searchQuery) }
}
```

### With section grouping (single selection)
```swift
ListPickerItem(
    title: { Text("Region") },
    value: { Text(selectedRegion ?? "Select region") },
    destination: {
        List {
            Section("EMEA") {
                ForEach(emeaRegions, id: \.self) { region in
                    ListPickerRow(
                        title: { Text(region) },
                        isSelected: selectedRegion == region,
                        onSelect: { selectedRegion = region }
                    )
                }
            }
            Section("Americas") {
                ForEach(americasRegions, id: \.self) { region in
                    ListPickerRow(
                        title: { Text(region) },
                        isSelected: selectedRegion == region,
                        onSelect: { selectedRegion = region }
                    )
                }
            }
        }
        .navigationTitle("Region")
        .toolbar {
            ToolbarItem(placement: .confirmationAction) {
                FioriButton { _ in Text("Apply") }
                    .fioriButtonStyle(FioriTertiaryButtonStyle())
                    .onTapGesture { applyAndDismiss() }
            }
        }
    }
)
```

### Half-modal presentation
```swift
@State private var showPicker = false
@State private var selectedCategory: String? = nil

ListPickerItem(
    title: { Text("Category") },
    value: { Text(selectedCategory ?? "Select category") }
) {
    showPicker = true
}
.sheet(isPresented: $showPicker) {
    NavigationStack {
        CategoryPickerList(selection: $selectedCategory)
            .navigationTitle("Category")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    FioriButton { _ in Text("Cancel") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { showPicker = false }
                }
                ToolbarItem(placement: .confirmationAction) {
                    FioriButton { _ in Text("Apply") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture {
                            applySelection()
                            showPicker = false
                        }
                }
            }
    }
    .presentationDetents([.medium, .large])
    .presentationDragIndicator(.visible)
}
```

### Read-only state
```swift
ListPickerItem(
    title: { Text("Approved By") },
    value: { Text("Jane Smith, John Doe") },
    isEditable: false
)
// Disclosure icon hidden; values wrap; no tap interaction
```

### With discard confirmation
```swift
.confirmationDialog(
    "Discard changes?",
    isPresented: $showDiscardConfirmation
) {
    Button("Discard", role: .destructive) {
        resetSelection()
        dismiss()
    }
    Button("Keep Editing", role: .cancel) {}
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Selection | Single | `selection: $selectedValue` (non-Set binding) |
| Selection | Multi | `selections: $selectedValues` (Set binding) |
| Presentation | Full view | Default push navigation |
| Presentation | Half modal | `.sheet` + `.presentationDetents([.medium, .large])` |
| Presentation | Full modal | `.sheet` + `.presentationDetents([.large])` |
| Value type | Text | `Text(item)` in destination list |
| Value type | Object cell | `ObjectItem {}` in destination — radio button left, no attributes |
| State | Default | Normal interactive cell |
| State | Read-only | `isEditable: false` — no disclosure icon |
| State | Disabled | `.disabled(true)` |
| Search | Yes | `.searchable(text:)` in destination |
| Section grouping | Yes | `Section {}` in destination list |
| Required | Yes | Asterisk (*) in label text |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use for **more than 8 options** — fewer → use `FilterFormCell`
- Add search when the list is large
- Use "Selected" grouping in multi-selection to minimize scrolling for deselection
- Show a discard confirmation when the user taps Cancel after making changes
- Use object cells in the value list only when additional info is necessary for the decision
- Implement a custom summary view if read-only selected values would create excessive cell height

**Don't:**
- Use for boolean inputs — use `Switch`
- Use for inputs requiring text entry or sliders
- Include attributes or accessory views when using object cells in the list
- Omit "Apply" — selection must always be explicitly confirmed

---

## Related Components

- [filter-form-cell.md](filter-form-cell.md) — for fewer than 8 options
- [forms.md](forms.md) — other form input cells
- [filter-feedback-bar.md](filter-feedback-bar.md) — showing active selections above a list
