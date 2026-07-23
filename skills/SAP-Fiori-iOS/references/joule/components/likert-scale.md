# Likert Scale — Joule Component

> SAP Fiori for iOS | Joule / Components

## What is it?

A Likert scale presents ordered response options for users to indicate agreement, satisfaction, or sentiment within Joule conversational flows. Dismissed after selection to keep conversation focused.

---

## Rules

**Do:**
- Use for measuring attitudes, sentiment, or subjective feedback
- Use clear, plain-language labels easy to understand at a glance
- Consider cognitive load when choosing number of scale points

**Don't:**
- Use vague or ambiguous labels
- Use for binary decisions (use a button or quick reply instead)

---

## Anatomy

**A. Likert Scale Item** — a single selectable option representing one point on the scale

Maximum: **7 items**

---

## Behavior

- Tap a Likert scale item → sends a user message with the selected item's content
- Likert scale **dismisses** after selection (keeps conversation focused)

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct LikertScaleView: View {
    let items: [String]  // max 7
    let onSelect: (String) -> Void

    var body: some View {
        HStack(spacing: 8) {
            ForEach(items.prefix(7), id: \.self) { item in
                FioriButton { _ in
                    Text(item)
                        .font(.fiori(forTextStyle: .footnote))
                }
                .fioriButtonStyle(FioriSecondaryButtonStyle())
                .onTapGesture {
                    onSelect(item)
                    // Joule posts item as user message then dismisses scale
                }
            }
        }
        .padding(.horizontal, 16)
    }
}

// Example 5-point satisfaction scale
LikertScaleView(
    items: ["Very Unsatisfied", "Unsatisfied", "Neutral", "Satisfied", "Very Satisfied"]
) { selected in
    sendUserMessage(selected)
    hideLikertScale()
}
```

---

## Related

- [quick-replies.md](quick-replies.md)
- [text-messages.md](text-messages.md)
