# Spatial UX Design — SAP Fiori for visionOS

> SAP Fiori for visionOS | Foundation

## Application Types

Choose the appropriate level of immersion for your application:

| Type | Description | Effort |
|------|-------------|--------|
| **Emulated iPad app** | Runs as-is; little to no UI changes | Low — but test thoroughly |
| **2D Spatial app** (windows only) | Standard SwiftUI with spatial adjustments | Medium — iterative approach |
| **Immersive app** (volumes + immersive spaces) | Full spatial 3D experience | High |

---

## Immersive App Sub-Types

**Spatial with 2D & 3D (volumes):**
- Uses volumes alongside windows
- App can be displayed and used side by side with other apps
- 3D content mixed with standard 2D UI

**Fully immersive (immersive spaces):**
- Single dedicated full space
- Only the application's content appears
- User's physical environment replaced or blended

---

## Choosing the Right Type

### Emulated iPad App
Requires little to no UI adjustment. Validate carefully — especially if the app has:
- Custom UI behaviors
- APIs not fully supported on visionOS (e.g., camera view)

### 2D Spatial App
If built on SwiftUI with standard controls → transition should be straightforward.

**Recommended approach:**
1. Get the application running on visionOS
2. Identify areas that need spatial design adjustments
3. Iterate and refine

Apple's extensive visionOS guidelines and tutorials serve as the starting point.

### Immersive App
Requires full spatial design and development investment. Use when the experience fundamentally benefits from spatial computing — not just because the platform supports it.

---

## Resources

- [get-started.md](../get-started.md) — required reading before this article
- [Apple HIG: Designing for visionOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos)
- [Apple HIG: Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout)
