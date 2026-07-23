# Empty State View — Component Guidelines

> ⚠️ **Deprecated** — This component appears to be superseded by [Illustrated Message](illustrated-message.md), which provides the same functionality with a more complete and up-to-date design system. Use `IllustratedMessage` for all new work.

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: No SDK class listed (no UIKit/SwiftUI reference in portal)

## What is it?

The empty state view provides fallback messaging when an app has no data to show. It can appear in cards, chart cards, chart floorplans, and chart headers.

> **Use `IllustratedMessage` instead.** It covers all the same use cases with richer guidance, illustration sizing rules, and CTA support. See [illustrated-message.md](illustrated-message.md).

---

## Anatomy

```
A. Illustration (optional)   ← custom or Fiori Moments library
B. Title                     ← reason for empty state; 1 line preferred
C. Description               ← chart full-screen mode only
```

**A. Illustration** (optional) — custom illustration or from the Fiori Moments library.
**B. Title** — explains the empty state reason; preferably one line.
**C. Description** — for charts, only available in full-screen mode.

---

## Migration

Replace `EmptyStateView` usage with `IllustratedMessage`:

```swift
// ❌ Old — Empty State View (deprecated)
// EmptyStateView(title: "No data", description: "Try again later")

// ✅ New — Illustrated Message
import FioriSwiftUICore

IllustratedMessage {
    Image(systemName: "chart.bar")
        .font(.system(size: 64))
        .foregroundStyle(Color.preferredColor(.tertiaryLabel))
} title: {
    Text("No data available")
} description: {
    Text("Try adjusting your filters or check back later.")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
        .multilineTextAlignment(.center)
}
```

---

## Related Components

- [illustrated-message.md](illustrated-message.md) — **use this instead**
- [charts.md](charts.md) — chart empty states
- [banner.md](banner.md) — system-level notifications
