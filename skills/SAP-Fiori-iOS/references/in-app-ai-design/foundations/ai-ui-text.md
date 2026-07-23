# AI UI Text — In-App AI Design

> SAP Fiori for iOS | In-App AI Design / Foundation

## What is it?

AI UI text is the primary communication between users and AI systems — conveying information, instructions, errors, and feedback. Effective AI UI text bridges complex AI operations with a user-friendly experience.

**Based on US English.** Adhere to default examples below; only deviate when absolutely necessary for a specific use case.

---

## Four Text Categories

### 1. Explanations
Make AI actions and decisions transparent. Use simple, concise language.

| ✅ Do | ❌ Don't |
|-------|---------|
| "Created with AI. Verify results before use." | "Generated utilizing advanced artificial intelligence algorithms. Validate output integrity prior to deployment." |
| "AI-generated content. Review before sharing." | "This content was produced by our machine learning system and may require validation." |

### 2. Instructions
Guide users through AI tasks. Short, action-oriented.

| ✅ Do | ❌ Don't |
|-------|---------|
| "Fix spelling and grammar." | "Make corrections." |
| "Tell AI what to do." | "Ask artificial intelligence to create content." |
| "Summarize" | "Use AI to generate a summary of this content" |

### 3. Descriptions
Explain what the AI is doing. Set expectations concisely.

| ✅ Do | ❌ Don't |
|-------|---------|
| "Output may contain errors." | "Consider verifying AI output errors." |
| "Generating results…" | "Artificial Intelligence is analyzing the current request…" |
| "Creating summary…" | "Our AI is currently processing your data to produce a summary." |

### 4. Error Messages
Clear, specific, actionable. Tell users what went wrong and how to fix it.

| ✅ Do | ❌ Don't |
|-------|---------|
| "An error occurred. Please try again." | "System error. Contact administrator." |
| "Request failed. Refine your request and try again." | "Artificial Intelligence is having trouble understanding you." |
| "Generation stopped. Try a shorter prompt." | "Error 500: AI processing failed." |

---

## Key Rules

- **Never include "AI" in button text:** Not "Create with AI", "Enhance with AI", "Generate with AI" — just "Create", "Enhance", "Generate"
- **Never spell out "Artificial Intelligence"** in UI text — use "AI" if needed, or omit entirely
- **Keep it short** — one sentence maximum for most UI text
- **Be actionable** — error messages must tell the user what to do next
- **Maintain consistency** — use the same phrasing across platforms

---

## SwiftUI Examples

```swift
// Explanation label on AI-generated content
HStack(spacing: 4) {
    Image(systemName: "sparkles")
        .foregroundStyle(Color.preferredColor(.tintColor))
        .font(.fiori(forTextStyle: .caption1))
    Text("Created with AI. Verify results before use.")
        .font(.fiori(forTextStyle: .caption1))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
}

// AI button label — action verb only, no "AI"
FioriButton { _ in
    HStack {
        Image(systemName: "sparkles")
        Text("Summarize")  // ✅ not "Summarize with AI"
    }
}

// AI generating description
Text("Generating results…")  // ✅
// not "Artificial Intelligence is analyzing your request…"

// AI error message
Text("Request failed. Refine your request and try again.")  // ✅
// not "AI is having trouble understanding you."
```

---

## Related

- [ai-buttons.md](ai-buttons.md) — button labels follow these rules
- [ai-progress-indicators.md](ai-progress-indicators.md) — indicator labels follow these rules
- [get-started.md](get-started.md)
