---
id: idea-20260717-interaction-dictionary
title: "Interaction-as-Dictionary — A Unified Modeling Framework"
tags:
  - modeling
  - epistemology
  - anti-essentialism
  - relationism
  - interaction
  - dictionary-metaphor
  - attention-filter
  - meta-model
importance: 9
connections:
  - type: idea
    slug: "interaction-as-essence-heuristic"
  - type: idea
    slug: "strategy-three-component-model"
  - type: idea
    slug: "knowledge-as-dictionary-of-perspectives"
  - type: idea
    slug: "three-layer-framework"
  - type: idea
    slug: "portal-model"
  - type: idea
    slug: "cohesion-coupling-heuristic"
  - type: idea
    slug: "attention-pointer-learning-model"
  - type: idea
    slug: "locate-first-model-last"
---

# Interaction-as-Dictionary — A Unified Modeling Framework

**One sentence**: Every knowledge point is a dictionary mapping interaction contexts to interaction patterns — and that's all it is.

## Relationship to Source Ideas

This framework synthesizes two previously independent ideas:

| Source Idea | What It Provides | Limitation (Before Synthesis) |
|---|---|---|
| [[interaction-as-essence-heuristic]] | The philosophical basis: "what something *is* doesn't matter — only how it interacts with other things matters." Properties are regularities; "essence" is just a property whose interaction scope happens to be very wide. | Describes *why* interaction is primary, but doesn't specify a *structure* for organizing interaction patterns. |
| [[knowledge-as-dictionary-of-perspectives]] | The data structure: a knowledge point IS a dictionary `{key: value, ...}` where key = perspective/layer, value = meaning under that perspective. Values can nest recursively. | Describes *how* to organize knowledge, but doesn't explain *why* the dictionary is the right structure — perspective selection criteria remain heuristic. |

**The synthesis**: Dictionary-of-perspectives answers "what does knowledge look like?" (a dictionary). Interaction-as-essence answers "why does it look like that?" (because the full content of a knowledge point IS the set of its interaction patterns, and a dictionary is the most natural container for that set). Together: **knowledge's structure is a dictionary; the dictionary's semantics is interaction.**

The synthesis also corrects one assumption in dictionary-of-perspectives: the original implicitly treats "perspective" as a viewing angle — a passive observation window. This framework redefines perspective as a **selective filter over interactions**, making foreground/background cuts on the full interaction set (see §5–6).

---

## 1. The Only Purpose of Learning Is Discovering Interactions

Not "understanding essence." Not "mastering knowledge." Not "passing exams." Interaction discovery is the endpoint. Everything else is a byproduct.

The thesis is anti-essentialist and operational: an object's internals are a black box — inaccessible and irrelevant. Its interface (interaction patterns with other objects) is the only operable data source.

---

## 2. Class vs. Object

### 2.1 At the language level, these entities ARE objects

"Merge sort," "Python function," "knowledge" — within the language filter, these participate in interactions as indivisible wholes. You can say "merge sort is faster than bubble sort" — in that comparison, "merge sort" is an object. It engages in a horizontal interaction with another language-level entity, and for that interaction it does not decompose. Language is itself a filter; within it, linguistic entities are objects.

### 2.2 The class interpretation is what vertical interaction looks like from above

Why does it feel like "merge sort" is a class? Because when you trace its **vertical interactions** downward — the language-level name connects to `merge_sort_algo` (algorithm filter), `merge_sort_code` (program filter), divide-and-conquer (conceptual filter) — the language-level name appears to "bundle" them. It looks like a class gathering instances.

But this is not what the language-level entity *is*. It is what the vertical interaction pattern *looks like* when observed from the language filter. Class is an impression created by a specific interaction relationship — not an intrinsic property of the entity. To say "language describes classes" is to mistake one filter's view of a vertical relationship for a definition of the entity itself.

The class/set description is convenient for understanding — it's a compact mental shorthand — but it is not more "essential" than the object interpretation. Both are valid views from different interaction angles.

### 2.3 The real object: a name → interaction-pattern-set binding

An object, in this framework, is: **within a given filter, a name bound to a stable set of interaction patterns.** Nothing more. The object has no intrinsic content beyond those patterns.

### 2.4 Analogy: function as object

In Python, a function is a first-class object — the label "function" suggests it is an operation (something executed), but it can simultaneously be passed, bound, inspected. Identity slides between levels:

- When it **participates in an interaction** → it is an **object** (an indivisible whole)
- When it is **decomposed and described** → it is a **class** (a collection of sub-entities)

Identity is not fixed — it is determined by the current interaction.

---

## 3. Definition of Object: Indivisible at the Interaction Level

