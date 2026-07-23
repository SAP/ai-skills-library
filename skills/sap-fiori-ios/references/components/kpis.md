# KPIs — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit` (KPI page)
> Development reference: UIKit `FUIKPIView`, SwiftUI `KPIItem`

## What is it?

Key performance indicators (KPIs) display measurable values to evaluate success or summarize an object. They can be used in headers, content areas, object cells, and modal windows.

---

## Placement Rules

| Location | Layout | Tappable |
|----------|--------|---------|
| Header / content area | Horizontal with fixed padding, center-aligned | Yes (optional) |
| Modal window | Vertically stacked, max 2 per row | No |
| Object cell / card | Inline | No |

---

## Anatomy

```
        [B. Unit]  A. KPI Value  [B. Unit]
                   C. KPI Label
              D. [████████░░] Progress
```

**A. KPI (metric)** — most prominent element, always above the label. **Mandatory.** May show a single value or a range (e.g. "1 of 2").

**B. KPI Unit Label** (optional) — clarifies the metric (e.g. $, h, M). Placed left or right of the metric. Maximum **2 unit labels**.

**C. KPI Label** — mandatory. Communicates what the KPI represents. Keep concise. For the progress view, can appear inside the indicator or below it.

**D. Progress View** (optional) — visual representation of completeness, 0–100%.

---

## Interaction

- **Header / content area KPIs** — can be read-only or tappable. When tappable, the KPI value appears in **tint color**. Tap navigates to a modal or a filtered list.
- **Cell KPIs** — never tappable.

---

## Adaptive Design

- Supported in compact and regular widths
- KPIs have defined minimum and maximum widths
- **Compact header**: 1–2 KPIs; overflow → multiple pages with page control
- **Regular header**: 4–5 KPIs depending on their width (see [kpi-header.md](kpi-header.md))

---

## Variations

### Standard KPI
Most common type — shows quantity, percentage, or value. Optional unit label (max 2).

```swift
import FioriSwiftUICore

// Basic KPI
KPIItem {
    Text("$1.4M")
        .font(.fiori(forTextStyle: .largeKPI, weight: .light))
        .foregroundStyle(Color.preferredColor(.primaryLabel))
} subtitle: {
    Text("Revenue")
        .font(.fiori(forTextStyle: .subheadline))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
}

// With unit label (left of metric)
KPIItem(
    kpiCaption: AttributedString("Orders"),
    items: [
        KPISubItem(
            value: AttributedString("342"),
            unit: AttributedString("K")  // right of metric
        )
    ],
    proposedViewSize: .large
)

// With two unit labels
KPIItem(
    kpiCaption: AttributedString("Revenue"),
    items: [
        KPISubItem(
            value: AttributedString("1.4"),
            unit: AttributedString("M"),   // right unit
            unitLeading: AttributedString("$")  // left unit
        )
    ],
    proposedViewSize: .large
)
```

### Time KPI
Shows a breakdown of time. Always include a unit label (h for hours, m for minutes).

```swift
KPIItem {
    HStack(alignment: .lastTextBaseline, spacing: 2) {
        Text("4")
            .font(.fiori(forTextStyle: .largeKPI, weight: .light))
        Text("h")
            .font(.fiori(forTextStyle: .title2))
            .foregroundStyle(Color.preferredColor(.secondaryLabel))
        Text("30")
            .font(.fiori(forTextStyle: .largeKPI, weight: .light))
        Text("m")
            .font(.fiori(forTextStyle: .title2))
            .foregroundStyle(Color.preferredColor(.secondaryLabel))
    }
    .foregroundStyle(Color.preferredColor(.primaryLabel))
} subtitle: {
    Text("Duration")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
}
```

### KPI with Icon
Icon sits to the **left** of the numeric value. Maximum **1 unit label** when using an icon.

```swift
KPIItem {
    HStack(alignment: .lastTextBaseline, spacing: 6) {
        Image(systemName: "cart")
            .font(.fiori(forTextStyle: .title2))
            .foregroundStyle(Color.preferredColor(.tintColor))
        Text("342")
            .font(.fiori(forTextStyle: .largeKPI, weight: .light))
    }
    .foregroundStyle(Color.preferredColor(.primaryLabel))
} subtitle: {
    Text("Orders")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
}
```

