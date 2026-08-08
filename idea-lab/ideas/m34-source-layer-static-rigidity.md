---
id: "idea-20260608-ms01"
title: "M34 Structural Defect: Source Layer Static Rigidity"
tags: [system-design, coevolution, m34, data-source, rigidity, architecture]
summary: "M34 suffers from a structural defect called source layer static rigidity: its data sources are hardcoded, while coevolution claims sit only in the routing layer. Because the perception boundary cannot evolve, the system's coverage breadth declines as the user's working methods change, creating a contradiction. This is not a bug but a missing design dimension; the improvement direction is a self-extension mechanism to dynamically discover new data sources or allow manual registration."
body_hash: "d0426ee7"
importance: 2.83  # auto
connections:
  - type: idea
    slug: "system-coevolution-p1-data-coverage"  # auto
  - type: idea
    slug: "conversation-as-data-source"  # auto
  - type: idea
    slug: "system-coevolution"  # auto
  - type: idea
    slug: "daily-to-ideas-pipeline-broken"  # auto
  - type: idea
    slug: "system-coevolution-p3-autonomy-boundary"  # review: 0.580
---
# M34 Structural Defect: Source Layer Static Rigidity

## Discovery Process
Created `resources/thinking-tools/flow-based-thinking.md` → discovered M34 does not perceive the file → investigated why → identified root cause.

## Defect Essence
M34 claims "coevolution," but its data sources are hardcoded (6 entity directories + daily notes). All evolutionary capability sits in the routing layer (weight adjustment, pattern detection) — the source layer is a static snapshot.

## Implication
As the user's working methods evolve (new directories, conversation becoming a primary thinking medium, etc.), M34's "coverage breadth" will steadily decline. The system believes it is still observing the full picture, when in reality the slice it observes is growing narrower.

## Severity
**Structural contradiction** — a system that claims to evolve cannot evolve its own perception boundary. This is not a bug; a dimension is missing at the design level.

## Improvement Direction
M34's source layer needs a self-extension mechanism — for example, periodic scanning of new directories, detecting new information carrier patterns, or allowing manual registration of new data sources by the user.

## Connections
- "Conversation as data source" is essentially the first concrete manifestation of this defect
- Already fixed in Round 1 perfection iteration (R003 closed universe → dynamic entity discovery)
