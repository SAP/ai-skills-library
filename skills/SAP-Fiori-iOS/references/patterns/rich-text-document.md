# Rich Text Document — Pattern Guide

> SAP Fiori for iOS | Patterns / Onboarding

## What is it?

Text-heavy legal documents (EULA, privacy policies, terms and conditions) displayed in apps. This guide ensures consistent styling and accessibility across SAP iOS applications.

---

## Anatomy / Heading Structure

| Level | Use for | Font Style | Size | Color | Weight |
|-------|---------|-----------|------|-------|--------|
| Heading 1 | Document title | Title 1 / 72 | 28pt | Primary Label | Black |
| Heading 2 | Subtitle | Title 3 / 72 | 20pt | Primary Label | Bold |
| Heading 3 | Section headlines | Body Bold / 72 | 17pt | Primary Label | Bold |
| Heading 4 | Introduction | Body Bold / 72 | 17pt | Primary Label | Bold |
| Heading 5 | Supplementary info | Body / 72 | 17pt | Tertiary Label | Regular |
| Paragraph | Body text | Body / 72 | 17pt | Primary Label | Regular |
| List | Body text | Body / 72 | 17pt | Primary Label | Regular |

> **Note:** Single consent screens have no titles. See [consent-forms.md](consent-forms.md).

---

## List Styling

### Numbered Lists (ordered)
Numbers, letters, or Roman numerals: `1, 2, 3` / `1, 1.1, 1.2` / `A, a, Ⅰ, i`

### Bulleted Lists (unordered)
Nested bullet format:
- Level 1: **Disc** (•)
- Level 2: **Circle** (○)
- Level 3+: **Square** (▪)

In nested lists, numbers/bullets align with the indented text of the level above.

---

## SwiftUI Code Example

```swift
import SwiftUI
import FioriThemeManager

struct RichTextDocumentView: View {
    let htmlContent: String

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                // Render HTML content
                // Use WKWebView or AttributedString for HTML rendering
                HTMLContentView(html: styledHTML(htmlContent))
                    .padding(.horizontal, 16)
            }
        }
    }

    func styledHTML(_ content: String) -> String {
        """
        <html>
        <head>
        <style>
        body { font-family: '72'; font-size: 17px;
               color: \(cssColor(.primaryLabel)); }
        h1   { font-size: 28px; font-weight: 900; }
        h2   { font-size: 20px; font-weight: 700; }
        h3, h4 { font-size: 17px; font-weight: 700; }
        h5   { font-size: 17px; font-weight: 400;
               color: \(cssColor(.tertiaryLabel)); }
        p, li { font-size: 17px; font-weight: 400; }
        </style>
        </head>
        <body>\(content)</body>
        </html>
        """
    }
}
```

---

## Accessibility Rules

### Unique, descriptive link text
Each hyperlink must describe what it opens. Users of assistive technology may navigate links out of context.

```swift
// ✅ Descriptive
Link("View full Privacy Policy", destination: privacyPolicyURL)

// ❌ Generic
Link("Click here", destination: privacyPolicyURL)
```

### Alternative text for images
Every image in the document must have concise, informative alt text.

```swift
Image("agreement-diagram")
    .accessibilityLabel("Diagram showing data flow between user device and SAP servers")
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use heading levels to convey document structure (assistive tech relies on them)
- Use SAP 72 font and Fiori color tokens
- Add alt text to every image
- Use unique, descriptive link text
- Align nested list bullets with the parent level's indented text

**Don't:**
- Add a title to single consent screens — they intentionally have none
- Use raw hex colors — use Primary Label / Tertiary Label tokens
- Mix numbered and bulleted lists at the same level without clear hierarchy

---

## Related Patterns

- [single-user-onboarding.md](single-user-onboarding.md)
- [consent-forms.md](consent-forms.md)
