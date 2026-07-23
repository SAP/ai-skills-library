# Document Scanner — Pattern Guide

> SAP Fiori for iOS | Patterns / Scanner
> Development reference: SwiftUI `DocumentScannerView` (Apple VisionKit)

## What is it?

The document scanner uses Apple's VisionKit to digitize physical documents with an on-device flow. Supports automatic and manual capture, plus editing (adjust, filter, rotate, retake, delete).

---

## Anatomy

### A. Camera View
- Auto/manual capture toggle (top right: "Manual" button)
- Shutter button for manual capture
- Flash toggle
- Filter selector
- Bottom-left: scan preview thumbnail (entry to gallery/edit)
- Bottom-right: "Save" button with scan count

### B. Gallery/Edit View
Full view of all captured scans in the session. Actions: adjust, filter, rotate, retake, delete. "Done" returns to camera view for final save.

---

## Capture Modes

### Automatic (default)
- Opens in auto mode
- Blue outline appears when document detected
- User holds steady → auto-captures
- Preview shown in bottom-left thumbnail

### Manual
- User taps "Manual" to switch
- Blue outline appears on detected document
- User taps shutter to capture

### Scan Confirmation
After each capture, user can save or retake.

---

## Edit Actions

| Action | Description |
|--------|-------------|
| **Adjust** | Drag corners to crop/realign |
| **Filter** | Color / Grayscale / Black & White / Photo |
| **Rotate** | 90-degree increments |
| **Retake** | Returns to camera view for that scan |
| **Delete** | Removes scan from session |

**Filter guidance:**
- Color → preserves original colors
- Grayscale → cleaner, professional look
- Black & White → sharper text, optimized contrast
- Photo → preserves image detail and colors

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

@State private var showDocScanner = false
@State private var scannedImages: [UIImage] = []

FioriButton { _ in
    Label("Scan Document", systemImage: "doc.viewfinder")
}
.fioriButtonStyle(FioriSecondaryButtonStyle())
.onTapGesture { showDocScanner = true }
.fullScreenCover(isPresented: $showDocScanner) {
    DocumentScannerView { images in
        scannedImages = images
        showDocScanner = false
    } onCancel: {
        showDocScanner = false
    }
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Default to auto-capture mode
- Allow users to preview scans before saving
- Provide all four filter options
- Support retake for individual scans without losing others

**Don't:**
- Skip scan confirmation — users need a chance to retake
