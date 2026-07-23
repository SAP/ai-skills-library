# Conversations List — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns

## What is it?

Multi-threading panel showing all saved conversation histories. Users can search, sort, switch, rename, delete, and create conversations.

---

## Anatomy

**A. Panel** — bottom sheet overview of all conversations
**B. Panel Header** — title + close (✕)
**C. Active Conversations Section** — collapsible; title + count + thread items
**D. Active Conversation** — individual active thread
**E. Expired Conversations Section** — collapsible; title + count + thread items
**F. Expired Conversation** — individual past thread
**G. Sort Action** — reorders list
**H. Search Bar** — filter threads by keyword; highlights matches dynamically
**I. "New Conversation" button** (+) — starts a new conversation

---

## States

| State | Description |
|-------|-------------|
| Selected | Most recently selected conversation |
| Unselected | Not currently selected |
| Default | ≤9 active conversations |
| Full | 10 active conversations |

---

## Key Behaviors

**Conversation title:** Auto-named "New Conversation" on creation; updated automatically once Joule responds.

**Active conversations:** Expand by default (resets on restart). **Expired conversations:** Collapsed by default (persistent across restarts).

**Conversation limit:** When limit reached, "New Conversation" button disabled; "New Conversation" option removed from overflow menu.

**Expired conversations:** Auto-deleted after predefined duration. Reopening shows error with "New Conversation" button (disabled if limit reached).

**Reopening Joule:** Returns to last open conversation (not the conversations list).

### Actions per conversation

| Action | How to trigger |
|--------|---------------|
| Open | Tap conversation |
| Create | "+" button or overflow "New Conversation" |
| Rename | Long-press → context menu, or swipe gesture, or overflow "Rename Conversation" |
| Delete | Long-press → context menu, or swipe gesture, or overflow "Delete Conversation" |

Rename and Delete both show a confirmation dialog. Delete from thread navigates to welcome screen (or conversations list if limit reached).

---

## Related

- [../components/joule-panel.md](../components/joule-panel.md)
- [initial-loading.md](initial-loading.md)
- [welcome-screen.md](welcome-screen.md)
