# Error Handling — Component Guidelines

> SAP Fiori for iOS | Category: Pattern Overview
> This is a conceptual guide — see the linked component files for implementation details.

## What is it?

Errors communicate to the user that something did not go as intended. Errors can originate at the app level (server error, connectivity) or the user level (invalid input, missing required field). Present the appropriate error type and, when possible, provide recovery instructions.

---

## Error Types

### 1. Error Banner
Used when the state of a workflow is disrupted and may require attention. Non-blocking — the user can continue using the app while the banner is visible. Dismissed via the "Close" button.

**→ See [banner.md](banner.md) for full implementation.**

```swift
BannerMessage {
    Text("Connection lost. Some data may be outdated.")
} icon: {
    Image(systemName: "exclamationmark.triangle.fill")
        .foregroundStyle(Color.preferredColor(.negativeLabel))
} closeAction: {
    showBanner = false
}
```

---

### 2. Full Page Error Message
Used for server-level errors that block the user from viewing the screen. Provides a clear explanation of what went wrong and a way for the user to continue (retry, go back, contact support).

**→ See [illustrated-message.md](illustrated-message.md) for full implementation.**

```swift
IllustratedMessage {
    Image(systemName: "exclamationmark.triangle")
        .font(.system(size: 64))
        .foregroundStyle(Color.preferredColor(.negativeLabel))
        .frame(width: 320, height: 240)  // XL size for full-screen
} title: {
    Text("Something went wrong")
} description: {
    Text("We couldn't load your data. Check your connection and try again.")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
        .multilineTextAlignment(.center)
} action: {
    FioriButton { _ in Text("Retry") }
        .fioriButtonStyle(FioriPrimaryButtonStyle())
}
```

---

### 3. Inline Validation
Used only in form sheets. Displayed directly beneath the input field. Explains the error with suggestions to correct it.

**→ See [inline-validation.md](inline-validation.md) for full implementation.**

```swift
TextFieldFormView(
    title: { Text("Email *") },
    text: $email,
    errorMessage: emailError.map { AttributedString($0) },
    helperText: emailError == nil ? { Text("Enter your SAP email address") } : nil
)
// Error message replaces helper text; reverts to helper text once corrected
```

---

## Choosing the Right Error Type

| Situation | Use |
|-----------|-----|
| Workflow disrupted, user can still navigate | Error banner (`BannerMessage`) |
| Server error blocks the whole screen | Full page error (`IllustratedMessage`) |
| Form field has invalid input | Inline validation (`TextFieldFormView` + `errorMessage`) |
| Multiple form fields invalid | Inline validation per field + optional `BannerMessage` at page level |

---

## Best Practices

- Always explain **what went wrong** — not just "Error"
- Always provide **how to recover** — retry button, back navigation, contact support
- Use semantic error colors: `Color.preferredColor(.negativeLabel)` for error text/icons
- For critical multi-field form errors, combine inline validation with a page-level `BannerMessage`
- For server errors, always offer a retry action or a way to exit the error state

---

## Related Components

- [banner.md](banner.md) — error banner (workflow-level)
- [illustrated-message.md](illustrated-message.md) — full-page error state
- [inline-validation.md](inline-validation.md) — form field errors
- [multi-message-handling.md](multi-message-handling.md) — multiple concurrent errors
