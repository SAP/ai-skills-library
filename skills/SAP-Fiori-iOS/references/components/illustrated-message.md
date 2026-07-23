# Illustrated Message — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Feedback
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIIllustratedMessage`, SwiftUI `IllustratedMessage`

## What is it?

An illustrated message communicates empty, error, and success states through a combination of solution-oriented messages, engaging illustrations, and a conversational tone. It turns a negative situation into a better user experience while ensuring consistency across the app.

---

## When to Use

Use the illustrated message when you want to improve the user experience for one or more message states in your application. Place it in:
- Full-screen pages
- Dialogs
- Cards

**Do not** use a banner or toast message for high-priority empty, error, or success states — those are for system-level transient notifications.

---

## Top Tips

**Turn a negative event into a positive one.** A well-designed illustrated message that leaves users feeling understood can result in a neutral or even positive reaction.

**Write coherent, solution-oriented messages.** The illustration, title, and call to action must work together as one unit. Never use an illustration without a message. A message + illustration is more powerful than a message alone.

**Tailor text to the use case.** Replace generic terms with specific business object names:
- ❌ "No data yet / When there is you'll see it here."
- ✅ "No orders yet / When there are, you'll see them here."

Replace generic criteria terms too:
- ❌ "No results found / Try changing your search criteria."
- ✅ "No suppliers found / Try adjusting your filter settings."

**Prioritize message over illustration.** When the container is too small to show all elements, remove the illustration so the full message remains readable.

---

## Anatomy

```
      [A. Illustration]     ← optional

       B. Title             ← always present, single line preferred

    C. Description          ← optional, ≤2 sentences

  [D. CTA Button 1] [D. CTA Button 2]   ← optional, max 2
```

### A. Illustration (optional)
Helps clarify the situation and adds personality. Must be appropriate for the container. Can use app-specific illustrations or the core design team's illustration library. Must conform to preset illustration sizes (see Adaptive Design).

### B. Title
Explains the state in simple words. **Sentence case.** Preferably one line. Default text can be customized for the specific use case.

### C. Description (optional)
Adds detail and prompts the next step. Max two sentences. Customize default text to fit the context.

### D. Call to Action (optional)
Maximum **two** CTA buttons. Style is flexible but must be consistent across the app.

---

## Illustration Sizes

Use fixed sizes matched to the container:

| Size | Dimensions | Container |
|------|-----------|-----------|
| **XL** | 320×240pt | Full-screen page, full-screen dialog |
| **L** | 160×160pt | Page section, larger dialogs, large cards (2×3, 2×2) |
| **M** | 92×92pt | Page section, smaller dialogs, medium card (2×1) |
| **S** | 64×64pt | Smaller dialogs, small card (1×1) |
| **XS** | 48×48pt | Smaller dialogs, small card (1×1) |

---

## Adaptive Design

### Message Width
- **Stretch** — message content fills the maximum container width
- **Fixed** — message container uses a fixed width for visual cohesion across a set of illustrated messages

### Call-to-Action Layout
- Buttons can be aligned: left, right, center, or fill
- Two buttons can be **horizontal** (side by side) or **vertical** (stacked)
- If two horizontal buttons exceed the container width, the layout **automatically switches to vertical**

---

## Variations

### Empty State
No content to display. Common use cases:
- Empty list, table, or inbox
- No notifications or planned activities
- State before a first search

### Error State
Caused by missing permissions, incorrect configuration, or a system issue. Common use cases:
- Unable to load, upload, or connect
- No search results found

### Success State
Action completed without errors. Common use cases:
- Reaching a daily goal or target
- Completing a work task

### Custom States
The component is flexible — customize title, description, CTA label, and illustration. Custom illustrations must conform to the preset illustration size dimensions above.

---

## SwiftUI Code Examples

### Full-screen empty state (Size XL illustration)
```swift
import FioriSwiftUICore

