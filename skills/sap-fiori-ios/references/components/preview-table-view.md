# Preview Table View — Component Guidelines

> SAP Fiori for iOS | Category: Fiori SDK — Table View Cells
> Figma: `https://www.figma.com/community/file/1450853598524410675/sap-fiori-for-ios-ui-kit`
> Development reference: UIKit `FUIObjectTableViewCell`, SwiftUI `SectionHeader`, `SectionFooter`

## What is it?

A preview table view displays a preview (subset) of a full list, populated with object cells or contact cells. Multiple preview table views can be stacked on a single screen. Commonly found in overview and object screens.

**Lists in a preview table view cannot be filtered.** List actions must be avoided — it is a read-only preview.

---

## When to Use

- Provide a quick overview of different data sets on the same screen (stack multiple previews)
- Allow navigation to the full list via "See All"
- Common in overview and object detail screens

---

## Anatomy

```
A. Section Header: "Open Invoices"
──────────────────────────────────────────
B. Content Area (≤3 cells)
   [ Object Cell 1 ]
   [ Object Cell 2 ]
   [ Object Cell 3 ]
──────────────────────────────────────────
C. Footer: See All (12) ›
```

**A. Section Header** — group label describing the content. Optional.
**B. Content Area** — ≤3 cells recommended. Cells shown depend on default sort/filter of the full list.
**C. Footer** — "See All (N) ›" with total count. Entire footer is tappable → navigates to full list report. Optional.

---

## Behavior

- Tap a cell → navigates to the object's detail screen
- Tap "See All" footer → navigates to the full list report
- No filtering within the preview — filtering belongs in the full list

### Empty State
When content is user-generated, the preview may start empty.
- **Hide** the preview entirely, OR
- Show an empty state label explaining there is no content yet
- A quick action button cell can guide the user to add content

---

## SwiftUI Code Examples

### Standard preview table view
```swift
import FioriSwiftUICore

struct InvoicePreview: View {
    let invoices: [Invoice]
    let totalCount: Int

    var body: some View {
        VStack(spacing: 0) {
            // Section header
            SectionHeader(title: AttributedString("Open Invoices"))

            // Content — max 3 cells
            ForEach(invoices.prefix(3)) { invoice in
                ObjectItem {
                    Text(invoice.number)
                } subtitle: {
                    Text(invoice.vendor)
                } status: {
                    Text(invoice.status)
                        .foregroundStyle(Color.preferredColor(.secondaryLabel))
                }
                .onTapGesture { navigateToInvoice(invoice) }

                Divider().padding(.leading, 16)
            }

            // "See All" footer
            SectionFooter(
                title: AttributedString("See All (\(totalCount))"),
                action: { navigateToInvoiceList() }
            )
        }
        .background(Color.preferredColor(.secondaryGroupedBackground))
        .clipShape(RoundedRectangle(cornerRadius: 8))
    }
}
```

### Multiple stacked previews on overview screen
```swift
ScrollView {
    VStack(spacing: 16) {
        InvoicePreview(invoices: recentInvoices, totalCount: 42)
        OrderPreview(orders: openOrders, totalCount: 18)
        TaskPreview(tasks: myTasks, totalCount: 7)
    }
    .padding(16)
}
```

### Empty state
```swift
VStack(spacing: 0) {
    SectionHeader(title: AttributedString("Attachments"))

    if attachments.isEmpty {
        // Empty state — show guidance or hide entirely
        VStack(spacing: 8) {
            Text("No attachments yet")
                .font(.fiori(forTextStyle: .body))
                .foregroundStyle(Color.preferredColor(.secondaryLabel))

            FioriButton { _ in Text("Add Attachment") }
                .fioriButtonStyle(FioriTertiaryButtonStyle())
                .onTapGesture { showAttachmentPicker() }
        }
        .padding(24)
    } else {
        ForEach(attachments.prefix(3)) { attachment in
            AttachmentRow(attachment: attachment)
        }
        SectionFooter(title: AttributedString("See All (\(attachments.count))"),
                      action: navigateToAttachments)
    }
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Show ≤3 cells in the preview
- Always include the total count in the "See All" footer
- Navigate to full list on "See All" tap
- Navigate to object detail on cell tap
- Show an empty state or hide the view when no content exists

**Don't:**
- Filter within the preview — filtering belongs in the full list
- Include list actions (delete, edit) in preview cells
- Show more than 3 cells — direct users to the full list for more

---

## Related Components

- [object-cell.md](object-cell.md) — cells used inside the preview
- [contact-cell.md](contact-cell.md) — contact cells used inside the preview
- [illustrated-message.md](illustrated-message.md) — empty state
