# Design Tokens — Design Foundations

> SAP Fiori for iOS | Foundation
> Related: [colors.md](colors.md), [theming.md](theming.md)

## What is it?

Design tokens are stored pieces of UI information (color, spacing, sizing, typography) that make up the design system's visual identity. They provide cross-platform consistency between iOS and Android, maintain visual consistency, scale design decisions, and are easy to update globally.

---

## Token Hierarchy

Three levels, each adding a layer of abstraction:

```
Reference Tokens  →  Semantic Tokens  →  Component Usage
(raw values)         (role-based)         (UI elements)

blue7 = #0070F2  →  tintColor = blue7  →  Button.foreground = tintColor
```

### Reference Tokens
Store static raw values (hex codes, line heights, type sizes). Named by value, not by usage.

**Never use reference tokens directly in UI components.** They are the foundation for semantic tokens only.

```swift
// ❌ Reference token — do not use directly in UI
// blue7 = #0070F2

// ✅ Semantic token — use this instead
Color.preferredColor(.tintColor)
```

### Semantic Tokens
Define the specific role of a reference token within the UI. Enable theming across iOS and Android. Each semantic token stores both light and dark mode values.

```swift
// Semantic token — maps to correct value for current mode
Color.preferredColor(.primaryLabel)       // light: #223548 / dark: #F5F6F7
Color.preferredColor(.tintColor)          // light: #0070F2 / dark: #4DB1FF
Color.preferredColor(.negativeLabel)      // light: #AA0808 / dark: #FF5C77
```

---

## Token Naming Structure

`sap.[level].[category].[group].[usage].[scale]`

| Part | Values | Example |
|------|--------|---------|
| Company | `sap` | `sap` |
| Level | `ref` (reference), `sem` (semantic) | `sem` |
| Category | `color`, `spacing`, `sizing`, `cornerRadius`, `typography` | `color` |
| Group (color only) | `brand`, `neutral`, `status`, `accents`, `header` | `neutral` |
| Usage (color only) | `background`, `foreground`, `stroke` | `foreground` |
| Scale | Number sequence | `1`, `2`, `3` |

---

## Light and Dark Mode

Each semantic token stores values for both **Morning Horizon** (light) and **Evening Horizon** (dark) modes. Apply a token once — it adapts automatically.

```swift
// One token, adapts to both modes
Color.preferredColor(.primaryLabel)  // light + dark handled automatically
```

---

## Accessibility Modes

In addition to light and dark, iOS semantic tokens also store values for:
- **Increased Contrast Light**
- **Increased Contrast Dark**

These activate when the user enables **Settings → Accessibility → Increase Contrast**. No code change needed — `Color.preferredColor(.token)` with `display: .device` handles it automatically.

```swift
Color.preferredColor(.primaryLabel, display: .device)       // follows system setting
Color.preferredColor(.primaryLabel, display: .highConstant) // always high contrast
```

---

## Native OS Mapping

Semantic tokens map to the native OS APIs, preserving native iOS components, behaviors, and interactions. This gives a unified workflow across iOS and Android while keeping each platform's native character.

```
Semantic Token (Horizon)  →  iOS System Token  →  Component Token
.tintColor                →  .systemBlue        →  Button.tint
```

---

## Theme Swapping

The Horizon palette is the baseline theme, but the entire token system can be swapped to a company's brand colors. Changing the reference tokens cascades through every semantic token and every component that uses them — no component-level changes needed.

```swift
// Override individual tokens at launch
ThemeManager.shared.setHexColor("FF6000", for: .tintColor, variant: .light)
ThemeManager.shared.setHexColor("FF8844", for: .tintColor, variant: .dark)

// Or load a full brand stylesheet
try? StyleSheetSettings.loadStylesheetByString(content: """
    @tintColor_lightBackground: #FF6000;
    @tintColor_darkBackground: #FF8844;
""")
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Always use semantic tokens in UI components
- Let the token system handle light/dark/contrast mode — don't detect manually
- Override tokens at the theme level (launch), not at the component level

**Don't:**
- Use reference tokens directly in UI
- Hardcode hex values
- Create local color constants that duplicate token values

---

## Related Foundations

- [colors.md](colors.md) — full semantic token reference
- [theming.md](theming.md) — applying and overriding the token system
