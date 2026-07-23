# AI User Feedback — In-App AI Design

> SAP Fiori for iOS | In-App AI Design / Patterns
> Development reference: `AIUserFeedback`

## What is it?

AI user feedback lets users give positive or negative feedback about embedded AI experiences — from component-level thumbs up/down to detailed category-based feedback.

---

## When to Use

**Do:** Allow users to rate their embedded AI experience.
**Don't:** Request feedback unrelated to AI.

**Tips:**
- Describe which AI experience is being evaluated
- Let users exit at any time
- Provide a re-entry point for later feedback
- Avoid requesting feedback multiple times for the same experience

---

## Anatomy

**A. Header** — nav bar with title + exit/back button
**B. Title** — what is being evaluated
**C. Description** (optional) — additional context
**D. Feedback Buttons** — thumbs up / thumbs down (empty by default)
**E. Filter** (optional, detail view) — categories for negative feedback
**F. Additional feedback** (optional, detail view) — key value form cell for free text
**G. Submit button** (optional, detail view) — submits negative feedback

---

## Entry Points

| Entry type | Use for |
|-----------|---------|
| **Automatic pop-up** | Screen-level AI experiences; shown when complete |
| **Inline buttons** | Component-level; thumbs up/down next to AI content |
| **Overflow button / menu item** | Re-entry point for submitting or modifying feedback later |

---

## Interaction Flows

### Positive Feedback
Tap thumbs-up → **immediate submission** → toast message confirms.

### Negative Feedback
Tap thumbs-down → detail view opens → optional filter categories + free text → tap "Submit" → toast confirms.

### Change of Mind
In negative detail view → tap thumbs-up → positive feedback recorded instead.

---

## States

| State | Behavior |
|-------|---------|
| Success | Toast: "Feedback submitted" |
| Error (field) | Inline error on missing/wrong field value |
| Error (submission) | Illustrated message replaces bottom sheet content; user can exit and retry later |

---

## Presentation

| Size class | Container |
|-----------|-----------|
| Compact | Bottom sheet (flexible height: default, mini, medium, large) |
| Regular — blocks interaction | Inspector |
| Regular — allows background interaction | Popover |

**Modal (intrusive):** Overlay behind sheet blocks all interaction — used with modal view.
**Activity (non-intrusive):** No overlay — user can scroll behind the sheet while providing feedback.

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

// Inline AI user feedback (component level)
struct AIUserFeedbackInline: View {
    let context: String
    @State private var feedbackState: FeedbackState = .none
    @State private var showDetail = false
    @State private var showToast = false

    enum FeedbackState { case none, positive, negative }

    var body: some View {
        HStack(spacing: 12) {
            // Thumbs up
            FioriButton { _ in
                Image(systemName: feedbackState == .positive
                      ? "hand.thumbsup.fill" : "hand.thumbsup")
                    .accessibilityLabel("Helpful")
            }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .foregroundStyle(feedbackState == .positive
                ? Color.preferredColor(.positiveLabel)
                : Color.preferredColor(.secondaryLabel))
            .onTapGesture {
                feedbackState = .positive
                submitPositiveFeedback(context: context)
                showToast = true
                autoDismissToast()
            }

            // Thumbs down
            FioriButton { _ in
                Image(systemName: feedbackState == .negative
                      ? "hand.thumbsdown.fill" : "hand.thumbsdown")
                    .accessibilityLabel("Not helpful")
            }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .foregroundStyle(feedbackState == .negative
                ? Color.preferredColor(.negativeLabel)
                : Color.preferredColor(.secondaryLabel))
            .onTapGesture {
                feedbackState = .negative
                showDetail = true
            }
        }
        .sheet(isPresented: $showDetail) {
            AIFeedbackDetailView(
                context: context,
                onPositive: {
                    feedbackState = .positive
                    showDetail = false
                    showToast = true
                },
                onSubmit: {
                    showDetail = false
                    showToast = true
                }
            )
            .presentationDetents([.medium, .large])
        }
        .overlay(alignment: .bottom) {
            if showToast {
                ToastMessage { Text("Feedback submitted") } icon: {
                    Image(systemName: "checkmark.circle.fill")
                        .foregroundStyle(Color.preferredColor(.positiveLabel))
                }
                .padding(.bottom, 24)
            }
        }
    }
}

// Detail view for negative feedback
struct AIFeedbackDetailView: View {
    let context: String
    let onPositive: () -> Void
    let onSubmit: () -> Void
    @State private var selectedReasons: Set<Int> = []
    @State private var additionalFeedback = ""

    let reasons = ["Inaccurate", "Incomplete", "Off-topic", "Too long", "Too short"]

    var body: some View {
        NavigationStack {
            Form {
                Section {
                    Text("How was the AI experience for \"\(context)\"?")
                        .font(.fiori(forTextStyle: .headline))

                    // Change of mind — thumbs up in detail view
                    HStack {
                        FioriButton { _ in Image(systemName: "hand.thumbsup") }
                            .fioriButtonStyle(FioriTertiaryButtonStyle())
                            .onTapGesture { onPositive() }
                        FioriButton { _ in Image(systemName: "hand.thumbsdown.fill") }
                            .fioriButtonStyle(FioriTertiaryButtonStyle())
                            .foregroundStyle(Color.preferredColor(.negativeLabel))
                    }
                }

                // E. Filter
                Section("What went wrong?") {
                    FilterFormView(
                        title: { Text("") },
                        options: reasons.map { AttributedString($0) },
                        selectedIndices: Binding(
                            get: { Array(selectedReasons) },
                            set: { selectedReasons = Set($0) }
                        ),
                        allowsMultipleSelection: true
                    )
                }

                // F. Additional feedback
                Section {
                    KeyValueFormView(
                        title: { Text("Additional comments (optional)") },
                        text: $additionalFeedback
                    )
                }
            }
            .navigationTitle("Feedback")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    FioriButton { _ in Image(systemName: "xmark").accessibilityLabel("Close") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { onSubmit() }  // exit without submitting
                }
                ToolbarItem(placement: .confirmationAction) {
                    // G. Submit button
                    FioriButton { _ in Text("Submit") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture {
                            submitNegativeFeedback(reasons: selectedReasons, text: additionalFeedback)
                            onSubmit()
                        }
                }
            }
        }
    }
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Submit positive feedback immediately on thumbs-up tap
- Show the detail view only for negative feedback
- Allow changing from negative to positive in the detail view
- Show toast on successful submission
- Use illustrated message for submission errors (not inline)
- Provide a re-entry point (overflow menu) for later feedback

**Don't:**
- Request the same feedback multiple times
- Make all filter/text fields mandatory for negative feedback
- Show multiple AI feedback components on the same screen

---

## Related

- [ai-insights.md](ai-insights.md)
- [ai-writing-assistant.md](ai-writing-assistant.md)
- [../components/toast-message.md](../components/toast-message.md)
- [../components/illustrated-message.md](../components/illustrated-message.md)
