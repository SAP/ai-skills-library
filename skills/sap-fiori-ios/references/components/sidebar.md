# Sidebar — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit` (Navigation page)
> Development reference: UIKit `FUISideBar`, SwiftUI `SideBar`

## What is it?

A sidebar provides app-level navigation and quick access to pinned or favorite content. It is designed for users who frequently switch between app-level destinations.

**Sidebar is only available in regular width (iPad).** For compact width (iPhone), use a tab bar instead.

---

## When to Use

- App-level navigation on iPad with multiple destinations
- When users switch between sections frequently
- When more than 5–6 destinations exist (beyond tab bar capacity)

---

## Anatomy

```
G. │ A. Header (title + edit button)
   │──────────────────────────────
   │ E. Search (optional)
   │──────────────────────────────
   │ B. Destination List
   │  D. ○ Overview
   │  E. ● Work Orders (active)    ← filled icon, tint color
   │
   │  F. Outlined Group: "Assets"  ← collapsible
   │     ○ Machines
   │     ○ Vehicles
   │──────────────────────────────
   │ C. Footer
```

**A. Header** — title + optional Edit button.
**B. Destination List** — navigation items.
**C. Footer** — optional bottom content.
**D. Default Cell** — inactive destination (unfilled icon).
**E. Active Cell** — current screen; filled icon in tint color. **Only one active at a time.**
**F. Outlined Group** — collapsible group of related destinations with a group header + chevron.
**G. Vertical Divider** — separates sidebar from content area.

### Primary Column
Default width: **320pt** (flexible).

### Destination List details
- **Icons** — optional; supplement labels as destination indicators
- **Labels** — keep concise; truncate when too long (never shrink or wrap)
- **Right accessories** — optional numbers or icon buttons. Within an outlined group, don't mix number + icon button or different icon buttons

---

## Behavior

### Selection
Only **one cell active at a time**. First launch defaults to the landing screen (e.g. Overview) as active.

### Outlined Groups (collapsible)
Tapping a group header expands/collapses its destination list. The header shows the group name and a chevron indicator.

### Collapse / Expand sidebar
- **Landscape** — sidebar visible by default; collapse via toggle icon (top left); reopen via edge swipe
- **Portrait** — sidebar opens as an overlay by default; collapse by tapping outside; reopen via edge swipe

### Scrolling
If the destination list exceeds the available height, the sidebar scrolls vertically. On scroll, the sidebar title collapses and stays fixed.

### Edit Mode
Tap "Edit" to enter edit mode:
- Toggle switches to hide/show individual items
- Drag handles to reorder items

---

## SwiftUI Code Examples

### Basic Sidebar with SideBar component
```swift
import FioriSwiftUICore

struct AppSidebarView: View {
    @State private var isEditing = false
    @State private var searchQuery = ""
    @State private var selectedItem: NavItem? = NavItem.overview
    @State private var navItems: [NavItem] = NavItem.allCases

    var body: some View {
        NavigationSplitView {
            SideBar(
                isEditing: $isEditing,
                queryString: $searchQuery,
                data: $navItems,
                selection: $selectedItem,
                title: AttributedString("My App"),
                isUsedInSplitView: true,
                destination: { item in
                    AnyView(destinationView(for: item))
                },
                item: { $item in
                    Label(item.label, systemImage: item.icon)
                }
            )
        } detail: {
            if let item = selectedItem {
                destinationView(for: item)
            } else {
                ContentUnavailableView(
                    "Select a destination",
                    systemImage: "sidebar.left"
                )
            }
        }
    }
}
```

### Native NavigationSplitView sidebar (simpler)
```swift
NavigationSplitView(columnVisibility: $columnVisibility) {
    List(navItems, selection: $selectedItem) { item in
        Label(item.label, systemImage: selectedItem == item
              ? item.iconFilled   // filled = active
              : item.icon)        // unfilled = inactive
            .foregroundStyle(selectedItem == item
                ? Color.preferredColor(.tintColor)
                : Color.preferredColor(.primaryLabel))
    }
    .listStyle(.sidebar)
    .navigationTitle("My App")
    .toolbar {
        ToolbarItem(placement: .primaryAction) {
            EditButton()
        }
    }
} detail: {
    DetailView(item: selectedItem)
}
```

### With outlined (collapsible) group
```swift
List(selection: $selectedItem) {
    // Ungrouped items
    Label("Overview", systemImage: "square.grid.2x2")
        .tag(NavItem.overview)
    Label("Work Orders", systemImage: "wrench.and.screwdriver")
        .tag(NavItem.workOrders)

    // Outlined group
    Section("Assets") {
        Label("Machines", systemImage: "gearshape")
            .tag(NavItem.machines)
        Label("Vehicles", systemImage: "car")
            .tag(NavItem.vehicles)
    }
}
.listStyle(.sidebar)  // sections are collapsible by default in sidebar style
```

### With right accessory (badge count)
```swift
Label {
    HStack {
        Text("Notifications")
        Spacer()
        Text("5")
            .font(.fiori(forTextStyle: .caption2))
            .foregroundStyle(Color.preferredColor(.secondaryLabel))
            .padding(.horizontal, 6)
            .background(Color.preferredColor(.secondaryBackground))
            .clipShape(Capsule())
    }
} icon: {
    Image(systemName: "bell")
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Cell state | Active | Filled icon + `.tintColor` |
| Cell state | Default (inactive) | Unfilled icon + `.primaryLabel` |
| Group | Outlined (collapsible) | `Section {}` with `.listStyle(.sidebar)` |
| Group | Expanded | Default open state |
| Group | Collapsed | Section collapsed |
| Right accessory | Number | Custom `HStack` with badge `Text` |
| Right accessory | Icon button | `FioriButton` in row trailing |
| Edit mode | Yes | `EditButton()` in toolbar |
| Default width | 320pt | `.navigationSplitViewColumnWidth(320)` |
| Visible | Landscape default | `NavigationSplitView` |
| Overlay | Portrait default | Automatic in `NavigationSplitView` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use only on regular width (iPad) — use tab bar on iPhone
- Keep destination labels concise — truncate rather than wrap
- Show only one active cell at a time
- Default the first launch to the landing/overview screen as active
- Within an outlined group, use consistent right accessories (all numbers, or all the same icon — never mixed)
- Provide edit mode when destinations are user-configurable

**Don't:**
- Use on compact width (iPhone) — use tab bar instead
- Mix number badges and icon buttons in the same outlined group
- Shrink or wrap labels that don't fit — truncate them

---

## Related Components

- [tab-bar.md](tab-bar.md) — compact width equivalent (iPhone)
- [navigation-bar.md](navigation-bar.md) — top navigation bar
- [hierarchy-view.md](hierarchy-view.md) — navigating hierarchical data structures
