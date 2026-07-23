# SAP Fiori for iOS — Design Skill

A Claude Code skill that brings the full SAP Fiori for iOS design system into your AI-assisted workflow. It gives Claude deep, structured knowledge of every component, foundation, pattern, and platform extension — so you get correctly tokenised SwiftUI code, accurate Figma-to-code mappings, and consistent Fiori design decisions without hunting through documentation.

---

## What's inside

| Area | Coverage |
|------|----------|
| **Foundations** | Colors (Horizon palette, 400+ tokens), SAP 72 typography, iconography, elevation, animation specs, theming, adaptive layout, accessibility, design tokens, time & date formats |
| **Components** | 60+ components — buttons, cards, lists, forms, charts, KPIs, navigation, pickers, modals, onboarding, and more |
| **Page Types** | Overview Page, List Report, Object Details, Profile & Settings |
| **Patterns** | Navigation, Create & Edit, Search, Sort & Filter, Authentication, Onboarding, Charts, Modality, Hierarchy, Offline |
| **Joule** | SAP's AI copilot — UI kit, component guidelines, conversation patterns |
| **In-App AI Design** | Embedded AI components, AI handoff patterns, foundations |
| **watchOS** | Fiori for Apple Watch — foundations and guidelines |
| **visionOS** | Fiori for Apple Vision Pro — foundations and guidelines |
| **CarPlay** | Fiori for automotive — design principles |
| **Figma UI Kit** | Direct integration with the SAP Fiori iOS UI Kit (file key `1450853598524410675`) — read component nodes, map variants to SwiftUI |
| **References** | Quick-lookup color token table |

---

## Installation

### Prerequisites

- [Claude Code](https://claude.ai/code) CLI installed
- macOS with zsh or bash

### Install

```bash
# 1. Clone or copy the skill into the agents skills directory
cp -r /path/to/fiori-ios-guidelines ~/.agents/skills/fiori-ios-guidelines

# 2. Link it so Claude Code can discover it
mkdir -p ~/.claude/skills
ln -sf ~/.agents/skills/fiori-ios-guidelines ~/.claude/skills/fiori-ios-guidelines
```

If you are working from the source project directory:

```bash
cp -r ~/Desktop/sap-fiori-ios-guidelines ~/.agents/skills/fiori-ios-guidelines
mkdir -p ~/.claude/skills
ln -sf ~/.agents/skills/fiori-ios-guidelines ~/.claude/skills/fiori-ios-guidelines
```

### Verify

Restart Claude Code, then run:

```
/fiori-ios-guidelines
```

Claude will confirm the skill is loaded and ready.

---

## Usage

Once installed the skill activates automatically when your prompt mentions any of the following trigger terms: **Fiori iOS**, **SwiftUI**, **iOS prototype**, **Figma to iOS**, **FioriButton**, **FioriTheme**, **animation**, **interaction**, **SAP 72**, **preferredFioriColor**, **ObjectItem**, **FioriSwiftUI**.

You can also invoke it explicitly:

```
/fiori-ios-guidelines <your question or request>
```

### How Claude uses the skill

- Reads the relevant component or foundation file before generating code
- Uses `Color.preferredColor(...)` tokens — never hardcoded hex values
- Maps Figma variant properties to the correct SwiftUI API
- Applies standard animation specs from the skill's animation table
- Respects Fiori layout, typography, and accessibility rules

---

## Example prompts

### Convert a Figma component to SwiftUI

```
Convert Figma node 123:456 from the SAP Fiori iOS UI Kit into SwiftUI.
```

```
Turn this Figma ObjectItem (3-line, with icon, Status: Warning) into SwiftUI code.
```

### Build a screen from scratch

```
Build a List Report page in SwiftUI using Fiori components — searchable list of
purchase orders, each row showing vendor name, amount, and a status tag.
```

```
Create a Fiori Object Details screen for an invoice with a header, key-value form
section, and a primary + secondary action button pair.
```

### Component guidance

```
Which Fiori component should I use for a multi-step approval workflow?
```

```
What's the correct Fiori pattern for showing an empty state when a search returns
no results?
```

### Animation and interaction

```
Add a Fiori-spec press animation to my custom card component.
```

```
What are the correct animation parameters for a view sliding in from the bottom?
```

### Theming and tokens

```
How do I override the tint color for a specific brand without breaking dark mode?
```

```
List all semantic color tokens related to status indicators (positive, negative,
critical, informative).
```

### Platform extensions

```
What Joule components are available for an in-app AI assistant on iOS?
```

```
How should I adapt a Fiori List Report layout for visionOS?
```

### Accessibility

```
Audit this SwiftUI view for Fiori accessibility compliance — Dynamic Type,
VoiceOver labels, and minimum touch target sizes.
```

---

## Key rules the skill enforces

**Never hardcode hex values.** Always use Fiori color tokens:

```swift
Color.preferredColor(.primaryLabel)              // adapts to Light / Dark
Color.preferredColor(.tintColor, background: .darkConstant)  // forced scheme
```

**Register the SAP 72 typeface at launch:**

```swift
import FioriThemeManager

ThemeManager.shared.setPaletteVersion(.v8)
Font.registerFioriFonts()
```

**Use Fiori font styles, not system styles:**

```swift
Text("Headline").font(.fiori(forTextStyle: .headline))
Text("42").font(.fiori(fixedSize: 36, weight: .light))
```

---

## File structure

```
fiori-ios-guidelines/
├── SKILL.md                  # Skill entry point — Figma mappings, quick-start template
├── README.md                 # This file
├── foundations/              # Colors, typography, theming, accessibility, animation …
├── components/               # 60+ individual component guidelines
├── patterns/                 # Navigation, search, auth, onboarding, charts …
├── page-types/               # Full-screen templates
├── joule/                    # SAP Joule AI copilot guidelines
├── in-app-ai-design/         # Embedded AI components and patterns
├── watchos/                  # Apple Watch guidelines
├── visionos/                 # Apple Vision Pro guidelines
├── carplay/                  # CarPlay automotive guidelines
├── discover/                 # Get started, design system overview, what's new
├── resources/                # UI kit links, Mentor app reference
├── references/               # Quick-lookup tables (colors)
└── .well-known/skills/       # Skill discovery manifest
```

---

## Resources

- [SAP Fiori for iOS UI Kit on Figma](https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit)
- [SAP Fiori Design Guidelines](https://experience.sap.com/fiori-design-ios/)
- [FioriSwiftUI on GitHub](https://github.com/SAP/cloud-sdk-ios-fiori)
