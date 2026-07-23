# Theming — Design Foundations

> SAP Fiori for iOS | Foundation
> Development reference: `ThemeManager.shared`, UI Theme Designer

## What is it?

Theming applies a color palette and logo to define a system-wide visual appearance for an app. It creates visual harmony, enhances readability, and expresses product branding across platforms.

---

## Themeable Elements

| Element | Description |
|---------|-------------|
| **Logo** | Visual symbol expressing the product's identity |
| **Tint colors** | Applied to interactive elements (buttons, icons, tabs, links) |
| **Semantic colors** | Colors communicating state, priority, or destructive/confirmational actions |
| **Accent colors** | Decorative colors bringing additional color variety to the UI |
| **Text colors** | All text content including numbers and symbols |
| **Surface** | Backgrounds of elevated components (cards, app bars, bottom nav) |
| **Background** | Main app background behind scrollable content |

---

## Theming Scenarios

### Basic Theme
Change only logo and primary tint. Keep default text, background, semantic, and accent colors from the Horizon baseline.

**Elements changed:** Logo, Tint

Sufficient to communicate brand without a major visual overhaul. Most apps start here.

### Detailed Theme
Full overhaul to match brand look and feel.

**Elements changed:** Logo, Tint, Text, Background, Semantic colors, Accent colors

---

## Theming Strategy

### Single-Theme Strategy
One theme for all users. Choose based on company branding or primary use environment:
- **Light theme** — brighter, suited for indoor/outdoor bright lighting
- **Dark theme** — more serious tone, suited for dim office/nighttime environments

### Two-Theme Strategy (industry standard)
Supports both Light and Dark modes to adapt to the user's lighting environment and system settings. All foreground colors must be considered on both themes.

---

## SwiftUI Implementation

### Setup at launch

```swift
// AppDelegate or App init
import FioriThemeManager

ThemeManager.shared.setPaletteVersion(.v8)   // pin to Fiori Next palette
Font.registerFioriFonts()                     // SAP 72 typeface
```

### Token overrides (basic theme — tint only)

```swift
// Override tint color to brand color
ThemeManager.shared.setHexColor("FF6000", for: .tintColor, variant: .light)
ThemeManager.shared.setHexColor("FF8844", for: .tintColor, variant: .dark)
```

### Stylesheet (detailed theme)

```swift
// Load brand stylesheet at launch
try? StyleSheetSettings.loadStylesheetByString(content: """
    @tintColor_lightBackground: #FF6000;
    @tintColor_darkBackground: #FF8844;
    @primaryLabel_lightBackground: #1A1A2E;
    @primaryLabel_darkBackground: #F0F0F0;
    @primaryBackground_lightBackground: #FAFAFA;
    @primaryBackground_darkBackground: #0D0D1A;
""")

// Or from a file
try? StyleSheetSettings.loadStylesheetByURL(brandStylesheetURL)
```

### Reset to default

```swift
ThemeManager.shared.reset()  // clears all overrides, reverts to Horizon defaults
```

---

## Color Priority Order

When resolving a color, the system applies overrides in this priority:

1. Stylesheet overrides (highest)
2. `ThemeManager.shared.setHexColor/setColor` overrides
3. Palette version default (`.v8`)
4. System fallback (lowest)

---

## Do's ✓ / Don'ts ✗

**Do:**
- Apply all theme overrides at app launch — never inside views
- Start with a basic theme (logo + tint) and expand as needed
- Test both light and dark variants when applying a two-theme strategy
- Ensure all foreground colors have been considered on both themes

**Don't:**
- Override token colors inside SwiftUI views
- Mix manual hex values in component code with theme overrides
- Forget to test semantic colors (error, warning, success) under the custom theme — they must remain readable

---

## Related Foundations

- [colors.md](colors.md) — full color token reference
- [design-tokens.md](design-tokens.md) — token hierarchy and naming
