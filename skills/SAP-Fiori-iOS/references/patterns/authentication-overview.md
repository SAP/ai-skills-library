# Authentication Overview — Pattern Guide

> SAP Fiori for iOS | Patterns / Authentication
> Related components: [signature-capture.md](../components/signature-capture.md)

## What is it?

Authentication verifies the identity of a user before allowing them to run or complete an action. It protects user information and data, especially on shared devices.

---

## Authentication Types

### Basic Authentication
Passcode/login-based authentication. Highly customizable to match enterprise security requirements.

Use cases:
- Initial app login
- Re-authentication after session timeout
- Passcode entry on return from background
- Multi-user passcode switching

→ See [basic-authentication.md](basic-authentication.md)

### Biometric Authentication
Uses Apple's Face ID and Touch ID for secure, convenient identity verification. SAP Fiori iOS fully supports both methods.

Use cases:
- Quick re-authentication without entering a passcode
- Fallback to passcode when biometrics are unavailable

→ See [biometric-authentication.md](biometric-authentication.md)

### Signature Capture
Users input their handwritten signature as a form of identity verification and consent. Captured as a bitmap or SVG with an optional watermark, saved to the backend.

Use cases:
- Approving workflows
- Signing documents or forms
- Confirming delivery or task completion

→ See [signature-capture.md](../components/signature-capture.md)

---

## Choosing the Right Method

| Scenario | Recommended method |
|----------|-------------------|
| First-time login / session start | Basic authentication (passcode / credentials) |
| Quick re-authentication | Biometric (Face ID / Touch ID) with passcode fallback |
| Legal consent or document signing | Signature capture |
| Shared device, multi-user | Basic authentication with user switching |
| High-security action confirmation | Biometric or passcode re-authentication |
