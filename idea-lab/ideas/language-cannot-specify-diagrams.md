---
id: idea-20260925-language-cannot-specify-diagrams
title: "Language Cannot Specify a Diagram — The Channel Is the Bottleneck, Not the Model"
tags:
  - representation
  - language-limits
  - diagram
  - visualization
  - human-machine-interface
  - AI
  - tool-design
  - unformed
summary: "# Language Cannot Specify a Diagram — The Channel Is the Bottleneck, Not the Model  > **Status: unformed.** Captured as a raw pain point, not a worked-out framework. The diagnosis below is a hypothesi"
body_hash: "b787cba6"
connections:
  - type: idea
    slug: "goal-singularity"  # auto, review: 0.529
  - type: idea
    slug: "human-structure-ai-completeness"  # auto, review: 0.520
  - type: idea
    slug: "human-machine-code-reading-gap"  # auto, review: 0.514
importance: 0.0  # auto
---
# Language Cannot Specify a Diagram — The Channel Is the Bottleneck, Not the Model

> **Status: unformed.** Captured as a raw pain point, not a worked-out framework. The diagnosis below is a hypothesis; the "what works" section is speculation.

**One sentence**: The reason AI can't draw the interaction diagram you have in mind is not that it can't draw — it's that **text is the wrong channel for specifying a picture**, so the part that actually distinguishes your diagram from a generic one never leaves your head.

## The Pain Point

You have a diagram in mind. You ask for it. What comes back is *correct and wrong at the same time* — every element is there, every arrow labeled right, and it is not your diagram. Then you try to say what's off and discover you can't. "No, arrange it differently" is the entire correction you are able to produce.

The instinct is to blame the model's drawing or spatial-reasoning ability. The diagnosis offered here is that the bottleneck sits earlier: **the specification channel is text, and text is a bad medium for spatial structure.** You are not failing to describe your diagram well enough. Your diagram may simply be undescribable, in the sense that the information that makes it *yours* has no textual form.

## Why Text Fails on Diagrams

| Property | Text | Diagram |
|---|---|---|
| Dimensionality | 1-D, serial, read left to right | 2-D, read all at once |
| What carries meaning | Word order, explicit relations | Adjacency, containment, alignment, grouping, relative position |
| Precision | "next to" — above? below? left? inside? | Exact by construction |
| Relation count | Described one clause at a time | O(n²) relations visible simultaneously |

Three consequences follow:

1. **Prose underspecifies.** "Put B next to A" is satisfied by a whole family of layouts. So is any paragraph you can write.
2. **Specifying a diagram in prose is lossy compression.** Many distinct diagrams satisfy the same text.
3. **The model fills the gap with the average.** Faced with an underspecified spec, it produces the *generic* member of the family — the centroid of every diagram matching your words. That is exactly the "correct but not mine" output above.

The failure is not random and not fixable by prompting harder. It is the deterministic result of asking a 1-D channel to carry 2-D information.

## The Correction Channel Is Just as Broken

The sharper version of the problem: this is not a one-shot specification failure that a better first attempt would fix. **The feedback loop is as un-speakable as the initial request.**

- "Move that one over there a bit" — "there" has no text referent.
- "Make it cleaner" — carries no gradient; the model has no way to know which of a hundred clean arrangements you mean.
- "No, not like that" — pure negative signal, zero direction.

Iterating doesn't converge, because each round costs a paragraph and returns an equally distant guess. This is why diagram requests with AI feel so much worse than code requests: **code has a textual surface, so the correction channel works.** Diagrams don't, so it doesn't.

## The Asymmetry

Human-to-human diagram handoff never worked this way. You sketched — whiteboard, napkin, a finger tracing a shape in the air. The channel was visual because the content was visual. Nothing about diagrams changed; the channel did. Text-only chat removed the visual channel and left only the weakest one available, and we then blamed the tool for what the interface made impossible.

## Why a Diagram DSL Works (and Prose Doesn't)

The clearest evidence for the channel diagnosis: people get dramatically better results by asking for **Mermaid, Graphviz, PlantUML, or TikZ** than by describing the same diagram in prose.

Note what this trade actually is. It is not "formal language is more precise than natural language" in general — it is that these notations are **serial on the surface with spatial semantics underneath**. You write left-to-right like prose, but each token denotes a *position or relation*, not a *word*. You have smuggled 2-D information through a 1-D channel.

The cost: you must learn the notation, and it only covers diagram classes the DSL anticipated. But the point stands — the win came from changing the channel's semantics, not from the model getting smarter.

## What Actually Works, and What Each Costs

| Approach | Fixes | Costs |
|---|---|---|
| Diagram DSL (Mermaid/TikZ) | Exactness, iterability | Learning curve; limited to anticipated diagram classes |
| Direct manipulation (drag boxes) | Exactness, zero ambiguity | Not expressible to an AI; doesn't scale to generation |
| Sketch / image input | Matches the natural channel | Requires multimodal input; sketching is its own skill |
| Iterative visual loop (point at the render) | Gives corrections a referent | Round-trip latency; needs a rendered artifact to point at |

The direction all four point: **give corrections a referent.** Half the pain is that "there" and "that one" have nothing to attach to.

## Open Questions

- **Channel or capability?** Is this really the input channel, or does the model also lack spatial reasoning? A clean test: give it an *image* of the target diagram and ask for a structurally equivalent one in a different layout. Succeeds → channel problem. Fails → capability problem. (Probably both, in unknown proportion — the whole diagnosis depends on that split.)
- **Where is the desirability boundary?** Some diagrams *are* fully specifiable in prose (a simple flowchart). Which properties of a diagram make it text-expressible, and which are irreducibly visual?
- **Is there a diagram-native input that keeps prose's ease?** Sketch, gesture, point-and-correct — something with prose's low ceremony but the diagram's ability to carry structure.
- **Does this generalize past diagrams?** Any target with spatial, topological, or continuous structure — UI layout, architecture, music, choreography — should show the same channel failure. Diagrams may be one instance of a broader class.

## Related

- [[structure-native-tools]] — the same mismatch from the tool's side: structure is discrete and exact, and text is not a structure-native channel into a model. DSLs are the symbolic half of the fix.
- [[human-machine-code-reading-gap]] — the human/machine representational gap in the opposite direction: there the human compresses what the machine spells out; here the human holds a 2-D object the machine can only receive as 1-D.
- [[call-tree-as-third-perspective]] and [[environment-diagram-dual-perspective]] — evidence that diagrams are not decoration but the representation that *carries* structure which prose loses.
- [[natural-language-narration-methodology]] — the complementary case: narration works well precisely where the content is already serial.
