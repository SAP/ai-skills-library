# Object Cell — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Table View Cells
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit` (Lists page)
> Development reference: UIKit `FUIObjectTableViewCell`, SwiftUI `ObjectItem`

## What is it?

The object cell is a highly customizable table view cell for previewing information about a business object. It is the primary building block for list reports and object detail pages.

---

## When to Use

**Do:**
- Preview information about an object in a list or object page
- Keep consistent height and alignment across all cells in the same list

**Don't:**
- Mix object cells with different heights and content types in the same list

---

## Anatomy

```
A. Left     B. Detail    C. Main Content              D. Description  E. Attrs   F. Accessory
Icon Stack  Image        Title (required)              (portrait:      (status/   (chevron /
(optional)  (optional)   Subtitle                      below main;     priority)  info / action)
                         Footnote                      landscape:
                         Caption                       own column)
                         Description
                         Rating Control
                         Avatar Stack
                         Tags
```

**A. Left Icon Stack** — up to 3 vertically stacked icons (left of detail image). Indicates unread state, attachments, etc.

**B. Detail Image** — visual representation within a **44px frame**. Min 16px, max 60px. Shape:
- **Circular** — for people/users
- **Square** — for objects

**C. Main Content** — primary text area. **Title is the only mandatory element.** Also supports: subtitle, footnote, caption, description, rating control, avatar stack, tags.

**D. Description** (optional) — portrait: below main content; landscape: separate column (wider text). Default truncates at 3 lines (configurable or full display).

**E. Attributes** — vertically or horizontally stacked labels/icons on the right side. Indicates condition, priority, or status.

**F. Accessory View** — secondary action or navigation indicator:
- Chevron (›) → push navigation
- Info disclosure (ⓘ) → modal
- Download icon → single action
- Overflow menu (…) → multiple actions

---

## Alignment Variants

| Variant | When to use |
|---------|------------|
| Vertically centered | Single-line content only |
| Top-aligned | Multi-line content |

---

## Variations

### Preview Object Cell (most common)
Chevron in accessory view. Tapping drills down to full object content (object page).

### Quick View Object Cell
Info disclosure icon in accessory view. Tapping opens a modal with additional info and simple actions — no full object page needed.

### Single Action Object Cell
Icon or button in accessory view for a specific action (download, add to cart, Follow/Unfollow toggle).

---

## Behavior & Interaction

### Edit Mode (Multi-Select)
Triggered by entering edit mode. Users can select single or multiple cells for bulk actions (delete, status change, etc.).

### Quick Actions (Swipe)
Swipe to reveal contextual actions (delete, approve, edit). **Always complemented by a visible single-tap alternative** — swipe must never be the only way to access an action.

Acceptable primary alternatives:
- Visible overflow button on the cell
- Single-tap navigation to detail page where action is available

### Context Menu & Preview (iOS 13+)
Long-press opens a context menu with preview. Secondary interaction only — must not be the sole way to access actions.

---

## SwiftUI Code Examples

### Standard preview object cell
```swift
import FioriSwiftUICore

