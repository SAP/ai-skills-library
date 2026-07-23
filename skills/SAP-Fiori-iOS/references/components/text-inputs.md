# Text Inputs — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit` (Forms page)
> Development reference: UIKit `FUITextFieldFormCell`, `FUIKeyValueFormCell`, `FUINoteFormCell`, `FUITitleFormCell`, SwiftUI `TextFieldFormView`, `KeyValueFormView`, `NoteFormView`, `TitleFormView`

## What is it?

Text input controls request text entry from the user. They are used in create and edit patterns.

---

## Required / Optional Labeling

| Rule | Pattern |
|------|---------|
| Required field | Asterisk (*) after the label: "Vendor *" |
| Optional field | "(optional)" after the label: "Notes (optional)" |
| Form with mostly required fields | Mark required fields with * |
| Form with mostly optional fields | Mark optional fields with (optional) |

Always include a note at the top of the form: *"* indicates required fields"*

---

## Anatomy

```
A. Label: "Invoice Number *"
┌────────────────────────────────── [D. Icon] ──┐
│ B. Input field (placeholder text)             │
└───────────────────────────────── [E. 24/100] ─┘
C. Semantic message (helper / error / warning)
```

**A. Label** — intent of the field. Required / optional marking applies here.
**B. Input Field** — tappable area. Shows "Clear" button while typing.
**C. Semantic Message** (optional) — helper text, error, warning, or success. Wraps as needed. In read-only state: "Read-only field".
**D. Right Accessory Icon** (optional) — barcode or OCR scanner to populate the field.
**E. Character Counter** (optional) — real-time count over limit (e.g. "24/100").

---

## Variations

### Title Form Cell
Single-line, fixed-height input for self-explanatory content (object title, person name).

- Always include clear prompt text ("Title", "Description")
- Mark required with (*), e.g. "Title *"
- Avoid vague prompts like "Tap to Write"
- Error state indicated via **inline banner** (not label/outline color — different from other text inputs)

**States:** Default, Typing, Typed, Disabled, Read-only

```swift
import FioriSwiftUICore

TitleFormView(
    title: { Text("Subject *") },
    text: $subject,
    placeholder: { Text("Enter subject") }
)
```

### Text Field Form Cell
Single-line, fixed-height. Label is required; placeholder is optional and should describe the expected format or type.

**Features:**
- **Grouped format** — parentheses/hyphens for phone numbers, credit card numbers
- **Prefix** — left-aligned unit or symbol (e.g. "USD", "+1")
- **Suffix** — right-aligned unit; moves with cursor (e.g. "kg", "%")
- **Barcode/OCR icon** — right accessory to populate field via scanner
- Error: label + bounding box outline turn red; helper text appears/changes to error message

**States:** Default, Active, Typing, Typed, Disabled, Read-only, Error

```swift
// Standard
TextFieldFormView(
    title: { Text("Vendor *") },
    text: $vendor,
    placeholder: { Text("Enter vendor name") },
    isRequired: true
)

// With prefix
TextFieldFormView(
    title: { Text("Amount *") },
    text: $amount,
    placeholder: { Text("0.00") },
    prefix: { Text("USD") }
)

// With suffix
TextFieldFormView(
    title: { Text("Weight") },
    text: $weight,
    placeholder: { Text("0.0") },
    suffix: { Text("kg") }
)

// With barcode scanner icon
TextFieldFormView(
    title: { Text("Item Barcode") },
    text: $barcode,
    controlState: .normal
) {
    FioriButton { _ in
        Image(systemName: "barcode.viewfinder")
            .accessibilityLabel("Scan barcode")
    }
    .fioriButtonStyle(FioriTertiaryButtonStyle())
    .onTapGesture { openBarcodeScanner() }
}

// Grouped format (phone number)
TextFieldFormView(
    title: { Text("Phone") },
    text: $phone,
    placeholder: { Text("(555) 000-0000") },
    keyboardType: .phonePad
)

// Read-only
TextFieldFormView(
    title: { Text("Invoice Number") },
    text: .constant("INV-2026-001"),
    controlState: .readonly,
    helperText: { Text("Read-only field") }
)

// Error state
TextFieldFormView(
    title: { Text("Email *") },
    text: $email,
    errorMessage: emailError.map { AttributedString($0) },
    helperText: emailError == nil ? { Text("Enter your SAP email address") } : nil
)
```

### Key Value Form Cell
Multi-line text entry **with a label**. Height behavior:

- **Fixed height** (with scroll) — when other accessories follow below (e.g. attachments)
- **Flexible height** (grows down) — when it is the bottommost component in the create pattern

Error: same as text field (label + outline red, helper text changes to error).

```swift
KeyValueFormView(
    title: { Text("Description") },
    text: $description,
    placeholder: { Text("Describe the invoice…") },
    minHeight: 100
)

// Fixed height when not last field
KeyValueFormView(
    title: { Text("Notes") },
    text: $notes,
    minHeight: 80,
    maxHeight: 120  // fixed — scroll appears if content exceeds
)
```

### Note Form Cell
Multi-line text entry **without a label**. Same behavior as Key Value Form Cell.

