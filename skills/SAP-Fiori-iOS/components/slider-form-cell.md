# Slider Form Cell — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUISliderFormCell`, `FUIRangeSliderFormCell`, SwiftUI `FioriSlider`

## What is it?

A slider form cell displays a continuous range of values along a track. The user drags a handle to select an approximate value between a defined minimum and maximum. Typically found in create and filter modals.

**Use a slider when the precise value does not matter. If the exact value matters, use a picker instead.**

---

## When to Use

- Selecting an approximate value from a continuous range (price range, distance, opacity)
- Create and filter modals where approximate values are acceptable

**If the exact value matters → use a picker, not a slider.**

---

## Anatomy

```
A. Label: "Price Range"
E. Track:  ●━━━━━━━━━━━━○━━━━━━━━━━━━○  min/max labels
                D. Handle ↑
C. Hint text (optional)
F. Value Input Field: [  150  ]         ← tap to type exact value
```

**A. Label** — describes the value range.
**B. Slider** — shows default min/max and selected value.
**C. Hint Text** (optional) — additional information about the slider.
**D. Handle** — drag to select value.
**E. Track** — full range; tinted/blue area highlights the selected section. Keep min/max labels short — long labels shorten the track.
**F. Value Input Field** — shows selected value; tap to open keyboard and enter an exact value within the min/max range.

---

## Variations

### Slider (basic)
Selects a single value. No value input field — handle only.

### Single Slider
Selects a single value. Includes a **value input field** that the user can tap to type an exact value.

**States:** Default, Typing (keyboard open), Disabled

### Range Slider
Selects a **range** between two values (lower bound and upper bound). Includes two handles and two value input fields (min and max).

**States:** Default, Typing (min), Typing (max), Disabled

---

## Behavior

### Drag
Slide the handle along the track to set an approximate value. The value input field updates in real time as the user drags.

### Tap to type
Tap the value input field to open the keyboard and enter an exact value. The value must be within the min/max range.

---

## Adaptive Design

- Supported in both compact and regular widths
- On iPad, may be displayed inside a **popover modal**

---

## SwiftUI Code Examples

### Basic slider (no value field)
```swift
import FioriSwiftUICore

@State private var opacity: Double = 0.5

FioriSlider(
    title: { Text("Opacity") },
    value: $opacity,
    range: 0...1,
    step: 0.01
)
```

### Single slider with value input field
```swift
@State private var price: Double = 500

FioriSlider(
    title: { Text("Max Price") },
    value: $price,
    range: 0...2000,
    step: 50,
    decimalPlaces: 0,
    showsValueLabel: true,
    thumbShape: Circle(),
    activeTrackShape: Capsule()
)
// Tap value label to type exact amount
```

### Range slider
```swift
@State private var minPrice: Double = 200
@State private var maxPrice: Double = 800

FioriSlider(
    title: { Text("Price Range") },
    lowerValue: $minPrice,
    upperValue: $maxPrice,
    range: 0...2000,
    step: 50,
    decimalPlaces: 0,
    showsLowerThumb: true,
    showsUpperThumb: true
)
```

### With hint text
```swift
FioriSlider(
    title: { Text("Distance") },
    value: $distance,
    range: 1...100,
    step: 1,
    decimalPlaces: 0
) {
    // Hint text
    Text("Maximum distance from your location in kilometers")
        .font(.fiori(forTextStyle: .footnote))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
}
```

### Disabled state
```swift
FioriSlider(
    title: { Text("Capacity") },
    value: .constant(75),
    range: 0...100,
    step: 1
)
.disabled(true)
```

### Inside a filter sheet
```swift
Form {
    Section("Price Range") {
        FioriSlider(
            title: { Text("") },
            lowerValue: $minPrice,
            upperValue: $maxPrice,
            range: 0...5000,
            step: 100,
            decimalPlaces: 0
        )
    }

    Section("Distance") {
        FioriSlider(
            title: { Text("Within") },
            value: $maxDistance,
            range: 1...500,
            step: 5,
            decimalPlaces: 0,
            showsValueLabel: true
        )
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Variation | Slider | `FioriSlider(value:, range:)` — no value field |
| Variation | Single slider | `FioriSlider` + `showsValueLabel: true` |
| Variation | Range slider | `FioriSlider(lowerValue:, upperValue:, range:)` |
| State | Default | Normal |
| State | Typing | Value input field focused — keyboard open |
| State | Disabled | `.disabled(true)` |
| Hint text | Yes | Trailing closure with `Text(...)` |
| Min/max labels | Short | Keep brief — long labels shorten the track |
| Track highlight | Active area | Tinted (tint color) automatically |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use when approximate values are acceptable
- Keep min/max labels short — long labels physically shorten the track
- Include the value input field (single/range slider) so users can type an exact value when needed
- Use range slider when both lower and upper bounds need to be set
- Validate typed values against the min/max range

**Don't:**
- Use when the exact value matters — use a picker instead
- Use long text for minimum and maximum value labels
- Use a slider for discrete binary choices (true/false, yes/no) — use a switch instead

---

## Related Components

- [pickers.md](pickers.md) — precise value selection when exact values matter
- [forms.md](forms.md) — other form input cells
- [filter-feedback-bar.md](filter-feedback-bar.md) — showing applied range filters
