# Iconography — Design Foundations

> SAP Fiori for iOS | Foundation
> Resources: SAP Fiori Icon Library, SF Symbols (Apple HIG)

## What is it?

Iconography is essential to a cohesive app experience. Icons communicate actions, information, feedback, and navigation. SAP icons have been redesigned for the Horizon visual theme — fresh, friendly, bold, with consistency of size, stroke, and visual balance for enterprise use.

---

## When to Use

**Do:**
- Use the SAP icon library for SAP Fiori apps
- Use icons to communicate important actions efficiently
- Use icons to indicate navigation to other screens

**Don't:**
- Use third-party icons
- Place icons too close together
- Use half-pixel increments for icon placement
- Use light-colored icons against light backgrounds

---

## SAP Design Principles for Icons

| Principle | Meaning |
|-----------|---------|
| Simple | Clear metaphors, minimal detail |
| Fresh | Modern, approachable aesthetic |
| Neutral | Enterprise-appropriate, not playful |
| Modern | Aligned with current design language |

---

## Icon Sources

### SAP Fiori Custom Symbols (SDK)
The SAP Fiori Icon Library is available as a **custom symbol library** in the SDK. Supports multiple weights and scales: thin, light, regular, bold, heavy, etc.

```swift
import FioriThemeManager

// SAP Fiori icon
FioriIcon.actions.favorite
FioriIcon.actions.unfavorite

// As SwiftUI Image
Image(fioriName: "some.icon.name")
    .foregroundStyle(Color.preferredColor(.tintColor))
```

### SF Symbols (Apple)
Use SF Symbols when no SAP-specific icon is needed. SAP 72 font and SF Symbols coexist — the 72 typeface maps one-to-one with SF font styles.

```swift
// SF Symbol
Image(systemName: "plus.circle.fill")
    .foregroundStyle(Color.preferredColor(.tintColor))
    .font(.fiori(forTextStyle: .title2))

// Accessibility label required for icon-only interactive elements
Image(systemName: "trash")
    .accessibilityLabel("Delete")
```

---

## Usage Hierarchy

**Use SAP Fiori custom symbols when:**
- The icon represents an SAP-specific business action or object
- The designer has specified a Fiori icon from the icon library
- The icon is a standard SAP brand element

**Use SF Symbols when:**
- A matching system symbol exists for a common iOS action (add, delete, share, etc.)
- The icon needs to match Apple's native UI patterns

---

## Sizing

| Context | Size | SwiftUI |
|---------|------|---------|
| Navigation bar | 24pt | `.font(.fiori(forTextStyle: .title3))` |
| Toolbar / tab bar | 28pt | `.font(.fiori(forTextStyle: .title2))` |
| Inline with body text | 17pt | `.font(.fiori(forTextStyle: .body))` |
| List row accent | 17pt | `.font(.fiori(forTextStyle: .headline))` |
| Large / hero | 48pt+ | `.font(.fiori(fixedSize: 48))` |

---

## Color

Always use Fiori color tokens for icon colors — never hardcode:

```swift
// Interactive icon
Image(systemName: "square.and.pencil")
    .foregroundStyle(Color.preferredColor(.tintColor))

// Status icon
Image(systemName: "checkmark.circle.fill")
    .foregroundStyle(Color.preferredColor(.positiveLabel))

// Secondary / decorative icon
Image(systemName: "info.circle")
    .foregroundStyle(Color.preferredColor(.secondaryLabel))

// Disabled icon
Image(systemName: "bell")
    .foregroundStyle(Color.preferredColor(.quaternaryLabel))
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Add `.accessibilityLabel()` to every icon-only interactive element
- Use `.accessibilityHidden(true)` for purely decorative icons
- Match icon color to context: `.tintColor` for actions, `.secondaryLabel` for decorative
- Use consistent icon weights within the same component

**Don't:**
- Use third-party icon sets
- Use light icons on light backgrounds
- Place icons with sub-pixel alignment
- Crowd icons too close together

---

## Resources

- [SAP Fiori Icon Library (SAPUI5 Icon Explorer)](https://sapui5.hana.ondemand.com/sdk/#/topic/21ea0ea94614480d9a910b2e93431291)
- [SF Symbols — Apple HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)
