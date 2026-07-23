# Joule Panel — Joule Component

> SAP Fiori for iOS | Joule / Components

## What is it?

The Joule panel is the container and foundation for all Joule interactive components. It holds the conversation, input field, and header controls. Three size variants: large, medium, and minimized.

---

## Rules

**Do:**
- Use panel to create a seamless conversational experience
- Use the resizable panel to give users flexibility

**Don't:**
- Use full-screen panel if the user needs to multitask
- Put conversational elements outside the panel

---

## Anatomy

### Large / Medium View
**A. Header** — grabber (resize handle), close button (✕), overflow button (•••)
**B. Content area** — all conversation components and interactions
**C. Input field** — always at the base of the panel

### Minimized View
**A. Container** — close button (✕) + tap to reopen default panel

---

## Three Size Variants

| Variant | Description | Navigation |
|---------|-------------|-----------|
| **Large** (default) | Full panel height — opens when Joule is triggered | Default on entry |
| **Medium** | Partial — parent view visible behind panel; can allow or block background interaction | Drag down from large |
| **Minimized** | Sits on top of (or replaces) tab bar; minimal space; follows user across app | Drag down from medium |

---

## Behavior

### Opening
Tap Joule entry point → large view panel opens.

### Closing
Tap ✕ in header or ✕ in minimized view.

### Resizing
Drag up/down on the grabber → seamlessly switches between large, medium, minimized.
Tap minimized container → returns to default (large) panel.

### Minimized view
- Only variant that follows the user as they navigate the app
- Indicates Joule is still open with an ongoing conversation
- Sits above tab bar or replaces it if no tab bar present

### Medium view with background interaction
- **With overlay** — blocks background interaction (modal behavior)
- **Without overlay** — allows background interaction (non-modal behavior)

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

enum PanelSize { case large, medium, minimized }
@State private var panelSize: PanelSize = .large
@State private var showJoule = false

// Joule entry point
FioriButton { _ in
    Image(systemName: "sparkles")
        .accessibilityLabel("Open Joule")
}
.fioriButtonStyle(FioriTertiaryButtonStyle())
.onTapGesture { showJoule = true; panelSize = .large }

// Panel
.sheet(isPresented: $showJoule) {
    NavigationStack {
        VStack(spacing: 0) {
            // B. Content area
            JouleConversationView()

            // C. Input field — always at base
            JouleInputField(onSend: sendMessage)
        }
        .navigationBarTitleDisplayMode(.inline)
        .toolbar {
            ToolbarItem(placement: .principal) {
                Text("Joule")
                    .font(.fiori(forTextStyle: .headline, weight: .bold))
                    .foregroundStyle(Color.preferredColor(.persistentLabel))
            }
            ToolbarItem(placement: .primaryAction) {
                Menu {
                    Button("AI Notice") { showAINotice = true }
                    Button("Conversations") { showConversations = true }
                } label: {
                    Image(systemName: "ellipsis.circle")
                }
            }
            ToolbarItem(placement: .cancellationAction) {
                Button { showJoule = false } label: {
                    Image(systemName: "xmark")
                }
            }
        }
    }
    .presentationDetents([.large, .medium, .fraction(0.1)])
    .presentationDragIndicator(.visible)
    .interactiveDismissDisabled(false)
}
```

---

## Related

- [input-field.md](input-field.md)
- [../foundations/layout.md](../foundations/layout.md)
- [../patterns/ai-notice.md](../patterns/ai-notice.md)
