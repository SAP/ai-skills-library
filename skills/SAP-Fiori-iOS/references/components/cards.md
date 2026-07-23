# Cards & Layouts — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit` (Cards page)
> Development reference: UIKit `FUICardView`, SwiftUI `Card`

## What is it?

A card provides brief, related pieces of information and serves as an entry point, teaser, or preview to more detailed content. Pressing a card navigates to a dedicated page with more detailed information.

---

## When to Use

**Do:**
- Display content from various sources using nested components such as lists, calendars, KPIs, and more
- Focus each card on a single topic — coherent and self-contained
- Use cards as an entry point, teaser, or preview to more detailed content
- Present information in a compact, easily scannable format
- Include a clear external link indicator (e.g. an icon) when selecting the card opens a web browser

**Don't:**
- Place unrelated elements on the same card
- Use inset grouped table view style as a substitute for the card component — inset grouped style does not automatically transform a component into a card
- Include too many UI elements within a single card

---

## Anatomy

Maximum recommended height: **520pt**. Actual height is determined by content.

Card content is organized in **blocks**:

```
┌─────────────────────────────────┐
│  B. Media (optional)            │  decorative image
│─────────────────────────────────│
│  C. Card Header                 │  title, subtitle, status
│─────────────────────────────────│
│                                 │
│  D. Card Body                   │  detail content, data, graphics
│                                 │
│─────────────────────────────────│
│  E. Card Footer                 │  actions (Approve, Submit…)
└─────────────────────────────────┘
    A. Card Container
```

### A. Card Container
Holds header, body, and footer.

### B. Media (optional)
Decorative element — an image that fits the card's context.

### C. Card Header
Uppermost part. Contains essential information: title, subtitle, status. Provides a quick overview of the card's associated detail page.

### D. Card Body
Central part. Provides additional information alongside the header — in-depth details, data, or graphics relevant to the card's context.

### E. Card Footer
Bottom of the card. Used for important or routine actions that directly impact the card's functionality (e.g. "Approve", "Submit").

---

## Orientation

### A. Vertical (recommended for carousels)
Content blocks stack vertically, increasing card height.

```swift
// Vertical — default Card layout
Card {
    Text("Invoice #1234")       // header title
} subtitle: {
    Text("SAP SE")
} body: {
    InvoiceBodyContent()
} footer: {
    ApproveRejectButtons()
}
```

### B. Horizontal (recommended for list layouts)
Media block is placed left or right of the vertically stacked content blocks, creating a wider card.

```swift
// Horizontal — media beside content
HStack(spacing: 0) {
    AsyncImage(url: product.imageURL) { img in
        img.resizable().aspectRatio(contentMode: .fill)
    } placeholder: {
        Color.preferredColor(.secondaryBackground)
    }
    .frame(width: 120)
    .clipped()

    Card {
        Text(product.name)
    } subtitle: {
        Text(product.category)
    } body: {
        ProductDetails(product: product)
    }
}
.background(Color.preferredColor(.secondaryGroupedBackground))
.clipShape(RoundedRectangle(cornerRadius: 12))
.shadow(color: Color.preferredColor(.cardShadow), radius: 4, x: 0, y: 2)
```

---

## Behavior & Interaction

### Selecting a Card
The card's background color changes on tap — immediate visual feedback. Navigates to a detail page (list report, object details).

```swift
Button {
    navigateToDetail(card)
} label: {
    CardView(card: card)
}
.buttonStyle(.plain)  // prevents default button styling from overriding card appearance
```

### Selecting an Interactive Element Within a Card
Only that element's background changes — not the whole card. If data needs loading after selection, a loading indicator appears.

```swift
Card {
    Text("Open Orders")
} body: {
    // Each row is independently tappable
    ForEach(orders) { order in
        ObjectItem { Text(order.number) }
            .onTapGesture { navigateToOrder(order) }
            // Only this row's background changes on tap
    }
}
```

### Empty States
- **Entire card fails to load** — show `IllustratedMessage` inside the card container
- **Only card body fails to load** — show `IllustratedMessage` in the body container only

```swift
Card {
    Text("Revenue")
} body: {
    if loadFailed {
        IllustratedMessage {
            Image(systemName: "exclamationmark.triangle")
                .foregroundStyle(Color.preferredColor(.criticalLabel))
        } title: {
            Text("Couldn't load data")
        } description: {
            Text("Pull to refresh")
        }
    } else {
        RevenueChartView()
    }
}
```

