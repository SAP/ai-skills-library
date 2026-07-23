# Chart Content Table View Cell — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIChartFloorplanTableViewCell`

## What is it?

The chart content table view cell is a full-width view that displays a visual representation of one or more datasets within a table view. It is used when the user needs to view chart data in context of a business object workflow, without needing to drill into individual chart values. Navigation to full chart details is supported.

---

## When to Use

- Displaying chart data inline within a business object detail page
- When the user needs a visual overview but doesn't need to interact with individual data points
- When chart data is contextually relevant to the surrounding object information

---

## Anatomy

```
A. Chart Title (+ optional timestamp)
B. Chart Summary (high-level data highlight)
C. Chart Plot
   ┌─────────────────────────────────┐
   │  Chart items (bars/lines/etc.)  │
   │  X-axis / Y-axis + labels       │
   │  Gridlines                      │
   │  Legend (multi-series only)     │
   └─────────────────────────────────┘
```

**A. Chart Title** — name of the chart and series displayed; optional timestamp.

**B. Chart Summary** — high-level details from the chart data (e.g. total sales in dollars for the year).

**C. Chart Plot** — full visual representation including chart items, axes with titles, axis labels, and gridlines.
- **Multi-series charts** — legend included at the bottom of the chart plot
- **Single-series charts** — legend not displayed

---

## SwiftUI Code Examples

### Chart content table view cell
```swift
import FioriSwiftUICore
import FioriCharts

struct RevenueChartCell: View {
    let chartModel: ChartModel

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            // A. Chart title + timestamp
            VStack(alignment: .leading, spacing: 2) {
                Text("Revenue by Quarter")
                    .font(.fiori(forTextStyle: .headline))
                    .foregroundStyle(Color.preferredColor(.primaryLabel))
                Text("Updated: Jan 2026")
                    .font(.fiori(forTextStyle: .footnote))
                    .foregroundStyle(Color.preferredColor(.tertiaryLabel))
            }

            // B. Chart summary
            Text("Total: $5.6M YTD")
                .font(.fiori(forTextStyle: .subheadline))
                .foregroundStyle(Color.preferredColor(.secondaryLabel))

            // C. Chart plot
            ChartView(chartModel)
                .frame(height: 220)
                .allowsHitTesting(false)  // read-only in cell context; enable for navigation
        }
        .padding(16)
    }
}

// Single series — no legend
let singleSeriesModel = ChartModel(
    chartType: .bar,
    data: [[12, 18, 15, 22]],
    titlesForCategory: [["Q1", "Q2", "Q3", "Q4"]],
    titlesForAxis: [ChartAxisTitle(title: "Revenue ($M)")],
    colorsForCategory: [0: [0: Color.preferredColor(.chart1)]]
)

// Multi-series — legend shown automatically
let multiSeriesModel = ChartModel(
    chartType: .bar,
    data: [
        [12, 18, 15, 22],  // Actual
        [14, 16, 18, 20]   // Budget
    ],
    titlesForCategory: [["Q1", "Q2", "Q3", "Q4"]],
    seriesAttributes: [
        ChartSeriesAttributes(colors: [Color.preferredColor(.chart1)]),
        ChartSeriesAttributes(colors: [Color.preferredColor(.chart2)])
    ]
    // Legend rendered automatically for multi-series
)
```

### Inside an object detail page
```swift
NavigationStack {
    List {
        // Business object header
        ObjectHeader {
            Text("Sales Order #5678")
        } subtitle: {
            Text("Acme Corporation")
        }

        // Chart content table view cell inline
        Section {
            RevenueChartCell(chartModel: revenueModel)
                .listRowInsets(EdgeInsets())  // full-width
        }

        // Other object detail rows
        Section("Details") {
            KeyValueItem(key: { Text("Total") }, value: { Text("$5.6M") })
            KeyValueItem(key: { Text("Period") }, value: { Text("Jan–Dec 2026") })
        }
    }
    .navigationTitle("Sales Order #5678")
    .navigationBarTitleDisplayMode(.inline)
}
```

### With navigation to full chart
```swift
struct ChartTableViewCell: View {
    let model: ChartModel
    let onTap: () -> Void

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text("Revenue by Quarter")
                .font(.fiori(forTextStyle: .headline))
            Text("Total: $5.6M YTD")
                .font(.fiori(forTextStyle: .subheadline))
                .foregroundStyle(Color.preferredColor(.secondaryLabel))
            ChartView(model)
                .frame(height: 200)
                .allowsHitTesting(true)  // navigation enabled
        }
        .padding(16)
        .onTapGesture { onTap() }  // navigates to full chart floorplan
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Chart type | Bar | `chartType: .bar` |
| Chart type | Column | `chartType: .column` |
| Chart type | Line | `chartType: .line` |
| Series | Single | No legend (`ChartView` omits legend automatically) |
| Series | Multi | Legend at bottom of chart plot (automatic) |
| Navigation | Enabled | `.allowsHitTesting(true)` + `.onTapGesture` |
| Navigation | Disabled | `.allowsHitTesting(false)` |
| Timestamp | Yes | Secondary text below chart title |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Show the legend only for multi-series charts
- Use full width — apply `.listRowInsets(EdgeInsets())` when inside a `List`
- Enable navigation (`allowsHitTesting: true`) when the user needs access to full chart details
- Keep the chart summary concise — one key metric or total

**Don't:**
- Use for interactive data exploration — that belongs in the full chart floorplan
- Show a legend for single-series charts

---

## Related Components

- [charts.md](charts.md) — full chart types and `ChartView` API
- [chart-header.md](chart-header.md) — simplified chart in an object header
- [object-cell.md](object-cell.md) — table view cell context
