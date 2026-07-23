# Timestamp — Joule Component

> SAP Fiori for iOS | Joule / Components

## What is it?

Timestamps provide temporal context in the Joule panel, indicating when messages were sent. They appear only at the **beginning of a conversation**.

---

## Anatomy

**A. Day/Date** — when the message was sent
**B. Time** — time of day

---

## Variations

| Condition | Day/Date display |
|-----------|----------------|
| Message sent today | "Today" |
| Message sent yesterday | "Yesterday" |
| Any other day | Day of week + date (e.g. "Tuesday, Jan 28") |

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct ConversationTimestamp: View {
    let date: Date

    var dayLabel: String {
        if Calendar.current.isDateInToday(date) {
            return "Today"
        } else if Calendar.current.isDateInYesterday(date) {
            return "Yesterday"
        } else {
            let formatter = DateFormatter()
            formatter.dateFormat = "EEEE, MMM d"  // "Tuesday, Jan 28"
            return formatter.string(from: date)
        }
    }

    var timeLabel: String {
        let formatter = DateFormatter()
        formatter.timeStyle = .short  // follows locale: "9:30 AM" or "09:30"
        return formatter.string(from: date)
    }

    var body: some View {
        VStack(spacing: 2) {
            Text(dayLabel)
                .font(.fiori(forTextStyle: .footnote, weight: .semibold))
                .foregroundStyle(Color.preferredColor(.secondaryLabel))
            Text(timeLabel)
                .font(.fiori(forTextStyle: .caption1))
                .foregroundStyle(Color.preferredColor(.tertiaryLabel))
        }
        .frame(maxWidth: .infinity)
        .padding(.bottom, 24)  // 24pt spacing to next content group (from layout.md)
    }
}
```

---

## Related

- [text-messages.md](text-messages.md)
- [joule-panel.md](joule-panel.md)
- [../foundations/layout.md](../foundations/layout.md)
- [../../foundations/time-and-date-formats.md](../../foundations/time-and-date-formats.md)
