# Status Info Label — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `LabelItem`, SwiftUI `LabelItem`

## What is it?

A status info label provides additional information about an object using a flexible combination of text and an icon. It is a non-interactive display component used in cards, object cells, and object headers.

---

## When to Use

**Do:**
- Display complementary, non-interactive information about an object

**Don't:**
- Use as an interactive component with links

**Top tips:**
- Keep text values concise — avoid complete sentences
- Customize icon + label layout based on needs
- Maximum **two words** for label-only variants

---

## Anatomy

```
[A. Icon]  B. Label  C. Dot  [A. Icon]  B. Label
```

**A. Icon** (optional) — visual illustration; can be leading or trailing relative to the label; can be used independently.
**B. Label** (optional) — short keywords, categories, or status. Can be used independently or with icon.
**C. Dot** (optional) — separator between horizontally arranged status info label items.

---

## Variations (Components)

| Variation | Contents |
|-----------|---------|
| A. Icon only | Visual: icon, image, logo, or avatar |
| B. Label only | Brief text; max **2 words** |
| C. Leading icon | Icon before label |
| D. Trailing icon | Icon after label |

---

## Layout

### Horizontal
Items arranged in a row. Optional dot (•) separator between items. Can wrap to next line.

### Stacked (column)
Items arranged vertically. Can be left or right-aligned.

---

## SwiftUI Code Examples

### Icon only
```swift
Image(systemName: "paperclip")
    .foregroundStyle(Color.preferredColor(.secondaryLabel))
    .font(.fiori(forTextStyle: .footnote))
```

### Label only (max 2 words)
```swift
Text("High Priority")
    .font(.fiori(forTextStyle: .footnote))
    .foregroundStyle(Color.preferredColor(.criticalLabel))
```

### Leading icon + label
```swift
HStack(spacing: 4) {
    Image(systemName: "location")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
    Text("Berlin, DE")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
}
.font(.fiori(forTextStyle: .footnote))
```

### Trailing icon + label
```swift
HStack(spacing: 4) {
    Text("Overdue")
        .foregroundStyle(Color.preferredColor(.negativeLabel))
    Image(systemName: "exclamationmark.circle")
        .foregroundStyle(Color.preferredColor(.negativeLabel))
}
.font(.fiori(forTextStyle: .footnote))
```

### Horizontal row with dot separators
```swift
HStack(spacing: 6) {
    HStack(spacing: 4) {
        Image(systemName: "calendar")
        Text("Due Jan 30")
    }

    Text("•")
        .foregroundStyle(Color.preferredColor(.tertiaryLabel))

    HStack(spacing: 4) {
        Image(systemName: "person")
        Text("Jane Smith")
    }

    Text("•")
        .foregroundStyle(Color.preferredColor(.tertiaryLabel))

    Text("High Priority")
        .foregroundStyle(Color.preferredColor(.criticalLabel))
}
.font(.fiori(forTextStyle: .footnote))
.foregroundStyle(Color.preferredColor(.secondaryLabel))
```

### Stacked column (left-aligned)
```swift
VStack(alignment: .leading, spacing: 4) {
    HStack(spacing: 4) {
        Image(systemName: "calendar")
        Text("Due: Jan 30, 2026")
    }
    HStack(spacing: 4) {
        Image(systemName: "location")
        Text("Berlin, Germany")
    }
    HStack(spacing: 4) {
        Image(systemName: "person")
        Text("Jane Smith")
    }
}
.font(.fiori(forTextStyle: .footnote))
.foregroundStyle(Color.preferredColor(.secondaryLabel))
```

### Inside an ObjectItem (attribute area)
```swift
ObjectItem {
    Text("Invoice #1234")
} subtitle: {
    Text("SAP SE")
} attributeText: {
    // Status info label as attribute
    HStack(spacing: 4) {
        Image(systemName: "clock")
            .foregroundStyle(Color.preferredColor(.criticalLabel))
        Text("Due in 2 days")
            .foregroundStyle(Color.preferredColor(.criticalLabel))
    }
    .font(.fiori(forTextStyle: .footnote))
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Component | Icon only | `Image(systemName:)` |
| Component | Label only | `Text(...)` — max 2 words |
| Component | Leading icon | `HStack { Image, Text }` |
| Component | Trailing icon | `HStack { Text, Image }` |
| Layout | Horizontal | `HStack` with optional `Text("•")` separators |
| Layout | Stacked | `VStack(alignment: .leading)` |
| Alignment | Left | `VStack(alignment: .leading)` |
| Alignment | Right | `VStack(alignment: .trailing)` |
| Interactive | Never | No `.onTapGesture`, no `Button` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Keep labels to 2 words maximum (label-only variant)
- Customize icon placement (leading or trailing) based on reading flow
- Use dot separators in horizontal layouts to visually separate items
- Use semantic color tokens for status-relevant labels (`.negativeLabel`, `.criticalLabel`)

**Don't:**
- Make status info labels interactive — no links, no buttons
- Write complete sentences
- Mix excessive items in a single horizontal row

---

## Related Components

- [object-item.md](object-item.md) — object cell using status info labels as attributes
- [cards.md](cards.md) — status info labels in card extended header
- [object-header.md](object-header.md) — status info labels in header extended area
