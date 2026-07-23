# Dictation — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns

## What is it?

Voice-to-text input for Joule. Captures and transcribes speech in real-time. Transcribed text persists in input field after stopping — user can edit before sending.

---

## Rules

**Do:** Request microphone access from first-time users. Keep keyboard visible. Provide listening feedback. Enable editing after dictation.
**Don't:** Hide listening/processing status. Hide stop action. Auto-submit or overwrite user input.

---

## Anatomy

**A. Stop/Cancel button** — ends session; transcribed text stays in input field
**B. Placeholder/Text area** — shows "Begin speaking…" then live transcription
**C. Audio visualizer** — indicates microphone activity
**D. Submit/Send button** — sends transcription to Joule

---

## States

| State | Description |
|-------|-------------|
| Idle | Waiting; "Begin speaking…" placeholder; Send inactive |
| Active Listening | Recording; audio visualizer active; live transcription; Send becomes active |

---

## Behavior

**Stop without sending:** Returns to default input mode. Transcription preserved in text area for review/editing. User can add attachments or send later.

**Dictation with content:** Works alongside active attachments or modes — transcription captured with existing context.

---

## Related

- [../components/input-field.md](../components/input-field.md)
- [modes.md](modes.md)
