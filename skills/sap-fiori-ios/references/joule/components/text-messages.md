# Text Messages — Joule Component

> SAP Fiori for iOS | Joule / Components

## What is it?

Text messages display the conversation between Joule and the user. Two categories: messages from Joule and messages from the user.

---

## Rules

**Do:**
- Use for most Joule-generated content — follow-up questions, simple information
- Right-align user messages (LTR devices)
- Dynamically adjust user message bubble shape based on position

**Don't:**
- Use for complex information like objects, statuses, tags — use Object Cards instead
- Use colors outside the Joule Foundations library
- Change positioning, spacing, or expansion behavior

---

## Anatomy

### Joule messages
- **Left-aligned** (LTR)
- **No bubbles** — text displayed directly

### User messages
**A. Bubble** — contains user text; position/spacing determined by surrounding elements
**B. Text message** — user's content
**C. Arm** — dynamic indicator showing position relative to other messages

---

## Message Position & Arms

| Position | Arm |
|----------|-----|
| Single message | No arm |
| Starting (first of group) | Arm at **bottom** of bubble |
| Center (between messages) | Arms at **top and bottom** |
| Ending (last of group) | Arm at **top** of bubble |

---

## Max Width

Messages maintain a minimum padding on each side to preserve sender distinction — Joule messages have right padding, user messages have left padding. Messages never span full panel width.

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct JouleConversationView: View {
    let messages: [ConversationMessage]

    var body: some View {
        ScrollViewReader { proxy in
            ScrollView {
                LazyVStack(spacing: 0) {
                    ForEach(Array(messages.enumerated()), id: \.element.id) { i, message in
                        switch message.sender {
                        case .joule:
                            // Left-aligned, no bubble
                            HStack {
                                Text(message.text)
                                    .font(.fiori(forTextStyle: .body))
                                    .foregroundStyle(Color.preferredColor(.primaryLabel))
                                    .frame(maxWidth: .infinity, alignment: .leading)
                                    .padding(.trailing, 48)  // min right padding
                                Spacer()
                            }
                            .padding(.horizontal, 16)
                            .padding(.vertical, messages[i].spacing(from: messages))

                        case .user:
                            // Right-aligned with bubble
                            HStack {
                                Spacer()
                                UserMessageBubble(
                                    text: message.text,
                                    position: message.position(in: messages)
                                )
                                .padding(.leading, 48)  // min left padding
                            }
                            .padding(.horizontal, 16)
                            .padding(.vertical, 2)  // 4pt between same-sender messages
                        }
                    }
                }
                .padding(.top, 16)
            }
        }
    }
}

// User bubble with dynamic arm
struct UserMessageBubble: View {
    let text: String
    let position: MessagePosition  // .single, .starting, .center, .ending

    var body: some View {
        Text(text)
            .font(.fiori(forTextStyle: .body))
            .foregroundStyle(Color.preferredColor(.persistentLabel))
            .padding(12)
            .background(Color.preferredColor(.jouleAccent2))  // Joule brand color
            .clipShape(RoundedRectangle(cornerRadius: cornerRadius(for: position)))
        // Arm positioning based on position enum
    }
}
```

---

## Related

- [../foundations/layout.md](../foundations/layout.md) — spacing rules
- [input-field.md](input-field.md)
- [../foundations/colors.md](../foundations/colors.md)
