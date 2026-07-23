# Map Pattern — Pattern Guide

> SAP Fiori for iOS | Patterns
> Development reference: Map View SDK

## What is it?

The map pattern displays the location of business objects with visual markers (points, polylines, polygons), supports search, routing, and object detail panels. Used for geospatial and location-based workflows.

---

## Features

- Geospatial and business data from the field
- Search for business objects
- Overview of object locations
- Preview business objects via detail panel
- Directions to objects from current location
- Show/hide map view and feature layers

---

## Anatomy

### A. Map Search (optional)
Two search panel types:
- With object list (items as object cells, filterable)
- Search bar only

### B. Toolbar (top-right, up to 6 actions)
Five default actions:
| Action | Description |
|--------|-------------|
| Map Settings | Opens modal with view options, feature layers, near-me radius, unit measure |
| Current Position | Shows real-time GPS location; two states: On / Off |
| Show/Hide Panels | Toggles all panels off/on |
| Map Legend | Shows symbol/color explanation |
| Zoom Extents | Resets zoom to show all markers |

### C. Map Markers
| Type | Use for |
|------|---------|
| Points | Single or multiple objects at a location; can show icons, images, numbers, letters |
| Polylines | Linear assets (pipelines, networks) |
| Polygons | Areas (functional locations, regional boundaries) |

**Clustering:** Objects close together merge as zoom decreases. A cluster marker shows the count. Tap cluster → list panel of objects. Same-type clusters use the type color; mixed-type clusters use neutral color.

### D. Detail Panel
Slides in when a marker is tapped. Contains:
- **Title** (tint color if drill-down available) + optional subtitle
- Additional information (short texts, status icons, tags)
- Directions button (with/without address)
- Actions cell (quick actions)

---

## Behavior

### Edit Existing Object
Triggered from the actions cell in the detail panel. Edit mode in place, preserving filters/settings. Save → returns to previous map view.

### Create New Object
Triggered by "Add" icon in nav bar. User selects type (point/polyline/polygon) → taps to place points → drag to reposition or use address field → save → returns to map view.

> Edit mode is only available in **regular width**.

### Map Routes
Routes show multiple stop sites with call-out tags. Select a route → detail panel lists stops → select a stop → zoom in + detail for that stop.

---

## Adaptive Design

| Feature | Compact | Regular |
|---------|---------|---------|
| Map Settings | Full-screen modal | Modal window |
| Map Legend | Bottom of screen (landscape: top-left) | Popover anchored to toolbar |
| Detail Panel | Slides up from bottom | Slides in from left, floats |
| Edit mode | Not available | Available |

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use tint color for object titles in the detail panel when drill-down is available
- Use neutral color for mixed-type clusters
- Provide search with object cell list for filterable results

**Don't:**
- Exceed 6 toolbar actions
- Use edit mode on compact — regular width only

---

## Related Components

- [../components/object-cell.md](../components/object-cell.md)
- [../components/filter-feedback-bar.md](../components/filter-feedback-bar.md)
- [../components/search-bar.md](../components/search-bar.md)
