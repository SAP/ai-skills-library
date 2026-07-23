# Buttons — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit` (Buttons page)
> Development reference: UIKit `FUIButton`, SwiftUI `FioriButton`

## What is it?

Buttons allow users to perform actions, make decisions, or begin a process. The label communicates the action that will be initiated.

---

## When to Use

**Do:**
- Use buttons only for actions
- Use simple, specific labels: "Create", "Edit", "Save", "Approve", "Reject", "Submit", "Cancel"
- Use short, meaningful labels in command form ("Save", not "Saving")
- Use toggle buttons to activate/deactivate or switch states (Follow/Unfollow, Select/Selected)
- Use secondary tint style for positive actions
- Use secondary negative style for destructive actions

**Don't:**
- Don't show too many buttons — it makes decisions harder. Use a segmented control instead when selecting from a small group
- Don't use green for positive actions — use tint style
- Don't truncate button labels

---

## Anatomy

A button consists of a label, a symbol, or both — on a filled or unfilled rectangular background with rounded corners.

Three content configurations:
- Symbol only
- Label only
- Label + symbol

---

## Button Types

### A. Primary Button
The most important action in the view. **Only one primary button per screen.**

Always uses filled (tint) style. Use for:
- Activate, Confirm, Continue, Create, Sign In, Scan

```swift
FioriButton { _ in Text("Sign In") }
    .fioriButtonStyle(FioriPrimaryButtonStyle())
```

### B. Secondary Button
Optional or lower-priority actions. Paired alongside primary or used standalone.

```swift
FioriButton { _ in Text("Dismiss") }
    .fioriButtonStyle(FioriSecondaryButtonStyle())
```

### C. Tertiary Button
Lowest-priority actions, or actions inside the navigation bar.

```swift
FioriButton { _ in Text("Learn More") }
    .fioriButtonStyle(FioriTertiaryButtonStyle())

// In navigation bar — symbol only
FioriButton { _ in
    Image(systemName: "plus")
        .accessibilityLabel("Add")
}
.fioriButtonStyle(FioriTertiaryButtonStyle())
```

### D. Toggle Button
Switches between two states without navigation. The button changes between secondary tint and secondary normal style.

Common pairs: Follow/Unfollow, Select/Selected, Bookmark/Bookmarked, Favorite/Unfavorite, Hold/Release

```swift
@State private var isFollowing = false

FioriButton(isSelectionPersistent: true) { state in
    Text(state == .selected ? "Following" : "Follow")
} image: { state in
    Image(systemName: state == .selected ? "person.fill.checkmark" : "person.badge.plus")
}
.fioriButtonStyle(FioriSecondaryButtonStyle())
// Visually switches between tint (selected) and normal (unselected)
```

---

## Button Styles

Styles work in tandem with button types to express priority and intent.

| Style | Use for |
|-------|---------|
| **Tint** | Primary actions; positive secondary actions |
| **Normal** | Medium-priority secondary/tertiary actions |
| **Negative** | Destructive secondary/tertiary actions |

> Note: Normal style has no Primary counterpart — Primary is always tint.

### Tint Style
- **Primary tint** — single most important action on screen
- **Secondary tint** — multiple equal-priority actions, or the positive action when paired with a negative one
- **Tertiary tint** — action in nav bar, or lowest priority on screen

### Normal Style
- **Secondary normal** — medium priority when mixed with tint-style actions; tint always outranks normal
- **Tertiary normal** — low-importance action; context-dependent

### Negative Style
- **Secondary negative** — one or more negative/destructive actions among equal-priority options
- **Tertiary negative** — multiple negative actions on a page (e.g. in multiple list rows), or lowest-priority destructive action

```swift
// Positive + negative pair (tint + negative)
HStack {
    FioriButton { _ in Text("Approve") }
        .fioriButtonStyle(FioriSecondaryButtonStyle())
        // secondary tint → positive

    FioriButton { _ in Text("Reject") }
        .fioriButtonStyle(FioriSecondaryButtonStyle())
        .tint(Color.preferredColor(.negativeLabel))
        // secondary negative → destructive
}

// Tertiary negative in a list row
FioriButton { _ in Text("Remove") }
    .fioriButtonStyle(FioriTertiaryButtonStyle())
    .tint(Color.preferredColor(.negativeLabel))
```

---

## Button Sizes

### 1. Auto-Width (default)
Grows to fit its label. Fixed height of **38pt**. Use inside components (cards, list rows, object cells).

```swift
FioriButton { _ in Text("Approve") }
    .fioriButtonStyle(FioriSecondaryButtonStyle())
// Width wraps content; height = 38pt automatically
```

### 2. Standalone
Fixed width **201pt**, height **44pt**. Use on single-topic pages (onboarding, sign-in, confirmation).

```swift
FioriButton { _ in Text("Sign In") }
    .fioriButtonStyle(FioriPrimaryButtonStyle())
    .frame(width: 201, height: 44)
```

### 3. Full-Width
Fills the container with **16pt horizontal padding**. Use in vertical button stacks.

```swift
FioriButton { _ in Text("Continue") }
    .fioriButtonStyle(FioriPrimaryButtonStyle())
    .frame(maxWidth: .infinity)
    .padding(.horizontal, 16)
```

### Toolbar
Buttons in `.toolbar {}` always use **38pt height** to save vertical space.

> Minimum touch area for any button: **44×44pt**

---

## Loading State Button

