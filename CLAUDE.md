# Project Hub — Cross-Cutting Conventions

## Design Philosophy

Originally a monolithic, heavy system. Decomposed into 5 subsystems by **internal cohesion** (connections within a subsystem >> connections between subsystems). Cross-module connections were **deliberately sacrificed** for simplicity — each subsystem is independently maintained.

When content spans categories, **duplicate** the file into both subsystems rather than cross-referencing. Each copy evolves independently. Two files, two contexts, no shared dependency.

## System Architecture

```
~/project-hub/
├── idea-lab/          ← Knowledge layer
├── skill-forge/       ← Behavior layer
├── mission-control/   ← Project command center
├── social-resources/   ← Social resources & networking
└── life-console/      ← Daily operations
```

Each subsystem has its own `CLAUDE.md` with module-specific conventions.

## User Preferences

- **Decision style**: Decisive — always picks the recommended option without hesitation; prefers "do it all at once" over phased waiting.
- **Communication**: Minimalist command-style — uses single-word prompts like "continue" to drive progress; dislikes verbose explanations or frequent confirmations.

## Global Conventions

- **File naming**: kebab-case English slugs for all entity files.
- **Project directory naming**: All projects under `~/` follow `teach-*` (learning, uses `/teach` skill) or `project-*` (building/creating/exercising, no `/teach`). See `mission-control/CLAUDE.md` for details.
- **Dates**: YYYY-MM-DD throughout.
- **Translation**: ideas/, skills/, social-resources/, daily/ are in scope for Chinese→English translation. literature-notes/ is NOT auto-translated (Obsidian imports, Chinese is source of truth).
- **Deliberate duplication**: Cross-module content is copied, not linked. Each copy lives independently in its own subsystem.
