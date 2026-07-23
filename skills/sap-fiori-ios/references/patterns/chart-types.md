# Chart Types — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK (FioriCharts)
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit` (Charts page)
> Development reference: UIKit `FUIChartFloorplanView`, SwiftUI `ChartView`

## What is it?

SAP Fiori for iOS supports multiple chart types. Select the chart that best fits the data type and how users will interact with it. All types are rendered via `ChartView(model:)` with the appropriate `chartType` on `ChartModel`.

For chart anatomy, contexts (floorplan / card / table cell), and interaction rules, see [charts.md](charts.md).

---

## Chart Types

### Horizontal Bar Chart (`.bar`)
Horizontal bars aligned to the y-axis. Good for **discrete quantities with long labels** — the y-axis has more space to expand.

**Do:** Use for discrete item measurements; use when item labels are long.
**Don't:** Use for time-based data — time flows left-to-right on x-axis, which conflicts.

```swift
ChartModel(chartType: .bar, data: [[...]], titlesForCategory: [[...]])
```

---

### Column Chart (`.column`)
Vertical bars. Side-by-side columns reinforce distinctness of items. **Y-axis baseline always starts at 0**; positive values above, negative below.

**Do:** Compare non-time-series values; use instead of line chart when individual values matter more than overall trend, or when dataset has missing values (gaps would appear in a line).
**Don't:** Use with very large datasets (columns become too narrow); use when x-axis labels get truncated — use horizontal bar instead (non-time-series only).

```swift
ChartModel(chartType: .column, data: [[...]], titlesForCategory: [[...]])
```

---

### Stacked Column Chart (`.stackedColumn`)
Extension of column chart. Shows the total of a group and the categories within it. Best when comparing totals and one part of the total.

**Two selection modes:**
- **Single selection** — select whole column to view total + each category's total
- **Series selection** — select one category/series across all columns for comparison

**Do:** Use to compare groups that are parts of a whole; show how a larger category divides into smaller ones.
**Don't:** Use with large datasets (categories too small to see patterns); use when data can have negative values (no negative space in stacked columns).

```swift
ChartModel(chartType: .stackedColumn, data: [[series1...], [series2...], [series3...]])
```

---

### Line Chart (`.line`)
Straight lines connecting plotted points. Shows **change in values over time** (continuous or discrete).

**Do:** Display trends — line connections show overall data shape.
**Don't:** Use when x-axis values are unrelated (line implies trend that doesn't exist); use when dataset has many missing values (use column instead to avoid breaks).

```swift
ChartModel(chartType: .line, data: [[...]], titlesForCategory: [[...]])
```

---

### Area Chart (`.area`)
Like a line chart but with color fill between lines and axis. **Emphasizes volume** and quantitative progression over time.

**Do:** Highlight quantitative progression over time.
**Don't:** Use when x and y data are unrelated; use when dataset has missing values (causes breaks — use column instead).

```swift
ChartModel(chartType: .area, data: [[...]])
// Note: area/stock/scatter/bubble charts use transparency variants of chart colors
```

---

### Combination Chart (`.combo`)
Combines column and line charts. Compares discrete values over time against a measurement (mean, target, expected value).

**Do:** Directly compare two series using the same measure (y-axis); dataset should be time series or ranked items.
**Don't:** Use when x-axis values are unrelated (line implies non-existent trend).

```swift
ChartModel(
    chartType: .combo,
    data: [[columnSeries...], [lineSeries...]],
    seriesAttributes: [
        ChartSeriesAttributes(chartType: .column, colors: [Color.preferredColor(.chart1)]),
        ChartSeriesAttributes(chartType: .line,   colors: [Color.preferredColor(.chart2)])
    ]
)
```

---

### Waterfall Chart (`.waterfall`)
Columns visualize the **cumulative effect of increases and decreases**. Column height and color determined by values. Legend always shows colors for increase, decrease, and total.

**Do:** Display sequential data; use contrasting colors to highlight value differences.
**Don't:** Use to compare data sets.

```swift
ChartModel(
    chartType: .waterfall,
    data: [[...]], // positive = increase, negative = decrease
    colorsForCategory: [
        0: [0: Color.preferredColor(.positiveLabel),   // increase
            1: Color.preferredColor(.negativeLabel),   // decrease
            2: Color.preferredColor(.chart1)]           // total
    ]
)
```

---

### Scatter Chart (`.scatter`)
Dots in 2D space showing **correlation between two variables** (x and y). Additional colors add a third dimension/series. Slide finger along a vertical/horizontal guide to move between points.

**Do:** Show correlation between two related variables.
**Don't:** Use when variables have no direct relationship.

```swift
ChartModel(chartType: .scatter, data: [[...]])
// Transparency color variants used
```

---

### Bubble Chart (`.bubble`)
Like scatter but adds a **third dimension via circle size**. Additional colors add a fourth dimension.

**Do:** Show correlation with size as a variable; scale bubble size by **area** (not diameter).
**Don't:** Use odd shapes; avoid too many sizes (looks chaotic).

```swift
ChartModel(chartType: .bubble, data: [[...]])
// Scale by area: radius = sqrt(value / π)
```

---

### Stock Chart (`.stocks`)
Line-based trend chart for financial data. Interactive — tap and slide on trend line. Shows:
- **Ticker name** — company identifier
- **Spot price** — current trading price
- **OHLC** — Open, High, Low, Close
- **Volume** — shares traded

```swift
ChartModel(chartType: .stocks, data: [[...]])
// Semantic colors: .stockUpStroke, .stockDownStroke
```

---

### Donut Chart (`.donut`)
**Part-to-whole** analysis. Circle divided into radial segments by category. Segments are interactive — tap one or multiple to see percentage and metric value.

**Do:** Use a unique color per segment; sort largest→smallest clockwise (unless labels have inherent order like Strongly Agree→Disagree).
**Don't:** Use more than **5 segments** (becomes difficult to read).

```swift
ChartModel(
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
```

---

## Quick Reference: When to Use Which Chart

| Need | Chart type |
|------|-----------|
| Trend over time | Line, Area |
| Compare discrete values | Column, Horizontal Bar |
| Long item labels | Horizontal Bar |
| Part of a whole | Donut, Stacked Column |
| Cumulative effect | Waterfall |
| Two-variable correlation | Scatter |
| Three-variable correlation | Bubble |
| Financial price history | Stock |
| Value + trend side by side | Combo |

---

## Color Rules

- Series colors: `Color.preferredColor(.chart1)` through `.chart12` — in that order
- Area, stock, scatter, bubble: use **transparency variants** of chart colors
- Semantic: `.chartGood`, `.chartNeutral`, `.chartCritical`, `.chartBad`
- Stock: `.stockUpStroke` (up), `.stockDownStroke` (down)
- Waterfall: `.positiveLabel` (increase), `.negativeLabel` (decrease)

---

## Related Components

- [charts.md](charts.md) — chart anatomy, contexts, and `ChartView` API
- [chart-header.md](chart-header.md) — simplified chart in object header (line/column only)
- [chart-content-table-view-cell.md](chart-content-table-view-cell.md) — full-width chart in a table cell
