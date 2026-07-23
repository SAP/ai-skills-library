# Contact Cell — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Table View Cells
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIContactCell`, SwiftUI `ContactItem`

## What is it?

The contact cell is a table view cell that gives quick access to communication methods for a contact. Commonly used in object and object details floorplans.

---

## Anatomy

```
[A. Detail Image]  B. Name          D. [📞] [📹] [💬] [✉️]
                   B. Title / Subtitle
                   C. Description (regular only)
```

**A. Detail Image** — avatar or photo on the far left. **Cannot be used if 4 action icons are included.**
**B. Name and Title** — contact name + optional subtitle/title.
**C. Description** (optional) — visible in **regular width only**. Good for addresses or longer context.
**D. Action Icons** — up to 4 communication actions: call, FaceTime, message, email.

---

## Actions

| Action | Behavior |
|--------|---------|
| Call | Alert asking to confirm call → phone call launches |
| FaceTime | Alert asking to confirm → FaceTime launches |
| Message | Modal where message can be drafted and sent immediately |
| Email | Modal where email can be drafted and sent immediately |
| Tap cell | Navigates to the contact's profile detail screen |

---

## Constraints

- If **4 action icons** are used, a **detail image cannot be used**
- Description is only shown in regular width
- The name/title and description container widths are flexible

---

## Adaptive Design

- Compact: name, title, action icons (no description)
- Regular: name, title, optional description, action icons
- Full-width variant available

---

## SwiftUI Code Examples

### Standard contact cell
```swift
import FioriSwiftUICore

ContactItem(
    title: AttributedString("Jane Smith"),
    subtitle: AttributedString("Engineering Lead"),
    descriptionText: AttributedString("SAP SE · Berlin"),
    detailImage: Image("jane_avatar"),
    activityItems: [
        ActivityItem(type: .phone, data: "+49-6227-747474"),
        ActivityItem(type: .email, data: "jane.smith@sap.com"),
        ActivityItem(type: .message, data: "+49-6227-747474")
    ]
)
```

### ViewBuilder form
```swift
ContactItem {
    Text("Jane Smith")
        .font(.fiori(forTextStyle: .headline))
} subtitle: {
    Text("Engineering Lead")
        .foregroundStyle(Color.preferredColor(.secondaryLabel))
} descriptionText: {
    // Only show on regular width
    Text("Building 4, Floor 3 · SAP SE · Berlin")
        .foregroundStyle(Color.preferredColor(.tertiaryLabel))
} detailImage: {
    AsyncImage(url: user.avatarURL) { image in
        image.resizable()
            .aspectRatio(contentMode: .fill)
            .clipShape(Circle())
    } placeholder: {
        Circle()
            .fill(Color.preferredColor(.accentBackground2))
            .overlay(
                Text(user.initials)
                    .font(.fiori(forTextStyle: .subheadline))
                    .foregroundStyle(Color.preferredColor(.accentLabel2))
            )
    }
    .frame(width: 44, height: 44)
} activityItems: {
    ActivityItems {
        ActivityItem(type: .phone, data: user.phone)
        ActivityItem(type: .email, data: user.email)
        ActivityItem(type: .message, data: user.phone)
    }
}
```

### 4 actions — no detail image
```swift
ContactItem(
    title: AttributedString("John Doe"),
    subtitle: AttributedString("Sales Manager"),
    // No detailImage — 4 actions used
    activityItems: [
        ActivityItem(type: .phone, data: "+1-555-0100"),
        ActivityItem(type: .facetime, data: "+1-555-0100"),
        ActivityItem(type: .message, data: "+1-555-0100"),
        ActivityItem(type: .email, data: "john@example.com")
    ]
)
```

### In a contacts list
```swift
List(contacts) { contact in
    ContactItem(
        title: AttributedString(contact.name),
        subtitle: AttributedString(contact.role),
        detailImage: Image(contact.avatarName),
        activityItems: contact.activityItems
    )
    .onTapGesture { navigateToProfile(contact) }
}
.navigationTitle("Contacts")
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Detail image | Photo | `AsyncImage` + `clipShape(Circle())` |
| Detail image | Initials | `Circle` fill + `Text` overlay |
| Detail image | None (4 actions) | Omit `detailImage` |
| Description | Yes (regular) | `descriptionText: { Text(...) }` |
| Description | No (compact) | Omit or hide via size class |
| Actions | 1–3 | `ActivityItems { }` |
| Actions | 4 | `ActivityItems { }` — no detail image |
| Tap cell | Navigates | `.onTapGesture { navigateToProfile() }` |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Show description only on regular width
- Omit the detail image when using 4 action icons
- Navigate to profile detail screen on cell tap
- Show action confirmation alerts for call and FaceTime

**Don't:**
- Use more than 4 action icons
- Show both 4 actions and a detail image

---

## Related Components

- [profile-header.md](profile-header.md) — full profile screen header
- [avatars.md](avatars.md) — avatar sizing and shape rules
- [object-item.md](object-item.md) — general list row (no contact-specific actions)
