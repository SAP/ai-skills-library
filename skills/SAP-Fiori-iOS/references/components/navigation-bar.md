# Navigation Bar — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit` (Navigation page)
> Development reference: UIKit `FUINavigationBar`, SwiftUI `NavigationStack` + `.toolbar {}`

## What is it?

The navigation bar is an integral part of every screen. It indicates the user's position within the app and contains page-level control actions.

---

## When to Use

**Do:**
- Keep title text **≤ 37 characters** (including spaces)
- With title only (no subtitle): title can wrap up to **2 lines**, then truncates
- With title + subtitle: limit title to **≤ 24 characters**; **do not wrap the title** when a subtitle is present
- Use an overflow button or pull-down button when there are too many actions
- Place "Close", "Cancel", and "Back" buttons consistently on the **left side**
- Omit "Back" button text if it is too long — icon only is acceptable
- Prefer **symbol buttons** in compact width; use label buttons only when no suitable icon exists

**Don't:**
- Show more than **3 buttons** on the right in compact width (iPhone)
- Show more than **4 buttons** on the right in regular width (iPad)
- Provide multiple similar actions (e.g. a "Back" and a "Save" that do the same thing)
- Truncate label buttons — use more concise words instead
- Wrap the title when a subtitle is also present

---

## Anatomy

```
A. Left accessory    B. Large Title / C. Title         D. Right accessory
[← Back]             Page Title                         [Edit] [Filter] [+]

E. Search bar (optional, persistent global search)
```

### A. Left Accessory
"Profile" button, "Back" button, or "Cancel". Shows where the user came from and enables back navigation.

### B. Large Title
Large version of the title — visible when the user is at the top of the screen. Hidden when the user scrolls down (default title takes over). Optional.

### C. Title
Page heading. Default (small) title is hidden while large title is visible. Can have an optional subtitle. If very long and truncated, user can **long-press** the title to see the full text in a popover.

### D. Right Accessory
Page-level actions. Max 3 (compact) / 4 (regular). Use overflow menu for additional actions.

### E. Search Bar (optional)
Persistent search field. Used for global search. On iPad, can be inline in the nav bar; on iPhone, always below the nav bar.

---

## Behavior

### Large title → default title on scroll
Large title scrolls out of view as the user scrolls down; the default (small) title appears in the bar.

**With ObjectHeader:** Use the nav bar without an additional title — the object header's title transitions into the nav bar on scroll. Adding a separate nav bar title would create redundancy.

### Long-press back button — history stack
Long-pressing the Back button opens a contextual menu of previously visited pages (breadcrumb stack), allowing the user to jump back multiple levels at once.

> If the app has complex object hierarchies, use a one-time in-product tooltip to announce this feature.

---

## Text vs. Icon buttons

> Use text labels for actions to make them clearer. Omit the label only when the icon is universally known (Add "+", Filter, Share, etc.).

---

## Adaptive Design

| Size class | Max right actions | Behavior |
|-----------|------------------|---------|
| Compact (iPhone) | 3 | Symbol buttons preferred |
| Regular (iPad) | 4 | More actions visible; some toolbar buttons may move here |

On iPad, elements like the avatar button often move from the nav bar to the sidebar, freeing nav bar space for actions.

---

## Variations

### Large Title (optional)
Emphasizes page content and purpose. Use for root/primary screens.

```swift
NavigationStack {
    List { ... }
        .navigationTitle("Invoices")
        .navigationBarTitleDisplayMode(.large)  // default
}
```

### Inline Title (default for pushed screens)
```swift
InvoiceDetailView()
    .navigationTitle("Invoice #1234")
    .navigationBarTitleDisplayMode(.inline)
```

### Title + Subtitle
```swift
// Limit title to ≤24 chars; no line wrapping
.navigationTitle("Sales Order #5678")
// Subtitle via toolbar principal placement
.toolbar {
    ToolbarItem(placement: .principal) {
        VStack(spacing: 2) {
            Text("Sales Order #5678")
                .font(.fiori(forTextStyle: .headline))
            Text("Acme Corporation")
                .font(.fiori(forTextStyle: .footnote))
                .foregroundStyle(Color.preferredColor(.secondaryLabel))
        }
    }
}
```

