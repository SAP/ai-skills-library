# Get Started — CarPlay Design

> CarPlay Design | Get Started

## What is it?

CarPlay is an automotive platform extension to existing iOS apps — not a standalone app. It assists users with **driving-related tasks** using the car's built-in display. Non-driving activities must not be included.

---

## Key Facts

| Fact | Detail |
|------|--------|
| App type | Extension to existing iOS app (like watchOS) |
| Apple approval | Required for persona and use case **before** design/development |
| Special entitlement | Apple must grant CarPlay API access per application |
| App types | Must fit one of Apple's predefined CarPlay app types |
| UI | Apple-provided templates only — no SAP Fiori styling, fonts, colors, or custom components allowed |
| Testing | Use the CarPlay simulator to evaluate and test |

---

## Important Constraints

- Apple templates **do not allow modifications** — no SAP Fiori fonts, colors, or custom UI controls
- Must fit Apple's predefined app types (Navigation, Point-of-Interest, etc.)
- Template depth limit: most apps max **5 templates deep**; fueling apps max **3**; driving task and quick food ordering apps max **2** (including root)

---

## Resources

- [Apple CarPlay Design Guidelines](https://developer.apple.com/design/human-interface-guidelines/carplay)
- [Apple CarPlay App Programming Guide](https://developer.apple.com/carplay/documentation/CarPlay-App-Programming-Guide.pdf)
