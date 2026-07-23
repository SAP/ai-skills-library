# KPI Header — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Headers
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit` (KPI page)
> Development reference: UIKit `FUIKPIHeader`, SwiftUI `KPIHeader`

## What is it?

The KPI header displays numerical data the user needs to track throughout the day. It is typically used in an overview pattern to provide contextual information at the top of a screen.

---

## Anatomy

A container holding multiple KPI items side by side. For individual KPI presentation options, see [kpi-item.md](kpi-item.md).

---

## Adaptive Design

### Compact Width (iPhone)

- Maximum **3 KPIs** per page
- Actual count may be lower depending on individual KPI width
- **Page controls** allow additional KPIs across multiple pages without crowding

| Pages | Layout |
|-------|--------|
| 1 page | Up to 3 KPIs visible |
| 2+ pages | Page indicator dots shown; user swipes to see more |

### Regular Width (iPad)

- Maximum **4 KPIs** in the header
- If more KPIs are needed, place the extras in the content area
- Only the **large variation** of the KPI progress view can be used here
- KPI progress view is always displayed **first**, followed by other KPIs

---

## SwiftUI Code Examples

### Basic KPIHeader
```swift
import FioriSwiftUICore

KPIHeader {
    KPIItem(
        kpiCaption: AttributedString("Revenue"),
        items: [KPISubItem(value: AttributedString("$1.4M"))],
        proposedViewSize: .large
    )
    KPIItem(
        kpiCaption: AttributedString("Orders"),
        items: [KPISubItem(value: AttributedString("342"))],
        proposedViewSize: .large
    )
    KPIItem(
        kpiCaption: AttributedString("Avg. Deal"),
        items: [KPISubItem(value: AttributedString("$4.1K"))],
        proposedViewSize: .large
    )
}
```

### With KPI progress view (regular width — shown first)
```swift
KPIHeader {
    // KPI progress view always first in regular width
    KPIProgressItem {
        Text("72%")
            .font(.fiori(forTextStyle: .KPI, weight: .light))
    } subtitle: {
        Text("Quota")
    } progress: {
        ProgressView(value: 0.72)
            .tint(Color.preferredColor(.positiveLabel))
    }

    // Additional KPIs follow
    KPIItem(
        kpiCaption: AttributedString("Revenue"),
        items: [KPISubItem(value: AttributedString("$1.4M"))],
        proposedViewSize: .large
    )
    KPIItem(
        kpiCaption: AttributedString("Deals"),
        items: [KPISubItem(value: AttributedString("28"))],
        proposedViewSize: .large
    )
}
```

### Compact with page controls (more than 3 KPIs)
```swift
// Use TabView with page style for paginated KPI header on compact
@Environment(\.horizontalSizeClass) var hSizeClass

if hSizeClass == .compact {
    TabView {
        // Page 1 — up to 3 KPIs
        KPIHeader {
            KPIItem(kpiCaption: AttributedString("Revenue"),
                    items: [.init(value: AttributedString("$1.4M"))],
                    proposedViewSize: .large)
            KPIItem(kpiCaption: AttributedString("Orders"),
                    items: [.init(value: AttributedString("342"))],
                    proposedViewSize: .large)
            KPIItem(kpiCaption: AttributedString("Open"),
                    items: [.init(value: AttributedString("18"))],
                    proposedViewSize: .large)
        }
        .tag(0)

        // Page 2
        KPIHeader {
            KPIItem(kpiCaption: AttributedString("Avg. Deal"),
                    items: [.init(value: AttributedString("$4.1K"))],
                    proposedViewSize: .large)
            KPIItem(kpiCaption: AttributedString("Win Rate"),
                    items: [.init(value: AttributedString("64%"))],
                    proposedViewSize: .large)
        }
        .tag(1)
    }
    .tabViewStyle(.page)
    .frame(height: 100)
} else {
    // Regular — all 4 in one row
    KPIHeader {
        KPIItem(kpiCaption: AttributedString("Revenue"),
                items: [.init(value: AttributedString("$1.4M"))],
                proposedViewSize: .large)
        KPIItem(kpiCaption: AttributedString("Orders"),
                items: [.init(value: AttributedString("342"))],
                proposedViewSize: .large)
        KPIItem(kpiCaption: AttributedString("Open"),
                items: [.init(value: AttributedString("18"))],
                proposedViewSize: .large)
        KPIItem(kpiCaption: AttributedString("Win Rate"),
                items: [.init(value: AttributedString("64%"))],
                proposedViewSize: .large)
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Size class | Compact | Max 3 KPIs per page; use `TabView(.page)` for more |
| Size class | Regular | Max 4 KPIs in one `KPIHeader` row |
| KPI progress | Yes | `KPIProgressItem` — always placed first |
| KPI progress | No | `KPIItem` only |
| Pages | 1 | Single `KPIHeader` |
| Pages | 2+ | `TabView` with `.page` style + page indicator |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Limit to 3 KPIs per page on compact, 4 total on regular
- Use page controls (`.tabViewStyle(.page)`) when compact needs more than 3 KPIs
- Always place the KPI progress view first when including it on regular width
- Place overflow KPIs in the content area on regular width rather than adding a 5th to the header

**Don't:**
- Crowd more than 3 KPIs into a single compact-width page
- Use the small KPI progress view variant in the KPI header — only the large variant is supported
- Place the KPI progress view after other KPIs on regular width

---

## Related Components

- [kpi-item.md](kpi-item.md) — individual KPI display options
- [object-header.md](object-header.md) — alternative header with KPI data
- [chart-header.md](chart-header.md) — header with chart visualization
