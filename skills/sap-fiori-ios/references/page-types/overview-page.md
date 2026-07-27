# Overview Page — Page Type Guide

> SAP Fiori for iOS | Page Types
> Development reference: `sap.f.SemanticPage`, `FUITableViewHeaderFooterView`, Overview Pattern SDK

## What is it?

The overview page is a hub that provides previews of information from different parts of the app. It highlights data the user needs to track and provides quick access to items relevant to day-to-day work.

Use the overview page to surface information that matters to the user — not a complete list of all app objects.

---

## Anatomy

```
A. KPI Header / Exceptions
   [$1.4M] [18 Open] [3 Overdue]   ← tap → filtered list
   (max 4 in regular, 3 in compact; page controls for overflow)

B. Preview Sections (contextually relevant)
   "Recent Customers"
   [ Object Cell 1 ]
   [ Object Cell 2 ]
   [ Object Cell 3 ]
   See All (24) ›

   "Open Invoices"
   [ Object Cell 1 ]
   ...

C. Facets (always at bottom)
   All Objects ›
   Products ›
   Equipment ›
   ...
```

**A. KPI Header / Exceptions** — key metrics or exceptions (urgent items, performance indicators). Tapping a number navigates to a filtered list. KPIs that don't need to always be visible do **not** stick on scroll — they scroll away to make room for content.

**B. Preview Sections** — quick access to contextually relevant objects (e.g. recent customers, not all customers). Uses Preview Table View pattern. Always contextually scoped to user's needs.

**C. Facets** — always at the bottom; entry point to every object type in the app. Less-frequently-used object types live here rather than as preview sections. Replaces the hamburger menu pattern.

---

## Navigation Bar

Actions in the overview page navigation bar have **global scope** — e.g. app-wide search, user settings. Not object-specific actions.

---

## Navigational Structure

### Hierarchical Navigation (most common)
The overview page is the **root** of hierarchical navigation — the entry point from which users drill down. Most natural fit.

### Flat Navigation (tab bar)
Can be used as one tab among several. Ensure content is **not simply duplicated** from other tabs — the overview must add unique value.

---

## Facets vs. Preview Sections

| Content type | Use |
|-------------|-----|
| Frequently accessed objects | Preview Table View section (B) |
| Less frequently accessed objects | Facets section (C) |
| Never use | Hamburger menu — use facets instead |

---

## KPI Header Rules

- Regular width: max **4 KPIs**
- Compact width: max **3 KPIs**; use page controls if more are needed
- KPIs that track progress (not urgent items) should **scroll off** — don't stick to top

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

struct OverviewPageView: View {
    @Environment(\.horizontalSizeClass) var hSizeClass

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 0) {

                    // A. KPI Header — scrolls away (non-sticky)
                    KPIHeader {
                        KPIItem(
                            kpiCaption: AttributedString("Revenue"),
                            items: [.init(value: AttributedString("$1.4M"))],
                            proposedViewSize: .large
                        )
                        .onTapGesture { navigateToFilteredRevenue() }

                        KPIItem(
                            kpiCaption: AttributedString("Open Orders"),
                            items: [.init(value: AttributedString("18"))],
                            proposedViewSize: .large
                        )
                        .onTapGesture { navigateToOpenOrders() }

                        KPIItem(
                            kpiCaption: AttributedString("Overdue"),
                            items: [.init(value: AttributedString("3"))],
                            proposedViewSize: .large
                        )
                        .foregroundStyle(Color.preferredColor(.negativeLabel))
                        .onTapGesture { navigateToOverdue() }
                    }
                    .padding(.bottom, 16)

                    // B. Contextual preview sections
                    VStack(spacing: 16) {
                        // Recent customers — contextually scoped
                        PreviewTableSection(
                            title: "Recent Customers",
                            items: recentCustomers,
                            totalCount: allCustomersCount
                        ) { customer in
                            ObjectItem { Text(customer.name) }
                                .subtitle: { Text(customer.id) }
                                .onTapGesture { navigateToCustomer(customer) }
                        } onSeeAll: {
                            navigateToCustomerList()
                        }

                        // Open invoices
                        PreviewTableSection(
                            title: "Open Invoices",
                            items: openInvoices,
                            totalCount: allInvoicesCount
                        ) { invoice in
                            ObjectItem { Text(invoice.number) }
                                .subtitle: { Text(invoice.vendor) }
                        } onSeeAll: {
                            navigateToInvoiceList()
                        }
                    }
                    .padding(.horizontal, 16)

                    // C. Facets — always at bottom
                    VStack(alignment: .leading, spacing: 0) {
                        Text("All Objects")
                            .font(.fiori(forTextStyle: .headline))
                            .padding(.horizontal, 16)
                            .padding(.vertical, 12)

                        ForEach(facetItems) { facet in
                            NavigationLink(destination: facet.destination) {
                                HStack {
                                    Text(facet.title)
                                        .font(.fiori(forTextStyle: .body))
                                        .foregroundStyle(Color.preferredColor(.primaryLabel))
                                    Spacer()
                                    Image(systemName: "chevron.forward")
                                        .foregroundStyle(Color.preferredColor(.tertiaryLabel))
                                }
                                .padding(.horizontal, 16)
                                .padding(.vertical, 12)
                            }
                            Divider().padding(.leading, 16)
                        }
                    }
                    .padding(.top, 16)
                }
            }
            .navigationTitle("Overview")
            .toolbar {
                // Global actions only
                ToolbarItem(placement: .primaryAction) {
                    FioriButton { _ in
                        Image(systemName: "person.circle")
                            .accessibilityLabel("Profile and Settings")
                    }
                    .fioriButtonStyle(FioriTertiaryButtonStyle())
                }
            }
            .searchable(text: $searchQuery, prompt: "Search all")  // global search
        }
    }
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Surface only contextually relevant preview sections (recent, open, urgent)
- Place facets at the bottom — it's the entry to the complete object catalog
- Keep nav bar actions global in scope
- Let performance KPIs scroll off screen — don't sticky them
- Use page controls on compact when more than 3 KPIs are needed

**Don't:**
- Show all objects in preview sections — show only the relevant subset
- Duplicate content already visible in other tabs (flat nav)
- Use a hamburger menu — use the facets section instead
- Make KPIs sticky unless they represent urgent items that must always be visible

---

## Related Components / Patterns

- [../components/kpi-header.md](../components/kpi-header.md)
- [../components/preview-table-view.md](../components/preview-table-view.md)
- [../components/collection-view.md](../components/collection-view.md)
