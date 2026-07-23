# Checkout Indicator — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Progress Indicators
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUICheckoutIndicatorView`, `FUIModalCheckoutViewController`, SwiftUI `CheckoutIndicator`

## What is it?

A checkout indicator communicates that data is being processed by the system — typically after a user action such as submitting, sending, or syncing. It transitions from processing to either a success or error/fail state on completion.

---

## When to Use

Use when the system is analyzing, sending, or syncing information based on a user action. Display with an optional label.

---

## Anatomy

```
A. Indicator (spinning → success ✓ / error ✗)
B. Label (optional; mandatory in error state)
```

**A. Indicator** — circular spinner that transitions to success (green checkmark) or error/fail (red X) on completion.
**B. Label** — optional during processing; **mandatory** in error state to communicate the error message.

---

## Value States

| State | Visual | Label |
|-------|--------|-------|
| Processing | Spinning indicator | Optional |
| Success | Green checkmark fill | Optional |
| Error / Fail | Red X fill | **Mandatory** |

---

## Placement

| Placement | Use when |
|-----------|---------|
| Full-screen | User task requires blocking all other actions; navigates to another page after completion |
| Modal | Same-screen loading for major user tasks; returns to same page after completion |

---

## SwiftUI Code Examples

### Full three-state lifecycle
```swift
import FioriSwiftUICore

enum ProcessingState { case idle, processing, success, failure(String) }

@State private var state: ProcessingState = .idle

ZStack {
    ContentView()

    switch state {
    case .idle:
        EmptyView()

    case .processing:
        CheckoutIndicator(
            title: AttributedString("Submitting invoice…"),
            state: .inProgress
        )

    case .success:
        CheckoutIndicator(
            title: AttributedString("Invoice submitted"),
            state: .success
        )
        .onAppear {
            DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
                state = .idle
                navigateToNextScreen()
            }
        }

    case .failure(let message):
        // Label is mandatory for error state
        CheckoutIndicator(
            title: AttributedString(message),
            state: .error
        )
    }
}

func submitInvoice() {
    state = .processing
    Task {
        do {
            try await invoiceService.submit()
            state = .success
        } catch {
            state = .failure("Submission failed. Check your connection and try again.")
        }
    }
}
```

### Modal checkout indicator
```swift
@State private var showProcessing = false
@State private var processingState: ProcessingState = .processing

Button("Submit") {
    showProcessing = true
    processRequest()
}
.sheet(isPresented: $showProcessing) {
    VStack(spacing: 24) {
        CheckoutIndicator(
            title: processingLabel,
            state: processingState.indicatorState
        )
        if case .failure = processingState {
            FioriButton { _ in Text("Dismiss") }
                .fioriButtonStyle(FioriSecondaryButtonStyle())
                .onTapGesture { showProcessing = false }
        }
    }
    .padding(32)
    .presentationDetents([.fraction(0.3)])
    .interactiveDismissDisabled(processingState == .processing)
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| State | Processing | `state: .inProgress` — spinning |
| State | Success | `state: .success` — green checkmark |
| State | Error / Fail | `state: .error` — red X + mandatory label |
| Placement | Full-screen | `ZStack` overlay on full view |
| Placement | Modal | `.sheet` with `presentationDetents` |
| Label | Optional (processing) | `title: AttributedString(...)` |
| Label | Mandatory (error) | Always set in error state |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Always show an error label — tell the user what went wrong and how to resolve it
- Block interaction during processing (`.interactiveDismissDisabled(true)` in modal)
- Navigate to next screen after success (full-screen placement)
- Return to same screen after success (modal placement)

**Don't:**
- Leave error state without a message
- Use for operations without a clear success/fail outcome — use activity indicator instead

---

## Related Components

- [activity-indicator.md](activity-indicator.md) — indeterminate spinner without outcome states
- [linear-progress-indicator.md](linear-progress-indicator.md) — determinate progress with known duration
- [banner.md](banner.md) — error feedback at page level
