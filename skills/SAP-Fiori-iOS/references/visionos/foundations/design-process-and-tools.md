# Design Process and Tools — SAP Fiori for visionOS

> SAP Fiori for visionOS | Foundation

## 2D Spatial Applications

The design process mirrors traditional 2D apps (iPadOS, macOS) with visionOS-specific enhancements.

### Design Scope

Start with validated requirements and information architecture regardless of platform. Key visionOS-specific enhancements to plan for:

**Infinite Canvas**
Users can resize the application window in their space. Adaptive design is essential to maximize the window surface area at any size. → See Adaptive Design / Adaptive Layout.

**System Multi-Window**
Users can open multiple apps simultaneously, overlapping in x, y, and z axes. No system-wide window management exists (no Mission Control or Stage Manager equivalent). Mitigate by:
- Clearly labeling your app window (navigation bar title)
- Maintaining safe areas at window edges for grab interactions without interfering with tab/scroll zones

**Application Multi-Window**
Apps can spawn multiple windows for persistent tool panes or auxiliary info panels. Recommended constraints:
- Connect additional windows with fixed spatial relationships and distances
- Use additional windows mainly for persistent views (toolbars, complementary visualizations)
- Make open/close behavior clear to users
- Note: only macOS supports multiple windows cross-platform — consider the development/testing implications

### Design Resources

- Apple visionOS design kit: [Apple Design Resources](https://developer.apple.com/design/resources/)
- Figma visionOS kit: Open in Figma
- Sketch: Add to Sketch Library

---

## Immersive Applications

Designing 3D content requires a different toolset.

### Apple Tools
- **Reality Composer Pro** (included with Xcode)
- **Reality Composer** for iOS/iPadOS

### Third-Party Tools (under evaluation)
- **ShapesXR** — VR prototype creation with Meta Quest
- **Twinmotion**
- **Unity**
