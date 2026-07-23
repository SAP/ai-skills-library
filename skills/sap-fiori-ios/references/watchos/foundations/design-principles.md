# Design Principles — SAP Fiori for watchOS

> SAP Fiori for watchOS | Foundation

## Wearables vs. Mobile

Watch apps are fundamentally different from mobile apps:

| Aspect | Mobile | Watch |
|--------|--------|-------|
| Device role | Standalone, app-focused | Companion, device-focused |
| Experience | End-to-end app | Selective, focused features |
| Usage | Active interaction | Mostly passive (85%) |
| Session length | Minutes | Seconds |

**Watch usage breakdown:**
- **85%** passive (sensors, background activity)
- **10%** glancing (notifications, complications)
- **5%** performing actions (timers, approvals)

---

## Do's / Don'ts

**Do:**
- Focus on single actions and relevant information
- Use one-tap interactions
- Minimize app hierarchies
- Leverage favourites/recents to infer user-relevant content

**Don't:**
- Translate mobile app capabilities directly to watch
- Apply mobile information architecture to watch
- Assume the mobile mental model applies to watch

> Design for the **smallest model** first to minimize future rework.

---

## watchOS vs. Wear OS Key Differences

| Feature | watchOS (Apple) | Wear OS (Google) |
|---------|----------------|-----------------|
| Tiles | Dock cards (similar to tiles) | Full tile support |
| Back navigation | Back button or hardware button | Swipe right or hardware button |
| Text layout | Mostly left-aligned | Mostly centered |
| Icon buttons | Uncommon | Very common |
| Text resizing | Cannot be deactivated | Can be deactivated |
| Display | Square only | Round, square, rectangular |
| Handover | Not default | Default feature |

---

## Six Design Principles

### 1. Focus on Critical Information and Tasks
Pick 1–2 most important mobile features for the watch. Consider: user context, hands-free needs, changing environment. Show system status and progress for multi-task workflows.

### 2. Enable Quick and Informed Actions
Actions must complete in **< 5 seconds** — otherwise users switch to phone. One primary action per screen. Use smart defaults (surface most-used options first). Use button hierarchy to distinguish primary from secondary/destructive actions. Add confirmation or loading screens for destructive actions.

### 3. Show Timely and Relevant Notifications
Rich notifications mirrored from phone (customizable). Keep notification text short and critical-information-focused. For non-destructive routine actions, include notification actions. Only notify when timely and relevant.

### 4. Provide Device Transitions
Watch is a companion to mobile — not standalone. Always allow users to continue interactions on their phone. Offer seamless handover (e.g., open notification details on phone, configure KPIs via phone settings).

### 5. Leverage Watch Interactions
Use native touch gestures (scroll, tap, swipe right = back). Enable haptics for states (success/failure) and actions (start/stop). Avoid text input — use predefined answers or voice input as fallback (text input > 5 seconds → users switch to phone).

### 6. Include Privacy and Security Features
Inform users about data collection. Only access data essential to current context. Avoid personal/sensitive data in notifications. Allow users to configure how sensitive data appears on watch.
