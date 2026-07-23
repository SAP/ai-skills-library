# Feedback Indicators — Component Guidelines

> SAP Fiori for iOS | Category: Pattern Overview
> Development reference: UIKit `FUIProgressIndicatorControl`, `FUIProcessingIndicatorView`, `FUICheckoutIndicatorView`
> This is a conceptual guide — see the linked component files for implementation details.

## What is it?

Feedback indicators provide timely responses to user actions or inform users about loading states and process conditions. Two categories:

| Category | Description | Components |
|----------|-------------|-----------|
| **System feedback** | System-generated status of activities and processes | Network activity indicator, Loading indicator |
| **User-triggered feedback** | Response to a specific user action | Checkout indicator, Progress/Processing indicator, Toast message |

---

## System Feedback

### Network Activity Indicator
The iOS system's built-in indeterminate progress view (spinner in the status bar). Appears automatically when the device is communicating with a network (loading, downloading, sending/receiving data). No custom implementation needed — the system manages it. See Apple HIG – Progress Indicators.

### Loading Indicator
Visual feedback that app content is loading. Three placement patterns:

| Pattern | Use when |
|---------|---------|
| **Full-screen** | App content is loading; centered on screen |
| **Lazy loading** | Additional list content is loading as user scrolls |
| **Partial loading** | Part of the screen needs to refresh; overlay covers the affected area |

**→ See [activity-indicator.md](activity-indicator.md) for full implementation.**

---

## User-Triggered Feedback

### Checkout Indicator
Communicates that data is being processed after a user action (analyzing, sending, syncing). Three states: **Processing → Success / Error**.

| Placement | Use when |
|-----------|---------|
| Full-screen | Major task blocks other actions; navigates to another page on completion |
| Modal | Major task blocks other actions; returns to same page on completion |

**→ See [checkout-indicator.md](checkout-indicator.md) for full implementation.**

### Progress and Processing Indicator
Two related circular indicators that can be chained:

| Indicator | Use when |
|-----------|---------|
| **Processing** | Request is being processed, % unknown |
| **Progress** | % is known; can include a stop/cancel button |

Typical flow: button tap → Processing → (% becomes known) → Progress → Complete/button.

**→ See [progress-and-processing-indicator.md](progress-and-processing-indicator.md) for full implementation.**

### Toast Message
Brief indicator centered on screen confirming a user action was completed. Auto-dismisses after 2–5 seconds.

**→ See [toast-message.md](toast-message.md) for full implementation.**

---

## Choosing the Right Feedback Indicator

| Situation | Indicator |
|-----------|----------|
| App content loading (unknown duration) | `LoadingIndicator` (full-screen) |
| More list items loading on scroll | `LoadingIndicator` (lazy/inline) |
| Part of screen refreshing | `LoadingIndicator` (partial overlay) |
| User submitted a request; processing with success/fail outcome | `CheckoutIndicator` |
| Download/upload with known % + cancel option | `ProgressIndicator` |
| Processing with unknown % | `ProcessingIndicator` |
| Brief confirmation after action completes | `ToastMessage` |

---

## Related Components

- [activity-indicator.md](activity-indicator.md) — loading indicator (system feedback)
- [checkout-indicator.md](checkout-indicator.md) — processing → success/error
- [progress-and-processing-indicator.md](progress-and-processing-indicator.md) — circular progress
- [toast-message.md](toast-message.md) — transient confirmation
- [linear-progress-indicator.md](linear-progress-indicator.md) — horizontal bar progress
- [skeleton-loading.md](skeleton-loading.md) — structural content placeholder
