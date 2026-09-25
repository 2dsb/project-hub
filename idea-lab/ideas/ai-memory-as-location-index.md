---
id: idea-20260925-ai-memory-as-location-index
title: "AI Memory as a Location Index — Know Where Knowledge Is, Transmit Only the Relevant Subtree"
tags:
  - AI
  - memory
  - long-context
  - retrieval
  - tree-structure
  - pointer-index
  - agent-architecture
  - unformed
summary: "The note sketches an unformed proposal that AI memory should act as a location index holding where knowledge is rather than the content itself, so passing state forward transmits only the relevant subtree of a chain or tree index and context becomes a budget of addresses instead of content. It argues this differs from retrieval-augmented generation because RAG retrieves by semantic similarity while a location index retrieves by structural position, returning the subtree that contains the answer rather than chunks that resemble the query. The idea mirrors human pointer-based attention and locate-first models, but open questions remain about pointer resolution cost, whether the index itself fits in context, what builds and maintains the tree, and how relevance is defined when structure is wrong."
body_hash: "a13618c4"
connections:
  - type: idea
    slug: "attention-pointer-learning-model"  # auto
importance: 0.48  # auto
---
# AI Memory as a Location Index — Know Where Knowledge Is, Transmit Only the Relevant Subtree

> **Status: unformed.** A sketch, not a design. The claim is stated; the mechanism is not worked out.

**One sentence**: An AI's memory should hold **where knowledge is**, not the knowledge itself — so that passing state forward means transmitting only the relevant subtree of a chain/tree index, and long context stops being a problem of size.

## The Vision

Three claims, stacked:

1. **Memory as index, not store.** What the AI remembers is a map of *locations* — "the thing about X is here" — rather than a copy of the content.
2. **Chain / tree structure.** The index is hierarchical: a chain where the path *is* the address, or a tree where branches partition the knowledge.
3. **Selective transfer.** When the conversation is handed to the next step, only the **relevant part** of the structure goes with it. Everything else stays behind the pointer.

The payoff: context stops being a budget of **content** and becomes a budget of **addresses** — and addresses are far cheaper than content.

## Why This Is Not Just RAG

This is the first thing the sketch has to survive, because retrieval-augmented generation already "transmits only the relevant part."

The difference is **how relevance is decided**:

| | RAG | Location index |
|---|---|---|
| Retrieval key | Semantic similarity to the query | **Structural position** in the index |
| What it returns | Chunks that *resemble* the question | The subtree that *contains* the answer |
| Where relevance lives | In an embedding space | In the model's own map of the domain |
| Cost model | Re-embed and search the corpus | Walk the tree |

Similarity retrieval returns things that *look like* the question. Structural retrieval returns things that *sit where* the answer must sit. Those are different and can disagree — the relevant subtree may contain nothing that resembles the query, and the most similar chunk may sit in an unrelated branch.

Whether that difference is real or just a better index is the open question, not the settled claim.

## The Human-Side Mirror

The corpus already contains this idea in the human case, which is what makes the AI version look less like a new proposal and more like a transplant:

- [[attention-pointer-learning-model]] — human attention is a single sequential pointer over a limited, decaying buffer. Same constraint, same move: hold the pointer, not the content.
- [[locate-first-model-last]] — separate *locating* knowledge points from *modeling* them. The AI version of this is: locate first (index), load last (context).
- [[knowledge-as-dictionary-of-perspectives]] — knowledge points are keyed by perspectives. That supplies the answer to "what would the index be keyed on?"
- [[knowledge-reconnection]] — retrieval-by-structure in the human system, as opposed to retrieval-by-similarity.

If the human version works because a pointer is cheaper than the content it points at, the AI version should work for the same reason — which is a good sign, and also a reason to check whether the analogy is doing real work or just being flattering.

## Chain vs Tree (a reading, not the author's claim)

"Chain/tree" may be naming **two structures for two jobs**, not one structure with two shapes:

- **Chain** — the natural shape of a *sequence of actions*: this, then that. The path is the plan.
- **Tree** — the natural shape of *knowledge*: this contains that. The path is the address.

If so, the mechanism is "action memory is a chain, knowledge memory is a tree," and they are indexed differently. Worth settling before designing, because it changes what "the relevant part" means in claim 3.

## Open Questions

- **Who resolves the pointer, and how cheaply?** If memory holds a location, something outside must hold the content. What is that store, and is resolving an address cheaper than just carrying the content? If not, the scheme loses.
- **Does the index itself fit?** Selective transfer requires knowing what is relevant, and that decision must be made from the index. So the index has to fit in context — the problem hasn't been removed, it's been moved up a level. Does it scale better there?
- **What builds and maintains the tree?** A correct index is the hard part. RAG avoids this by re-embedding; a structural index must be built and kept valid as knowledge changes.
- **What makes "relevant" well-defined?** Structural position gives relevance only if the structure is right. A wrong branch silently returns a confidently wrong subtree — a failure mode similarity search doesn't have in the same way.

## Related

- [[ai-cannot-learn-after-training]] — conversation isn't learning, so context is the *only* working memory; this idea exists because that is true
- [[two-perspective-system-correctness]] — abstract index vs concrete storage; memory-as-index is that same boss/worker split applied to context
- [[structure-native-tools]] — trees as structure-native I/O; this asks whether the same applies to memory
- [[ai-task-cost-bounds]] — what a pointer costs vs what content costs
