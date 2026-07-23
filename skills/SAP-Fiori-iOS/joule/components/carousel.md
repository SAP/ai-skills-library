# Carousel — Joule Component

> SAP Fiori for iOS | Joule / Components

## What is it?

The Joule carousel displays multiple object cards horizontally with a glimpse of the next card visible at the panel edge, encouraging swipe/scroll. Spans the full width of the Joule panel.

---

## Do's / Don'ts

**Do:** Keep card content concise so the carousel stays compact and users can review their query without excessive scrolling.
**Don't:** Use colors outside the Joule Foundations library for CTA buttons in the cards.

---

## Anatomy

**A. Container** — carousel layout with 16pt left margin; last card is cut off at the right panel edge
**B. Cards** — object cards with flexible properties

---

## Behavior

- **Scroll snapping** — cards snap to predefined positions (not free scroll)
- **Error state** — if any card fails to load, the entire carousel is replaced with an `IllustratedMessage`

---

## Adaptive Design

Medium and expanded screens may show more cards, with larger margins and spacing between cards.

---

## SwiftUI Code Example

```swift
ScrollView(.horizontal, showsIndicators: false) {
    LazyHStack(spacing: 12) {
        ForEach(cards) { card in
            if card.loadFailed {
                // Error state replaces entire carousel
            } else {
                JouleObjectCard(card: card)
                    .frame(width: panelWidth - 48)  // partial next card visible
            }
        }
    }
    .scrollTargetLayout()
    .padding(.leading, 16)
    .padding(.trailing, 8)  // partial visibility of next card
}
.scrollTargetBehavior(.viewAligned)  // snap behavior
.scrollClipDisabled()
// If any card fails → replace with IllustratedMessage
```

---

## Related

- [object-card.md](object-card.md)
- [../foundations/layout.md](../foundations/layout.md)
- [../../patterns/cards.md](../../components/cards.md)
