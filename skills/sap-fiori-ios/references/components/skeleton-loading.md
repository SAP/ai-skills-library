# Skeleton Loading — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Progress Indicators
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: SDK skeleton loading components

## What is it?

Skeleton loading is a progress indicator that shows structural placeholders while a screen or section is loading. It is used when the layout and structure of the content are known but the actual data hasn't arrived yet.

**Use when loading time exceeds 1 second and the target layout is known.**

---

## When to Use

**Do:**
- Use only when the target structure and layout are known
- Use when loading time exceeds 1 second
- Use generic cell/card placeholders, or build customized ones from basic placeholders
- Provide feedback when loading takes longer than expected or data retrieval fails

**Don't:**
- Use placeholder types that don't match the target content type
- Get overly detailed with customized placeholders — distracts the user
- Combine multiple types of progress indicators with skeleton loading (e.g. spinner + skeleton simultaneously)

---

## Anatomy

**A. Placeholder** — replaces actual content during loading. Should match the content's type, layout, and size. If specific details can't be determined, ensure the type aligns with the content.

**B. Container** — fixed lines, paddings, and margins. There may be slight size variations between the placeholder container and the actual content container.

---

## Shimmer Effect

The default shimmer animation:
- Black shimmer at **8% opacity**
- Moves **left to right** in a continuous loop
- Applied automatically to all placeholders

---

## Transition

Skeleton loading automatically transitions to actual content once data fetching completes. Use for loading times > 1 second.

---

## Placeholder Types

### Basic Placeholders (building blocks)

| Type | Options |
|------|---------|
| **Text** | 5 height options matching font sizes: 13pt (footnote/caption), 20pt (body/headline/title3), 28pt (title1/title2), 41pt (large title/medium KPI), 57pt (large KPI). Adjustable width. |
| **Image** | Various size options. Optional icon (customizable per iconography guidelines). |
| **Avatar** | Multiple fixed sizes. Also used for KPI progress chart placeholders. |
| **Button** | Replaces label buttons, symbol buttons, filter buttons, or tags. |
| **Object Cell** | One-line or multi-line object cell placeholder. |

> Use these text placeholder heights instead of matching font sizes directly — they represent the visual block size, not the exact type size.

### Card Placeholders
For skeleton loading at card level:
- One-line object card
- Multi-line object card
- Analytic data table card
- List card
- Generic card placeholder (when card type is unknown)

### Header Placeholders
For replacing headers during skeleton loading:
- Object header placeholder (compact and regular variants)

---

## SwiftUI Code Examples

### Text placeholder (shimmer animation)
```swift
struct SkeletonText: View {
    let height: CGFloat
    let width: CGFloat
    @State private var opacity: Double = 0.3

    var body: some View {
        RoundedRectangle(cornerRadius: 4)
            .fill(Color.preferredColor(.secondaryBackground))
            .frame(width: width, height: height)
            .overlay(
                // Shimmer: 8% opacity black, left to right
                LinearGradient(
                    colors: [.clear, Color.black.opacity(0.08), .clear],
                    startPoint: .leading,
                    endPoint: .trailing
                )
                .offset(x: shimmerOffset)
            )
            .clipShape(RoundedRectangle(cornerRadius: 4))
            .onAppear { startShimmer() }
    }
}
```

### Object cell placeholder (multi-line)
```swift
struct SkeletonObjectCell: View {
    @State private var shimmerOffset: CGFloat = -200

    var body: some View {
        HStack(spacing: 12) {
            // Avatar placeholder — fixed size
            Circle()
                .fill(Color.preferredColor(.secondaryBackground))
                .frame(width: 40, height: 40)

            VStack(alignment: .leading, spacing: 6) {
                // Headline placeholder — 20pt
                RoundedRectangle(cornerRadius: 4)
                    .fill(Color.preferredColor(.secondaryBackground))
                    .frame(height: 20)

                // Subheadline placeholder — 20pt, shorter width
                RoundedRectangle(cornerRadius: 4)
                    .fill(Color.preferredColor(.secondaryBackground))
                    .frame(width: 180, height: 20)

                // Footnote placeholder — 13pt
                RoundedRectangle(cornerRadius: 4)
                    .fill(Color.preferredColor(.secondaryBackground))
                    .frame(width: 120, height: 13)
            }

            Spacer()
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 12)
        .shimmer()
    }
}
```

