# Colors — SAP Fiori for watchOS

> SAP Fiori for watchOS | Foundation

## What is it?

watchOS color palette based on the Horizon visual theme. Colors are **brighter and less saturated** than mobile. **Dark mode only** — saves battery and accommodates varying light conditions.

---

## Core Colors

| Hex | Name | Use |
|-----|------|-----|
| `#000000` | Primary Background | Watch background; label color for tint buttons |
| `#F2F4FC` 14% | Secondary Background | Cards, action backgrounds |
| `#F2F4FC` 20% | Tertiary Background | Secondary buttons next to primary |
| `#222223` | Quaternary Background | Opaque buttons or cards |
| `#F5F6F7` | Primary Label | Titles, primary text |
| `#D5DADD` | Secondary Label | Subtitles, secondary text, section headers |
| `#A9B4BE` | Tertiary Label | Footer text, status, placeholder |
| `#8396A8` | Quaternary Label | Symbols, icons |
| `#89D1FF` | Tint | Tappable elements |
| `#4DB1FF` | Tint Tap State | Tap state of tappable elements |
| `#FF5C77` | Negative Label | Negative/destructive actions or labels |
| `#EE3939` | Negative Label Tap State | Negative tap state |
| `#FFC933` | Critical Label | Attention-needed elements |
| `#FFB300` | Critical Label Tap State | Critical tap state |
| `#BDE986` | Positive Label | Positive elements |
| `#5DC122` | Positive Label Tap State | Positive tap state |
| `#5B738B` 50% | Separator | Decorative separators, hairlines |
| `#8396A8` | Separator (Opaque) | Higher contrast borders, text field borders |

---

## Accent Colors

| Hex | Name |
|-----|------|
| `#FFC933` | Mango |
| `#FF5C77` | Red |
| `#B894FF` | Indigo |
| `#4DB1FF` | Blue |
| `#64EDD2` | Teal |
| `#BDE986` | Green |
| `#FF8AF0` | Pink |
| `#FEADC8` | Raspberry |
| `#A9B4BE` | Grey |

---

## Key Rules

- **Dark mode only** — no light mode for watchOS
- Colors are brighter/less saturated than standard Fiori mobile colors
- Use the dedicated watchOS palette for optimal readability on small screens

```swift
// watchOS uses direct Color values (not Color.preferredColor)
// Reference the watchOS palette directly in WatchKit/SwiftUI for Watch
Color(red: 0.137, green: 0.820, blue: 1.0)  // Tint: #89D1FF
```
