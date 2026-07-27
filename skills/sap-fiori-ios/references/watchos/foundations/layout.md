# Layout — SAP Fiori for watchOS

> SAP Fiori for watchOS | Foundation

## What is it?

Best practices for watchOS app layouts — keeping content legible, aligned, organized, and accessible on small screens.

---

## Key Rules

### Full Width
Use the full screen width for interactive elements. The watch frame creates natural visual padding — no additional padding needed.

### Element Limits
- Max **3 symbol buttons** side by side
- Max **2 text buttons** side by side
- Two equal-priority text buttons with short labels can be placed next to each other

### Auto-Rotation
Uncommon on watchOS (display usually turns off on wrist turn). Use only for specific cases (e.g., QR code scanning in logistics where display must stay on and rotate).

---

## Screen Sizes

Apps always use rectangular layout. Screen sizes: 28, 40, 41, 42, 44, and 45mm.

**Start with the smallest screen, then optimize for larger sizes (45mm).**

Align text with the **leading edge** of the navigation bar title or "Back" button.

---

## Margins

Rounded watch corners may clip content. Always stay within the given margins. If using the SAP Fiori for watchOS Design Kit, margins are preset — do not change defaults.

---

## Touch Target

Minimum touch target: **40×40pt**

Essential on small screens to avoid accidental taps.

```swift
// Ensure minimum 40×40pt touch target
Button(action: approve) {
    Image(systemName: "checkmark")
}
.frame(minWidth: 40, minHeight: 40)
```

---

## Resources

- [Apple HIG: Layout for watchOS](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Apple HIG: Supporting Multiple Watch Sizes](https://developer.apple.com/design/human-interface-guidelines/layout)
