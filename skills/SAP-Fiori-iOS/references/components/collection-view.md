# Collection View — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUICollectionItemView`, `FUICollectionViewTableViewCell`, `FUICollectionViewLayout`

## What is it?

The collection view is a container that displays items in a visual grid. It previews content using a highly visual layout — always populated with images, never text-only. Collection views are commonly found in overview, object, and object details floorplans.

---

## When to Use

- Display a visual grid of items where images provide the primary value (products, attachments, profiles)
- Preview a subset of a larger list (with a "See All" link)
- Show all items in a set when the full count is known

**Empty collection view:**
- If content is system-generated (e.g. top 10 products), the view always has content
- If content is user-generated (e.g. attachments), the view may start empty
  - **Hide** the collection view entirely, OR
  - Show an **empty state** with a label explaining there is no content yet — no navigation until a cell is added

**Don't** use a collection view to display text-only content — images are required.

---

## Anatomy

```
A. [Section Header]                    [B. See All (N) ›]
┌────────────────────────────────────────────────────┐
│  C. Collection View Cells                          │
│  [ cell ] [ cell ] [ cell ] [ cell ] →             │
└────────────────────────────────────────────────────┘
```

### A. Section Header
Top-left label describing the collection's content. **Mandatory.**

### B. "See All" Label
Top-right navigational link — drills down to the full list. Includes the total count (e.g. "See All (24) ›"). Used when only a subset is displayed (horizontal scroll and horizontal fit variations).

### C. Collection View Cells
Mix of images and short text labels. Each cell navigates to a detail view. See Collection View Cell guidelines for cell specifications.

**Cell sizes and types:**

| # | Type | Size |
|---|------|------|
| 1 | Profile image | 110pt |
| 2 | Initials | 110pt |
| 3 | Image 60×60pt | 110pt |
| 4 | Image 80×60pt | 110pt |
| 5 | Doctype icons | 110pt |
| 6 | Button action | 110pt |
| 7 | Icon actions | 120pt |
| 8 | Image 110×90pt | 120pt |
| 9 | Image 110×100pt | 120pt |
| 10 | Image only | 120pt |

---

## Variations

### 1. Horizontal Scroll
Single horizontal row; scrolls left and right. Use to preview a subset of a list.

- Maximum **20 cells** recommended
- Fixed **16pt padding** between cells
- Always include "See All" with total count

```swift
ScrollView(.horizontal, showsIndicators: false) {
    LazyHStack(spacing: 16) {
        ForEach(items.prefix(20)) { item in
            CollectionCellView(item: item)
                .frame(width: 110, height: 110)
                .onTapGesture { navigateToDetail(item) }
        }
    }
    .padding(.horizontal, 16)
}
```

### 2. Horizontal Fit
Single horizontal row; **does not scroll**. Use when the exact number of cells is known.

- Cells can be **left-aligned** or **justified**
- Padding auto-calculated from container width and cell count
- Min **6pt** / max **65pt** padding between cells
- Include "See All" when showing a subset

```swift
// Justified horizontal fit — equal spacing calculated from available width
GeometryReader { proxy in
    let cellWidth: CGFloat = 110
    let cellCount = CGFloat(min(items.count, maxVisible))
    let totalCellWidth = cellWidth * cellCount
    let spacing = max(6, min(65, (proxy.size.width - totalCellWidth - 32) / max(cellCount - 1, 1)))

    HStack(spacing: spacing) {
        ForEach(items.prefix(Int(cellCount))) { item in
            CollectionCellView(item: item)
                .frame(width: cellWidth, height: cellWidth)
        }
    }
    .padding(.horizontal, 16)
}
.frame(height: 110)
```

### 3. Multi-Row
Cells stack vertically — use when displaying **all** cells (no "See All" needed).

- Horizontal padding auto-calculated (min 6pt / max 65pt)
- Fixed **16pt vertical** padding between rows
- If cell sizes don't fit the width cleanly, left-align instead of justify

```swift
@Environment(\.horizontalSizeClass) var hSizeClass

// Column count based on size class and cell width
let cellWidth: CGFloat = 110
let padding: CGFloat = 16

var columnCount: Int {
    let containerWidth = UIScreen.main.bounds.width - (padding * 2)
    return max(1, Int(containerWidth / (cellWidth + 6)))
}

var columns: [GridItem] {
    Array(repeating: GridItem(.flexible(), spacing: 16), count: columnCount)
}

LazyVGrid(columns: columns, spacing: 16) {
    ForEach(items) { item in
        CollectionCellView(item: item)
            .aspectRatio(1, contentMode: .fit)
            .onTapGesture { navigateToDetail(item) }
    }
}
.padding(16)
```

