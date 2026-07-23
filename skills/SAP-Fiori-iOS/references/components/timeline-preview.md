# Timeline Preview — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Timeline
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUITimelinePreviewView`, SwiftUI `TimelinePreview`

## What is it?

The timeline preview gives users a brief horizontal glimpse of upcoming objects, sorted chronologically. All objects are **read-only**. Tapping anywhere in the preview navigates to the full timeline view.

---

## When to Use

**Do:**
- Display objects with timestamps and status via nodes
- Allow navigation to the full timeline view

**Don't:**
- Show detailed or extended descriptions — keep it brief

---

## Anatomy

```
A. Header: "My Schedule"    B. See All (24) ›
──────────────────────────────────────────────
C. Object 1   C. Object 2   (compact: 2 items)
D. Timestamp  D. Timestamp  (regular: 4 items)
E. Node─────── Node─────────
F. Title      F. Title
```

**A. Header Cell** — overview of the preview.
**B. Disclosure** — "See All (N)" with total count; taps to full timeline.
**C. Timeline Preview Object** — compact representation: timestamp, node, title.
**D. Timestamp** — time or date. If current: must show "Today" + timestamp.
**E. Node and Node Line** — indicates status and tense (past/current/future).
**F. Title** — concise; wraps up to **2 lines**.

---

## Items Shown

| Size class | Items visible |
|-----------|--------------|
| Compact (iPhone) | 2 |
| Regular (iPad) | 4 |

---

## Node and Node Line Rules

| Shape | State | Visual |
|-------|-------|--------|
| Diamond | Start/end event — past or current | Blue filled ◆ |
| Diamond | Start/end event — future | Grey unfilled ◇ |
| Circle | Open object | Open circle ○ |
| Circle with dots | In-progress | ⋯ inside circle |
| Circle with check | Completed | ✓ inside circle |
| Node line | Past events | Blue |
| Node line | Current + future | Grey |

---

## SwiftUI Code Examples

### Basic timeline preview
```swift
import FioriSwiftUICore

struct SchedulePreview: View {
    let events: [ScheduleEvent]
    let totalCount: Int

    var body: some View {
        TimelinePreview(
            title: AttributedString("My Schedule"),
            disclosureTitle: AttributedString("See All (\(totalCount))"),
            items: events.prefix(previewCount).map { event in
                TimelinePreviewItem(
                    title: AttributedString(event.title),
                    timestamp: AttributedString(event.formattedTime),
                    state: event.timelineState
                )
            },
            action: { navigateToFullTimeline() }
        )
    }

    var previewCount: Int {
        horizontalSizeClass == .regular ? 4 : 2
    }
}
```

### Manual layout
```swift
VStack(spacing: 0) {
    // Header
    HStack {
        Text("Upcoming Events")
            .font(.fiori(forTextStyle: .headline))
        Spacer()
        Button("See All (\(totalCount))") { navigateToTimeline() }
            .font(.fiori(forTextStyle: .subheadline))
            .foregroundStyle(Color.preferredColor(.tintColor))
    }
    .padding(.horizontal, 16)
    .padding(.vertical, 8)

    // Horizontal preview items
    ScrollView(.horizontal, showsIndicators: false) {
        HStack(alignment: .top, spacing: 0) {
            ForEach(Array(events.prefix(4).enumerated()), id: \.element.id) { i, event in
                VStack(alignment: .leading, spacing: 4) {
                    // Timestamp
                    Text(event.isToday ? "Today\n\(event.time)" : event.time)
                        .font(.fiori(forTextStyle: .caption1))
                        .foregroundStyle(event.isToday
                            ? Color.preferredColor(.tintColor)
                            : Color.preferredColor(.secondaryLabel))
                        .lineLimit(2)
                        .frame(height: 32, alignment: .bottom)

                    // Node + line
                    HStack(spacing: 0) {
                        TimelineNode(state: event.state)
                        if i < 3 {
                            Rectangle()
                                .fill(event.isPast
                                    ? Color.preferredColor(.tintColor)
                                    : Color.preferredColor(.separator))
                                .frame(height: 2)
                        }
                    }

                    // Title
                    Text(event.title)
                        .font(.fiori(forTextStyle: .footnote))
                        .foregroundStyle(Color.preferredColor(.primaryLabel))
                        .lineLimit(2)
                }
                .frame(width: 80)
            }
        }
        .padding(.horizontal, 16)
    }
}
.onTapGesture { navigateToTimeline() }
// Tapping anywhere navigates to full timeline
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Items | Compact (2) | `.prefix(2)` |
| Items | Regular (4) | `.prefix(4)` |
| Current timestamp | Today | `"Today\n\(time)"` in tint color |
| Node | Open | `.open` state |
| Node | In-progress | `.inProgress` |
| Node | Complete | `.complete` |
| Node | Start/end | `.diamond` shape |
| Node line | Past | `.tintColor` |
| Node line | Future | `.separator` |
| Tap | Anywhere | `.onTapGesture` on container |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Show "Today" + timestamp for current events
- Always include "See All (N)" with total count
- Make the entire preview tappable (not just a button)
- Show 2 items compact, 4 items regular

**Don't:**
- Show detailed descriptions — only timestamp, node, title
- Make individual items independently tappable — the whole preview navigates to the full view

---

## Related Components

- [timeline-view.md](timeline-view.md) — the full timeline this preview leads to
- [calendar.md](calendar.md) — calendar + timeline combination
