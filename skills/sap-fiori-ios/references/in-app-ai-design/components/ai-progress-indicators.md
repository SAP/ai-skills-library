# AI Progress Indicators — In-App AI Design

> SAP Fiori for iOS | In-App AI Design / Components
> Extends: [../components/activity-indicator.md](../components/activity-indicator.md), [../components/linear-progress-indicator.md](../components/linear-progress-indicator.md)

## What is it?

AI progress indicators communicate the status of a user's AI request while content is being generated. They keep users informed, manage expectations, and show the system is actively working.

**Only use for AI operations.** Do not use for non-AI scenarios or operations < 1 second.

---

## Types

### Linear Progress Indicator
- **A. Indicator** — animated bar showing active processing
- **B. Track** — static bar showing overall range
- **C. AI Icon** — looping sparkle animation
- **D. Label** — text confirming AI is running (no "AI" if icon is present)

Variants: determinate (known progress) and indeterminate (unknown duration).

### Activity Indicator
- **A. AI Icon** — looping sparkle animation
- **B. Label** (optional) — confirms AI is active

Layouts: horizontal (icon + label side by side) or vertical (icon above label).

### Checkout Indicator
- **A. AI Icon** — looping sparkle animation
- **B. Label** (optional)

Used for processing states with success/error outcomes.

### Button Loading State
- **A. AI Icon** — looping sparkle animation replaces button icon
- **B. Label** (optional) — "Generating…" or similar

Colors and sizes follow the in-place loading state spec for regular buttons.

---

## Timing Rules

- **Show indicator** 1 second after generation is triggered
- **Minimum display** 1000ms — prevents flickering
- **Pulses between animation loops**
- **Animation:** iOS native breathe animation, looped continuously

---

## Placement

| Context | Indicator type | Use when |
|---------|---------------|---------|
| Full screen | Checkout indicator | Action is the only/primary action; no other actions allowed |
| Partial screen | Activity indicator | Loading applies to part of screen; other actions still allowed |
| In-place | Button loading state | Applies only to a button or small component; other actions allowed |

---

## Text Rules (follows AI UI Text guidelines)

- Include label only when it adds clarity
- Never include "AI" in the label when the AI icon is already shown
- Keep labels short: "Generating results…" not "AI is analyzing your request…"

---

## Stop Generation

Always provide a way for users to stop the generation process.

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

// Activity indicator with AI icon (partial screen)
VStack(spacing: 8) {
    Image(systemName: "sparkles")
        .symbolEffect(.breathe)
        .font(.system(size: 32))
        .foregroundStyle(Color.preferredColor(.tintColor))
    Text("Generating results…")
        .font(.fiori(forTextStyle: .footnote))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
}
.padding(24)

// Linear progress indicator with AI icon
VStack(alignment: .leading, spacing: 8) {
    LinearProgressIndicator(
        indicatorColor: Color.preferredColor(.tintColor),
        progress: generationProgress  // nil for indeterminate
    )
    HStack(spacing: 6) {
        Image(systemName: "sparkles")
            .symbolEffect(.breathe)
            .foregroundStyle(Color.preferredColor(.tintColor))
            .font(.fiori(forTextStyle: .footnote))
        Text("Creating summary…")  // no "AI" — icon is present
            .font(.fiori(forTextStyle: .footnote))
            .foregroundStyle(Color.preferredColor(.secondaryLabel))
    }
}

// Button in loading state (in-place)
FioriButton { _ in
    HStack(spacing: 6) {
        Image(systemName: "sparkles")
            .symbolEffect(.breathe, isActive: isGenerating)
        Text(isGenerating ? "Generating…" : "Generate")
    }
}
.fioriButtonStyle(FioriSecondaryButtonStyle())
.disabled(isGenerating)

// Stop generation button
if isGenerating {
    FioriButton { _ in Text("Stop Generating") }
        .fioriButtonStyle(FioriSecondaryButtonStyle())
        .onTapGesture { stopGeneration() }
}

// Show indicator 1 second after trigger, minimum 1000ms
.task {
    try? await Task.sleep(for: .seconds(1))  // 1s delay before showing
    showIndicator = true
    await generateContent()
    try? await Task.sleep(for: .milliseconds(200))  // ensure min 1000ms total
    showIndicator = false
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Show indicator 1 second after generation starts
- Keep indicator visible for at least 1000ms
- Provide a way to stop generation
- Use breathe animation for the AI icon
- Omit "AI" from labels when the AI icon is shown

**Don't:**
- Use for non-AI loading states
- Show for operations < 1 second
- Use AI progress indicators in non-AI scenarios

---

## Related

- [ai-buttons.md](ai-buttons.md)
- [ai-ui-text.md](ai-ui-text.md)
- [../components/linear-progress-indicator.md](../components/linear-progress-indicator.md)
- [../components/activity-indicator.md](../components/activity-indicator.md)
