# Adaptive Layout — Design Foundations

> SAP Fiori for iOS | Foundation
> Platforms: iPhone, iPad, Mac Catalyst, visionOS

## What is it?

SAP Fiori for iOS supports auto layout and adaptivity concepts that ensure a great user experience across all Apple devices and platforms. Layouts dynamically rearrange and resize in response to:
- Device orientation changes
- Different screen sizes (iPhone, iPad, Mac Catalyst)
- Stage Manager window resizing
- Multitasking (split view, slide over)

**Think in columns, not screens.** Static page types (object details, list reports) should be designed as column compositions that adapt to available space — rather than as fixed-size screens. SAP Fiori apps adapt their layout based on size class while staying recognizably consistent.

### Benefits of Adaptive Layout

| Benefit | How |
|---------|-----|
| **Streamlined navigation** | Menus and controls are accessible next to the workspace; intuitive gesture-based navigation |
| **Better data visualization** | Charts and spreadsheets are more readable and interactive on larger screens |
| **Efficient data entry** | Extra space for keyboards and form fields reduces scrolling and errors |
| **Document editing** | Full-page views, side-by-side comparisons, and stylus support on iPad |

---

## Layout Basics

### Horizontal Space

| Size class | Layout margin | Notes |
|-----------|--------------|-------|
| **Compact** | **16pt** | Full-width components; spacing between elements fixed or flexible per component |
| **Regular** | **20pt** | Generally larger internal spacing than compact |

**Regular width sub-classes:**
- **Readable width** — content constrained to a comfortable reading width (≤672pt) even though the screen is wider
- **Full-width regular** — content fills the available regular-width space

```swift
// Readable width constraint (regular)
.frame(maxWidth: 672)

// Full-width (compact and regular)
.frame(maxWidth: .infinity)
    .padding(.horizontal, horizontalSizeClass == .regular ? 20 : 16)
```

### Vertical Space

Three variants of vertical size class:

| Variant | When | Key behavior |
|---------|------|-------------|
| **Compact height** | iPhone landscape (select devices) | Reduced inner padding/spacing; more content visible |
| **Regular height — iPhone** | iPhone portrait (default) | Standard component heights |
| **Regular height — iPad** | iPad | Some components use extra height variants |

```swift
@Environment(\.verticalSizeClass) var vSizeClass

// Reduce padding in compact height (iPhone landscape)
.padding(.vertical, vSizeClass == .compact ? 4 : 12)
```

### Three Main Layout Regions

For seamless size class transitions and user orientation:

```
A. Navigation Bar  ← top
B. Body            ← main content area
C. Navigation      ← bottom (tab bar) or side (sidebar on iPad)
```

These three regions remain consistent across size classes, providing continuity as the layout adapts.

## Size Classes

iOS defines two main size classes — **regular** and **compact** — applied independently to horizontal and vertical space.

**Horizontal size class is generally more important than vertical** because vertical scrolling is common. Design primarily around horizontal size class.

| Device / Context | Horizontal | Vertical |
|-----------------|------------|---------|
| iPhone portrait | Compact | Regular |
| iPhone landscape (most models) | Compact | Compact |
| iPhone landscape (large models, e.g. Pro Max) | Regular | Compact |
| iPad full screen | Regular | Regular |
| iPad split 1/3 (most iPads) | Compact | Regular |
| iPad split 1/2 (most iPads) | Compact | Regular |
| iPad split 1/2 (12.9" / 13" iPad) | Regular | Regular |
| iPad split 2/3 | Regular | Regular |

**Key rules:**
- Size class is determined by device type, orientation, and multitasking state — **not by device model**
- Design with size classes, not specific devices — window space is dynamic (Stage Manager, split view, orientation)
- In compact width: one column only
- In regular width: two to three columns possible

```swift
@Environment(\.horizontalSizeClass) var hSizeClass
@Environment(\.verticalSizeClass) var vSizeClass

var body: some View {
    if hSizeClass == .compact {
        CompactLayout()
    } else {
        RegularLayout()
    }
}
```

---

## Multi-Column Layout

