# mission-control — Project Command Center

mission-control stores metadata only. Actual project files live in `~/<project>/`.

## _PROJECTS.md

Single table with 5 columns: `Project | Directory | Priority | Type | Status`.

- **Status**: `active` / `completed` / `paused` / `archived`
- **Type**: `project` (has an end point) or `ongoing` (continuous — track frequency, not completion)

## Naming Convention

All projects use one of two prefixes:

- **`teach-*`** — learning anything (courses, books, skills, tools). Uses the `/teach` skill.
- **`project-*`** — building, creating, exercising, or managing. Does NOT use `/teach`.

Directory name and registry name must match exactly.
