# Offline — Component Guidelines

> SAP Fiori for iOS | Category: Pattern Overview
> Development reference: UIKit `FUIOfflineBannerMessageView`
> See also [banner.md](banner.md) for BannerMessage implementation.

## What is it?

Mobile apps don't always have network connectivity. Offline-enabled SAP Fiori apps should regularly sync with the server and provide a manual sync option for situations where connectivity is critical.

---

## Sync Button Placement

Location depends on how often the user needs to sync:

| Sync frequency | Placement |
|----------------|----------|
| Infrequent | Profile or settings menu (sync form cell button) |
| Regular / frequent | Global action — overview screen (hierarchical nav) or first screen of every tab (flat nav) |

```swift
// Sync in navigation bar (regular access)
.toolbar {
    ToolbarItem(placement: .primaryAction) {
        FioriButton { _ in
            Image(systemName: isSyncing ? "arrow.triangle.2.circlepath" : "arrow.clockwise")
                .symbolEffect(.rotate, isActive: isSyncing)
                .accessibilityLabel(isSyncing ? "Syncing" : "Sync")
        }
        .fioriButtonStyle(FioriTertiaryButtonStyle())
        .onTapGesture { triggerSync() }
    }
}

// Sync in settings (infrequent access)
Section("Data") {
    FioriButton { _ in
        HStack {
            Text("Sync Now")
            Spacer()
            if isSyncing {
                ProgressView()
                    .tint(Color.preferredColor(.tintColor))
            }
        }
    }
    .fioriButtonStyle(FioriTertiaryButtonStyle())
    .frame(maxWidth: .infinity, alignment: .leading)

    if let lastSync = lastSyncDate {
        Text("Last synced: \(lastSync, style: .relative) ago")
            .font(.fiori(forTextStyle: .footnote))
            .foregroundStyle(Color.preferredColor(.tertiaryLabel))
    }
}
```

---

## Offline Feedback Signals

Multiple feedback mechanisms communicate connectivity state simultaneously:

### 1. Status Bar
Changes color in offline mode — visible on every screen, constant indicator.

```swift
// Apply tint to status bar area in offline mode
.background(
    isOffline
        ? Color.preferredColor(.criticalLabel).opacity(0.15)
        : Color.clear
)
```

### 2. Sync Button — Spinning Icon
While syncing, the sync button shows a spinning icon.

```swift
Image(systemName: "arrow.triangle.2.circlepath")
    .symbolEffect(.rotate.byLayer, isActive: isSyncing)
    .foregroundStyle(isSyncing
        ? Color.preferredColor(.tintColor)
        : Color.preferredColor(.secondaryLabel))
```

### 3. Timestamp
After sync completes, the timestamp updates to reflect the last sync time.

```swift
VStack(spacing: 2) {
    Image(systemName: "arrow.clockwise")
    if let lastSync = lastSyncDate {
        Text(lastSync, style: .relative)
            .font(.fiori(forTextStyle: .caption2))
            .foregroundStyle(Color.preferredColor(.tertiaryLabel))
    }
}
```

### 4. Syncing Indicator Under Header
When the user navigates away during sync, a syncing indicator appears under the header.

```swift
if isSyncing {
    LinearProgressIndicator(
        indicatorColor: Color.preferredColor(.tintColor),
        progress: nil  // indeterminate while syncing
    )
    .frame(height: 2)
}
```

### 5. Banners

**Offline banner** — shown when app goes offline. Can auto-dismiss or be persistent.

```swift
// Auto-dismissing offline banner
.onReceive(networkMonitor.$isConnected) { isConnected in
    if !isConnected {
        showOfflineBanner = true
    } else {
        DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
            withAnimation { showOfflineBanner = false }
        }
    }
}

if showOfflineBanner {
    BannerMessage {
        Text(networkMonitor.isConnected
             ? "Back online"
             : "You are offline. Changes will sync when connected.")
    } icon: {
        Image(systemName: networkMonitor.isConnected ? "wifi" : "wifi.slash")
            .foregroundStyle(Color.preferredColor(
                networkMonitor.isConnected ? .positiveLabel : .secondaryLabel))
    }
}
```

**Sync banner** — shown while a user-triggered sync is in progress. Must include Cancel or Close. Replace text with "Sync Completed" when done.

```swift
if showSyncBanner {
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
        if syncState == .syncing { cancelSync() }
        showSyncBanner = false
    } action: {
        if syncState == .syncing {
            FioriButton { _ in Text("Cancel Sync") }
                .fioriButtonStyle(FioriTertiaryButtonStyle())
                .onTapGesture { cancelSync(); showSyncBanner = false }
        }
    }
}
```

---

## Offline Feedback Priority

Apply multiple signals at once — users may be on any screen when connectivity changes:

| Signal | Scope | Always visible |
|--------|-------|----------------|
| Status bar color change | Every screen | ✓ |
| Offline banner | Current screen | Until dismissed |
| Sync button spinning | Navigation bar | While syncing |
| Timestamp update | Near sync button | After sync |
| Syncing indicator under header | Current screen | While syncing |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Provide both automatic and manual sync
- Show the "Sync Completed" message after a user-triggered sync finishes
- Always provide Cancel or Close on sync banners
- Surface the sync button globally when users sync frequently
- Change the status bar to indicate offline mode on every screen

**Don't:**
- Only use one feedback signal — combine them for reliability
- Leave users without a way to cancel a running sync
- Hide the sync button deep in settings when users need it regularly

---

## Related Components

- [banner.md](banner.md) — offline and sync banner implementation
- [activity-indicator.md](activity-indicator.md) — loading/syncing indicators
- [navigation-bar.md](navigation-bar.md) — sync button placement in nav bar
