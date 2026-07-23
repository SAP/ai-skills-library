# AI Handoff — Joule

> SAP Fiori for iOS | Joule
> See also: [../in-app-ai-design/patterns/ai-handoff.md](../in-app-ai-design/patterns/ai-handoff.md)

## What is it?

An AI handoff is the user's transition between contextual embedded AI features and the Joule conversational panel. Seamless handoffs create a unified AI experience that keeps workflows cohesive.

---

## Do's / Don'ts

**Do:**
- Minimize workflow disruptions
- Use smooth, seamless transitions
- Share context between Joule and embedded AI
- Set clear user expectations with CTAs, entry points, and visual cues
- Use transitional micro-interactions and animations

**Don't:**
- Upend the user's expected workflow
- Force users into Joule without warning
- Use inconsistent transitions or visual cues
- Hide AI markers or loading/generating states

---

## Embedded AI vs. Joule

| | Embedded AI | Joule |
|--|-------------|-------|
| **User path** | Follows app structure: buttons, menus, fixed layouts | Conversational panel — removes UI constraints |
| **Best for** | Quick approval, form autofill, inline hints, contextual validation | Multi-step planning, cross-module retrieval, bulk actions, troubleshooting |
| **Handoff moment** | Task expands beyond page/form → redirect to Joule | Exploration done → hand results back to embedded AI for execution |
| **Strengths** | Fast, focused, contextual | Flexible, open-ended, cross-module |
| **Limitations** | Bound to existing UI; not scalable for complex tasks | Requires context switching; can interrupt flow if overused |

---

## Joule Patterns

| Pattern | Use for |
|---------|---------|
| **Entry point** | General guidance for new users; onboarding queries |
| **Insight tool** | Quick summaries from multiple data sources |
| **Comprehensive request handler** | Complex needs; custom solutions for unique tasks |
| **Proactive assistant** | Decision-making prompts; optimization suggestions |
| **One-stop shop** | Cross-module tasks; bulk actions |

## Embedded AI Patterns

| Pattern | Use for |
|---------|---------|
| **Contextual helper** | Simple, targeted tasks in current workflow |
| **Insight generator** | In-context recommendations, error detection, summaries |

---

## Handoff Examples

### Embedded AI → Joule
**Work order summary:** User taps AI "Summary" button → summary generated in-screen → user wants more detail about action items → opens Joule → asks follow-up in natural language.

**Account synopsis:** User generates an AI Insights view for a sales lead → opens Joule → asks for recommended next steps including a sample email draft.

**When to hand off to Joule:**
- Task expands beyond the current page/form
- User needs cross-module information
- User wants open-ended exploration

### Joule → Embedded AI
**Goal form:** User asks Joule to fill out a form → Joule generates content and provides a navigation link → user reviews fields → uses embedded AI writing assistant to refine individual fields before submission.

**When to hand off to Embedded AI:**
- Task requires direct user input or review (editing, submitting)
- User benefits from working contextually in the app UI

---

## Related

- [get-started.md](get-started.md)
- [../in-app-ai-design/patterns/ai-handoff.md](../in-app-ai-design/patterns/ai-handoff.md)
