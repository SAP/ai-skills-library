# Persistent Attachment — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns

## What is it?

User-initiated file upload in Joule conversations. Users can attach a single file to provide context alongside their prompt.

**Do not** use for Joule-prompted attachment — use [attachment-by-prompt.md](attachment-by-prompt.md) instead.

---

## Rules / Tips

- Users can only upload **one file at a time**
- Disable "+" and "@" buttons when an attachment is active
- Display sent attachments in the user text message container
- Use the attachment chip to indicate the current file context
- Use icons as file thumbnails
- "Send" remains disabled until a text message is also entered

---

## Anatomy

### Input Field with Attachment
**A. "+" button** — opens attachment/mode selector
**B. Input field** — attachment shown above text area until sent
**C. Attachment chip** — shows uploaded file; tap ✕ to remove
**D. Text area** — prompt alongside attachment
**E. Send button** — disabled until text is present

### Sent Attachment Bubble
**A. Bubble** — user message style container
**B. Attachment** — object cell: icon + file name + download icon; tap to view, download icon to download
**C. Text message** — prompt displayed below attachment

---

## Behavior

- Upload: tap "+" → select file → file uploads → shown as chip in input field
- Submit: write prompt + tap Send → bubble appears with attachment + text
- After submission: Joule answers based on that file; context anchors to latest upload
- Remove focus: tap the attachment chip → removes context anchor; re-enables "@" and "+"

### States
| State | Description |
|-------|-------------|
| Default | File uploaded successfully; ✕ removes it |
| Uploading | Progress feedback shown |
| Error | Error message below file name; remove to upload another |

---

## Priority / Chip Rules

- Attachment chip has highest priority — overrides thinking mode and agent chips
- While attachment chip is active: "+" and "@" are disabled
- Max one chip at a time

---

## Related

- [attachment-by-prompt.md](attachment-by-prompt.md)
- [modes.md](modes.md)
