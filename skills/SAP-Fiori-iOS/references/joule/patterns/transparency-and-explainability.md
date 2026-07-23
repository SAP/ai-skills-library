# Transparency and Explainability — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns

## What is it?

Provides clarity about how Joule's AI-generated responses were created. Users can view response insights (how the response was generated) or source information (links to original content) via the response action bar.

---

## Rules

**Do:** Provide for every Joule-generated response. Use response insights for unlinked types. Use sources view for linked types.
**Don't:** Use for non-Joule responses. Mix up where unlinked and linked response types appear. Change style or placement of the information icon button.

---

## Two Response Action Buttons

**A. Information icon (ⓘ)** — opens Response Insights View (unlinked sources)
**B. Source button** — opens Source Information View (linked sources; hidden if no linked sources)

---

## Response Insights View (modal bottom sheet)
**A. Navigation bar** — title
**B. Insights list** — title + description per insight

## Source Information View (modal bottom sheet)
**A. Navigation bar** — title
**B. Sources list** — title + description + external link icon per source; fill panel width

---

## Response Types

### Read-Only Sources (non-interactive)

| Type | Description | Title/Description |
|------|-------------|-------------------|
| Small Talk | LLM generates itself; not grounded in SAP knowledge | Predefined |
| Capability-Based | SAP-implemented functionality | Title dynamic; description = "SAP AI Joule use case" |
| Extensibility | Customer-implemented capability | Predefined |
| External | From Microsoft Copilot or other assistants | Both dynamic |

### Actionable Source (interactive)

| Type | Description |
|------|-------------|
| Information Retrieval | Answers from SAP Help Portal or customer-uploaded docs; appears as citation [1] in response |

---

## Opening Sources

- **Bottom sheet link** → tap External Link icon → opens in device default app
- **Inline citation** [1] → tap → opens link in device default app

---

## Related

- [../components/response-actions.md](../components/response-actions.md)
- [../components/text-messages.md](../components/text-messages.md)
