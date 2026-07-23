# Welcome Screen — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns

## What is it?

The welcome screen greets users when Joule opens for the first time, when a conversation restarts, or when a new conversation is created. Opens with keyboard active.

---

## Rules

**Do:**
- Show Joule illustration and greeting on open/new conversation
- Auto-open keyboard on load
- Use short, conversational, time-of-day-relevant greeting (1–2 lines)

**Don't:**
- Drop the persistent AI notice
- Update input field placeholder without Joule UX team approval
- Create variations of required visual/textual content — must stay consistent

---

## Anatomy

**A. Joule Header** — title "Joule" + menu button (conversations list) + Close (✕) + overflow (•••)
**B. Joule icon illustration** — animated branding element below header
**C. Welcome message** — streaming animation as Joule loads; varies by time zone
**D. Input field** — keyboard opens automatically
**E. Persistent AI notice** — always visible disclaimer; full content in overflow menu

---

## Behavior

- Opens in **full panel size** (via entry point)
- User can swipe down for medium-size view
- After first message sent: illustration and welcome message disappear; timestamp appears
- Keyboard opens automatically on load

---

## Variations

| Variant | Description |
|---------|-------------|
| Full-size (default) | Used when welcome screen loads |
| Medium-size | User swiped down from full-size |

---

## Related

- [entry-point.md](entry-point.md)
- [initial-loading.md](initial-loading.md)
- [conversations-list.md](conversations-list.md)
- [../components/joule-panel.md](../components/joule-panel.md)
- [ai-notice.md](ai-notice.md)
