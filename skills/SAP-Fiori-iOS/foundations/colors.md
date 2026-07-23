# Colors — Design Foundations

> SAP Fiori for iOS | Foundation
> Development reference: `FUIColorStyle`
> API: `Color.preferredColor(._token_)`

## What is it?

Color defines visual hierarchy and directs user attention. SAP Fiori iOS uses the **Horizon theme color palette** — a unified system of dynamic colors that adapt to Light mode, Dark mode, and accessibility modes.

**Never hardcode hex values.** Always use `Color.preferredColor(.token)`.

---

## Color Categories

### Background Colors

Two sets: **Background** (flat layouts) and **Grouped Background** (grouped/platter layouts). Each has primary, secondary, and tertiary variants for hierarchy.

**When to use:**
- **Background** — standard table views, flat layouts, white primary background
- **Grouped Background** — grouped table views, platter-based designs

**Hierarchy pattern:**
- Primary → overall view
- Secondary → grouping within the overall view
- Tertiary → grouping within secondary elements

In Dark mode, **Elevated** variants automatically apply to modal sheets, form sheets, and overlay panels — brighter than base colors to make foreground interfaces appear to advance.

| Token | Light | Dark | Use for |
|-------|-------|------|---------|
| `.primaryBackground` | `#F5F6F7` | `#161C21` | Overall view |
| `.secondaryBackground` | `#FFFFFF` | `#242E38` | Grouping within view |
| `.tertiaryBackground` | N/A | `#171D23` | Grouping within secondary |
| `.primaryGroupedBackground` | `#F5F6F7` | `#000000` | Grouped interface main bg |
| `.secondaryGroupedBackground` | `#FFFFFF` | `#161C21` | Grouped cell background |
| `.tertiaryGroupedBackground` | `#F5F6F7` | `#242E38` | Nested grouped cells |

### Tint Colors

Indicate interactive elements (text links, icon buttons, primary buttons) and branded UI areas.

| Token | Light | Dark | Use for |
|-------|-------|------|---------|
| `.tintColor` | `#0070F2` | `#4DB1FF` | Tappable elements (primary button, text links, icon buttons) |
| `.tintColor2` | `#0057D2` | `#4DB1FF` | Tappable elements on lower-contrast backgrounds (secondary tint label) |
| `.tintColor3` | `#0070F2` @ 8% | `#4DB1FF` @ 16% | Secondary tint button background |
| `.tintColorTapState` | `#0040B0` | `#1B90FF` | Tap/pressed state |

### Label Colors

Text hierarchy — five variants from primary to quinary.

| Token | Light | Dark | Use for |
|-------|-------|------|---------|
| `.primaryLabel` | `#223548` | `#F5F6F7` | Primary text, titles |
| `.secondaryLabel` | `#475E75` | `#D5DADD` | Subtitles, secondary text, section headers |
| `.tertiaryLabel` | `#5B738B` | `#A9B4BE` | Footnotes, statuses, placeholders |
| `.quaternaryLabel` | `#8396A8` @ 46% | `#A9B4BE` @ 30% | Disabled text |
| `.quinaryLabel` | `#FFFFFF` | `#000000` | Primary button labels and icons |

### Fill Colors

Transparent fills for elements on top of existing backgrounds.

| Token | Light | Dark | Use for |
|-------|-------|------|---------|
| `.primaryFill` | Grey 5 @ 24% | Grey 5 @ 30% | Thin/small shapes overlay |
| `.secondaryFill` | Grey 5 @ 20% | Grey 5 @ 28% | Medium shapes, button tap states |
| `.tertiaryFill` | Grey 5 @ 15% | Grey 5 @ 20% | Large shapes (secondary button) |
| `.quaternaryFill` | Grey 5 @ 9% | Grey 5 @ 16% | Disabled fills, search bar |

### Separator Colors

| Token | Light | Dark | Use for |
|-------|-------|------|---------|
| `.separator` | Grey 6 @ 37% | Grey 5 @ 37% | Decorative separators, hairlines |
| `.separatorOpaque` | Grey 6 @ 83% | Grey 5 @ 83% | Higher-contrast borders |

### Semantic Colors

Status, state, and priority indicators.

