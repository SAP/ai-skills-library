# Chart Header — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Headers
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIObjectHeaderChartView`, SwiftUI `HeaderChart`

## What is it?

The chart header displays simple chart data inside an object header. It provides at-a-glance insight about the object it is associated with, supported in both compact and regular widths.

**The chart header can only be used inside the object header.**

---

## When to Use

**Do:**
- Use when simple data (e.g. a trend) is important to view at a glance
- Use to draw attention to one key aspect of the associated object
- Always place inside an object header

**Don't:**
- Use for complex or multi-series data sets — use a full chart in the content area instead
- Use if you are only including a title and subtitle (no analytical content) — omit the chart header entirely in that case

---

## Anatomy

At least one analytical component (trend, KPI, or chart plot) is required. All other elements are optional.

| Element | Required | Notes |
|---------|----------|-------|
| Chart title | Yes | |
| Subtitle / timestamp label | No | |
| Trend label + icon | No | One of: trend, KPI, or chart plot must be present |
| X-axis labels | No | Only **first and last** x-axis labels allowed |
| Y-axis lines | No | Max **3 lines**; **no y-axis labels** in this view |
| Chart data | No | Column or line charts **only** |

---

## Behavior & Interaction

### Non-interactive (read-only)
Chart is display-only. If the chart displays truncated text or data from a large dataset, provide a full chart in the content area below so users can see details.

### Interactive (tap to navigate)
When navigation is enabled, the chart title appears in **tint color**. The entire chart container is a single touch target — one tap navigates to the full-screen chart floorplan.

---

## SwiftUI Code Examples

### Basic non-interactive chart header
```swift
import FioriSwiftUICore
import FioriCharts

HeaderChart {
    Text("Revenue")
        .font(.fiori(forTextStyle: .subheadline))
        .foregroundStyle(Color.preferredColor(.primaryLabel))
} subtitle: {
    Text("Last 6 months")
        .font(.fiori(forTextStyle: .footnote))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
} trend: {
    HStack(spacing: 4) {
        Image(systemName: "arrow.up.right")
            .foregroundStyle(Color.preferredColor(.positiveLabel))
        Text("+12%")
            .foregroundStyle(Color.preferredColor(.positiveLabel))
    }
    .font(.fiori(forTextStyle: .footnote))
} chart: {
    ChartView(ChartModel(
        chartType: .line,
        data: [[2.1, 2.4, 1.9, 2.8, 2.6, 3.1]],
        titlesForCategory: [["Jan", nil, nil, nil, nil, "Jun"]],  // first + last only
        colorsForCategory: [0: [0: Color.preferredColor(.chart1)]]
    ))
    .allowsHitTesting(false)  // read-only
}
```

### Interactive chart header (tap navigates to full chart)
```swift
HeaderChart {
    // Title in tint color signals interactivity
    Text("Revenue")
        .font(.fiori(forTextStyle: .subheadline))
        .foregroundStyle(Color.preferredColor(.tintColor))
} subtitle: {
    Text("Last 6 months")
        .font(.fiori(forTextStyle: .footnote))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
} chart: {
    ChartView(ChartModel(
        chartType: .column,
        data: [[2.1, 2.4, 1.9, 2.8, 2.6, 3.1]],
        titlesForCategory: [["Jan", nil, nil, nil, nil, "Jun"]],
        colorsForCategory: [0: [0: Color.preferredColor(.chart1)]]
    ))
}
.onTapGesture {
    navigateToFullScreenChart()
}
// Single tap target — entire container
```

### Inside an ObjectHeader
```swift
ObjectHeader {
    Text("Sales Order #5678")
} subtitle: {
    Text("Acme Corporation")
} headerChart: {
    HeaderChart {
        Text("Revenue")
            .foregroundStyle(Color.preferredColor(.tintColor))
    } trend: {
        HStack(spacing: 4) {
            Image(systemName: "arrow.up.right")
                .foregroundStyle(Color.preferredColor(.positiveLabel))
            Text("+8%")
                .foregroundStyle(Color.preferredColor(.positiveLabel))
        }
        .font(.fiori(forTextStyle: .footnote))
    } chart: {
        ChartView(ChartModel(
            chartType: .line,
            data: [[1.2, 1.8, 1.5, 2.1, 1.9, 2.4]],
            titlesForCategory: [["Q1", nil, nil, nil, nil, "Q4"]],
            colorsForCategory: [0: [0: Color.preferredColor(.chart1)]]
        ))
    }
    .onTapGesture { navigateToFullChart() }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Chart type | Line | `chartType: .line` |
| Chart type | Column | `chartType: .column` |
| Interactive | Yes | Title in `.tintColor`, `.onTapGesture {}` on container |
| Interactive | No | Title in `.primaryLabel`, `.allowsHitTesting(false)` |
| Trend | Yes | `trend: { HStack with icon + text }` |
| X-axis labels | Yes | First + last in `titlesForCategory`, `nil` for middle |
| Y-axis lines | 1–3 | Configured on `ChartModel` — no labels |
| Placement | Object header | Always inside `ObjectHeader` `headerChart: {}` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Always place inside an object header — never standalone
- Include at least one analytical element: trend, KPI, or chart plot
- Use **tint color** for the chart title when navigation is enabled
- Show only first and last x-axis labels
- Limit y-axis to max 3 lines with no labels
- Provide a full chart in the content area if the header chart may truncate data

**Don't:**
- Use for multi-series or complex data — keep it to a single trend or simple series
- Use if there is no analytical content (title/subtitle only)
- Add y-axis labels in this view
- Use chart types other than column or line

---

## Related Components

- [object-header.md](object-header.md) — the only valid container for chart header
- [../patterns/charts.md](../patterns/charts.md) — full chart for the content area
