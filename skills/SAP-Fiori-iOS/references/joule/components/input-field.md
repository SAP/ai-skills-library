# Input Field — Joule Component

> SAP Fiori for iOS | Joule / Components

## What is it?

The input field is where users type to communicate with Joule. It supports text input (up to 2000 characters / 6 lines), attachments, dictation, voice, and agent mentions.

---

## Rules

**Do:**
- Allow up to **2000 characters** across up to **6 lines**
- Auto-save text if user taps outside without sending
- Show character count helper text when input reaches **1800 characters**
- Stop accepting input at **2000 characters**

**Don't:**
- Send an empty message
- Allow typing past the character limit

---

## Anatomy

| Element | Description |
|---------|-------------|
| **A. Text input box** | Container for typed text |
| **B. Attachments & Modes button** (+) | Upload attachments |
| **C. Placeholder text** | "Message Joule" (default) |
| **D. Dictation button** | Activates voice dictation |
| **E. Voice button** | Activates voice mode; becomes active Send button when text is present |
| **F. User input** | Live text display |
| **G. Mention button** | Tag an agent for specific replies; disabled when attachment uploaded; hidden once agent selected |
| **H. Character limit** | Shows at 1800 chars — "1800/2000" format |
| **I. Send button** | Sends message to Joule |
| **J. Expand/Collapse button** | Appears after 5 lines; toggles expanded view |

---

## States

| State | Description |
|-------|-------------|
| Initial loading | Field loading — not ready for input |
| Enabled (default) | Ready for user input |
| Active | Tapped — keyboard up, no text yet |
| Typing | User is entering text |
| Max height | 5+ lines — field becomes scrollable |
| Expanded | User tapped Expand — more visible area |
| Dictation mode | Waveform shown; tap stop to end dictation |

---

## Behavior

- Tap outside while typing → keyboard dismisses, text preserved in field
- Input > 5 lines → Expand button appears
- Input > 1800 chars → character counter appears
- Input = 2000 chars → further typing blocked
- After dictation → transcribed text appears in field for review before sending
- Width = panel width

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

@State private var messageText = ""
@State private var isExpanded = false
@State private var isDictating = false

let maxChars = 2000
let warnChars = 1800

VStack(spacing: 0) {
    // H. Character counter (only at 1800+)
    if messageText.count >= warnChars {
        HStack {
            Spacer()
            Text("\(messageText.count)/\(maxChars)")
                .font(.fiori(forTextStyle: .caption2))
                .foregroundStyle(messageText.count >= maxChars
                    ? Color.preferredColor(.negativeLabel)
                    : Color.preferredColor(.secondaryLabel))
                .padding(.horizontal, 16)
        }
    }

    HStack(alignment: .bottom, spacing: 8) {
        // B. Attachments button
        FioriButton { _ in Image(systemName: "plus") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())

        // A. Text input
        TextEditor(text: Binding(
            get: { messageText },
            set: { if $0.count <= maxChars { messageText = $0 } }
        ))
        .frame(minHeight: 36, maxHeight: isExpanded ? .infinity : 120)
        .overlay(alignment: .topLeading) {
            if messageText.isEmpty {
                Text("Message Joule")  // C. Placeholder
                    .foregroundStyle(Color.preferredColor(.tertiaryLabel))
                    .padding(.top, 8).padding(.leading, 4)
                    .allowsHitTesting(false)
            }
        }

        // D/E/I. Action buttons
        if isDictating {
            FioriButton { _ in Image(systemName: "stop.circle.fill") }
                .fioriButtonStyle(FioriTertiaryButtonStyle())
                .onTapGesture { stopDictation() }
        } else if messageText.isEmpty {
            FioriButton { _ in Image(systemName: "mic") }  // D. Dictation
                .fioriButtonStyle(FioriTertiaryButtonStyle())
                .onTapGesture { startDictation() }
        } else {
            FioriButton { _ in Image(systemName: "arrow.up.circle.fill") }  // I. Send
                .fioriButtonStyle(FioriPrimaryButtonStyle())
                .onTapGesture { sendMessage() }
        }
    }
    .padding(12)
}
```

---

## Related

- [joule-panel.md](joule-panel.md)
- [../patterns/persistent-attachment.md](../patterns/persistent-attachment.md)
