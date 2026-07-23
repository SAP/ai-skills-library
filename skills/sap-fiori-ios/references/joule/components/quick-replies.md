# Quick Replies — Joule Component

> SAP Fiori for iOS | Joule / Components

## What is it?

Quick replies offer guided preset answers users can select, streamlining interaction. Unlike menu selection, quick replies **disappear after selection**.

---

## Rules

**Do:**
- Keep text under **20 characters** per reply
- Keep count under **6** replies
- List most likely to be tapped replies first

**Don't:**
- Exceed **32 characters** (including spaces) per reply
- Provide more than **11** quick reply options

---

## Anatomy

**A. Container** — holds quick reply text
**B. Text** — expected user response; truncates, does not wrap

---

## States

| State | Visual |
|-------|--------|
| Enabled | Default — interactive |
| Tapped | Pressed feedback |
| Disabled | Dimmed — not interactive |

---

## Behavior

- Tap a quick reply → sends it as a user text message
- **All quick replies in the group disappear** after selection
- Text truncates; does not wrap (consistent heights)
- Max width = group container width; group max width constrained for readability

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct QuickRepliesView: View {
    let replies: [String]  // max 11; recommend ≤6
    let onSelect: (String) -> Void
    @State private var dismissed = false

    var body: some View {
        if !dismissed {
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 8) {
                    ForEach(replies.prefix(11), id: \.self) { reply in
                        FioriButton { _ in
                            Text(reply)
                                .lineLimit(1)  // truncate — no wrap
                        }
                        .fioriButtonStyle(FioriSecondaryButtonStyle())
                        .onTapGesture {
                            onSelect(reply)
                            dismissed = true  // all replies disappear
                        }
                    }
                }
                .padding(.horizontal, 16)
            }
        }
    }
}
```

---

## Related

- [menu-selection.md](menu-selection.md) — list persists after selection
- [text-messages.md](text-messages.md)
