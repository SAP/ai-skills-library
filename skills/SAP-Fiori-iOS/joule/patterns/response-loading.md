# Response Loading — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns

## What is it?

Loading indicators shown while Joule processes responses. Two modes: standard (< 10 seconds) and long-running (> 10 seconds with status messages).

---

## Rules

**Do:** Use for Joule processing responses only.
**Don't:** Use for user responses.

**Long-running tips:**
- Use if operation > 10 seconds
- If > 10 seconds with no status update → show default message "Working on your request"
- Format: [action/verb] + [noun] (e.g. "Analyzing invoice data")
- Max **55 characters** per status message
- Max status update duration: **60 seconds**; show max 1–2 seconds per update before next

---

## Anatomy

**A. Loading chat bubble** — animated dots indicating Joule is responding
**B. Status message** — long-running: what Joule is processing
**C. Clock icon** — replaces "Send" button during loading

---

## States

| State | Behavior |
|-------|---------|
| Loading | Input blocked; clock icon shown |
| Tap clock | Toast: "Joule is still processing" |
| Success | Response displayed immediately |
| Error (>60s) | Error message shown |

---

## Variations

### Standard Loading (< 10s)
Loading chat bubbles only — no status message.

### Long-Running Loading (> 10s)
Loading bubbles + concise status updates.

### Streaming (loading complete, content rendering)
- **Text streaming** — response text appears progressively with animation (can disable in device settings)
- **Skeleton loading** — shown for non-text rich content (images, videos, cards) before ready
- **"Scroll for More" button** — appears when response extends beyond screen; re-appears on scroll up/down

---

## SwiftUI Code Example

```swift
// Loading chat bubble
HStack(alignment: .bottom, spacing: 4) {
    ForEach(0..<3) { i in
        Circle()
            .fill(Color.preferredColor(.secondaryLabel))
            .frame(width: 6, height: 6)
            .opacity(animationPhase == i ? 1.0 : 0.3)
    }
}

// Clock icon replacing Send during loading
if isLoading {
    Image(systemName: "clock")
        .foregroundStyle(Color.preferredColor(.tertiaryLabel))
        .onTapGesture {
            showToast = true  // "Joule is still processing"
        }
}

// Status message (long-running)
if let status = currentStatus, elapsedTime > 10 {
    Text(status)  // max 55 chars, format: verb + noun
        .font(.fiori(forTextStyle: .footnote))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
}
```

---

## Related

- [../components/joule-panel.md](../components/joule-panel.md)
- [../components/input-field.md](../components/input-field.md)
