# Key Value Table View Cell — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Table View Cells
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIKeyValueTableViewCell`, SwiftUI `KeyValueItem`

## What is it?

The key value table view cell is a read-only cell for displaying simple sets of data. It pairs a descriptive key label with a corresponding value.

---

## When to Use

**Do:**
- Display simple sets of data or information

**Don't:**
- Use as an editable field — use `TextFieldFormView` or `KeyValueFormView` for input

**Tips:**
- Display a key label alongside a value, not with an image
- Convey uneditable information only

---

## Anatomy

```
A. Key Label           B. Value
"Vendor"               SAP SE
```

**A. Key Label** — descriptive label.
**B. Value** — the data for the label. **Wraps as needed.**

---

## Actionable Values

By default the cell is read-only. In certain cases a value can be actionable (e.g. phone number opens keypad, address opens Maps). Actionable values:
- Text in **tint color**
- Text weight: **Semibold**
- Still uneditable — just triggers an action on tap

---

## Adaptive Design

Available in compact, regular, regular-readable, and regular full-width.
Regular width supports an optional **two-column layout** (two key/value pairs side by side).

---

## SwiftUI Code Examples

### Basic read-only
```swift
import FioriSwiftUICore

KeyValueItem(
    key: { Text("Vendor") },
    value: { Text("SAP SE") }
)
```

### Value wraps as needed
```swift
KeyValueItem(
    key: { Text("Address") },
    value: {
        Text("Dietmar-Hopp-Allee 16, 69190 Walldorf, Germany")
        // Wraps to multiple lines automatically
    }
)
```

### Actionable value (phone number → opens keypad)
```swift
KeyValueItem(
    key: { Text("Phone") },
    value: {
        // Tint color + semibold = actionable indicator
        Text("+49 6227 747474")
            .foregroundStyle(Color.preferredColor(.tintColor))
            .font(.fiori(forTextStyle: .body, weight: .semibold))
    }
)
.onTapGesture {
    if let url = URL(string: "tel:+496227747474") {
        UIApplication.shared.open(url)
    }
}
```

### Actionable value (address → opens Maps)
```swift
KeyValueItem(
    key: { Text("Address") },
    value: {
        Text("Dietmar-Hopp-Allee 16, Walldorf")
            .foregroundStyle(Color.preferredColor(.tintColor))
            .font(.fiori(forTextStyle: .body, weight: .semibold))
    }
)
.onTapGesture { openInMaps(address) }
```

### Two-column layout (regular width)
```swift
@Environment(\.horizontalSizeClass) var hSizeClass

if hSizeClass == .regular {
    HStack(alignment: .top, spacing: 16) {
        VStack(alignment: .leading, spacing: 12) {
            KeyValueItem(key: { Text("Vendor") }, value: { Text("SAP SE") })
            KeyValueItem(key: { Text("Invoice #") }, value: { Text("INV-2026-001") })
        }
        VStack(alignment: .leading, spacing: 12) {
            KeyValueItem(key: { Text("Amount") }, value: { Text("$1,450.00") })
            KeyValueItem(key: { Text("Due Date") }, value: { Text("30 Jan 2026") })
        }
    }
} else {
    VStack(alignment: .leading, spacing: 12) {
        KeyValueItem(key: { Text("Vendor") }, value: { Text("SAP SE") })
        KeyValueItem(key: { Text("Invoice #") }, value: { Text("INV-2026-001") })
        KeyValueItem(key: { Text("Amount") }, value: { Text("$1,450.00") })
        KeyValueItem(key: { Text("Due Date") }, value: { Text("30 Jan 2026") })
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Value | Read-only | `Text(value)` default style |
| Value | Actionable | `.tintColor` + `.semibold` + `.onTapGesture` |
| Value | Wrapping | Default — `Text` wraps automatically |
| Layout | Single column | `VStack` of `KeyValueItem` |
| Layout | Two columns (regular) | `HStack` of two `VStack`s |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use tint color + semibold weight to signal actionable values
- Let value text wrap freely — never truncate
- Use two-column layout on regular width for better space usage

**Don't:**
- Use for editable inputs
- Display an image in the key label area — text only

---

## Related Components

- [text-inputs.md](text-inputs.md) — editable key/value form cells
- [object-cell.md](object-cell.md) — richer list rows with more content zones
- [status-info-label.md](status-info-label.md) — icon + label combinations
