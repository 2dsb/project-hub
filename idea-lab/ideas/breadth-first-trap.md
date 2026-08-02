---
id: idea-{ts-1748960400-b3d5f2}
title: Breadth-First Search → Depth-First Execution
tags:
- productivity
- information-overload
- execution
- meta-skill
- actionable
summary: "The note contrasts two cognitive bottlenecks: using breadth-first search where depth-first execution is needed, due to anxiety-driven pseudo-efficiency that incurs high switching costs, and recursive dependency nesting that overloads working memory like a stack overflow. For the first, the fix is to externalize a step chain before any searching, throttle result openings, and search only when stuck—or ask AI for step-by-step guidance. For the second, one should draw the full dependency tree to offload cognitive load, then execute from the bottom-up leaves, adding newly discovered prerequisites as child nodes without mentally maintaining the entire hierarchy."
body_hash: "1f7e4338"
importance: 4.53  # auto
connections:
  - type: project
    slug: ai-ability
  - type: idea
    slug: flow-based-thinking
  - type: idea
    slug: goal-singularity
  - type: idea
    slug: completion-vs-quitting
  - type: idea
    slug: certainty-gravity
  - type: permanent
    slug: 卡片笔记写作法c3.4
  - type: permanent
    slug: 优秀的绵羊c6.3
  - type: idea
    slug: "framework-extraction-pattern"  # review: 0.546
  - type: idea
    slug: "efficiency-formula"  # review: 0.541
  - type: idea
    slug: "freedom-exploration-generator"  # review: 0.538
  - type: idea
    slug: "attention-as-bottleneck"  # review: 0.536
  - type: idea
    slug: "how-to-deal-with-complexity"  # review: 0.500
  - type: idea
    slug: "learning-pipeline"  # auto, review: 0.552
  - type: idea
    slug: "environment-diagram-dual-perspective"  # auto, review: 0.511
  - type: idea
    slug: "data-pattern-prediction-chain"  # auto, review: 0.507
---
# Breadth-First Search → Depth-First Execution

## Pattern A: Search Overload (Horizontal)
**Symptoms**: Before starting a task, you open 15-20 reference pages (tutorials, videos, guides, tool sites), mentally context-switching across all of them.

**Root cause**: Using "breadth-first search" for a "depth-first" job — speculative searching is anxiety-driven pseudo-efficiency; the switching cost vastly outweighs the information value.

**Fix**:
1. **Write a 3-step chain before starting**: Don't search for anything yet. First, write down the step chain in one sentence. Strictly focus on only the current step at any given time.
2. **Search throttling**: When you do search, open only the 1-2 most relevant results. Source priority: official docs > recent blog posts > video tutorials.
3. **Search only when stuck**: Don't predict what you'll need later. Start doing first, search only when you hit a wall.
4. **Use AI instead of multiple tabs**: For configuration-type tasks, ask AI directly for step-by-step guidance.

**Trigger**: More than 5 reference pages open → close them all, write the step chain, return to the current step.

---

## Pattern B: Dependency Nesting (Vertical)
**Symptoms**: You want to do X, but the guide says you need A first; A requires C and D; C in turn needs… The entire dependency chain is maintained in your head, exhausting working memory.

**Root cause**: Recursively expanding the dependency tree in your head → stack overflow. Your brain is not a terminal; it's not built to maintain multi-level call stacks.

**Fix**:
1. **Draw the dependency tree first, don't execute**: Work backward from the goal and write down the entire tree. Externalization = offloading cognitive load.
2. **Execute from the leaves up**: The bottom-level leaves of the tree = "things you can do right now." Do them, cross them off, work bottom-up. You don't need to remember the whole picture — just ask "what's the next executable leaf?"
3. **Hang new dependencies onto the tree**: If you discover a new prerequisite during execution → add it as a child node on the tree → go back to step 2.

**Trigger**: More than 3 levels of nested "to do X, I first need to… which first needs to…" in your head → stop and draw the dependency tree.
