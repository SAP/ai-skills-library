# Timeline View — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Timeline
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUITimelineCell`, `FUITimelineMarkerCell`, SwiftUI `TimelineItem`, `TimelineMarker`

## What is it?

The timeline view displays a list of items (tasks, events, meetings) in chronological order with tappable cells. Items can be filtered and searched.

---

## When to Use

**Do:**
- Show a brief, concise overview of objects
- Organize objects by due date or time
- Indicate status of objects through node color and shape

**Don't:**
- Show all object details in the cell — tap to drill down for details

---

## Anatomy

### Full Timeline View
```
A. Header Cell: "My Tasks"
──────────────────────────────────────
 12:00  ◆ B. Timeline Marker (start)
        │
 14:30  ● C. Past object (filled blue)
        │
[Today] ● D. Current object (blue cell bg)
        │
 16:00  ○ Future object (grey unfilled)
        │
 18:00  ◆ B. Timeline Marker (end)
```

**A. Header Cell** — categorical overview.
**B. Timeline Marker Cell** — diamond-shaped node; marks start/end or visual breaks.
**C. Now Indicator** (optional) — indicates today's cell(s).
**D. Timeline Cells** — concise key info; tappable to drill down.

### Timeline Cell Anatomy
```
A. Timestamp  B. Node/Line  C. Title (3 lines max)
              │             D. Status Stack
              │             E. Description (2 lines max)
              │             F. Attributes (1 line max)
```

**A. Timestamp Column** — flexible format; optional non-interactive icon below.
**B. Node / Node Line** — color and shape communicate state.
**C. Title** — wraps to max 3 lines before truncating.
**D. Status Stack** — status of the object.
**E. Description** — wraps to max 2 lines before truncating.
**F. Attributes** — cannot exceed 1 line.

---

## Node States

| State | Node | Node Line | Cell background |
|-------|------|-----------|----------------|
| Past | Filled blue ● | Blue | Normal |
| Current (today) | Filled blue ● | Blue | Blue tint |
| Future | Grey unfilled ○ | Grey | Normal |
| Start/End marker | Diamond ◆ | Matching color | Normal |

**Node icons:**
- Open circle → open object
- Three dots (…) → in-progress
- Checkmark → completed

---

## Navigation Patterns

| App type | How timeline is reached |
|----------|------------------------|
| Flat navigation | Own tab in tab bar |
| Hierarchical navigation | Via timeline preview cell |
| Landing screen | Direct — no preview needed |

---

## SwiftUI Code Examples

### Basic timeline
```swift
import FioriSwiftUICore

VStack(spacing: 0) {
    ForEach(Array(events.enumerated()), id: \.element.id) { index, event in
        TimelineItem {
            Text(event.title)
                .font(.fiori(forTextStyle: .headline))
        } subtitle: {
            Text(event.subtitle)
                .foregroundStyle(Color.preferredColor(.secondaryLabel))
        } attribute: {
            Text(event.timestamp)
                .foregroundStyle(Color.preferredColor(.tertiaryLabel))
        } status: {
            Text(event.status)
                .foregroundStyle(event.statusColor)
        } timelineNode: {
            TimelineMarker(
                state: event.markerState,
                isLastItem: index == events.count - 1
            )
        }
        .onTapGesture { navigateToDetail(event) }
    }
}
```

### With timeline marker (start/end)
```swift
VStack(spacing: 0) {
    // Start marker
    TimelineItem {
        Text("Project Kickoff")
    } attribute: {
        Text("Jan 15, 09:00")
    } timelineNode: {
        TimelineMarker(state: .complete, isLastItem: false, nodeShape: .diamond)
    }

    // Regular items
    ForEach(milestones) { milestone in
        TimelineItem {
            Text(milestone.title)
        } attribute: {
            Text(milestone.date)
        } timelineNode: {
            TimelineMarker(state: milestone.state, isLastItem: false)
        }
    }

    // End marker
    TimelineItem {
        Text("Project Completion")
    } attribute: {
        Text("Mar 31, 17:00")
    } timelineNode: {
        TimelineMarker(state: .open, isLastItem: true, nodeShape: .diamond)
    }
}
```

### Current item (today indicator)
```swift
TimelineItem {
    Text("Sprint Review")
        .font(.fiori(forTextStyle: .headline))
} attribute: {
    VStack(alignment: .leading) {
        Text("Today")
            .foregroundStyle(Color.preferredColor(.tintColor))
            .font(.fiori(forTextStyle: .footnote, weight: .bold))
        Text("14:00 – 15:00")
            .foregroundStyle(Color.preferredColor(.tertiaryLabel))
    }
} timelineNode: {
    TimelineMarker(state: .inProgress, isLastItem: false)
}
.background(Color.preferredColor(.tintColor).opacity(0.08))
```

### Combined with Calendar view
```swift
VStack(spacing: 0) {
    CalendarWeekView(selection: $selectedDate, calendar: .current)
        .frame(height: 80)
    Divider()
    ScrollView {
        VStack(spacing: 0) {
            ForEach(events(for: selectedDate)) { event in
                TimelineItem { Text(event.title) }
                    .attribute: { Text(event.time) }
            }
        }
        .padding(.horizontal, 16)
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Node | Past (filled blue) | `TimelineMarker(state: .complete)` |
| Node | Current (filled blue + bg) | `.inProgress` + blue background |
| Node | Future (grey) | `TimelineMarker(state: .open)` |
| Node | Start/End marker | `nodeShape: .diamond` |
| Node icon | Open | `.open` state |
| Node icon | In-progress | `.inProgress` state |
| Node icon | Complete | `.complete` state |
| Last item | Yes | `isLastItem: true` — removes connecting line |
| Title wrapping | 3 lines max | `.lineLimit(3)` |
| Description | 2 lines max | `.lineLimit(2)` |
| Attributes | 1 line | `.lineLimit(1)` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Always set `isLastItem: true` on the final node — removes the connecting line
- Show concise cell content — detail belongs on the drill-down page
- Use blue for past/current, grey for future — consistently
- Combine with `CalendarView` for schedule views

**Don't:**
- Show all object details in the timeline cell

---

## Related Components

- [timeline-preview.md](timeline-preview.md) — horizontal preview that navigates to this view
- [calendar.md](calendar.md) — calendar + timeline combination
