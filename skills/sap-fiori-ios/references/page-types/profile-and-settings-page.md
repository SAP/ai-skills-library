# Profile and Settings Page — Page Type Guide

> SAP Fiori for iOS | Page Types
> Development reference: `sap.f.SemanticPage`

## What is it?

The profile and settings page is a modal view holding user-specific and app-specific settings. It lets users customize their app experience.

**Entry point:** Right side of the navigation bar on the home screen only.

**Presentation:**
- Compact (iPhone): full-screen modal
- Regular (iPad): form sheet modal (centered)

---

## Anatomy

```
A. Profile Header (optional)
   [ Avatar / initials ]
   User Name
   Job Title
   [ Action: Change Photo / Start Shift ]

B. Settings
   Personal information
   App preferences (units, language)
   Notification preferences
   Permissions

C. App Information
   About (version number)
   Legal
   Feedback / Support

D. Sign Out & Sync
   [ Sign Out ]      ← semantic negative (or "Exit Demo" in demo mode)
   [ Manual Sync ]   ← optional
```

**Version number only:** If "About" contains only a version number, place it at the bottom of the main profile screen (not in a sub-section).

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct ProfileAndSettingsView: View {
    @Environment(\.dismiss) private var dismiss
    @Environment(\.horizontalSizeClass) var hSizeClass

    var body: some View {
        NavigationStack {
            List {
                // A. Profile header
                Section {
                    ProfileHeader {
                        Text(currentUser.name)
                    } subtitle: {
                        Text(currentUser.jobTitle)
                            .foregroundStyle(Color.preferredColor(.secondaryLabel))
                    } detailImage: {
                        AsyncImage(url: currentUser.avatarURL) { img in
                            img.resizable().clipShape(Circle())
                        } placeholder: {
                            Circle().fill(Color.preferredColor(.accentBackground3))
                                .overlay(Text(currentUser.initials)
                                    .foregroundStyle(Color.preferredColor(.accentLabel3)))
                        }
                        .frame(width: 80, height: 80)
                    }
                }
                .listRowBackground(Color.clear)

                // B. Settings
                Section("Preferences") {
                    NavigationLink("Units of Measure") { UnitsSettingsView() }
                    NavigationLink("Notifications") { NotificationSettingsView() }
                    NavigationLink("Language & Region") { LanguageSettingsView() }
                }

                Section("Privacy") {
                    NavigationLink("Permissions") { PermissionsView() }
                    Toggle("Analytics", isOn: $analyticsEnabled)
                }

                // C. App information
                Section("Support") {
                    NavigationLink("Help & Documentation") { HelpView() }
                    NavigationLink("Send Feedback") { FeedbackView() }
                    NavigationLink("Legal") { LegalView() }
                }

                // D. Sign out & sync
                Section {
                    FioriButton { _ in Text("Manual Sync") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .frame(maxWidth: .infinity, alignment: .leading)

                    FioriButton { _ in Text("Sign Out") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .tint(Color.preferredColor(.negativeLabel))
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .onTapGesture { signOut() }
                }

                // Version at bottom if About contains only version number
                Section {
                    Text("Version 24.4.0")
                        .font(.fiori(forTextStyle: .footnote))
                        .foregroundStyle(Color.preferredColor(.tertiaryLabel))
                        .frame(maxWidth: .infinity, alignment: .center)
                }
                .listRowBackground(Color.clear)
            }
            .navigationTitle("Profile")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    FioriButton { _ in Text("Done") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { dismiss() }
                }
            }
        }
    }
}

// Entry point in nav bar (home screen only)
.toolbar {
    ToolbarItem(placement: .navigationBarTrailing) {
        FioriButton { _ in
            Image(systemName: "person.circle")
                .accessibilityLabel("Profile and Settings")
        }
        .fioriButtonStyle(FioriTertiaryButtonStyle())
        .onTapGesture { showProfile = true }
    }
}
// Compact: full-screen; Regular: form sheet
.fullScreenCover(isPresented: $showProfile.projectedValue,
                 isPresented: hSizeClass == .compact) {
    ProfileAndSettingsView()
}
.sheet(isPresented: $showProfile.projectedValue,
       isPresented: hSizeClass != .compact) {
    ProfileAndSettingsView()
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Place the profile entry point on the right side of the nav bar, home screen only
- Use full-screen modal on compact, form sheet on regular
- Put Sign Out in its own section, clearly separated from settings
- Place version-only About info at the bottom of the main screen

**Don't:**
- Place the profile entry point on every screen — home screen only
- Put Sign Out inline with other settings rows without visual separation

---

## Related Components / Patterns

- [../components/profile-header.md](../components/profile-header.md)
- [../patterns/navigation.md](../patterns/navigation.md)
- [object-details-page.md](object-details-page.md)