### KPI Progress View (small + large)
Shows completeness visually (0–100%). Two sizes:
- **Small** — cards, content areas
- **Large** — headers, prominent content areas (see [kpi-header.md](kpi-header.md) for header rules)

Label can appear **inside** the progress indicator or **below** it (wraps to 2 lines if needed).

```swift
// Large — percentage label inside indicator
KPIProgressItem {
    Text("72%")
        .font(.fiori(forTextStyle: .KPI, weight: .light))
} subtitle: {
    Text("Quota Attainment")
} footnote: {
    Text("$1.4M / $1.95M")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
} progress: {
    ProgressView(value: 0.72)
        .tint(Color.preferredColor(.tintColor))
}

// Small — label below, for cards
KPIProgressItem {
    Text("64%")
        .font(.fiori(forTextStyle: .headline, weight: .light))
} subtitle: {
    Text("On-time Delivery")
} progress: {
    ProgressView(value: 0.64)
        .tint(Color.preferredColor(.positiveLabel))
}
.proposedViewSize: .small
```

---

## Tappable KPI (navigates to modal or filtered list)
```swift
// Tappable — value in tint color
VStack(spacing: 4) {
    Text("$1.4M")
        .font(.fiori(forTextStyle: .largeKPI, weight: .light))
        .foregroundStyle(Color.preferredColor(.tintColor))  // tint = tappable
    Text("Revenue")
        .font(.fiori(forTextStyle: .subheadline))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
}
.onTapGesture { showRevenueDetail() }
.accessibilityLabel("Revenue: $1.4M — tap to view details")
```

---

## KPIs in a Header (horizontal, center-aligned)
```swift
// Center-aligned horizontal strip
HStack(spacing: 24) {
    KPIItem(kpiCaption: AttributedString("Revenue"),
            items: [.init(value: AttributedString("$1.4M"))],
            proposedViewSize: .large)
    KPIItem(kpiCaption: AttributedString("Orders"),
            items: [.init(value: AttributedString("342"))],
            proposedViewSize: .large)
    KPIItem(kpiCaption: AttributedString("Win Rate"),
            items: [.init(value: AttributedString("64%"))],
            proposedViewSize: .large)
}
.frame(maxWidth: .infinity)  // center-aligned
```

## KPIs in a Modal (vertically stacked, max 2 per row, not tappable)
```swift
LazyVGrid(columns: [GridItem(.flexible()), GridItem(.flexible())], spacing: 16) {
    ForEach(kpis) { kpi in
        KPIItem(
            kpiCaption: AttributedString(kpi.label),
            items: [.init(value: AttributedString(kpi.value))],
            proposedViewSize: .large
        )
        // Not tappable in modal context
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Type | Standard | `KPIItem` with value + subtitle |
| Type | Time | `HStack` with value + unit labels |
| Type | With icon | `HStack` with icon left of value |
| Type | Progress (large) | `KPIProgressItem` (large) |
| Type | Progress (small) | `KPIProgressItem` (small / `.proposedViewSize: .small`) |
| Unit label | Left | `unitLeading: AttributedString(...)` |
| Unit label | Right | `unit: AttributedString(...)` |
| Tappable | Yes | Value in `.tintColor` + `.onTapGesture` |
| Tappable | No | Value in `.primaryLabel` — no gesture |
| Progress label | Inside | Label inside `progress` builder |
| Progress label | Below | Label in `subtitle` builder |
| Placement | Header | Horizontal `HStack`, center-aligned |
| Placement | Modal | `LazyVGrid` 2-column, not tappable |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Always include both a numeric value (A) and a label (C) — both are mandatory
- Show the value in tint color when the KPI is tappable
- Use unit labels to clarify ambiguous metrics ($ for currency, h for hours)
- Use the large progress view in headers, small in cards
- Center-align KPIs in header and content area arrangements

**Don't:**
- Make cell/modal KPIs tappable
- Use more than 2 unit labels on a single KPI
- Use more than 1 unit label when the KPI has an icon
- Use long, descriptive KPI labels — keep them concise

---

## Related Components

- [kpi-header.md](kpi-header.md) — KPI strip at the top of a screen
- [object-header.md](object-header.md) — KPI in right accessory of object header
- [cards.md](cards.md) — KPI in card body
