# AI Notice — In-App AI Design

> SAP Fiori for iOS | In-App AI Design / Patterns

## What is it?

An AI notice informs users when content is AI-generated, reminding them to verify accuracy. Shown beneath form cells that contain AI-generated or AI-suggested content.

---

## When to Use

**Do:**
- Show where content is AI-generated on a page
- Use for components or pages containing AI-generated content

**Don't:**
- Use when text is created without AI
- Use for authenticated user input, legally binding actions, or attachment handling

---

## Text Variants

| Content type | Text | When |
|-------------|------|------|
| Hosted SAP AI — AI created it | "Created with AI" | AI generated the entire/partial content |
| Hosted SAP AI — AI suggested it | "Suggested by AI" | AI recommended content from another data source |
| Third-party AI — created | "Created with \<Name\> AI" | Third-party AI generated the content |
| Third-party AI — suggested | "Suggested by \<Name\> AI" | Third-party AI recommended the content |

**Rule:** Use "Created with AI" for text inputs. Use "Suggested by AI" for list pickers, switches, and picker form cells.

**Optional add-on for high-risk use cases:** "Verify before use."

---

## Anatomy

**A. AI Notice** — shows below helper text; if no helper text exists, occupies the helper text area
**B. Verification text** (optional) — "Verify before use." for high-risk scenarios
**C. Additional disclosure** (optional) — hyperlink to bottom sheet or browser with more AI info

---

## Interactive vs. Non-Interactive

| Scenario | AI notice type | Banner |
|----------|---------------|--------|
| ≤3 AI-generated fields | **Interactive** (tap hyperlink for details) | No banner |
| >3 AI-generated fields | **Non-interactive** (text only) | Yes — "Learn more" opens bottom sheet |

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

// AI notice below a text field (interactive, ≤3 fields)
VStack(alignment: .leading, spacing: 4) {
    TextFieldFormView(
        title: { Text("Summary") },
        text: $summary
    )

    // A. AI notice in helper text area
    HStack(spacing: 4) {
        Image(systemName: "sparkles")
            .font(.fiori(forTextStyle: .caption1))
            .foregroundStyle(Color.preferredColor(.tintColor))
        // C. Interactive disclosure link
        Button("Created with AI") {
            showAIDetails = true
        }
        .font(.fiori(forTextStyle: .caption1))
        .foregroundStyle(Color.preferredColor(.tintColor))

        // B. Optional verification text (high-risk)
        Text("Verify before use.")
            .font(.fiori(forTextStyle: .caption1))
            .foregroundStyle(Color.preferredColor(.secondaryLabel))
    }
}
.sheet(isPresented: $showAIDetails) {
    AIDisclosureSheet()
        .presentationDetents([.medium, .large])
        .presentationDragIndicator(.visible)
}

// Page-level banner (>3 AI fields — non-interactive notices)
if aiFieldCount > 3 {
    BannerMessage {
        HStack {
            Image(systemName: "sparkles")
                .foregroundStyle(Color.preferredColor(.tintColor))
            Text("Some fields were created with AI.")
        }
    } action: {
        FioriButton { _ in Text("Learn More") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .onTapGesture { showAIDetails = true }
    }
}

// Non-interactive AI notice (used with banner)
HStack(spacing: 4) {
    Image(systemName: "sparkles")
        .font(.fiori(forTextStyle: .caption1))
        .foregroundStyle(Color.preferredColor(.tintColor))
    Text("Created with AI")
        .font(.fiori(forTextStyle: .caption1))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
    // No button/link — banner handles the disclosure
}

// "Suggested by AI" for list picker / switch / picker
HStack(spacing: 4) {
    Image(systemName: "sparkles")
        .font(.fiori(forTextStyle: .caption1))
        .foregroundStyle(Color.preferredColor(.tintColor))
    Text("Suggested by AI")
        .font(.fiori(forTextStyle: .caption1))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
}
```

---

## Risk Assessment

| Risk level | AI notice | Verification text |
|-----------|-----------|------------------|
| **High** (affects others, irreversible, critical/destructive) | Required | Recommended: "Verify before use." |
| **Low** (affects only current user, easily correctable) | Use for transparency | Optional |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use "Created with AI" for text inputs; "Suggested by AI" for pickers/switches
- Add "Verify before use." for high-risk use cases
- Switch to banner + non-interactive notices when >3 fields are AI-generated
- Be consistent with AI service names across the app

**Don't:**
- Show AI notice on non-AI content
- Overwhelm users — balance transparency with UX
- Use the same notice style inconsistently across similar form cells

---

## Related

- [ai-acknowledgement.md](ai-acknowledgement.md)
- [ai-ui-text.md](ai-ui-text.md)
- [../components/banner.md](../components/banner.md)