### Logo on home screen (≤24pt height, max 30pt)
```swift
.toolbar {
    ToolbarItem(placement: .navigationBarLeading) {
        Image("app-logo")
            .resizable()
            .scaledToFit()
            .frame(height: 24)  // max 30pt in exceptional cases
    }
}
```

### Right actions — 3 max on compact
```swift
.toolbar {
    ToolbarItemGroup(placement: .primaryAction) {
        FioriButton { _ in
            Image(systemName: "line.3.horizontal.decrease.circle")
                .accessibilityLabel("Filter")
        }
        .fioriButtonStyle(FioriTertiaryButtonStyle())

        FioriButton { _ in
            Image(systemName: "arrow.up.arrow.down")
                .accessibilityLabel("Sort")
        }
        .fioriButtonStyle(FioriTertiaryButtonStyle())

        FioriButton { _ in
            Image(systemName: "plus")
                .accessibilityLabel("Add invoice")
        }
        .fioriButtonStyle(FioriTertiaryButtonStyle())
    }
}
```

### Overflow menu for additional actions
```swift
.toolbar {
    ToolbarItemGroup(placement: .primaryAction) {
        FioriButton { _ in Image(systemName: "plus").accessibilityLabel("Add") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())

        // Overflow for additional actions
        Menu {
            Button("Export") { exportData() }
            Button("Share") { shareData() }
            Button("Archive") { archiveData() }
        } label: {
            Image(systemName: "ellipsis.circle")
                .accessibilityLabel("More actions")
        }
    }
}
```

### Search field in navigation bar (iPad only)
```swift
// iPad: search inline in nav bar (no large title)
NavigationStack {
    List { ... }
        .navigationTitle("Products")
        .navigationBarTitleDisplayMode(.inline)
        .searchable(text: $searchQuery,
                    placement: .navigationBarDrawer(displayMode: .always))
}

// iPhone: search always below nav bar (never inline)
NavigationStack {
    List { ... }
        .navigationTitle("Products")
        .searchable(text: $searchQuery,
                    placement: .navigationBarDrawer)
}
```

### Cancel / Close on left (consistent placement)
```swift
.toolbar {
    ToolbarItem(placement: .cancellationAction) {
        FioriButton { _ in Text("Cancel") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .onTapGesture { dismiss() }
    }
}
```

### No navigation bar
Some screens provide page info and actions in the content area itself — the nav bar can be hidden:

```swift
.navigationBarHidden(true)
// or
.toolbar(.hidden, for: .navigationBar)
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Title style | Large | `.navigationBarTitleDisplayMode(.large)` |
| Title style | Default / Inline | `.navigationBarTitleDisplayMode(.inline)` |
| Subtitle | Yes | `ToolbarItem(placement: .principal)` with VStack |
| Left | Back | Automatic in `NavigationStack` |
| Left | Cancel / Close | `ToolbarItem(placement: .cancellationAction)` |
| Left | Profile / Logo | `ToolbarItem(placement: .navigationBarLeading)` |
| Right | 1–3 actions (compact) | `ToolbarItemGroup(placement: .primaryAction)` |
| Right | 1–4 actions (regular) | Same — system adapts |
| Right | Overflow | `Menu {}` as last right item |
| Search | Below nav bar (iPhone) | `.searchable(placement: .navigationBarDrawer)` |
| Search | Inline (iPad) | `.searchable(placement: .navigationBarDrawer(displayMode: .always))` |
| Logo | Yes | `ToolbarItem(leading)` — max 24pt height |
| No nav bar | Yes | `.toolbar(.hidden, for: .navigationBar)` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Keep title ≤37 characters (≤24 with subtitle)
- Consistently place Cancel/Close/Back on the left
- Use symbol buttons in compact; text buttons when no clear icon exists
- Overflow additional actions into a Menu when limit is reached
- Hide the nav bar title when using ObjectHeader (prevents redundant titles on scroll)
- Note max logo height: 24pt standard, 30pt exceptional maximum

**Don't:**
- Show >3 buttons right side on iPhone or >4 on iPad
- Truncate label buttons — rewrite to be more concise
- Wrap the title when a subtitle is present
- Duplicate actions that do the same thing

---

## Related Components

- [buttons.md](buttons.md) — button styles for toolbar actions
- [sidebar.md](sidebar.md) — iPad navigation elements that move off the nav bar
- [object-header.md](object-header.md) — nav bar interaction with scrolling object headers
