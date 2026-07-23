# Detail View — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns

## What is it?

An in-depth view of a single object's attributes, triggered when tapping an object card or list card item (when detail view is enabled). Panel transitions to detail view; "Back" returns to conversation.

---

## Rules

**Do:** Use to display additional information that would take too much space in the original view.
**Don't:** Show unrelated details — only information for the specific object.

**Tips:**
- Section out content for clarity
- Don't hide vital information only in detail view — show it in the original view too

---

## Anatomy

**A. Joule Panel** — unique panel view
**B. Panel Header** — "Back" button replaces Joule logo; unnecessary right accessories removed
**C. Header** — title + optionally: subtitle, description, status
**D. Body** — optional section header + up to 5 key/value pairs; values can be plain text or actionable links
**E. Footer** (optional) — up to 3 action buttons

---

## Trigger

Enabled via `detailView` property on Object Card or List Card. Tap card/list item → panel slides to detail view. Tap "Back" → returns to conversation.

---

## Related

- [../components/object-card.md](../components/object-card.md)
- [../components/list-card.md](../components/list-card.md)
- [../components/illustrated-message.md](../components/illustrated-message.md)
