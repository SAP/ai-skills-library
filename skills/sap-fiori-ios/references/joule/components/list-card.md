# List Card — Joule Component

> SAP Fiori for iOS | Joule / Components

## What is it?

The Joule list card displays a set of items or links in list format. Used to show people, products, services, organizations, actions, or options.

---

## Rules

**Do:** Use to show actionable or navigable list content.
**Don't:** Use when there is too much content.

**Tips:**
- Keep list items relevant and titles consistent
- Keep icons consistent — all items have icons, or none do
- Keep right accessories consistent
- Prioritize most relevant information, top to bottom

---

## Anatomy

**A. Container** — holds header, body, footer
**B. Header** (optional) — icon/image, title, counter, status, subtitle, description
**C. Body** — list items; each can have icon/image, title, subtitle, description, action button
**D. Footer** (optional) — list-level actions and/or "View More" expansion

---

## Behavior

### Detail View (optional)
Tap a list item → detail view slides in from right; "Back" returns to conversation.

### "View More"
- Default: shows **3 items**
- "View More" appears when more exist; shows up to 3 more per tap
- **Maximum: 20 items total**

### Overflow
More than 1 action per item → overflow button (•••) → selection menu with up to 3 actions.

### Error
No content → show appropriate error handling (illustrated message).

---

## Variations

- **With / without header** — header adds title, subtitle, description context
- **With / without footer** — footer adds list-level CTA and/or "View More"

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct JouleListCard: View {
    let items: [ListCardItem]
    let totalCount: Int
    @State private var visibleCount = 3

    var body: some View {
        VStack(spacing: 0) {
            // B. Header (optional)
            CardHeader {
                Text("Open Invoices")
            } subtitle: {
                Text("\(totalCount) total")
                    .foregroundStyle(Color.preferredColor(.secondaryLabel))
            }

            // C. Body — list items
            ForEach(items.prefix(visibleCount)) { item in
                ObjectItem {
                    Text(item.title)
                } subtitle: {
                    Text(item.subtitle)
                } status: {
                    Text(item.status)
                        .foregroundStyle(Color.preferredColor(.secondaryLabel))
                }
                .onTapGesture { navigateToDetail(item) }
                Divider().padding(.leading, 16)
            }

            // D. Footer — "View More"
            if visibleCount < min(totalCount, 20) {
                FioriButton { _ in Text("View More (\(totalCount - visibleCount))") }
                    .fioriButtonStyle(FioriTertiaryButtonStyle())
                    .frame(maxWidth: .infinity)
                    .padding(12)
                    .onTapGesture {
                        visibleCount = min(visibleCount + 3, 20)
                    }
            }
        }
        .background(Color.preferredColor(.secondaryGroupedBackground))
        .clipShape(RoundedRectangle(cornerRadius: 12))
        .shadow(color: Color.preferredColor(.cardShadow), radius: 4, x: 0, y: 2)
    }
}
```

---

## Related

- [object-card.md](object-card.md)
- [../../components/object-cell.md](../../components/object-cell.md)
- [../../components/cards.md](../../components/cards.md)
