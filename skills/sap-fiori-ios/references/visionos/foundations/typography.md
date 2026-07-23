# Typography — SAP Fiori for visionOS

> SAP Fiori for visionOS | Foundation

## What is it?

SAP Fiori for visionOS uses **SF Pro** as its primary typeface. visionOS uses bolder versions of Dynamic Type body and title styles and introduces Extra Large Title styles for wide, editorial-style layouts.

---

## Key Differences from iOS

- Body and title styles use **bolder weights** than standard iOS
- **Extra Large Title 1** and **Extra Large Title 2** introduced for wide layouts
- Tracking values differ from iOS — see Apple HIG for visionOS-specific values

---

## SwiftUI Usage

```swift
// Standard Dynamic Type styles — same API, visionOS applies bolder weights automatically
Text("Invoice #1234")
    .font(.largeTitle)  // bolder on visionOS

Text("Details")
    .font(.title)

Text("Body content")
    .font(.body)

// Extra Large Titles (visionOS / editorial layouts)
Text("Welcome")
    .font(.extraLargeTitle)   // visionOS-specific

Text("Dashboard")
    .font(.extraLargeTitle2)  // visionOS-specific
```

The system applies appropriate visionOS font weights and tracking automatically when using standard text styles — no manual overrides needed.

---

## Resources

- [Apple HIG: Typography for visionOS](https://developer.apple.com/design/human-interface-guidelines/typography#visionOS)
- [visionOS Type Tracking Values](https://developer.apple.com/design/human-interface-guidelines/typography#iOS-iPadOS-visionOS-tracking-values)
