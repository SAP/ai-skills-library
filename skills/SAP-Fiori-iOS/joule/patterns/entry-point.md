# Entry Point — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns

## What is it?

The Joule entry point is the Joule icon button in the navigation bar. Tapping it opens the Joule panel.

---

## Rules

**Do:**
- Always expose the Joule icon in the nav bar on the home screen
- Keep entry point position consistent across devices
- Show Joule icon as the **first item** in nav bar or overflow menu
- Provide entry point on every screen where users might need help

**Don't:**
- Use the Joule icon as a toggle (it doesn't indicate active/inactive state)
- Use other buttons (FAB, etc.) as entry point
- Show multiple entry points on one screen

---

## Placement Options

### Nav Bar (default — preferred)
Joule icon as the first action button in the navigation bar.

```swift
.toolbar {
    ToolbarItem(placement: .primaryAction) {
        FioriButton { _ in
            Image("joule-icon")  // Joule star icon
                .accessibilityLabel("Open Joule")
        }
        .fioriButtonStyle(FioriTertiaryButtonStyle())
        .onTapGesture {
            if joulePanelSize == .minimized {
                joulePanelSize = .large  // restore from minimized
            } else {
                showJoule = true
                joulePanelSize = .large
            }
        }
    }
}
```

### Overflow Menu (when nav bar space is unavailable)
First item in the overflow menu.

```swift
Menu {
    Button {
        showJoule = true
        joulePanelSize = .large
    } label: {
        Label("Joule", image: "joule-icon")  // first in menu
    }
    // other menu items
} label: {
    Image(systemName: "ellipsis.circle")
}
```

---

## Behavior When Joule Is Already Active

| Panel state | Tap entry point |
|-------------|----------------|
| Minimized | Returns panel to large (default) size |
| Medium | Returns panel to large (default) size |
| Closed | Opens panel in large size |

---

## Related

- [../components/joule-panel.md](../components/joule-panel.md)
- [welcome-screen.md](welcome-screen.md)
