---
id: idea-20260717-interaction-essence
title: Interaction-as-Essence Heuristic
tags:
  - modeling
  - epistemology
  - anti-essentialism
  - relationism
  - heuristic
importance: 4
connections:
  - type: idea
    slug: "interaction-as-dictionary"
  - type: idea
    slug: "three-layer-framework"
  - type: idea
    slug: "portal-model"
  - type: idea
    slug: "cohesion-coupling-heuristic"
---

# Interaction-as-Essence Heuristic

**Two-part modeling heuristic**: (1) don't ask what a thing is — ask how it interacts with other things; (2) "essence" is just a property whose interaction scope happens to be very wide.

## Part 1: Interaction Over Essence

What something *is* doesn't matter. The only useful thing is how it interacts with other things. When modeling, the question "what is the essence of X?" should be replaced with "in what interaction scenarios, in what ways, does X affect what?"

This dissolves a wide class of modeling problems: the object's internals are a black box — inaccessible and irrelevant. Its interface (interaction patterns with other objects) is the only operable data source.

## Part 2: Properties as Regularities; Essence as Limiting Case

A property *is* a regularity — a "given conditions → behavior" mapping. What we call "essential" vs "accidental" properties are not qualitatively different kinds of things. They differ only quantitatively — in the *scope* (breadth and density) of interactions they govern:

- A property that governs a very wide range of interactions → perceived as "essential" (e.g., proton number in chemistry)
- A property that governs a narrow range of interactions → perceived as "accidental" (e.g., the color of a particular sample)

There is no qualitative line between them. "Essence" is the asymptotic limit of interaction scope — you never reach it, you only approach it through the density and breadth of interaction patterns.

This generalizes Part 1 to cover cases where essentialism *appears* to work: proton number seems intrinsically essential not because it transcends interaction, but because it governs so many interaction patterns (chemical bonds, spectra, nuclear reactions) that we can't imagine what "considering it without interaction" would even mean. That's a difference of degree, not kind.

## Practical Use

When stuck on a "what is X?" question:
1. Replace with: "In what scenarios does X interact with what, and how?"
2. If an "essential" property is claimed, ask: "What range of interactions does it actually govern? Could a narrower-scope property serve the same modeling purpose?"
3. The heuristic doesn't deny that some properties are more useful than others — it just asserts that usefulness is measured by interaction scope, not by proximity to some inaccessible "true nature."

## Connections to Existing Frameworks

- **Explains** [[three-layer-framework]]: The three layers (Conceptual, Technical, Math) are defined by their cross-layer interaction patterns, not by intrinsic content type. The framework's practical value comes from the four standard connection patterns between layers — interaction is the structure, not an afterthought.
- **Explains** [[portal-model]]: The execution model's value is not in representing the "essence" of how Python runs, but in serving as a mental portal that lets you predict program behavior. Behavior prediction = interaction with the programmer's reasoning.
- **Parallel to** [[cohesion-coupling-heuristic]]: High cohesion, low coupling is the software engineering version of "focus on interactions, not essence." Modules don't have intrinsic natures; they have interfaces and interaction patterns. Good design = interaction scope well-partitioned.
