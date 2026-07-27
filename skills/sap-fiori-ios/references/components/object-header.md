# Object Header — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Headers
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIObjectHeader`, SwiftUI `ObjectHeader`

## What is it?

The object header provides a quick view of the most important or most frequently used information about one instance of an object. It connects visually to the navigation bar via a seamless background and is visually separated from the content area below. Information should be clear and concise — a high-level summary, not a data dump.

---

## When to Use

**Do:**
- Use to provide a summary of an object detail screen

**Don't:**
- Overload with too much information — keep it to the most important details

---

## Anatomy

Only the **title** is required. All other elements are optional.

```
┌────────────────────────────────────────────────┐
│ [A. Thumbnail]  B. Title                       │
│                 B. Subtitle          D. Right  │
│                 C. Tags              Accessory │
│                                                │
│ E. Label items (location / date / time)        │
│ F. Description (optional)                      │
│                                                │
│ ← swipe →  G. Page control (if chart present) │
│ H. Header Chart (on second page)               │
└────────────────────────────────────────────────┘
```

### A. Thumbnail
Product image, avatar, logo, or icon. Helps the user visually identify the object.

### B. Main Content
Title (required) and subtitle.

### C. Tags
Complementary information displayed as tags — visually distinct from plain text, functioning as independent bits of information.

### D. Right Accessory
Object status or an important KPI.

### E. Label Items
Important quick-read details such as location, date, and time. Each label item can be text only or combined with an image.

### F. Description
Additional details — only use when it provides genuinely valuable information.

### G. Page Control
Appears when a header chart is placed on a second page. User swipes to navigate between the main header and the chart page.

### H. Header Chart
A chart (line or column) for quickly understanding relevant trend or status information. For full chart header guidance, see [chart-header.md](chart-header.md).

---

## Layout

### Compact
All elements stack vertically. Thumbnail, title, subtitle, tags, right accessory, label items, description, and chart page all available.

### Regular (iPad)
More horizontal space allows label items and the right accessory to spread out. Thumbnail and content are arranged with more breathing room.

---

## SwiftUI Code Examples

### Minimal (title only)
```swift
import FioriSwiftUICore

