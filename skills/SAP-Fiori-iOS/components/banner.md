# Banner — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Feedback
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit` (Notifications page)
> Development reference: UIKit `FUIBannerMessageView`, `FUIOfflineBannerMessageView`, `FUIProgressBannerMessageView`, `FUIBannerMultiMessageViewController`, SwiftUI `BannerMessage`, `BannerMultiMessageSheet`

## What is it?

A banner is a notification that informs users about an event or a change in system status. It contains a short notification text and optionally a button for a recommended action. Banners are **system-level** — not for component-level messages.

---

## When to Use

**Do:**
- Inform users about a system event or status change within **two lines of text**

**Don't:**
- Use a banner to show component-level messages (form field errors, card errors — handle those inline)
- Write text that extends beyond two lines

**Top tips:**
- Keep banner text short and concise
- Ensure the user can still interact with the app — the banner must not cover critical content

---

## Anatomy

```
[E. Indicator Track — semantic color]
┌────────────────────────────────────────┐
│ [B. Icon]  A. Banner text   [C.Close] │
│            [D. Action button]          │
└────────────────────────────────────────┘
```

**A. Banner Text** — clear message, optionally includes a recommended action. Max two lines.

**B. Icon** (optional) — indicates sync-in-progress status.

**C. Close Button** (optional) — allows the user to dismiss the banner.

**D. Action Button** (optional) — enables a recommended action.

**E. Indicator Track** (optional) — appears **above** the banner in a semantic color to indicate progress or banner type.

---

## Position

### Overlapping (default)
Banner slides down from under the navigation bar or header component. Partially covers content below. Disappears by sliding back up.

```swift
// Banner appears below nav bar, overlapping content
VStack(spacing: 0) {
    NavigationStack {
        ZStack(alignment: .top) {
            ContentView()

            if showBanner {
                BannerMessage {
                    Text("Sync failed. Check your connection.")
                } closeAction: {
                    showBanner = false
                }
                .transition(.move(edge: .top).combined(with: .opacity))
                .animation(.easeInOut(duration: 0.25), value: showBanner)
            }
        }
    }
}
```

### Embedded
Banner appears **between** elements — pushes content below it down, covers nothing.

```swift
VStack(spacing: 0) {
    NavigationHeaderView()

    if showBanner {
        BannerMessage {
            Text("You are working offline.")
        }
        // Pushes list content down
    }

    List { ... }
}
```

### Scrolling behavior
The banner **sticks to the navigation bar** as the user scrolls. If a header component sits between the nav bar and the banner, the banner sticks to the nav bar once the header scrolls out of view. Content hidden underneath the overlapping banner may reveal itself when the user scrolls to the top.

---

## Variations

### Persistent Banner (default)
Remains visible until the system condition changes. Can be configured to auto-dismiss after a timer or to show a "Close" button.

```swift
@State private var showBanner = true

if showBanner {
    BannerMessage {
        Text("You are working in read-only mode.")
    } icon: {
        Image(systemName: "lock.fill")
            .foregroundStyle(Color.preferredColor(.criticalLabel))
    } closeAction: {
        showBanner = false  // dismissible variant
    }
}
```

### Error State Banner
Notifies the user that a workflow is disrupted. Dismissed via the "Close" button.

```swift
BannerMessage {
    Text("Connection lost. Some data may be outdated.")
} icon: {
    Image(systemName: "exclamationmark.triangle.fill")
        .foregroundStyle(Color.preferredColor(.negativeLabel))
} closeAction: {
    showErrorBanner = false
}
```

### Offline State Banner
Used when the app goes offline. Can auto-dismiss after a few seconds or remain persistent.

```swift
// Auto-dismissing offline banner
.onReceive(networkMonitor.$isConnected) { isConnected in
    if !isConnected {
        showOfflineBanner = true
    } else if showOfflineBanner {
        // Auto-dismiss after reconnect
        DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
            withAnimation { showOfflineBanner = false }
        }
    }
}

if showOfflineBanner {
    BannerMessage {
        Text(networkMonitor.isConnected ? "Back online" : "You are offline.")
    } icon: {
        Image(systemName: networkMonitor.isConnected ? "wifi" : "wifi.slash")
            .foregroundStyle(Color.preferredColor(
                networkMonitor.isConnected ? .positiveLabel : .secondaryLabel
            ))
    }
    .transition(.move(edge: .top).combined(with: .opacity))
    .animation(.easeInOut(duration: 0.25), value: showOfflineBanner)
}
```

### Progress / Sync Banner
Indicates a loading or in-progress state. A spinning icon shows sync is active. Replace text with "Sync completed" when done. Allow users to cancel or close.

```swift
// Sync banner with cancel action
BannerMessage {
    Text(syncState == .syncing ? "Syncing data…" : "Sync completed")
} icon: {
    if syncState == .syncing {
        ProgressView()
            .tint(Color.preferredColor(.tintColor))
    } else {
        Image(systemName: "checkmark.circle.fill")
            .foregroundStyle(Color.preferredColor(.positiveLabel))
    }
} closeAction: {
    syncState = .idle
    showSyncBanner = false
} action: {
    if syncState == .syncing {
        FioriButton { _ in Text("Cancel") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .onTapGesture { cancelSync() }
    }
}
```

### Multi-Message Banner
When a screen has multiple messages, the banner shows a summary (type + count) with an action link that opens a detail view:
- **Compact** — opens in a bottom sheet (`BannerMultiMessageSheet`)
- **Regular** — opens in a popover

```swift
import FioriSwiftUICore

@State private var showMultiMessageSheet = false

BannerMessage {
    Text("3 messages require attention")
} action: {
    FioriButton { _ in Text("View All") }
        .fioriButtonStyle(FioriTertiaryButtonStyle())
        .onTapGesture { showMultiMessageSheet = true }
}
.sheet(isPresented: $showMultiMessageSheet) {
    BannerMultiMessageSheet(messages: systemMessages)
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Type | Error | Icon: `.negativeLabel`, indicator track: `.negativeLabel` |
| Type | Offline | Icon: wifi.slash, `FUIOfflineBannerMessageView` |
| Type | Sync / Progress | Spinning icon, `FUIProgressBannerMessageView` |
| Type | Informational | Icon: `.informativeLabel` |
| Position | Overlapping | `ZStack(alignment: .top)` |
| Position | Embedded | `VStack` — banner pushes content down |
| Dismissible | Yes | `closeAction: {}` |
| Dismissible | No | Omit `closeAction` |
| Action | Yes | `action: { FioriButton {} }` |
| Multi-message | Yes | `BannerMultiMessageSheet` / popover |
| Indicator track | Yes | Configured via `indicatorColor` parameter |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Keep text to **two lines maximum**
- Let the user interact with the app while the banner is visible
- Auto-dismiss offline banners after reconnection (with a short delay)
- Replace sync text with "Sync completed" when the sync finishes
- Always provide a Cancel or Close option on sync banners
- Use multi-message handling when multiple banners would stack

**Don't:**
- Use banners for component-level feedback (form validation, card errors)
- Write long banner text — truncate or rewrite to fit two lines
- Stack multiple banners — use multi-message handling instead
- Cover interactive controls with the banner in overlapping mode

---

## Related Components

- [illustrated-message.md](illustrated-message.md) — full empty/error screen states
- [loading-indicator.md](loading-indicator.md) — progress indicators
- [forms.md](forms.md) — inline field-level error handling
