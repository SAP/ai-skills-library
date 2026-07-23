# AI Acknowledgement — In-App AI Design

> SAP Fiori for iOS | In-App AI Design / Patterns
> Development reference: `IllustratedMessage`

## What is it?

AI acknowledgement brings essential information about an AI service to users' attention in a standardized way. It educates users about AI capabilities, data collection, privacy practices, and risks — establishing trust and baseline expectations.

---

## When to Use

### High-Risk (recommended)
- Privacy / data collection
- Legal or financial advice
- Educational content
- News and fact-checking

### Low-Risk (optional — AI Notice may suffice)
- Entertainment
- Recipe / lifestyle suggestions
- Generic communication responses

---

## Do's / Don'ts

**Do:**
- Inform users about present AI services
- Educate on important AI system properties
- Notify users about AI service changes
- Provide easy re-access to acknowledgement details
- Enable opt-in / opt-out of AI features

**Don't:**
- Use for failed/successful AI process notifications
- Send marketing about the AI service
- Use for non-AI information
- Make acknowledgement details hard to access
- Limit users' ability to manage AI preferences

---

## Three Surfaces

### 1. Onboarding (replaces consent form)
Agreement screen in the onboarding flow explaining AI terms, functionality, and data usage. User consents or declines. A "Learn more" hyperlink opens a bottom sheet with additional details.

```swift
// Onboarding AI acknowledgement — part of consent flow
UserConsentForm(
    userConsentPages: [
        UserConsentPage(
            title: AttributedString("AI Data Services"),
            body: AttributedString(aiAcknowledgementText),
            isRequired: false
        )
    ],
    action: FioriButton(title: AttributedString("Allow"), action: { _ in accept() }),
    secondaryAction: FioriButton(title: AttributedString("Not Now"), action: { _ in decline() })
)
// "Learn more" → bottom sheet with detailed AI privacy info
```

### 2. In-App Service Update Dialog
Shown when the AI service agreement is updated. User taps "Done" to dismiss or "Learn more" to see full details (full-screen dialog). "Back" returns to the app.

```swift
// AI service update — shown on app entry after update
.sheet(isPresented: $showAIUpdate) {
    NavigationStack {
        IllustratedMessage {
            Image(systemName: "sparkles.rectangle.stack")
                .font(.system(size: 48))
                .foregroundStyle(Color.preferredColor(.tintColor))
        } title: {
            Text("AI Service Update")
        } description: {
            Text(aiUpdateSummaryText)
                .multilineTextAlignment(.center)
        } action: {
            HStack {
                FioriButton { _ in Text("Learn More") }
                    .fioriButtonStyle(FioriSecondaryButtonStyle())
                    .onTapGesture { showDetails = true }
                FioriButton { _ in Text("Done") }
                    .fioriButtonStyle(FioriPrimaryButtonStyle())
                    .onTapGesture { showAIUpdate = false }
            }
        }
        .navigationDestination(isPresented: $showDetails) {
            AIServiceUpdateDetailView()
        }
    }
    .presentationDetents([.medium, .large])
}
```

### 3. Re-Accessing from Settings
"AI Acknowledgement" section in the Settings page. Shows contextual hint badge when there's an unreviewed update. Reverts to default styling after review. User can opt in/out here.

```swift
// In profile & settings
Section("AI") {
    NavigationLink {
        AIAcknowledgementDetailView()
    } label: {
        HStack {
            Text("AI Acknowledgement")
            Spacer()
            if hasUnreviewedUpdate {
                Circle()
                    .fill(Color.preferredColor(.tintColor))
                    .frame(width: 8, height: 8)  // contextual hint dot
            }
        }
    }
}

// Detail view — opt out
FioriButton { _ in Text("Opt Out") }
    .fioriButtonStyle(FioriSecondaryButtonStyle())
    .tint(Color.preferredColor(.negativeLabel))
    .onTapGesture { showOptOutConfirmation = true }
```

---

## Bottom Sheet for AI Privacy Details

```swift
.sheet(isPresented: $showPrivacyDetails) {
    ScrollView {
        VStack(alignment: .leading, spacing: 16) {
            Text("AI Data Privacy Details")
                .font(.fiori(forTextStyle: .title2))
            Text(aiPrivacyDetailsText)
                .font(.fiori(forTextStyle: .body))
        }
        .padding(24)
    }
    .presentationDetents([.medium, .large])
    .presentationDragIndicator(.visible)
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Show a contextual hint in settings when the acknowledgement has an unreviewed update
- Allow users to opt back in after opting out
- Be transparent about what opting out means for the user's experience
- Use clear, straightforward language

**Don't:**
- Use this pattern for AI processing success/failure notifications (use progress indicators instead)
- Market premium AI features through this pattern

---

## Related

- [ai-notice.md](ai-notice.md)
- [../components/illustrated-message.md](../components/illustrated-message.md)
- [../patterns/consent-forms.md](../patterns/consent-forms.md)
