# Progress and Processing Indicator — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Progress Indicators
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIProgressIndicatorControl`, `FUIProcessingIndicatorView`, `FUIModalProcessingIndicator`, SwiftUI `ProgressIndicator`, `ProcessingIndicator`

## What is it?

Two related circular indicators that help users understand the status of an action:

- **Processing Indicator** — unknown progress; spinning animation while the system is working
- **Progress Indicator** — known progress; circular fill showing completion percentage; can include a stop action

They are often used together in a single user flow (e.g. processing → progress → complete/button).

---

## Anatomy

```
Processing Indicator:    Progress Indicator:
   A. Indicator             A. Indicator (filled arc)
   (spinning)               B. Track (circular background)
                            C. Icon (optional stop button)
```

**A. Indicator** — communicates loading status (processing) or actual progress (progress indicator).
**B. Track** — base circle showing full range (progress indicator only).
**C. Icon** (optional, progress indicator only) — interactive icon (e.g. stop) for user action during loading.

---

## Variations

### Processing Indicator
Used when request is being processed and **percentage is unknown**. Can transition to a progress indicator once the actual progress begins.

### Progress Indicator
Shows current stage of a process with a known percentage. Can include an optional interactive icon to allow user action (e.g. stop download). Replaced by another button or element once the process finishes.

---

## Combined Flow Pattern

```
Button tap
    → Processing Indicator (data transferring, % unknown)
    → Progress Indicator (download started, % known)
    → Button / Complete state (process finished)

User can tap the stop icon on Progress Indicator to terminate.
```

---

## SwiftUI Code Examples

### Processing indicator (indeterminate)
```swift
import FioriSwiftUICore

ProcessingIndicator(
    title: { Text("Processing…") },
    progressIndicatorStyle: .indeterminate
)
```

### Progress indicator (determinate, with stop action)
```swift
@State private var downloadProgress: Double = 0
@State private var isDownloading = true

ProgressIndicator(
    progress: downloadProgress,
    icon: isDownloading ? Image(systemName: "stop.fill") : nil,
    onIconTap: { cancelDownload() }
)
```

### Full combined flow
```swift
enum DownloadState { case idle, processing, downloading, complete }

@State private var downloadState: DownloadState = .idle
@State private var progress: Double = 0

switch downloadState {
case .idle:
    FioriButton { _ in Text("Download") }
        .fioriButtonStyle(FioriPrimaryButtonStyle())
        .onTapGesture {
            downloadState = .processing
            startTransfer()
        }

case .processing:
    ProcessingIndicator(
        title: { Text("Connecting…") },
        progressIndicatorStyle: .indeterminate
    )

case .downloading:
    ProgressIndicator(
        progress: progress,
        icon: Image(systemName: "stop.fill")
    ) {
        cancelDownload()
        downloadState = .idle
    }

case .complete:
    FioriButton { _ in Text("Open File") }
        .fioriButtonStyle(FioriSecondaryButtonStyle())
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Type | Processing | `ProcessingIndicator` — spinning |
| Type | Progress | `ProgressIndicator(progress:)` — arc fill |
| Icon | Stop | `icon: Image(systemName: "stop.fill")` |
| Icon | None | Omit `icon` |
| State | Processing → Progress | Transition from `ProcessingIndicator` to `ProgressIndicator` |
| State | Complete | Replace with `FioriButton` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Chain processing → progress → complete in a single user flow when appropriate
- Allow the user to stop/cancel via the optional icon
- Replace the indicator with a button or completion state when done

**Don't:**
- Use processing indicator when the percentage is known — use progress indicator
- Leave the indicator indefinitely without offering a cancel option

---

## Related Components

- [activity-indicator.md](activity-indicator.md) — full-screen / partial loading spinner
- [linear-progress-indicator.md](linear-progress-indicator.md) — horizontal bar progress
- [checkout-indicator.md](checkout-indicator.md) — circular indicator with success/error outcome states
