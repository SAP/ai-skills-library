# Error Handling — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns
> Extends: [../../components/illustrated-message.md](../../components/illustrated-message.md)

## What is it?

Joule error handling uses illustrated messages to inform users when something goes wrong and guide recovery where possible.

**Use illustrated message** unless the issue can be solved conversationally.

---

## Anatomy

**A. Header** — short sentence summarizing the error
**B. Description** — 1–3 sentences; further details + guidance
**C. Illustration** (optional)
**D. CTA button** (optional) — action to fix or retry

---

## Error Types

### In-Chat Errors (appear within conversation)

| Type | Description | CTA? |
|------|-------------|------|
| **Empty/No Result** | Joule processed request but no content to show | No |
| **Non-Recoverable Service Error** (4xx) | Backend issue; user can't fix it | No — provide info or async link to submit a ticket |
| **Recoverable (Temporary Interruption)** | Network or coverage issue; retry likely fixes it | Yes — "Retry" |

### Interruption Errors (attached to bottom of panel, blocks input)

| Type | Description |
|------|-------------|
| **Pre-Conversation Error** | Error before any conversation exists — no canvas to host in-chat message; input field disabled |
| **Timeout** | Max session time reached; user must restart session |

---

## SwiftUI Code Example

```swift
// Recoverable in-chat error
IllustratedMessage {
    Image(systemName: "wifi.slash")
        .font(.system(size: 64))
        .foregroundStyle(Color.preferredColor(.criticalLabel))
} title: {
    Text("Connection issue")
} description: {
    Text("Joule couldn't connect. Please try again.")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
} action: {
    FioriButton { _ in Text("Retry") }
        .fioriButtonStyle(FioriSecondaryButtonStyle())
        .onTapGesture { retryRequest() }
}

// Pre-conversation interruption error (blocks input field)
VStack {
    Spacer()
    IllustratedMessage {
        // error illustration
    } title: {
        Text("Joule is unavailable")
    } description: {
        Text("Unable to start a conversation. Please try again later.")
    }
    // Input field disabled
}
```

---

## Related

- [../components/illustrated-message.md](../components/illustrated-message.md)
- [confirmation.md](confirmation.md)