Apply when a user-triggered, non-disruptive process is running. The icon/label is replaced with an activity indicator and optional loading message.

**Only apply the animation when processing time is longer than 1000ms.**

### Loading State Variants

| Variant | Width behavior |
|---------|---------------|
| Auto-width loading | Width grows to show full loading message |
| Fixed-width loading | Width stays fixed; hides text if no space, shows indicator only |
| Full-width loading | Expands to container width; other buttons hide until complete |

### States

**A. Processing** — activity indicator rotates, replaces icon/label
**B. Success** — indicator replaced with success icon + message; remains for **3 seconds** then auto-advances
**C. Fail** — text replaced with error message; buttons become user action options

```swift
enum ButtonLoadingState {
    case idle, processing, success, failed
}

@State private var loadingState: ButtonLoadingState = .idle

FioriButton { _ in
    switch loadingState {
    case .idle:
        Text("Submit")
    case .processing:
        HStack(spacing: 8) {
            ProgressView()
                .tint(Color.preferredColor(.primaryBackground))
            Text("Submitting…")
        }
    case .success:
        HStack(spacing: 8) {
            Image(systemName: "checkmark")
            Text("Submitted")
        }
    case .failed:
        HStack(spacing: 8) {
            Image(systemName: "exclamationmark.circle")
            Text("Failed — Retry")
        }
    }
}
.fioriButtonStyle(FioriPrimaryButtonStyle())
.disabled(loadingState == .processing)
.frame(maxWidth: .infinity)
.onTapGesture {
    guard loadingState == .idle || loadingState == .failed else { return }
    Task {
        loadingState = .processing
        do {
            try await submitForm()
            loadingState = .success
            // Auto-advance after 3 seconds
            try await Task.sleep(for: .seconds(3))
            loadingState = .idle
        } catch {
            loadingState = .failed
        }
    }
}
```

---

## States

| State | Description | SwiftUI |
|-------|-------------|---------|
| Active | Button is interactive | Default |
| Tap / Pressed | Button has been pressed | Handled by style automatically |
| Disabled | Action available but disabled | `.disabled(true)` |
| Keyboard Focus | Focused via keyboard navigation | Automatic on iPadOS/macCatalyst |
| VoiceOver Focus | Focused during VoiceOver | Automatic + `.accessibilityLabel()` |

```swift
// Disabled
FioriButton { _ in Text("Submit") }
    .fioriButtonStyle(FioriPrimaryButtonStyle())
    .disabled(!formIsValid)
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Type | Primary | `FioriPrimaryButtonStyle()` |
| Type | Secondary | `FioriSecondaryButtonStyle()` |
| Type | Tertiary | `FioriTertiaryButtonStyle()` |
| Style | Tint | Default (no extra modifier) |
| Style | Negative | `.tint(Color.preferredColor(.negativeLabel))` |
| Style | Normal | `.tint(Color.preferredColor(.secondaryLabel))` |
| State | Disabled | `.disabled(true)` |
| State | Loading | Replace label with `ProgressView` + text |
| Width | Auto | Default — wraps content |
| Width | Standalone | `.frame(width: 201, height: 44)` |
| Width | Full | `.frame(maxWidth: .infinity).padding(.horizontal, 16)` |
| Toggle | Yes | `isSelectionPersistent: true` |
| Content | Label only | `FioriButton { _ in Text("...") }` |
| Content | Symbol only | `FioriButton { _ in Image(systemName: "...") }` |
| Content | Label + symbol | ViewBuilder with both `label` and `image` parameters |

---

## Common Patterns

### One primary + one secondary (most common)
```swift
VStack(spacing: 12) {
    FioriButton { _ in Text("Continue") }
        .fioriButtonStyle(FioriPrimaryButtonStyle())
        .frame(maxWidth: .infinity)

    FioriButton { _ in Text("Cancel") }
        .fioriButtonStyle(FioriSecondaryButtonStyle())
        .frame(maxWidth: .infinity)
}
.padding(.horizontal, 16)
```

### Approve / Reject (tint + negative)
```swift
HStack(spacing: 12) {
    FioriButton { _ in Text("Reject") }
        .fioriButtonStyle(FioriSecondaryButtonStyle())
        .tint(Color.preferredColor(.negativeLabel))

    FioriButton { _ in Text("Approve") }
        .fioriButtonStyle(FioriSecondaryButtonStyle())
}
```

### Navigation bar tertiary
```swift
.toolbar {
    ToolbarItem(placement: .primaryAction) {
        FioriButton { _ in
            Image(systemName: "square.and.pencil")
                .accessibilityLabel("Edit")
        }
        .fioriButtonStyle(FioriTertiaryButtonStyle())
    }
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- One Primary button per screen maximum
- Use tint/secondary for positive, negative/secondary for destructive
- Keep labels in command form and untruncated
- Meet 44×44pt minimum touch target
- Apply loading state only when processing > 1000ms
- Show success state for exactly 3 seconds before auto-advancing

**Don't:**
- Use green for positive actions — use tint style
- Stack more than 3 buttons vertically without reconsidering the information architecture
- Truncate labels — resize or shorten copy instead
- Use Primary style for more than one button in the same view

---

## Related Components

- [navigation-bar.md](navigation-bar.md) — tertiary buttons in toolbar
- [text-inputs.md](text-inputs.md) — form submission button patterns
- [single-user-onboarding.md](../patterns/single-user-onboarding.md) — standalone button sizing in onboarding
