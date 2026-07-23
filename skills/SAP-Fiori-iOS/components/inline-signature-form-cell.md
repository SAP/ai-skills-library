# Inline Signature Form Cell — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIInlineSignatureFormCell`, `FUIInlineSignatureFormView`, SwiftUI `SignatureCaptureView`

## What is it?

The inline signature form cell allows users to enter their signature directly within a form to verify identity and express consent. Unlike the standalone signature capture component, this component's interaction is integrated into the form — the user can review surrounding content while signing.

---

## When to Use

**Do:**
- Use when user consent is required
- Use a concise header to communicate the purpose and importance of the signature
- Use an asterisk (*) next to the header to indicate the signature is required

**Don't:**
- Use for insignificant or non-essential tasks

---

## Anatomy

```
A. Header: "Signature *"                    [Cancel]  ← Cancel hidden initially
──────────────────────────────────────────────────────
│                                                    │
│  B. Signature Canvas                               │
│  (inactive → tap to activate)                      │
│                                                    │
──────────────────────────────────────────────────────
C. Footer: [Clear]  [Save]  /  [Re-enter Signature]  ← hidden initially
```

### A. Header
Label describing the signature purpose. Shows an asterisk (*) when required. "Cancel" button is **hidden initially** — appears when the canvas is active.

### B. Signature Canvas
Drawable area for freehand input. Initially inactive. Tap once to activate.

### C. Footer
**Hidden initially.** Appears when the canvas is activated. Contains:
- **Active state**: Clear, Save
- **Saved state**: Re-enter Signature

---

## Lifecycle / States

| State | Canvas | Footer | Header Cancel |
|-------|--------|--------|---------------|
| **Inactive** | Not drawable | Hidden | Hidden |
| **Active** | Drawable | Visible (Clear/Save both disabled) | Visible |
| **Signed** | Drawing in progress | Visible (Clear/Save enabled) | Visible |
| **Saved** | Read-only, shows signature | "Re-enter Signature" | Hidden |

### State Transitions

```
Inactive ──tap canvas──► Active ──start drawing──► Signed
    ▲                        │                        │
    │                     Cancel                   Cancel / Clear
    │                        │                        │
    └────────────────────────┴────────────────────────┘

Signed ──Save──► Saved ──Re-enter Signature──► Inactive (cleared)
```

- **Inactive → Active**: tap anywhere on the canvas
- **Active → Inactive**: tap Cancel
- **Active → Signed**: start drawing
- **Signed → Active**: tap Clear
- **Signed → Saved**: tap Save
- **Signed → Inactive**: tap Cancel (clears signature)
- **Saved → Inactive (cleared)**: tap Re-enter Signature

---

## SwiftUI Code Examples

### Basic inline signature form cell
```swift
import FioriSwiftUICore

@State private var signatureImage: UIImage? = nil
@State private var isSigned = false

SignatureCaptureView(
    title: AttributedString("Signature *"),
    isRequired: true,
    onSave: { image in
        signatureImage = image
        isSigned = true
    },
    onDelete: {
        signatureImage = nil
        isSigned = false
    },
    watermark: AttributedString("Authorized Signature"),
    signatureLineColor: Color.preferredColor(.separator),
    cropsImage: true
)
```

### Inside a form (standard workflow)
```swift
struct ApprovalFormView: View {
    @State private var approverName = ""
    @State private var comments = ""
    @State private var signatureImage: UIImage? = nil

    var isFormComplete: Bool {
        !approverName.isEmpty && signatureImage != nil
    }

    var body: some View {
        NavigationStack {
            Form {
                Section("Approver Details") {
                    TextFieldFormView(
                        title: { Text("Approver Name") },
                        text: $approverName,
                        isRequired: true
                    )
                    NoteFormView(
                        title: { Text("Comments") },
                        text: $comments
                    )
                }

                // Inline signature always last — user reviews content above while signing
                Section {
                    SignatureCaptureView(
                        title: AttributedString("Signature *"),
                        isRequired: true,
                        onSave: { image in signatureImage = image },
                        onDelete: { signatureImage = nil },
                        cropsImage: true
                    )
                }
            }
            .navigationTitle("Approve Request")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .primaryAction) {
                    FioriButton { _ in Text("Submit") }
                        .fioriButtonStyle(FioriPrimaryButtonStyle())
                        .disabled(!isFormComplete)
                        .onTapGesture { submitApproval() }
                }
            }
        }
    }
}
```

### Showing the saved signature preview
```swift
if let signature = signatureImage {
    VStack(alignment: .leading, spacing: 8) {
        Text("Signature *")
            .font(.fiori(forTextStyle: .subheadline))
            .foregroundStyle(Color.preferredColor(.secondaryLabel))

        Image(uiImage: signature)
            .resizable()
            .scaledToFit()
            .frame(maxHeight: 80)
            .padding(8)
            .background(Color.preferredColor(.secondaryBackground))
            .clipShape(RoundedRectangle(cornerRadius: 8))

        FioriButton { _ in Text("Re-enter Signature") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .onTapGesture {
                signatureImage = nil  // returns to inactive state
            }
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| State | Inactive | Initial render — no binding value |
| State | Active | Canvas focused / drawable |
| State | Signed | Drawing in progress |
| State | Saved | `signatureImage` non-nil, read-only canvas |
| Required | Yes | `isRequired: true` + asterisk in title |
| Watermark | Yes | `watermark: AttributedString(...)` |
| Crop | Yes | `cropsImage: true` (recommended) |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Place the inline signature at the **bottom** of the form — the user should review content above before signing
- Use an asterisk (*) in the header label when the signature is required
- Write a concise, purposeful header (e.g. "Approval Signature *", "Consent *")
- Crop the image before storing (`cropsImage: true`) to remove surrounding whitespace
- Disable the Submit button until a signature is saved

**Don't:**
- Use for low-stakes or non-essential tasks
- Place the signature canvas in the middle of a form
- Use the standalone `SignatureView` when the user needs to review form content while signing — use this inline variant instead

---

## Related Components

- [signature-view.md](signature-view.md) — standalone full-screen signature capture
- [forms.md](forms.md) — other form input cells
- [inline-validation.md](inline-validation.md) — required field validation
