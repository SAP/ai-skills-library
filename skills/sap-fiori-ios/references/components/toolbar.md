# Toolbar — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIToolbar`, SwiftUI `.toolbar { ToolbarItemGroup(placement: .bottomBar) }`

## What is it?

The toolbar sits at the **bottom edge** of the screen and contains closing or finalizing actions that impact the entire current view. It remains fixed during scrolling.

**Use for actions that impact the whole view — not for actions on specific items only.**

---

## When to Use

**Do:**
- Use for closing or finalizing actions
- Use descriptive, concise verb labels
- Use a primary button only when there is a clear primary action
- Use an overflow menu when iPhone needs >2 text buttons or iPad needs >3
- Place the positive/most important action on the **right**

**Don't:**
- Use when the action influences only specific items (not the whole view)
- Combine icon-only and text-only buttons in the same toolbar
- Mix tertiary buttons with secondary or primary buttons
- Use helper text when an overflow button is present

---

## Anatomy

```
[B. Secondary] [E. Tertiary]  F. Helper text  [C. Primary →]
     ← compact: equal width distribution →
     ← regular: right-aligned →

D. Overflow opens action sheet when limit exceeded
```

**A. Toolbar Container** — always visible; full screen width.
**B. Secondary Text Button** — non-primary actions. Use secondary style when 2+ buttons present.
**C. Primary Text Button** — most important action; one per view. If toolbar has only one button, use primary style.
**D. Overflow Button** — activates when >2 (compact) or >3 (regular) text buttons exist.
**E. Tertiary Text/Icon Button** — low-emphasis additional actions.
**F. Helper Text** — read-only status/info. Cannot coexist with overflow button.
**G. Tertiary Icon Button** — universally recognized icons only.

---

## Overflow Rules

| Size class | Overflow triggers at |
|-----------|---------------------|
| Compact (iPhone) | >2 text buttons |
| Regular (iPad) | >3 text buttons |

Most important actions appear first (right side). Overflow tapping opens an **action sheet** with text-only buttons.

**Long label rule:** If two buttons don't fit, the secondary button moves to overflow and the primary/more important button stretches full width.

---

## Adaptive Layout

| Size class | Button distribution |
|-----------|-------------------|
| Compact | Equally distributed across full width |
| Regular | Right-aligned |

Western Z-pattern reading: the bottom right is the best position for a finalizing action.

---

## Semantic Actions

Destructive/negative → secondary negative style (red)
Positive action → secondary tint style
Positive action goes on the **right**.

---

## SwiftUI Code Examples

### One primary button
```swift
.toolbar {
    ToolbarItemGroup(placement: .bottomBar) {
        Spacer()
        FioriButton { _ in Text("Submit") }
            .fioriButtonStyle(FioriPrimaryButtonStyle())
    }
}
```

### Primary + secondary
```swift
.toolbar {
    ToolbarItemGroup(placement: .bottomBar) {
        FioriButton { _ in Text("Cancel") }
            .fioriButtonStyle(FioriSecondaryButtonStyle())
        Spacer()
        FioriButton { _ in Text("Save") }
            .fioriButtonStyle(FioriPrimaryButtonStyle())
    }
}
```

### Semantic (Reject/Approve)
```swift
.toolbar {
    ToolbarItemGroup(placement: .bottomBar) {
        // Negative on left
        FioriButton { _ in Text("Reject") }
            .fioriButtonStyle(FioriSecondaryButtonStyle())
            .tint(Color.preferredColor(.negativeLabel))
        Spacer()
        // Positive on right
        FioriButton { _ in Text("Approve") }
            .fioriButtonStyle(FioriSecondaryButtonStyle())
    }
}
```

### Two secondary (no clear primary)
```swift
.toolbar {
    ToolbarItemGroup(placement: .bottomBar) {
        FioriButton { _ in Text("Decline") }
            .fioriButtonStyle(FioriSecondaryButtonStyle())
        Spacer()
        FioriButton { _ in Text("Accept") }
            .fioriButtonStyle(FioriSecondaryButtonStyle())
    }
}
```

### Overflow (>2 on compact)
```swift
.toolbar {
    ToolbarItemGroup(placement: .bottomBar) {
        FioriButton { _ in Text("Save") }
            .fioriButtonStyle(FioriPrimaryButtonStyle())

        Menu {
            Button("Share") { share() }
            Button("Archive") { archive() }
            Button("Duplicate") { duplicate() }
        } label: {
            Image(systemName: "ellipsis.circle")
                .accessibilityLabel("More actions")
        }
    }
}
```

### With helper text
```swift
// Helper text — only when NO overflow button
.toolbar {
    ToolbarItemGroup(placement: .bottomBar) {
        Text("3 items selected")
            .font(.fiori(forTextStyle: .footnote))
            .foregroundStyle(Color.preferredColor(.secondaryLabel))
        Spacer()
        FioriButton { _ in Text("Delete") }
            .fioriButtonStyle(FioriSecondaryButtonStyle())
            .tint(Color.preferredColor(.negativeLabel))
    }
}
```

### Tertiary icon buttons
```swift
.toolbar {
    ToolbarItemGroup(placement: .bottomBar) {
        FioriButton { _ in Image(systemName: "trash").accessibilityLabel("Delete") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
        FioriButton { _ in Image(systemName: "square.and.arrow.up").accessibilityLabel("Share") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
        Spacer()
        FioriButton { _ in Image(systemName: "checkmark").accessibilityLabel("Done") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Primary | Yes | `FioriPrimaryButtonStyle()` — right |
| Secondary | Yes | `FioriSecondaryButtonStyle()` |
| Tertiary text | Yes | `FioriTertiaryButtonStyle()` |
| Tertiary icon | Yes | `FioriTertiaryButtonStyle()` + icon only |
| Semantic negative | Yes | `.tint(Color.preferredColor(.negativeLabel))` |
| Overflow | Compact >2 / Regular >3 | `Menu {}` as last item |
| Helper text | Yes (no overflow) | `Text(...)` + `Spacer()` |
| Layout | Compact | Equal distribution |
| Layout | Regular | Right-aligned |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Place the primary/positive action on the right
- Use overflow when button limit is exceeded — never truncate labels
- Use filled buttons (primary/secondary) for the most likely actions
- Keep helper text only when there is no overflow button

**Don't:**
- Mix icon-only and text-only buttons
- Mix tertiary with primary/secondary in the same toolbar
- Use for item-specific actions (not whole-view actions)
- Show helper text alongside an overflow button

---

## Related Components

- [buttons.md](buttons.md) — button styles used in toolbar
- [navigation-bar.md](navigation-bar.md) — top-bar actions
