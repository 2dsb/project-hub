---
id: idea-20260925-filter-map-as-general-test
title: "The Filter-Map Test Generalizes Past Math — File Instruments by What They Measure, Not by Domain"
tags:
  - teach-method
  - learning
  - verification
  - knowledge-map
  - programming
  - blind-spot
  - assessment
summary: "The filter-map test was wrongly filed as a math instrument, but it is a general structural-verification tool that programming also needs whenever no good execution test exists. Execution tests measure behavior, not whether the learner holds the right map of concepts, bindings, and constraints, and structural knowledge is the normal case where this matters. Its structure is supplied by interaction-as-dictionary, in which perspectives are selective filters, so domains supply the filters while the framework supplies the layout. Therefore verification instruments should be classified by what they measure, not by the domain they came from."
body_hash: "bc0823b1"
connections:
  - type: idea
    slug: "pattern-pipeline"  # auto, review: 0.547
  - type: idea
    slug: "learning-cycle-microstructure"  # auto, review: 0.529
  - type: idea
    slug: "content-independent-framework"  # auto, review: 0.521
  - type: idea
    slug: "teach-method-fixes"  # auto, review: 0.518
  - type: idea
    slug: "knowledge-mastery-two-axis-model"  # auto, review: 0.514
  - type: idea
    slug: "knowledge-map-format"  # auto, review: 0.510
  - type: idea
    slug: "human-machine-code-reading-gap"  # auto, review: 0.508
  - type: idea
    slug: "fundamental-model-of-learning"  # auto, review: 0.504
  - type: idea
    slug: "goal-predicate-f"  # auto, review: 0.504
  - type: idea
    slug: "data-structure-first-code-reading"  # auto, review: 0.502
importance: 0.0  # auto
---
# The Filter-Map Test Generalizes Past Math — File Instruments by What They Measure, Not by Domain

**One sentence**: The **filter-map test** — reproducing the cycle's knowledge map from memory — was assumed to belong to mathematics, but it applies equally to **programming**, particularly when no good execution test exists; the error was filing verification instruments by the *domain they came from* instead of by *what they measure*.

## The Blind Spot

The map test emerged in an analytic-geometry workspace (`~/teach-analytic-geometry/reference/cycle3-redraw.html`) and got filed, implicitly, as a **math instrument** — a theory-domain verification for a subject where you cannot simply run something and see if it works.

Programming is the opposite case in that classification: an *operational* domain, where verification is execution. You write the function, you run the tests, it passes or it doesn't.

The blind spot is taking that classification as complete. **Programming also needs the map test** — and needs it in exactly the case the user names: *when no good test can be found.*

## What the Redraw Actually Is

Looking at the analytic-geometry artifact rather than its label, it is not a recall quiz. It is a **structured map**:

- **Regions** — *Region I · The origin*, *Region II · Axis A*, *Axis B* — spatial organization, not a sequence
- **Blocks** inside each region — numbered units of knowledge
- **Two faces per block**, marked `●` algebra and `★` geometry, joined by `↔`

That last structure matters. Each block carries **both** representations and the **link between them**, so reproducing the map requires holding the concept *and* its operational face *and* the correspondence. It is a two-perspective instrument, not a single-axis recall test — the same shape as [[environment-diagram-dual-perspective]] and the bridge described in [[abstraction-barrier-as-dual-perspective-bridge]].

Which is precisely why it should not have been filed as math-specific. An instrument that tests structure-plus-binding is not "the theory-domain fallback." It is a general instrument that happened to be invented in a theory domain.

## Where the Map's Structure Comes From

This answers the question the instrument otherwise raises — *who decides what the map's regions and blocks are?* If each domain had to invent its own decomposition, the redraw would be far more expensive than it looks and would not generalize.

It does not have to. The structure is supplied by **[[interaction-as-dictionary]]**, and the name is not a coincidence — the *filter* in "filter-map" **is** that framework's perspective-as-filter.

The framework holds that:

- Every knowledge point is a **dictionary** mapping interaction contexts to interaction patterns
- A **perspective is a selective filter** — it foregrounds certain interactions and suppresses others
- A **key is a filter name**; its value is the patterns that pass through it
- An object is a name bound to a stable set of interaction patterns **within a given filter**

Read the analytic-geometry map through it and it stops looking hand-made:

