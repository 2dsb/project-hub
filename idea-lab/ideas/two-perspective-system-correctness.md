---
id: idea-20260801-b7e3a1
title: Two-Perspective System Correctness — Dependency Graph + Storage Matrix
tags:
  - system-design
  - maintenance
  - correctness
  - data-modeling
  - meta-cognition
summary: "The Two-Perspective System Correctness framework captures that a change in one part of a system requires updates elsewhere by using a horizontal data dependency graph and"
importance: -1
connections:
  - type: idea
    slug: "audit-blind-spot-spec-limitation"  # auto, review: 0.510
  - type: idea
    slug: "cohesion-coupling-decomposition-heuristic"
---
## Problem

Even for a "moderately simple" system (190 ideas, 6 scripts, 3 derived files), it's easy to lose track of what needs updating when you change something. If this is hard for a small system, how do you handle a large one?

## Two Perspectives

Think of it as a hierarchy: each abstract data type is a "boss" (大哥), and each boss has several "workers" (小弟) — concrete copies of the data in specific files and formats.

### Horizontal: Boss-to-Boss (Data Dependency Graph)

A directed graph where each node is a **boss** (abstract data type, independent of storage). An edge A → B means "if Boss A changes, Boss B must follow." Bosses talk to bosses.

For idea-lab:

```
(body + id + title + tags) ──→ summary ──→ connections ──→ importance
```

Each edge corresponds to one atomic operation.

**Important nuance**: The bosses don't actually exist — only workers do. A "horizontal" boss-to-boss edge is always implemented as a worker-to-worker operation in practice: read data A from storage location X → compute → write data B to storage location Y. The boss graph is the abstract model; the actual execution is always 小弟-to-小弟.

### Vertical: Boss-to-Workers (Storage Propagation)

Each boss has several workers — concrete instances in specific files. When a boss updates, it notifies all its workers to sync.

A storage matrix captures which workers exist for each boss. Rows = bosses (data types), columns = workers' locations.

## Example: idea-lab Maintenance System

### Storage Matrix

Rows = data types, columns = storage locations. ✓ means the data exists there.

| Data type | `ideas/*.md` | `ideas-index.json` | `connection-suggestions.json` | `graph.html` |
|-----------|-------------|-------------------|-----------------------------|-------------|
| id+title+tags+body | ✓ | ✓ | | ✓ |
| summary | ✓ | ✓ | | ✓ |
| connections | ✓ | ✓ | ✓ | ✓ |
| importance | ✓ | ✓ | | ✓ |
| total | | ✓ | | |
| generated | | ✓ | | |

### Dependency Graph

```
(body + id + title + tags) ──→ summary ──→ connections ──→ importance
```

### Operations Mapped to the Two Perspectives

Each maintain.py step is either horizontal (boss-to-boss), vertical (boss-to-workers), or both:

| Step | Script | Abstract (boss view) | Actual (worker-to-worker) |
|------|--------|---------------------|--------------------------|
| 1 | `generate_summaries` | body → summary | .md body → DeepSeek API → .md summary |
| 2 | `compute_connections` | summary → connections | .md summary → embedding model → suggestions.json connections |
| 3 | `write_connections` | (sync connections) | suggestions.json connections → .md connections |
| 4 | `compute_importance` | connections → importance | .md connections → PageRank → .md importance |
| 5 | `rebuild_index` | (sync all 6 bosses) | .md (all 6 fields) → index.json |
| 6 | `generate_graph` | (sync all 6 bosses) | index.json → pyvis → graph.html |

### Operation Modules

Three user-facing triggers, each grouping a subset of the steps:

| Trigger | Module (which steps run) | Starting step |
|---------|------------------------|---------------|
| Changed body | Steps 1→6 (`maintain.py`) | 1 |
| Changed tags | Steps 2→6 (`maintain.py --skip-summaries`) | 2 |
| Manual connection edit | Step 5 only (`rebuild_index.py`) | 5 |

The module is the answer to "what should I run?" — it encodes which edges in the dependency graph are downstream of the user's change.

### Requirements as Chain Reactions

A user requirement is fundamentally: "update these specific workers." From those starting workers, changes propagate through the system in a chain reaction — alternating between horizontal (boss-to-boss) and vertical (boss-to-workers) steps until all affected workers are consistent.

For example, "edit .md body" triggers the chain:

```
.md body changed (worker)
  → horizontal: body boss → summary boss
  → vertical: summary boss → .md summary (worker)
  → horizontal: summary boss → connections boss
  → vertical: connections boss → suggestions.json + .md connections (workers)
  → horizontal: connections boss → importance boss
  → vertical: importance boss → .md importance (worker)
  → vertical: all 6 bosses → index.json (worker snapshot)
  → vertical: all 6 bosses → graph.html (worker snapshot)
```

Every requirement can be modeled this way: pick the starting workers, then follow the horizontal+vertical chain until every reachable worker is updated.

## Operations

Two atomic types, corresponding to the two perspectives:

| Type | What it does | Example |
|------|-------------|---------|
| **Horizontal** | Boss A changes → Boss B recalculates (follow one edge in the dependency graph) | body changed → recompute summary |
| **Vertical** | Boss notifies all its workers to sync (propagate to every storage location) | importance changed → update .md + index.json + graph.html |

These atomics are grouped into **operation modules** (e.g., `maintain.py` = 6 horizontal + vertical steps).

## Correctness Check

To verify "everything that should update does update":

1. **Horizontal check**: Every edge in the dependency graph has a corresponding operation
2. **Vertical check**: Every True cell in the storage matrix has a propagation path back to the source of truth (.md files)
3. **Coverage check**: Every node in the dependency graph is reachable from user-facing mutation points (edit body, edit tags, manual connection, set importance:-1)

## Why This Matters

### The Real Advantage: Separating Macro from Micro

The framework's core value is that it splits system maintenance into two cleanly separated levels:

| Level | What it models | Examples |
|-------|---------------|---------|
| **Macro** | The boss/worker structure, dependency edges, storage matrix | "body → summary → connections → importance" |
| **Micro** | How each edge is actually implemented | "summary is generated via DeepSeek API call", "importance = -1 is a special case that skips overwrite", "CRUD: create new connection vs. skip existing" |

The macro level is **clean and stable** — it's a small graph you can hold in your head and verify for completeness. The micro level is where all the **messy implementation details** live: specific algorithms (embedding similarity, PageRank), special cases (-1 preservation), format conversions (YAML → JSON → HTML), CRUD logic (insert vs. update vs. skip).

This separation means:
- You can **reason about correctness** at the macro level without drowning in micro details
- You can **change an implementation** (e.g., switch from cosine similarity to a different metric) without touching the macro model
- You can **verify coverage** systematically: every macro edge has at least one micro implementation, every ✓ in the storage matrix has a sync path

The framework doesn't eliminate complexity — it **quarantines** it. Macro stays clean; micro handles the mess.

### Practical Payoff

This framework turns an intuitive, error-prone "did I forget something?" into a systematic checklist. The dependency graph tells you **what changes**, the storage matrix tells you **where to write it**. Together they guarantee completeness.

For more complex systems, the same pattern scales: identify data types → draw dependency edges → map storage locations → verify every edge has an operation and every cell has a propagation path.
