# Navigation — Pattern Guide

> SAP Fiori for iOS | Patterns
> Related components: Navigation Bar, Sidebar, Sibling Navigation, Tab Bar

## What is it?

Navigation style determines how users move through an app's content. Choose the style based on the app's content structure to provide the clearest and most efficient experience.

---

## Navigation Styles

### Hierarchical Navigation
Suitable for apps based on a **single content category**. Users start at an overview screen and drill down into subcategories step by step.

- Can only go back and forth step-by-step
- Overview screen provides high-level summary of the entire app
- Use modals to prevent endless loops when at deeper navigation levels

```swift
NavigationStack {
    OverviewView()               // root
        .navigationDestination(for: Category.self) { category in
            CategoryListView(category: category)     // level 2
                .navigationDestination(for: Item.self) { item in
                    ItemDetailView(item: item)       // level 3
                }
        }
}
```

**Preventing endless loops:** When a user is deep in a hierarchy and would otherwise create a circular navigation path, present the content in a modal instead of pushing to a new screen.

### Flat Navigation
Suitable for apps with **multiple content categories**. Uses a tab bar where each tab represents one content category. Within each tab, users drill down hierarchically.

- Optional search tab for global search
- Profile and settings: place in the nav bar (right side), accessible from every tab
- If profile is frequently viewed, give it its own tab

```swift
TabView(selection: $selectedTab) {
    NavigationStack { InvoicesView() }
        .tabItem { Label("Invoices", systemImage: "doc.text") }
        .tag(Tab.invoices)

    NavigationStack { OrdersView() }
        .tabItem { Label("Orders", systemImage: "cart") }
        .tag(Tab.orders)

    NavigationStack { ProfileView() }
        .tabItem { Label("Profile", systemImage: "person.circle") }
        .tag(Tab.profile)
}
```

---

## Profile Placement

| Access frequency | Placement |
|-----------------|-----------|
| Standard | Right side of navigation bar, accessible from every tab |
| Frequently viewed (e.g. progress tracking) | Own dedicated tab |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Evaluate content structure first, then choose navigation style
- Keep hierarchical navigation linear — back and forth step by step
- Use modals at deep levels to prevent circular navigation
- Make profile/settings accessible from every screen

**Don't:**
- Use hierarchical navigation for multi-category apps — use flat (tab bar)
- Hide profile deep in a menu if users need it frequently
- Mix navigation styles inconsistently within the same app

---

## Related Components

- [../components/navigation-bar.md](../components/navigation-bar.md)
- [../components/sidebar.md](../components/sidebar.md)
- [../components/tab-bar.md](../components/tab-bar.md)
- [../components/sibling-navigation.md](../components/sibling-navigation.md)