`NavigationSplitView` is the SwiftUI class for multi-column layouts. On large devices (iPad, Mac), columns appear side by side. On narrow screens (iPhone, slide over, Apple Watch), all columns collapse into a stack automatically.

Each column has its own navigation bar and optional toolbar. Changes in one column trigger content changes in subsequent columns.

> Use consistently — either two-column or three-column throughout your app. Don't mix.

### Two-Column Layout (sidebar + detail)

```swift
NavigationSplitView {
    // Column 1: Sidebar — navigation
    List(items, selection: $selectedItem) { item in
        Text(item.title)
    }
    .navigationTitle("Invoices")
} detail: {
    // Column 2: Detail — flexible width, fills remaining space
    if let item = selectedItem {
        InvoiceDetailView(item: item)
    } else {
        ContentUnavailableView("Select an invoice", systemImage: "doc.text")
    }
}
```

Sidebar can be hidden to show detail only:
```swift
NavigationSplitView(columnVisibility: $columnVisibility) { ... } detail: { ... }
// columnVisibility = .detailOnly hides sidebar
```

### Three-Column Layout (sidebar + content + detail)

```swift
NavigationSplitView(columnVisibility: $columnVisibility) {
    SideBar(...)        // Column 1: Sidebar — fixed width
} content: {
    InvoiceListView()   // Column 2: Content/list — fixed width
} detail: {
    InvoiceDetailView() // Column 3: Detail — flexible, fills remaining space
}
```

- Sidebar and content column have **fixed width**
- Detail column is **flexible** — fills remaining space
- Sidebar and content column can be hidden (detail only)
- On compact: all columns collapse to a stack (system-determined order)

### Fiori SideBar Component (SAP-specific)

```swift
SideBar(
    isEditing: $isEditing,
    queryString: $searchQuery,
    data: $navItems,
    selection: $selectedItem,
    title: AttributedString("My App"),
    isUsedInSplitView: true,
    destination: { item in DetailView(item: item) },
    item: { $item in SideBarItemRow(item: item) }
)
```

---

## Inspector (Auxiliary Column)

The SwiftUI inspector is a context-dependent auxiliary column showing properties or details about selected content. It can extend any layout — not just `NavigationSplitView`.

**Behavior:**
- Regular: appears as a **trailing column** next to the detail
- Split screen: displayed as an **overlay**
- Compact: adjusts to a **resizable sheet**
- Fixed width; detail column takes remaining space
- Content within the inspector can be scrolled

**Rules:**
- Show/hide via a navigation bar button
- Do **not** add push navigation inside the inspector — it should be the final information layer

```swift
someView
    .inspector(isPresented: $showInspector) {
        InspectorContent()
            .inspectorColumnWidth(min: 200, ideal: 300, max: 400)
    }
```

**With two-column layout:** inspector appears as a trailing fourth column; detail column width adjusts automatically.

**With three-column layout:** opening the inspector hides the sidebar to make room.

---

## Adaptive Apps

### Information Architecture

Start by mapping the app's compact flow (hierarchical navigation), then adapt it for regular (multi-column). The goal is **fewer levels** in regular size class by merging related screens into columns.

**Process:**
1. Map current compact information architecture
2. Identify list+detail screen pairs — merge into one multi-column screen for regular
3. Determine presentation modifiers for each use case (see Usage Patterns below)
4. Convert navigation (tab bar → sidebar/adaptable)

### Navigation Conversion

| Navigation type | Compact | Regular |
|----------------|---------|---------|
| Few primary destinations | Tab bar | Tab bar |
| Hierarchical / deep navigation | Tab bar | Sidebar (flattens hierarchy) |
| iOS 18+ adaptable | Tab bar | User can switch to sidebar |

**iOS 18 `.sidebarAdaptable` behavior by platform:**
- iOS 18 → tab bar at bottom
- iPadOS 18 → tab bar convertible to sidebar by user
- macOS 15 / tvOS 18 → sidebar
- visionOS 2 → ornament + sidebar for secondary tabs

```swift
// iOS 18+ — adaptable tab/sidebar
TabView {
    Tab("Overview", systemImage: "square.grid.2x2") { OverviewView() }
    Tab("Orders", systemImage: "cart") { OrdersView() }
    Tab("Assets", systemImage: "gearshape") { AssetsView() }
}
.tabViewStyle(.sidebarAdaptable)
```

