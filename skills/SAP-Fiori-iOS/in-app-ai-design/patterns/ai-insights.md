# AI Insights — In-App AI Design

> SAP Fiori for iOS | In-App AI Design / Patterns
> Note: Guidance only — not part of the SDK.

## What is it?

AI Insights display a standardized summary, analysis, or suggestion generated with AI. Two variants: full-screen (all content is AI-generated) and card (part of screen is AI-generated).

---

## When to Use

**Do:**
- Full-screen: only when **all** content on the screen is AI-generated
- Card: when part of a screen shows AI insights; use multiple cards for multiple insight categories

**Don't:**
- Show user-generated content in the full-screen variant
- Display multiple AI user feedback patterns on the same screen

---

## Anatomy

### Full-Screen AI Insights
```
A. Header (AI insights overview)
B. AI Notice (optional, highly recommended)
C. AI Insights Content (sections with swappable component slots)
D. AI User Feedback (optional inline thumbs up/down)
E. Footer (optional — AI button to regenerate or perform actions)
```

### Card AI Insights
```
A. Card container
B. AI Tag (optional, highly recommended)
C. AI Insights Content (sections with swappable slots)
D. AI User Feedback (optional)
E. Footer (optional)
```

---

## States

| State | Behavior |
|-------|---------|
| **Generated** | Shows AI content in recommended layouts |
| **Loading** | Skeleton loading placeholders + loading state buttons |
| **Error** | `IllustratedMessage` with retry/exit option |

---

## SwiftUI Code Example

### Card AI Insights
```swift
import FioriSwiftUICore

struct AIInsightsCard: View {
    let insights: AIInsightsData
    @State private var isLoading = true
    @State private var loadError = false

    var body: some View {
        Card {
            // B. AI Tag in header
            HStack {
                Text("Account Synopsis")
                    .font(.fiori(forTextStyle: .headline))
                Spacer()
                HStack(spacing: 4) {
                    Image(systemName: "sparkles")
                        .foregroundStyle(Color.preferredColor(.tintColor))
                    Text("AI")
                        .font(.fiori(forTextStyle: .caption1))
                        .foregroundStyle(Color.preferredColor(.tintColor))
                }
            }
        } body: {
            if isLoading {
                // Loading state — skeleton
                VStack(alignment: .leading, spacing: 8) {
                    ForEach(0..<3) { _ in
                        RoundedRectangle(cornerRadius: 4)
                            .fill(Color.preferredColor(.secondaryBackground))
                            .frame(height: 14)
                            .shimmer()
                    }
                }
                .padding(16)
            } else if loadError {
                // Error state
                IllustratedMessage {
                    Image(systemName: "exclamationmark.triangle")
                        .font(.system(size: 40))
                        .foregroundStyle(Color.preferredColor(.criticalLabel))
                } title: {
                    Text("Couldn't load insights")
                } action: {
                    FioriButton { _ in Text("Retry") }
                        .fioriButtonStyle(FioriSecondaryButtonStyle())
                        .onTapGesture { loadInsights() }
                }
            } else {
                // C. Generated content
                VStack(alignment: .leading, spacing: 12) {
                    Text(insights.summary)
                        .font(.fiori(forTextStyle: .body))
                        .foregroundStyle(Color.preferredColor(.primaryLabel))

                    // AI Notice (recommended)
                    HStack(spacing: 4) {
                        Image(systemName: "sparkles")
                            .foregroundStyle(Color.preferredColor(.tintColor))
                        Text("Created with AI. Verify before use.")
                            .foregroundStyle(Color.preferredColor(.secondaryLabel))
                    }
                    .font(.fiori(forTextStyle: .caption1))
                }
                .padding(16)
            }
        } footer: {
            // D. AI User Feedback + E. Regenerate button
            HStack {
                AIUserFeedbackInline(context: "Account Synopsis")
                Spacer()
                FioriButton { _ in
                    HStack(spacing: 4) {
                        Image(systemName: "sparkles")
                        Text("Regenerate")
                    }
                }
                .fioriButtonStyle(FioriTertiaryButtonStyle())
                .onTapGesture { loadInsights() }
            }
        }
    }
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Always include an AI Notice (B/B tag) — optional but highly recommended
- Use skeleton loading, not a spinner, during content generation
- Use IllustratedMessage for error states with retry
- Split into multiple cards when insights span categories

**Don't:**
- Show user-generated content in the full-screen variant
- Display multiple AI user feedback components on one screen

---

## Related

- [ai-user-feedback.md](ai-user-feedback.md)
- [ai-notice.md](ai-notice.md)
- [../components/cards.md](../components/cards.md)
- [../components/illustrated-message.md](../components/illustrated-message.md)
- [../components/skeleton-loading.md](../components/skeleton-loading.md)