IllustratedMessage {
    // XL illustration: 320×240pt
    Image("illustration_no_orders")
        .resizable()
        .aspectRatio(contentMode: .fit)
        .frame(width: 320, height: 240)
} title: {
    Text("No orders yet")
        .font(.fiori(forTextStyle: .title2))
} description: {
    Text("When there are, you'll see them here.")
        .font(.fiori(forTextStyle: .body))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
        .multilineTextAlignment(.center)
} action: {
    FioriButton { _ in Text("Create Order") }
        .fioriButtonStyle(FioriPrimaryButtonStyle())
}
```

### Error state with retry
```swift
IllustratedMessage {
    Image(systemName: "exclamationmark.triangle")
        .font(.system(size: 64))
        .foregroundStyle(Color.preferredColor(.criticalLabel))
        .frame(width: 92, height: 92)  // Size M
} title: {
    Text("Couldn't load invoices")
} description: {
    Text("Check your connection and try again.")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
        .multilineTextAlignment(.center)
} action: {
    FioriButton { _ in Text("Retry") }
        .fioriButtonStyle(FioriSecondaryButtonStyle())
}
```

### Success state
```swift
IllustratedMessage {
    Image("illustration_task_complete")
        .resizable()
        .aspectRatio(contentMode: .fit)
        .frame(width: 160, height: 160)  // Size L
} title: {
    Text("Order submitted")
} description: {
    Text("Your purchase order has been sent for approval. You'll be notified once it's reviewed.")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
        .multilineTextAlignment(.center)
} action: {
    FioriButton { _ in Text("View Order") }
        .fioriButtonStyle(FioriPrimaryButtonStyle())
}
```

### Two CTA buttons (horizontal → vertical fallback)
```swift
IllustratedMessage {
    Image(systemName: "lock.slash")
        .font(.system(size: 64))
        .foregroundStyle(Color.preferredColor(.tertiaryLabel))
} title: {
    Text("Access denied")
} description: {
    Text("You don't have permission to view this content. Contact your administrator.")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
        .multilineTextAlignment(.center)
} action: {
    // Horizontal layout — auto-switches to vertical if too wide
    ViewThatFits(in: .horizontal) {
        HStack(spacing: 12) {
            FioriButton { _ in Text("Request Access") }
                .fioriButtonStyle(FioriPrimaryButtonStyle())
            FioriButton { _ in Text("Go Back") }
                .fioriButtonStyle(FioriSecondaryButtonStyle())
        }
        VStack(spacing: 12) {
            FioriButton { _ in Text("Request Access") }
                .fioriButtonStyle(FioriPrimaryButtonStyle())
                .frame(maxWidth: .infinity)
            FioriButton { _ in Text("Go Back") }
                .fioriButtonStyle(FioriSecondaryButtonStyle())
                .frame(maxWidth: .infinity)
        }
    }
}
```

### In a card body (illustration removed — container too small)
```swift
// Size M or smaller containers: drop illustration, keep message
Card {
    Text("Recent Activity")
} body: {
    IllustratedMessage {
        // No illustration — container too small to fit all elements
        EmptyView()
    } title: {
        Text("No activity yet")
    } description: {
        Text("Activity will appear here once available.")
            .font(.fiori(forTextStyle: .footnote))
            .foregroundStyle(Color.preferredColor(.secondaryLabel))
            .multilineTextAlignment(.center)
    }
    .padding(16)
}
```

### Pre-search empty state (no CTA)
```swift
IllustratedMessage {
    Image(systemName: "magnifyingglass")
        .font(.system(size: 64))
        .foregroundStyle(Color.preferredColor(.tertiaryLabel))
} title: {
    Text("Search for suppliers")
} description: {
    Text("Enter a name or ID above to find suppliers.")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
        .multilineTextAlignment(.center)
}
// No action button — user needs to search first
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| State | Empty | SF Symbol or custom illustration |
| State | Error | `.criticalLabel` or `.negativeLabel` icon |
| State | Success | `.positiveLabel` icon or custom illustration |
| Illustration | XL | `.frame(width: 320, height: 240)` |
| Illustration | L | `.frame(width: 160, height: 160)` |
| Illustration | M | `.frame(width: 92, height: 92)` |
| Illustration | S | `.frame(width: 64, height: 64)` |
| Illustration | XS | `.frame(width: 48, height: 48)` |
| Illustration | None | `EmptyView()` (small containers) |
| CTA | 1 button | Single `FioriButton` |
| CTA | 2 buttons horizontal | `HStack` with `ViewThatFits` fallback |
| CTA | 2 buttons vertical | `VStack` |
| Message width | Fixed | `.frame(maxWidth: 280)` |
| Message width | Stretch | `.frame(maxWidth: .infinity)` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Always include a title — never use an illustration alone
- Customize default text with business-object-specific language
- Remove the illustration when the container is too small to show all elements
- Use the correct illustration size for the container (XL for full-screen, S/XS for small cards)
- Maintain consistent CTA button styles across all illustrated messages in the app
- Keep description to two sentences maximum

**Don't:**
- Use a banner or toast for high-priority empty/error/success states — use illustrated message
- Use an illustration that is unrelated to the message
- Use generic terms ("data", "object") when specific terms are available
- Include more than two CTA buttons
- Place an illustrated message inside a banner

---

## Related Components

- [banner.md](banner.md) — system-level transient notifications
- [loading-indicator.md](loading-indicator.md) — loading states before content appears
- [forms.md](forms.md) — inline field-level validation
