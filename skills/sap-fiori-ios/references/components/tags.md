# Tags — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIButton` (tag style), SwiftUI `Tag`

## What is it?

Tags display quick, useful bits of information — keywords, labels, categories, or statuses. They are **not interactive** and serve as independent bits of information with a visually distinct appearance from plain text.

---

## When to Use

**Do:**
- Keep tag labels concise — max **2 words** recommended
- Use to display complementary information about an object

**Don't:**
- Write full sentences in a tag
- Place icons or images inside a tag
- Overload with excessive tags or very long text values

---

## Anatomy

```
A. Container (filled or outlined)
B. Label
```

**A. Container** — two styles: filled (default) or outlined.
**B. Label** — keyword or short information. Max 2 words.

---

## Variations

### Style
| Style | Visual |
|-------|--------|
| Filled (default) | Solid background fill |
| Outlined | Transparent background with border |

### Color
| Color | Use |
|-------|-----|
| Default (grey) | General tags |
| Accent colors | Categorical differentiation using `.accentBackground` + `.accentLabel` pairs |

---

## Layout

Tags are **not interactive**. Multiple tags line up horizontally. The row can wrap to the next line depending on the parent container.

---

## SwiftUI Code Examples

### Basic tag (filled, default grey)
```swift
import FioriSwiftUICore

Tag("Finance")

// Or manually:
Text("Finance")
    .font(.fiori(forTextStyle: .footnote))
    .foregroundStyle(Color.preferredColor(.primaryLabel))
    .padding(.horizontal, 8)
    .padding(.vertical, 4)
    .background(Color.preferredColor(.secondaryBackground))
    .clipShape(Capsule())
```

### Outlined style
```swift
Text("Q4 2026")
    .font(.fiori(forTextStyle: .footnote))
    .foregroundStyle(Color.preferredColor(.primaryLabel))
    .padding(.horizontal, 8)
    .padding(.vertical, 4)
    .overlay(Capsule().stroke(Color.preferredColor(.separator), lineWidth: 1))
    .clipShape(Capsule())
```

### Accent color tag
```swift
Text("High Priority")
    .font(.fiori(forTextStyle: .footnote))
    .foregroundStyle(Color.preferredColor(.accentLabel1))
    .padding(.horizontal, 8)
    .padding(.vertical, 4)
    .background(Color.preferredColor(.accentBackground1))
    .clipShape(Capsule())
```

### Horizontal tag row (wrapping)
```swift
// Wrapping tag row
let tags = ["Finance", "Q4 2026", "EMEA", "Approved"]

FlowLayout(spacing: 6) {
    ForEach(tags, id: \.self) { tag in
        Tag(tag)
    }
}

// Non-wrapping (scrollable if overflow)
ScrollView(.horizontal, showsIndicators: false) {
    HStack(spacing: 6) {
        ForEach(tags, id: \.self) { tag in Tag(tag) }
    }
}
```

### Inside ObjectItem
```swift
ObjectItem {
    Text("Invoice #1234")
} subtitle: {
    Text("SAP SE")
} tags: {
    Tag("Finance")
    Tag("Overdue")
}
```

### Inside card header (extended header)
```swift
Card {
    Text("Sales Order #5678")
} tags: {
    Tag("Open")
    Tag("High Priority")
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Style | Filled | `.background(Color.preferredColor(.secondaryBackground))` |
| Style | Outlined | `.overlay(Capsule().stroke(...))` |
| Color | Default grey | `.secondaryBackground` fill |
| Color | Accent | `.accentBackground1`–`.accentBackground10` + matching label |
| Layout | Horizontal row | `HStack` or `ScrollView(.horizontal)` |
| Layout | Wrapping | `FlowLayout` or `LazyVGrid` |
| Interactive | Never | No `.onTapGesture`, no `Button` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Keep labels to max 2 words
- Use accent color pairs (background + label) consistently per category
- Allow tag rows to wrap when space is constrained

**Don't:**
- Make tags tappable/interactive
- Place icons or images inside tags
- Write sentences or long labels

---

## Related Components

- [object-cell.md](object-cell.md) — uses tags in main content area
- [cards.md](cards.md) — tags in card header
- [filter-feedback-bar.md](filter-feedback-bar.md) — filter chips (similar appearance, but interactive)
