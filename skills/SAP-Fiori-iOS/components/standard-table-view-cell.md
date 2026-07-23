# Standard Table View Cell — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Table View Cells
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: SwiftUI native `List` row

## What is it?

A standard table view cell is a highly customizable list cell used as a navigational element that leads to a detail page.

---

## When to Use

**Do:**
- Use as a navigational element to a detail page

**Don't:**
- Use as an editable field — use text input form cells instead

---

## Anatomy

```
A. Icon Stack  B. Detail Image  C. Main Content (label*)  D. Right Accessory  E. Disclosure
(optional)     (optional)       (* only mandatory item)   (optional)          (optional)
```

**A. Icon Stack** — up to 3 vertically stacked icons left of the detail image. Indicates unread state, attachments, etc.

**B. Detail Image** — 44px frame. Min 16px, max 60px.
- Circular frame → person/user
- Square frame → object

**C. Main Content** — label is the only mandatory element.

**D. Right Accessory** — vertically or horizontally stacked labels/icons indicating condition, priority, or status.

**E. Disclosure Content** — trailing edge. Navigation indicator (chevron, etc.).

---

## SwiftUI Code Examples

### Navigation row
```swift
NavigationLink(destination: DetailView(item: item)) {
    HStack {
        Image(systemName: item.icon)
            .foregroundStyle(Color.preferredColor(.tintColor))
            .frame(width: 28)
        Text(item.label)
            .font(.fiori(forTextStyle: .body))
    }
}
```

### With right accessory (status label)
```swift
HStack {
    Image(systemName: "doc.text")
        .foregroundStyle(Color.preferredColor(.tintColor))
    Text("Contract Template")
        .font(.fiori(forTextStyle: .body))
    Spacer()
    Text("Active")
        .font(.fiori(forTextStyle: .footnote))
        .foregroundStyle(Color.preferredColor(.positiveLabel))
}
```

### With detail image + label + disclosure
```swift
NavigationLink(destination: CategoryDetail(category: cat)) {
    HStack(spacing: 12) {
        Image(cat.iconName)
            .resizable()
            .frame(width: 40, height: 40)
            .clipShape(RoundedRectangle(cornerRadius: 8))  // square = object
        Text(cat.name)
            .font(.fiori(forTextStyle: .body))
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Detail image | Circular | `.clipShape(Circle())` |
| Detail image | Square | `.clipShape(RoundedRectangle(cornerRadius: 8))` |
| Disclosure | Chevron | `NavigationLink` (automatic) |
| Right accessory | Status label | `Spacer()` + `Text(...)` |
| Icon stack | 1–3 icons | `VStack` of `Image` left of detail image |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use for navigation to a detail page
- Use circular images for people, square for objects

**Don't:**
- Use for editable inputs
- Use more than 3 icons in the icon stack

---

## Related Components

- [object-cell.md](object-cell.md) — richer version with more content zones
- [key-value-table-view-cell.md](key-value-table-view-cell.md) — read-only key/value display
