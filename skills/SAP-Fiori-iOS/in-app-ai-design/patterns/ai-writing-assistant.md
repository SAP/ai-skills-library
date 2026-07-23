# AI Writing Assistant — In-App AI Design

> SAP Fiori for iOS | In-App AI Design / Patterns
> Development reference: `waTextInput`, `waResult`, `waFeedbackResult`, `waHelperAction`

## What is it?

The AI writing assistant edits text in text input fields via a panel of quick prompts, allowing users to refine content efficiently. Opens as a panel above the keyboard (compact) or as a popover (regular/iPad).

---

## When to Use

**Do:**
- Repetitive text writing and editing tasks
- Sparking creativity with diverse outputs
- Accelerating text iteration and refinement

**Don't:**
- Non-text editing tasks
- Customized outputs (use guided prompts, custom prompts, or Joule instead)
- Fields where AI editing adds no value (pre-populated confident AI recommendations, unpredictable user intent, insufficient context)

---

## Anatomy

**A. Entry point** — "Writing Assistant" button opens the panel
**B. Text input field** — updated text highlighted in blue after each AI edit; full text updated unless user pre-selects a portion
**C. Panel navigation bar** — Cancel / Done + version annotation ("Version 2/2")
**D. Undo / Redo buttons** — navigate version history; disabled at boundaries
**E. Quick prompts** — immediately update the text; icons optional but must be consistent
**F. Prompt groups** — categories of quick prompts; always show disclosure chevron
**G. Feedback** — thumbs up/down after each text update

---

## Interaction Flow

1. User taps "Writing Assistant" button → panel opens
2. Before any edit: panel shows "×" close button (immediate close, no confirmation)
3. After first edit: nav changes to **Cancel / Done**
4. **Done** → saves latest text, closes panel
5. **Cancel** → confirmation dialog; user can continue editing or discard changes
6. Tapping outside panel → confirmation dialog

---

## Versioning

- Each quick prompt tap creates a new version
- Version annotation updates: "Version 2/3", "Version 3/3"
- Undo → go to previous version; select new prompt → replaces all subsequent versions
- Undo disabled at first version; Redo disabled at latest version

---

## Recommended Text Labels

### Quick Prompts

| Menu label | Performed AI prompt text | Action |
|-----------|-------------------------|--------|
| Generate | Generated Text | Create first version |
| Regenerate | Regenerated Text | Regenerate with same prompt |
| Fix Spelling and Grammar | Fixed Spelling and Grammar | Correct errors |
| Make Bulleted List | Made Bulleted List | Organize into a list |
| Translate → \<Language\> | Translated to \<Language\> | Convert to language |

### Prompt Groups (with submenus)

| Group | Submenu items | Performed text |
|-------|--------------|----------------|
| Rewrite Text | Simplify / Expand / Summarize | Simplified / Expanded / Summarized Text |
| Change Tone | Make More Casual / Make More Professional | Made More Casual / Made More Professional |
| Adjust Length | Make Shorter / Make Longer | Shortened / Lengthened Text |

**Rule for unlisted prompts:** Use imperative verb; keep short; be consistent.

---

## Icon Rules

- Prompt **groups** always have a **disclosure chevron** (→)
- Quick prompt icons: optional; if used, **use consistently for all quick prompts** — don't mix icon and no-icon prompts
- Align icon usage across SAP apps where possible

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct WritingAssistantView: View {
    @Binding var text: String
    @State private var showAssistant = false
    @State private var showCancelConfirmation = false
    @State private var hasEdited = false
    @State private var versionHistory: [String] = []
    @State private var currentVersionIndex = 0

    var body: some View {
        VStack {
            // B. Text input — highlighted after AI edit
            TextEditor(text: $text)
                .font(.fiori(forTextStyle: .body))
                .frame(minHeight: 100)

            // A. Entry point button
            FioriButton { _ in
                HStack(spacing: 6) {
                    Image(systemName: "sparkles")
                    Text("Writing Assistant")
                }
            }
            .fioriButtonStyle(FioriSecondaryButtonStyle())
            .onTapGesture {
                versionHistory = [text]
                currentVersionIndex = 0
                showAssistant = true
            }
        }
        .sheet(isPresented: $showAssistant) {
            WritingAssistantPanel(
                text: $text,
                versionHistory: $versionHistory,
                currentVersionIndex: $currentVersionIndex,
                hasEdited: $hasEdited,
                onDismiss: { showAssistant = false }
            )
            .presentationDetents([.medium, .large])
        }
    }
}