### Skeleton Loading
Three skeleton sizes (small / medium / large) — choose the size that approximately matches the loaded card's height. Apply while data is loading.

```swift
if isLoading {
    SkeletonCard(size: .medium)  // custom — see loading-indicator.md for skeleton pattern
} else {
    InvoiceCard(invoice: invoice)
}
```

---

## Adaptive Design

| Size class | Card behavior |
|-----------|--------------|
| Compact (iPhone) | Narrow card — full width minus padding |
| Regular (iPad) | Wider layout — multi-column grid possible |

```swift
@Environment(\.horizontalSizeClass) var hSizeClass

var columns: [GridItem] {
    hSizeClass == .regular
        ? [GridItem(.flexible()), GridItem(.flexible())]
        : [GridItem(.flexible())]
}

LazyVGrid(columns: columns, spacing: 16) {
    ForEach(cards) { card in
        CardView(card: card)
    }
}
.padding(16)
```

---

## SwiftUI Card Container (base pattern)

```swift
import FioriSwiftUICore

struct FioriCardContainer<Content: View>: View {
    let content: Content

    init(@ViewBuilder content: () -> Content) {
        self.content = content()
    }

    var body: some View {
        content
            .background(Color.preferredColor(.secondaryGroupedBackground))
            .clipShape(RoundedRectangle(cornerRadius: 12))
            .shadow(color: Color.preferredColor(.cardShadow), radius: 4, x: 0, y: 2)
    }
}
```

---

---

## Card Header

> Development reference: UIKit `FUICardMainHeaderView`, `FUICardExtHeaderView`, SwiftUI `CardHeader`

The card header is positioned at the top of a card. It provides essential information about the card and its related detail page content — a quick overview of title, subtitle, and status.

### When to Use

**Do:**
- Include essential information about the card's content in the header
- Use a maximum of **3 lines total** for title + subtitle in the main header
- Use a maximum of **3 rows** in the extended header
- Include only icon buttons that have a direct impact on the card (e.g. bookmark, favorite)
- Ensure good contrast between title text and header image (white on dark, black on light)
- Maintain consistent header component positioning across all cards in the app
- Use a counter only when the card body contains a list (card cells or data table)

**Don't:**
- Use the card header for detailed information — use the card body instead
- Place charts, calendars, or other complex components in the card header
- Duplicate the title if it already appears in the header image

### Anatomy

```
┌──────────────────────────────────────────┐
│  B. Header Image / Media (optional)      │
│──────────────────────────────────────────│
│  C. Main Header                          │
│  [D. Left Accessory]  Title      [E. Right Accessory] │
│                       Subtitle            │
│  [A. Flex Item]                           │
│──────────────────────────────────────────│
│  D. Extended Header (optional)           │
│  [Status] [Text] [Rating] [Tags]  [F. Right KPI] │
│  [Row 2]                          [     ] │
│  [Row 3]                          [     ] │
└──────────────────────────────────────────┘
```

**A. Header Container** — holds image, main header, and extended header.

**B. Header Image (Media)** — optional decorative image. Title text on the image must have sufficient contrast.

**C. Main Header** — title, subtitle, left accessory, right accessory, flex item.

**D. Extended Header** — additional elements: status labels, text, rating controls, tags, KPI value. Up to 3 rows.

### Main Header Components (all optional)

| Slot | Contents | Notes |
|------|----------|-------|
| **A. Flex Item** | Tags, labels, custom components | Flexible container; positioned above left accessory by default, or inside title/subtitle area (above title / between title+subtitle / below subtitle) |
| **B. Title** | Short card description | Max 3 lines combined with subtitle |
| **C. Subtitle** | Refinement or clarification of title | Max 3 lines combined with title |
| **D. Left Accessory** | Thumbnail, avatar, or icon stack | |
| **E. Right Accessory** | Up to 2 elements: icon button, counter, or custom composable | Hugs content, expands left as needed. Counter indicates list item count — logic must be implemented by the app team |

### Extended Header Components (all optional, up to 3 rows)

