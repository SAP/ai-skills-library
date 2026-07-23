# Barcode Scanner — Pattern Guide

> SAP Fiori for iOS | Patterns / Scanner
> Development reference: UIKit `FUIBarcodeScanViewController`

## What is it?

The barcode scanner allows users to quickly locate objects by scanning a barcode via the device's built-in camera. Part of the search workflow — launched from the barcode icon in the search bar.

---

## Anatomy

Full-screen modal with three elements:

**A. Navigation Bar** — "Cancel" button, title, flash icon toggle
**B. Scan Window** — full screen with gray overlay
**C. Alignment Guide** — guides the camera position to the barcode

---

## Workflow

1. User sees search bar with barcode icon → taps icon
2. Scanner opens as full-screen modal
3. User aligns barcode in the alignment guide
4. Scan recognized → scanner slides down
5. List filtered by scan result
6. Tap object cell → navigate to object details

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

@State private var showScanner = false
@State private var scannedCode: String? = nil

// Search bar with barcode icon
HStack {
    TextField("Search or scan", text: $searchQuery)
    FioriButton { _ in
        Image(systemName: "barcode.viewfinder")
            .accessibilityLabel("Scan barcode")
    }
    .fioriButtonStyle(FioriTertiaryButtonStyle())
    .onTapGesture { showScanner = true }
}
.fullScreenCover(isPresented: $showScanner) {
    BarcodeScannerView { code in
        scannedCode = code
        searchQuery = code   // filter list by result
        showScanner = false
    } onCancel: {
        showScanner = false
    }
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Launch from the search bar barcode icon
- Filter the list immediately after a successful scan
- Provide flash toggle for low-light environments

**Don't:**
- Use as the only input method — search bar typing must also be available

---

## Related Patterns

- [search.md](search.md)
- [ocr-scanner.md](ocr-scanner.md)
- [qr-code-scanner.md](qr-code-scanner.md)
