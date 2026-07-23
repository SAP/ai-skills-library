# Create & Edit — Pattern Guide

> SAP Fiori for iOS | Patterns
> Development reference: Create and Filter Patterns SDK

## What is it?

The create & edit pattern generates or updates business objects via a modal. Triggered by a "+" or "Edit" action in the navigation bar, it presents a form with grouped input cells for the object's properties.

**The edit modal should be identical to the create modal** to avoid user confusion.

---

## Anatomy

```
A. Navigation Bar: [Cancel]   "New Invoice"   [Save]
──────────────────────────────────────────────────────
B. Key Information
   [ Title form cell — required fields ]
   [ Text field — required fields ]

C. Properties
   [ List Picker ]
   [ Date Picker ]
   [ Switch ]
   [ Segmented Control ]
   [ Additional text fields ]

D. Accessory (bottom)
   [ Notes / Key Value form cell ]
   [ Attachment form cell ]
```

**A. Navigation Bar** — title + "Cancel" (left) + "Save"/"Create"/"Add" (right)
**B. Key Information** — most important fields; some may be required or pre-populated
**C. Properties** — additional object properties; group by data type/hierarchy
**D. Accessory** — notes, attachments; always at bottom

---

## Form Cells Used

| Cell type | Use when |
|-----------|---------|
| **Title form cell** | Short single-line text (object name, title) |
| **Text field form cell** | Labeled inputs; use stacked variant for long content or small screens |
| **Key value form cell** | Multi-line text; fixed height when accessories follow, flexible when last field |
| **List picker form cell** | Single or multi-select from a defined category |
| **Pickers** | Date, time, or date+time selection; default = current date/time |
| **Segmented control form cell** | Quick single-select from a small set of short values |
| **Switch form cell** | Boolean on/off property; may reveal additional fields when on |
| **Attachment form cell** | File uploads (image, video, audio); always at bottom |

---

## Launch

Triggered by tapping the "+" button in the navigation bar → presents the create modal.

---

## Adaptive Design

| Context | Presentation |
|---------|-------------|
| Compact (iPhone) | Full-screen modal |
| Regular — single action behind "+" | Popover |
| Regular — multiple actions behind "+" | Form sheet modal |

```swift
@Environment(\.horizontalSizeClass) var hSizeClass
@State private var showCreate = false

// Trigger button
FioriButton { _ in Image(systemName: "plus").accessibilityLabel("Create") }
    .fioriButtonStyle(FioriTertiaryButtonStyle())
    .onTapGesture { showCreate = true }

// Compact: full-screen
.fullScreenCover(isPresented: $showCreate.projectedValue,
                 isPresented: hSizeClass == .compact) {
    CreateFormView()
}

// Regular (single action): popover
.popover(isPresented: $showCreate.projectedValue,
         isPresented: hSizeClass != .compact) {
    CreateFormView()
        .frame(width: 375, height: 600)
}
```

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct CreateInvoiceView: View {
    @Environment(\.dismiss) private var dismiss
    @State private var title = ""
    @State private var vendor: String? = nil
    @State private var amount = ""
    @State private var dueDate = Date()
    @State private var isAutoApprove = false
    @State private var notes = ""
    @State private var attachments: [AttachmentItem] = []
    @State private var showSuccessToast = false

    var canSave: Bool { !title.isEmpty && vendor != nil }

    var body: some View {
        NavigationStack {
            List {
                // B. Key information
                Section("Key Information") {
                    TitleFormView(
                        title: { Text("Invoice Title *") },
                        text: $title,
                        placeholder: { Text("Enter title") }
                    )
                    ListPickerItem(
                        title: { Text("Vendor *") },
                        value: { Text(vendor ?? "Select vendor") },
                        destination: { VendorPickerView(selection: $vendor) }
                    )
                }

                // C. Properties
                Section("Details") {
                    TextFieldFormView(
                        title: { Text("Amount") },
                        text: $amount,
                        prefix: { Text("USD") },
                        keyboardType: .decimalPad
                    )
                    DateTimePicker(
                        title: { Text("Due Date") },
                        selection: $dueDate,
                        pickerComponents: .date
                    )
                    SwitchView(
                        title: { Text("Auto-Approve") },
                        isOn: $isAutoApprove
                    )
                }

                // D. Accessory
                Section {
                    KeyValueFormView(
                        title: { Text("Notes") },
                        text: $notes,
                        placeholder: { Text("Add notes…") }
                    )
                    // Attachment always last
                    Attachment(attachments: $attachments)
                }
            }
            .navigationTitle("New Invoice")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    FioriButton { _ in Text("Cancel") }
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .onTapGesture { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    FioriButton { _ in Text("Create") }  // not "Done"
                        .fioriButtonStyle(FioriTertiaryButtonStyle())
                        .disabled(!canSave)
                        .onTapGesture { save() }
                }
            }
        }
        .overlay(alignment: .bottom) {
            if showSuccessToast {
                ToastMessage { Text("Invoice created") } icon: {
                    Image(systemName: "checkmark.circle.fill")
                        .foregroundStyle(Color.preferredColor(.positiveLabel))
                }
                .padding(.bottom, 24)
                .onAppear {
                    DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
                        withAnimation { showSuccessToast = false }
                        dismiss()
                    }
                }
            }
        }
    }

    func save() {
        createInvoice(title: title, vendor: vendor!, amount: amount, dueDate: dueDate)
        showSuccessToast = true
    }
}
```

---

## Feedback After Save

Show a `ToastMessage` after the user taps Save/Create to confirm the action. Then dismiss.

```swift
// ✅ Toast confirms completion
ToastMessage { Text("Invoice created") }

// ✅ Or for edits
ToastMessage { Text("Changes saved") }
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use "Create" / "Add" / "Save" for the confirmation button — not "Done" (too vague)
- Make the edit modal identical to the create modal
- Show a toast message on successful save
- Group form cells by data hierarchy: key info → properties → accessory
- Place attachments at the bottom of the form
- On regular width with a single action: use a popover; with multiple: use a form sheet

**Don't:**
- Use "Done" as the save button label
- Omit the toast confirmation after saving
- Put attachments anywhere but the bottom

---

## Related Patterns

- [authentication-overview.md](authentication-overview.md)
- [../components/text-inputs.md](../components/text-inputs.md)
- [../components/attachment-form-cell.md](../components/attachment-form-cell.md)
- [../components/toast-message.md](../components/toast-message.md)
- [../foundations/modals.md](../components/modals.md)
