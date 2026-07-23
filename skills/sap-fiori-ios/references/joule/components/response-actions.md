# Response Actions — Joule Component

> SAP Fiori for iOS | Joule / Components

## What is it?

Response actions let users act on Joule-generated responses — copy, like, dislike, regenerate, view sources, or view explainability. Placed 4pt below every Joule response group.

---

## Rules

**Do:** Provide response actions after every Joule-generated response.
**Don't:** Show response actions for non-Joule-generated responses or notifications.

**Tips:**
- Never remove icons even if the action is unavailable — show error state if user taps an unavailable action
- Never change the style or order of the icon buttons — intentionally designed and positioned

---

## Anatomy (in order)

| Button | Icon | Accessibility label |
|--------|------|---------------------|
| **A. Copy** | Copy icon | "Copy" |
| **B. Thumbs Up** | 👍 | "Like this response" |
| **C. Thumbs Down** | 👎 | "Dislike this response" |
| **D. Regenerate** | Refresh icon | "Regenerate this response" |
| **E. Information** | ⓘ | "View sources" |
| **F. Sources** | Sources icon | "Source" |

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct ResponseActionsBar: View {
    let response: JouleResponse
    @State private var feedbackState: FeedbackState = .none

    enum FeedbackState { case none, positive, negative }

    var body: some View {
        HStack(spacing: 16) {
            // A. Copy
            FioriButton { _ in
                Image(systemName: "doc.on.doc")
                    .accessibilityLabel("Copy")
            }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .onTapGesture { UIPasteboard.general.string = response.text }

            // B. Thumbs up
            FioriButton { _ in
                Image(systemName: feedbackState == .positive
                      ? "hand.thumbsup.fill" : "hand.thumbsup")
                    .accessibilityLabel("Like this response")
            }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .foregroundStyle(feedbackState == .positive
                ? Color.preferredColor(.positiveLabel)
                : Color.preferredColor(.secondaryLabel))
            .onTapGesture { feedbackState = .positive; submitPositiveFeedback() }

            // C. Thumbs down
            FioriButton { _ in
                Image(systemName: feedbackState == .negative
                      ? "hand.thumbsdown.fill" : "hand.thumbsdown")
                    .accessibilityLabel("Dislike this response")
            }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .foregroundStyle(feedbackState == .negative
                ? Color.preferredColor(.negativeLabel)
                : Color.preferredColor(.secondaryLabel))
            .onTapGesture { feedbackState = .negative; showFeedbackDetail() }

            // D. Regenerate
            FioriButton { _ in
                Image(systemName: "arrow.clockwise")
                    .accessibilityLabel("Regenerate this response")
            }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .onTapGesture { regenerateResponse() }

            // E. Information / Sources
            FioriButton { _ in
                Image(systemName: "info.circle")
                    .accessibilityLabel("View sources")
            }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .onTapGesture { showSources() }
        }
        // Placement: 4pt below Joule response (from layout.md)
    }
}
```

---

## Related

- [../foundations/layout.md](../foundations/layout.md) — 4pt spacing rule
- [../patterns/feedback.md](../patterns/feedback.md)
- [../patterns/transparency-and-explainability.md](../patterns/transparency-and-explainability.md)
