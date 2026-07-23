# Biometric Authentication — Pattern Guide

> SAP Fiori for iOS | Patterns / Authentication

## What is it?

Biometric authentication uses Face ID or Touch ID to verify user identity securely and conveniently. SAP Fiori iOS supports both Apple biometric methods.

---

## Anatomy

```
A. Navigation Bar: Title  [Cancel]  (optional)

        B. [Face ID / Touch ID icon]

C. Description
   "Use Face ID to sign in quickly and securely."

D. Sub Description
   "You can change this later in Settings."

E. [Enable Face ID]    ← emphasized primary button
   [Not Now]           ← secondary button (optional)

F. Learn More ›
```

**A. Navigation Bar** — title and optional Cancel action.
**B. ID Icon** — must match the device's biometric type (Face ID or Touch ID).
**C. Description** — concisely explains the function and benefit.
**D. Sub Description** — explains how to change the setting later.
**E. Button(s)** — emphasized button enables biometrics; optional secondary to decline.
**F. Learn More link** — additional information about the biometric type.

---

## Variations

### By Biometric Type

| Type | Behavior on decline |
|------|-------------------|
| **Touch ID** | Tapping "Not Now" or "Allow" simply dismisses the form; no alert shown |
| **Face ID** | Tapping "Deny" shows an alert: user must give consent to continue; tapping "Allow" dismisses and proceeds |

```swift
import LocalAuthentication

let context = LAContext()
var error: NSError?

if context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &error) {
    let biometricType = context.biometryType
    // .faceID → show Face ID icon and copy
    // .touchID → show Touch ID icon and copy
    // .opticID → show Optic ID icon (visionOS)
}
```

### By Button Count

**One button (single consent form):**
- Multiple single consent forms → each presented as a **separate modal**
- No title on single consent screens
- No bundling multiple single forms into one modal

**Two buttons (sequential consent forms):**
- Navigation bar shows current and total page count (e.g. "1 of 3")
- Action bar (with final confirmation) appears only on the **last page**

---

## SwiftUI Code Example

```swift
import LocalAuthentication
import FioriSwiftUICore

struct BiometricAuthView: View {
    @Environment(\.dismiss) private var dismiss
    @State private var showDenyAlert = false

    var biometricType: LABiometryType {
        let context = LAContext()
        _ = context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: nil)
        return context.biometryType
    }

    var iconName: String {
        switch biometricType {
        case .faceID: return "faceid"
        case .touchID: return "touchid"
        default: return "lock.shield"
        }
    }

    var biometricName: String {
        biometricType == .faceID ? "Face ID" : "Touch ID"
    }

    var body: some View {
        NavigationStack {
            VStack(spacing: 32) {
                Spacer()

                // B. ID Icon
                Image(systemName: iconName)
                    .font(.system(size: 64))
                    .foregroundStyle(Color.preferredColor(.tintColor))

                VStack(spacing: 12) {
                    // C. Description
                    Text("Use \(biometricName) to sign in quickly and securely.")
                        .font(.fiori(forTextStyle: .body))
                        .multilineTextAlignment(.center)

                    // D. Sub Description
                    Text("You can change this later in Settings → \(biometricName).")
                        .font(.fiori(forTextStyle: .footnote))
                        .foregroundStyle(Color.preferredColor(.secondaryLabel))
                        .multilineTextAlignment(.center)
                }
                .padding(.horizontal, 32)

                Spacer()

                VStack(spacing: 12) {
                    // E. Enable button
                    FioriButton { _ in Text("Enable \(biometricName)") }
                        .fioriButtonStyle(FioriPrimaryButtonStyle())
                        .frame(maxWidth: .infinity)
                        .onTapGesture { enableBiometrics() }

                    // E. Decline (optional)
                    FioriButton { _ in Text("Not Now") }
                        .fioriButtonStyle(FioriSecondaryButtonStyle())
                        .frame(maxWidth: .infinity)
                        .onTapGesture {
                            if biometricType == .faceID {
                                showDenyAlert = true  // Face ID requires consent alert
                            } else {
                                dismiss()  // Touch ID: just dismiss
                            }
                        }

                    // F. Learn More
                    Button("Learn More") { openLearnMore() }
                        .font(.fiori(forTextStyle: .footnote))
                        .foregroundStyle(Color.preferredColor(.tintColor))
                }
                .padding(.horizontal, 32)
                .padding(.bottom, 40)
            }
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    FioriButton { _ in Text("Cancel") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { dismiss() }
                }
            }
            .alert("Face ID Required", isPresented: $showDenyAlert) {
                Button("Allow") { dismiss() }
                Button("Cancel", role: .cancel) {}
            } message: {
                Text("You must allow Face ID to continue.")
            }
        }
    }

    func enableBiometrics() {
        let context = LAContext()
        context.evaluatePolicy(
            .deviceOwnerAuthenticationWithBiometrics,
            localizedReason: "Authenticate to enable \(biometricName)"
        ) { success, error in
            DispatchQueue.main.async {
                if success { dismiss() }
            }
        }
    }
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Match the icon to the device's actual biometric type (Face ID or Touch ID)
- Show a consent alert when the user denies Face ID — it is required
- Present multiple single consent forms as separate modals, not bundled
- Show the current/total page count in the nav bar for sequential forms
- Always provide a fallback to passcode/basic auth

**Don't:**
- Bundle multiple single consent forms into one modal
- Show the action bar before the last page of a sequential form
- Show a denial alert for Touch ID — just dismiss

---

## Related Patterns

- [authentication-overview.md](authentication-overview.md)
- [basic-authentication.md](basic-authentication.md)
