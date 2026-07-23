# Step Progress Indicator — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Progress Indicators
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIStepProgressIndicator`, SwiftUI `StepProgressIndicator`

## What is it?

The step progress indicator tracks and displays a user's position in a multi-step flow. It allows navigation to other steps and supports linear, non-linear, and dynamic step patterns.

---

## When to Use

**Do:**
- Minimum **2 steps** required
- Use dynamic steps for sub-steps or steps dependent on previous actions
- Show a partial view of the last step on screen to indicate the indicator is scrollable
- Keep step names to **≤2 lines** of text

**Don't:**
- Show both a header step name and step names under nodes simultaneously
- Count dynamic steps in the total number of steps
- Show a partial step if the indicator is not scrollable

---

## Anatomy

### Default View
```
A. Current step name (optional)          [B. All Steps →]
   ①────────②────────③────────④────────⑤
C. Step node      D. Step line      E. Step name
```

**A. Current step name** — describes the current step (optional).
**B. All Steps button** — navigates to the All Steps view (optional).
**C. Step node** — number or icon for each step.
**D. Step line** — connects steps; absent on the final step.
**E. Step name** — labels each step (optional).

### All Steps View
Vertical list of all steps with nodes, lines, and names. Presented as:
- **Compact** — full-screen push
- **Regular (iPad)** — popover modal

---

## Step Value States

| State | Visual |
|-------|--------|
| Complete | Filled, tint color |
| Active | Highlighted current step |
| Error | Red indicator |
| Error Active | Red + active highlight |
| Default | Unfilled / upcoming |
| Disabled | Dimmed, not tappable |

---

## Step Types (mutually exclusive)

| Type | Notes |
|------|-------|
| **Numeric** | Default — shows step number (1, 2, 3…). Max 3 digits. Cannot mix with icon steps. |
| **Icon** | Replaces numbers with 16pt icons. Cannot mix with numeric steps. |
| **Dynamic** | Sub-steps (2.1, 2.2…) or conditional steps that appear based on user actions. Not counted in total. |

---

## Navigation

- **Linear flow** — user can only tap the next step once the current one is complete
- **Non-linear flow** — user can tap any step regardless of state

---

## Horizontal Scrolling

When steps exceed screen width, the indicator scrolls horizontally. When the user completes the last visible step:
- The indicator auto-scrolls to the next screen
- The newly active step pins as the first step
- On the final screen, the bar is **right-aligned**

---

## Node Width

| Context | Min width |
|---------|-----------|
| Compact | 86pt |
| Regular | 126pt |
| Regular full-width | 140pt |

Fewer than 4 steps (compact) or 5 steps (regular) → nodes expand to fill the full width.

---

## SwiftUI Code Examples

### Basic step progress indicator
```swift
import FioriSwiftUICore

@State private var currentStep = 0
let steps = ["Details", "Review", "Approve", "Done"]

StepProgressIndicator(
    selection: $currentStep,
    steps: steps.indices.map { i in
        Step(id: "\(i)", title: steps[i])
    }
)
```

### With value states
```swift
StepProgressIndicator(
    selection: $currentStep,
    steps: [
        Step(id: "details",  title: "Details",  state: .completed),
        Step(id: "review",   title: "Review",   state: .inProgress),
        Step(id: "approve",  title: "Approve",  state: .disabled),
        Step(id: "done",     title: "Done",     state: .disabled)
    ]
)
```

### With All Steps button
```swift
StepProgressIndicator(
    selection: $currentStep,
    steps: formSteps,
    showAllStepsButton: true
)
// All Steps view: push on compact, popover on regular — automatic
```

### Dynamic steps (sub-steps appear conditionally)
```swift
@State private var steps: [Step] = baseSteps

// Add sub-steps based on user action
func onUserSelectsOption(_ option: Option) {
    if option.requiresSubSteps {
        steps.insert(
            Step(id: "2.1", title: "Sub-step A"),
            at: currentStep + 1
        )
    }
    // Dynamic steps are NOT counted in total
}
```

### Non-linear navigation
```swift
StepProgressIndicator(
    selection: $currentStep,
    steps: steps,
    isLinear: false  // any step is tappable regardless of state
)
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Step type | Numeric | Default `Step` with title |
| Step type | Icon | `Step` with `icon: Image(systemName:)` |
| Step type | Dynamic | Insert `Step` into array conditionally |
| State | Complete | `state: .completed` |
| State | Active | `state: .inProgress` |
| State | Error | `state: .error` |
| State | Disabled | `state: .disabled` |
| Flow | Linear | `isLinear: true` (default) |
| Flow | Non-linear | `isLinear: false` |
| All Steps | Yes | `showAllStepsButton: true` |
| All Steps view | Compact | Push navigation |
| All Steps view | Regular | Popover |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Minimum 2 steps
- Keep step labels ≤2 lines
- Show a partial last step to indicate scrollability
- Use dynamic steps for conditional sub-flows — don't count them in total

**Don't:**
- Mix numeric and icon steps in the same indicator
- Show both header step name and step-node labels simultaneously
- Show partial steps on a non-scrollable indicator

---

## Related Components

- [sibling-navigation.md](sibling-navigation.md) — lateral navigation between same-level items
