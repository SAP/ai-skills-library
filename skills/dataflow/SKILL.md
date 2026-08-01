---
name: Dataflow Diagram
description: Generates an interactive data flow diagram as a self-contained HTML file from a free-text description. Use this skill whenever the user asks to visualize a data pipeline, data flow, system integration, or ETL process. Trigger on: "draw a data flow", "visualize my pipeline", "create a flow diagram", "map data sources", "show me how data moves".
---

# Dataflow Diagram

Generates an interactive data flow diagram as a self-contained HTML file using a canvas-based particle engine with draggable nodes, pan/zoom, and animated particles flowing along edges.

**Usage:** `/dataflow <description of the flow in free text>`

## Steps

1. **Infer nodes and edges** from the free-text description.

   Node types:
   - `n-source` — orange — data origin / SAP source system
   - `n-process` — blue — transformation / computation
   - `n-storage` — purple — database / data store
   - `n-queue` — cyan — message queue / event stream
   - `n-decision` — amber — condition / approval gate
   - `n-output` — green — final destination / data product
   - `n-external` — red — third-party / external API
   - `n-actor` — slate — human role / team

2. **Show summary** — list nodes and edges, then ask: *"Looks right? Say 'go' to generate, or tell me what to adjust."*

3. **Generate the HTML file** to the user's working directory. The file is fully self-contained with embedded JS/CSS.

4. **Confirm** with file path, node/edge counts, and instructions to open in browser.