| Slot | Contents |
|------|----------|
| **A. Status Info Label** | Text + optional icon — describes card status |
| **B. Text** | Plain text |
| **C. Rating Control** | Average rating display |
| **D. Tags (Tag Bar)** | Keywords, labels, categories, statuses |
| **E. Custom Composable** | Any custom component when SDK components don't fit |
| **F. Right Accessory** | KPI value or custom composable — height and width flexible; adjacent rows share horizontal space |

**Row behavior:**
- Each row is limited to one line by default; can be configured to wrap
- With a right accessory: row 1 spans full width; rows 2–3 share horizontal space with the right accessory
- Right accessory only: hugs content, expands as needed

### Behavior

**Overflow menu** — tapping the overflow button opens a menu for host-level card actions (e.g. hide card). Close by tapping anywhere on the card or the overflow icon again.

**Action button** — if a card needs only one specific action (e.g. bookmark), place the icon button directly on the card header instead of an overflow menu.

### SwiftUI Code Examples

#### Basic main header
```swift
import FioriSwiftUICore

Card {
    Text("Open Orders")           // title
} subtitle: {
    Text("Last updated: Today")   // subtitle
} detailImage: {
    Image(systemName: "cart.fill")
        .foregroundStyle(Color.preferredColor(.tintColor))
        .font(.fiori(forTextStyle: .title3))
}
```

#### Main header with right accessory (counter)
```swift
Card {
    Text("Pending Approvals")
} subtitle: {
    Text("Finance · Q3 2026")
} headerAction: {
    // Counter
    Text("3 of 12")
        .font(.fiori(forTextStyle: .footnote))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
}
```

#### Main header with overflow menu
```swift
Card {
    Text("Revenue Overview")
} subtitle: {
    Text("YTD 2026")
} action: {
    // Overflow / bookmark action button
    FioriButton { _ in
        Image(systemName: "ellipsis")
            .accessibilityLabel("More options")
    }
    .fioriButtonStyle(FioriTertiaryButtonStyle())
}
```

#### Extended header with status + tags
```swift
Card {
    Text("Sales Order #5678")
} subtitle: {
    Text("Acme Corp")
} tags: {
    Tag("Open")
    Tag("High Priority")
} status: {
    // Status info label in extended header
    HStack(spacing: 4) {
        Image(systemName: "clock")
            .foregroundStyle(Color.preferredColor(.criticalLabel))
        Text("Due in 2 days")
            .foregroundStyle(Color.preferredColor(.criticalLabel))
    }
    .font(.fiori(forTextStyle: .footnote))
}
```

#### Header image with title (ensure contrast)
```swift
Card {
    Text("Product Launch Event")
        .foregroundStyle(.white)  // white on darker image
} media: {
    AsyncImage(url: event.imageURL) { image in
        image.resizable().aspectRatio(contentMode: .fill)
    } placeholder: {
        Color.preferredColor(.secondaryBackground)
    }
    .frame(height: 160)
    .clipped()
}
```

---

## Card Body

> Development reference: UIKit `FUICardBaseContainer`, SwiftUI `CardBody`

The card body is the central part of the card. It displays additional information alongside the card header, enabling card types such as chart cards, list cards, object cards, and more.

### When to Use

**Do:**
- Include only additional details that are important to the card's context
- Limit the number of components in the card body
- Use components relevant to the card's context
- Keep component placement consistent across all cards in the app (e.g. if a KPI is centered in one card body, center it in all others)

**Don't:**
- Overcrowd the body with too many elements — keep cards compact
- Add status labels or tags to the card body — use the card header for those
- Use the card body for complex tasks — provide detailed functionality on a subsequent detail page

The card body is **optional**. The container is flexible in height until the card's maximum height (520pt) is reached.

### Recommended Existing Components for the Card Body

| | Component | Notes |
|-|-----------|-------|
| A | Avatar row | |
| B | Calendar | |
| C | Text | |
| D | Illustrated message | For empty and error states |
| E | Map | |
| F | KPI | |
| G | KPI with progress chart | |
| H | Label bar | |
| I | Tag bar | |
| J | Custom slot | Any custom component |

### Card-Specific Body Variants

These variants have **reduced horizontal and vertical spacing** compared to their standard counterparts, ensuring a concise card design:

