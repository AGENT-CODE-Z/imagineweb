# Schema Rules

## Coordinate System
- Use: x, y, width, height
- Do NOT use: top, left, right, bottom

## Common Fields
- id: unique string
- type: lowercase string
- bbox: object with x, y, width, height
- children: array of ids

## Job Status
Allowed values:
- queued
- processing
- done
- failed