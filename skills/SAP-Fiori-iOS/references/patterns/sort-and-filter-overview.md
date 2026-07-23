# Sort & Filter Overview — Pattern Guide

> SAP Fiori for iOS | Patterns
> Development reference: Create and Filter Patterns SDK

## What is it?

The sort and filter pattern narrows down results from a dataset by setting sort and filter criteria. Three distinct approaches exist — choose based on complexity and context.

---

## Three Approaches

### Sort & Filter Form
For **advanced, complex filtering** with many options. Opens as a full-screen modal (compact) or popover (regular).

**Use when:**
- Large, complex filter sets with many options
- Large amount of data requiring advanced filtering

**Don't use when:**
- User needs to see results update immediately (use Filter Feedback Bar instead)

→ See [sort-and-filter-form.md](sort-and-filter-form.md)

### Filter Feedback Bar
For **contextual, on-screen filtering** that shows results updating in real time.

**Use when:**
- Frequently used filter options
- Users need to interact with already-applied filters
- Immediate visual feedback to filter changes is important

**Don't use when:**
- Many complex filters need to be applied (use Sort & Filter Form instead)

→ See [../components/filter-feedback-bar.md](../components/filter-feedback-bar.md)

### Quick Sort
For **contextual on-screen sorting only** — no filtering. Available as a menu (direct) or submenu (within overflow menu). Works at component level (cards, preview tables) or full-screen (list reports).

**Use when:**
- Only sorting is needed (no filtering)
- Fast, contextual sort change

**Don't use when:**
- Filtering is also required

→ See [quick-sort.md](quick-sort.md)

---

## Decision Table

| Need | Use |
|------|-----|
| Complex filters, large dataset | Sort & Filter Form |
| Live filter feedback, frequent filters | Filter Feedback Bar |
| Sort only, fast access | Quick Sort |
| Sort + filter together | Sort & Filter Form |

---

## Related Patterns

- [sort-and-filter-form.md](sort-and-filter-form.md)
- [quick-sort.md](quick-sort.md)
- [../components/filter-feedback-bar.md](../components/filter-feedback-bar.md)
