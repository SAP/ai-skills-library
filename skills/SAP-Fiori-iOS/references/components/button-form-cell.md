# Button Form Cell — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIButtonFormCell`, SwiftUI `FioriButton`

## What is it?

A button form cell represents an action that can be taken within a view. It appears inside a `Form` or `List` as a tappable row — distinct from the standalone `FioriButton` which appears outside of list contexts.

---

## When to Use

**Do:**
- Use to represent an action within the current view

**Don't:**
- Use to represent a selection — use a segmented control form cell or list picker instead

---

## Behavior

### Text Wrapping
Button form cells allow text to wrap — text is never truncated. Keep labels short and concise regardless.

---

## Variations

### Standard Button Form Cell
Used for an action within the current screen view.

```swift
import FioriSwiftUICore
import SwiftUI

Form {
    Section {
        // Other form fields
        TextFieldFormView(title: { Text("Name") }, text: $name)
    }

    Section {
        // Standard button form cell
        FioriButton { _ in
            Text("Add Item")
        }
        .fioriButtonStyle(FioriTertiaryButtonStyle())
        .frame(maxWidth: .infinity, alignment: .leading)
    }
}
```

### Centered Button Form Cell
Used for a global action affecting the whole window or application (e.g. Sign In, Save). Always placed at the **bottom** of the view in its **own separate section**.

```swift
Form {
    Section("Account") {
        KeyValueFormView(keyText: { Text("Email") }, value: { Text(user.email) })
        KeyValueFormView(keyText: { Text("Name") }, value: { Text(user.name) })
    }

    // Centered global action — its own section at the bottom
    Section {
        FioriButton { _ in Text("Save Changes") }
            .fioriButtonStyle(FioriPrimaryButtonStyle())
            .frame(maxWidth: .infinity, alignment: .center)
    }
}
```

### Semantic Button Form Cell
Used when the action requires careful user attention — destructive or high-consequence actions like Sign Out or Delete. Uses semantic (negative) color. Always placed in its **own separate section**.

```swift
Form {
    Section("Settings") {
        // Settings rows
    }

    // Semantic action — separate section, negative color
    Section {
        FioriButton { _ in Text("Sign Out") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .tint(Color.preferredColor(.negativeLabel))
            .frame(maxWidth: .infinity, alignment: .leading)
    }

    Section {
        FioriButton { _ in Text("Delete Account") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .tint(Color.preferredColor(.negativeLabel))
            .frame(maxWidth: .infinity, alignment: .leading)
    }
}
```

### All three variations together
```swift
Form {
    Section("Details") {
        TextFieldFormView(title: { Text("Title") }, text: $title)
        NoteFormView(title: { Text("Notes") }, text: $notes)
    }

    // Standard — inline action
    Section {
        FioriButton { _ in Text("Add Attachment") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .frame(maxWidth: .infinity, alignment: .leading)
    }

    // Centered — global/primary action
    Section {
        FioriButton { _ in Text("Submit") }
            .fioriButtonStyle(FioriPrimaryButtonStyle())
            .frame(maxWidth: .infinity, alignment: .center)
    }

    // Semantic — destructive, own section
    Section {
        FioriButton { _ in Text("Delete Draft") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .tint(Color.preferredColor(.negativeLabel))
            .frame(maxWidth: .infinity, alignment: .leading)
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Variation | Standard | Leading alignment, tertiary style |
| Variation | Centered | `.frame(maxWidth: .infinity, alignment: .center)`, primary style |
| Variation | Semantic | `.tint(Color.preferredColor(.negativeLabel))` |
| Placement | Standard | Inline in relevant section |
| Placement | Centered / Semantic | Own separate `Section` at bottom |
| Text | Wrapping | Allowed — no `.lineLimit(1)` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Place centered and semantic button form cells in their **own separate sections**
- Always put centered/global actions at the **bottom** of the view
- Use semantic (negative) color for destructive actions
- Allow text to wrap — never truncate

**Don't:**
- Use a button form cell for selection — use segmented control or list picker
- Mix a centered button form cell in a section with other form rows
- Use a standard `Button` inside a `Form` where the Fiori form cell style is expected

---

## Related Components

- [buttons.md](buttons.md) — standalone FioriButton outside of forms
- [forms.md](forms.md) — other form input cells
