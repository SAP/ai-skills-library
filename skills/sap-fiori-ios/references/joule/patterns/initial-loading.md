# Initial Loading — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns

## What is it?

Shows while Joule loads, allowing users to begin typing their query immediately — reducing perceived wait time. Input cannot be sent until loading completes.

---

## When to Show

- First time Joule opens (cold start → welcome screen)
- Switching between conversations
- Creating a new conversation

---

## Rules

**Don't** change the input field variant during initial loading — the loading variant must be used (messages can't be sent yet).

---

## Anatomy

**A. Joule logo illustration** — floating animated icon indicating processing
**B. Joule header** — minimize/close panel controls
**C. Input field** — loading variant; user can type but cannot send
**D. AI notice** — persistent disclaimer

---

## Transition Behavior

| Scenario | After loading completes |
|----------|------------------------|
| Cold start | Transitions to welcome screen |
| Warm start (returning user) | Transitions to last selected conversation |
| New conversation | Transitions to welcome screen |
| Switch conversations | Transitions to newly selected conversation |
| Close + reopen during typing | Query preserved in input field |

---

## Error State

If loading fails → processing error message with reload option.

---

## Related

- [../components/joule-panel.md](../components/joule-panel.md)
- [welcome-screen.md](welcome-screen.md)
- [conversations-list.md](conversations-list.md)