| | Variant | Description |
|-|---------|-------------|
| A | Additional Spacing | Extra space between elements for visual separation |
| B | Chart | Simplified chart: title, subtitle, KPI, visualization (lines/bars), legend |
| C | Contact Cell | Left accessories (thumbnail/avatar) + title/subtitle/footnote + right accessories (1–2 buttons, labels, or statuses) |
| D | Data Table | Two-column table, up to 3 entries. Text color, icons/images, and placement are configurable |
| E | Hairline (Separator) | Visual separator between body elements |
| F | Image | Media image matching the card's content |
| G | Object Cell | Left accessories (thumbnail/avatar/icon stack) + title/subtitle/footnote + right accessories (button, KPI, labels, or statuses) |

### Behavior

**Interactive components** in the card body take over interaction from the card itself. For example, a contact cell in the body handles its own tap navigation — tapping it goes to the contact's detail page, not the card's detail page.

**Empty / error states** — use `IllustratedMessage` inside the card body to communicate no-data or error conditions.

### SwiftUI Code Examples

#### Text body
```swift
Card {
    Text("Quarterly Update")
} body: {
    Text("Revenue grew 12% YoY, driven by cloud subscriptions. Operating margin improved to 28%.")
        .font(.fiori(forTextStyle: .body))
        .foregroundStyle(Color.preferredColor(.primaryLabel))
        .padding(16)
}
```

#### KPI body
```swift
Card {
    Text("Revenue")
} body: {
    VStack(alignment: .leading, spacing: 4) {
        Text("$1.4M")
            .font(.fiori(forTextStyle: .largeKPI, weight: .light))
            .foregroundStyle(Color.preferredColor(.primaryLabel))
        HStack(spacing: 4) {
            Image(systemName: "arrow.up.right")
                .foregroundStyle(Color.preferredColor(.positiveLabel))
            Text("+12% vs last quarter")
                .font(.fiori(forTextStyle: .footnote))
                .foregroundStyle(Color.preferredColor(.positiveLabel))
        }
    }
    .padding(16)
}
```

#### Chart body (card variant — simplified)
```swift
import FioriCharts

Card {
    Text("Monthly Sales")
} subtitle: {
    Text("YTD 2026")
} body: {
    VStack(alignment: .leading, spacing: 8) {
        // KPI above chart
        Text("$8.4M")
            .font(.fiori(forTextStyle: .KPI, weight: .light))
            .foregroundStyle(Color.preferredColor(.primaryLabel))
            .padding(.horizontal, 16)

        // Chart visualization
        ChartView(ChartModel(
            chartType: .line,
            data: [[2.1, 2.4, 1.9, 2.8, 2.6, 3.1, 3.4, 2.9, 3.2, 3.8, 4.1, 4.3]],
            titlesForCategory: [["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]],
            colorsForCategory: [0: [0: Color.preferredColor(.chart1)]]
        ))
        .frame(height: 120)
        .allowsHitTesting(false)  // read-only in card context
    }
    .padding(.vertical, 8)
}
```

#### Object cell body (card variant)
```swift
Card {
    Text("Open Orders")
} subtitle: {
    Text("3 of 12")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
} body: {
    // Card-variant object cells — reduced spacing
    VStack(spacing: 0) {
        ForEach(orders.prefix(3)) { order in
            ObjectItem {
                Text(order.number)
            } subtitle: {
                Text(order.customer)
            } status: {
                Text(order.status)
                    .foregroundStyle(order.isLate
                        ? Color.preferredColor(.negativeLabel)
                        : Color.preferredColor(.secondaryLabel))
            }
            .onTapGesture { navigateToOrder(order) }
            // Each row handles its own navigation independently

            if order.id != orders.prefix(3).last?.id {
                Divider()
                    .padding(.leading, 16)  // hairline separator
            }
        }
    }
}
```

#### Data table body (two columns, up to 3 entries)
```swift
Card {
    Text("Invoice Summary")
} body: {
    VStack(spacing: 0) {
        ForEach([
            ("Vendor", "SAP SE"),
            ("Amount", "$1,450.00"),
            ("Due Date", "30 Jan 2026")
        ], id: \.0) { key, value in
            HStack {
                Text(key)
                    .font(.fiori(forTextStyle: .subheadline))
                    .foregroundStyle(Color.preferredColor(.secondaryLabel))
                Spacer()
                Text(value)
                    .font(.fiori(forTextStyle: .subheadline))
                    .foregroundStyle(Color.preferredColor(.primaryLabel))
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 8)
            Divider().padding(.leading, 16)
        }
    }
}
```

