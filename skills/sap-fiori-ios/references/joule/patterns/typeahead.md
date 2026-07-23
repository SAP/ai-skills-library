# Typeahead — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns

## What is it?

Real-time query suggestions shown above the input field as users type on the welcome screen. Helps complete prompts faster.

---

## Rules

**Do:**
- Only on **welcome screen**, first prompt of each new conversation
- Show suggestions above input field (not obstructing it)
- Apply blurred background with slight opacity behind suggestions
- Highlight the suggested part
- Max **3 suggestions** at a time
- Prefix with ellipsis (…) when suggestion exceeds one line

**Don't:**
- Show when input field is empty
- Auto-insert without explicit user tap
- Show more than 3 suggestions
- Show outside welcome screen

If no suggestions can be generated → collapse entirely (no empty rows)

---

## Anatomy

**A. Typeahead container** — list of up to 3 suggestions
**B. User prompt** — what the user has typed (or "…" if suggestions overflow one line)
**C. Suggestion** — Joule's completion
**D. Insert icon** — populates suggestion into input field for editing

---

## Behavior

- **Tap suggestion text** → sends directly; new conversation starts
- **Tap insert icon (→)** → populates input field; user can edit before sending
- All 3 suggestions show user prompt + suggestion when they fit one line
- If any suggestion exceeds one line → user prompt replaced with "…" across all 3 suggestions

---

## SwiftUI Code Example

```swift
struct TypeaheadView: View {
    let userInput: String
    let suggestions: [String]  // max 3
    let onSend: (String) -> Void
    let onInsert: (String) -> Void

    var body: some View {
        if !userInput.isEmpty && !suggestions.isEmpty {
            VStack(spacing: 0) {
                ForEach(suggestions.prefix(3), id: \.self) { suggestion in
                    HStack {
                        // B + C: user prompt + suggestion (or … + suggestion)
                        Text(suggestionText(for: suggestion))
                            .font(.fiori(forTextStyle: .body))
                            .lineLimit(1)
                        Spacer()
                        // D: Insert icon
                        FioriButton { _ in
                            Image(systemName: "arrow.up.left")
                                .accessibilityLabel("Insert suggestion")
                        }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { onInsert(suggestion) }
                    }
                    .padding(12)
                    .contentShape(Rectangle())
                    .onTapGesture { onSend(suggestion) }  // tap text = send directly
                    Divider()
                }
            }
            .background(.ultraThinMaterial)  // blurred background
        }
    }

    func suggestionText(for suggestion: String) -> AttributedString {
        // Highlight suggestion part in different style from user prompt
        var attributed = AttributedString(userInput)
        attributed.foregroundColor = .init(Color.preferredColor(.primaryLabel))
        var suggestionPart = AttributedString(suggestion)
        suggestionPart.foregroundColor = .init(Color.preferredColor(.tintColor))
        return attributed + suggestionPart
    }
}
```

---

## Related

- [welcome-screen.md](welcome-screen.md)
- [../components/input-field.md](../components/input-field.md)
