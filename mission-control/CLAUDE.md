# mission-control — Project Command Center

mission-control stores project metadata in a single registry table. Actual project files live in `~/<project>/`.

## _PROJECTS.md

Single registry table — the **only source of truth** for all projects. No individual card files.

Columns: `Project | Directory | Priority | Type | Status`

- **Priority**: `critical` > `high` > `medium` > `low`
- **Status**: `active` / `completed` / `paused` / `archived`
- **Type**: `project` (has an end point) or `ongoing` (continuous — track frequency, not completion)

### Adding a project

1. Create `~/teach-<slug>/` or `~/project-<slug>/` with a `README.md` inside
2. Add a row to the `_PROJECTS.md` table
3. Update the project count in the header

### Removing a project

1. Delete the row from `_PROJECTS.md`
2. Delete the `~/<project>/` directory (or archive it)
3. Update the project count

## Naming Convention

All projects use one of two prefixes:

- **`teach-*`** — learning anything (courses, books, skills, tools). Uses the `/teach` skill.
- **`project-*`** — building, creating, exercising, or managing. Does NOT use `/teach`.

Directory name and registry name must match exactly.
