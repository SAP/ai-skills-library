# Linear Progress Indicator — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Progress Indicators
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUILinearProgressIndicator`, SwiftUI `LinearProgressIndicator`

## What is it?

A linear progress indicator communicates the status of an ongoing process (login, file upload, content refresh). It fills along a horizontal track and can be determinate (known progress) or indeterminate (unknown duration).

**Only use when the wait time exceeds 1 second.**

---

## Anatomy

### Active state
```
A. Indicator (filled portion) ████████░░░░
B. Track (full width)         ────────────
C. Label (optional)           Uploading… 60%
```

### Value state (success / error)
```
B. Track (fills completely — success green / error red)
C. Validation message (mandatory for both states)
```

**A. Indicator** — the filled/animated portion.
**B. Track** — the full-width background track.
**C. Label / Validation message** — optional during active state; **mandatory** for error and success states.

---

## When to Use Labels

| Condition | Label |
|-----------|-------|
| Process < 10s | Omit label |
| Process ≥ 10s | Include label |
| Height/width too constrained | Omit label |
| Error state | **Mandatory** — explain what failed and how to resolve |
| Success state | **Mandatory** — confirm what completed |

Keep labels to **1 line** (2 lines maximum on compact only — wrapping not recommended).
For determinate indicators, include a progress value at the end of the label (e.g. "Uploading… 60%", "30/100 files").
Do not include a progress value in error or success states.

---

## Variations

### A. Determinate
Known duration — fills from 0% to 100%, never decreasing. Use for file uploads/downloads of known size.

### B. Indeterminate
Unknown duration — animating indicator. Use when duration can't be determined.

### C. Indeterminate → Determinate
Switches from indeterminate to determinate once the process reaches a point where its duration is known.

---

## Value States

### Success
- Indicator turns **green**, entire track fills with success color
- Label changes to success message (mandatory)
- Either persists until user action OR **auto-disappears after 3 seconds**

### Error / Fail
- Animation stops; indicator turns **red**, entire track fills with error color
- Label changes to error message (mandatory) — explain what failed and how to resolve

---

## Adaptive Design

| Size class | Label wrapping |
|-----------|---------------|
| Compact | Wrapping allowed (max 2 lines, not recommended) |
| Regular | No wrapping — label never exceeds 1 line |

On regular width, keep the indicator + label within **672pt** for readability.

---

## SwiftUI Code Examples

### Determinate with progress value in label
```swift
import FioriSwiftUICore

@State private var uploadProgress: Double = 0
@State private var uploadState: ProgressState = .active

LinearProgressIndicator(
    indicatorColor: uploadState == .success
        ? Color.preferredColor(.positiveLabel)
        : uploadState == .error
        ? Color.preferredColor(.negativeLabel)
        : Color.preferredColor(.tintColor),
    progress: uploadProgress
)

// Label below
if uploadState == .active {
    Text("Uploading file… \(Int(uploadProgress * 100))%")
        .font(.fiori(forTextStyle: .footnote))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
} else if uploadState == .success {
    Text("Upload complete")
        .font(.fiori(forTextStyle: .footnote))
        .foregroundStyle(Color.preferredColor(.positiveLabel))
} else {
    Text("Upload failed. Check your connection and try again.")
        .font(.fiori(forTextStyle: .footnote))
        .foregroundStyle(Color.preferredColor(.negativeLabel))
}
```

### Indeterminate
```swift
LinearProgressIndicator(
    indicatorColor: Color.preferredColor(.tintColor),
    progress: nil  // nil = indeterminate
)
```

### Indeterminate → Determinate transition
```swift
@State private var progress: Double? = nil  // nil = indeterminate

LinearProgressIndicator(
    indicatorColor: Color.preferredColor(.tintColor),
    progress: progress
)

// Switch to determinate when size becomes known
.onReceive(uploadSizePublisher) { totalBytes in
    if totalBytes > 0 {
        progress = 0.0  // switch to determinate
    }
}
.onReceive(uploadProgressPublisher) { bytesUploaded in
    if let total = totalBytes {
        progress = Double(bytesUploaded) / Double(total)
    }
}
```

### Full upload pattern with all states
```swift
enum UploadState { case idle, uploading, success, error(String) }

@State private var uploadState: UploadState = .idle
@State private var progress: Double = 0

VStack(alignment: .leading, spacing: 4) {
    switch uploadState {
    case .idle:
        EmptyView()

    case .uploading:
        LinearProgressIndicator(
            indicatorColor: Color.preferredColor(.tintColor),
            progress: progress
        )
        // Label only if process > 10s
        Text("Uploading report… \(Int(progress * 100))%")
            .font(.fiori(forTextStyle: .footnote))
            .foregroundStyle(Color.preferredColor(.secondaryLabel))

    case .success:
        LinearProgressIndicator(
            indicatorColor: Color.preferredColor(.positiveLabel),
            progress: 1.0
        )
        Text("Report uploaded successfully")  // mandatory
            .font(.fiori(forTextStyle: .footnote))
            .foregroundStyle(Color.preferredColor(.positiveLabel))
        // Auto-dismiss after 3s or wait for user action

    case .error(let message):
        LinearProgressIndicator(
            indicatorColor: Color.preferredColor(.negativeLabel),
            progress: 1.0
        )
        Text(message)  // mandatory — explain and guide resolution
            .font(.fiori(forTextStyle: .footnote))
            .foregroundStyle(Color.preferredColor(.negativeLabel))
            .lineLimit(2)  // max 2 lines on compact; 1 on regular
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Variation | Determinate | `progress: Double (0.0–1.0)` |
| Variation | Indeterminate | `progress: nil` |
| Variation | Indeterminate → Determinate | Start `nil`, switch to `Double` |
| State | Active | `.tintColor` indicator |
| State | Success | `progress: 1.0` + `.positiveLabel` color |
| State | Error / Fail | `progress: 1.0` + `.negativeLabel` color |
| Label | With progress value | `"Uploading… 60%"` (determinate only) |
| Label | Success message | Mandatory — short completion confirmation |
| Label | Error message | Mandatory — what failed + how to resolve |
| Label wrapping | Compact | Max 2 lines |
| Label wrapping | Regular | Max 1 line — no wrapping |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Only use when wait time > 1 second
- Include a progress value in determinate labels (60%, 30/100)
- Make error and success labels mandatory
- Auto-dismiss success after 3 seconds OR wait for user action (choose based on context)
- Keep within 672pt width on regular screens

**Don't:**
- Show labels for processes < 10 seconds
- Include progress values in error or success state labels
- Allow wrapping on regular width — keep to 1 line
- Let progress decrease — determinate bars only fill forward

---

## Related Components

- [activity-indicator.md](activity-indicator.md) — indeterminate spinner (no track)
- [checkout-indicator.md](checkout-indicator.md) — circular indicator with success/error states
- [skeleton-loading.md](skeleton-loading.md) — structural placeholder while loading
