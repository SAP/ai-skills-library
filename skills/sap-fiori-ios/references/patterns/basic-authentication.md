# Basic Authentication — Pattern Guide

> SAP Fiori for iOS | Patterns / Authentication
> Development reference: `FUIBasicAuthenticationScreen`

## What is it?

The basic authentication pattern provides general-purpose credential-based authentication (passcode, username/password, or custom fields). Text input fields are configurable by admins and developers.

---

## Anatomy

```
A. Navigation Bar: [Cancel]

B. Body Title
   "Sign In"

C. Body Text
   "Enter your credentials to continue."

D. [Text Input Fields] (1 or more, set by admin/developer)
   Username
   Password

E. [Sign In]   ← disabled until all fields are filled
```

**A. Navigation Bar** — includes "Cancel" to exit authentication.
**B. Body Title** — concise label describing the authentication step.
**C. Body Text** — details how to complete the step.
**D. Text Input Fields** — can be more than two; configured by admins/developers.
**E. Sign In Button** — disabled until all fields are filled; tap starts verification.

---

## Behavior

### Sign In Flow
1. All text fields empty → Sign In button **disabled**
2. All text fields filled → Sign In button **enabled**
3. Tap Sign In → verification begins

### Information Verification
While verifying: `BannerMessage` with label **"Verifying Information…"**

### Failed Sign In
On failure: `BannerMessage` with label **"Sign In Failed"**

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct BasicAuthView: View {
    @State private var username = ""
    @State private var password = ""
    @State private var isVerifying = false
    @State private var showError = false
    @Environment(\.dismiss) private var dismiss

    var canSignIn: Bool { !username.isEmpty && !password.isEmpty }

    var body: some View {
        NavigationStack {
            VStack(spacing: 24) {
                // Verification / error banner
                if isVerifying {
                    BannerMessage { Text("Verifying Information…") }
                } else if showError {
                    BannerMessage { Text("Sign In Failed") } icon: {
                        Image(systemName: "exclamationmark.triangle.fill")
                            .foregroundStyle(Color.preferredColor(.negativeLabel))
                    } closeAction: { showError = false }
                }

                VStack(alignment: .leading, spacing: 8) {
                    Text("Sign In")
                        .font(.fiori(forTextStyle: .title1))
                    Text("Enter your credentials to continue.")
                        .font(.fiori(forTextStyle: .body))
                        .foregroundStyle(Color.preferredColor(.secondaryLabel))
                }

                VStack(spacing: 0) {
                    TextFieldFormView(
                        title: { Text("Username") },
                        text: $username,
                        placeholder: { Text("Enter username") }
                    )
                    TextFieldFormView(
                        title: { Text("Password") },
                        text: $password,
                        placeholder: { Text("Enter password") }
                    )
                }

                FioriButton { _ in Text("Sign In") }
                    .fioriButtonStyle(FioriPrimaryButtonStyle())
                    .frame(maxWidth: .infinity)
                    .disabled(!canSignIn)
                    .onTapGesture { signIn() }

                Spacer()
            }
            .padding(24)
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    FioriButton { _ in Text("Cancel") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { dismiss() }
                }
            }
        }
    }

    func signIn() {
        isVerifying = true
        Task {
            do {
                try await authenticate(username: username, password: password)
                isVerifying = false
                // proceed to app
            } catch {
                isVerifying = false
                showError = true
            }
        }
    }
}
```

---

## Adaptive Design

Supported in both compact (iPhone) and regular (iPad) width. Layout adjusts automatically.

---

## Do's ✓ / Don'ts ✗

**Do:**
- Disable the Sign In button until all required fields are filled
- Show "Verifying Information…" banner during the verification process
- Show "Sign In Failed" banner on failure with a close option
- Use "Cancel" in the navigation bar to allow exiting

**Don't:**
- Enable the Sign In button while fields are empty
- Leave the user without feedback during verification

---

## Related Patterns

- [authentication-overview.md](authentication-overview.md)
- [biometric-authentication.md](biometric-authentication.md)
