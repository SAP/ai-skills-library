# Modality — Pattern Guide

> SAP Fiori for iOS | Patterns
> See also: [../components/sheets.md](../components/sheets.md), [../components/modals.md](../components/modals.md)

## What is it?

Modality temporarily shifts user focus to a specific task by presenting content in a separate layer above the current view. It disables interaction with the underlying screen until the user completes or dismisses the modal.

---

## When to Use

**Do:**
- Use for critical information requiring user acknowledgment
- Use for decisions or inputs that must be completed before continuing

**Don't:**
- Use for routine navigation or trivial actions

**Top tips:**
- Keep modal tasks self-contained
- Respect platform conventions: swipe-down to dismiss on iPhone, tap outside to dismiss form sheets on iPad
- Use form sheets/popovers on iPad instead of full-screen when full immersion isn't needed
- Don't overload modals with too many options
- Avoid multiple stacked modal layers unless absolutely required

---

## Modal Types

### Alerts
Critical information requiring immediate user acknowledgment. Max 2 actions (default + cancel). Block all interaction until dismissed. Centered on screen; used in both compact and regular width.

```swift
.alert("Delete Invoice?", isPresented: $showAlert) {
    Button("Delete", role: .destructive) { delete() }
    Button("Cancel", role: .cancel) {}
} message: {
    Text("This action cannot be undone.")
}
```

### Action Sheets
List of 2+ choices related to the current context. Appears from the bottom; blocks parent view. Used for context-specific options.

```swift
.confirmationDialog("Choose Action", isPresented: $showActions, titleVisibility: .visible) {
    Button("Share") { share() }
    Button("Archive") { archive() }
    Button("Delete", role: .destructive) { delete() }
    Button("Cancel", role: .cancel) {}
}
```

### Activity Views (Share Sheets)
System-provided modal for sharing content or performing system actions (share, copy, print). Customizable with app-specific actions. Full-screen on iPhone; popover/sheet on iPad.

```swift
ShareLink(item: document.url, subject: Text("Invoice #1234"))
// or
.sheet(isPresented: $showShare) {
    ActivityView(activityItems: [document.url])
}
```

### Popovers (iPad only)
Transient contextual view for quick tasks (filter, select). Regular width only. Tap outside to dismiss.

```swift
// Only on regular width (iPad)
.popover(isPresented: $showPopover) {
    FilterView()
        .frame(width: 320, height: 400)
}
```

### Modal Sheets
Required completion or explicit dismissal. Full-screen on iPhone; form sheet (centered, dimmed bg) on iPad. Include Cancel / Done in nav bar.

```swift
.sheet(isPresented: $showModal) {
    NavigationStack {
        FormView()
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") { showModal = false }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Save") { save(); showModal = false }
                }
            }
    }
}
```

### Non-Modal Sheets
Background interaction remains enabled. Used for supplementary workflows (filters, side panels). Dismissed by background tap, swipe, or Done button — no forced action required.

```swift
.sheet(isPresented: $showFilters) {
    FilterPanelView()
        .presentationDetents([.medium])
        .presentationBackgroundInteraction(.enabled)  // non-modal
}
```

---

## Summary Table

| Type | Compact | Regular | Background interaction | Dismiss |
|------|---------|---------|----------------------|---------|
| Alert | Centered | Centered | ✗ | Choose action |
| Action sheet | Bottom | Bottom | ✗ | Choose action or Cancel |
| Activity view | Full-screen | Popover/sheet | ✗ | Cancel or select action |
| Popover | N/A | Popover | ✓ | Tap outside |
| Modal sheet | Full-screen | Form sheet (centered) | ✗ | Done/Cancel |
| Non-modal sheet | Sheet | Sheet/side panel | ✓ | Tap outside, swipe, Done |

---

## Related Components

- [../components/sheets.md](../components/sheets.md) — SwiftUI implementation
- [../components/modals.md](../components/modals.md) — Fiori modal patterns