#### Empty state body
```swift
Card {
    Text("Recent Activity")
} body: {
    IllustratedMessage {
        Image(systemName: "tray")
            .font(.system(size: 40))
            .foregroundStyle(Color.preferredColor(.tertiaryLabel))
    } title: {
        Text("No activity yet")
    } description: {
        Text("Activity will appear here once available.")
            .foregroundStyle(Color.preferredColor(.secondaryLabel))
            .multilineTextAlignment(.center)
    }
    .padding(24)
}
```

---

## Card Footer

> Development reference: UIKit `FUICardFooterView`, SwiftUI `CardFooter`

The card footer (also called card toolbar) is the bottom part of the card. It contains important or routine actions that directly impact the card — such as "Approve" or "Submit". Maximum **two action buttons**.

### When to Use

**Do:**
- Include only 1–2 of the most important, routine actions
- With two buttons: primary action on the **right**, secondary action on the **left**
- Use short, concise button labels that describe the action performed after tapping
- Use symbol buttons when the label would be too long and a universally known icon exists
- Use filled buttons (Primary or Secondary) — they are more visually prominent than tertiary buttons

**Don't:**
- Use long button labels — move to overflow or use a symbol button instead
- Truncate button labels — use the overflow mechanism instead

### Anatomy

```
┌──────────────────────────────────────────┐
│  [C. Secondary Action]  [B. Primary Action] │
└──────────────────────────────────────────┘
         A. Card Footer Container
```

**A. Card Footer Container** — holds 1–2 buttons, evenly distributed.

**B. Primary Action Button** — highlights the most important action. One per card. Use Primary button style.

**C. Secondary Action Button** — for non-primary actions. Use Secondary button style. If the action is destructive, use secondary negative style.

Three valid configurations:
1. One primary button only
2. One primary (right) + one secondary (left)
3. One secondary negative (left) + one secondary tint (right) — when no clear primary exists

### Overflow Button (SwiftUI only)

> Not available in UIKit implementation.

| Size class | Overflow triggers when |
|------------|----------------------|
| Compact | More than 2 text buttons |
| Regular | More than 3 text buttons |

Additional buttons move into an overflow menu — no limit on the number of items in the menu. Most important actions are shown first.

**Long label behavior:** When a label is too long to show two buttons side by side, the secondary button moves into overflow and the primary button extends to full width.

### Feedback Indicators (must be implemented manually — not in SDK)

> User-triggered feedback indicators are not supported by the SAP BTP SDK for iOS and must be implemented manually.

**Partial loading (overlay)** — after a footer action, an overlay progress indicator covers the affected area while data loads. The rest of the card remains navigable. Show a `ToastMessage` for brief confirmation of the action.

**In-place loading** — when the card's status changes or an action is triggered, an in-place loading indicator can be used within the card.

**Card disappears after action** — show a `ToastMessage` to confirm the status change. If the action fails, show a `BannerMessage` instead.

When a component within the card navigates to a new page, the feedback indicator should appear only on that component — not the whole card.

### SwiftUI Code Examples

#### One primary button
```swift
Card {
    Text("Invoice #1234")
} footer: {
    FioriButton { _ in Text("Submit") }
        .fioriButtonStyle(FioriPrimaryButtonStyle())
        .frame(maxWidth: .infinity)
}
```

#### Primary + secondary (approve / reject pattern)
```swift
Card {
    Text("Purchase Request #9876")
} footer: {
    // Secondary on left, Primary on right
    HStack(spacing: 12) {
        FioriButton { _ in Text("Reject") }
            .fioriButtonStyle(FioriSecondaryButtonStyle())
            .tint(Color.preferredColor(.negativeLabel))  // secondary negative
            .frame(maxWidth: .infinity)

        FioriButton { _ in Text("Approve") }
            .fioriButtonStyle(FioriPrimaryButtonStyle())
            .frame(maxWidth: .infinity)
    }
    .padding(.horizontal, 16)
    .padding(.vertical, 12)
}
```

