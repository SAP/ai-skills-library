# Object Card — Joule Component

> SAP Fiori for iOS | Joule / Components
> Extends: [../../components/cards.md](../../components/cards.md)

## What is it?

Object cards in Joule preview a business object. Tapping navigates to a detail view with more information.

---

## Rules

**Do:** Use as a teaser/preview for detailed object content.
**Don't:** Place unrelated elements in a card.

**Tips:**
- Keep focused on one topic, self-contained
- Present information compactly and scannably
- Use a reasonable number of UI elements

---

## Anatomy

**A. Container** — holds header, body, footer
**B. Header** — title (required) + optionally: avatar, subtitle, status row, description, counter
**C. Body** (optional) — flexible content: media header, avatar, subtitle, description, counter
**D. Footer** (optional) — up to 3 action buttons

---

## Behavior

### Detail View (optional)
Tap card → Joule panel transitions to detail view of the object. "Back" returns to conversation.

### Error
No content to display → show appropriate error handling (illustrated message).

### Max Width
Cards fill container width up to a maximum for readability across devices.

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct JouleObjectCard: View {
    let card: JouleCardData
    let onTap: (() -> Void)?

    var body: some View {
        Card {
            // B. Header — title required
            Text(card.title)
                .font(.fiori(forTextStyle: .headline))
        } subtitle: {
            Text(card.subtitle)
                .foregroundStyle(Color.preferredColor(.secondaryLabel))
        } status: {
            Text(card.status)
                .foregroundStyle(Color.preferredColor(.secondaryLabel))
        } body: {
            // C. Body (optional)
            if let detail = card.detail {
                Text(detail)
                    .font(.fiori(forTextStyle: .body))
                    .padding(16)
            }
        } footer: {
            // D. Footer — max 3 buttons
            HStack(spacing: 12) {
                ForEach(card.actions.prefix(3)) { action in
                    FioriButton { _ in Text(action.label) }
                        .fioriButtonStyle(FioriSecondaryButtonStyle())
                        .onTapGesture { action.handler() }
                }
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 12)
        }
        .onTapGesture { onTap?() }  // opens detail view if enabled
    }
}
```

---

## Related

- [list-card.md](list-card.md)
- [carousel.md](carousel.md)
- [../../components/cards.md](../../components/cards.md)
