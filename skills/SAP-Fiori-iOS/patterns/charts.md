# Charts — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK (FioriCharts)
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit` (Charts page)
> Development reference: `FioriCharts` — `ChartView`

## What is it?

`FioriCharts` is the charting module for SAP Fiori iOS. All chart types are rendered through a single `ChartView(model:)` entry point — the `ChartModel` drives the chart type, data series, colors, and configuration.

Charts are used in different contexts with different levels of interactivity:

| Context | Interactivity | Component |
|---------|--------------|-----------|
| **Floorplan** | Fully interactive — select data points, tap legend, zoom/pan | `ChartView` (full-screen) |
| **Card / Header** | Thumbnail — tap navigates to full interactive chart | `ChartView` inside `Card` or `HeaderChart` |
| **Table Cell** | Full-width view — read-only; navigation to chart supported | `FUIChartFloorplanTableViewCell` / custom |

---

## Anatomy (Floorplan)

A full chart floorplan has four elements. Size and visibility vary by context.

```
A. Chart Title      "Total Sales ($) by Month"
B. Subtitle         "2025–2026"
C. Timestamp        "Updated: Jan 2026"

D. Chart Summary
   Summary Name     "YTD ($)"     ← updates on drill down
   Series           Series A: 1.4M  ↑ +12%    (two or more series)
                    Series B: 1.2M  ↓ -3%
   Average Value    (default) → Selected value (on selection)
   Trend icons      ↑ ↓ in semantic colors

E. Chart Plot       [bars / lines / chart items]
   Y-Axis Title
   X-Axis Title
   Gridlines (min 2 for column/line; 2 for bar)

F. Legend           (multi-series only; omitted for single series)
```

### Chart Title rules
- Should reflect quantitative (measure) + categorical (dimension) criteria: e.g. "Total Sales ($) by Month"
- **Must update** when the user changes filter options or drills in/out
- Subtitle shows current series (e.g. "2025–2026")
- Timestamp is optional

### Chart Summary rules
- Max **4 data series** displayed at one time; filter menu to select which series to show if more exist
- Summary Name: concise + unit (e.g. "$", "°C"); **updates on drill down** to reflect current data level
- Single series → series label not shown; two or more → shown in descending order (most recent first)
- Trend icons (↑↓): use semantic colors; same decimal precision as summary values
- Drill-down label: tint color when drill-down is available; normal color when not

### Chart Plot rules
- Column/line: minimum **2 y-axis gridlines** (baseline + line above max); add negative baseline gridline if data goes below zero
- Horizontal bar: **2 x-axis gridlines** (baseline + single gridline)

### Legend
- **Single series** → no legend
- **Multi-series** → legend at bottom of chart plot

### Color Palette
Use `Color.preferredColor(.chart1)` through `.chart12` for series colors — they are accessible in both light and dark modes. Area, stock, scatter, and bubble charts use transparency variants (see Chart Types).

---

## Selection and Filter (Floorplan only)

- **Select**: tap a chart item directly, or tap-and-drag to the item
- On selection: data values appear in the chart summary
- **Filter**: allows changing dimensions and adjusting sort order
- **Drill down**: supported in chart summary section — measure (quantitative variable) should remain consistent during drill down when possible

## Available Chart Types

| Type | `.chartType` value | Use for |
|------|--------------------|---------|
| Line | `.line` | Trends over time |
| Area | `.area` | Volume trends |
| Column | `.column` | Categorical comparison |
| Stacked Column | `.stackedColumn` | Part-to-whole by category |
| Bar | `.bar` | Horizontal categorical comparison |
| Waterfall | `.waterfall` | Contribution to total |
| Combo | `.combo` | Mixed bar + line |
| Bubble | `.bubble` | 3-variable relationships |
| Scatter | `.scatter` | Correlation / distribution |
| Donut | `.donut` | Part-to-whole composition |
| Bullet | `.bullet` | Actual vs. target |
| Harvey Ball | `.harveyBall` | Compact completion % |
| Radial | `.radial` | Single metric completion |
| Stocks | `.stocks` | OHLC / candlestick |

---

## SwiftUI Code Examples

### Line chart
```swift
import FioriCharts

let model = ChartModel(
    chartType: .line,
    data: [[10, 24, 18, 35, 29, 42]],
    titlesForCategory: [["Jan", "Feb", "Mar", "Apr", "May", "Jun"]],
    titlesForAxis: [ChartAxisTitle(title: "Revenue ($K)")],
    colorsForCategory: [0: [0: Color.preferredColor(.chart1)]]
)

ChartView(model)
    .frame(height: 220)
```

### Column chart with multiple series
```swift
let model = ChartModel(
    chartType: .column,
    data: [
        [12, 24, 18, 30],   // Series 1: Actual
        [15, 20, 22, 28]    // Series 2: Budget
    ],
    titlesForCategory: [["Q1", "Q2", "Q3", "Q4"]],
    seriesAttributes: [
        ChartSeriesAttributes(colors: [Color.preferredColor(.chart1)], lineWidth: 0),
        ChartSeriesAttributes(colors: [Color.preferredColor(.chart2)], lineWidth: 0)
    ]
)

ChartView(model)
    .frame(height: 240)
```

### Donut chart
```swift
let model = ChartModel(
    chartType: .donut,
    data: [[35, 25, 20, 12, 8]],
    titlesForCategory: [["Cloud", "License", "Support", "Consulting", "Other"]],
    colorsForCategory: [0: [
        0: Color.preferredColor(.chart1),
        1: Color.preferredColor(.chart2),
        2: Color.preferredColor(.chart3),
        3: Color.preferredColor(.chart4),
        4: Color.preferredColor(.chart5)
    ]]
)

ChartView(model)
    .frame(height: 200)
```

### KPI + sparkline combination
```swift
VStack(alignment: .leading, spacing: 8) {
    Text("$1.4M")
        .font(.fiori(forTextStyle: .largeKPI, weight: .light))

    ChartView(ChartModel(
        chartType: .line,
        data: [[8, 12, 10, 16, 14, 18, 22]],
        indexesOfUserInteractionEnabledSeries: [],
        chartType: .line
    ))
    .frame(height: 40)
    .allowsHitTesting(false)  // read-only sparkline
}
```

---

## Color Rules

Always use chart color tokens — never hardcode series colors:

```swift
// ✅ Correct
Color.preferredColor(.chart1)   // first series
Color.preferredColor(.chart2)   // second series
// ... up to .chart12

Color.preferredColor(.chartGood)      // positive/target met
Color.preferredColor(.chartNeutral)   // neutral
Color.preferredColor(.chartCritical)  // below threshold

// Stock charts
Color.preferredColor(.stockUpStroke)   // price increase
Color.preferredColor(.stockDownStroke) // price decrease
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use `Color.preferredColor(.chart1)` through `.chart12` for series — in that order
- Keep line charts to 4 or fewer series — more becomes unreadable
- Include axis labels and a legend for charts with multiple series
- Use donut/radial for single-metric composition; use column/bar for comparison

**Don't:**
- Hardcode chart series colors
- Use more than 6 series on a single chart
- Use 3D chart effects — Fiori uses flat charts only
- Mix chart types in the same `ChartView` (use `.combo` explicitly)

---

## Related Components

- [kpi-item.md](kpi-item.md) — numeric KPI display
- [cards.md](cards.md) — chart inside a card
