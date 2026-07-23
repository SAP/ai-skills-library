# Time and Date Formats — Design Foundations

> SAP Fiori for iOS | Foundation
> Based on U.S. time and date standards. Formats vary internationally — always follow user locale.

## What is it?

There is no single "right" approach for time and date formatting — conventions vary globally. This guide shares best practices for SAP Fiori iOS apps, based on U.S. standards. Consistency within the app is more important than any specific format.

---

## Time Formats

### 12-Hour Time (U.S. standard)

**AM/PM rules:**
- Capitalized: `AM` / `PM`
- No periods: not `A.M.`
- No spaces between letters: not `A M`
- One space between time and indicator: `9:30 AM`
- No leading zero for hours 1–9: `9:30 AM` not `09:30 AM`

| ✅ Do | ❌ Don't |
|-------|---------|
| `9:30 AM` | `09:30 AM` |
| `12:00 PM` | `12:00 P.M.` |
| `1:10 AM` | `1:10am` |

Midnight = `12:00 AM`; Noon = `12:00 PM`

AM/PM can be omitted when context makes it obvious: `"Breakfast at 7"`, `"9 – 5"` for working hours.

### 24-Hour Time

- Always two digits for hours and minutes: `09:30`, `00:30`
- No AM/PM indicator
- Midnight = `00:00`; Noon = `12:00`
- Afternoon hours above 12: `13:00` = 1:00 PM, `23:59` = 11:59 PM

Less common in the U.S.; use when required by user locale or enterprise context.

---

## Time Use Cases

### Exact Time

```
Full precision:    11:15 AM
Hour only:         12 PM
Context-obvious:   Breakfast at 7
```

### Relative Time

Use long form or abbreviated consistently throughout the app.

```
Long:         3 minutes ago
Abbreviated:  3m ago

Long:         2 hours ago
Abbreviated:  2h ago

Long:         Yesterday
Abbreviated:  Yest.
```

### Time Ranges

Consistency matters more than specific format. Pick one approach and use it throughout:

```
Option A:  9:00 AM – 5:00 PM
Option B:  9 AM to 5 PM
```

### Durations

```
Long:         2 hours 30 minutes
Abbreviated:  2h 30m

Long:         45 seconds
Abbreviated:  45s
```

---

## Date Use Cases

### Relative Dates

Use natural language relative to now. Both options are acceptable — choose one and be consistent:

| Distance from now | Natural language options |
|-------------------|------------------------|
| Same day | "Today", "This morning", "Tonight" |
| Previous day | "Yesterday" |
| Next day | "Tomorrow" |
| Within a week | "Last Tuesday", "Next Friday" |
| More distant | Full date |

**Abbreviated relative dates:** `"Last wk."`, `"Yest."`, `"Tmrw."` — use when space is constrained.

⚠️ Avoid ambiguous abbreviations: if `"m"` means both months and miles on the same screen, spell out at least one.

---

## Space Constraints

When space is tight, prioritize the most important information. Rules:
- Decide whether date or time matters more to the user in context
- Keep the higher-priority element in full; abbreviate or omit the other
- Be consistent — same truncation rule throughout the app

---

## Date + Time Combined

When both date and time are shown (document timestamp, event):
- Place the more important element first
- Example: date-first for calendar events; time-first for live activity feeds

---

## SwiftUI Implementation

Use `Date` formatting APIs — never hardcode format strings:

```swift
// Relative time
Text(date, style: .relative)   // "3 minutes ago"
Text(date, style: .offset)     // "-3 min."

// Exact time
Text(date, style: .time)       // "9:30 AM" (follows locale)

// Date only
Text(date, style: .date)       // "Jan 30, 2026" (follows locale)

// Custom format respecting locale
let formatter = DateFormatter()
formatter.dateStyle = .medium
formatter.timeStyle = .short
formatter.locale = Locale.current  // always use current locale
Text(formatter.string(from: date))

// Duration
let components = DateComponents(hour: 2, minute: 30)
Text(components, formatter: DateComponentsFormatter())
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use `Locale.current` for all date/time formatting
- Be consistent — choose one format and use it throughout the app
- Put the more important element (date or time) first when showing both
- Omit AM/PM when context makes it obvious

**Don't:**
- Hardcode date format strings (they break for international users)
- Mix abbreviated and full formats on the same screen without clear reason
- Use the same abbreviation letter for two different units on the same screen

---

## Related Components

- [pickers.md](../components/pickers.md) — date and time picker inputs
