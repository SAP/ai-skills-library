# Info View — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Onboarding
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIInfoViewController`

## What is it?

The info view is used in onboarding scenarios to display customizable information in a transitionary screen state that **locks regular navigation**. It is closely related to the What's New component and feedback screens used in multi-user onboarding.

---

## When to Use

**Do:**
- Use when the user must perform an action or remain in a transitionary state before continuing
- Alter button styling when prioritization or hierarchy is required — the default link/ghost style is not mandatory

**Don't:**
- Use interchangeably with the What's New component — if the user still needs to be able to navigate away or go back, use What's New instead

**The key distinction:** Info View **locks navigation**. What's New does not.

---

## Anatomy

```
A. Navigation Bar (contrast — no actions)
──────────────────────────────────────────
         B. Title

         C. Description

         D. Progress Indicator (optional)
            [  spinner  ]
            Optional label (max 3 words)

         E. Button Stack
         ┌──────────────────┐
         │  Primary Button  │
         └──────────────────┘
         ┌──────────────────┐
         │ Secondary Button │
         └──────────────────┘
```

### A. Navigation Bar
Default contrast navigation bar with **no actions** — no back button, no close. This distinguishes the info view from a stacked modal and prevents the user from navigating away.

### B. Title
Clear and concise. Communicates what the user needs to know.

### C. Description
Summarized explanation of the current state or required action.

### D. Progress Indicator (optional)
- **Spinner** — indicates the screen state is in progress; rotates until the system is ready to transition
- **Label** — optional text below the spinner; maximum **3 words**

### E. Button Stack
Two button form cells stacked vertically:
- **Top button** = Primary action
- **Bottom button** = Secondary action

---

## Behavior

### Progress Spinner
The spinner continues to rotate until the system or app is ready to transition. It indicates the screen state is actively in progress — not just a loading delay.

### Action Buttons
Emphasized actions that allow the user to navigate away from or alter the application state. The button stack is the only navigation available while the info view is active.

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct AppActivationInfoView: View {
    @State private var isActivating = true

    var body: some View {
        NavigationStack {
            VStack(spacing: 32) {
                Spacer()

                // Title
                Text("Activating Your Account")
                    .font(.fiori(forTextStyle: .largeTitle))
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 32)

                // Description
                Text("Please wait while we set up your workspace. This may take a moment.")
                    .font(.fiori(forTextStyle: .body))
                    .foregroundStyle(Color.preferredColor(.secondaryLabel))
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 32)

                // Progress indicator
                if isActivating {
                    VStack(spacing: 12) {
                        ProgressView()
                            .scaleEffect(1.5)
                            .tint(Color.preferredColor(.tintColor))
                        Text("Setting up…")  // max 3 words
                            .font(.fiori(forTextStyle: .footnote))
                            .foregroundStyle(Color.preferredColor(.secondaryLabel))
                    }
                }

                Spacer()

                // Button stack
                VStack(spacing: 12) {
                    // Primary (top)
                    FioriButton { _ in Text("Continue") }
                        .fioriButtonStyle(FioriPrimaryButtonStyle())
                        .frame(maxWidth: .infinity)
                        .disabled(isActivating)

                    // Secondary (bottom)
                    FioriButton { _ in Text("Cancel") }
                        .fioriButtonStyle(FioriSecondaryButtonStyle())
                        .frame(maxWidth: .infinity)
                }
                .padding(.horizontal, 32)
                .padding(.bottom, 40)
            }
            .navigationBarBackButtonHidden(true)  // no back navigation
            .toolbar(.hidden, for: .navigationBar)  // no nav bar actions
        }
    }
}
```

### Multi-user onboarding transition screen
```swift
struct UserSwitchInfoView: View {
    var body: some View {
        VStack(spacing: 24) {
            Spacer()

            Text("Switching User")
                .font(.fiori(forTextStyle: .title1))

            Text("Your session is being prepared. All unsaved changes have been saved.")
                .font(.fiori(forTextStyle: .body))
                .foregroundStyle(Color.preferredColor(.secondaryLabel))
                .multilineTextAlignment(.center)
                .padding(.horizontal, 32)

            VStack(spacing: 8) {
                ProgressView()
                    .tint(Color.preferredColor(.tintColor))
                Text("Preparing…")  // 3 words max
                    .font(.fiori(forTextStyle: .footnote))
                    .foregroundStyle(Color.preferredColor(.tertiaryLabel))
            }

            Spacer()

            VStack(spacing: 12) {
                FioriButton { _ in Text("Sign In as New User") }
                    .fioriButtonStyle(FioriPrimaryButtonStyle())
                    .frame(maxWidth: .infinity)

                FioriButton { _ in Text("Stay Signed In") }
                    .fioriButtonStyle(FioriSecondaryButtonStyle())
                    .frame(maxWidth: .infinity)
            }
            .padding(.horizontal, 32)
            .padding(.bottom, 40)
        }
        .navigationBarBackButtonHidden(true)
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Navigation bar | Contrast, no actions | `.navigationBarBackButtonHidden(true)` + `.toolbar(.hidden)` |
| Spinner | Visible | `ProgressView()` |
| Spinner label | Yes (max 3 words) | `Text(...)` below `ProgressView` |
| Spinner label | None | Omit label |
| Primary button | Top of stack | `FioriPrimaryButtonStyle()` |
| Secondary button | Bottom of stack | `FioriSecondaryButtonStyle()` |
| Button style | Custom priority | Override style as needed |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Hide all back/navigation actions — the info view locks navigation by design
- Keep the spinner label to **3 words maximum**
- Place the primary action as the **top** button, secondary as the **bottom**
- Customize button styles when action priority/hierarchy requires it

**Don't:**
- Use when the user should still be able to navigate away — use What's New instead
- Show more than two buttons in the stack
- Write a spinner label longer than 3 words

---

## Related Components

- [onboarding.md](onboarding.md) — WelcomeScreen, ActivationScreen, EULA, Consent
- [loading-indicator.md](loading-indicator.md) — loading patterns outside onboarding
