# Object Details Page — Page Type Guide

> SAP Fiori for iOS | Page Types
> Development reference: `FUIObjectFloorplan`

## What is it?

The object details page shows all attributes of a single business object. It includes a header area, content area, and optional action area. Users can drill down into specific attributes from here.

Accessed from: overview page, list report, or a related business object.

---

## Anatomy

```
A. Header
   ObjectHeader / ProfileHeader
   (most important info — captures attention first)

B. Contextual Content
   Supplemental info giving comprehensive context

C. Instructional Content
   Helps user complete the current task efficiently
   (prioritized for the current scenario)

D. Referential Content
   Relevant but not always essential info
   (arranged by frequency of use)

E. Facets (low-frequency content)
   Drill-down links at bottom of screen

[Optional Toolbar with actions]
```

---

## Content Priority

Placement is based on priority and frequency relative to the user's task. This is a **suggestion** — sections can move up if they fulfill the priority or frequency rule for a specific business scenario.

| Section | Purpose | Placement |
|---------|---------|-----------|
| A. Header | Identity + key info | Top — always first |
| B. Contextual | Full context for the task | Below header |
| C. Instructional | Task completion help | Middle |
| D. Referential | Adjacent supporting info | Lower |
| E. Facets | Low-frequency drilldowns | Bottom |

**Facets rule:** Avoid excessively long screens. Put low-frequency content in facets at the bottom — users drill down to access it.

---

## Actions

- Common nav bar actions: Add, Edit, Share, Save
- Toolbar: additional actions when tab bar is not present
- **Edit** → opens a modal with form cells for editing

---

## Object Types

### Standard Object (most common)
Uses `ObjectHeader`. Examples: work orders, tasks, issues, parts.

### Profile
Uses `ProfileHeader`. For person/user profile objects.

### Child Object
Shows details of one attribute of a parent object. Usually the **last screen** in a workflow — no further drill-down. Can include actions and modal views.

Child objects at the same level → use **Sibling Navigation** pattern.

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct InvoiceDetailView: View {
    let invoice: Invoice

    var body: some View {
        ScrollView {
            VStack(spacing: 0) {

                // A. Header
                ObjectHeader {
                    Text(invoice.number)
                        .font(.fiori(forTextStyle: .title1))
                } subtitle: {
                    Text(invoice.vendor)
                        .foregroundStyle(Color.preferredColor(.secondaryLabel))
                } tags: {
                    Tag(invoice.status)
                } detailContent: {
                    Text(invoice.formattedAmount)
                        .font(.fiori(forTextStyle: .KPI, weight: .light))
                }

                Divider()

                // B. Contextual content
                VStack(alignment: .leading, spacing: 0) {
                    SectionHeader(title: AttributedString("Details"))
                    KeyValueItem(key: { Text("Vendor") }, value: { Text(invoice.vendor) })
                    KeyValueItem(key: { Text("Due Date") }, value: { Text(invoice.dueDate) })
                    KeyValueItem(key: { Text("Payment Terms") }, value: { Text(invoice.paymentTerms) })
                }

                // C. Instructional content
                VStack(alignment: .leading, spacing: 0) {
                    SectionHeader(title: AttributedString("Required Actions"))
                    // Task-specific items
                }

                // D. Referential content
                VStack(alignment: .leading, spacing: 0) {
                    SectionHeader(title: AttributedString("Related Documents"))
                    // Less critical but accessible
                }

                // E. Facets — low frequency, always at bottom
                VStack(alignment: .leading, spacing: 0) {
                    SectionHeader(title: AttributedString("More"))
                    NavigationLink("History") { InvoiceHistoryView(invoice: invoice) }
                        .padding(16)
                    NavigationLink("Attachments (\(invoice.attachmentCount))") {
                        AttachmentListView(invoice: invoice)
                    }
                    .padding(16)
                }
            }
        }
        .navigationTitle(invoice.number)
        .navigationBarTitleDisplayMode(.inline)
        .toolbar {
            ToolbarItemGroup(placement: .primaryAction) {
                FioriButton { _ in Image(systemName: "square.and.arrow.up").accessibilityLabel("Share") }
                    .fioriButtonStyle(FioriTertiaryButtonStyle())
                FioriButton { _ in Text("Edit") }
                    .fioriButtonStyle(FioriTertiaryButtonStyle())
                    .onTapGesture { showEdit = true }
            }
        }
        .sheet(isPresented: $showEdit) {
            EditInvoiceView(invoice: invoice)  // modal with form cells
        }
    }
}
```

---

## Navigational Structure

```
Overview Page  →  List Report  →  Object Details  →  Child Object
                                        ↓
                                   Edit Modal
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use ObjectHeader for standard objects; ProfileHeader for people
- Put low-frequency content in facets at the bottom
- Open Edit as a modal (not a push navigation)
- Use Sibling Navigation for child objects at the same level

**Don't:**
- Put all content inline — use facets for low-frequency info to avoid excessive scrolling
- Push to an edit screen — use a modal instead

---

## Related Components / Patterns

- [../components/object-header.md](../components/object-header.md)
- [../components/profile-header.md](../components/profile-header.md)
- [../components/sibling-navigation.md](../components/sibling-navigation.md)
- [../patterns/hierarchy.md](../patterns/hierarchy.md)
