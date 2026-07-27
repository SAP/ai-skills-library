# Attachment Form Cell — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIAttachmentsFormCell`, SwiftUI `Attachment`

## What is it?

An attachment control allows users to upload files — images, audio, video, text, PDFs, CSVs, and presentations — to a form. The "Add (+)" button enables users to upload from the photo library or other supported apps.

---

## When to Use

**Do:**
- Use as the **last piece of information** in a create screen or edit mode workflow
- Place at the **bottom** of a create modal, object page, or object detail page

**Don't:**
- Use for uploading profile images — use an avatar picker instead

---

## Anatomy

```
A. Label: "Attachments (3)"     [B. Add (+) button]   ← hidden in read-only
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  C. Preview  │ │  C. Preview  │ │  C. Preview  │  → overflow to next row
│  D. Name     │ │  D. Name     │ │  D. Name     │
│  D. Size     │ │  D. Size     │ │  D. Date     │
└──────────────┘ └──────────────┘ └──────────────┘
```

### A. Label
Shows the count of attachments in the container.

### B. Add (+) Button
- **Active state** — visible; allows adding attachments
- **Read-only / disabled state** — hidden

### C. Attachment Item
Preview of the image, video, or document. If no preview is available, shows a doctype icon with the file name. Tapping opens a modal previewer.

### D. Attachment Text Content
- Line 1 — **mandatory**: attachment item name
- Line 2 — optional: file size, date uploaded, or other metadata
- Line 3 — optional

---

## States

| State | Add (+) | View | Delete |
|-------|---------|------|--------|
| Active | Visible | ✓ | ✓ (in previewer) |
| Read-only | Hidden | ✓ | ✗ (delete icon disabled) |
| Disabled | Hidden | ✗ | ✗ |

---

## Behavior & Interaction

### Adding Attachments
1. Tap "Add (+)" → action sheet with source options (photo library, files app, camera, etc.)
2. Select source → modal drill-down to select the file
3. Modal slides down → attachment appears in the grid

The "Add (+)" button **stays in place** as attachments are added. New attachments appear to the right. When the row is full, attachments overflow to the next row.

**Large files:** Show a loading state while the file is processing.

### Viewing Attachments
Tap an attachment item → full previewer opens. User can swipe through all attachment items.

### Deleting Attachments
In the previewer, tap the "Delete" icon (top right). Optionally show a confirmation dialog before deleting. After deletion, the grid and label count update automatically.

### Error Handling
If a file fails to upload, a **red error icon** appears on the attachment item. Tapping it shows the error reason. Display a semantic error message below the attachment form cell with details or guidance on how to resolve.

---

## Adaptive Design

| Context | Layout |
|---------|--------|
| iPhone (compact) | Single-column grid |
| iPad modal compact | Compact grid in modal |
| iPad regular-readable | Wider grid |

---

## SwiftUI Code Examples

### Basic attachment form cell
```swift
import FioriSwiftUICore

@State private var attachments: [AttachmentItem] = []

Attachment(
    attachments: $attachments,
    title: { Text("Attachments (\(attachments.count))") },
    addAction: {
        // Present source picker
        showAttachmentPicker = true
    }
)
```

### Full workflow with states
```swift
@State private var attachments: [AttachmentItem] = []
@State private var isReadOnly = false
@State private var showPicker = false
@State private var isUploading = false

VStack(alignment: .leading, spacing: 0) {
    // Place at bottom of form
    Attachment(
        attachments: $attachments,
        isEditable: !isReadOnly
    ) {
        // Add button action
        showPicker = true
    }
    .disabled(isReadOnly)

    // Semantic error message if upload failed
    if let uploadError {
        Text(uploadError)
            .font(.fiori(forTextStyle: .footnote))
            .foregroundStyle(Color.preferredColor(.negativeLabel))
            .padding(.top, 4)
    }
}
.sheet(isPresented: $showPicker) {
    AttachmentSourcePicker { result in
        Task {
            isUploading = true
            do {
                let item = try await upload(result)
                attachments.append(item)
            } catch {
                uploadError = error.localizedDescription
            }
            isUploading = false
        }
    }
}
```

### Loading state for large files
```swift
VStack {
    Attachment(attachments: $attachments)

    if isUploading {
        HStack(spacing: 8) {
            ProgressView()
                .tint(Color.preferredColor(.tintColor))
            Text("Uploading…")
                .font(.fiori(forTextStyle: .footnote))
                .foregroundStyle(Color.preferredColor(.secondaryLabel))
        }
        .padding(.top, 8)
    }
}
```

### Read-only (view-only, no add/delete)
```swift
// In view mode — Add (+) button hidden, delete disabled in previewer
Attachment(
    attachments: .constant(existingAttachments),
    isEditable: false
)
```

### With delete confirmation
```swift
Attachment(
    attachments: $attachments,
    onDelete: { item in
        // Show confirmation before removing
        itemToDelete = item
        showDeleteConfirmation = true
    }
)
.confirmationDialog(
    "Delete attachment?",
    isPresented: $showDeleteConfirmation,
    titleVisibility: .visible
) {
    Button("Delete", role: .destructive) {
        if let item = itemToDelete {
            attachments.removeAll { $0.id == item.id }
        }
    }
    Button("Cancel", role: .cancel) {}
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| State | Active | `isEditable: true` (default) |
| State | Read-only | `isEditable: false` |
| State | Disabled | `.disabled(true)` |
| Add button | Visible | Active state |
| Add button | Hidden | Read-only or disabled |
| Preview | Image | Thumbnail rendered by SDK |
| Preview | No preview | Doctype icon + filename |
| Error | Upload failed | Red error icon on item + semantic error text below |
| Loading | Large file | `ProgressView` below attachment grid |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Place at the **bottom** of the form — it is always the last field
- Show a loading state when uploading large files
- Display a semantic error message below the cell (not just the red icon on the item)
- Optionally confirm before deleting attachments
- Update the label count automatically after add/delete

**Don't:**
- Use for profile image uploads
- Place in the middle or top of a form
- Hide the error — always surface upload failures with both an icon and a message

---

## Related Components

- [text-inputs.md](text-inputs.md) — other input form cells
- [illustrated-message.md](illustrated-message.md) — empty state before any attachment is added