```swift
NoteFormView(
    text: $notes,
    placeholder: { Text("Add notes…") }
)
```

---

## Behavior

### Keyboard
Tapping any text input opens the keyboard automatically. Use the appropriate keyboard type for the data:

| Data type | Keyboard |
|-----------|---------|
| Phone number | `.phonePad` |
| Number | `.numberPad` or `.decimalPad` |
| Email | `.emailAddress` |
| URL | `.URL` |
| Default text | `.default` |

### Clear Button
A "Clear" button appears while the user is typing. Tapping it clears all content in the field.

---

## Error Handling

| Component | Error visual |
|-----------|-------------|
| Text Field, Key Value, Note | Label + outline turn **red**; helper text becomes error message |
| Title Form Cell | Inline **banner** (not label/outline color) |

- Error persists until the user corrects it
- When the user starts typing in an errored field, the error clears
- If helper text existed before the error, it **reverts to helper text** after correction
- For form-level errors, combine with a `BannerMessage`

---

## Character Counter

Optional. Shows real-time character count over the limit (e.g. "24/100").

### Hard limit (typing stops at limit)
Input automatically stops at the character limit. Helper text changes to **"Character limit reached"**.

### Soft limit (typing continues past limit — error)
User can type past the limit; counter turns **red**; helper text changes to **"Reduce the number of characters"**. Error persists until input is shortened within the limit.

```swift
TextFieldFormView(
    title: { Text("Subject *") },
    text: $subject,
    maxLength: 100,      // hard limit — typing stops
    showsCharacterCount: true
)

NoteFormView(
    text: $notes,
    maxLength: 500,      // soft limit — error shown when exceeded
    enforcesMaxLength: false,
    showsCharacterCount: true
)
```

---

## Currency Format

For currency entry, the text field:
1. Displays the ISO currency code in the input label (e.g. "USD")
2. Applies localized formatting (separators, decimals) as the user types
3. After editing ends, can display the corresponding currency symbol
4. Symbol placement and formatting follow the locale — customizable if needed

```swift
TextFieldFormView(
    title: { Text("Amount") },
    text: $amountText,
    prefix: { Text("USD") },
    keyboardType: .decimalPad,
    placeholder: { Text("0.00") }
)
// Apply locale-aware formatting on .onSubmit or focus change
.onSubmit { amountText = formatCurrency(amountText, locale: .current) }
```

---

## Full Form Example

```swift
Form {
    // Required field indicator at top
    Section(footer: Text("* indicates required fields")
        .font(.fiori(forTextStyle: .footnote))
        .foregroundStyle(Color.preferredColor(.secondaryLabel))) {

        TextFieldFormView(
            title: { Text("Vendor *") },
            text: $vendor,
            isRequired: true,
            errorMessage: vendorError.map { AttributedString($0) }
        )

        TextFieldFormView(
            title: { Text("Amount *") },
            text: $amount,
            prefix: { Text("USD") },
            keyboardType: .decimalPad,
            isRequired: true
        )

        TextFieldFormView(
            title: { Text("Reference (optional)") },
            text: $reference,
            placeholder: { Text("e.g. PO-1234") }
        )

        KeyValueFormView(
            title: { Text("Notes (optional)") },
            text: $notes,
            placeholder: { Text("Add any relevant notes…") }
        )
    }
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI |
|---------------|-------------|---------|
| Variation | Title | `TitleFormView` |
| Variation | Text field | `TextFieldFormView` |
| Variation | Key value | `KeyValueFormView` |
| Variation | Note | `NoteFormView` |
| Required | Yes | `isRequired: true` + " *" in label |
| Optional | Yes | "(optional)" in label text |
| State | Default | Normal |
| State | Active | Focused — keyboard up |
| State | Typing | Keyboard + clear button visible |
| State | Typed | Value present |
| State | Disabled | `.disabled(true)` |
| State | Read-only | `controlState: .readonly` |
| State | Error | `errorMessage: AttributedString(...)` |
| Prefix | Yes | `prefix: { Text("USD") }` |
| Suffix | Yes | `suffix: { Text("kg") }` |
| Scanner icon | Yes | Right accessory icon |
| Character counter | Hard limit | `maxLength:` + `showsCharacterCount: true` |
| Character counter | Soft limit | `enforcesMaxLength: false` |
| Currency | Yes | ISO prefix + locale formatting on submit |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Mark required fields with * and note the convention at the top of the form
- Show "Read-only field" helper text on read-only cells
- Revert error helper text back to original helper text when the error is corrected
- Use appropriate keyboard types for the data being entered
- Show character counter when there is a meaningful limit
- Fix key value cell height (with scroll) when other accessories follow; allow flexible growth when it's the last field

**Don't:**
- Use vague placeholder text like "Tap to Write" in title form cells
- Leave error state without an explanatory helper text message
- Omit the (optional) label when the form has few optional fields among many required ones

---

## Related Components

- [inline-validation.md](inline-validation.md) — error/warning/success messages below inputs
- [banner.md](banner.md) — form-level error banner
- [forms.md](forms.md) — complete form pattern reference
