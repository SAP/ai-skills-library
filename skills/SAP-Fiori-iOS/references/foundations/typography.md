# Typography — Design Foundations

> SAP Fiori for iOS | Foundation
> Font: SAP 72 | SDK: `Font.fiori(forTextStyle:)` in `FioriThemeManager`

## What is it?

SAP 72 is the primary typeface for SAP Fiori iOS. Font styles map one-to-one with SF font styles, enabling smooth coexistence with SF Symbols and preserving Dynamic Type accessibility support.

---

## 72 Typeface

SAP's proprietary typeface designed for enterprise use. Key properties:

| Property | Detail |
|----------|--------|
| **Legibility** | Optimized for screen use |
| **Font styles** | Robust typographic hierarchy |
| **Brand voice** | Credible and humane |
| **Character set** | Accommodates complex content |
| **Language support** | Windows Glyph List |
| **Accessibility** | Improved character recognition |

---

## Setup (required once at launch)

```swift
// In AppDelegate or App init
Font.registerFioriFonts()
```

If not called, all `Font.fiori()` calls silently fall back to the system font (SF Pro).

---

## Font Style Scale

All 15 styles support Dynamic Type (scale with user's text size preference):

| `FioriTextStyle` | Base pt | Maps to Apple style | Use for |
|-----------------|---------|--------------------|----|
| `.extraLargeTitle` | 52 | `.largeTitle` | Hero / display |
| `.extraLargeTitle2` | 48 | `.largeTitle` | Large display |
| `.largeKPI` | 48 | `.largeTitle` | Large KPI numbers |
| `.KPI` | 36 | `.largeTitle` | KPI metrics |
| `.largeTitle` | 34 | `.largeTitle` | Page titles |
| `.title1` | 28 | `.title` | Section headings |
| `.title2` | 22 | `.title2` | Sub-section headings |
| `.title3` | 20 | `.title3` | Tertiary headings |
| `.headline` | 17 | `.headline` | List row primary text |
| `.body` | 17 | `.body` | Body copy |
| `.callout` | 16 | `.callout` | Supporting text |
| `.subheadline` | 15 | `.subheadline` | Metadata, labels |
| `.footnote` | 13 | `.footnote` | Footnotes, captions |
| `.caption1` | 12 | `.caption` | Small captions |
| `.caption2` | 11 | `.caption2` | Smallest text |

---

## API

```swift
// Scaled — Dynamic Type-aware (preferred)
Font.fiori(forTextStyle: Font.FioriTextStyle) -> Font
Font.fiori(forTextStyle:, weight: Font.FioriWeight) -> Font
Font.fiori(forTextStyle:, weight:, isItalic: Bool) -> Font
Font.fiori(forTextStyle:, weight:, isItalic:, isCondensed: Bool) -> Font

// Fixed size — KPI numbers only
Font.fiori(fixedSize: CGFloat) -> Font
Font.fiori(fixedSize:, weight: Font.FioriWeight) -> Font

// Condensed
Font.fioriCondensed(forTextStyle: Font.FioriTextStyle) -> Font
```

---

## Available Weights

10 constants on `Font.FioriWeight`:

| Weight | Typical use |
|--------|-------------|
| `.ultraLight` | Decorative large text |
| `.thin` | Light display |
| `.light` | KPI numbers, large display |
| `.regular` | Body text (default) |
| `.medium` | Slightly emphasized |
| `.semibold` | Labels, form field labels |
| `.semiboldDuplex` | Special optical variant — same visual weight as semibold, wider spacing |
| `.bold` | Strong emphasis, headings |
| `.heavy` | Display only |
| `.black` | Display only |

> Physical 72 font files: Regular, Light, Bold, Semibold, Condensed, SemiboldDuplex. Other weights are synthesized.

---

## Usage Examples

```swift
// Standard body text
Text("Description")
    .font(.fiori(forTextStyle: .body))

// Bold headline
Text("Invoice #1234")
    .font(.fiori(forTextStyle: .headline, weight: .bold))

// KPI metric — fixed size, light weight
Text("$1.4M")
    .font(.fiori(fixedSize: 36, weight: .light))

// Condensed table label
Text("VENDOR NAME")
    .font(.fiori(forTextStyle: .caption1, isCondensed: true))

// Italic footnote
Text("*Estimated")
    .font(.fiori(forTextStyle: .footnote, isItalic: true))
```

---

## Dynamic Type

SAP 72 integrates with iOS Dynamic Type. Styles scale automatically with the user's preferred text size setting.

```swift
// ✅ Scales with Dynamic Type
Text("Balance")
    .font(.fiori(forTextStyle: .headline))

// ❌ Fixed — does not scale (use only for KPI numbers)
Text("Balance")
    .font(.fiori(fixedSize: 17))
```

Allow text to wrap at large sizes — never truncate labels:

```swift
Text(longLabel)
    .font(.fiori(forTextStyle: .body))
    .lineLimit(nil)          // allow wrapping
    .fixedSize(horizontal: false, vertical: true)
```

---

## Developer Note

Due to UIKit limitations, the `leading` property is not directly modifiable in `UIFont`. SAP Fiori works around this by adding line spacing in attributed strings. See the SDK reference documentation for details.

---

## Do's ✓ / Don'ts ✗

**Do:**
- Always call `Font.registerFioriFonts()` at launch before any view renders
- Use `Font.fiori(forTextStyle:)` for all scalable text
- Use `.light` weight for large KPI numbers — improves readability
- Use fixed size only for KPI figures where precise sizing matters

**Don't:**
- Use `Font.custom("72", size: 17)` directly — always go through `Font.fiori()`
- Hardcode font sizes for body text — use Dynamic Type styles
- Mix SF Pro and SAP 72 in the same text label

---

## Related Foundations

- [accessibility.md](accessibility.md) — Dynamic Type layout patterns at large sizes
