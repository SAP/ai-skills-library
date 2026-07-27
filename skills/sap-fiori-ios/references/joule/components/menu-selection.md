# Menu Selection — Joule Component

> SAP Fiori for iOS | Joule / Components

## What is it?

Menu selection presents a list of preset options users can select to answer Joule. Unlike quick replies, the list **remains visible after selection**.

---

## Rules

**Do:**
- List important/frequently used items first
- Group logically related items
- Keep the list manageable

**Don't:**
- Mix items with icons and items without icons in the same list

---

## Anatomy

**A. Menu selection item** — a button from the list
**B. Icon** (optional) — must be consistent (all items have icons, or none do)
**C. Label** — mandatory; describes the triggered action

Recommended initial display: **3–5 items**
Maximum: **15 items**
"View All" appears when list has **>6 items**

---

## Behavior

- Tap a menu item → sends chosen item as a user message
- List **remains visible** after selection (unlike quick replies which disappear)
- "View All (#)" button → shows all remaining items

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct JouleMenuSelection: View {
    let items: [MenuSelectionItem]  // max 15
    let onSelect: (MenuSelectionItem) -> Void
    @State private var showAll = false

    var visibleItems: [MenuSelectionItem] {
        showAll ? items : Array(items.prefix(6))
    }
    var hasMore: Bool { items.count > 6 && !showAll }

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            ForEach(visibleItems) { item in
                FioriButton { _ in
                    HStack(spacing: 12) {
                        if let icon = item.icon {
                            icon.foregroundStyle(Color.preferredColor(.tintColor))
                        }
                        Text(item.label)
                            .font(.fiori(forTextStyle: .body))
                            .foregroundStyle(Color.preferredColor(.primaryLabel))
                        Spacer()
                    }
                    .padding(12)
                }
                .buttonStyle(.plain)
                .onTapGesture { onSelect(item) }

                Divider()
            }

            // "View All" button
            if hasMore {
                FioriButton { _ in Text("View All (\(items.count))") }
                    .fioriButtonStyle(FioriTertiaryButtonStyle())
                    .frame(maxWidth: .infinity)
                    .padding(12)
                    .onTapGesture { showAll = true }
            }
        }
        .background(Color.preferredColor(.secondaryGroupedBackground))
        .clipShape(RoundedRectangle(cornerRadius: 12))
    }
}
```

---

## Related

- [quick-replies.md](quick-replies.md)
- [list-card.md](list-card.md)