#### Two equal-priority secondary actions
```swift
Card {
    Text("Meeting Invite")
} footer: {
    HStack(spacing: 12) {
        FioriButton { _ in Text("Decline") }
            .fioriButtonStyle(FioriSecondaryButtonStyle())
            .frame(maxWidth: .infinity)

        FioriButton { _ in Text("Accept") }
            .fioriButtonStyle(FioriSecondaryButtonStyle())
            .frame(maxWidth: .infinity)
    }
    .padding(.horizontal, 16)
    .padding(.vertical, 12)
}
```

#### With partial loading feedback (manual implementation)
```swift
@State private var isSubmitting = false
@State private var showSuccessToast = false

Card {
    Text("Invoice #1234")
} body: {
    ZStack {
        InvoiceBody()
            .opacity(isSubmitting ? 0.4 : 1.0)

        if isSubmitting {
            ProgressView()
                .tint(Color.preferredColor(.tintColor))
        }
    }
} footer: {
    FioriButton { _ in Text("Submit") }
        .fioriButtonStyle(FioriPrimaryButtonStyle())
        .frame(maxWidth: .infinity)
        .disabled(isSubmitting)
        .onTapGesture {
            Task {
                isSubmitting = true
                try await submitInvoice()
                isSubmitting = false
                showSuccessToast = true
            }
        }
}
.toast(isPresented: $showSuccessToast) {
    ToastMessage {
        Text("Invoice submitted")
    } icon: {
        Image(systemName: "checkmark.circle.fill")
            .foregroundStyle(Color.preferredColor(.positiveLabel))
    }
}
```

---

## Figma Variants → SwiftUI (Full Card)

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Orientation | Vertical | Default `Card {}` |
| Orientation | Horizontal | `HStack` with media + `Card {}` |
| Header / Image | Yes | `media: { AsyncImage(...) }` |
| Header / Left accessory | Avatar | `detailImage: { ... }` |
| Header / Right accessory | Counter | `headerAction: { Text("3 of 12") }` |
| Header / Right accessory | Overflow | `action: { FioriButton { _ in Image(systemName: "ellipsis") } }` |
| Header / Extended | Status | `status: { ... }` |
| Header / Extended | Tags | `tags: { Tag("...") }` |
| Body | Chart | `ChartView(model)` inside `body: {}` |
| Body | Object cells | `ObjectItem {}` inside `body: {}` |
| Body | KPI | `Text` with `.fiori(forTextStyle: .largeKPI)` |
| Body | Empty state | `IllustratedMessage {}` inside `body: {}` |
| Footer | 1 primary | `FioriPrimaryButtonStyle()` full width |
| Footer | Primary + secondary | `HStack` — secondary left, primary right |
| Footer | Destructive | `.tint(Color.preferredColor(.negativeLabel))` |

---

## Layouts

Cards are placed within layout containers. Two layout types are available: Carousel (horizontal) and Masonry (grid). They can be combined on the same page, but note that they have different outer margins.

---

### Carousel Layout

> Development reference: UIKit `FUICollectionViewLayout.carousel`, SwiftUI `Carousel`

A carousel displays multiple cards horizontally with a glimpse of the next card visible at the screen edge, encouraging horizontal swipe/scroll to reveal more.

#### When to Use

**Do:**
- Use for a sequence of **3 or more** related cards
- Use to maximize information density and preserve context without long vertical scrolling
- Use to highlight specific content users should browse (featured products, articles)
- Combine with a header cell with a title so the carousel's context is clear

**Don't:**
- Use with fewer than 3 cards — place them vertically instead
- Use when card content is critical and must always be visible (real-time KPIs, statuses)

#### Anatomy

All cards in a carousel share the same height by default — determined by the tallest card. Shorter cards are stretched to match; the footer is always bottom-aligned. This can produce whitespace between body and footer on shorter cards.

Variable-height carousels are supported but not recommended. If used, cards are top-aligned.

#### Behavior

**Scroll snapping (default)** — cards snap to predefined positions during scroll ("drag gesture"). Gives a sense of precision.

**Simple scrolling** — free horizontal scroll without snapping. Choose based on card count and target audience.

**"See All" navigation** — if the carousel contains many cards, add a header cell with a "See All" action. Tapping it navigates to a page showing all cards in a list (vertical stack). On regular size class, use a masonry layout for that "See All" page instead of a vertical stack.

**Empty state** — show `IllustratedMessage` inside the carousel container when no cards are available.

#### Adaptive Design

