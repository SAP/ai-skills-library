# Avatars — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIImageView`, UIKit `groupedAvatarsViews`, SwiftUI `AvatarStack`

## What is it?

An avatar is a visual element used to display images — user profiles, user initials, placeholder images, icons, or business-related images such as product pictures.

Two shapes exist with distinct semantic meaning:
- **Round** — represents a person, user profile, initials, or generic icon
- **Rounded square (thumbnail)** — represents a business object such as a product, document, or icon

---

## When to Use

**Do:**
- Use an avatar to display user profiles, user initials, placeholder images, icons, or business-related images such as product pictures.
- Use a round avatar to represent a user or profile within list rows, collection views, or cards.
- Use a round avatar to display user initials or generic icons.
- Use a rounded square avatar (thumbnail) to display an image of an object, such as a product, within list rows, collection views, or cards.
- Use an indicator (badge) on the avatar to display a status.

**Don't:**
- Don't use an avatar for interactive icons. Use a `FioriButton` with an icon inside instead.

---

## Anatomy

### A. Avatar
The avatar is a container — round or rounded-square — holding an image, icon, or initials.

- **Round** → user / person / profile
- **Rounded square (thumbnail)** → object / product / business image

### B. Badge (optional)
An optional badge in the bottom-right corner indicates a status (online, away, busy, etc.).

### C. Avatar Stack
Multiple avatars grouped horizontally. Maximum 6 visible; the 6th (or last) shows the overflow count ("+N").

- Avatar stack: round avatars only, **16pt** size
- Avatar group: round avatars, **16pt** (default) or **24pt**

### D. Label (optional)
A short descriptive label that can be positioned before, after, above, or below the avatar stack. Long labels wrap by default; wrapping can be overridden by the parent component.

---

## Sizes

Use these predefined sizes for visual consistency, especially when avatars are inset into other components:

| Size | Common use |
|------|-----------|
| 16pt | Avatar stack only |
| 24pt | Avatar group, compact inline |
| 32pt | List row secondary |
| 40pt | List row primary (`ObjectItem`, `ContactItem`) |
| 44pt | List row touch target minimum |
| 48pt | Card header |
| 60pt | Profile summary |
| 90pt | Profile header (`ProfileHeader`) |
| 110pt | Prominent profile / hero |

As a standalone component there is more flexibility, but always use one of these sizes when the avatar is embedded inside another Fiori component.

---

## Shape

| Context | Shape |
|---------|-------|
| User / person / initials / generic icon | Round (`.clipShape(Circle())`) |
| Product / object / business image / icon for object | Rounded square (`.clipShape(RoundedRectangle(cornerRadius: 8))`) |

---

## Color

By default, avatars with initials use the SAP Fiori accent color palette (`.accentLabel1`–`.accentLabel10` paired with `.accentBackground1`–`.accentBackground10`). Assign accent colors consistently per user or object — do not randomize on each render.

---

## Behavior

Avatars are typically **not interactive** — they serve a decorative or informational purpose as part of a parent component (card, list row, header). Do not add tap gestures to an avatar unless it navigates to a profile or detail screen.

---

## SwiftUI Code Examples

### Round avatar — photo
```swift
AsyncImage(url: user.avatarURL) { image in
    image
        .resizable()
        .aspectRatio(contentMode: .fill)
        .clipShape(Circle())
} placeholder: {
    Circle().fill(Color.preferredColor(.secondaryBackground))
}
.frame(width: 40, height: 40)
```

### Round avatar — initials fallback
```swift
Circle()
    .fill(Color.preferredColor(.accentBackground3))
    .frame(width: 40, height: 40)
    .overlay(
        Text(user.initials)  // e.g. "JS"
            .font(.fiori(forTextStyle: .subheadline, weight: .semibold))
            .foregroundStyle(Color.preferredColor(.accentLabel3))
    )
```

### Rounded square avatar — product / object thumbnail
```swift
AsyncImage(url: product.imageURL) { image in
    image
        .resizable()
        .aspectRatio(contentMode: .fill)
        .clipShape(RoundedRectangle(cornerRadius: 8))
} placeholder: {
    RoundedRectangle(cornerRadius: 8)
        .fill(Color.preferredColor(.secondaryBackground))
}
.frame(width: 40, height: 40)
```

