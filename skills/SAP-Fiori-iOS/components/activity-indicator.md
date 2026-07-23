# Activity Indicator — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Progress Indicators
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUILoadingIndicatorView`, `FUIModalLoadingIndicatorView`, SwiftUI `LoadingIndicator`

## What is it?

The activity indicator is an animated circular spinner that communicates indeterminate progress — when the duration of an operation is unknown. The spinner fills clockwise during loading.

---

## Anatomy

```
[A. Spinner]  B. Label (optional)

or:

[A. Spinner]
 B. Label
```

**A. Spinner** — mandatory. Spins clockwise. Size differs by size class (see below).
**B. Label** (optional) — provides context about what is loading. Can appear to the right of or below the spinner.

---

## Spinner Sizes

| Size class | Spinner size |
|-----------|-------------|
| Compact (iPhone) | 22×22pt |
| Regular (iPad) | 30×30pt |

Label text size is the same on both size classes.

---

## Usage Patterns

### Full-Screen Loading
Centered on screen. Informs the user that app content is loading. Include a label when possible to describe what is loading.

### Lazy Loading
Appears inline below the current list content while additional items are being fetched as the user scrolls.

### Partial Loading
Placed on top of an overlay covering a portion of the screen. Overlay and indicator disappear once loading completes.

---

## SwiftUI Code Examples

### Full-screen loading
```swift
import FioriSwiftUICore

@State private var isLoading = true

ZStack {
    ContentView()
        .blur(radius: isLoading ? 2 : 0)
        .disabled(isLoading)

    if isLoading {
        LoadingIndicator(
            title: AttributedString("Loading invoices…"),
            isPresented: $isLoading,
            showsLoadingAnimation: true
        )
    }
}
```

### Partial loading overlay
```swift
ZStack {
    CardContent()
        .opacity(isRefreshing ? 0.4 : 1.0)

    if isRefreshing {
        ProgressView()
            .scaleEffect(1.2)
            .tint(Color.preferredColor(.tintColor))
    }
}
```

### Lazy loading (inline below list)
```swift
List {
    ForEach(items) { item in ObjectItem { Text(item.title) } }

    if isLoadingMore {
        HStack {
            Spacer()
            ProgressView()
                .tint(Color.preferredColor(.tintColor))
            Spacer()
        }
        .padding(.vertical, 8)
        .onAppear { loadMoreItems() }
    }
}
```

### With label
```swift
VStack(spacing: 12) {
    ProgressView()
        .scaleEffect(1.5)
        .tint(Color.preferredColor(.tintColor))
    Text("Syncing data…")
        .font(.fiori(forTextStyle: .subheadline))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Include a label when possible to describe what is loading
- Use the correct spinner size: 22pt compact, 30pt regular
- Use partial loading overlay for section-level updates

**Don't:**
- Use for operations with known duration — use `LinearProgressIndicator` instead
- Leave loading indefinitely without feedback if it takes longer than expected

---

## Related Components

- [linear-progress-indicator.md](linear-progress-indicator.md) — determinate progress (known duration)
- [checkout-indicator.md](checkout-indicator.md) — processing with success/error outcome
- [skeleton-loading.md](skeleton-loading.md) — structural placeholder while content loads