Carousel works in both compact (iPhone) and regular (iPad) size classes. When used on the same page as a masonry layout, note the visual imbalance: carousel has asymmetric outer margins (different left vs right spacing), while masonry has equal margins on both sides.

#### SwiftUI Code Examples

```swift
import FioriSwiftUICore

// Carousel with scroll snapping (default)
Carousel {
    ForEach(featuredItems) { item in
        FeaturedCard(item: item)
            .frame(width: cardWidth)
    }
}

// Determine card width — show partial next card
var cardWidth: CGFloat {
    UIScreen.main.bounds.width - 48  // 16pt leading + 16pt card-to-card + 16pt peek
}
```

```swift
// Native SwiftUI scroll carousel with snapping
ScrollView(.horizontal, showsIndicators: false) {
    LazyHStack(spacing: 12) {
        ForEach(cards) { card in
            CardView(card: card)
                .frame(width: UIScreen.main.bounds.width - 48)
                .scrollTransition { content, phase in
                    content.opacity(phase.isIdentity ? 1 : 0.85)
                }
        }
    }
    .scrollTargetLayout()
    .padding(.horizontal, 16)
}
.scrollTargetBehavior(.viewAligned)  // scroll snapping
.scrollClipDisabled()  // allows peek of next card
```

```swift
// Simple scrolling (no snapping)
ScrollView(.horizontal, showsIndicators: false) {
    LazyHStack(spacing: 12) {
        ForEach(cards) { card in
            CardView(card: card)
                .frame(width: UIScreen.main.bounds.width - 48)
        }
    }
    .padding(.horizontal, 16)
}
// No .scrollTargetBehavior — free scroll
```

```swift
// Carousel with header cell + "See All"
VStack(alignment: .leading, spacing: 8) {
    // Header cell
    HStack {
        Text("Featured Orders")
            .font(.fiori(forTextStyle: .title3, weight: .semibold))
            .foregroundStyle(Color.preferredColor(.primaryLabel))
        Spacer()
        FioriButton { _ in Text("See All") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .onTapGesture { navigateToAllOrders() }
    }
    .padding(.horizontal, 16)

    // Carousel
    ScrollView(.horizontal, showsIndicators: false) {
        LazyHStack(spacing: 12) {
            ForEach(orders) { order in
                OrderCard(order: order)
                    .frame(width: UIScreen.main.bounds.width - 48)
            }
        }
        .scrollTargetLayout()
        .padding(.horizontal, 16)
    }
    .scrollTargetBehavior(.viewAligned)
    .scrollClipDisabled()
}
```

```swift
// Carousel empty state
ScrollView(.horizontal, showsIndicators: false) {
    if cards.isEmpty {
        IllustratedMessage {
            Image(systemName: "rectangle.stack")
                .font(.system(size: 48))
                .foregroundStyle(Color.preferredColor(.tertiaryLabel))
        } title: {
            Text("No cards available")
        } description: {
            Text("Cards will appear here once data is available.")
                .multilineTextAlignment(.center)
        }
        .frame(width: UIScreen.main.bounds.width - 32)
        .padding(24)
    } else {
        LazyHStack(spacing: 12) {
            ForEach(cards) { card in
                CardView(card: card)
                    .frame(width: UIScreen.main.bounds.width - 48)
            }
        }
        .scrollTargetLayout()
        .padding(.horizontal, 16)
    }
}
.scrollTargetBehavior(.viewAligned)
.scrollClipDisabled()
```

<!-- MASONRY LAYOUT SECTION — to be added -->

---

### Masonry Layout

> Development reference: UIKit `FUICollectionViewLayout.masonry`, SwiftUI `MasonryLayout`

The masonry layout arranges cards in a flexible grid where all cards share a consistent width (based on column count) but vary in height. This creates an asymmetric, space-efficient appearance.

#### When to Use

**Do:**
- Use to showcase important content from different data sources side by side (product features, KPIs, statuses)
- Use to give users an overview of a specific data set
- Use when there are **9 or more** cards to display
- Use a title (via header cell) when the page includes multiple card layouts (e.g. carousel + masonry)

**Don't:**
- Use when you only have a few cards — place them vertically or use a carousel instead

#### Anatomy

- All cards share a **consistent width** determined by column count
- Card **height varies** based on content — creates the asymmetric masonry appearance
- Column count is determined by horizontal size class and is customizable
- Card positions are **static** — users cannot rearrange them

