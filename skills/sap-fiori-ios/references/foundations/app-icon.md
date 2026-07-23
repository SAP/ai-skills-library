# App Icon — Design Foundations

> SAP Fiori for iOS | Foundation

## What is it?

The app icon communicates the purpose of the SAP mobile app and supports users in recognizing it in the App Store and on their home screens. The design direction complements the Horizon visual design and creates a recognizable mobile brand.

---

## Appearance Modes

Maintain consistent core visual features across all system appearances. Do not create custom variants that change elements between modes — this makes the app harder to find when users switch appearances.

| Mode | Guidance |
|------|---------|
| Default | Full color palette |
| Dark | Same palette, but more subdued |
| Clear (light/dark) | Even more subtle — harmonizes with system tone |
| Tinted (light/dark) | Subtle — adapts to system accent color |

---

## App Naming Convention

| Name type | Max length | Rules |
|-----------|-----------|-------|
| **General App Name** (App Store) | 30 characters | No "mobile" or "app" in the title |
| **Short Name** (home screen) | 12 characters | No "SAP" prefix |

Use the SAP Naming Center for official name requests and approvals.

---

## Anatomy (Three-Layer Architecture)

| Layer | Role |
|-------|------|
| Database Layer | Base shape |
| Logic Layer | Second layer |
| UI Layer | Third/top layer |
| Highlight Layer | Optional fourth layer |

---

## Icon Composer (Xcode 26+)

Apple's Icon Composer (integrated with Xcode 26) creates layered `.icon` files with the Liquid Glass effect. Import it via **Edit → Save** for handoff to development.

### Template Setup

**Background:**
- Fill: Gradient
- Color 1: `#FFFFFF`
- Color 2: `#EAECF0`
- Background auto-adjusts for dark and transparent variants

### Layer Styling Reference

| Layer | Gradient Color 1 | Gradient Color 2 | Specular | Blur | Translucency |
|-------|-----------------|-----------------|---------|------|-------------|
| First (Database) | `#0057D2` | `#002A86` | On | Off | Off |
| Second (Logic) | `#1B90FF` | `#0057D2` | On | Off | Off |
| Third (UI) | `#4DB1FF` | `#1B90FF` | On | Off | Off |
| Highlight | `#FFFFFF` (solid) | — | On | On 20% | On 50% |

All layers: Opacity 100%, Blend Mode Normal, Mode Individual, Shadow Neutral 50%.

### Review Checklist

- [ ] View against dark backgrounds — visibility and contrast
- [ ] Preview monochrome version
- [ ] Check tinted color options in Icon Composer
- [ ] Export as `.icon` for development
- [ ] Export PNG for marketing/documentation if needed

---

## Do's ✓ / Don'ts ✗

**Do:**
- Use an SAP Fiori icon as the metaphor base
- Keep the same color palette across all appearance modes (adjust subtlety, not palette)
- Keep app name ≤30 characters; short name ≤12 characters and without "SAP"

**Don't:**
- Use "mobile" or "app" in the App Store name
- Use "SAP" in the home screen short name
- Create icon variants that change visual elements between appearance modes
