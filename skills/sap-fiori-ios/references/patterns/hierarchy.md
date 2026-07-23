# Hierarchy Pattern — Pattern Guide

> SAP Fiori for iOS | Patterns
> Development reference: UIKit `FUIHierarchyView`, `FUIHierarchyViewController`, `FUIListPickerFormCell`, `FUIListFloorplan`

## What is it?

The hierarchy pattern combines a **list report** with a **hierarchy view** to enable navigation and interaction with hierarchically structured data. It supports workflows like creating objects within a hierarchy, or browsing parent/child object relationships.

---

## Anatomy

### List Report (first screen)
Standard list report with an added **hierarchy accessory** on each row. Supports:
- Search
- Filter
- Create

### Hierarchy View (second screen)
Displays the selected object with its parent and/or child objects expanded in a column-based layout. See [hierarchy-view.md](../components/hierarchy-view.md) for full component guidance.

---

## Behavior

### Single Selection (create use case)
A list picker with single selection can be embedded in the hierarchy pattern. Used when creating a new object and the user needs to identify where it lives within a group or location.

### Modal with Breadcrumb (adaptive)
When using the hierarchy pattern inside a modal (form sheet), use the hierarchy view with a **breadcrumb** to show the user's current position in the hierarchy.

---

## SwiftUI Code Example

```swift
import FioriSwiftUICore

// List report with hierarchy accessory
NavigationStack {
    List(hierarchyItems, selection: $selectedItem) { item in
        HStack {
            ObjectItem {
                Text(item.name)
            } subtitle: {
                Text(item.type)
            }
            Spacer()
            // Hierarchy accessory — navigates to hierarchy view
            if item.hasChildren {
                Image(systemName: "list.bullet.indent")
                    .foregroundStyle(Color.preferredColor(.tintColor))
                    .onTapGesture { navigateToHierarchy(item) }
            }
        }
    }
    .navigationTitle("Cost Centers")
    .searchable(text: $searchQuery)
    .toolbar {
        ToolbarItem(placement: .primaryAction) {
            FioriButton { _ in Image(systemName: "plus").accessibilityLabel("Create") }
                .fioriButtonStyle(FioriTertiaryButtonStyle())
                .onTapGesture { showCreate = true }
        }
    }
}

// Hierarchy view (second screen)
NavigationLink(destination:
    HierarchyView(
        data: $hierarchyData,
        expandedItems: $expandedItems
    ) { node in
        HierarchyItemView {
            Text(node.name)
        } subtitle: {
            Text(node.code)
        }
    }
) {
    Text("View Hierarchy")
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use the hierarchy accessory in list reports to indicate navigable hierarchy
- Add breadcrumbs when the hierarchy view is presented in a modal
- Use single-selection list picker for create workflows that need hierarchy location

**Don't:**
- Use for single-level data — use a standard list report instead
- Navigate more than 3 levels deep without breadcrumb context

---

## Related Components / Patterns

- [../components/hierarchy-view.md](../components/hierarchy-view.md)
- [list-report.md](list-report.md)
