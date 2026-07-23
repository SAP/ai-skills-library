# Elevation — Design Foundations

> SAP Fiori for iOS | Foundation

## What is it?

Elevation is the virtual height of an interface element above the background surface, expressed through shadows and blur effects (materials). SAP Fiori iOS uses subtle translucent materials and minimal shadows to create layered depth aligned with iOS's minimalist design language.

---

## Shadows

Shadows make key interface elements stand out and appear interactive — cards, modals, actionable components. Use soft, diffused shadows that mimic real-world lighting while maintaining visual harmony.

### Elevation Levels

Five levels (0–4) establish visual hierarchy. Higher levels guide user attention to more prominent/interactive content.

| Level | Token | Use for |
|-------|-------|---------|
| 0 | `.cardShadow` @ none | Modal and non-modal sheets (no shadow) |
| 1 | — | N/A |
| 2 | `.cardShadow` | Cards |
| 3 | `.cardShadow` (stronger) | Toast messages, quick sort menus |
| 4 | `.cardShadow` (strongest) | Popovers |

```swift
// Cards (Level 2)
VStack { content }
    .background(Color.preferredColor(.secondaryGroupedBackground))
    .clipShape(RoundedRectangle(cornerRadius: 12))
    .shadow(color: Color.preferredColor(.cardShadow), radius: 4, x: 0, y: 2)

// Toast / popover (Level 3–4)
VStack { content }
    .background(Color.preferredColor(.secondaryGroupedBackground))
    .clipShape(RoundedRectangle(cornerRadius: 12))
    .shadow(color: Color.preferredColor(.cardShadow), radius: 8, x: 0, y: 4)
```

---

## Materials

Apple's materials use blur and transparency to create layered depth. They integrate navigation bars, modals, toolbars, and contextual menus while maintaining immersive visual harmony.

### Material Thickness and Focus

| Thickness | Background blur | Use for |
|-----------|----------------|---------|
| Thick | Heavy blur | Strong element separation (action sheets, alerts) |
| Regular | Moderate blur | Standard overlays |
| Thin | Light blur | Subtle separation |
| UltraThin | Minimal blur | Barely-there separation |
| Chrome | Adaptive | Navigation bars, tab bars, toolbars — system chrome |

**Rule:** Thicker = more focus on foreground; thinner = more background context preserved.

### Vibrancy

Vibrancy increases brightness and contrast on blurred backgrounds, keeping text, icons, and buttons legible and prominent against material surfaces.

### Material Colors (SAP)

| Token | Use |
|-------|-----|
| `.chrome` | Navigation bar, tab bar, toolbar, sibling nav — translucency when content scrolls underneath |
| `.chromeSecondary` | Same context but for page/modal views with secondary backgrounds |

### Practical Usage

```swift
// Navigation bar — materials handled automatically by system
// Just set the translucency intent:
.toolbarBackground(.automatic, for: .navigationBar)  // default
.toolbarBackground(.visible, for: .navigationBar)    // always visible

// Tab bar — automatic
// No manual material configuration needed

// Action sheet — system applies Regular material automatically
.confirmationDialog("Delete?", isPresented: $showDialog) {
    Button("Delete", role: .destructive) { delete() }
    Button("Cancel", role: .cancel) {}
}

// Custom card with shadow
struct ElevatedCard<Content: View>: View {
    let level: Int  // 2 = card, 3 = toast, 4 = popover
    let content: Content

    var shadowRadius: CGFloat { CGFloat(level * 2) }
    var shadowY: CGFloat { CGFloat(level) }

    var body: some View {
        content
            .background(Color.preferredColor(.secondaryGroupedBackground))
            .clipShape(RoundedRectangle(cornerRadius: 12))
            .shadow(
                color: Color.preferredColor(.cardShadow),
                radius: shadowRadius,
                x: 0,
                y: shadowY
            )
    }
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Always use `.cardShadow` token — never hardcode shadow colors
- Clip views before applying shadows (`.clipShape` before `.shadow`)
- Use materials for nav bars, toolbars, and tab bars — let the system handle them
- Apply thicker materials for action sheets and alerts; thinner for navigation elements

**Don't:**
- Apply shadows to list rows (flat surfaces stay flat)
- Use multiple layered shadows on a single view
- Hardcode shadow colors or opacity values

---

## Related Components

- [navigation-bar.md](../components/navigation-bar.md)
- [tab-bar.md](../components/tab-bar.md)
- [toolbar.md](../components/toolbar.md)
- [cards.md](../components/cards.md)
