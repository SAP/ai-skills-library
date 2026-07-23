# Tab Bar — Component Guidelines

> SAP Fiori for iOS | Category: M3 Standard (adapted)
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit` (Navigation page)
> Development reference: UIKit `UITabBar`

## What is it?

The tab bar (tab view) is a navigation element at the bottom of a screen. It uses tab items to navigate between mutually exclusive, same-level content panes. Use it for navigation only — not for actions on the current view (use a toolbar for that).

**On iPad, consider using a sidebar instead.** The sidebar accommodates more items and makes navigation more efficient.

---

## When to Use

**Do:**
- Keep tab labels ≤ **25 characters** (including spaces)
- Use concrete nouns or verbs as labels (e.g. "Home", "Orders", "Profile")
- Use a "More" tab as overflow when iPhone needs more than **5** items or iPad needs more than **6**
- Use icon-only tabs only for universally recognized icons (store, search, basket, profile)
- Use **filled icon** for active tab, **unfilled icon** for inactive tabs

**Don't:**
- Mix tabs with labels and icon-only tabs in the same bar
- Use more than **5** items in compact width or **6** in regular width
- Remove a tab when its content is unavailable — keep it, explain why it's unavailable instead

---

## Anatomy

```
────────────────────────────────────────── ← tab bar container (A)
 [B.icon+E.badge] [B.icon] [B.icon] [B.icon]
  F. Active label  label    label    label
    (C. tint)    (D. unfilled)
```

**A. Tab Bar Container** — always visible, even when navigating within a tab. Translucent with blur effect by default. Full screen width; tabs equally distributed.

**B. Tab Icon** — portrait: icon above label; landscape: icon and label side by side.

**C. Active Tab** — filled icon variant in **tint color**.

**D. Inactive Tabs** — unfilled icon variant.

**E. Notification Badge** — red badge on the tab icon; can show a number count.

**F. Tab Label** — short, concise text. Omit only if icon is universally understood.

---

## Behavior

- Tap inactive tab → activates tab → navigates to that content
- Tab bar **stays fixed** at the bottom even when content scrolls
- Tab bar **hides when the keyboard appears**
- Default appearance: translucent with blur (retains context of background content)
- **Haptic feedback** on tab selection (selection feedback) and on incoming notification (notification feedback) — system-controlled, not configurable

### "More" Tab
When items exceed the limit, the last tab becomes "More", opening a list of remaining items on a separate screen. Limit use — content hidden in "More" is easy to overlook.

---

## Adaptive Design

- Follows global layout margins for each size class
- Compact: max **5** tabs; Regular: max **6** tabs
- On iPad, consider switching to a `SideBar` for apps with many destinations

---

## SwiftUI Code Examples

### Standard tab view
```swift
import FioriSwiftUICore

enum Tab { case overview, orders, notifications, profile }

@State private var selectedTab: Tab = .overview

TabView(selection: $selectedTab) {
    NavigationStack { OverviewView() }
        .tabItem {
            Label("Overview", systemImage: selectedTab == .overview
                  ? "square.grid.2x2.fill"  // filled = active
                  : "square.grid.2x2")
        }
        .tag(Tab.overview)

    NavigationStack { OrdersView() }
        .tabItem {
            Label("Orders", systemImage: selectedTab == .orders
                  ? "cart.fill" : "cart")
        }
        .tag(Tab.orders)

    NavigationStack { NotificationsView() }
        .tabItem {
            Label("Alerts", systemImage: selectedTab == .notifications
                  ? "bell.fill" : "bell")
        }
        .badge(unreadCount)  // notification badge
        .tag(Tab.notifications)

    NavigationStack { ProfileView() }
        .tabItem {
            Label("Profile", systemImage: selectedTab == .profile
                  ? "person.circle.fill" : "person.circle")
        }
        .tag(Tab.profile)
}
.tint(Color.preferredColor(.tintColor))  // active tab color
```

### Icon-only tabs (universally recognized icons)
```swift
TabView {
    SearchView()
        .tabItem { Image(systemName: "magnifyingglass").accessibilityLabel("Search") }
    BasketView()
        .tabItem { Image(systemName: "basket.fill").accessibilityLabel("Basket") }
    ProfileView()
        .tabItem { Image(systemName: "person.circle.fill").accessibilityLabel("Profile") }
}
.tint(Color.preferredColor(.tintColor))
```

### iPad adaptive (tab → sidebar on regular width)
```swift
// iOS 18+ — adapts automatically
TabView {
    Tab("Overview", systemImage: "square.grid.2x2") {
        NavigationStack { OverviewView() }
    }
    Tab("Orders", systemImage: "cart") {
        NavigationStack { OrdersView() }
    }
    Tab("Assets", systemImage: "gearshape") {
        NavigationStack { AssetsView() }
    }
}
.tabViewStyle(.sidebarAdaptable)  // sidebar on iPad, tab bar on iPhone
.tint(Color.preferredColor(.tintColor))
```

### Unavailable tab (keep it, explain why)
```swift
NavigationStack { UnavailableView(reason: "Requires manager access") }
    .tabItem { Label("Reports", systemImage: "chart.bar") }
    // Tab is present but shows explanation — do not remove it
```

### Notification badge
```swift
.badge(unreadCount)          // numeric badge
.badge("•")                  // dot badge (new content)
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Tab count | 2–5 (compact) | `TabView` with 2–5 `.tabItem {}` |
| Tab count | 2–6 (regular) | Same — adapts automatically |
| Tab icon | Active (filled) | `systemImage: "cart.fill"` |
| Tab icon | Inactive (unfilled) | `systemImage: "cart"` |
| Label | Yes | `Label("Title", systemImage:)` |
| Label | Omitted (icon only) | `Image(systemName:).accessibilityLabel(...)` |
| Badge | Number | `.badge(count)` |
| Badge | Dot | `.badge("•")` |
| Active color | Tint | `.tint(Color.preferredColor(.tintColor))` |
| Adaptive (iPad) | Sidebar | `.tabViewStyle(.sidebarAdaptable)` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Wrap each tab's content in its own `NavigationStack` to preserve per-tab navigation state
- Apply `.tint(Color.preferredColor(.tintColor))` for correct Fiori active-tab color
- Use filled icon for active, unfilled for inactive
- Keep labels ≤25 characters
- Use `.sidebarAdaptable` on iPad (iOS 18+)
- Keep unavailable tabs visible with an explanation

**Don't:**
- Mix labeled and icon-only tabs in the same bar
- Exceed 5 tabs (compact) or 6 tabs (regular)
- Reset navigation state when switching tabs
- Use the tab bar for actions — use a toolbar instead

---

## Related Components

- [sidebar.md](sidebar.md) — iPad navigation alternative for apps with many destinations
- [navigation-bar.md](navigation-bar.md) — top-level navigation bar
