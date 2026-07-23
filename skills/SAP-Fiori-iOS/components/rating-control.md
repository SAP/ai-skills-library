# Rating Control — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIRatingControl`, SwiftUI `RatingControl`

## What is it?

The rating control displays an average rating for an object and allows users to set their own rating on a scale of 1 (lowest) to 5 (highest).

---

## Anatomy

```
A. Leading text   B. ★ ★ ★ ☆ ☆   C. Trailing text
  (optional)         (stars)         (optional)
```

**A. Leading text** (optional) — describes the average rating value (read-only states).
**B. Rating Controls** — star display.
**C. Trailing text** (optional) — average rating value or total number of ratings.

---

## Star Display Rules

| State | Star types allowed |
|-------|-------------------|
| Editable / Disabled | Full stars and empty stars only |
| Read-only (multiple ratings) | Full stars, empty stars, **and half stars** |

### Half-star threshold rule (read-only)
On a 0–5 scale:
- < 0.75 → half star
- 0.75–1.25 → full star
- 1.25–1.75 → full star + half star
- (pattern continues in 0.5 increments)

---

## Variations

### Read-Only
Displays rating in large or small format. Non-interactive.

- **Large** — standard display size
- **Small** — compact; used in filter form cell buttons, data table cells, object cells
- **Accented** — uses semantic colors instead of default star color

### Interactive (Editable)
Larger, tappable variant. Used in forms and table view cells when the user rates an object.

**Interaction:**
- Tap individual stars to select
- Tap and drag horizontally to slide to a rating

### Disabled
Same visual as editable, but non-interactive (dimmed).

---

## SwiftUI Code Examples

### Read-only (large, with average and count)
```swift
import FioriSwiftUICore

RatingControl(
    rating: .constant(4),
    ratingControlStyle: .standard,
    ratingBounds: 0...5,
    showsValueLabel: true,
    averageRating: 4.3,
    reviewCount: 128
)
// Displays: ★★★★☆  4.3 (128)
```

### Read-only small (for object cells, data table)
```swift
RatingControl(
    rating: .constant(3),
    ratingControlStyle: .standard,
    ratingBounds: 0...5
)
// Small variant used inline
```

### Read-only accented (semantic colors)
```swift
RatingControl(
    rating: .constant(5),
    ratingControlStyle: .standard,
    ratingBounds: 0...5,
    isAccented: true  // uses semantic colors
)
```

### Interactive (editable)
```swift
@State private var userRating = 0

RatingControl(
    rating: $userRating,
    ratingControlStyle: .editable,
    ratingBounds: 0...5,
    showsValueLabel: true
)
// Supports tap + drag to select rating
```

### Accumulative (aggregate with user's own rating)
```swift
RatingControl(
    rating: $userRating,
    ratingControlStyle: .accumulativeValue,
    ratingBounds: 0...5,
    showsValueLabel: true,
    averageRating: 3.8,
    reviewCount: 214
)
```

### Disabled
```swift
RatingControl(
    rating: .constant(3),
    ratingControlStyle: .editableDisabled,
    ratingBounds: 0...5
)
```

### In a filter form cell (small, for rating filter)
```swift
FilterFeedbackBarItem(
    title: AttributedString("4★ & above"),
    accessoryIcon: Image(systemName: "star.fill")
        .foregroundStyle(Color.preferredColor(.criticalLabel))
)
// Or inline small RatingControl inside a filter chip
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Style | Read-only large | `ratingControlStyle: .standard` |
| Style | Read-only small | `.standard` (compact size context) |
| Style | Accented | `isAccented: true` |
| Style | Interactive/Editable | `ratingControlStyle: .editable` |
| Style | Disabled | `ratingControlStyle: .editableDisabled` |
| Style | Accumulative | `ratingControlStyle: .accumulativeValue` |
| Half stars | Yes (read-only only) | Automatic when `averageRating` is fractional |
| Leading text | Yes | `leadingText: AttributedString(...)` |
| Trailing text | Yes | `showsValueLabel: true` + `reviewCount:` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use half stars only in read-only multi-rating displays — never in editable/disabled states
- Use the small variant when embedding in object cells, data tables, or filter chips
- Support both tap and drag in interactive mode

**Don't:**
- Use half stars in editable or disabled states
- Use the large interactive variant inline in dense lists — it takes too much space

---

## Related Components

- [rating-control-form-cell.md](rating-control-form-cell.md) — rating control inside a form cell
- [object-item.md](object-item.md) — object cells that can display small read-only ratings
