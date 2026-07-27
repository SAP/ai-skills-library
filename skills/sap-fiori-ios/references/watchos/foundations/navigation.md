# Navigation — SAP Fiori for watchOS

> SAP Fiori for watchOS | Foundation

## What is it?

watchOS navigation must be quick and minimal. Choose hierarchical or page-based navigation for apps with more than one screen. Limit hierarchy to 2–3 levels maximum.

---

## Rules

**Do:**
- Provide clear navigation paths
- Use no more than 2–3 hierarchy levels
- Divide information across multiple screens
- Let users complete important actions without scrolling

**Don't:**
- Use more than 3 hierarchy levels
- Create long scrolling areas

---

## Navigation Types

### Hierarchical Navigation
Parent-child page relationships. Home screen provides relevant actions/information directly. Users drill down by tapping objects or overflow menus. Max 2–3 levels.

```swift
// watchOS NavigationStack
NavigationStack {
    WorkOrderList()
        .navigationTitle("Work Orders")
        .navigationDestination(for: WorkOrder.self) { order in
            WorkOrderDetail(order: order)  // level 2 — keep it here
        }
}
```

### Page-Based (Flat) Navigation
Flat collection of screens navigated by swiping left/right. Best for apps with multiple content categories (not hierarchical relationships). Page count always visible via page control — current page shown as solid dot.

```swift
// watchOS TabView with page style
TabView {
    OrdersView()
    NotificationsView()
    KPIsView()
}
.tabViewStyle(.page)
```

### Back Navigation
Standard "Back" button returns to previous view. Users familiar with it from mobile — consistent behavior expected.

---

## Comparison

| Pattern | Use for |
|---------|---------|
| Hierarchical | Apps with one main content category and parent-child structure |
| Page-based | Apps with multiple independent content categories |

---

## Resources

- [../get-started.md](../get-started.md)
- [Apple HIG: Navigation for watchOS](https://developer.apple.com/design/human-interface-guidelines/navigation)
