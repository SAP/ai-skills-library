# Illustrated Message — Joule Component

> SAP Fiori for iOS | Joule / Components
> Extends: [../../components/illustrated-message.md](../../components/illustrated-message.md)

## What is it?

Joule-specific illustrated messages communicate empty, error, and success states for conversation content. Follow the base component guidelines with Joule-specific constraints.

---

## Joule-Specific Rules

- **Use horizontal layout** for both illustrated message and buttons — conserves vertical space in the panel
- **Use Size S (64×64pt) or XS (48×48pt)** illustrations — prevents excess whitespace
- **Only use Joule Foundations colors** for CTA buttons
- **Do not set a custom width** — the component is purposefully contained to fit the Joule panel

---

## Anatomy

**A. Container** — fills panel width up to max width
**B. Illustration** (optional) — Size S or XS; from app library or core design team
**C. Title** — sentence case; one line preferred
**D. Description** (optional) — max 3 sentences
**E. CTAs** (optional) — up to 2 buttons; horizontal layout preferred

---

## States

| State | Common Joule use cases |
|-------|----------------------|
| Empty | Empty list, no notifications |
| Error | Unable to load/connect, no search results |
| Success | Daily goal reached, task completed |
| Custom | App-specific use cases |

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

// Joule illustrated message — horizontal layout, Size S illustration
IllustratedMessage {
    Image("illustration_error")
        .resizable().aspectRatio(contentMode: .fit)
        .frame(width: 64, height: 64)  // Size S
} title: {
    Text("Unable to load")
} description: {
    Text("Check your connection and try again.")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
} action: {
    // Horizontal CTA layout
    HStack(spacing: 12) {
        FioriButton { _ in Text("Retry") }
            .fioriButtonStyle(FioriSecondaryButtonStyle())
        FioriButton { _ in Text("Cancel") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
    }
}
// Do not set custom width — let panel container constrain it
```

---

## Related

- [../../components/illustrated-message.md](../../components/illustrated-message.md)
- [text-messages.md](text-messages.md)
