# Modes — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns

## What is it?

The mode selector lets users apply a thinking mode to their next Joule prompt. Thinking modes change how Joule processes and responds (e.g., deep research). Accessed via the "+" icon button alongside attachments.

---

## Rules

**Do:** Display selected mode as a chip. Show "+" sheet when user needs to change mode.
**Don't:** Allow multiple thinking modes simultaneously. Change the chip priority hierarchy. Show Voice button when a chip is active.

---

## Chip Priority Hierarchy

```
Attachment (highest — cannot be overridden)
    ↑ overrides ↓
Agent / Thinking Mode (can override each other)
```

- At most **one chip** at a time
- While attachment chip is active: "+" and "@" disabled
- "Default" mode never shown as chip (it's the baseline)

---

## Anatomy

### Attachment & Mode Selector Sheet
**A. Thinking Modes Section** — list of modes; each has unique icon + label; Default always selected by default

### Mode Selector Chip
**A. Chip** — icon + label + "×" remove; max width 250pt
- Attachment chip: middle truncation of filename
- Mode/Agent chip: end truncation

---

## Behavior

- Tap "+" → bottom sheet opens → select mode → sheet closes → chip appears in input field
- Tap "×" on chip → reverts to Default (no chip shown)
- Select different mode → overrides current mode chip
- Upload attachment → overrides mode/agent chip; "+" and "@" disabled

---

## Chip Variants

| Chip type | Contents | Priority |
|-----------|----------|---------|
| Attachment | File type icon + filename (middle truncate) | Highest |
| Thinking Mode | Mode icon + label (end truncate) | Medium |
| Agent | Agent icon + label (end truncate) | Medium |

---

## Related

- [../components/input-field.md](../components/input-field.md)
- [persistent-attachment.md](persistent-attachment.md)
