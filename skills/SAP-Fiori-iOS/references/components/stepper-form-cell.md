# Stepper Form Cell — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIStepperFormCell`, SwiftUI `StepperView`

## What is it?

A stepper displays and allows users to incrementally increase or decrease a selected value using "+" and "−" buttons. The value can also be typed directly into the value input field.

---

## Anatomy

```
A. Label: "Quantity"
C. Stepper Container: [ − ] [ 5 ] [ + ]
                         D.   E.   D.
B. Helper text (optional)
```

**A. Label** — describes the intent or desired value.
**B. Helper Text** (optional) — additional information.
**C. Stepper Container** — houses the stepper component.
**D. +/− Buttons** — segmented control buttons for incremental changes.
**E. Value / Input Field** — displays the current value; tap to open keyboard and enter exact value.

---

## Behavior

### Tap +/−
Increments or decrements the value by the defined step amount.

### Tap value field
Opens the keyboard to enter an exact value directly.

### States
| State | Behavior |
|-------|---------|
| Default | Interactive — +/− buttons active |
| Typing | Keyboard open — user entering a value directly |
| Disabled | No interaction; dimmed appearance |

---

## Adaptive Design

- Supported in both compact and regular widths
- On iPad, may appear inside a **popover modal**

---

## SwiftUI Code Examples

### Basic stepper
```swift
import FioriSwiftUICore

@State private var quantity = 1

StepperView(
    title: { Text("Quantity") },
    value: $quantity,
    step: 1,
    range: 1...99
)
```

### With helper text
```swift
StepperView(
    title: { Text("Number of Copies") },
    value: $copies,
    step: 1,
    range: 1...100
) {
    Text("Maximum 100 copies per order")
        .font(.fiori(forTextStyle: .footnote))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
}
```

### With decimal step
```swift
@State private var weight: Double = 1.0

StepperView(
    title: { Text("Weight (kg)") },
    value: $weight,
    step: 0.5,
    range: 0.5...50.0,
    decimalPlaces: 1
)
```

### Disabled state
```swift
StepperView(
    title: { Text("Items") },
    value: .constant(3),
    step: 1,
    range: 1...10
)
.disabled(true)
```

### Inside a form
```swift
Form {
    Section("Order Details") {
        StepperView(
            title: { Text("Quantity *") },
            value: $quantity,
            step: 1,
            range: 1...999
        )

        StepperView(
            title: { Text("Reorder Point") },
            value: $reorderPoint,
            step: 5,
            range: 0...500
        ) {
            Text("Alert when stock falls below this value")
                .font(.fiori(forTextStyle: .footnote))
                .foregroundStyle(Color.preferredColor(.secondaryLabel))
        }
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| State | Default | Normal `StepperView` |
| State | Typing | Value input field focused — keyboard open |
| State | Disabled | `.disabled(true)` |
| Helper text | Yes | Trailing closure with `Text(...)` |
| Step | Integer | `step: 1` |
| Step | Decimal | `step: 0.5`, `decimalPlaces: 1` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Define a meaningful `range` to prevent out-of-bounds values from keyboard input
- Use helper text to communicate constraints (max value, unit, purpose)
- Use appropriate step granularity — whole numbers for counts, decimals for measurements

**Don't:**
- Use for boolean or binary values — use a switch instead
- Use when a large numeric range would require many taps — use a slider or picker instead

---

## Related Components

- [slider-form-cell.md](slider-form-cell.md) — continuous range selection
- [pickers.md](pickers.md) — scrollable value selection
- [forms.md](forms.md) — other form input cells
