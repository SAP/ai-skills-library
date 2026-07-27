# Sibling Navigation — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIPageViewController`

## What is it?

Sibling navigation lets users move between child objects at the same level of a hierarchy — for example, stepping through work orders, instructional steps, or hardware components in a list.

---

## When to Use

**Do:**
- Use when there is a sequence of objects (work orders, instructional steps, hardware components)

**Don't:**
- Use to replace hierarchical navigation between parent and child objects — sibling nav is only for moving between children
- Use when there is no sequence of objects in the app

---

## Anatomy

Sibling navigation uses two existing components — the **navigation bar two-line title** and the **toolbar**:

```
Navigation bar:
  Upper line:  "3 of 12"         ← current / total count
  Lower line:  "Work Orders"     ← parent object name

Toolbar:
  [← Previous]              [Next →]
```

**A. Navigation bar info**
- Upper line: current position and total count (e.g. "3 of 12")
- Lower line: parent object name

**B. Toolbar buttons**
- Previous: push-transitions to the previous child view
- Next: push-transitions to the next child view

Navigation between siblings uses a **push transition**.

---

## Variations

| Variation | When to use |
|-----------|-------------|
| **Text-based** | App has a toolbar with action buttons; or app has no toolbar. Use for both compact and regular. |
| **Icon-based** | App has a toolbar with 2+ action buttons; toolbar is icon-based. **Compact width only.** |

> Use text-based sibling nav on regular width — there is enough space for full text. Icon-based is only for compact.

---

## Adaptive Design

Both compact and regular follow standard toolbar behavior and adapt accordingly.

---

## SwiftUI Code Examples

### Text-based sibling navigation
```swift
import SwiftUI

struct WorkOrderDetailView: View {
    let items: [WorkOrder]
    @State private var currentIndex: Int

    init(items: [WorkOrder], startIndex: Int = 0) {
        self.items = items
        self._currentIndex = State(initialValue: startIndex)
    }

    var body: some View {
        WorkOrderContent(item: items[currentIndex])
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                // Two-line title: "3 of 12" / "Work Orders"
                ToolbarItem(placement: .principal) {
                    VStack(spacing: 2) {
                        Text("\(currentIndex + 1) of \(items.count)")
                            .font(.fiori(forTextStyle: .headline))
                            .foregroundStyle(Color.preferredColor(.primaryLabel))
                        Text("Work Orders")
                            .font(.fiori(forTextStyle: .footnote))
                            .foregroundStyle(Color.preferredColor(.secondaryLabel))
                    }
                }

                // Text-based Previous / Next in toolbar
                ToolbarItemGroup(placement: .bottomBar) {
                    FioriButton { _ in
                        HStack(spacing: 4) {
                            Image(systemName: "chevron.backward")
                            Text("Previous")
                        }
                    }
                    .fioriButtonStyle(FioriTertiaryButtonStyle())
                    .disabled(currentIndex == 0)
                    .onTapGesture {
                        withAnimation { currentIndex -= 1 }
                    }

                    Spacer()

                    FioriButton { _ in
                        HStack(spacing: 4) {
                            Text("Next")
                            Image(systemName: "chevron.forward")
                        }
                    }
                    .fioriButtonStyle(FioriTertiaryButtonStyle())
                    .disabled(currentIndex == items.count - 1)
                    .onTapGesture {
                        withAnimation { currentIndex += 1 }
                    }
                }
            }
    }
}
```

### Icon-based sibling navigation (compact only)
```swift
// Use when toolbar already has 2+ action buttons
ToolbarItemGroup(placement: .bottomBar) {
    FioriButton { _ in
        Image(systemName: "chevron.backward")
            .accessibilityLabel("Previous")
    }
    .fioriButtonStyle(FioriTertiaryButtonStyle())
    .disabled(currentIndex == 0)
    .onTapGesture { currentIndex -= 1 }

    Spacer()

    // Other toolbar action buttons
    FioriButton { _ in Image(systemName: "square.and.arrow.up").accessibilityLabel("Share") }
        .fioriButtonStyle(FioriTertiaryButtonStyle())
    FioriButton { _ in Image(systemName: "pencil").accessibilityLabel("Edit") }
        .fioriButtonStyle(FioriTertiaryButtonStyle())

    Spacer()

    FioriButton { _ in
        Image(systemName: "chevron.forward")
            .accessibilityLabel("Next")
    }
    .fioriButtonStyle(FioriTertiaryButtonStyle())
    .disabled(currentIndex == items.count - 1)
    .onTapGesture { currentIndex += 1 }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Variation | Text-based | `Text("Previous")` / `Text("Next")` in toolbar |
| Variation | Icon-based (compact) | `Image(systemName: "chevron.backward/forward")` |
| Nav bar | Two-line title | `ToolbarItem(placement: .principal)` with `VStack` |
| Upper line | "X of Y" | `Text("\(currentIndex + 1) of \(items.count)")` |
| Lower line | Parent name | `Text(parentName)` in secondary style |
| Previous | Disabled at first | `.disabled(currentIndex == 0)` |
| Next | Disabled at last | `.disabled(currentIndex == items.count - 1)` |
| Transition | Push | `withAnimation { currentIndex += 1 }` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Show current position and total count in the upper nav bar line
- Show the parent object name in the lower nav bar line
- Disable Previous at the first item and Next at the last item
- Use text labels for regular width; icon-only for compact with 2+ toolbar actions

**Don't:**
- Use to navigate between parent and child objects — sibling nav is lateral, not hierarchical
- Use icon-based variation on regular width — use text-based instead

---

## Related Components

- [navigation-bar.md](navigation-bar.md) — two-line title placement
- [tab-bar.md](tab-bar.md) — app-level navigation between sections