### 4. Multi-Column
Uses **table view cells** (not collection cells) in a grid layout. The only variation where table view cells are used in a collection view. Contact cells are excluded.

Use cases:
- Full content display: label/value cells in a multi-column grid
- Subset display: predefined number of object cells inside a preview table view

```swift
// Multi-column with ObjectItem cells
let columns = [GridItem(.flexible()), GridItem(.flexible())]

LazyVGrid(columns: columns, spacing: 0) {
    ForEach(items) { item in
        ObjectItem {
            Text(item.title)
        } subtitle: {
            Text(item.subtitle)
        }
        .padding(.vertical, 8)
        Divider()
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Variation | Horizontal scroll | `ScrollView(.horizontal)` + `LazyHStack` |
| Variation | Horizontal fit | `HStack` with calculated spacing |
| Variation | Multi-row | `LazyVGrid` with `.flexible()` columns |
| Variation | Multi-column | `LazyVGrid` with `ObjectItem` cells |
| Alignment | Left | `HStack(alignment: .leading)` |
| Alignment | Justified | Calculated equal spacing |
| Cell spacing | Fixed (horizontal scroll) | `16pt` |
| Cell spacing | Auto (fit/grid) | Min 6pt / max 65pt |
| See All | Yes | `Button` / `FioriButton` top-right with count |
| Empty state | Yes | `IllustratedMessage` |

---

## Behavior & Interaction

- Tapping a cell navigates to the item's detail view
- "See All" navigates to the full list (list report format on compact; masonry layout on regular)
- Empty state: no navigation until at least one cell exists
- All variations support both compact and regular width size classes
- For horizontal/vertical fit: define cell counts separately for landscape and portrait

---

## Do's ✓ / Don'ts ✗

**Do:**
- Always include a section header — it is mandatory
- Include "See All (N)" with total count when showing a subset in horizontal scroll or horizontal fit
- Populate cells with images — this is a visual component
- Limit horizontal scroll to 20 cells maximum
- Use multi-row when all items must be visible (no "See All" needed)
- Show an empty state label when user-generated content hasn't been added yet

**Don't:**
- Use collection view for text-only content
- Use contact cells in multi-column variation
- Omit the total count from the "See All" label
- Allow navigation in empty state — wait until at least one cell is present

---

## Collection View Cell

> Development reference: UIKit `UICollectionView`, `FUIObjectCollectionViewCell`

The collection view cell is the individual item within a collection view. Cells are always visual — they must include an image.

### Anatomy

```
┌─────────────────┐
│                 │
│   A. Image      │
│                 │
├─────────────────┤
│ B. Title        │  (optional)
│ C. Subtitle     │  (optional)
│ D. Attribute    │  (optional)
└─────────────────┘
```

**A. Image** — required. Collection cells must include an image.
**B. Title** — optional. Short description of the object.
**C. Subtitle** — optional. Further information about the object.
**D. Attribute** — optional. Additional metadata, e.g. availability status.

### Behavior

A single tap navigates to the object's detail view. For attachment cells, the tap opens a preview with quick actions (Share, Delete).

### Variations

| Variation | Size | Notes |
|-----------|------|-------|
| Standard image with labels | 110pt or 120pt | Fixed sizes when labels are shown |
| Standard image without labels | 60×60pt – 110×110pt | Size depends on image; rectangular width ≥ height |
| Profile image (circular) | 110pt | Use for people; falls back to initials if no photo |
| Doctype icons | 110pt | Document type icons in a rectangular image view |
| Icon actions | 120pt | 1 or 2 icon actions; count must be consistent across all cells |
| Button actions | 120pt | 1 button action only |

**Icon actions** — use for simple, icon-representable actions. The number of icon actions must be consistent across all cells in the collection.

**Button actions** — use for more complex actions. Only one button action per cell is allowed.

### SwiftUI Code Examples

#### Standard cell (image + title + subtitle)
```swift
struct CollectionCellView: View {
    let item: CollectionItem

    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            AsyncImage(url: item.imageURL) { image in
                image.resizable().aspectRatio(contentMode: .fill)
            } placeholder: {
                Color.preferredColor(.secondaryBackground)
            }
            .frame(width: 110, height: 80)
            .clipShape(RoundedRectangle(cornerRadius: 6))

