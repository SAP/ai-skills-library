# Multi-User Onboarding — Pattern Guide

> SAP Fiori for iOS | Patterns / Onboarding
> Development reference: `FUIMultiUserPasscodeController`, Onboarding Patterns SDK

## What is it?

The multi-user onboarding pattern handles scenarios where more than one user shares a single device. Users can select from existing accounts or add a new account. It extends the single-user onboarding pattern as an additional module.

---

## When to Use

**Do:** Use when multiple users share one device.
**Don't:** Use when only one user activates their account — use [single-user-onboarding.md](single-user-onboarding.md) instead.

---

## Anatomy

### Sign In Screen
```
A. App Logo (optional) + App Title (max 2 lines compact / 1 line regular)

B. User Profile
   [ User photo / initials ]
   User Title (primary ID: name)
   User Subtitle (secondary ID: job title)

C. Sign In Form
   [ Passcode field ]  ← numeric or alphanumeric
   [ Sign In ]  ← disabled until passcode entered
   Forgot Passcode?

D. [ Switch or Add User ]
```

### Switch or Add User Screen
```
E. Navigation Bar: [Back]  "Switch or Add User"  [Add User +]
F. [ Search field ]
G. Selected user section
H. User list (sorted earliest → most recently onboarded)
```

---

## Behavior

### Sign In
- Default loaded profile = current/previous user
- Tap passcode field → keyboard appears, placeholder "Passcode" replaced with obfuscated entry
- Sign In enabled only after passcode entry
- Tap "Forgot Passcode?" → push to passcode recovery screen
- Tap "Switch or Add User" → push to switch screen

### Switch or Add User
- **Back button** — saves current selection, returns to Sign In with updated profile
- **Add User button** — opens the single-user onboarding flow for a new user
- **Search** — local search filters onboarded user profiles
- **User list** — works like a list picker; tap to select/deselect; checkmark indicates selection
- Section headers ("Selected", "All") appear based on list size

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct MultiUserSignInView: View {
    @State private var passcode = ""
    @State private var showSwitchUser = false
    let currentUser: UserProfile

    var canSignIn: Bool { !passcode.isEmpty }

    var body: some View {
        VStack(spacing: 24) {
            // A. App details
            VStack(spacing: 4) {
                Image("app-logo")
                    .resizable().scaledToFit().frame(height: 60)
                Text("My SAP App")
                    .font(.fiori(forTextStyle: .title2))
                    .lineLimit(2)  // compact: max 2 lines
            }

            // B. User profile
            VStack(spacing: 8) {
                AsyncImage(url: currentUser.avatarURL) { img in
                    img.resizable().clipShape(Circle())
                } placeholder: {
                    Circle().fill(Color.preferredColor(.accentBackground3))
                        .overlay(Text(currentUser.initials)
                            .font(.fiori(forTextStyle: .title3))
                            .foregroundStyle(Color.preferredColor(.accentLabel3)))
                }
                .frame(width: 80, height: 80)

                Text(currentUser.name)
                    .font(.fiori(forTextStyle: .title3))
                Text(currentUser.jobTitle)
                    .font(.fiori(forTextStyle: .subheadline))
                    .foregroundStyle(Color.preferredColor(.secondaryLabel))
            }

            // C. Sign in form
            VStack(spacing: 12) {
                SecureField("Passcode", text: $passcode)
                    .textFieldStyle(.roundedBorder)
                    .keyboardType(.numberPad)

                FioriButton { _ in Text("Sign In") }
                    .fioriButtonStyle(FioriPrimaryButtonStyle())
                    .frame(maxWidth: .infinity)
                    .disabled(!canSignIn)
                    .onTapGesture { signIn() }

                Button("Forgot Passcode?") { showForgotPasscode() }
                    .font(.fiori(forTextStyle: .footnote))
                    .foregroundStyle(Color.preferredColor(.tintColor))
            }

            // D. Switch or add user
            FioriButton { _ in Text("Switch or Add User") }
                .fioriButtonStyle(FioriSecondaryButtonStyle())
                .frame(maxWidth: .infinity)
                .onTapGesture { showSwitchUser = true }
        }
        .padding(32)
        .navigationDestination(isPresented: $showSwitchUser) {
            SwitchOrAddUserView()
        }
    }
}

struct SwitchOrAddUserView: View {
    @State private var searchQuery = ""
    @State private var selectedUser: UserProfile?
    let onboardedUsers: [UserProfile]

    var filteredUsers: [UserProfile] {
        searchQuery.isEmpty ? onboardedUsers
            : onboardedUsers.filter { $0.name.localizedCaseInsensitiveContains(searchQuery) }
    }

    var body: some View {
        List(filteredUsers, selection: $selectedUser) { user in
            HStack {
                Text(user.name)
                Spacer()
                if selectedUser?.id == user.id {
                    Image(systemName: "checkmark")
                        .foregroundStyle(Color.preferredColor(.tintColor))
                }
            }
        }
        .searchable(text: $searchQuery, placement: .navigationBarDrawer(displayMode: .always))
        .navigationTitle("Switch or Add User")
        .navigationBarTitleDisplayMode(.inline)
        .toolbar {
            ToolbarItem(placement: .primaryAction) {
                FioriButton { _ in Image(systemName: "person.badge.plus").accessibilityLabel("Add User") }
                    .fioriButtonStyle(FioriTertiaryButtonStyle())
                    .onTapGesture { startNewUserOnboarding() }
            }
        }
    }
}
```

---

## Adaptive Design

Supported in compact and regular width. Sign In screen adapts app title to 2 lines (compact) or 1 line (regular).

---

## Do's ✓ / Don'ts ✗

**Do:**
- Default to the current/previous user profile on the Sign In screen
- Sort the user list earliest → most recently onboarded
- Keep the Sign In button disabled until a passcode is entered
- Include a blank transition screen between onboarding steps

**Don't:**
- Use for single-user devices — use single-user onboarding instead
- Show the Add User flow without first capturing the passcode of the current user

---

## Related Patterns

- [single-user-onboarding.md](single-user-onboarding.md)
- [../components/search-bar.md](../components/search-bar.md)
- [../components/list-picker-form-cell.md](../components/list-picker-form-cell.md)
