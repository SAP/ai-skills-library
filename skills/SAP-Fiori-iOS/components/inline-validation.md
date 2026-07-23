# Inline Validation — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Input and Selection
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIInlineValidationTableViewCell`, `FUIInlineValidationView`

## What is it?

Inline validation provides static information or temporary feedback in response to user input. It is placed directly beneath the relevant form cell and can display helper text, success, warning, or error messages.

---

## Anatomy

```
[ Input Field ]
[A. Icon]  B. Message text     ← directly below the field
```

**A. Icon** — visually accessible cue. Present for success, warning, and error. **Helper text has no icon.**

**B. Text** — succinct, clear message. Wraps to maximum **3 lines** in some cases; **1 line recommended**.

---

## Variations

| Variation | Icon | Color | Persistence |
|-----------|------|-------|-------------|
| Helper text | None | `.secondaryLabel` | **Persists** always |
| Success | ✓ | `.positiveLabel` | Temporary — may disappear |
| Warning | ⚠ | `.criticalLabel` | Temporary — may disappear |
| Error | ✕ | `.negativeLabel` | Disappears when error is corrected |

---

## Behavior

### Helper Text
Provides persistent contextual information. Always visible. When a success, warning, or error message needs to appear temporarily, it replaces the helper text — then **reverts back to helper text** once resolved.

### Success / Warning
Appears in response to user interaction. May disappear after a short time.

### Error
Appears in response to invalid input. Disappears once the error is corrected. Critical errors may block form submission until resolved. In severe cases, use a `BannerMessage` in addition to the inline error.

---

## SwiftUI Code Examples

### Helper text (persistent)
```swift
import FioriSwiftUICore

TextFieldFormView(
    title: { Text("Invoice Number") },
    text: $invoiceNumber,
    placeholder: { Text("e.g. INV-2026-001") },
    helperText: { Text("Must start with INV- followed by year and sequence") }
)
// No icon; helper text always visible
```

### Error message (replaces helper text while invalid)
```swift
@State private var amount = ""
var amountError: String? {
    guard !amount.isEmpty else { return nil }
    return Double(amount) == nil ? "Enter a valid number" : nil
}

TextFieldFormView(
    title: { Text("Amount") },
    text: $amount,
    placeholder: { Text("0.00") },
    errorMessage: amountError.map { AttributedString($0) },
    helperText: amountError == nil ? { Text("Enter the invoice amount in USD") } : nil
)
// Helper text shows when valid; error message replaces it when invalid
// Once corrected, reverts to helper text automatically
```

### Warning message
```swift
var dueDateWarning: String? {
    guard let date = dueDate else { return nil }
    return Calendar.current.isDateInPast(date)
        ? "Due date is in the past"
        : nil
}

TextFieldFormView(
    title: { Text("Due Date") },
    text: $dueDateText,
    warningMessage: dueDateWarning.map { AttributedString($0) }
)
```

### Success message
```swift
var vatNumberFeedback: (message: String, isSuccess: Bool)? {
    guard vatNumber.count == 9 else { return nil }
    return isValidVAT(vatNumber)
        ? ("VAT number is valid", true)
        : ("VAT number not recognised", false)
}

TextFieldFormView(
    title: { Text("VAT Number") },
    text: $vatNumber,
    successMessage: vatNumberFeedback?.isSuccess == true
        ? AttributedString(vatNumberFeedback!.message) : nil,
    errorMessage: vatNumberFeedback?.isSuccess == false
        ? AttributedString(vatNumberFeedback!.message) : nil
)
```

### Critical error blocking submission
```swift
@State private var showErrors = false

var vendorError: String? {
    showErrors && vendor.isEmpty ? "Vendor name is required" : nil
}
var amountError: String? {
    showErrors && amount.isEmpty ? "Amount is required" : nil
}
var hasErrors: Bool { vendorError != nil || amountError != nil }

VStack {
    Form {
        TextFieldFormView(
            title: { Text("Vendor") },
            text: $vendor,
            errorMessage: vendorError.map { AttributedString($0) },
            helperText: vendorError == nil ? { Text("Enter the vendor name") } : nil
        )
        TextFieldFormView(
            title: { Text("Amount") },
            text: $amount,
            errorMessage: amountError.map { AttributedString($0) }
        )
    }

    FioriButton { _ in Text("Submit") }
        .fioriButtonStyle(FioriPrimaryButtonStyle())
        .frame(maxWidth: .infinity)
        .padding(16)
        .onTapGesture {
            showErrors = true
            if !hasErrors { submitForm() }
        }
}
```

### Inline error + page-level banner (critical errors)
```swift
// For critical errors, combine inline messages with a banner
if hasErrors && showErrors {
    BannerMessage {
        Text("Please correct the errors below before submitting.")
    } icon: {
        Image(systemName: "exclamationmark.triangle.fill")
            .foregroundStyle(Color.preferredColor(.negativeLabel))
    }
}

Form {
    TextFieldFormView(
        title: { Text("Vendor") },
        text: $vendor,
        errorMessage: vendorError.map { AttributedString($0) }
    )
}
```

---

## Figma Variants → SwiftUI

| Figma Property | Figma Value | SwiftUI parameter |
|---------------|-------------|-------------------|
| Variation | Helper text | `helperText: { Text(...) }` |
| Variation | Success | `successMessage: AttributedString(...)` |
| Variation | Warning | `warningMessage: AttributedString(...)` |
| Variation | Error | `errorMessage: AttributedString(...)` |
| Icon | None | Helper text (no icon by design) |
| Icon | ✓ green | Success — automatic |
| Icon | ⚠ yellow | Warning — automatic |
| Icon | ✕ red | Error — automatic |
| Persistence | Permanent | Helper text |
| Persistence | Temporary | Success, warning, error |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Always show helper text for fields that benefit from context
- Replace helper text with error/warning/success messages temporarily — revert back when resolved
- Keep messages to **1 line** (3 lines maximum)
- Block submission and show error messages when required fields are invalid
- Combine inline errors with a `BannerMessage` for critical multi-field errors

**Don't:**
- Add an icon to helper text — it intentionally has none
- Use inline validation as the only error signal for critical issues — add a banner when multiple required fields fail
- Write error messages that only state the problem without explaining how to fix it
- Truncate messages — use wrapping (up to 3 lines)

---

## Related Components

- [forms.md](forms.md) — form cells that inline validation is attached to
- [banner.md](banner.md) — page-level companion for critical errors
