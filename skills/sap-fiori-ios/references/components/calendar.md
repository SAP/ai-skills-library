# Calendar — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUICalendarView`, SwiftUI `CalendarView`

## What is it?

The calendar view provides a visual overview of a week, a month, or multiple months. It can also display correlations between dates (availability, pricing, holidays) and support date range selection.

---

## When to Use

**Do:**
- Display a visual overview of a week, a month, multiple months, or a range of selected dates
- Visually present correlations between two dates — consecutive holidays, peak vs. off-season pricing, hotel availability
- Combine with object cells (agenda) or timeline (timesheet) in the space below the calendar

**Don't:**
- Use calendar view when a text-based or list-based picker can fulfill the primary requirement — use `DateTimePicker` or `DateRangePicker` instead

---

## Anatomy

The calendar is composed of four parts:

```
┌─────────────────────────────────────┐
│  D. Month Label (nav bar / title)   │
│─────────────────────────────────────│
│  B. Week Label Container            │
│  Su  Mo  Tu  We  Th  Fr  Sa        │
│─────────────────────────────────────│
│                                     │
│  C. Date Cell Container             │
│   1   2   3   4   5   6   7        │
│   8   9  10  11  12  13  14        │
│  ...                                │
│                                     │
└─────────────────────────────────────┘  ← A. Calendar View Container

[ Space for agenda / timeline below ]
```

### A. Calendar View Container
Outer container. The space below it is available for different configurations — e.g. `ObjectItem` rows as an agenda, or `TimelineItem` rows as a timesheet.

### B. Week Label Container
Row of day-of-week abbreviations. Start day is configurable (see Variations).

### C. Date Cell Container
Grid of date cells. Three display types available (see Variations).

### D. Month Label
Displayed as navigation bar title or large title. Uses three-letter title-case abbreviations: Jan, Feb, Mar…

---

## Variations

### Calendar View Types

| Type | Use for |
|------|---------|
| Month View *(default)* | Full month overview, event dots |
| Week View | Compact week strip, typically above a day agenda |
| Expandable View | Collapses to week strip, expands to month on tap |
| Date Selection View | Selecting a single date or date range |

```swift
import FioriSwiftUICore

// Month view (default)
CalendarMonthView(
    selection: $selectedDate,
    calendar: .current
)

// Week view
CalendarWeekView(
    selection: $selectedDate,
    calendar: .current
)

// Full calendar with expandable behavior
CalendarView(
    selection: $selectedDate,
    calendar: .current
)
```

### Week Label — Start Day

| Start Day | Standard |
|-----------|---------|
| Sunday *(default)* | US |
| Monday | Europe, Asia, Oceania |
| Saturday | Middle East |

```swift
var calendar = Calendar.current
calendar.firstWeekday = 2  // 1 = Sunday, 2 = Monday, 7 = Saturday

CalendarView(selection: $selectedDate, calendar: calendar)
```

### Date Cell Display Types

| Type | Contents | Notes |
|------|---------|-------|
| Number Only | Day number alone | Clean, no indicators |
| Number with Dot Indicator *(default)* | Day number + colored dot | Indicates events/data on a date |
| Number with Icon Indicator & Legend | Day number + icon | Icon legend requires custom configuration — not provided out of the box; app teams must configure using the chart legend component |

> **Important:** Two display types cannot be mixed in the same calendar instance. Configure the entire calendar with one type only.

### Month Label Types

| Type | Behavior |
|------|---------|
| Single-Line Title *(default)* | Month + year on one line in nav bar |
| Double-Line Title | Month on first line, year on second |
| Large Title | Large title above calendar — must be **fixed** (not scrollable with content) |

---

## SwiftUI Code Examples

