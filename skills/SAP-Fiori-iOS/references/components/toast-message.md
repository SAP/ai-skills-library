# Toast Message — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Feedback
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit` (Notifications page)
> Development reference: UIKit `FUIToastMessage`, SwiftUI `ToastMessage`

## What is it?

A toast message is a brief, non-intrusive indicator that appears in response to a user action. It confirms that the action has been processed and completed. It appears at the center of the screen and auto-dismisses after 2–5 seconds.

---

## When to Use

**Do:**
- Use when a user action needs brief, non-intrusive confirmation (saved, deleted, sent, copied)

**Don't:**
- Use to convey important information — use a `BannerMessage` for persistent system-level messages

**Top tips:**
- Keep text short, concise, and under **three lines**
- Do not include links or buttons — toast messages dismiss automatically and the user can't reliably interact with them

---

## Anatomy

```
      ┌──────────────────────────────┐
      │  [B. Icon]  A. Label text    │
      └──────────────────────────────┘
```

**A. Label** — required. Clearly confirms the user action or provides brief system feedback.

**B. Icon** (optional) — enhances message clarity.

---

## Placement

### Absolute Position (default)
Toast appears at the **center of the screen** horizontally and vertically.

### Relative Position
Vertical position is customizable — can be set relative to other components. Horizontal position is always centered.

---

## Variations

| Variation | Use |
|-----------|-----|
| Single-line *(default)* | Recommended for all standard confirmations |
| Multi-line | When text exceeds one line; max **three lines** |

---

## Behavior

- Triggered by user actions
- **Auto-dismisses after 2–5 seconds**
- No user interaction required or expected (no links, no buttons)

---

## SwiftUI Code Examples

### Basic toast (single-line)
```swift
import FioriSwiftUICore

@State private var showToast = false

Button("Save") {
    save()
    showToast = true
}

// Overlay at root level
.overlay(alignment: .center) {
    if showToast {
        ToastMessage {
            Text("Changes saved")
        }
        .transition(.opacity.combined(with: .scale(scale: 0.9)))
        .animation(.easeInOut(duration: 0.2), value: showToast)
        .onAppear {
            DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
                withAnimation { showToast = false }
            }
        }
    }
}
```

### With optional icon
```swift
ToastMessage {
    Text("Invoice submitted")
} icon: {
    Image(systemName: "checkmark.circle.fill")
        .foregroundStyle(Color.preferredColor(.positiveLabel))
}
```

### Common trigger patterns
```swift
// After delete
func deleteItem(_ item: Item) {
    items.removeAll { $0.id == item.id }
    showToastMessage = "Item deleted"
    showToast = true
    autoDismiss()
}

// After copy to clipboard
func copyToClipboard(_ text: String) {
    UIPasteboard.general.string = text
    showToastMessage = "Copied to clipboard"
    showToast = true
    autoDismiss()
}

// After send
func sendMessage() async {
    try await send()
    showToastMessage = "Message sent"
    showToast = true
    autoDismiss()
}

func autoDismiss(after seconds: Double = 2) {
    DispatchQueue.main.asyncAfter(deadline: .now() + seconds) {
        withAnimation { showToast = false }
    }
}
```

### Relative position (above tab bar)
```swift
ZStack(alignment: .bottom) {
    ContentView()

    if showToast {
        ToastMessage {
            Text("Draft saved")
        }
        .padding(.bottom, 80)  // above tab bar height
        .transition(.move(edge: .bottom).combined(with: .opacity))
        .animation(.easeInOut(duration: 0.25), value: showToast)
        .onAppear { autoDismiss() }
    }
}
```

### Multi-line (max 3 lines)
```swift
ToastMessage {
    Text("Your purchase order has been submitted for approval.")
        .multilineTextAlignment(.center)
        .lineLimit(3)
}
```

### Reusable toast modifier
```swift
struct ToastModifier: ViewModifier {
    @Binding var isPresented: Bool
    let message: String
    let icon: String?
    let duration: Double

    func body(content: Content) -> some View {
        ZStack {
            content
            if isPresented {
                VStack {
                    Spacer()
                    ToastMessage {
                        Text(message)
                    } icon: {
                        if let icon {
                            Image(systemName: icon)
                                .foregroundStyle(Color.preferredColor(.positiveLabel))
                        }
                    }
                    .padding(.bottom, 32)
                }
                .transition(.opacity)
                .animation(.easeInOut(duration: 0.2), value: isPresented)
                .onAppear {
                    DispatchQueue.main.asyncAfter(deadline: .now() + duration) {
                        withAnimation { isPresented = false }
                    }
                }
            }
        }
    }
}

extension View {
    func toast(isPresented: Binding<Bool>,
               message: String,
               icon: String? = nil,
               duration: Double = 2) -> some View {
        modifier(ToastModifier(isPresented: isPresented,
                               message: message,
                               icon: icon,
                               duration: duration))
    }
}

// Usage
ContentView()
    .toast(isPresented: $showToast, message: "Saved", icon: "checkmark.circle.fill")
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Lines | Single | Default `ToastMessage` |
| Lines | Multi (2–3) | `.lineLimit(3)` + `.multilineTextAlignment(.center)` |
| Icon | Yes | `icon: { Image(systemName:) }` |
| Icon | No | Omit `icon` parameter |
| Position | Center (default) | `.overlay(alignment: .center)` |
| Position | Relative | `.overlay(alignment: .bottom)` + `.padding(.bottom, offset)` |
| Duration | 2s | `asyncAfter(deadline: .now() + 2)` |
| Duration | 5s | `asyncAfter(deadline: .now() + 5)` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Limit text to **3 lines maximum** — single line is preferred
- Auto-dismiss after **2–5 seconds**
- Trigger only in response to a user action — not spontaneously
- Use a success icon (`.positiveLabel`) for completed actions
- Position relative to the screen when the default center position would overlap important content

**Don't:**
- Use for important information that requires the user's attention — use `BannerMessage` instead
- Include links or buttons — the user can't reliably interact before auto-dismiss
- Show multiple toasts simultaneously — queue them or show only the most recent

---

## Related Components

- [banner.md](banner.md) — persistent system-level notifications
- [illustrated-message.md](illustrated-message.md) — full empty/error/success states
