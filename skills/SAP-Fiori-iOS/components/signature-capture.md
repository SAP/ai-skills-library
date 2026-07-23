# Signature Capture — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUISignatureCaptureController`, `FUISignatureCaptureView`, SwiftUI `SignatureCaptureView`

## What is it?

Signature capture allows users to input their signature on screen to authorize workflows. The signature is captured as a bitmap or SVG with an optional watermark and saved to the backend.

**For forms requiring careful review of content during signing, use [Inline Signature Form Cell](inline-signature-form-cell.md) instead.**

---

## When to Use

- Signing forms or documents
- Approving orders
- Confirming tasks
- Indicating receipt of an article
- Signing off for another person

---

## Anatomy

```
A. Navigation Bar: [Cancel]   "Signature"   [Done]

B. Signature Canvas
   _______________________________________________
  |                                               |
  |                 ← signature line →            |
  |_______________________________________________|

C. Toolbar: [Clear]

D. Watermark (optional — added to saved image)
```

**A. Navigation Bar** — "Cancel" and "Done" buttons. Title defaults to "Signature" (customizable).
**B. Signature Canvas** — freehand drawing area with a signature line guide.
**C. Toolbar** — "Clear" button to erase and start over.
**D. Watermark** (optional) — text automatically added to the saved signature image.

---

## Entry Flows

### From a Button Form Cell
Tapping a button in a form opens the signature capture modal. After signing, the button can be replaced with the inline signature form cell showing the saved signature.

### As Part of Navigation Flow
Signature capture can be integrated as a full step in a screen flow (e.g. approval workflow step 3 of 4).

---

## Adaptive Design

Supported in compact and regular width on iPhone and iPad. Can be presented in:
- Modal sheet
- Bottom sheet
- Form sheet
- Popover

---

## SwiftUI Code Examples

### Presented from a button (bottom sheet)
```swift
import FioriSwiftUICore

@State private var showSignature = false
@State private var signatureImage: UIImage? = nil

FioriButton { _ in
    HStack {
        Image(systemName: "signature")
        Text(signatureImage == nil ? "Add Signature" : "Re-sign")
    }
}
.fioriButtonStyle(FioriSecondaryButtonStyle())
.onTapGesture { showSignature = true }
.sheet(isPresented: $showSignature) {
    SignatureCaptureView(
        onSave: { image in
            signatureImage = image
            showSignature = false
        },
        onDelete: { signatureImage = nil },
        title: AttributedString("Authorization Signature"),
        watermark: AttributedString("Authorized by \(currentUser.name)"),
        cropsImage: true
    )
    .presentationDetents([.medium, .large])
}
```

### As part of a navigation flow
```swift
NavigationStack {
    ApprovalStep1View()
        .navigationDestination(for: ApprovalStep.self) { step in
            switch step {
            case .details:   ApprovalDetailsView()
            case .signature: SignatureCaptureView(onSave: saveAndProceed)
            case .complete:  ApprovalCompleteView()
            }
        }
}
```

### Showing the saved signature in the form
```swift
if let sig = signatureImage {
    VStack(alignment: .leading, spacing: 8) {
        Text("Signature")
            .font(.fiori(forTextStyle: .subheadline))
            .foregroundStyle(Color.preferredColor(.secondaryLabel))

        Image(uiImage: sig)
            .resizable()
            .scaledToFit()
            .frame(maxHeight: 80)
            .padding(8)
            .background(Color.preferredColor(.secondaryBackground))
            .clipShape(RoundedRectangle(cornerRadius: 8))

        FioriButton { _ in Text("Re-sign") }
            .fioriButtonStyle(FioriTertiaryButtonStyle())
            .onTapGesture { showSignature = true }
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Title | Custom | `title: AttributedString(...)` |
| Watermark | Yes | `watermark: AttributedString(...)` |
| Watermark | No | Omit `watermark` |
| Crop | Yes (recommended) | `cropsImage: true` |
| Presentation | Bottom sheet | `.sheet` + `.presentationDetents([.medium, .large])` |
| Presentation | Form sheet | `.sheet` (iPad default) |
| Presentation | Popover | `.popover` (iPad) |
| Entry | From button | `FioriButton` → `.sheet` |
| Entry | Navigation flow | `NavigationStack` destination |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use `cropsImage: true` to remove surrounding whitespace before storing
- Customize the title to match the context ("Authorization Signature", not just "Signature")
- Replace the trigger button with the inline signature preview after signing
- Use inline signature form cell when the user needs to review form content while signing

**Don't:**
- Use signature capture as a security / authentication mechanism
- Make the canvas smaller than 300×150pt
- Store raw uncropped images — always crop

---

## Related Components

- [inline-signature-form-cell.md](inline-signature-form-cell.md) — signature within a form (review content while signing)
- [button-form-cell.md](button-form-cell.md) — trigger button for signature capture
