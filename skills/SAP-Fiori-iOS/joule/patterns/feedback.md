# Feedback — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns

## What is it?

Users provide positive or negative feedback on Joule's AI-generated responses via thumbs up/down in the response action bar. Always provide — even if unavailable (show error state, not hidden controls).

---

## Rules

**Don't remove** feedback thumbs even when unavailable — error states establish consistent mental model. Don't change style or placement.

---

## Anatomy

### Thumb Buttons (in response action bar)
**A. Thumbs Up** — positive feedback
**B. Thumbs Down** — opens feedback selection view

### Feedback Selection View (bottom sheet)
**A. Nav bar** — Close (✕) + title + Submit button
**B. Feedback categories** — single-select chips; "Not specified" always last, selected by default
**C. Text input** — optional free text

---

## Behavior

**Positive:** Tap 👍 → immediate submission → toast confirms.

**Negative:** Tap 👎 → feedback selection sheet opens → select category (required) + optional text → tap Submit → toast confirms.

**Change of mind:** In negative sheet → tap 👍 → positive recorded instead.

**Cancel negative:** Tap Close (✕) or tap outside sheet → not submitted. Any category selection or text entered is **saved** for if user reopens the sheet.

---

## Error States

| Error | Trigger | What happens |
|-------|---------|-------------|
| Retrieval error | Feedback feature or categories can't be loaded | Toast message: "Feedback unavailable" when user taps thumbs |
| Submission error | User opened sheet but submit fails | Illustrated message in sheet: feedback saved but not submitted; try again later |

---

## Adaptive Design

- Compact: bottom sheet (height adjusts to content; may extend behind Submit footer on small screens)
- Regular: fills panel width

---

## Related

- [../components/response-actions.md](../components/response-actions.md)
- [../components/text-messages.md](../components/text-messages.md)
- [../../components/toast-message.md](../../components/toast-message.md)
