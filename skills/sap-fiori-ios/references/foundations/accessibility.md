# Accessibility — Design Foundations

> SAP Fiori for iOS | Foundation
> Standards: WCAG 2.1, Apple HIG Accessibility

## What is it?

The iOS design system is designed to be compliant with accessibility standards. Components are flexible, readable, and adaptable for a wide range of users, including those with visual, motor, auditory, speech, or cognitive impairments.

---

## Color Contrast Ratio

Sufficient color contrast ensures text and visual elements are legible for all users, including those who are visually impaired or color-blind. If text appears faint against its background, check the contrast ratio.

**Process:**
1. Determine the current contrast ratio (use a color contrast calculator)
2. Determine the target ratio for the UI element type
3. Follow the Fiori color pairing system below

### Contrast Ratio Requirements

| Text / Element type | Minimum ratio | Pairing rule |
|--------------------|--------------|-------------|
| Small text (< 18pt regular, < 14pt bold) | **4.5:1** | Colors 5 steps apart in the palette |
| Large text (≥ 18pt regular, ≥ 14pt bold) | **3:1** | Colors 4 steps apart in the palette |
| Graphical objects, UI components | **3:1** | Colors 4 steps apart in the palette |
| High-contrast theme | **7:1** | Colors 7 steps apart in the palette |

### Color Pairing System (Horizon Palette)

The Horizon color palette is WCAG-compliant by design. Pair colors by counting steps apart in the spectrum:

| Target ratio | Steps apart | Example |
|-------------|------------|---------|
| 4.5:1 | 5 steps | Color 4 paired with Color 9 |
| 3:1 | 4 steps | Color 4 paired with Color 8 |
| 7:1 | 7 steps | Color 4 paired with Color 11 |

```swift
// ✅ Semantic tokens already comply with contrast requirements
Text("Invoice #1234")
    .foregroundStyle(Color.preferredColor(.primaryLabel))   // on .primaryBackground
    // Automatically meets 4.5:1

// ✅ Always use semantic tokens — never raw palette colors in UI
// ❌ Color.preferredColor(.grey4) on Color.preferredColor(.grey7) — verify manually
```

### Increase Contrast Mode

The Fiori color palette includes an "Increase Contrast" variant that automatically activates when the user enables **Settings → Accessibility → Increase Contrast** on iOS. App foreground and background colors are enhanced automatically.

> Note: Increase Contrast enhances visibility but does not guarantee a 7:1 ratio in all cases.

```swift
// Colors adapt automatically — no code change needed
// Use Color.preferredColor(.token) and it handles all contrast modes
Color.preferredColor(.primaryLabel, display: .device)  // adapts to Increase Contrast setting
Color.preferredColor(.primaryLabel, display: .highConstant)  // force high contrast
```

---

## Dynamic Type

### Built-In Text Styles

Apply `Font.fiori(forTextStyle:)` to support Dynamic Type. This allows users to choose their preferred text size in iOS settings, and automatically adjusts tracking and leading for every size.

**Never use fixed font sizes for body/label text.** Only use `Font.fiori(fixedSize:)` for KPI numbers where layout precision matters more than scaling.

```swift
// ✅ Scales with Dynamic Type
Text("Invoice Vendor")
    .font(.fiori(forTextStyle: .subheadline))

// ❌ Does not scale
Text("Invoice Vendor")
    .font(.fiori(fixedSize: 15))
```

### Design Patterns for Large Text

#### 1. Prioritizing Content
At very large text sizes, hide lower-priority content to keep the most important information readable.

```swift
@Environment(\.dynamicTypeSize) var typeSize

ObjectItem {
    Text(invoice.number)
} subtitle: {
    Text(invoice.vendor)
} footnote: {
    // Hide at AX sizes — description becomes secondary
    if typeSize < .accessibility3 {
        Text(invoice.description)
    }
}
```

#### 2. Rearranging Layouts
At very large text sizes, rearrange components so text labels have more space to grow.

```swift
@Environment(\.dynamicTypeSize) var typeSize

// ObjectHeader: move image and status above text at AX sizes
if typeSize >= .accessibility3 {
    VStack(alignment: .leading) {
        HStack {
            thumbnailView
            statusView
        }
        titleAndSubtitleView
    }
} else {
    HStack {
        thumbnailView
        VStack(alignment: .leading) {
            titleAndSubtitleView
            statusView
        }
    }
}
```

#### 3. Stacking Text Labels
Form cells stack key label and value vertically at large text sizes. Never truncate — allow text to wrap.

```swift
@Environment(\.dynamicTypeSize) var typeSize

// Stack key/value vertically at large sizes
if typeSize >= .xxxLarge {
    VStack(alignment: .leading, spacing: 4) {
        Text(key).foregroundStyle(Color.preferredColor(.secondaryLabel))
        Text(value)
    }
} else {
    HStack {
        Text(key).foregroundStyle(Color.preferredColor(.secondaryLabel))
        Spacer()
        Text(value)
    }
}
```

#### General Dynamic Type rules
- Allow text to wrap — never truncate labels at large sizes
- Test at **AX5** (the largest accessibility size) — this is where layout breaks most often
- Use `.lineLimit(nil)` for any label that might truncate at large sizes
- Use `ViewThatFits` or `@Environment(\.dynamicTypeSize)` to switch layouts

---

## VoiceOver

```swift
// Required: label every icon-only interactive element
FioriButton { _ in Image(systemName: "trash") }
    .accessibilityLabel("Delete invoice")

// Group related elements
VStack {
    Text("Invoice #1234")
    Text("Due: 30 Jan 2026")
    Text("$1,450.00")
}
.accessibilityElement(children: .combine)

// Hide decorative elements
Image("decorative-wave")
    .accessibilityHidden(true)

// Custom actions
ObjectItem { Text("Order #5678") }
    .accessibilityAction(named: "Approve") { approveOrder() }
    .accessibilityAction(named: "Reject") { rejectOrder() }
```

---

## Minimum Touch Target

All interactive elements must be at least **44×44pt**:

```swift
FioriButton { _ in
    Image(systemName: "ellipsis")
}
.frame(minWidth: 44, minHeight: 44)
```

---

## Reduce Motion

```swift
@Environment(\.accessibilityReduceMotion) var reduceMotion

someView
    .animation(reduceMotion ? .none : .spring(response: 0.3), value: isExpanded)
```

---

## iOS Accessibility Features

Beyond color contrast and Dynamic Type, iOS provides: VoiceOver, reading support, Switch Control, dictation, and more. See [Accessibility on iOS](https://www.apple.com/accessibility/iphone/) and the [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/accessibility).

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use semantic color tokens — they are already WCAG-compliant by design
- Use `Font.fiori(forTextStyle:)` for all body/label text — never fixed sizes
- Test at AX5 Dynamic Type size
- Add `.accessibilityLabel()` to every icon-only button
- Respect `.accessibilityReduceMotion`
- Meet 44×44pt minimum touch targets

**Don't:**
- Hardcode colors and verify contrast manually — use the semantic token system
- Use color as the only indicator of state (add icon or text too)
- Truncate text at large Dynamic Type sizes — wrap instead
- Use `.accessibilityHidden(true)` on interactive elements

---

## Related Foundations

- [colors.md](colors.md) — full color token reference and contrast pairing
- [typography.md](typography.md) — SAP 72 font and Dynamic Type styles
