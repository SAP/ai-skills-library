# AI Handoff — In-App AI Design

> SAP Fiori for iOS | In-App AI Design

## What is it?

An AI handoff is the transition between contextual embedded AI features and the Joule conversational panel. A seamless handoff gives users a unified AI experience that keeps their workflow cohesive.

---

## When to Use Which

| | Embedded AI | Joule |
|--|-------------|-------|
| **User path** | Follows app structure: buttons, menus, fixed layouts | Removes UI constraints: conversational panel |
| **Best for** | Quick approval, form autofill, inline hints, contextual validation | Multi-step planning, cross-module retrieval, bulk actions, troubleshooting |
| **Handoff moment** | Task expands beyond page/form → redirect to Joule | Exploration done → hand results back to embedded AI for execution |
| **Strengths** | Fast, focused, contextual | Flexible, open-ended, cross-module |
| **Limitations** | Bound to existing UI; not scalable for complex tasks | Requires context switching; may interrupt flow if overused |

---

## Do's / Don'ts

**Do:**
- Minimize workflow disruptions
- Use smooth, seamless transitions
- Share context between Joule and embedded AI
- Set clear user expectations with clear CTAs and visual cues
- Use transitional micro-interactions

**Don't:**
- Force users into Joule without warning
- Use inconsistent transitions or visual cues
- Hide AI markers or loading/generating states

---

## Joule Patterns

| Pattern | Use for |
|---------|---------|
| **Entry point** | General guidance for new users; general queries about getting started |
| **Insight tool** | Quick summaries from multiple data sources |
| **Comprehensive request handler** | Complex user needs; custom solutions for unique tasks |
| **Proactive assistant** | Decision-making prompts; optimization suggestions |
| **One-stop shop** | Cross-module tasks; bulk actions |

## Embedded AI Patterns

| Pattern | Use for |
|---------|---------|
| **Contextual helper** | Simple, targeted tasks in current workflow |
| **Insight generator** | In-context recommendations, error detection, page summaries |

---

## Handoff Examples

### Embedded AI → Joule
User taps AI "Summary" button on a work order → summary generated in-screen → user wants more detail → opens Joule → asks follow-up questions in natural language.

**When to handoff to Joule:**
- Task expands beyond what the current page can handle
- User needs cross-module information
- User wants to explore open-ended questions

### Joule → Embedded AI
User asks Joule to fill out a goal form → Joule generates content and provides a link → user navigates to the form → uses embedded AI writing assistant to refine individual fields before submission.

**When to handoff to Embedded AI:**
- Task requires direct user input or review (editing a form, submitting)
- User benefits from working contextually (in a data table, in a specific form)

---

## SwiftUI Implementation Note

```swift
// Provide a clear entry point to Joule from embedded AI context
FioriButton { _ in
    HStack {
        Image(systemName: "sparkles")  // AI star icon
        Text("Ask Joule")
    }
}
.fioriButtonStyle(FioriSecondaryButtonStyle())
.onTapGesture {
    // Pass current context to Joule before opening
    openJoule(context: currentWorkOrderContext)
}

// On return from Joule, apply results to embedded UI
.onReceive(jouleResultPublisher) { result in
    applyJouleResultToForm(result)
}
```

---

## Related

- [get-started.md](get-started.md)
- [ai-ui-text.md](ai-ui-text.md)
- [ai-buttons.md](ai-buttons.md)
