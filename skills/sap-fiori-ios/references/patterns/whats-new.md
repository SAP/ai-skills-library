# What's New — Pattern Guide

> SAP Fiori for iOS | Patterns / Onboarding
> Development reference: `FUIWhatsNewController`, `FUIWhatsNewViewController`

## What is it?

The What's New component shows users updates, new features, bug fixes, and news for an application. Accessible two ways: as a pop-up modal after login, or from the user's profile page.

---

## Entry Points

### Pop-Up Modal
Shown automatically after login when there are updates to communicate.

### From Profile
Linked in the profile page menu list. Users can access it on-demand.

> **Do not** show a call-to-action button when users open What's New from the profile page.

---

## Anatomy

```
A. Stacked Modal
   Navigation bar: Title  [Close ✕]

B. Content (per page)
   [ Image ]  (optional — recommended)
   Title: Clear, concise feature overview
   Description: Brief explanation (scrollable if long)

C. Call-To-Action
   [Next] — for first and middle pages (multi-page view)
   [Start] — for last page (multi-page) or single page

D. Page Indicator  ● ● ○ ○
   Shows progress in multi-page view
```

Navigation between pages: tap "Next", swipe left/right. Tap "Start" or "Close" → modal closes.

---

## Choosing a View Type

### List View
Use when:
- 3–6 updates to announce
- Short descriptions and/or small images
- Users should spend less time per update

### Page View
Use when:
- 1–4 updates to announce
- Long descriptions and/or large images
- Users should spend more time per update

Both support "with image" and "no image" variants. **Images are recommended.**

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

// Page view with multiple updates
struct WhatsNewView: View {
    @Environment(\.dismiss) private var dismiss
    @State private var currentPage = 0

    let updates: [AppUpdate] = [
        AppUpdate(
            title: "New Dashboard",
            description: "Your key metrics are now visible at a glance with the redesigned overview screen.",
            image: Image("whats-new-dashboard")
        ),
        AppUpdate(
            title: "Faster Search",
            description: "Search results now load 3x faster with offline caching support.",
            image: Image("whats-new-search")
        ),
        AppUpdate(
            title: "Dark Mode",
            description: "Full dark mode support across all screens.",
            image: Image("whats-new-dark")
        )
    ]

    var isLastPage: Bool { currentPage == updates.count - 1 }

    var body: some View {
        NavigationStack {
            TabView(selection: $currentPage) {
                ForEach(Array(updates.enumerated()), id: \.offset) { index, update in
                    VStack(spacing: 24) {
                        // B. Image (recommended)
                        update.image
                            .resizable()
                            .aspectRatio(contentMode: .fit)
                            .frame(maxHeight: 240)

                        VStack(spacing: 8) {
                            Text(update.title)
                                .font(.fiori(forTextStyle: .title2))
                                .multilineTextAlignment(.center)

                            ScrollView {
                                Text(update.description)
                                    .font(.fiori(forTextStyle: .body))
                                    .foregroundStyle(Color.preferredColor(.secondaryLabel))
                                    .multilineTextAlignment(.center)
                            }
                        }
                        .padding(.horizontal, 32)
                    }
                    .tag(index)
                }
            }
            .tabViewStyle(.page(indexDisplayMode: .never))

            // D. Page indicator
            HStack(spacing: 8) {
                ForEach(0..<updates.count, id: \.self) { index in
                    Circle()
                        .fill(index == currentPage
                              ? Color.preferredColor(.tintColor)
                              : Color.preferredColor(.separator))
                        .frame(width: 8, height: 8)
                }
            }
            .padding(.bottom, 16)

            // C. CTA button
            FioriButton { _ in Text(isLastPage ? "Start" : "Next") }
                .fioriButtonStyle(FioriPrimaryButtonStyle())
                .frame(maxWidth: .infinity)
                .padding(.horizontal, 32)
                .padding(.bottom, 40)
                .onTapGesture {
                    if isLastPage {
                        dismiss()
                    } else {
                        withAnimation { currentPage += 1 }
                    }
                }

            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .principal) {
                    Text("What's New")
                        .font(.fiori(forTextStyle: .headline))
                }
                ToolbarItem(placement: .primaryAction) {
                    FioriButton { _ in Image(systemName: "xmark").accessibilityLabel("Close") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { dismiss() }
                }
            }
        }
    }
}
```

---

## Adaptive Design

Supports compact and regular sizes, including landscape for both.

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use eye-catching images — they are optional but recommended
- Label the last-page button "Start" (not "Next")
- Allow swipe left/right navigation between pages
- Show "Close" button on all pages

**Don't:**
- Show a CTA button when accessed from the profile page
- Use the "What's New" component for routine navigation
- Show more than 6 items (use list view for 3–6, page view for 1–4)

---

## Related Patterns

- [single-user-onboarding.md](single-user-onboarding.md)
