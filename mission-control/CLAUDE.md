# mission-control — Project Command Center

mission-control stores metadata only. Actual project files live in `~/<project>/`.

## _PROJECTS.md

Single table with 5 columns: `Project | Directory | Priority | Type | Status`.

- **Status**: `active` / `completed` / `paused` / `archived`
- **Type**: `project` (has an end point) or `ongoing` (continuous — track frequency, not completion)

## Individual Project Cards

One file per project. Frontmatter + one-sentence body summary. Frontmatter fields: `title`, `directory`, `priority`, `status`, `type`, `deadline` (optional), `tags`.

Each project lives in `~/<slug>/README.md`. The card in mission-control is the metadata entry in the registry.
