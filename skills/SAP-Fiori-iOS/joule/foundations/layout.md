# Layout — Joule Foundation

> SAP Fiori for iOS | Joule / Foundation

## What is it?

Joule's layout organizes conversational elements clearly and intuitively — messages, input fields, and interactive components — to ensure smooth communication, quick comprehension, and accessibility.

---

## Horizontal Spacing

**Panel padding: 16pt**

The padding between all elements and the Joule panel border is 16pt. The top padding within the conversation container is also 16pt.

```swift
// Panel content padding
.padding(.horizontal, 16)
.padding(.top, 16)
```

---

## Vertical Spacing

Three main content groupings in the Joule panel:
1. Timestamp
2. Content sent by the user
3. Content created by Joule

### Between groupings: 24pt

| Gap | Value |
|-----|-------|
| Between timestamp and user content | 24pt |
| Between user content and Joule content | 24pt |

```swift
VStack(spacing: 24) {
    TimestampView()
    UserMessageGroup()
    JouleResponseGroup()
}
```

### Within the same grouping

| Gap | Value | Between |
|-----|-------|---------|
| Between user text messages | 4pt | Two messages from the same user |
| Between Joule text messages | 12pt | Two text messages from Joule |
| Between interactive components | 16pt | Quick reply, object card, illustrated message, menu selection, list |
| Between text message and interactive component | 16pt | Joule text → any interactive component |

```swift
// User messages (4pt)
VStack(spacing: 4) {
    UserTextBubble(text: message1)
    UserTextBubble(text: message2)
}

// Joule text messages (12pt)
VStack(spacing: 12) {
    JouleTextMessage(text: response1)
    JouleTextMessage(text: response2)
}

// Interactive components (16pt)
VStack(spacing: 16) {
    JouleTextMessage(text: intro)
    QuickReplyRow(replies: replies)      // 16pt after text
    ObjectCard(data: cardData)           // 16pt between interactive components
}
```

### Response actions: 4pt below Joule responses

Response actions appear under every Joule response group (text messages, cards, illustrated messages, etc.).

```swift
VStack(spacing: 4) {
    JouleResponseGroup()
    ResponseActionsRow()  // always 4pt below
}
```

---

## Spacing Summary

| Context | Value |
|---------|-------|
| Panel horizontal padding | 16pt |
| Panel top padding | 16pt |
| Between content groupings (timestamp / user / Joule) | 24pt |
| Between user text messages | 4pt |
| Between Joule text messages | 12pt |
| Between interactive components | 16pt |
| Between text message and interactive component | 16pt |
| Between Joule response and response actions | 4pt |

---

## Full Conversation Layout Example

```swift
ScrollView {
    VStack(spacing: 0) {
        // Timestamp
        TimestampView(date: timestamp)
            .padding(.bottom, 24)

        // User message group
        VStack(spacing: 4) {
            UserTextBubble(text: "Show me open invoices")
            UserTextBubble(text: "For this month")
        }
        .padding(.bottom, 24)

        // Joule response group
        VStack(alignment: .leading, spacing: 12) {
            JouleTextMessage(text: "Here are your open invoices for July:")
            JouleTextMessage(text: "I found 18 invoices totaling $42,600.")
        }

        // Interactive component — 16pt after last Joule text
        VStack(spacing: 16) {
            EmptyView()  // spacing from text above
                .frame(height: 16)
            ObjectCard(data: invoiceCard)
            QuickReplyRow(replies: ["See all", "Filter by vendor", "Export"])
        }

        // Response actions — 4pt below
        ResponseActionsRow()
            .padding(.top, 4)
    }
    .padding(.horizontal, 16)
    .padding(.top, 16)
}
```

---

## Related Foundations

- [../foundations/adaptive-layout.md](../foundations/adaptive-layout.md)
- [colors.md](colors.md)