ObjectItem {
    Text("Invoice #1234")
        .font(.fiori(forTextStyle: .headline))
} subtitle: {
    Text("SAP SE")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
} footnote: {
    Text("Due: 30 Jan 2026")
        .foregroundStyle(Color.preferredColor(.tertiaryLabel))
} status: {
    Text("Overdue")
        .foregroundStyle(Color.preferredColor(.negativeLabel))
} detailImage: {
    Image(systemName: "doc.text.fill")
        .font(.fiori(forTextStyle: .title3))
        .foregroundStyle(Color.preferredColor(.tintColor))
}
// Chevron (›) added automatically in List context
```

### With left icon stack
```swift
ObjectItem {
    Text("Contract #567")
} footnoteIcons: {
    Image(systemName: "paperclip")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
    Image(systemName: "exclamationmark.circle")
        .foregroundStyle(Color.preferredColor(.criticalLabel))
} detailImage: {
    Image(systemName: "doc.fill")
        .foregroundStyle(Color.preferredColor(.tintColor))
}
```

### Quick view (info disclosure)
```swift
ObjectItem {
    Text("Product XR-400")
} subtitle: {
    Text("Electronics")
} detailImage: {
    AsyncImage(url: product.imageURL) { img in
        img.resizable()
            .aspectRatio(contentMode: .fill)
            .clipShape(RoundedRectangle(cornerRadius: 6))
    } placeholder: {
        RoundedRectangle(cornerRadius: 6)
            .fill(Color.preferredColor(.secondaryBackground))
    }
    .frame(width: 44, height: 44)
} accessory: {
    // Info disclosure → opens modal, not push
    Image(systemName: "info.circle")
        .foregroundStyle(Color.preferredColor(.tintColor))
}
.onTapGesture { showQuickView = true }
```

### Single action (toggle Follow)
```swift
ObjectItem {
    Text("Jane Smith")
} subtitle: {
    Text("Engineering Lead")
} detailImage: {
    Image("jane_avatar").clipShape(Circle())
} accessory: {
    FioriButton(isSelectionPersistent: true) { state in
        Text(state == .selected ? "Following" : "Follow")
    }
    .fioriButtonStyle(FioriSecondaryButtonStyle())
}
```

### With swipe actions + visible overflow alternative
```swift
ObjectItem {
    Text("Invoice #1234")
} subtitle: {
    Text("SAP SE")
} accessory: {
    // Visible overflow menu — primary access to actions
    Menu {
        Button("Approve") { approve(invoice) }
        Button("Reject") { reject(invoice) }
        Button("Delete", role: .destructive) { delete(invoice) }
    } label: {
        Image(systemName: "ellipsis.circle")
            .foregroundStyle(Color.preferredColor(.tintColor))
    }
}
.swipeActions(edge: .trailing) {
    // Swipe = secondary / shortcut only
    Button(role: .destructive) { delete(invoice) } label: {
        Label("Delete", systemImage: "trash")
    }
}
.swipeActions(edge: .leading) {
    Button { approve(invoice) } label: {
        Label("Approve", systemImage: "checkmark.circle")
    }
    .tint(Color.preferredColor(.positiveLabel))
}
```

### Multi-select edit mode
```swift
List(invoices, selection: $selectedInvoices) { invoice in
    ObjectItem { Text(invoice.number) }
        .subtitle: { Text(invoice.vendor) }
}
.environment(\.editMode, $editMode)
.toolbar {
    ToolbarItem(placement: .primaryAction) {
        EditButton()
    }
}
```

### AttributedString convenience form
```swift
ObjectItem(
    title: AttributedString("Invoice #1234"),
    subtitle: AttributedString("SAP SE"),
    footnote: AttributedString("Due: 30 Jan 2026"),
    status: AttributedString("Overdue")
)
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Alignment | Vertically centered | Single-line content |
| Alignment | Top-aligned | Multi-line content |
| Variation | Preview | Chevron in accessory (automatic in `List`) |
| Variation | Quick view | Custom info icon in accessory |
| Variation | Single action | Button/icon in accessory |
| Detail image | Circular (person) | `.clipShape(Circle())` |
| Detail image | Square (object) | `.clipShape(RoundedRectangle(cornerRadius: 6))` |
| Left icons | 1–3 | `footnoteIcons: { Image... Image... }` |
| Description | Portrait | Below main content |
| Description | Landscape | Separate column |
| Quick actions | Swipe | `.swipeActions` + visible overflow alternative |
| Edit mode | Yes | `.environment(\.editMode, $editMode)` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Keep consistent height and content across all cells in a list
- Use circular images for people, square for objects
- Always provide a single-tap alternative when using swipe actions
- Use top alignment for multi-line cells

**Don't:**
- Mix cells with different heights in the same list
- Make swipe gestures the only way to access actions
- Use more than 3 left icon stack icons

---

## Related Components

- [object-header.md](object-header.md) — header version of object display
- [contact-cell.md](contact-cell.md) — contact-specific cell with communication actions
- [key-value-table-view-cell.md](key-value-table-view-cell.md) — read-only key/value display