**Core logic**: Decomposability is not determined by "does it have internal structure?" but by "do the parts of that internal structure possess independent interaction signatures within the current filter?"

The same entity can be an object in one filter and a class in another. Atomicity is filter-relative.

Three complementary angles (not competitors — three views of the same core claim):

| Angle | Criterion |
|---|---|
| **Decomposition** | If you break it apart, the pieces have no independent interaction signatures — breaking it *changes* it. |
| **Granularity** | It is the smallest unit that has a meaningful interaction signature within the current filter. Below this level, nothing has its own interaction patterns. |
| **Interface** | It possesses a set of interaction patterns that can only function as a whole — they cannot be distributed to smaller entities without information loss. |

---

## 4. The Only Thing We Need to Do: Find Objects, Find Interactions

That's it. Two operations.

Methods for finding objects appear diverse (linguistic decomposition, perspective-based binding), but they are fundamentally one operation: **identify a stable cluster of interaction patterns within undifferentiated data, then bind a name to it.**

This is exactly the method described in [[knowledge-as-dictionary-of-perspectives]]: enumerate keys (interaction contexts), fill in values (interaction patterns), nest where needed.

### Example: `open("data.txt")`

Take a simple line of Python: `f = open("data.txt")`. Instead of asking "what is a file object, essentially?", enumerate its interactions:

**Horizontal (within the program-level filter)** — `f` interacts with other program-level objects:
- `content = f.read()` — returns the file's full contents as a string
- `lines = f.readlines()` — returns a list of lines
- `f.close()` — terminates the connection
- `with open(...) as f:` — auto-closes on block exit

**Vertical (program → conceptual filter)** — the program-level name `open("data.txt")` binds to conceptual-level entities:
- "A channel that delivers data from disk to memory"
- "A cursor position that advances as you read"
- These conceptual entities in turn interact with each other ("reading advances the cursor → subsequent reads start from the new position")

**Horizontal (within the conceptual filter)** — the concept "file handle" interacts with other concepts:
- Streams, buffers, and encoding
- The file system's notion of a path
- The programmer's mental model of "data now available"

None of this requires knowing what `open("data.txt")` "essentially is." The interaction map is the understanding. Once the map is filled in, the question of essence dissolves — there's nothing left to ask.

Importantly: **the process of discovering objects is itself conducted through interaction** — the interaction between you and the raw data. Nothing escapes the system.

### Side note: the status of mental models

This framework demotes "mental models" from claims about reality to tools within the interaction network. Take [[portal-model]] — a conceptual-level object that helps the programmer predict code behavior. Its value is not in whether it "correctly" describes how Python executes. The question "is the Portal Model right?" is replaced by: "does this object interact productively with other objects?" — does it help you infer `f`'s state after `f.read()`? Does it help you locate a bug? If yes, keep it. If not, swap it for another analogy. A mental model is just another node in the interaction graph — it has no special epistemic status.

The same applies to any analogy, metaphor, or "way of thinking about" something. They are objects in the conceptual filter. Their only reason for existing is the interactions they enable or block.

---

## 5. The Attention Filter: How Humans Participate

Humans are not passive observers of interaction. Human cognition comes with a built-in filter that has limited resolution.

We naturally notice **first-order interactions** — simple, intuitive input-output relationships — and ignore **hundredth-order interactions** — relationships that oscillate rapidly, depend on multi-level cascades, or are non-monotonic. Not because the hundredth-order interactions don't exist, but because they are invisible through the human attention filter.

**"Importance" is not a property of the interaction itself. It is the interaction's visibility through the human attention filter.**

The full chain:

> **Raw interactions → Attention filter → Named objects → Further interaction discovery**

The attention filter determines which interactions enter the model and which are discarded as noise. Its bandwidth, biases, and blind spots constrain the upper bound of all knowledge built on top of it.

---

## 6. Perspective Redefined: Selective Filter Over Interactions

(This is the key correction to the original dictionary-of-perspectives concept.)

A perspective is not "viewing something from an angle." It is not "choosing an interaction context." A perspective is **a selective filter that pushes certain interactions to the foreground and suppresses others to the background.**

Example: "Merge sort from the algorithmic perspective"
- Foreground: O(n log n), stability, comparison count
- Background: memory byte layout, CPU cache behavior, the Python interpreter's call stack

Memory layout and cache behavior ARE interactions of merge sort — but the algorithmic filter chooses not to look at them.

**The same interaction set, given a different filter, yields a different perspective.** A perspective's value is not in revealing new information, but in suppressing noise — it lets you see clearly along one dimension, at the cost of temporary blindness along others.

