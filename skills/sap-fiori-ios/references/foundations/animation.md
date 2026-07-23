# Animation — Design Foundations

> SAP Fiori for iOS | Foundation

## What is it?

SAP Fiori for iOS uses four standard transition types. Use the system-provided transitions — do not override them unless specifically required.

---

## Transition Types

### Push
Eases a new screen in from the side while the prior screen slides out the opposite direction. Standard for **drill-down navigation** in `NavigationStack`.

```swift
// Push is automatic in NavigationStack — do not override
NavigationStack {
    List(items) { item in
        NavigationLink(destination: DetailView(item: item)) {
            ObjectItem { Text(item.title) }
        }
    }
}
```

### Modal
A new window slides up from the bottom, covering the content below. Used to present tasks that require completion or cancellation before the user resumes other actions.

```swift
// Modal slides up automatically — do not override
.sheet(isPresented: $showModal) { FormView() }
.fullScreenCover(isPresented: $showFullScreen) { DetailView() }
```

### Zoom In / Out
Used to make images or documents larger for detailed viewing.

```swift
// System default zoom — do not override
.quickLookPreview($previewURL)
// or use NavigationTransition.zoom for custom zoom
```

### Dissolve
Gently fades between two screens. **Recommended for enabling and closing edit mode.**

```swift
// Dissolve for edit mode transition
withAnimation(.easeInOut(duration: 0.25)) {
    isEditing.toggle()
}

// Apply to the view change
if isEditing {
    EditModeView()
        .transition(.opacity)
} else {
    ReadModeView()
        .transition(.opacity)
}
```

---

## Animation Specs (Component-level)

| Interaction | Animation |
|-------------|-----------|
| Button tap press | `.scaleEffect(0.97)` + `.spring(response: 0.2, dampingFraction: 0.8)` |
| View appear | `.opacity(0→1)` + `.offset(y: 8→0)` + `.easeOut(duration: 0.25)` |
| Sheet present | System default — do not override |
| List row tap | `.opacity` feedback, `duration: 0.15` |
| Navigation push | System default — do not override |
| Toggle switch | System default — do not override |
| Loading/skeleton | `.opacity(0.3→1.0)` repeating, `.easeInOut(duration: 0.9)` |
| Error shake | `.offset(x: ±6)` × 3 cycles, `duration: 0.07` each |
| Edit mode enable/disable | `.opacity` dissolve, `.easeInOut(duration: 0.25)` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use Push for drill-down navigation
- Use Modal for task-focused windows
- Use Dissolve for edit mode transitions
- Respect `.accessibilityReduceMotion` — remove or simplify animations when enabled

**Don't:**
- Override system Push and Modal transitions
- Add custom animations to navigation gestures
- Animate for decoration — only animate to guide attention or communicate state

```swift
@Environment(\.accessibilityReduceMotion) var reduceMotion

someView
    .animation(reduceMotion ? .none : .spring(response: 0.3), value: isExpanded)
```
