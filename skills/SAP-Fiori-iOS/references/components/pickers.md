# Pickers — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit` (Pickers page)
> Development reference: UIKit `FUIDatePickerFormCell`, `FUIDurationPickerFormCell`, `FUIValuePickerFormCell`, SwiftUI `DateTimePicker`, `DurationPickerComponent`, `ValuePicker`

## What is it?

A picker is used to select a single value by scrolling through a short list of predictable values. Commonly used for dates, times, durations, or custom value lists.

---

## Anatomy

```
A. Table Cell (in form)
┌────────────────────────────────────────┐
│ Label               Selected Value     │  ← value in tint color when active
└────────────────────────────────────────┘
        ↓ tap to open

B. Scrollable List
┌────────────────────────────────────────┐
│    ...  January  ...                   │
│    ...  2025     ...                   │
│  ▶  February  ◀  26  ▶  2026  ◀       │
│    ...  March    ...                   │
└────────────────────────────────────────┘
```

**A. Table Cell** — label + selected value. Value shows in **tint color** when the picker is active.

**B. Scrollable List** — values in logical order. Accessed by tapping the table cell.

---

## Variations

### Date Picker
Selects a specific date, time, or combination.

| Mode | Columns |
|------|---------|
| Date | Month, Day, Year |
| Time | Hours, Minutes, AM/PM |
| Date and Time | Date, Hours, Minutes, AM/PM |

```swift
import FioriSwiftUICore

// Date only
@State private var selectedDate = Date()

DateTimePicker(
    selection: $selectedDate,
    pickerComponents: .date
)

// Time only
DateTimePicker(
    selection: $selectedDate,
    pickerComponents: .hourAndMinute
)

// Date and time
DateTimePicker(
    selection: $selectedDate,
    pickerComponents: [.date, .hourAndMinute]
)
```

### Date Range Picker
Selects a range between two dates. The selected range can include or exclude disabled dates depending on app configuration.

```swift
@State private var startDate = Date()
@State private var endDate = Calendar.current.date(byAdding: .day, value: 7, to: Date())!

DateRangePicker(
    startDate: $startDate,
    endDate: $endDate
)
```

### Value Picker
Selects from any list of text or number values. For numbers, always include appropriate granularity.

```swift
// Text values
@State private var selectedCurrency = "USD"
let currencies = ["USD", "EUR", "GBP", "JPY", "CHF"]

ValuePicker(
    title: { Text("Currency") },
    value: { Text(selectedCurrency) },
    items: currencies.map { AttributedString($0) },
    selectedIndex: Binding(
        get: { currencies.firstIndex(of: selectedCurrency) ?? 0 },
        set: { selectedCurrency = currencies[$0] }
    )
)

// Numeric values with appropriate granularity
@State private var selectedQuantity = 1
let quantities = Array(1...100)

ValuePicker(
    title: { Text("Quantity") },
    value: { Text("\(selectedQuantity)") },
    items: quantities.map { AttributedString("\($0)") },
    selectedIndex: Binding(
        get: { quantities.firstIndex(of: selectedQuantity) ?? 0 },
        set: { selectedQuantity = quantities[$0] }
    )
)
```

### Duration Picker
Selects a length of time in hours and minutes. Maximum: **23 hours 59 minutes**.

```swift
@State private var duration: TimeInterval = 3600  // 1 hour in seconds

DurationPickerComponent(
    duration: $duration,
    maximumDuration: 23 * 3600 + 59 * 60  // 23h 59m
)
```

---

## Adaptive Design

| Size class | Behavior |
|-----------|---------|
| Compact (iPhone) | Scrollable list inline or expands below the cell |
| Regular (iPad) | Scrollable list can appear below the cell in a form sheet modal |

---

## Inside a Form (standard pattern)

```swift
Form {
    Section("Scheduling") {
        // Date picker form cell
        DateTimePicker(
            title: { Text("Due Date") },
            selection: $dueDate,
            pickerComponents: .date
        )

        // Time picker form cell
        DateTimePicker(
            title: { Text("Reminder Time") },
            selection: $reminderTime,
            pickerComponents: .hourAndMinute
        )
    }

    Section("Duration") {
        DurationPickerComponent(
            title: { Text("Estimated Time") },
            duration: $estimatedDuration
        )
    }

    Section("Settings") {
        ValuePicker(
            title: { Text("Priority") },
            value: { Text(selectedPriority) },
            items: priorities.map { AttributedString($0) },
            selectedIndex: $priorityIndex
        )
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Type | Date | `DateTimePicker(pickerComponents: .date)` |
| Type | Time | `DateTimePicker(pickerComponents: .hourAndMinute)` |
| Type | Date and Time | `DateTimePicker(pickerComponents: [.date, .hourAndMinute])` |
| Type | Date range | `DateRangePicker(startDate:, endDate:)` |
| Type | Value | `ValuePicker(items:, selectedIndex:)` |
| Type | Duration | `DurationPickerComponent(duration:)` |
| Active state | Yes | Value label in `.tintColor` |
| Active state | No | Value label in `.primaryLabel` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use for selecting from a short, predictable list of values
- For numbers in a value picker, include appropriate granularity (e.g. don't jump from 1 to 10 if 1-10 are all valid)
- Display the selected value in tint color when the picker is active
- Use date range picker when both start and end dates are needed

**Don't:**
- Use a picker when the user needs to type a free-form value — use a text field instead
- Exceed 23h 59m in the duration picker — it is the hard maximum
- Use a value picker for more than ~20 options — consider a list picker instead

---

## Related Components

- [list-picker-form-cell.md](list-picker-form-cell.md) — for larger or dynamic value lists
- [forms.md](forms.md) — other form input cells
- [calendar.md](calendar.md) — visual date selection in calendar format
