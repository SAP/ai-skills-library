# Sheets — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: SwiftUI `.sheet`, `.fullScreenCover`, `.popover`

## What is it?

Sheets present focused content or actions without navigating away from the primary screen. They can be modal (require explicit dismissal) or non-modal (allow background interaction).

---

## When to Use

- **Modal sheets** — brief, focused workflows: editing, adding, assigning
- **Non-modal sheets** — contextual, optional tools: filters, metadata, search

**Top tips:**
- Adapt behavior based on size class (compact vs. regular)
- Provide a clear dismiss mechanism (button or swipe)
- Keep sheet tasks short and focused
- Avoid hiding critical actions in deep navigation within a sheet
- Don't nest multiple sheets unless necessary

---

## Variations

### Modal Sheet
Blocks interaction with the underlying content. Use when the user must complete a task before returning. Slides up from the bottom; includes drag indicator, title bar, action/cancel buttons.

Use for quick decisions or small workflows — not complex multi-step flows.

```swift
@State private var showSheet = false

Button("Edit") { showSheet = true }
    .sheet(isPresented: $showSheet) {
        NavigationStack {
            EditFormView()
                .navigationTitle("Edit Invoice")
                .navigationBarTitleDisplayMode(.inline)
                .toolbar {
                    ToolbarItem(placement: .cancellationAction) {
                        FioriButton { _ in Text("Cancel") }
                            .fioriButtonStyle(FioriTertiaryButtonStyle())
                            .onTapGesture { showSheet = false }
                    }
                    ToolbarItem(placement: .confirmationAction) {
                        FioriButton { _ in Text("Save") }
                            .fioriButtonStyle(FioriTertiaryButtonStyle())
                            .onTapGesture { save(); showSheet = false }
                    }
                }
        }
        .presentationDetents([.medium, .large])
        .presentationDragIndicator(.visible)
    }
```

### Full-Screen Modal (compact only)
Entire screen; used for complex, high-attention workflows. Exit via Cancel (left) or completion action (right) in the navigation bar. No swipe-to-dismiss.

```swift
Button("Create Order") { showFullScreen = true }
    .fullScreenCover(isPresented: $showFullScreen) {
        NavigationStack {
            CreateOrderView()
                .navigationTitle("New Order")
                .toolbar {
                    ToolbarItem(placement: .cancellationAction) {
                        FioriButton { _ in Text("Cancel") }
                            .fioriButtonStyle(FioriTertiaryButtonStyle())
                            .onTapGesture { showFullScreen = false }
                    }
                    ToolbarItem(placement: .confirmationAction) {
                        FioriButton { _ in Text("Submit") }
                            .fioriButtonStyle(FioriTertiaryButtonStyle())
                            .onTapGesture { submit(); showFullScreen = false }
                    }
                }
        }
    }
```

### Form Sheet (regular width default)
Default modal presentation on iPad — centered with semi-transparent overlay. Tap outside to dismiss.

```swift
// On iPad, .sheet() automatically uses form sheet style
// No extra configuration needed
Button("Add Vendor") { showFormSheet = true }
    .sheet(isPresented: $showFormSheet) {
        VendorFormView()
    }
// Tapping outside dismisses (default behavior)
```

### Non-Modal Sheet
Allows background interaction while the sheet is open. Used for filters, metadata, search tools.

```swift
// Dismiss via swipe down, Done button, or tapping outside
.sheet(isPresented: $showFilters) {
    FilterPanelView()
        .presentationDetents([.medium])
        .presentationBackgroundInteraction(.enabled)  // non-modal: allows background interaction
}
```

### Popover (iPad only, regular width)
Small amount of info or functionality. Anchored to the triggering element. Auto-dismissed when focus is lost. Regular width only — never use on compact (iPhone).

```swift
@Environment(\.horizontalSizeClass) var hSizeClass
@State private var showPopover = false

Button("Info") { showPopover = true }
    .popover(isPresented: $showPopover) {
        InfoDetailView()
            .frame(width: 320, height: 240)
    }
// Only use on regular width — on compact use .sheet instead
```

### Adaptive sheet (compact = sheet, regular = popover)
```swift
@Environment(\.horizontalSizeClass) var hSizeClass
@State private var showOptions = false

Button("Options") { showOptions = true }
    .modifier(AdaptiveSheet(isPresented: $showOptions) {
        OptionsView()
    })

struct AdaptiveSheet<SheetContent: View>: ViewModifier {
    @Environment(\.horizontalSizeClass) var hSizeClass
    @Binding var isPresented: Bool
    let content: () -> SheetContent

    func body(content: Content) -> some View {
        if hSizeClass == .compact {
            content.sheet(isPresented: $isPresented) { self.content() }
        } else {
            content.popover(isPresented: $isPresented) { self.content() }
        }
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Type | Modal sheet (compact) | `.sheet` + `.presentationDetents([.medium, .large])` |
| Type | Full-screen modal (compact) | `.fullScreenCover` |
| Type | Form sheet (regular) | `.sheet` — automatic on iPad |
| Type | Non-modal (regular) | `.sheet` + `.presentationBackgroundInteraction(.enabled)` |
| Type | Popover (regular) | `.popover` |
| Dismiss | Button | `ToolbarItem(placement: .cancellationAction)` |
| Dismiss | Swipe | Default `.sheet` behavior |
| Dismiss | Tap outside | Form sheet + non-modal default |
| Drag indicator | Yes | `.presentationDragIndicator(.visible)` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use form sheet (centered) as the default modal on iPad
- Use full-screen modal only for complex, high-attention compact-width workflows
- Always provide Cancel (left) and completion action (right) in full-screen modals
- Use popovers for small amounts of info on iPad only

**Don't:**
- Use popovers on iPhone (compact) — use `.sheet` instead
- Nest multiple sheets
- Use modal sheets for long, complex multi-step workflows
- Hide critical actions inside a sheet without visible alternatives

---

## Related Components

- [navigation-bar.md](navigation-bar.md) — Cancel/Done buttons in sheet navigation bar
- [buttons.md](buttons.md) — button styles for sheet actions