            Text(item.title)
                .font(.fiori(forTextStyle: .caption1))
                .foregroundStyle(Color.preferredColor(.primaryLabel))
                .lineLimit(2)

            if let subtitle = item.subtitle {
                Text(subtitle)
                    .font(.fiori(forTextStyle: .caption2))
                    .foregroundStyle(Color.preferredColor(.secondaryLabel))
                    .lineLimit(1)
            }
        }
        .frame(width: 110)
    }
}
```

#### Profile image cell (circular, with initials fallback)
```swift
struct ProfileCollectionCell: View {
    let user: User

    var body: some View {
        VStack(spacing: 6) {
            AsyncImage(url: user.avatarURL) { image in
                image.resizable()
                    .aspectRatio(contentMode: .fill)
                    .clipShape(Circle())
            } placeholder: {
                Circle()
                    .fill(Color.preferredColor(.accentBackground3))
                    .overlay(
                        Text(user.initials)
                            .font(.fiori(forTextStyle: .title3))
                            .foregroundStyle(Color.preferredColor(.accentLabel3))
                    )
            }
            .frame(width: 60, height: 60)

            Text(user.name)
                .font(.fiori(forTextStyle: .caption1))
                .foregroundStyle(Color.preferredColor(.primaryLabel))
                .lineLimit(1)
        }
        .frame(width: 110)
    }
}
```

#### Cell with icon actions (1–2 actions, consistent count)
```swift
struct AttachmentCollectionCell: View {
    let attachment: Attachment
    let onShare: () -> Void
    let onDelete: () -> Void

    var body: some View {
        VStack(spacing: 4) {
            Image(systemName: attachment.doctypeIcon)
                .font(.system(size: 40))
                .foregroundStyle(Color.preferredColor(.tintColor))
                .frame(width: 110, height: 80)
                .background(Color.preferredColor(.secondaryBackground))
                .clipShape(RoundedRectangle(cornerRadius: 6))

            Text(attachment.filename)
                .font(.fiori(forTextStyle: .caption1))
                .foregroundStyle(Color.preferredColor(.primaryLabel))
                .lineLimit(1)

            // Icon actions — consistent count across all cells
            HStack(spacing: 16) {
                FioriButton { _ in
                    Image(systemName: "square.and.arrow.up")
                        .accessibilityLabel("Share")
                }
                .fioriButtonStyle(FioriTertiaryButtonStyle())
                .onTapGesture { onShare() }

                FioriButton { _ in
                    Image(systemName: "trash")
                        .accessibilityLabel("Delete")
                }
                .fioriButtonStyle(FioriTertiaryButtonStyle())
                .onTapGesture { onDelete() }
            }
        }
        .frame(width: 120)
    }
}
```

#### Cell with button action (1 action only)
```swift
struct ProductCollectionCell: View {
    let product: Product
    let onAddToCart: () -> Void

    var body: some View {
        VStack(spacing: 4) {
            AsyncImage(url: product.imageURL) { image in
                image.resizable().aspectRatio(contentMode: .fill)
            } placeholder: {
                Color.preferredColor(.secondaryBackground)
            }
            .frame(width: 110, height: 90)
            .clipShape(RoundedRectangle(cornerRadius: 6))

            Text(product.name)
                .font(.fiori(forTextStyle: .caption1))
                .foregroundStyle(Color.preferredColor(.primaryLabel))
                .lineLimit(2)

            // Button action — one only
            FioriButton { _ in Text("Add to Cart") }
                .fioriButtonStyle(FioriSecondaryButtonStyle())
        }
        .frame(width: 120)
    }
}
```

### Do's ✓ / Don'ts ✗

**Do:**
- Always include an image — cells without images are not valid
- Keep the icon action count consistent across all cells in the same collection
- Use circular images for people, rectangular for objects and documents
- Use initials as the fallback when no profile photo is available

**Don't:**
- Use more than 2 icon actions per cell
- Use more than 1 button action per cell
- Make rectangular image width smaller than its height

---

## Related Components

- [cards.md](cards.md) — card-based grid layouts (carousel, masonry)
- [object-item.md](object-item.md) — list-based object display
- [avatars.md](avatars.md) — avatar sizing and shape rules
- [illustrated-message.md](illustrated-message.md) — empty state
