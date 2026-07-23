# OCR Scanner — Pattern Guide

> SAP Fiori for iOS | Patterns / Scanner
> Development reference: Optical Character Recognition (OCR) SDK

## What is it?

The OCR scanner recognizes text from a physical object or document and automatically enters it into a form field. Used as an alternative input method when the user is completing a form.

---

## Anatomy

Full-screen modal:

**A. Navigation Bar** — "Cancel", title, optional settings, flash toggle
**B. Scan Window** — full screen with gray overlay
**C. Alignment Guide** — guides camera to the text target; configurable to match the object shape (e.g. short box for single line, larger for full document)
**D. Manual Entry Button** — (multi-field scan only) skips scan and allows manual input

---

## Scan Flow (4 steps)

1. **Launch** — camera icon in a text field (single-field) or add icon (multi-field)
2. **Scan** — modal opens; user aligns object in alignment box
3. **Text Recognized** — live feedback line shows detected text
4. **Confirmation** — scanner auto-dismisses; scanned text populates the form field

---

## Alignment Guide Configuration

The alignment box size is configurable:
- **Single-line scan** → short narrow box for one line of text
- **Full document scan** → larger box covering the document area
- **Object-specific** → shaped to match the form of the scanned object (e.g. business card)

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

@State private var invoiceNumber = ""
@State private var showOCR = false

TextFieldFormView(
    title: { Text("Invoice Number") },
    text: $invoiceNumber,
    placeholder: { Text("Enter or scan") }
) {
    // Camera icon launches OCR scanner
    FioriButton { _ in
        Image(systemName: "camera.viewfinder")
            .accessibilityLabel("Scan text")
    }
    .fioriButtonStyle(FioriTertiaryButtonStyle())
    .onTapGesture { showOCR = true }
}
.fullScreenCover(isPresented: $showOCR) {
    OCRScannerView { recognizedText in
        invoiceNumber = recognizedText  // auto-populates field
        showOCR = false
    } onCancel: {
        showOCR = false
    }
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Show live text recognition feedback as the scanner detects text
- Auto-dismiss and populate the field on confirmation
- Provide a Manual Entry button for multi-field scans
- Configure the alignment box shape to match the scanned object

**Don't:**
- Use OCR as the only way to input text — manual entry must always be available

---

## Related Patterns

- [barcode-scanner.md](barcode-scanner.md)
- [create-and-edit.md](create-and-edit.md)
- [../components/text-inputs.md](../components/text-inputs.md)