### Month calendar with date selection
```swift
import FioriSwiftUICore

struct InvoiceCalendarView: View {
    @State private var selectedDate = Date()

    var body: some View {
        NavigationStack {
            VStack(spacing: 0) {
                CalendarView(
                    selection: $selectedDate,
                    calendar: .current
                )

                Divider()

                // Agenda below calendar
                List(invoices(for: selectedDate)) { invoice in
                    ObjectItem {
                        Text(invoice.number)
                    } subtitle: {
                        Text(invoice.vendor)
                    } footnote: {
                        Text(invoice.dueDate)
                    }
                }
            }
            .navigationTitle("January")
            .navigationBarTitleDisplayMode(.inline)
        }
    }
}
```

### Week view + day agenda (timesheet pattern)
```swift
VStack(spacing: 0) {
    CalendarWeekView(
        selection: $selectedDate,
        calendar: .current
    )
    .frame(height: 80)

    Divider()

    ScrollView {
        VStack(spacing: 0) {
            ForEach(timesheetEntries(for: selectedDate)) { entry in
                TimelineItem {
                    Text(entry.project)
                } subtitle: {
                    Text(entry.description)
                } attribute: {
                    Text(entry.duration)
                        .foregroundStyle(Color.preferredColor(.secondaryLabel))
                } timelineNode: {
                    TimelineMarker(state: .complete, isLastItem: false)
                }
            }
        }
        .padding(.horizontal, 16)
    }
}
```

### Date range selection
```swift
@State private var startDate: Date? = nil
@State private var endDate: Date? = nil

CalendarView(
    selection: $selectedDate,
    calendar: .current
)
// Configure for range selection at the model/delegate level
```

### Alternate calendar (Hebrew example)
```swift
var hebrewCalendar = Calendar(identifier: .hebrew)

CalendarView(
    selection: $selectedDate,
    calendar: hebrewCalendar
)
```

### Calendar with Monday start (Europe)
```swift
var europeanCalendar = Calendar.current
europeanCalendar.firstWeekday = 2  // Monday

CalendarView(
    selection: $selectedDate,
    calendar: europeanCalendar
)
.navigationTitle("Juli 2026")
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| View type | Month | `CalendarMonthView` |
| View type | Week | `CalendarWeekView` |
| View type | Expandable | `CalendarView` (default) |
| View type | Date selection | `CalendarView` in selection mode |
| Start day | Sunday | `calendar.firstWeekday = 1` |
| Start day | Monday | `calendar.firstWeekday = 2` |
| Start day | Saturday | `calendar.firstWeekday = 7` |
| Cell type | Number only | Configure on model |
| Cell type | Dot indicator | Default |
| Cell type | Icon indicator | Custom configuration required |
| Month label | Single-line | `.navigationBarTitleDisplayMode(.inline)` |
| Month label | Large title | `.navigationBarTitleDisplayMode(.large)` — fix position, do not scroll |
| Calendar system | Gregorian | `Calendar(identifier: .gregorian)` |
| Calendar system | Chinese | `Calendar(identifier: .chinese)` |
| Calendar system | Hebrew | `Calendar(identifier: .hebrew)` |
| Calendar system | Islamic | `Calendar(identifier: .islamicCivil)` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use a single cell display type consistently across the entire calendar — never mix types
- Fix large title month labels in place — they must not scroll with the calendar content
- Use the space below the calendar for contextual content (agenda, timesheet, event list)
- Set `calendar.firstWeekday` based on the user's locale, not a hardcoded value
- Use three-letter title-case month abbreviations (Jan, Feb, Mar) for month labels

**Don't:**
- Use calendar view when a picker (`DateTimePicker`, `DateRangePicker`) would suffice
- Mix dot indicators and icon indicators in the same calendar
- Rely on the SDK for the icon indicator legend — it must be custom-configured

---

## Related Components

- [text-inputs.md](text-inputs.md) — `DateTimePicker`, `DateRangePicker` for text-based date input
- [timeline-view.md](timeline-view.md) — timesheet view below calendar
- [object-cell.md](object-cell.md) — agenda rows below calendar