struct WritingAssistantPanel: View {
    @Binding var text: String
    @Binding var versionHistory: [String]
    @Binding var currentVersionIndex: Int
    @Binding var hasEdited: Bool
    let onDismiss: () -> Void

    @State private var showCancelDialog = false

    var canUndo: Bool { currentVersionIndex > 0 }
    var canRedo: Bool { currentVersionIndex < versionHistory.count - 1 }
    var versionLabel: String { "Version \(currentVersionIndex + 1)/\(versionHistory.count)" }

    var body: some View {
        NavigationStack {
            VStack(spacing: 0) {
                // D. Undo / Redo
                if hasEdited {
                    HStack {
                        Button("Undo") { undo() }.disabled(!canUndo)
                        Spacer()
                        Text(versionLabel)
                            .font(.fiori(forTextStyle: .footnote))
                            .foregroundStyle(Color.preferredColor(.secondaryLabel))
                        Spacer()
                        Button("Redo") { redo() }.disabled(!canRedo)
                    }
                    .padding(.horizontal, 16)
                    .padding(.vertical, 8)
                    Divider()
                }

                // E. Quick prompts + F. Prompt groups
                List {
                    Section {
                        QuickPromptRow(label: "Fix Spelling and Grammar",
                                       icon: Image(systemName: "checkmark.circle")) {
                            applyPrompt("Fix Spelling and Grammar")
                        }
                        QuickPromptRow(label: "Make Bulleted List",
                                       icon: Image(systemName: "list.bullet")) {
                            applyPrompt("Make Bulleted List")
                        }
                    }

                    Section {
                        // F. Prompt group — always has disclosure chevron
                        NavigationLink("Rewrite Text") {
                            RewriteTextSubmenu(onSelect: applyPrompt)
                        }
                        NavigationLink("Change Tone") {
                            ChangeToneSubmenu(onSelect: applyPrompt)
                        }
                        NavigationLink("Adjust Length") {
                            AdjustLengthSubmenu(onSelect: applyPrompt)
                        }
                    }
                }

                // G. Feedback (after each edit)
                if hasEdited {
                    AIUserFeedbackInline(context: "Writing Assistant")
                        .padding(16)
                }
            }
            .navigationTitle(hasEdited ? "Writing Assistant" : "Writing Assistant")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: hasEdited ? .cancellationAction : .primaryAction) {
                    if hasEdited {
                        Button("Cancel") { showCancelDialog = true }
                    } else {
                        Button {
                            onDismiss()
                        } label: {
                            Image(systemName: "xmark")
                        }
                    }
                }
                if hasEdited {
                    ToolbarItem(placement: .confirmationAction) {
                        Button("Done") { onDismiss() }
                    }
                }
            }
            .confirmationDialog(
                "Discard changes?",
                isPresented: $showCancelDialog,
                titleVisibility: .visible
            ) {
                Button("Discard", role: .destructive) {
                    text = versionHistory[0]  // revert to original
                    onDismiss()
                }
                Button("Keep Editing", role: .cancel) {}
            } message: {
                Text("Your text edits will be lost.")
            }
        }
    }

    func applyPrompt(_ prompt: String) {
        hasEdited = true
        // Remove any subsequent versions (undo branching)
        versionHistory = Array(versionHistory.prefix(currentVersionIndex + 1))
        // Apply AI transformation
        let newText = applyAITransformation(text: text, prompt: prompt)
        versionHistory.append(newText)
        currentVersionIndex = versionHistory.count - 1
        text = newText
    }

    func undo() {
        currentVersionIndex -= 1
        text = versionHistory[currentVersionIndex]
    }

    func redo() {
        currentVersionIndex += 1
        text = versionHistory[currentVersionIndex]
    }
}
```

---

## Adaptive Design

| Size class | Presentation |
|-----------|-------------|
| Compact (iPhone) | Panel above keyboard |
| Regular (iPad) | Popover; text highlight non-interactive while popover is open |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Highlight updated text in blue after each AI edit
- Show Cancel/Done only after the first edit (not before)
- Show confirmation dialog when user tries to exit after editing
- Include AI notice on text fields that received AI edits
- Use consistent icons: either all prompts have icons, or none do
- Always show disclosure chevron on prompt groups

**Don't:**
- Use for non-text tasks
- Show AI writing assistant where AI editing adds no value
- Mix icon and no-icon quick prompts in the same panel

---

## Related

- [ai-notice.md](ai-notice.md)
- [ai-user-feedback.md](ai-user-feedback.md)
- [ai-ui-text.md](ai-ui-text.md)
- [../components/text-inputs.md](../components/text-inputs.md)
