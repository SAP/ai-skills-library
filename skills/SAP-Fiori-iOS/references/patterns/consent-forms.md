# Consent Forms — Pattern Guide

> SAP Fiori for iOS | Patterns / Onboarding
> Development reference: `FUISinglePageUserConsentForm`, `FUIMultiPageUserConsentForm`

## What is it?

The consent form pattern stores a digital record of the user's understanding and permission for terms of service, data privacy, or app-related permissions. Used in onboarding scenarios.

Slides up as a modal from the bottom on launch; slides down on dismissal.

---

## Anatomy

```
A. Navigation Bar: [Cancel] / [Back]   "Privacy Policy"   [Next]

B. Body Title
   "Data Privacy"

C. Body Text
   Explanation of the consent topic and why it matters.

D. Learn More ›  (optional)

E. Toolbar: [Not Now / Deny]   [Allow]   ← appears on last page only
```

**A. Navigation Bar** — "Cancel" (first step), "Back" (subsequent steps), or step count
**B. Body Title** — concise consent topic label
**C. Body Text** — details relevance and importance of the consent
**D. Learn More link** (optional) — additional information
**E. Toolbar** — primary consent actions; visible only on the last page

---

## Scroll Behavior

Nav bar background matches screen background by default. When scrolling is enabled, the nav bar gains a shadow effect on scroll. Applies to all screen sizes.

---

## Alerts

### Cancel Alert
Both optional and mandatory: tapping "Cancel" shows an alert asking if the user wants to quit onboarding.
- "No" → dismisses alert, continues onboarding

### Deny Alert (mandatory only)
Tapping "Deny" on a mandatory consent screen shows an alert requiring consent to continue.
- "Allow" → dismisses modal, proceeds to next step

---

## Form Arrangements

### Single Consent Form
- Each consent form presented as its own **separate modal** (never bundled)
- **No title** on single consent screens
- Multiple single forms → multiple separate modals

### Sequential Consent Form
- Nav bar shows current and total page count (e.g. "1 of 3")
- First step: modal that slides up from bottom + "Cancel" in nav bar
- Subsequent steps: push transition + "< Back to [Screen Title]"
- Toolbar with actions (Not Now/Deny + Allow) appears only on the **last page**

---

## Form Conditions

| Condition | "Not Now" / "Allow" | "Deny" behavior |
|-----------|-------------------|----------------|
| **Optional** | Dismisses form, proceeds to next onboarding step; no alert | N/A |
| **Mandatory** | "Allow" proceeds; "Deny" shows alert requiring consent | Alert blocks until user allows |

---

## Mixed Forms

If an app has both single and sequential consent forms:
- Single forms → separate modals
- Sequential forms → their own separate modal

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

// Single consent form
UserConsentForm(
    userConsentPages: [
        UserConsentPage(
            title: AttributedString("Data Privacy"),
            body: AttributedString("We collect usage data to improve the app. You can opt out at any time in Settings."),
            isRequired: false  // optional
        )
    ],
    action: FioriButton(title: AttributedString("Allow"), action: { _ in acceptConsent() }),
    secondaryAction: FioriButton(title: AttributedString("Not Now"), action: { _ in skipConsent() })
)

// Sequential consent form (multi-page)
UserConsentForm(
    userConsentPages: [
        UserConsentPage(title: AttributedString("Terms of Use"),
                        body: AttributedString(termsText),
                        isRequired: true),
        UserConsentPage(title: AttributedString("Privacy Policy"),
                        body: AttributedString(privacyText),
                        isRequired: true),
        UserConsentPage(title: AttributedString("Analytics"),
                        body: AttributedString(analyticsText),
                        isRequired: false)
    ],
    // Toolbar only shown on last page
    action: FioriButton(title: AttributedString("Allow"), action: { _ in acceptAll() }),
    secondaryAction: FioriButton(title: AttributedString("Deny"), action: { _ in denyConsent() })
)
// Nav bar auto-shows "1 of 3", "2 of 3", etc.
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Present each single consent form as its own separate modal
- Show toolbar actions only on the last page of sequential forms
- Show a deny alert on mandatory forms — "Allow" is the only way forward
- Always provide a Learn More link for complex legal content

**Don't:**
- Bundle multiple single consent forms into one modal
- Show the toolbar before the last sequential page
- Omit titles on single consent screens (they intentionally have none)

---

## Related Patterns

- [single-user-onboarding.md](single-user-onboarding.md)
- [../components/navigation-bar.md](../components/navigation-bar.md)
