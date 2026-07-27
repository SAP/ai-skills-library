# Design Principles — CarPlay Design

> CarPlay Design | Foundation

## What is it?

CarPlay apps assist users with **driving-related tasks** using the car's built-in display. They are extensions of iOS apps, enabling specific actions that don't distract from driving.

---

## Who Benefits Most

Users who drive frequently as part of their daily routine:
- Delivery drivers
- Field maintenance technicians
- Regional sales representatives

A CarPlay solution is valuable when users frequently change destinations/routes during their workday.

---

## Core Principle

**Safe driving is the priority.** All design decisions must minimize driver distraction. Content and interactions must enhance the driving experience — the interface must be straightforward enough that the driver can focus on the road.

---

## Design Principles

### 1. Focus on the User
Understand the driving context. Driving must be a core, frequent activity in the user's workflow for CarPlay to add value.

### 2. Driving-Related Use Cases Only
Only include information and actions that are **necessary while driving** — exclude pre/post-drive activities. This determines which Apple app type your app fits into.

**Business CarPlay app types to consider:**
- **Navigation apps** — route guidance, destination management
- **Point-of-Interest apps** — finding locations relevant to work tasks

### 3. UI Templates
CarPlay requires specific Apple-provided UI templates. Templates are determined by the approved persona and app type. No custom SAP Fiori UI controls or styling permitted.

**Template depth limits:**
| App type | Max depth (including root) |
|----------|---------------------------|
| Most apps | 5 templates |
| Fueling apps | 3 templates |
| Driving task / quick food ordering | 2 templates |

---

## What NOT to Include

- Non-driving activities (admin tasks, complex data entry)
- Custom fonts or colors (Apple templates only)
- SAP Fiori-specific components or patterns
- Deep navigation hierarchies exceeding template limits

---

## Resources

- [Apple CarPlay App Programming Guide](https://developer.apple.com/carplay/documentation/CarPlay-App-Programming-Guide.pdf)
- [get-started.md](get-started.md)
