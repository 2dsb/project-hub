# idea-lab — Knowledge Layer

Two input sources → one melting pot:

```
Literature Notes ──→ ideas (melting pot) ←── Project Notes
                      │
                      └── connections emerge, insights compound
```

## Structure

- **ideas/**: The melting pot — all ideas live here. Knowledge from literature notes and project notes feeds in; connections emerge and insights compound.
- **literature-notes/**: Content from books/web, rewritten in own words. Source: 卡片笔记写作法. Do NOT auto-translate — Chinese is source of truth.
- **project-notes/**: Learning extracted from completed projects.

## Idea Metadata

5 fields only: `id`, `title`, `tags`, `importance` (0-10), `connections` (links to other ideas).

## Artifacts

- **ideas-index.json**: Auto-generated from all idea files. Regenerate after any batch change to ideas/.
- Relationship graph (planned): global view of all idea connections.
