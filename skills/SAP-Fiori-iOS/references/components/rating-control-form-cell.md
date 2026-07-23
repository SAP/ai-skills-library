# Rating Control Form Cell — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIRatingControlFormCell`, SwiftUI `RatingControlFormView`

## What is it?

The rating control form cell displays an average rating for an object within a form, and allows users to set their own rating on a scale from 1 (lowest) to 5 (highest).

---

## Anatomy

```
A. Label        B. Rating Controls
"Satisfaction"  ★ ★ ★ ☆ ☆
```

**A. Label** — describes the intent of the rating.
**B. Rating Controls** — star display. Size and interactivity differ by variation.

---

## Variations

| Variation | Size | Interaction |
|-----------|------|-------------|
| **Display** | Small, read-only | No interaction — shows current average |
| **Interactive** | Larger, tappable | User can set rating by tap or drag |

### Interaction (interactive variation)
- **Tap** individual stars to select a rating
- **Tap and drag** horizontally across stars to choose a rating fluidly

---

## Adaptive Design

On regular width (iPad), the rating control form cell may be displayed in a form sheet, popover, or full-screen modal.

---

## SwiftUI Code Examples

### Interactive rating in a form
```swift
import FioriSwiftUICore

@State private var userRating = 0

RatingControlFormView(
    title: { Text("Your Rating") },
    rating: $userRating,
    ratingControlStyle: .editable,
    ratingBounds: 0...5,
    isRequired: false
)
```

### Display (read-only, shows average)
```swift
RatingControlFormView(
    title: { Text("Customer Satisfaction") },
    rating: .constant(4),
    ratingControlStyle: .standard,
    ratingBounds: 0...5,
    showsValueLabel: true,
    averageRating: 4.2,
    reviewCount: 86
)
```

### Interactive with accumulative value display
```swift
RatingControlFormView(
    title: { Text("Product Rating") },
    rating: $userRating,
    ratingControlStyle: .accumulativeValue,
    ratingBounds: 0...5,
    showsValueLabel: true,
    averageRating: 3.8,
    reviewCount: 214
)
```

### Inside a full form
```swift
Form {
    Section("Feedback") {
        TextFieldFormView(
            title: { Text("Name") },
            text: $reviewerName
        )

        // Display — shows average, read-only
        RatingControlFormView(
            title: { Text("Overall Rating") },
            rating: .constant(averageRating),
            ratingControlStyle: .standard,
            showsValueLabel: true,
            averageRating: averageRating,
            reviewCount: reviewCount
        )

        // Interactive — user sets their rating
        RatingControlFormView(
            title: { Text("Your Rating") },
            rating: $userRating,
            ratingControlStyle: .editable,
            isRequired: true
        )

        NoteFormView(
            title: { Text("Comments") },
            text: $comments
        )
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Variation | Display (read-only) | `ratingControlStyle: .standard` + `.constant(value)` |
| Variation | Interactive | `ratingControlStyle: .editable` + `$binding` |
| Show value label | Yes | `showsValueLabel: true` |
| Show average + count | Yes | `averageRating:` + `reviewCount:` |
| Required | Yes | `isRequired: true` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use the display variation to show an existing average rating (read-only context)
- Use the interactive variation when the user needs to set their own rating
- Support both tap and drag interaction for the interactive variation
- Label the form cell clearly — the label should communicate what is being rated

**Don't:**
- Use an interactive rating control without a way to submit the rating
- Use the display variation where editing is expected — it gives no feedback on tap

---

## Related Components

- [rating-control.md](rating-control.md) — standalone rating control (not in a form)
- [forms.md](forms.md) — other form input cells