ObjectHeader {
    Text("Invoice #1234")
        .font(.fiori(forTextStyle: .title1))
}
```

### Standard object header
```swift
ObjectHeader {
    Text("Sales Order #5678")
        .font(.fiori(forTextStyle: .title1))
} subtitle: {
    Text("Acme Corporation")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
} tags: {
    Tag("Open")
    Tag("High Priority")
} detailImage: {
    Image(systemName: "cart.fill")
        .font(.fiori(forTextStyle: .largeTitle))
        .foregroundStyle(Color.preferredColor(.tintColor))
} detailContent: {
    VStack(alignment: .trailing, spacing: 2) {
        Text("$14,500")
            .font(.fiori(forTextStyle: .KPI, weight: .light))
            .foregroundStyle(Color.preferredColor(.primaryLabel))
        Text("Total")
            .font(.fiori(forTextStyle: .footnote))
            .foregroundStyle(Color.preferredColor(.secondaryLabel))
    }
}
```

### With thumbnail (product image / avatar)
```swift
ObjectHeader {
    Text("Product XR-400")
} subtitle: {
    Text("Electronics · In stock")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
} detailImage: {
    AsyncImage(url: product.imageURL) { image in
        image.resizable()
            .aspectRatio(contentMode: .fill)
            .clipShape(RoundedRectangle(cornerRadius: 8))
    } placeholder: {
        RoundedRectangle(cornerRadius: 8)
            .fill(Color.preferredColor(.secondaryBackground))
    }
    .frame(width: 60, height: 60)
}
```

### With label items (location, date)
```swift
ObjectHeader {
    Text("Service Ticket #99")
} subtitle: {
    Text("Plumbing · Building A")
} tags: {
    Tag("Urgent")
} bodyText: {
    VStack(alignment: .leading, spacing: 4) {
        // Label items: text + optional icon
        HStack(spacing: 6) {
            Image(systemName: "location")
                .foregroundStyle(Color.preferredColor(.secondaryLabel))
            Text("Floor 3, Room 301")
                .font(.fiori(forTextStyle: .footnote))
                .foregroundStyle(Color.preferredColor(.secondaryLabel))
        }
        HStack(spacing: 6) {
            Image(systemName: "calendar")
                .foregroundStyle(Color.preferredColor(.secondaryLabel))
            Text("Due: 25 Jul 2026")
                .font(.fiori(forTextStyle: .footnote))
                .foregroundStyle(Color.preferredColor(.secondaryLabel))
        }
    }
}
```

### With description
```swift
ObjectHeader {
    Text("Project Alpha")
} subtitle: {
    Text("SAP Internal · R&D")
} description: {
    // Only when it adds genuine value
    Text("Cross-functional initiative to modernize the invoicing workflow across EMEA region.")
        .font(.fiori(forTextStyle: .body))
        .foregroundStyle(Color.preferredColor(.primaryLabel))
}
```

### With header chart (two-page header)
```swift
ObjectHeader {
    Text("Revenue Dashboard")
} subtitle: {
    Text("YTD 2026")
} headerChart: {
    HeaderChart {
        Text("Revenue")
            .foregroundStyle(Color.preferredColor(.tintColor))  // tint = interactive
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
            titlesForCategory: [["Jan", nil, nil, nil, nil, "Jun"]],
            colorsForCategory: [0: [0: Color.preferredColor(.chart1)]]
        ))
    }
    .onTapGesture { navigateToFullChart() }
}
// Page control appears automatically when headerChart is present
```

### Inside a detail screen (standard pattern)
```swift
NavigationStack {
    ScrollView {
        VStack(spacing: 0) {
            ObjectHeader {
                Text(invoice.number)
            } subtitle: {
                Text(invoice.vendor)
            } tags: {
                Tag(invoice.status)
            } detailContent: {
                Text(invoice.formattedAmount)
                    .font(.fiori(forTextStyle: .KPI, weight: .light))
                    .foregroundStyle(Color.preferredColor(.primaryLabel))
            }

            Divider()
            InvoiceDetailBody(invoice: invoice)
        }
    }
    .navigationTitle(invoice.number)
    .navigationBarTitleDisplayMode(.inline)
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Thumbnail | Image | `detailImage: { AsyncImage(...).clipShape(RoundedRectangle) }` |
| Thumbnail | Avatar | `detailImage: { Circle()... }` |
| Thumbnail | Icon | `detailImage: { Image(systemName:) }` |
| Thumbnail | None | Omit `detailImage` |
| Tags | Yes | `tags: { Tag("...") Tag("...") }` |
| Right accessory | Status text | `detailContent: { Text(...).foregroundStyle(.secondaryLabel) }` |
| Right accessory | KPI | `detailContent: { Text(...).font(.fiori(forTextStyle: .KPI)) }` |
| Label items | Text only | `Text` in `bodyText` |
| Label items | Text + icon | `HStack { Image + Text }` in `bodyText` |
| Description | Yes | `description: { Text(...) }` |
| Header chart | Yes | `headerChart: { HeaderChart {...} }` + page control auto |
| Header chart | None | Omit `headerChart` |
| Size class | Compact | Stacked vertical layout (default) |
| Size class | Regular | Wider layout — same API, system adapts |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Keep content clear and concise — high-level summary only
- Use the title as the object's primary identifier (number, name, ID)
- Use tags for categorical labels, not status — express status in the right accessory
- Only include a description when it provides genuinely valuable additional context
- Use tint color for the chart title when the header chart is interactive
- Let the page control appear automatically — don't suppress it when a header chart is present

**Don't:**
- Overload with too many elements — every slot doesn't need to be filled
- Duplicate information already visible in the navigation bar title
- Use the header chart for multi-series or complex data — keep it to a single trend
- Place interactive actions in the object header — use the toolbar instead

---

## Related Components

- [chart-header.md](chart-header.md) — header chart component (H slot)
- [kpi-header.md](kpi-header.md) — alternative KPI-focused header
- [object-cell.md](object-cell.md) — list row version of object display
