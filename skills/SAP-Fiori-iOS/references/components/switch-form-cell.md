# Switch Form Cell — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUISwitchFormCell`, SwiftUI `SwitchView`

## What is it?

A switch form cell toggles two mutually exclusive states: on and off. It controls the availability of related UI elements on the current screen and must always be used inside a table cell (form row).

---

## When to Use

- Toggling a setting or feature on/off
- Controlling the visibility or availability of other UI elements on the same screen

**Don't** add text labels to describe the current value ("Enabled" / "Disabled") — the switch's position communicates its state. If more definition is needed, add a drill-down row instead.

---

## Behavior

Tap the toggle to change state. The change takes effect immediately.

---

## States

| State | Behavior | Visual |
|-------|---------|--------|
| On | Feature/setting active | Toggle filled (tint color) |
| Off | Feature/setting inactive | Toggle empty |
| Disabled | Non-interactive | Dimmed |
| Read-only | Non-interactive | **Text label** in place of the visual switch |

### Read-only state
The read-only switch replaces the visual toggle with a **text label** customized to the scenario (e.g. "Active" / "Inactive", "Enabled" / "Not available"). Use optional helper text to indicate it is read-only or to provide context.

---

## Switch with Further Selection

When toggling on reveals additional configuration options, add a drill-down cell row below the switch. The additional row can be a date picker, list picker, or any other input.

```
[ ✓ Notify Me          ON  ]   ← switch
[   Notification Date  ›   ]   ← drill-down, only visible when switch is ON
```

---

## SwiftUI Code Examples

### Basic switch form cell
```swift
import FioriSwiftUICore

@State private var isAutoApprove = false

SwitchView(
    title: { Text("Auto-Approve Below $500") },
    isOn: $isAutoApprove
)
```

### With helper text
```swift
SwitchView(
    title: { Text("Enable Notifications") },
    isOn: $notificationsEnabled
) {
    Text("You'll receive alerts when your invoice is approved or rejected.")
        .font(.fiori(forTextStyle: .footnote))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
}
```

### Read-only state (text label instead of toggle)
```swift
// Read-only — show text label, not toggle
SwitchView(
    title: { Text("Two-Factor Authentication") },
    isOn: .constant(true),
    controlState: .readonly
)
// SDK replaces toggle with contextual text label (e.g. "Active")
// Add helper text to indicate read-only if needed
```

### Disabled state
```swift
SwitchView(
    title: { Text("Override Budget Limit") },
    isOn: $overrideEnabled
)
.disabled(true)
```

### Switch with further selection (drill-down pattern)
```swift
@State private var notifyOnApproval = false
@State private var notificationDate = Date()

Form {
    Section("Notifications") {
        SwitchView(
            title: { Text("Notify Me") },
            isOn: $notifyOnApproval
        )

        // Only show when switch is ON
        if notifyOnApproval {
            DateTimePicker(
                title: { Text("Notification Date") },
                selection: $notificationDate,
                pickerComponents: [.date, .hourAndMinute]
            )
            .transition(.opacity.combined(with: .move(edge: .top)))
        }
    }
}
.animation(.easeInOut(duration: 0.2), value: notifyOnApproval)
```

### Controlling other UI element availability
```swift
@State private var useCreditCard = false

Form {
    Section("Payment") {
        SwitchView(
            title: { Text("Pay by Credit Card") },
            isOn: $useCreditCard
        )

        // Related fields — available only when switch is ON
        TextFieldFormView(
            title: { Text("Card Number") },
            text: $cardNumber
        )
        .disabled(!useCreditCard)
        .opacity(useCreditCard ? 1 : 0.4)

        TextFieldFormView(
            title: { Text("CVV") },
            text: $cvv
        )
        .disabled(!useCreditCard)
        .opacity(useCreditCard ? 1 : 0.4)
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| State | On | `isOn: .constant(true)` / `$binding = true` |
| State | Off | `isOn: .constant(false)` / `$binding = false` |
| State | Disabled | `.disabled(true)` |
| State | Read-only | `controlState: .readonly` — visual toggle replaced by text |
| Helper text | Yes | Trailing closure with `Text(...)` |
| Further selection | Yes | Conditional row below switch, animate in/out |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Let the toggle position communicate state — no "On/Off" text labels next to the switch
- Use read-only state with a contextual text label when the value can't be changed
- Animate the appearance of drill-down rows when the switch toggles
- Apply changes immediately on toggle — no "Apply" button needed

**Don't:**
- Add text to describe the switch's current value ("Enabled" / "Disabled") next to the toggle
- Use for non-boolean choices — use a segmented control or list picker instead
- Use outside a form row (table cell context)

---

## Related Components

- [segmented-control-form-cell.md](segmented-control-form-cell.md) — for more than two mutually exclusive options
- [pickers.md](pickers.md) — drill-down value selection when switch reveals further options
- [forms.md](forms.md) — other form input cells