### Card placeholder (generic)
```swift
struct SkeletonCard: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            // Header placeholders
            HStack(spacing: 12) {
                RoundedRectangle(cornerRadius: 6)
                    .fill(Color.preferredColor(.secondaryBackground))
                    .frame(width: 40, height: 40)

                VStack(alignment: .leading, spacing: 6) {
                    RoundedRectangle(cornerRadius: 4)
                        .fill(Color.preferredColor(.secondaryBackground))
                        .frame(height: 20)
                    RoundedRectangle(cornerRadius: 4)
                        .fill(Color.preferredColor(.secondaryBackground))
                        .frame(width: 120, height: 13)
                }
                Spacer()
            }

            // Body placeholders
            VStack(alignment: .leading, spacing: 6) {
                ForEach(0..<3) { _ in
                    RoundedRectangle(cornerRadius: 4)
                        .fill(Color.preferredColor(.secondaryBackground))
                        .frame(height: 13)
                }
            }
        }
        .padding(16)
        .background(Color.preferredColor(.secondaryGroupedBackground))
        .clipShape(RoundedRectangle(cornerRadius: 12))
        .shadow(color: Color.preferredColor(.cardShadow), radius: 4, x: 0, y: 2)
        .shimmer()
    }
}
```

### Shimmer view modifier (reusable)
```swift
struct ShimmerModifier: ViewModifier {
    @State private var phase: CGFloat = -1

    func body(content: Content) -> some View {
        content
            .overlay(
                GeometryReader { geo in
                    LinearGradient(
                        colors: [.clear, Color.black.opacity(0.08), .clear],
                        startPoint: .leading,
                        endPoint: .trailing
                    )
                    .frame(width: geo.size.width * 2)
                    .offset(x: phase * geo.size.width)
                }
                .clipped()
            )
            .onAppear {
                withAnimation(
                    .linear(duration: 1.2).repeatForever(autoreverses: false)
                ) {
                    phase = 1
                }
            }
    }
}

extension View {
    func shimmer() -> some View { modifier(ShimmerModifier()) }
}
```

### Full list with skeleton loading
```swift
@State private var isLoading = true
@State private var items: [Invoice] = []

List {
    if isLoading {
        // Show skeleton cells while loading
        ForEach(0..<6, id: \.self) { _ in
            SkeletonObjectCell()
                .listRowSeparator(.hidden)
        }
    } else {
        ForEach(items) { item in
            ObjectItem { Text(item.number) }
                .subtitle: { Text(item.vendor) }
        }
    }
}
.task {
    items = await loadInvoices()
    isLoading = false
}
```

### Object header placeholder
```swift
struct SkeletonObjectHeader: View {
    var body: some View {
        HStack(spacing: 12) {
            // Thumbnail placeholder
            RoundedRectangle(cornerRadius: 8)
                .fill(Color.preferredColor(.secondaryBackground))
                .frame(width: 60, height: 60)

            VStack(alignment: .leading, spacing: 8) {
                // Title — 28pt
                RoundedRectangle(cornerRadius: 4)
                    .fill(Color.preferredColor(.secondaryBackground))
                    .frame(height: 28)

                // Subtitle — 20pt, shorter
                RoundedRectangle(cornerRadius: 4)
                    .fill(Color.preferredColor(.secondaryBackground))
                    .frame(width: 160, height: 20)
            }
            Spacer()
        }
        .padding(16)
        .shimmer()
    }
}
```

---

## Text Placeholder Heights Reference

| Height | Replaces |
|--------|---------|
| 13pt | Footnote, Caption 1, Caption 2 |
| 20pt | Subheadline, Callout, Body, Headline, Title 3 |
| 28pt | Title 2, Title 1 |
| 41pt | Large Title, Medium KPI |
| 57pt | Large KPI |

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Type | Text | `RoundedRectangle` at correct height |
| Type | Image | `RoundedRectangle` at target image size |
| Type | Avatar | `Circle` at fixed avatar size |
| Type | Button | `RoundedRectangle` at button height |
| Type | Object cell | `SkeletonObjectCell` (HStack layout) |
| Type | Card | `SkeletonCard` (VStack with header/body) |
| Type | Object header | `SkeletonObjectHeader` |
| Animation | Shimmer | `.shimmer()` modifier (8% black, L→R) |
| Transition | To real content | `isLoading = false` replaces placeholders |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Match placeholder type and approximate size to the actual content
- Use text placeholder heights from the reference table — not raw font sizes
- Apply the shimmer animation (8% black, left-to-right loop)
- Transition automatically to real content when data arrives
- Show feedback (error message or illustrated message) if data retrieval fails

**Don't:**
- Use when the target layout is unknown — use an activity indicator instead
- Mix skeleton loading with other progress indicators (spinner, linear bar) on the same screen
- Make placeholders overly detailed — approximate layout is sufficient
- Use for loading times under 1 second

---

## Related Components

- [activity-indicator.md](activity-indicator.md) — when layout is unknown
- [linear-progress-indicator.md](linear-progress-indicator.md) — determinate progress
- [illustrated-message.md](illustrated-message.md) — error state when data retrieval fails
