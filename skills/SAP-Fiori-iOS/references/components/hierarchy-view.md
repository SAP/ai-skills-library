# Hierarchy View — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIHierarchyView`, `FUIListFloorplan`

## What is it?

The hierarchy view shows the relationship between parent and child objects in a column-based layout. It serves as an entry point for the user to understand where an object lives within a larger hierarchical structure.

**For single-level data sets, use a list report instead.**

---

## When to Use

- Multi-level hierarchical data (org charts, product categories, cost centers, bill of materials)
- When users need to navigate between parent and child levels
- Minimum two levels required — single-level data belongs in a list report

---

## Usage Guidelines

**Single-line object cells:** Use the horizontal variation of the hierarchy accessory to avoid unnecessary spacing between cells.

**Action buttons:** Use with caution next to the hierarchy icon — combining single action buttons and contact icons creates too many touch targets in close proximity.

**Icon stacks:** Use with caution inside hierarchy cells — they can cause heavy text truncation due to limited horizontal space per column.

---

## Anatomy

```
│ Column 1 (Level 1) │ Column 2 (Level 2) │ Column 3 (Level 3) │ → scroll
│                    │                    │                    │
│ ▶ Parent A         │ ▶ Child A1         │   Grandchild A1a   │
│                    │   Child A2         │   Grandchild A1b   │
│   Parent B         │                    │                    │
│ ▶ Parent C         │                    │                    │
```

- **▶ Hierarchy icon** — appears on objects that have children; hidden on leaf nodes
- Tapping the hierarchy icon expands the object to reveal its children in the next column
- Each column shows one level of the hierarchy

---

## Behavior & Interaction

### Hierarchy Icon
Tapping expands the object and displays its children in the adjacent column. Hidden for objects without children (leaf nodes).

### Horizontal Swipe
Once a path has been expanded, horizontal swiping scrolls the columns. The nearest column snaps to the edge.

### Vertical Scroll
Within a single column, users can scroll vertically to view more objects at that level.

---

## Variations

### Two-Column Layout
Parent level in column 1, child objects in column 2 when expanded.

### Three-Column Layout
When column 2 also contains parent objects, expanding them shows their children in column 3.

### More Than Three Columns
For large hierarchies with many levels, additional columns are added automatically to display preceding and succeeding levels.

### Picker Mode
A select-state symbol appears in the left accessory of each cell, enabling users to select items from the hierarchy.

---

## SwiftUI Code Examples

### Basic hierarchy view
```swift
import FioriSwiftUICore

struct OrgChartView: View {
    @State private var expandedNodes: Set<String> = []

    var body: some View {
        HierarchyView(
            data: orgChartData,
            expandedItems: $expandedNodes
        ) { node in
            HierarchyItemView {
                Text(node.name)
                    .font(.fiori(forTextStyle: .headline))
            } subtitle: {
                Text(node.title)
                    .foregroundStyle(Color.preferredColor(.secondaryLabel))
            }
        }
    }
}
```

### Picker mode (selection)
```swift
@State private var selectedNodes: Set<String> = []

HierarchyView(
    data: costCenterData,
    expandedItems: $expandedItems,
    selectedItems: $selectedNodes
) { node in
    HierarchyItemView {
        Text(node.name)
    } subtitle: {
        Text(node.code)
            .foregroundStyle(Color.preferredColor(.secondaryLabel))
    }
}
```

### Caution: icon stack in hierarchy cell
```swift
// ⚠️ Use with caution — icon stacks can cause heavy truncation in narrow columns
HierarchyItemView {
    Text(node.name)
        .lineLimit(1)  // always limit to 1 line in hierarchy cells
} footnoteIcons: {
    // Keep icon stacks minimal — 1–2 icons maximum
    Image(systemName: "exclamationmark.circle")
        .foregroundStyle(Color.preferredColor(.criticalLabel))
}
```

### Caution: action buttons in hierarchy cell
```swift
// ⚠️ Avoid combining action buttons AND hierarchy icon — too many touch targets
// If actions are needed, prefer a detail navigation on row tap instead
HierarchyItemView {
    Text(node.name)
}
// Tap the row → navigate to detail
.onTapGesture { navigateToDetail(node) }
// Don't add action buttons inline
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Columns | 2 | Two levels expanded |
| Columns | 3 | Three levels expanded |
| Columns | 3+ | Additional columns auto-added |
| Mode | Browse | Default `HierarchyView` |
| Mode | Picker | Add `selectedItems` binding |
| Hierarchy icon | Visible | Node has children |
| Hierarchy icon | Hidden | Leaf node (no children) |
| Accessory | Horizontal | Use horizontal hierarchy accessory variant |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use for multi-level hierarchies (2+ levels)
- Use the horizontal hierarchy accessory variant with single-line cells
- Limit text to 1 line per cell — column widths are narrow
- Hide the hierarchy icon for leaf nodes

**Don't:**
- Use for single-level data — use a list report instead
- Combine action buttons and contact icons next to the hierarchy icon
- Use icon stacks carelessly — they cause truncation in narrow columns

---

## Related Components

- [object-item.md](object-item.md) — list rows for flat/single-level data
- [sidebar.md](sidebar.md) — hierarchical navigation pattern for iPad