| Map element | What it is under the framework |
|---|---|
| `●` algebra / `★` geometry | Two **filters** on the same knowledge — two interaction contexts |
| A block's content | The **interaction patterns** visible through each filter |
| `↔` between them | The binding between one object seen through two filters |
| Regions | Groupings of objects by the filters that reach them |
| Blocks within a region | Objects, recursively promoted from interaction patterns |

So the map is not invented per domain. Its **axes are the domain's filters**, produced by the same analysis the framework prescribes: find the objects, find their interactions, ask which perspective makes which interactions visible. **The domain supplies the filters; the framework supplies the layout.**

That is also why the instrument transfers to programming without redesign — programming has filters too (runtime behavior, static type structure, module boundaries, data flow), each making a different set of interactions visible. `●` and `★` would simply be a different pair of filter names.

**It also makes the map auditable, not just gradeable.** [[knowledge-as-dictionary-of-perspectives]] yields a generation heuristic — *systematically enumerate missing keys* — so a map can be checked for **absent filters**, which is a check no execution test can perform at any price.

## Why Programming Needs It

An execution test verifies **behavior**: does the artifact work. It does not verify **structure**: does the learner know where the artifact sits — which concept it instantiates, what it relates to, what would change if a constraint moved.

Those come apart in programming constantly:

- A learner can pass every test while holding a wrong map — *right answers, wrong structure*
- A learner can be unable to write a test for the thing at all, because the knowledge is not behavioral — knowing *when* to reach for an abstraction, *why* a module boundary sits where it does, *which* of two equivalent formulations is the idiomatic one

Writing a test requires the knowledge to be behavioral. A large share of programming knowledge is not.

So the trigger — *if you can't find a good test* — is not an edge case in programming. It is the **normal condition for structural knowledge**, which is where the map test is the only instrument available.

## The General Lesson

The two verification instruments fail in different directions, which is why both belong everywhere:

| Instrument | Measures | Blind to |
|---|---|---|
| **Execution test** | Behavior — does it work | Structure — whether the map is right |
| **Filter-map redraw** | Structure — is the map right | Whether it can be used |

The error was classifying them by **domain** (execution → operational, redraw → theory) when the real axis is **what they measure**. Once filed correctly, every domain draws from the full set instead of from its own column.

This is the same correction [[learning-cycle-microstructure]] makes one level down — treating the verification method as a **swappable plugin** rather than a property of the domain. This idea is the reason that matters: the plugin set does not change when the domain does.

## Open Questions

- **Does the framework produce regions, or only entries?** A dictionary is flat — key → value. But the analytic-geometry map has **regions**, a spatial hierarchy sitting *above* the entries. Whether [[interaction-as-dictionary]] generates that hierarchy or only the leaf entries is the remaining question. If it generates only entries, the regions are still hand-made and the cost problem returns in a smaller form.
- **Are filters discovered or chosen?** If a domain admits many filters, the map's content depends on which you pick — and two learners could hold structurally different but equally valid maps. That makes the redraw harder to grade against a single reference, and raises the question of whether a *canonical* filter set exists per domain.
- **How is a redraw graded?** A map can be wrong in ways that resist scoring — a missing block, a misplaced block, and a wrong link between two correct blocks are different failures. The exam tiers in `/teach` have crisp pass bars; a redraw needs one too.
- **Does it need a reference map?** Grading against an authored map ([[knowledge-map-format]]'s MAP.md) is one option; grading against the learner's own earlier map is another, and tests consolidation rather than fidelity.
- **Do both instruments compose?** Running them together on the same cycle — behavior *and* structure — may be strictly stronger than either, but doubles the verification cost.

## Related

- [[interaction-as-dictionary]] — supplies the map's structure: filters are the axes, interaction patterns are the entries. The *filter* in filter-map is this framework's perspective-as-filter
- [[knowledge-as-dictionary-of-perspectives]] — its generation heuristic (systematically enumerate missing keys) is what makes a map auditable for absent filters
- [[learning-cycle-microstructure]] — verification as a swappable plugin; this idea is the evidence that the plugin set is domain-independent
- [[knowledge-map-format]] — MAP.md as the authored reference a redraw could be graded against
- [[environment-diagram-dual-perspective]] — the two-perspective structure the analytic-geometry `●`/`★` blocks instantiate
- [[abstraction-barrier-as-dual-perspective-bridge]] — what the `↔` between the two faces is doing
- [[plugin-architecture-vs-defaults]] — the same warning applies: a verification plugin set is only worth having if it beats the distilled default
