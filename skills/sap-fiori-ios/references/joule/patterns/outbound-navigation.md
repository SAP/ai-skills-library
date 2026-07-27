# Outbound Navigation — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns
> Note: Design best practice — not part of Joule mobile client SDK.

## What is it?

Outbound navigation transitions users from Joule to other parts of the app or external content. Always user-initiated with clear messaging about where the navigation leads.

---

## Rules

**Do:** Inform user clearly before navigating. Maintain context before/after navigation.
**Don't:** Enable without user initiation. Overuse — it can make Joule seem inefficient.

---

## Destination Types

### In-App Destination
- Joule informs user it will navigate to a specific app section
- Smooth transition animation
- **Minimized Joule panel** maintains context and allows easy return

### External App Destination
- Joule informs user it will open another app
- Joule panel not shown in external app (can't maintain conversation context)
- If required app not installed → Joule directs to App Store

### Non-Mobile Native Web Destination
- Joule opens web content via app's default mechanism
- Behavior depends on app setup (e.g., hybrid viewer, SFSafariViewController)

---

## SwiftUI Code Example

```swift
// In-app navigation with minimized Joule
FioriButton { _ in
    HStack {
        Image(systemName: "arrow.right.circle")
        Text("View Invoice List")
    }
}
.fioriButtonStyle(FioriSecondaryButtonStyle())
.onTapGesture {
    joulePanelSize = .minimized  // minimize to keep context
    navigateToInvoiceList()
}

// External app link
Link(destination: URL(string: "someapp://action")!) {
    Text("Open in External App")
}

// Web content
Link(destination: URL(string: "https://help.sap.com/...")!) {
    Text("Learn More ›")
        .foregroundStyle(Color.preferredColor(.tintColor))
}
```

---

## Related

- [../components/joule-panel.md](../components/joule-panel.md)
- [../components/list-card.md](../components/list-card.md)