| Token | Light | Dark | Use for |
|-------|-------|------|---------|
| `.negativeLabel` | `#AA0808` | `#FF5C77` | Errors, negative actions |
| `.criticalLabel` | `#A93E00` | `#FFB300` | Warnings, attention needed |
| `.positiveLabel` | `#188918` | `#5DC122` | Success, positive states |
| `.informativeLabel` | `#0057D2` | `#4DB1FF` | Informational |
| `.neutralLabel` | `#354A5F` | `#8396A8` | Neutral priority |
| `.negativeBackground` | Red 6 @ 8% | Red 6 @ 12% | Error background |
| `.criticalBackground` | Mango 6 @ 8% | Mango 6 @ 12% | Warning background |
| `.positiveBackground` | Green 6 @ 8% | Green 6 @ 12% | Success background |
| `.informationBackground` | Blue 6 @ 8% | Blue 6 @ 12% | Info background |
| `.neutralBackground` | Grey 6 @ 8% | Grey 6 @ 12% | Neutral background |

### Accent Colors

10 pairs (label + background) for avatars, icons, data visualizations. All pairs are WCAG-compliant.

| Label token | Background token | Hue |
|------------|----------------|-----|
| `.accentLabel1` | `.accentBackground1` | Mango |
| `.accentLabel2` | `.accentBackground2` | Red |
| `.accentLabel3` | `.accentBackground3` | Raspberry |
| `.accentLabel4` | `.accentBackground4` | Pink |
| `.accentLabel5` | `.accentBackground5` | Indigo |
| `.accentLabel6` | `.accentBackground6` | Blue |
| `.accentLabel7` | `.accentBackground7` | Teal |
| `.accentLabel8` | `.accentBackground8` | Green |
| `.accentLabel9` | `.accentBackground9` | Grey |

### Chart Colors

**Qualitative palette** (data series — use in numbered order):
`.chart1` through `.chart12`. Start with Chart 1 and proceed in sequence.

| Token | Light | Dark |
|-------|-------|------|
| `.chart1` | `#168EFF` | `#3278BE` |
| `.chart2` | `#C87B00` | `#F2A634` |
| `.chart3` | `#75980B` | `#B4CE35` |
| `.chart4` | `#DF1278` | `#FA4F96` |
| … | … | … |
| `.chart12` | `#A68A5B` | `#A68A5B` |

**Semantic palette** (status in charts):
| Token | Use |
|-------|-----|
| `.chartBad` | Negative/bad values |
| `.chartCritical` | Warning values |
| `.chartGood` | Positive/good values |
| `.chartNeutral` | Neutral values |

### Material Colors

Apple Materials with blur/transparency for navigation bars, modals, toolbars.

| Token | Use |
|-------|-----|
| `.chrome` | Navigation bar, toolbar, tab bar, sibling nav — translucency over scrolling content |
| `.chromeSecondary` | Same as Chrome but for page/modal views with secondary backgrounds |

---

## Light & Dark Mode

| Mode | Description |
|------|-------------|
| **Light** (default) | High-contrast UI on light backgrounds; color used sparingly to highlight |
| **Dark** | Dim backgrounds + brighter foregrounds; base vs. elevated backgrounds for depth perception; preserves battery life |

Colors adapt automatically via `Color.preferredColor(.token)` — no manual mode detection needed for standard token usage.

---

## SwiftUI Usage

```swift
// ✅ Always use tokens — never hex values
Text("Invoice #1234")
    .foregroundStyle(Color.preferredColor(.primaryLabel))

Rectangle()
    .fill(Color.preferredColor(.secondaryGroupedBackground))

Image(systemName: "checkmark.circle.fill")
    .foregroundStyle(Color.preferredColor(.positiveLabel))

// ✅ Force a specific appearance
Color.preferredColor(.tintColor, background: .darkConstant)
Color.preferredColor(.primaryLabel, display: .highConstant)  // high contrast

// ❌ Never hardcode
Color(hex: "#0070F2")
```

---

## Related Foundations

- [design-tokens.md](design-tokens.md) — token hierarchy and naming
- [accessibility.md](accessibility.md) — color contrast rules and pairing system
- [theming.md](theming.md) — applying and overriding the color palette
