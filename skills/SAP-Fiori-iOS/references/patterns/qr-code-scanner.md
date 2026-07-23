# QR Code Scanner — Pattern Guide

> SAP Fiori for iOS | Patterns / Scanner
> Development reference: UIKit `FUIOnboardingScanViewController`

## What is it?

The QR code scanner is used during onboarding as an activation method. Users scan a provided QR code using the camera or from their camera roll. Used on the Welcome Screen when QR code activation is required.

---

## Anatomy

**A. Navigation Bar (stacked modal)** — "Cancel", "Scan" title, flash toggle
**B. Alignment Guide** — guides camera to QR code
**C. Chevron** — toggles camera roll visibility (revealed/hidden)
**D. Scrolling Camera Roll** — horizontal scroll through camera roll images
**E. Camera Gallery Icon** — opens full photos/albums gallery
**F. Successful Scan Content** — feedback confirming successful scan
**G. Call-To-Action Button** — continues onboarding

---

## Behavior

### Camera Scan
User aligns QR code in the guide → system recognizes → displays feedback.

### Camera Roll Access
- User must grant photo access in Settings first
- Camera roll revealed after permission granted
- Scroll horizontally through images
- Chevron collapses/expands the camera roll (snaps on toggle)
- Down chevron = expanded; Up chevron = collapsed

### Camera Gallery
Alternative to scrolling camera roll — tap image icon to open full gallery.

### Scan Feedback

| Result | Feedback |
|--------|---------|
| Unsuccessful | "Non-QR code image" message |
| Invalid QR code | "Invalid QR code" message |
| Successful | Success content + CTA button to continue |

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

@State private var showQRScanner = false

// Welcome screen → QR code activation button
FioriButton { _ in Text("Scan QR Code") }
    .fioriButtonStyle(FioriPrimaryButtonStyle())
    .onTapGesture { showQRScanner = true }
    .sheet(isPresented: $showQRScanner) {
        QRCodeScannerView { result in
            switch result {
            case .success(let code):
                activateWithCode(code)
                showQRScanner = false
            case .invalid:
                showInvalidAlert = true
            case .notQRCode:
                showNotQRAlert = true
            }
        } onCancel: {
            showQRScanner = false
        }
        // Includes camera roll and gallery access
    }
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Show all three feedback states (unsuccessful, invalid, successful)
- Allow both camera and camera roll/gallery as scan sources
- Request photo permission before revealing camera roll controls
- Provide a CTA button on successful scan to continue onboarding

**Don't:**
- Skip the invalid QR code feedback — users need to know the code doesn't work

---

## Related Patterns

- [single-user-onboarding.md](single-user-onboarding.md)
- [barcode-scanner.md](barcode-scanner.md)
