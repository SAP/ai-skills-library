# Attachment by Prompt — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns

## What is it?

Joule-initiated attachment flow — lets users upload documents **when Joule requests it**. Only Joule can initiate this flow; do not use for user-initiated uploads (use [persistent-attachment.md](persistent-attachment.md) instead).

---

## Rules

**Do:** Use when Joule prompts the user to upload a document.
**Don't:** Use for user-initiated file upload.

**Tips:**
- No overlay behind the attachment sheet — user must be able to read Joule's prompt
- Display sent attachments in a user text message bubble-style container
- Use icons as file thumbnails

---

## Anatomy

### Attachment Sheet
**A. Navigation Bar** — label + Close (✕) + Submit (disabled until file uploaded)
**B. Attachment Form Cell** — "Add (+)" button to upload files

### Sent Attachment Bubble
**A. Bubble** — user text message style container
**B. Attachment Form Cell** — list of object cells: icon thumbnail + file name + Download icon; tap to view

---

## Behavior

- Upload: tap "Add (+)" → file uploads → shown in scrollable grid
- Submit: tap "Submit" → attachments appear in conversation as sent bubble
- Attachment sheet height must not exceed panel height

### Error States
- **Upload error** — inline error for unsupported format or file >10MB
- **Loading error** — illustrated message when attachment flow disrupted or sent attachments fail to load

---

## Related

- [persistent-attachment.md](persistent-attachment.md)
- [../../components/attachment-form-cell.md](../../components/attachment-form-cell.md)