### Avatar with status badge
```swift
ZStack(alignment: .bottomTrailing) {
    // Avatar
    Circle()
        .fill(Color.preferredColor(.accentBackground2))
        .frame(width: 40, height: 40)
        .overlay(
            Text(user.initials)
                .font(.fiori(forTextStyle: .subheadline))
                .foregroundStyle(Color.preferredColor(.accentLabel2))
        )

    // Status badge
    Circle()
        .fill(Color.preferredColor(.positiveLabel))  // online = positive
        .frame(width: 10, height: 10)
        .overlay(Circle().stroke(Color.preferredColor(.primaryBackground), lineWidth: 1.5))
        .offset(x: 2, y: 2)
}
```

### AvatarStack (up to 6, with overflow)
```swift
import FioriSwiftUICore

// SDK component
AvatarStack(avatarsTitle: AttributedString("+\(max(0, users.count - 3))")) {
    Avatars {
        ForEach(users.prefix(3)) { user in
            Circle()
                .fill(Color.preferredColor(.accentBackground2))
                .frame(width: 16, height: 16)
                .overlay(
                    Text(user.initials)
                        .font(.fiori(fixedSize: 7))
                        .foregroundStyle(Color.preferredColor(.accentLabel2))
                )
        }
    }
}
```

### AvatarStack with label (positioned after)
```swift
HStack(spacing: 8) {
    AvatarStack(avatarsTitle: AttributedString("+2")) {
        Avatars {
            Image("user1").clipShape(Circle()).frame(width: 16, height: 16)
            Image("user2").clipShape(Circle()).frame(width: 16, height: 16)
            Image("user3").clipShape(Circle()).frame(width: 16, height: 16)
        }
    }
    Text("5 participants")
        .font(.fiori(forTextStyle: .footnote))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
        .lineLimit(2)  // allow wrap per spec — label is not truncated
}
```

### Inside ObjectItem
```swift
ObjectItem {
    Text("Sprint Review")
} subtitle: {
    Text("5 participants")
} detailContent: {
    AvatarStack(avatarsTitle: AttributedString("+2")) {
        Avatars {
            Image("a1").clipShape(Circle()).frame(width: 16, height: 16)
            Image("a2").clipShape(Circle()).frame(width: 16, height: 16)
            Image("a3").clipShape(Circle()).frame(width: 16, height: 16)
        }
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Shape | Round | `.clipShape(Circle())` |
| Shape | Rounded square | `.clipShape(RoundedRectangle(cornerRadius: 8))` |
| Content | Photo | `AsyncImage` or `Image` |
| Content | Initials | `Text(initials)` overlay on colored shape |
| Content | Icon | `Image(systemName:)` overlay on colored shape |
| Size | 16pt | Avatar stack only |
| Size | 24pt | Compact group |
| Size | 40pt | Standard list row |
| Size | 90pt | Profile header |
| Badge | Status | `ZStack` with small `Circle` bottom-trailing |
| Stack | Yes | `AvatarStack` with `Avatars {}` |
| Stack label position | After | `HStack` with label trailing |
| Stack label position | Below | `VStack` with label below |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use **round** for people, **rounded square** for objects — consistently
- Limit avatar stack to **6 avatars maximum**; show "+N" for overflow
- Use accent color pairs (`.accentBackground` + `.accentLabel`) for initials avatars
- Assign accent colors deterministically (e.g. based on user ID mod 10) — not randomly
- Allow the avatar stack label to wrap to a new line when truncated
- Use 40pt in standard list rows (`ObjectItem`, `ContactItem`)

**Don't:**
- Use an avatar as an interactive element — use `FioriButton` with an icon instead
- Mix round and rounded-square avatars in the same stack
- Use more than 6 avatars in a stack without the overflow count
- Use raw palette colors for initials — always use the accent token pairs

---

## Related Components

- [contact-item.md](contact-item.md) — avatar in a contact list row
- [profile-header.md](profile-header.md) — large profile avatar
- [object-item.md](object-item.md) — avatar/thumbnail in a list row
