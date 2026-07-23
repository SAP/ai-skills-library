# SAP Fiori iOS — Color Token Quick Reference

All colors are accessed via `Color.preferredFioriColor(forStyle: .<tokenName>)`.
Colors are dynamic — they automatically switch between Light and Dark mode.

## Core Semantic Tokens (use these first)

| Token | Light Hex | Dark Hex | Use for |
|-------|-----------|----------|---------|
| `.primaryLabel` | `#32363A` | `#FFFFFF` | Primary text |
| `.secondaryLabel` | `#6A6D70` | `#A8AAAC` | Secondary/supporting text |
| `.tertiaryLabel` | `#89919A` | `#8396A8` | Tertiary/placeholder text |
| `.quaternaryLabel` | `#B0B5BA` | `#5B7085` | Hint, disabled text |
| `.tintColor` | `#0070F2` | `#4DB1FF` | Interactive / brand blue |
| `.tintColor2` | `#0040B0` | `#85CAFF` | Secondary interactive |
| `.primaryBackground` | `#FFFFFF` | `#1C2228` | Main screen background |
| `.secondaryBackground` | `#F5F6F7` | `#29343D` | Grouped sections, cards |
| `.tertiaryBackground` | `#EDEFF0` | `#354045` | Tertiary surfaces |
| `.primaryGroupedBackground` | `#F5F6F7` | `#1C2228` | Inset grouped tables |
| `.secondaryGroupedBackground` | `#FFFFFF` | `#29343D` | Grouped cell background |
| `.tertiaryGroupedBackground` | `#F5F6F7` | `#354045` | Nested grouped |
| `.separator` | `#E5E5EA` | `#38434D` | List / divider lines |

## Semantic Status Tokens

| Token | Light | Dark | Use for |
|-------|-------|------|---------|
| `.positiveLabel` | `#256F3A` | `#30914C` | Success, positive values |
| `.negativeLabel` | `#BB0000` | `#FF8888` | Error, negative values |
| `.criticalLabel` | `#E9730C` | `#FFBA00` | Warning / critical |
| `.informativeLabel` | `#0070F2` | `#4DB1FF` | Informational |
| `.positiveBackground` | `#F5FAE5` | `#0E2B16` | Success background |
| `.negativeBackground` | `#FFEAF4` | `#350000` | Error background |
| `.criticalBackground` | `#FFF8D6` | `#450B00` | Warning background |
| `.informativeBackground` | `#EBF8FF` | `#00144A` | Info background |

## Fill Tokens

| Token | Use for |
|-------|---------|
| `.primaryFill` | Filled controls background (light fills) |
| `.secondaryFill` | Secondary fills |
| `.tertiaryFill` | Tertiary fills |
| `.quaternaryFill` | Quaternary fills |
| `.tintColorTapState` | Button/tap highlight over tintColor |

## Chart Color Tokens

| Token | Use for |
|-------|---------|
| `.chart1` – `.chart12` | Data series colors |
| `.chartGood` | Positive chart indicators |
| `.chartNeutral` | Neutral chart indicators |
| `.chartCritical` | Critical/warning chart indicators |
| `.stockUpStroke` | Stock up indicator |
| `.stockDownStroke` | Stock down indicator |

## Accent Colors (decorative labels + backgrounds)

| Label Tokens | Background Tokens |
|-------------|-------------------|
| `.accentLabel1` – `.accentLabel10` | `.accentBackground1` – `.accentBackground10` |

## Core Palette (avoid in UI — use semantic tokens above)

| Range | Lightest | Darkest |
|-------|----------|---------|
| Grey | `grey1` (#F5F6F7) | `grey11` (#12171C) |
| Blue | `blue1` (#EBF8FF) | `blue11` (#00144A) |
| Teal | `teal1` (#DAFDF5) | `teal11` (#012931) |
| Green | `green1` (#F5FAE5) | `green11` (#0E2B16) |
| Mango | `mango1` (#FFF8D6) | `mango11` (#450B00) |
| Red | `red1` (#FFEAF4) | `red11` (#350000) |
| Pink | `pink1` (#FFF0FA) | `pink11` (#28004A) |
| Raspberry | `raspberry1` (#FFF0F5) | `raspberry11` (#510136) |
| Indigo | `indigo1` (#F1ECFF) | `indigo11` (#0E0637) |

## SwiftUI Usage Pattern

```swift
// ✅ Correct — dynamic color token
Text("Invoice #123")
    .foregroundStyle(Color.preferredColor(.primaryLabel))

Rectangle()
    .fill(Color.preferredColor(.secondaryBackground))

// ✅ Status color
Image(systemName: "checkmark.circle")
    .foregroundStyle(Color.preferredColor(.positiveLabel))

// ❌ Never hardcode hex
Text("Invoice")
    .foregroundColor(Color(hex: "#32363A"))  // WRONG
```
