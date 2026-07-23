# AI Buttons — In-App AI Design

> SAP Fiori for iOS | In-App AI Design / Components
> Extends: [../components/buttons.md](../components/buttons.md)

## What is it?

AI buttons trigger AI-powered features within the user flow. The sparkle star icon (✦) signals that the action is AI-powered.

---

## Rules

**Do:**
- Follow all SAP Fiori Button rules
- Use **secondary buttons** by default
- Use **leading icons only** (star icon before label)
- Use only the **star/sparkle icon** (✦)
- Use primary buttons only when it's the primary action on the page/panel
- Keep labels concise and descriptive of the action

**Don't:**
- Include "AI" in the button label: not "Create with AI", "Enhance with AI", "Generate with AI" — just "Create", "Enhance", "Generate"
- Add trailing icons
- Use vague labels
- Use two primary buttons in a button group

---

## Anatomy

**A. Container** — follows FioriButton background colors and states
**B. Icon** — sparkle/star icon (leading) indicating AI-powered action
**C. Text** — concise action description (no "AI" in the text)

---

## Content Generation States

| State | Button appearance |
|-------|------------------|
| Default | "Generate" (star icon + label) |
| Generating | "Stop Generating" (allows user to cancel) |
| Complete / Stopped | "Revise" (allows re-generation) |

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

// Standard AI secondary button
FioriButton { _ in
    HStack(spacing: 6) {
        Image(systemName: "sparkles")  // B. Star icon — leading only
        Text("Summarize")              // C. No "AI" in label
    }
}
.fioriButtonStyle(FioriSecondaryButtonStyle())

// Primary AI button (only when it's THE primary action)
FioriButton { _ in
    HStack(spacing: 6) {
        Image(systemName: "sparkles")
        Text("Generate")
    }
}
.fioriButtonStyle(FioriPrimaryButtonStyle())

// Generation state machine
enum GenerationState { case idle, generating, complete }
@State private var generationState: GenerationState = .idle

FioriButton { _ in
    HStack(spacing: 6) {
        Image(systemName: "sparkles")
        switch generationState {
        case .idle:       Text("Generate")
        case .generating: Text("Stop Generating")
        case .complete:   Text("Revise")
        }
    }
}
.fioriButtonStyle(FioriSecondaryButtonStyle())
.onTapGesture {
    switch generationState {
    case .idle:
        generationState = .generating
        startGeneration()
    case .generating:
        generationState = .complete
        stopGeneration()
    case .complete:
        generationState = .generating
        startGeneration()
    }
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Secondary style by default; primary only for the main action
- Always use leading star icon
- Label describes the action: "Summarize", "Draft", "Translate", "Fix"

**Don't:**
- Add "AI" to labels: not "Summarize with AI"
- Use trailing icons
- Use icon-only AI buttons without a label (unless in a toolbar with space constraints)

---

## Related

- [../components/buttons.md](../components/buttons.md)
- [ai-progress-indicators.md](ai-progress-indicators.md)
- [ai-ui-text.md](ai-ui-text.md)
