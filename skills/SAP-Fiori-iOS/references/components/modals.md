# Modals — Component Guidelines

> SAP Fiori for iOS | Category: Pattern Overview
> Development reference: `FUIModalCheckoutViewController`, `FUIModalProcessingIndicator`, `FUIModalLoadingIndicatorView`, `FUIModalLoadingIndicator`, `FUIModalProcessingIndicatorView`
> This is a conceptual guide — see [sheets.md](sheets.md) for full SwiftUI implementation.

## What is it?

A modal is used for completing a task, updating content, or selecting filters. It focuses the user on the current task. Modals are commonly used in create and filter patterns.

A modal **slides up from the bottom** by default. In edit mode, it uses a **Dissolve transition** instead.

---

## Variations by Size Class

### Compact Width — Full-Screen Modal

Modals in compact width (iPhone) are presented as **full-screen windows**.

Exit requires tapping one of two navigation bar buttons:
- **Left button** — "Cancel" — abandons the task, discards progress
- **Right button** — completion action — use descriptive language: "Create", "Add", "Save"

> Avoid "Done" — it's too vague. Use the action verb instead.

```swift
// Compact: full-screen modal
.fullScreenCover(isPresented: $showModal) {
    NavigationStack {
        CreateFormView()
            .navigationTitle("New Invoice")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    FioriButton { _ in Text("Cancel") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { showModal = false }
                }
                ToolbarItem(placement: .confirmationAction) {
                    FioriButton { _ in Text("Create") }  // not "Done"
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { create(); showModal = false }
                }
            }
    }
}
```

### Regular Width — Form Sheet (default)

In regular width (iPad), modals default to **form sheets**: centered on screen with a semi-transparent overlay.

- Used for **data collection** (create, edit forms)
- User should be able to complete the task without referring to outside information
- **Tap outside** → dismisses like "Cancel" (no save, no completion)
- On dismiss: modal slides downward off screen

```swift
// Regular: form sheet (default .sheet behavior on iPad)
.sheet(isPresented: $showFormSheet) {
    NavigationStack {
        CreateFormView()
            .navigationTitle("New Invoice")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    FioriButton { _ in Text("Cancel") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { showFormSheet = false }
                }
                ToolbarItem(placement: .confirmationAction) {
                    FioriButton { _ in Text("Create") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { create(); showFormSheet = false }
                }
            }
    }
}
// Tap outside automatically dismisses (default .sheet behavior)
```

### Regular Width — Popover

For **quick tasks** (filtering, selecting an option). Tapping outside dismisses.

```swift
.popover(isPresented: $showPopover) {
    FilterOptionsView()
        .frame(width: 320, height: 400)
}
// Tap outside = dismiss
```

### Regular Width — Full-Screen Modal

For **complex tasks requiring full attention**. Apply **readable width** to components — wide screens are hard to read at full width.

```swift
.fullScreenCover(isPresented: $showFullScreen) {
    NavigationStack {
        ComplexWorkflowView()
            .frame(maxWidth: 672)  // readable width
            .navigationTitle("Complex Task")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    FioriButton { _ in Text("Cancel") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { showFullScreen = false }
                }
                ToolbarItem(placement: .confirmationAction) {
                    FioriButton { _ in Text("Save") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { save(); showFullScreen = false }
                }
            }
    }
}
```

---

## Summary Table

| Size class | Modal type | Dismiss mechanism | Use for |
|-----------|-----------|------------------|---------|
| Compact | Full-screen | Nav bar Cancel/action buttons only | Create, edit, filter |
| Regular | Form sheet *(default)* | Nav bar buttons **or** tap outside | Data collection |
| Regular | Popover | Tap outside | Quick tasks, filter |
| Regular | Full-screen | Nav bar buttons only | Complex, high-attention workflows |

---

## Button Label Guidelines

| Action | Label |
|--------|-------|
| Creating something | "Create" |
| Adding something | "Add" |
| Saving changes | "Save" |
| Abandoning task | "Cancel" |
| ❌ Avoid | "Done" (too vague) |

---

## Transitions

- **Default** — slides up from bottom
- **Edit mode** — Dissolve transition

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use descriptive action verbs for the right nav bar button ("Create", "Add", "Save")
- Apply readable width (≤672pt) for full-screen modals on regular width
- Ensure tapping outside a form sheet or popover acts as Cancel (no unsaved data)

**Don't:**
- Use "Done" as a completion button label
- Show content in a full-screen modal that could be shown in a form sheet
- Require users to refer to content outside the modal to complete the task

---

## Related Components

- [sheets.md](sheets.md) — full SwiftUI implementation of all sheet/modal types
- [buttons.md](buttons.md) — nav bar button styles and placement
- [forms.md](forms.md) — form patterns typically presented in modals
