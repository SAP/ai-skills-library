# Design Principles — SAP Fiori for visionOS

> SAP Fiori for visionOS | Foundation

## What is it?

visionOS delivers spatial computing experiences blending virtual elements with the real world. Users control the degree of blending (except fully immersive apps where VR takes precedence).

---

## User Interaction

Primary input: **gaze (eye tracking)** + **spatial input (hand/finger tracking)**

### Key Recommendations

- **Define activity regions carefully** — avoid overlap; include sufficient padding so eye tracking can reliably detect user intent
- **Test custom UI activity regions early** — avoid major rework later
- **Dense layouts** → consider onboarding guidance with Apple's TipKit for hand gestures
- **Accessibility** — visionOS offers robust features that augment or replace default gaze/spatial input; test and optimize custom layouts
- **Mouse and keyboard** — supported like iPadOS/macOS; consider desk usage scenarios for data entry
- **Spatial audio** — crucial for spatial and immersive apps; mandatory in immersive experiences to provide coherent UX matching physical appearance of objects

---

## Adaptive Design

2D spatial apps require adaptive/responsive UI — the surface scales smoothly on x and y axes.

- Programmatically limit minimum and maximum length for each axis
- Consider minimum dimensions for complex data grids
- See [../foundations/adaptive-layout.md](../../../foundations/adaptive-layout.md)

### Additional visionOS-Specific Guidance

- **Single-pane experience** — apps can work without hierarchical navigation (like Mail/Notes), simplifying UI and enabling multitasking
- **Tab bar** — suitable for simple information architecture with distinct categories
- **Sidebar** — default navigation for multi-object apps; flattens hierarchies, enables quick context switching
- **Ornaments** — unique visionOS control; **never use for navigation**
- **Avoid auto-resizing/repositioning windows** — takes control from the user; disorienting in 3D space

---

## Application Window Management

**Default: single-window** (like iPad) — simpler development, more user-friendly.

**Multi-window justified when:**
- Users "extract" specific objects to pin nearby (info cards, charts)
- A second window shows a repository view while main window shows a personalized subset
- Tool palettes: attaching action panes to declutter the main content area

---

## Designing for Spatial UI (Figma)

- **Z-axis** — define z-axis offsets for custom elements (toolbars, ornaments, tab bars have specific z offsets for 3D layering)
- **No light/dark mode** — visionOS uses glass materials that reflect environment lighting; UI auto-adapts to luminance behind it
- **Background images in mockups** — use a muted office/living room image when sharing specs to show glass material effect
- **Developer mode in Figma** — simplifies specs; reduces manual 3D coach mark positioning

---

## Related

- [spatial-ux-design.md](spatial-ux-design.md)
- [terminology.md](terminology.md)
- [design-process-and-tools.md](design-process-and-tools.md)
