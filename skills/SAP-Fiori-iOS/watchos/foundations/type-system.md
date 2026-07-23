# Type System — SAP Fiori for watchOS

> SAP Fiori for watchOS | Foundation

## What is it?

SAP Fiori for watchOS uses **SF Compact** as its primary typeface. SF Compact is optimized for small screens and integrates seamlessly with watchOS accessibility features including Dynamic Type.

---

## Typeface

| Context | Font |
|---------|------|
| Standard UI | SF Compact (multiple weights, Display and Text variants) |
| Complications | SF Compact Rounded (recommended) |

SF Compact has multiple weights in both Display (for headlines/large text) and Text (for body/smaller text) variants.

---

## Key Notes

- SF Compact is Apple's native watchOS typeface — blends seamlessly with the native experience
- **Dynamic Type cannot be deactivated** on watchOS (unlike Wear OS) — all components must be optimized for text resizing
- Use system-provided text styles via SwiftUI to inherit Dynamic Type support automatically

```swift
// watchOS — use system text styles for Dynamic Type support
Text("Invoice #1234")
    .font(.headline)  // SF Compact, scales with Dynamic Type

Text("Due: Jan 30")
    .font(.footnote)

// Complications — use SF Compact Rounded
Text("18")
    .font(.system(.title, design: .rounded))
```

---

## Resources

- [Apple HIG: Typography for watchOS](https://developer.apple.com/design/human-interface-guidelines/typography)
