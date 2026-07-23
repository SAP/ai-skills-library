# Search — Pattern Guide

> SAP Fiori for iOS | Patterns
> Development reference: UIKit `FUISearchBar`
> See also: [../components/search-bar.md](../components/search-bar.md), [../components/search-to-select.md](../components/search-to-select.md)

## What is it?

The search pattern locates information or objects within a large collection. Built on the `SearchBar` component with additional states and behaviors for a complete search experience.

---

## States and Variations

### Loading State
After the user types a query, skeleton loading appears while results are fetching.

```swift
if isSearching {
    ForEach(0..<5, id: \.self) { _ in
        SkeletonObjectCell()
    }
} else {
    ForEach(searchResults) { result in
        ObjectItem { Text(result.title) }
    }
}
```

### Empty State
Displayed when no matching results are found.

```swift
if searchResults.isEmpty && !searchQuery.isEmpty {
    ContentUnavailableView.search(text: searchQuery)
    // or
    IllustratedMessage {
        Image(systemName: "magnifyingglass")
            .font(.system(size: 48))
            .foregroundStyle(Color.preferredColor(.tertiaryLabel))
    } title: {
        Text("No results for \"\(searchQuery)\"")
    } description: {
        Text("Try a different search term.")
    }
}
```

### Recent Searches
Display previous search history when the search field becomes active (before typing).

```swift
.searchable(text: $searchQuery, prompt: "Search invoices") {
    if searchQuery.isEmpty {
        Section("Recent") {
            ForEach(recentSearches, id: \.self) { recent in
                Text(recent).searchCompletion(recent)
            }
        }
    }
}
```

### Search Suggestions with Bolded Exact Match
As the user types, show matching suggestions with the query term bolded.

```swift
.searchSuggestions {
    ForEach(suggestions(for: searchQuery)) { suggestion in
        // Bold the matched portion
        Text(suggestion.attributedTitle(matching: searchQuery))
            .searchCompletion(suggestion.value)
    }
}
```

### Search with Quick Filter Bar
Search combined with filter feedback bar for refined results.

```swift
VStack(spacing: 0) {
    // Filter feedback bar below search bar
    FilterFeedbackBar(items: $filterItems) { item in
        toggleFilter(item)
    }
    Divider()
    List(filteredAndSearchedResults) { result in
        ObjectItem { Text(result.title) }
    }
}
.searchable(text: $searchQuery, placement: .navigationBarDrawer(displayMode: .always))
```

### Search to Select
Multi-value selection while searching. See [../components/search-to-select.md](../components/search-to-select.md).

---

## Full Search Pattern

```swift
NavigationStack {
    List {
        if isLoading {
            // Skeleton loading while results fetch
            ForEach(0..<8, id: \.self) { _ in
                SkeletonObjectCell().listRowSeparator(.hidden)
            }
        } else if searchResults.isEmpty && !searchQuery.isEmpty {
            // Empty state
            ContentUnavailableView.search(text: searchQuery)
        } else {
            ForEach(searchResults) { result in
                ObjectItem { Text(result.title) }
                    .subtitle: { Text(result.subtitle) }
            }
        }
    }
    .navigationTitle("Invoices")
    .searchable(
        text: $searchQuery,
        placement: .navigationBarDrawer(displayMode: .always),
        prompt: "Search invoices"
    ) {
        // Recent searches (shown before typing)
        if searchQuery.isEmpty {
            ForEach(recentSearches, id: \.self) { recent in
                Label(recent, systemImage: "clock")
                    .searchCompletion(recent)
            }
        }
    }
    .onChange(of: searchQuery) { performSearch() }
}
```

---

## Do's ✓ / Don'ts ✗

**Do:**
- Show skeleton loading while results are fetching (not a spinner)
- Show a clear empty state with a helpful message
- Display recent searches before the user starts typing
- Bold the exact match portion in search suggestions
- Combine with filter feedback bar for complex datasets

**Don't:**
- Leave the list blank during loading — always show skeleton or results
- Show an empty state for the pre-search state (before any query is entered)

---

## Related Components / Patterns

- [../components/search-bar.md](../components/search-bar.md)
- [../components/search-to-select.md](../components/search-to-select.md)
- [../components/filter-feedback-bar.md](../components/filter-feedback-bar.md)
- [sort-and-filter-overview.md](sort-and-filter-overview.md)