#### Card Prioritization

Cards are placed top-left first. The most important card goes in the **upper-left corner**. Subsequent cards fill top-to-bottom, left-to-right — each new card positioned at the top edge and leftmost available position.

#### Behavior

Cards scroll **vertically**. No horizontal scrolling.

**Empty state** — show `IllustratedMessage` inside the masonry container when no cards exist.

#### Adaptive Design

| Size class | Recommended columns |
|-----------|-------------------|
| Compact (iPhone) | 1 column |
| Regular (iPad) | 3 columns |
| Regular with sidebar | Reduce columns to fit narrower content area |

#### SwiftUI Code Examples

```swift
import FioriSwiftUICore

// Masonry layout using SDK component
MasonryLayout(numOfColumns: columnCount) {
    ForEach(cards) { card in
        DashboardCard(card: card)
    }
}
.padding(16)

var columnCount: Int {
    horizontalSizeClass == .regular ? 3 : 1
}
```

```swift
// Native SwiftUI masonry (LazyVGrid with variable height)
@Environment(\.horizontalSizeClass) var hSizeClass

var columns: [GridItem] {
    let count = hSizeClass == .regular ? 3 : 1
    return Array(repeating: GridItem(.flexible(), spacing: 12), count: count)
}

ScrollView {
    LazyVGrid(columns: columns, alignment: .leading, spacing: 12) {
        ForEach(cards) { card in
            DashboardCard(card: card)
        }
    }
    .padding(16)
}
```

```swift
// With header cell title
VStack(alignment: .leading, spacing: 8) {
    Text("Overview")
        .font(.fiori(forTextStyle: .title3, weight: .semibold))
        .foregroundStyle(Color.preferredColor(.primaryLabel))
        .padding(.horizontal, 16)

    LazyVGrid(columns: columns, spacing: 12) {
        ForEach(cards) { card in
            DashboardCard(card: card)
        }
    }
    .padding(.horizontal, 16)
}
```

```swift
// Sidebar-aware column count
@Environment(\.horizontalSizeClass) var hSizeClass

// Reduce columns when sidebar is visible
var columnCount: Int {
    switch hSizeClass {
    case .regular where hasSidebar: return 2
    case .regular:                  return 3
    default:                        return 1
    }
}
```

```swift
// Masonry empty state
if cards.isEmpty {
    IllustratedMessage {
        Image(systemName: "square.grid.2x2")
            .font(.system(size: 48))
            .foregroundStyle(Color.preferredColor(.tertiaryLabel))
    } title: {
        Text("No data available")
    } description: {
        Text("Cards will appear here once data is available.")
            .multilineTextAlignment(.center)
    }
    .padding(24)
} else {
    LazyVGrid(columns: columns, spacing: 12) {
        ForEach(cards) { card in
            DashboardCard(card: card)
        }
    }
    .padding(16)
}
```

#### Carousel + Masonry on the Same Page

Combining both layouts is supported but creates a **visual margin imbalance**:
- Carousel: asymmetric outer margins (different left vs. right spacing for the peek effect)
- Masonry: symmetric outer margins (equal left and right)

Mitigate by using consistent section titles (header cells) to visually separate the two layout areas.

---

## Do's ✓ / Don'ts ✗

**Do:**
- Focus each card on a single topic
- Keep card height under 520pt
- Use skeleton loading while card data is fetching (3 size options: small/medium/large)
- Show `IllustratedMessage` for both full-card and body-only empty/error states
- Place primary footer action on the right, secondary on the left
- Use overflow for additional footer actions beyond 2 (compact) or 3 (regular)
- Implement partial loading overlay manually — it's not in the SDK

**Don't:**
- Use inset grouped table view style as a substitute for cards
- Mix unrelated content in a single card
- Place status labels or tags in the card body — use the card header
- Truncate footer button labels — use overflow or a symbol button instead
- Use green for positive footer actions — use secondary tint style

---

## Related Components

- [object-item.md](object-item.md) — object cell in card body
- [kpi-item.md](kpi-item.md) — KPI in card body or header
- [charts.md](charts.md) — chart in card body
- [illustrated-message.md](illustrated-message.md) — empty/error states in card
- [banner-message.md](banner-message.md) — failed action feedback
- [loading-indicator.md](loading-indicator.md) — skeleton loading pattern
