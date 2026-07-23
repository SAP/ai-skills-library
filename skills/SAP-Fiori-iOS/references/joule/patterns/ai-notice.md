# AI Notice — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns

## What is it?

The Joule AI notice is a legal disclaimer accessible from the overflow menu in the panel header. It contains a link to Joule Data Protection and Privacy information and must be accessible at all times.

---

## Rules

**Do:**
- Include a link to the Joule Data Protection and Privacy page
- Include a "Back to Conversation" button
- Make accessible at any time while Joule is open

**Don't:**
- Modify the copy or link without legal team approval

---

## Anatomy

**A. Header** — panel title ("Joule") + close button (✕)
**B. Title** — "AI Notice"
**C. Content:**
- "Powered by SAP Business AI, for more information visit"
- "Joule Data Protection and Privacy" — link to legal page

**D. Button** — "Back to Conversation" — returns user to Joule panel

---

## Behavior

- Accessed via overflow menu (•••) in panel header
- Tap "Back to Conversation" → returns to Joule panel

---

## Variations

| Variant | Description |
|---------|-------------|
| Full-size | Default panel height |
| Medium-size | User swipes full-size down → medium sheet |

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct JouleAINoticeView: View {
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            VStack(spacing: 24) {
                // B. Title
                Text("AI Notice")
                    .font(.fiori(forTextStyle: .title2, weight: .bold))
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .padding(.horizontal, 16)

                // C. Content
                VStack(alignment: .leading, spacing: 8) {
                    Text("Powered by SAP Business AI, for more information visit")
                        .font(.fiori(forTextStyle: .body))
                        .foregroundStyle(Color.preferredColor(.primaryLabel))

                    Link("Joule Data Protection and Privacy",
                         destination: URL(string: "https://www.sap.com/joule-privacy")!)
                        .font(.fiori(forTextStyle: .body))
                        .foregroundStyle(Color.preferredColor(.tintColor))
                }
                .padding(.horizontal, 16)

                Spacer()

                // D. Back to Conversation button
                FioriButton { _ in Text("Back to Conversation") }
                    .fioriButtonStyle(FioriPrimaryButtonStyle())
                    .frame(maxWidth: .infinity)
                    .padding(.horizontal, 16)
                    .padding(.bottom, 32)
            }
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .principal) {
                    Text("Joule")
                        .font(.fiori(forTextStyle: .headline, weight: .bold))
                }
                ToolbarItem(placement: .cancellationAction) {
                    Button { dismiss() } label: {
                        Image(systemName: "xmark")
                    }
                }
            }
        }
        .presentationDetents([.large, .medium])
        .presentationDragIndicator(.visible)
    }
}

// Access from overflow menu in panel header
Menu {
    Button("AI Notice") { showAINotice = true }
    // other overflow items
} label: {
    Image(systemName: "ellipsis.circle")
}
.sheet(isPresented: $showAINotice) {
    JouleAINoticeView()
}
```

---

## Related

- [../components/joule-panel.md](../components/joule-panel.md)
- [../../in-app-ai-design/patterns/ai-acknowledgement.md](../../in-app-ai-design/patterns/ai-acknowledgement.md)
