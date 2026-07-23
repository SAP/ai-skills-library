# Colors — Joule Foundation

> SAP Fiori for iOS | Joule / Foundation

## What is it?

Joule extends the SAP Fiori Horizon color system with a distinct brand palette centered on vibrant purple and electric violet — establishing Joule's identity and helping it stand out among SAP Fiori products.

---

## Joule Brand Colors

| Token | Use |
|-------|-----|
| **Joule Brand** | Core Joule color. Panel header, input field button background, primary Joule button tap state. One of the two Joule gradient variables. |
| **Joule Accent 1** | Joule theme color. Second Joule gradient variable. |
| **Joule Accent 2** | User text message backgrounds. |
| **Joule Accent 3** | List card checkmark and text button. Quick reply state layer at 10% opacity. |
| **Selected Fill** | Conversation list — highlights selected conversation. Search results — highlights matching items. |
| **Joule Gradient** | Quick reply stroke. (Gradient of Joule Brand → Joule Accent 1) |
| **Persistent Label** | Header text, icons, icon background (20% opacity). Welcome message text and Joule icon logo. User text message text. Input field icon. |

---

## Relationship to SAP Fiori Colors

Joule's color system **builds on the Horizon visual theme** — it does not replace it. Standard SAP Fiori UI colors (backgrounds, labels, fills, separators, semantic colors) apply throughout. The Joule brand palette is layered on top for Joule-specific elements.

```swift
import FioriThemeManager

// Standard Fiori tokens — apply everywhere
Color.preferredColor(.primaryLabel)
Color.preferredColor(.primaryBackground)

// Joule brand tokens — Joule-specific elements
Color.preferredColor(.jouleBrand)       // panel header, input button bg
Color.preferredColor(.jouleAccent1)     // theme / gradient 2nd stop
Color.preferredColor(.jouleAccent2)     // user message bubble bg
Color.preferredColor(.jouleAccent3)     // list card checkmark
Color.preferredColor(.jouleGradient1)   // gradient start
Color.preferredColor(.jouleGradient2)   // gradient end
Color.preferredColor(.jouleSelectedFill) // selected conversation
Color.preferredColor(.jouleSelectedLabel)
```

---

## Elevation in Joule

Joule uses shadows to suggest elevation — sharper for base-layer components, softer for elevated components. The Joule card system also uses an outline to create stronger contrast. Follows [../foundations/elevation.md](../foundations/elevation.md).

---

## Light & Dark Mode

| Mode | Description |
|------|-------------|
| **Light** (default) | Joule brand colors on light Horizon backgrounds |
| **Dark** | Dimmer backgrounds, brighter foreground colors; Joule brand remains vibrant |

Colors adapt automatically via `Color.preferredColor(.token)` — same API as standard Fiori colors.

---

## Accessibility

Joule follows the same WCAG compliance standards as SAP Fiori iOS. Color pairings use the Horizon pairing system. See [../foundations/accessibility.md](../foundations/accessibility.md) and [../foundations/colors.md](../foundations/colors.md).

---

## Related Foundations

- [../foundations/colors.md](../foundations/colors.md) — full Fiori color token reference
- [../foundations/elevation.md](../foundations/elevation.md) — shadow levels
- [../foundations/accessibility.md](../foundations/accessibility.md) — contrast ratios
