# Confirmation Step — Joule Pattern

> SAP Fiori for iOS | Joule / Patterns

## What is it?

A confirmation step verifies Joule correctly understood a user's request before executing, especially for high-stakes or irreversible actions.

---

## Rules

**Do:** Use for high-stakes or irreversible actions.
**Don't:** Use when the system can proceed without further input. Don't use for easily undoable actions. Don't overload the flow with too many confirmations.

**Tips:**
- Guide users to next step when applicable
- Never use "Cancel" as a label — use "Go Back" to avoid confusion

---

## Anatomy

**A. Header** — title stating the confirmation purpose
**B. Description** — details the action + prompts user to decide
**C. "Go Back" button** — mandatory; cancels without confirming; closes confirmation
**D. "Confirm" button** — primary; confirms and proceeds

---

## Behavior

- Confirmation step slides up from the bottom
- Blocks the input field; all chat actions disabled while visible
- "Go Back" → step disappears, action cancelled
- "Confirm" → Joule sends feedback message about the action result

---

## SwiftUI Code Example

```swift
struct JouleConfirmationStep: View {
    let title: String
    let description: String
    let onGoBack: () -> Void
    let onConfirm: () -> Void

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            Text(title)
                .font(.fiori(forTextStyle: .headline))
            Text(description)
                .font(.fiori(forTextStyle: .body))
                .foregroundStyle(Color.preferredColor(.secondaryLabel))
            HStack(spacing: 12) {
                FioriButton { _ in Text("Go Back") }  // ✅ not "Cancel"
                    .fioriButtonStyle(FioriSecondaryButtonStyle())
                    .onTapGesture { onGoBack() }
                FioriButton { _ in Text("Confirm") }
                    .fioriButtonStyle(FioriPrimaryButtonStyle())
                    .onTapGesture { onConfirm() }
            }
        }
        .padding(16)
        .background(Color.preferredColor(.secondaryGroupedBackground))
        .clipShape(RoundedRectangle(cornerRadius: 12))
    }
}
```

---

## Related

- [error-handling.md](error-handling.md)
