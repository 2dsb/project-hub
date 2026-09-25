---
id: idea-20260925-standardize-the-framework-not-the-product
title: "Standardize the Framework, Not the Product — A Language for Customization"
tags:
  - product-design
  - customization
  - dsl
  - modularity
  - platform-economics
  - framework-design
  - cost-reduction
  - startup-idea
  - unformed
summary: "The central claim is that customization becomes cheap for everyone if what is standardized is the framework rather than the product, with a domain-specific customization language as the user-facing way to fill the framework’s slots. Because the machinery is fixed while materials vary, each new bespoke product is an instantiation rather than a rebuilt framework, so cost falls. A language lowers the barrier only if its vocabulary stays bounded to that parameter space; otherwise it becomes a general-purpose programming language and the barrier returns. The design must avoid the Factory Paradox, ruling things out so the framework describes something, while staying general enough for real products."
body_hash: "3dcfc6f0"
connections:
  - type: idea
    slug: "standard-engineering"  # auto, review: 0.567
  - type: idea
    slug: "reconceptualizing-standard-engineering"  # auto, review: 0.557
  - type: idea
    slug: "core-capability-supporting-infrastructure-pattern"  # auto, review: 0.504
importance: 0.0  # auto
---
# Standardize the Framework, Not the Product — A Language for Customization

> **Status: unformed.** Stated as a question ("can we?"), not a finding. The thesis is sharp; the mechanism is not worked out.

**One sentence**: Lower the barrier to customization until every user can build a product that is *theirs* — by standardizing the **framework** rather than the product, and giving users a **language** in which to instantiate it.

## The Three Claims

1. **The goal**: lower the customization threshold so that every user is capable of building their own bespoke product.
2. **The means**: construct a language specific to *customization* — a notation whose vocabulary is the act of customizing.
3. **The thesis**: what gets standardized is the **framework**, not the product. Cost falls as a consequence.

The third line is the load-bearing one. "Custom products for everyone" sounds like a contradiction — bespoke means expensive, and universality means generic. The resolution is that these are claims about two different things: the product varies, the machinery producing it does not.

## Why the Thesis Works

The economics are the factory's, and [[world-factory-framework]] already states them: *a factory does not contain its products.* It has machinery — molds, jigs, assembly lines — and any incoming material gets fed through them.

- The **machinery is fixed**; the **materials vary**.
- Universality is a property of the machinery, not the inventory.
- Fitting is **instantiation**: the framework supplies the shape, the product fills the slots.

Cost follows directly. A bespoke product whose framework is rebuilt each time costs O(N) — every unit is a project. Standardize the framework and the cost becomes: **pay once for the machinery, then each instance is an instantiation.** The Nth custom product is cheap in a way the first was not.

This is why "lower the barrier" and "standardize the framework" are the same claim. The barrier *is* the framework-rebuilding cost, paid by the user in skill or by the vendor in labor.

## The Language Is the Interface to the Machinery

If the framework is fixed, the user needs a way to fill its slots — and that is what the customization language is. Its job is not to be expressive. Its job is to be **the framework's parameter space, made writable**.

Two existence proofs that this pattern genuinely lets non-specialists build bespoke things:

| Framework (standardized) | Language (user-facing) | What users build |
|---|---|---|
| A relational storage engine | SQL | Their own queries |
| A grid + formula evaluator | Spreadsheet formulas | Their own models, reports, tools |

Neither user writes general-purpose code. Both produce artifacts nobody standardized. The engine was fixed; the product was not.

## Why a Language Lowers the Barrier Instead of Just Moving It

The obvious objection: a language still has to be learned, so haven't we just relocated the threshold?

The answer is that learning cost is **bounded by vocabulary size**, and the vocabulary here is exactly the framework's slots. Two things follow:

- A **domain-specific** language has a bounded, finite vocabulary — learnable in an afternoon, because there is a ceiling on what it can say.
- A **general-purpose** language has unbounded vocabulary, so its learning cost is unbounded.

Customization requires only the first. The user is not being asked to program; they are being asked to fill in a form whose fields happen to compose.

## The Trap: Vacuous Generality

There is a failure mode, and it is the one [[world-factory-framework]] names as the **Factory Paradox**: *a factory that accepts everything describes nothing.*

If the customization language can express anything, it **is** a general-purpose programming language, and the barrier is fully restored — just with worse tooling. So the language must **rule things out**. It has to constrain meaningfully, and the constraint must be accepted as a feature.

This produces the central design tension: **the framework must be general enough to admit the products users actually want, and narrow enough that the language stays small.** Those pull in opposite directions, and the whole idea lives or dies on where the line lands.

## Open Questions

- **What are the slots?** The design reduces to one question: what is the parameter space — the axes along which users actually vary? Get this wrong and users hit the ceiling and demand escape hatches, which is general-purpose programming returning through the back door.
- **Is "customization" one domain or many?** A language is specific to a framework, and frameworks are specific to domains. So this may not be one idea but a pattern — "find the framework, standardize it, ship a language" — applied per domain.
- **What does AI change?** If a model can take intent and emit instantiations, the user-facing language may be natural language with the framework as a constraint. That would collapse the learning cost to zero — but the framework's slots still have to exist, so the hard part is unchanged. It is worth asking whether AI makes the *language* unnecessary or merely makes the *interface* to it conversational.
- **Who captures the value?** Standardizing the framework is where the leverage sits — the framework owner, not the product builder, holds the position. This is a business-structure question as much as a design one.

## Related

- [[world-factory-framework]] — the same thesis in the epistemic register: fixed scaffold, variable instances, and the Factory Paradox that limits it
- [[content-independent-framework]] — the knowledge-domain version of "organize by structure, not content"; the same reason frameworks outlive products
- [[ai-organization-programming-language]] — a worked precedent for building a language over a fixed substrate, with the same "is this a real language or just sugar?" question
- [[structure-native-tools]] — whether a framework can treat the product's structure as native I/O rather than something to coerce
- [[language-cannot-specify-diagrams]] — the complementary failure: a language lowers the barrier only if it can actually carry what the user means