In the dictionary model: **key = filter name, value = the interaction patterns that pass through that filter.**

---

## 7. Three Types of Interaction Operations

### 7.1 Horizontal interaction (within a single filter)

Different objects, when passed through the same filter, can be directly compared or related. Merge sort and quicksort under the "algorithmic complexity" filter both exhibit O(n log n) — the shared filter places their outputs in the same comparison space.

Horizontal interaction is **pattern comparison within a shared filter.**

### 7.2 Vertical interaction (across filters)

Each filter space has its own name → patterns bindings: `merge_sort_algo` in the algorithmic filter, `merge_sort_code` in the program filter. These names are independent entities — there is no "merge sort" that transcends them.

But the names themselves can interact. The binding relationship between `merge_sort_algo` and `merge_sort_code` IS a vertical interaction pattern. The relationship between the divide-and-conquer concept and the `T(n) = 2T(n/2) + O(n)` recurrence is not a derivation — it is **an alignment between two names in different filter spaces.**

Vertical interaction does not require assuming "the same thing" exists across filters. Each filter space has its own entities; vertical interaction connects them.

### 7.3 Class abstraction (an impression created by vertical interaction)

When a set of names across different filters have dense vertical interactions, and we view this structure from the language filter, the language-level name appears to "bundle" the filter-level names. We call this impression a **class** ("merge sort"). The class itself binds no interaction patterns and has no ontological weight — it is what vertical interaction density looks like from above. It is a convenient shorthand for conversation, not an entity in its own right.

---

## 8. Interaction Patterns as Objects (Recursion)

Two objects can have a direct interaction (merge sort ↔ quicksort under complexity comparison). But "this comparison" is itself an interaction pattern — and it can enter into relationships with other comparisons ("insertion sort ↔ bubble sort comparison" vs. "merge sort ↔ quicksort comparison" → which has the larger gap?).

Objects interact → producing interaction patterns. Those patterns can be **promoted to objects** — bound to names — and enter the next level of interaction analysis. The model is recursive.

This embeds the "meta" level without requiring a separate framework: pattern-level interaction is the same operation, one recursion level up.

---

## 9. Acknowledged Limitations

- **"Interaction" itself is not rigorously defined.** The stability, robustness, and scope conditions of interaction patterns are open problems. This is a heuristic framework, not a formal system.
- **Verification mechanisms** (distinguishing real interactions from noise/coincidence/post-hoc rationalization) belong to the practical layer and are not addressed here.
- **Bootstrapping** — how the model starts from zero, how the first object is carved out of raw experience — is deferred to the methodology described in [[knowledge-as-dictionary-of-perspectives]].

---

## 10. Methodology

[[knowledge-as-dictionary-of-perspectives]] is the current operational methodology. It provides:

1. **Generation heuristic**: When encountering a new knowledge point, two questions both work:
   - "What are its angles?" — a discovery tool: propose candidate filters, see which ones yield stable interaction patterns
   - "**What does it interact with?**" — the deeper question: angles are a means; interaction discovery is the end
   
   The two are in a means-end relationship, not competition. "What are its angles?" is often the more natural starting point — you may not know what something interacts with until you try a few perspectives and see which ones catch. But the purpose of enumerating angles is always to uncover interaction patterns.
2. **Key selection criterion**: Keys are determined by interaction relationships, not by disciplinary convention. The question is not "what perspectives does this field have?" but "what does this thing interact with?"
3. **Recursive nesting**: A value can itself be a dictionary — corresponding to hierarchical refinement of interaction contexts (e.g., philosophy has one top-level key but deep nesting because its interactions are all concept-to-concept).
4. **Anti-essentialist operationalization**: "What is X?" → "In what scenarios does X interact with what, and how?" The question dissolves into the method.

---

## Connections to Existing Frameworks

- **Explains** [[three-layer-framework]]: The three layers are defined by their cross-layer interaction patterns, not by intrinsic content type. The framework's value comes from the four standard connection patterns — interaction IS the structure.
- **Explains** [[portal-model]]: The execution model's value is not representing the "essence" of how Python runs, but serving as a mental portal for predicting program behavior — behavior prediction IS interaction with the programmer's reasoning.
- **Parallel to** [[cohesion-coupling-heuristic]]: High cohesion, low coupling is the software engineering version of "focus on interactions, not essence." Modules have interfaces and interaction patterns, not intrinsic natures.
- **Related to** [[attention-pointer-learning-model]]: The attention filter (§5) is a learning-theoretic parallel — attention selects which interactions get processed.
- **Behavioral corollary** of [[locate-first-model-last]]: You locate objects by scanning their interaction patterns; you model only after the interaction map is in place.