**Sidebar secondary destinations:** place under collapsible section headers. Tab bar shows only primary destinations; secondary destinations navigate full-screen.

### Reducing Navigation Hierarchies (Regular)

| Technique | How it reduces hierarchy |
|-----------|------------------------|
| **Presentation modifiers** | Modal in compact → popover/inspector in regular (removes one push level) |
| **Sidebar groups** | Tab + list in compact → sidebar group in regular (list screen no longer needed) |
| **Card carousel** | Extra list in compact → wider carousel shows more cards in regular |
| **List detail** | Separate list + detail screens → single `NavigationSplitView` screen |

### Component Substitutions (Regular vs. Compact)

| Instead of (compact) | Use in regular |
|---------------------|----------------|
| Preview table view | Multi-column collection view (2 columns) |
| List | Data table or cards (masonry layout) |
| Flat list for deep data | Hierarchy view |

Users must be able to access the same information on both size classes. Use progressive disclosure for compact views.

### Multi-Window (iPad)

Apps should support multiple windows and multitasking when useful. Don't require multiple windows, but support them.

**Use cases:**
- Drag list item to new window → list and details side by side
- Open two detail views to compare objects
- Create new object while keeping existing object open for reference
- Drag work items to create a to-do window per item
- Drag attachments between apps (photo, PDF, custom object)

---

## Usage Patterns

Recommended presentation types per use case and size class:

| Use case | Compact | Regular |
|---------|---------|---------|
| **Data entry** (forms, create/edit) | Modal form sheet (large detent) or full-screen modal | Modal form sheet or modal page sheet |
| **Searching & browsing** | Full-screen list | Full-screen list (global) or list detail (local) |
| **Task execution** | Full-screen list | List detail or split view |
| **Approval & review** | Full-screen list | List detail |
| **Filtering & sorting** | Modal form sheet (large detent) | Popover (or modal sheet for complex filters) |
| **Attachments & notes** | Modal sheet | Modal sheet |
| **Settings & preferences** | Full-screen list or full-screen modal | Modal page sheet |
| **Comparison** | Scrollable list with segmented control toggle | Multi-column (2 columns) |
| **Step-by-step flow** | Modal form sheet (large detent) or full-screen modal | Multi-column: steps list + form + optional inspector |

### Data Entry detail
- Compact full-screen modal supports push navigation within the modal for nested pages
- Regular modal page sheet keeps focus while maintaining background context

### Filtering detail
- Compact: full-screen sheet keeps users focused on filter options
- Regular: popover for lightweight access; use modal sheet only when filters are very complex

### Step-by-step detail (Regular)
- Left column: vertical step list (step navigation)
- Middle column: main form/task for selected step
- Inspector (right column): step guidance or completion checklist

---

## Adaptive Grid

```swift
// Adapts column count to available width
LazyVGrid(columns: [GridItem(.adaptive(minimum: 160, maximum: 320))]) {
    ForEach(items) { item in
        CardView(item: item)
    }
}
```

---

## Safe Areas

Never ignore safe areas. Fiori content should stay within them:

```swift
// ✅ Correct — content respects safe area
ScrollView { content }

// ✅ Background extends under safe area
Color.preferredColor(.primaryBackground)
    .ignoresSafeArea()  // only for background fills

// ❌ Wrong — interactive content in unsafe area
VStack { content }
    .ignoresSafeArea()  // clips content on notched devices
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Think in columns, not screens — design for column compositions
- Use `NavigationSplitView` for all iPad list/detail layouts
- Use `.sidebarAdaptable` on iOS 18+ for nav that scales across devices
- Test at 1/3 split view width on iPad — the narrowest regular layout
- Use `ContentUnavailableView` for empty detail states
- Support multi-window on iPad whenever the content benefits from it

**Don't:**
- Use `NavigationStack` alone on iPad — it won't use the screen width
- Mix two-column and three-column `NavigationSplitView` in the same app (use custom solution instead)
- Add push navigation inside an inspector
- Ignore compact size class — the same app runs on iPhone and iPad split view
- Require multiple windows — support them, but don't depend on them
