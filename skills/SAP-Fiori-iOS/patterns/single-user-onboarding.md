# Single-User Onboarding — Pattern Guide

> SAP Fiori for iOS | Patterns / Onboarding
> Development reference: `FUIWelcomeScreen`, Onboarding Patterns SDK

## What is it?

The SAP Fiori single-user onboarding pattern provides a consistent, native-first experience for first-time app setup. It is a sequence of configurable flows covering activation, authentication, passcode, permissions, and app launch. Use only when **one user per device**; for shared devices, use [multi-user-onboarding.md](multi-user-onboarding.md).

---

## Do's / Don'ts

**Do:** Use to streamline activation and simplify security.
**Don't:** Use when multiple users share a device.

**Top tips:**
- Send a clear welcome email with visual instructions
- Keep the process as simple as possible
- Don't repeat onboarding after first-time completion
- Don't skip onboarding for first-time logins
- Minimize permission requests during onboarding

---

## First-Time User Flow

```
Installation (email / MDM / pre-install)
    → Launch (splash screen — optional)
    → Welcome Screen
    → Activation
    → Authentication (mandatory)
    → Passcode Creation (optional)
    → Biometric Authentication (optional)
    → Permissions / Consent (optional)
    → Use App
```

### 1. Splash Screen
First branded screen after system launch screen. Minimal — typically just a centered logo. Keep lightweight; avoid unnecessary delays.

### 2. Welcome Screen (`FUIWelcomeScreen`)
Sets the app's tone and presents key actions. Supports:
- Legal terms agreement (checkbox)
- Demo mode
- Continue to setup

**Welcome screen variations** (based on backend setup):
| Type | Behavior |
|------|---------|
| MDM / Hardcoded | Data pushed automatically; user signs in directly |
| Activation Link | User needs link from welcome email |
| Discovery Service | User enters corporate email; service finds backend |
| QR Code Scanner | User scans provided QR code |
| Standard App Store | All onboarding variants supported |

**Configurations:** Top image (logo), bottom image (secondary logo/affiliate), user legal agreements (EULA, terms — must check checkbox to proceed).

### 3. Activation
Identifies company domain, connects app to correct system landscape. Varies by security requirements and device type (corporate MDM devices may skip steps automatically).

### 4. Authentication (mandatory)
The only required step. Handled by the identity provider — may launch within app or external browser.

### 5. Passcode Creation (optional)
If security policy requires an app passcode:
- "Create Passcode" flow — must comply with admin security standards
- "Skip Passcode" variant — available when device/MDM security is sufficient
- App auto-locks after configurable inactivity timeout

### 6. Biometric Authentication (optional)
Face ID / Touch ID based on device capabilities. Native iOS authentication dialog.

### 7. Permissions / Consent (optional)
EULA, data privacy consent, location sharing, voice permissions. Uses the [consent-forms.md](consent-forms.md) pattern.

---

## Returning User Flow

```
App Launch
    → Passcode Entry / Biometric Auth (if configured)
    → Passcode Change (if security policy changed)
    → Use App
```

**Passcode Change** — triggered automatically when security policy changes (passcode complexity, required length, skip-passcode setting). Can also be invoked manually from Settings/Security screen. Provide context explaining why users are asked to update.

---

## Adaptive Design

- Onboarding screens adapt to all iOS device sizes
- Welcome screens: **portrait only** on compact; portrait + landscape on regular

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

// Standard welcome screen
WelcomeScreen(
    title: AttributedString("Welcome"),
    description: AttributedString("Sign in with your SAP credentials to continue."),
    icon: Image("app-logo"),
    action: FioriButton(
        title: AttributedString("Sign In"),
        action: { _ in startSignIn() }
    ),
    secondaryAction: FioriButton(
        title: AttributedString("Try Demo"),
        action: { _ in startDemo() }
    )
)

// Full onboarding state machine
enum OnboardingStep {
    case splash, welcome, activation, auth, passcode, biometric, consent, app
}

@State private var step: OnboardingStep = .splash

switch step {
case .splash:   SplashScreen(onComplete: { step = .welcome })
case .welcome:  WelcomeScreen(..., action: FioriButton { _ in step = .activation })
case .activation: ActivationScreen(..., action: FioriButton { _ in step = .auth })
case .auth:     BasicAuthView(onSuccess: { step = .passcode })
case .passcode: PasscodeCreationView(onComplete: { step = .biometric })
case .biometric: BiometricAuthView(onComplete: { step = .consent })
case .consent:  UserConsentForm(..., action: FioriButton { _ in step = .app })
case .app:      MainAppView()
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Include a blank white transition screen between modular onboarding steps
- Support all welcome screen variations for App Store distribution
- Trigger passcode change automatically when security policy changes
- Make the process modular — each step is independent

**Don't:**
- Repeat onboarding for returning users
- Skip onboarding for first-time logins
- Request multiple system permissions simultaneously unless absolutely required

---

## Related Patterns

- [multi-user-onboarding.md](multi-user-onboarding.md)
- [consent-forms.md](consent-forms.md)
- [biometric-authentication.md](biometric-authentication.md)
- [basic-authentication.md](basic-authentication.md)
