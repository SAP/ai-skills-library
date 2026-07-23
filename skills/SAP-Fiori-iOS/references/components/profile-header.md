# Profile Header — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Headers
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIProfileHeader`, SwiftUI `ProfileHeader`

## What is it?

The profile header helps the user recognize and learn more about a person. It may also allow the user to quickly contact that person without drilling down into contact details. Typically used in an object pattern or profile and settings screen.

---

## When to Use

**Do:**
- Use in an object pattern or profile and settings screen

**Don't:**
- Use without the full name of the person — name is always required

---

## Anatomy

Only the **title** (full name) is required. All other elements are optional.

```
         [A. Image / Avatar]         ← center-aligned on compact

           B. Full Name              ← required; tint color if tappable
           B. Role / Department

    C. Additional info line 1
    C. Additional info line 2 (or short paragraph)

   [D. Action icons: 2–5 max]        ← hidden on compact when description present

         [E. Button]                 ← optional action button
```

### A. Image
Not required but **highly recommended** — helps the user recognize the person. Falls back to initials if no photo.

### B. Main Content
Full name + one additional piece of information (role, department, etc.).

### C. Additional Information
Two short strings or a short paragraph of relevant text.

### D. Action Icons
Quick-contact actions (phone, email, message, etc.). Min **2**, max **5**. Fewer is better — only include frequently used actions in the current context. Disabled icons use grey color.

**Compact constraint:** When a description is present on compact, action icons are **not displayed**. Choose between contact actions or description — not both on compact.

### E. Button
Optional. Triggers an action on the object (add to list, start event, mark/bookmark). Toggles between active and inactive state on repeated taps. Text must clearly communicate what will happen.

---

## Behavior

### Scrolled State
As the user scrolls down, the header collapses. **Action icons remain visible** in the collapsed header state.

---

## Compact Layout
Content is always **center-aligned** on compact width. The designer must decide whether the primary purpose of this screen is:
- **Contact the person** → include action icons, omit description
- **Learn about the person** → include description, action icons will not show

---

## Variations

### Profile Header with Action Icons
2–5 action icons for instant contact. Max 5 is possible but not recommended — only show what's relevant to the context.

```swift
import FioriSwiftUICore

ProfileHeader {
    Text("Jane Smith")
        .font(.fiori(forTextStyle: .title2))
} subtitle: {
    Text("Engineering Lead")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
} descriptionText: {
    Text("SAP SE · Cloud Engineering · Berlin")
        .foregroundStyle(Color.preferredColor(.tertiaryLabel))
} detailImage: {
    AsyncImage(url: user.avatarURL) { image in
        image.resizable()
            .aspectRatio(contentMode: .fill)
            .clipShape(Circle())
    } placeholder: {
        Circle()
            .fill(Color.preferredColor(.accentBackground3))
            .overlay(
                Text(user.initials)
                    .font(.fiori(forTextStyle: .largeTitle))
                    .foregroundStyle(Color.preferredColor(.accentLabel3))
            )
    }
    .frame(width: 80, height: 80)
} activityItems: {
    ActivityItems {
        ActivityItem(type: .phone, data: "+49-6227-747474")
        ActivityItem(type: .email, data: "jane.smith@sap.com")
        ActivityItem(type: .message, data: "+49-6227-747474")
    }
}
```

### Profile Header with Tappable Name
Name displayed in tint color as an entry point to drill into more details about the person.

```swift
ProfileHeader {
    // Tint color signals the name is tappable
    Text("Jane Smith")
        .font(.fiori(forTextStyle: .title2))
        .foregroundStyle(Color.preferredColor(.tintColor))
} subtitle: {
    Text("Engineering Lead")
} detailImage: {
    Image("jane_avatar")
        .resizable()
        .clipShape(Circle())
        .frame(width: 80, height: 80)
}
.onTapGesture { navigateToProfile(user) }
```

### Profile Header with Action Button (toggle)
```swift
@State private var isFollowing = false

ProfileHeader {
    Text("Jane Smith")
} subtitle: {
    Text("Engineering Lead")
} detailImage: {
    Image("jane_avatar")
        .resizable()
        .clipShape(Circle())
        .frame(width: 80, height: 80)
} action: {
    FioriButton(isSelectionPersistent: true) { state in
        Text(state == .selected ? "Following" : "Follow")
    } image: { state in
        Image(systemName: state == .selected
              ? "person.fill.checkmark"
              : "person.badge.plus")
    }
    .fioriButtonStyle(FioriSecondaryButtonStyle())
    // Active state = selected, inactive = normal
}
```

### Compact — description vs. action icons (choose one)
```swift
@Environment(\.horizontalSizeClass) var hSizeClass

ProfileHeader {
    Text("Jane Smith")
} subtitle: {
    Text("Engineering Lead")
} detailImage: {
    Image("jane_avatar")
        .resizable()
        .clipShape(Circle())
        .frame(width: 80, height: 80)
} descriptionText: {
    // Only show description on compact when contact actions are not needed
    if hSizeClass == .compact {
        Text("Leads the Cloud Engineering team. 12 years at SAP.")
            .foregroundStyle(Color.preferredColor(.secondaryLabel))
    }
} activityItems: {
    // Only show actions on compact when description is not present
    if hSizeClass != .compact {
        ActivityItems {
            ActivityItem(type: .phone, data: user.phone)
            ActivityItem(type: .email, data: user.email)
        }
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Image | Photo | `AsyncImage` + `clipShape(Circle())` |
| Image | Initials | `Circle` fill + `Text` overlay |
| Image | None | Omit `detailImage` |
| Name | Tappable | `.foregroundStyle(Color.preferredColor(.tintColor))` + `.onTapGesture` |
| Name | Static | `.foregroundStyle(Color.preferredColor(.primaryLabel))` |
| Action icons | 2–5 | `ActivityItems { ActivityItem(...) }` |
| Action icon | Disabled | `.foregroundStyle(Color.preferredColor(.tertiaryLabel))` |
| Button | Toggle (shape) | `FioriButton(isSelectionPersistent: true)` |
| Button | Emphasized | `FioriPrimaryButtonStyle()` |
| Description | Yes (compact) | Omit action icons |
| Description | Yes (regular) | Can coexist with action icons |
| Alignment | Compact | Center-aligned (automatic) |
| Alignment | Regular | Layout adapts (automatic) |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Always include the full name
- Decide upfront for compact: contact actions OR description — not both
- Use tint color for the name when it navigates to more details
- Include action icons only for the most relevant contact methods in context
- Apply grey color to disabled action icons
- Make the action button toggle between active and inactive states clearly

**Don't:**
- Use without the person's full name
- Show more than 5 action icons (and avoid even that many)
- Show both description and action icons on compact width
- Use profile header for non-person objects — use `ObjectHeader` instead

---

## Related Components

- [contact-item.md](contact-item.md) — list row version for people
- [object-header.md](object-header.md) — header for non-person business objects
- [avatars.md](avatars.md) — avatar sizing and shape rules
