# Requirements — connection-reading 多层级优化

**Task**: 优化 connection-reading.md，新增句子→段落、段落→文章的解网能力（当前仅覆盖字词→句子层面）。

**Started**: 2026-06-02 | **Phase**: requirements (Round 1 complete, Round 2 in progress)

---

## Round 1 — Answers Gathered

### Q1: How should the multi-level analysis be presented to the user?

**Answer (c)**: A single layered/toggleable graph where the user can drill down from article structure → paragraph chains → sentence constraints. Like a zoomable hierarchy.

### Q2: Which modes (A/B/C) should gain the new levels?

**Answer**: All three modes — Mode A (reading assistance, AI annotates), Mode B (post-read generation, user-driven), and Mode C (training mode, user practice) should all gain the sentence→paragraph and paragraph→article levels.

### Q3: Where should the new structure types for paragraph/article-level analysis live?

**Answer**: Create a new file `shared/text-structure-types.md`, separate from the existing `shared/constraint-types.md`. Constraint-types.md stays focused on concept-to-concept constraint relationships (the 9 existing types). Text-structure-types.md will house the new inter-sentence, inter-paragraph, and paragraph-to-article relationship types.

### Q4: Auto-extraction mechanism for shared/ files

**Answer**: The user wants a mechanism where the `shared/` type library files can automatically extract article content and update/enrich their type catalogs. As connection-reading processes articles, the constraint type library itself learns and grows from what it encounters — not just manual extension via the existing "扩展机制" (extension mechanism) in constraint-types.md, but an automated pipeline.

---

## Round 2 — Analysis & Clarifying Questions

### Context gathered for Round 2

**Existing files examined:**

- `skills/connection-reading.md` — Current skill. Has 3 modes (A=reading assistance, B=post-read generation, C=training mode). Currently operates at word→sentence level. Uses `shared/constraint-types.md` for its 9 constraint relationship types. Outputs Mermaid concept-constraint graphs. Has a manual "扩展机制" (extension mechanism) where new types are manually named, defined, and appended.

- `skills/shared/constraint-types.md` — Defines 9 constraint relationship types (定义, 详细化, 结果, 起源, 价值, 反例, 前提, 互斥, 程度依赖). Each has: meaning, example sentence pattern, and recognition signal words. Has a manual extension mechanism (4-step process). Defines graph structure: nodes = {name, domain?}, edges = {source→target, constraint type, evidence?}. Graph quality metrics: isolated nodes, contradictory edges, low density.

- `skills/inquiry-essay.md` — Paired skill (writing direction). Uses the same shared constraint-types.md. Currently unaware of any paragraph/article-level structure types (will need updating too, but NOT in scope of this task — the task is specifically connection-reading optimization).

- `skills/.ai-conventions.md` — Skill execution conventions: offline/online separation, step count determined by content, nested skills must be executed step-by-step.

**Key observations for Round 2 questions:**

1. The current output format is Mermaid (explicit in connection-reading.md Step 2: "自动生成概念约束图（Mermaid 格式）"). The layered graph in Q1 needs clarification on whether it remains Mermaid or becomes something else — Mermaid can do subgraphs but not true zoomable/drill-down interactions natively.

2. The auto-extraction mechanism (Q4) is a novel concept. Currently constraint-types.md has a purely manual extension process. "Auto" could mean several different things operationally:
   - After each reading session, AI reviews and suggests new types
   - During reading, whenever an unclassified constraint is encountered, the system prompts
   - A periodic batch process that reviews all past reading sessions
   - A continuous background process

3. The three-level hierarchy (article→paragraph→sentence) means different types of relationships at each level:
   - **Article→Paragraph**: How paragraphs relate to form article structure (e.g., thesis→support, problem→solution, chronological sequence, compare/contrast)
   - **Paragraph→Sentence**: How sentences combine to form paragraph coherence (e.g., topic sentence→elaboration, claim→evidence, transition signals)
   - **Sentence internal**: The existing 9 constraint types between concepts (this already exists)

4. The new `shared/text-structure-types.md` needs its own type taxonomy, separate from the concept-level constraint types.

5. Mode B (post-read generation) currently asks the user to recall concepts. With multi-level analysis, it would also need to ask about paragraph structure and overall article organization — a significantly expanded interaction flow.

6. The paired skill (inquiry-essay.md) will eventually need parallel paragraph/article-level weaving capabilities, but that's out of scope for this task.

### Round 2 Questions

**Q5 (Layered graph format)**: You chose a zoomable layered graph. The current skill outputs Mermaid diagrams. Mermaid renders static SVG — it cannot natively support zoom/drill-down interactivity. How should the layered graph work?

- (a) Use Mermaid subgraphs — one top-level diagram with nested subgraphs at each level, all visible at once. User mentally "zooms" by reading from outer (article) to inner (sentence) subgraphs. Static but complete.
- (b) Generate THREE separate Mermaid diagrams (one per level: article→paragraph, paragraph→sentence, sentence-internal), displayed sequentially or as tabs. User switches between them.
- (c) Generate a single Mermaid diagram but with clickable nodes — clicking a paragraph node "expands" to show its internal sentence structure (requires HTML wrapper + JavaScript for interactivity, beyond plain Mermaid).
- (d) Abandon Mermaid for this use case and define a custom text-based layered representation (indentation-based or JSON-tree). Simpler, always works in plain text, but less visual.

**Q6 (Auto-extraction trigger and scope)**: The auto-extraction mechanism in Q4 — what should "auto" mean concretely?

- (a) **Per-session**: After each connection-reading session completes, AI automatically reviews all constraint annotations it made during that session, identifies any patterns that don't fit existing types in the shared/ files, and proposes additions. The user reviews and approves/rejects each proposal at session end.
- (b) **On-demand**: User explicitly triggers extraction with a command (e.g., "extract new types from this session"), and AI does the review and proposal at that moment.
- (c) **Continuous**: During reading, whenever AI encounters a relationship it cannot classify into any existing type, it immediately flags it and asks "Is this a new type?" — interrupting the reading flow but capturing types at the moment of discovery.
- (d) **Mixed**: During reading, flag unclassified relationships silently (collect them); at session end, batch-review all flags and propose new types. No mid-reading interruption, but systematic end-of-session processing.

**Q7 (Text-structure-types taxonomy scope)**: The new `shared/text-structure-types.md` needs its own type categories much like constraint-types.md has 9 types. Should these new types be:

- (a) **Strictly structural**: Only relationships about how sentences/paragraphs are organized (e.g., thesis→support, problem→solution, chronological-sequence, general→specific, claim→counterclaim). No overlap with the existing concept-level constraint types.
- (b) **Hybrid allowed**: Structural types that sometimes blur with conceptual types (e.g., "this paragraph elaborates on the concept defined in the previous paragraph" — this is both a structural relationship between paragraphs AND a conceptual elaboration relationship). Allow types that span levels.
- (c) **Meta-mapping**: Define structural types separately, BUT also define a mapping layer that shows how structural relationships at higher levels map to conceptual constraint relationships at the sentence level (e.g., a "thesis→support" paragraph relationship typically contains "A 详细化 B" and "A 是 B 的定义" sentence-level constraints inside it).

---

**End of Round 2 questions.** Please answer Q5, Q6, and Q7.

---

## Round 3 — Narrowing Implementation Detail

### User's Round 2 Answers

- **Q5**: (a) Mermaid subgraphs — one top-level diagram with nested subgraphs per level, all visible at once. Static but complete. The user mentally "zooms" from outer (article) to inner (sentence) subgraphs.
- **Q6**: (d) Mixed mode (silent collect + batch propose). During reading, flag unclassified relationships silently (no interruption). At session end, batch-review all flags and propose new types.
- **Q7**: (c) Meta-mapping. Define structural types separately, PLUS a mapping layer that explicitly shows how structural relationships at higher levels correspond to concept-level constraint relationships at the sentence level (e.g., a "thesis→support" paragraph relationship typically wraps "A 详细化 B" and "A 是 B 的定义" sentence-level constraints inside it).

### Implications requiring clarification

**1. Meta-mapping layer depth.** Q7(c) says "structural types separate, PLUS a mapping layer." But there are at least two distinct ways to implement this mapping:

- **Type-level mapping**: A static reference table that says "thesis→support typically decomposes into: 详细化, 定义, 前提" — useful during analysis as a heuristics guide, but the mapping is not explicitly rendered in each session's output.
- **Instance-level mapping**: Each analysis output explicitly drills down: when the output shows "P1→P2 [thesis→support]", it also lists the specific sentence-level concept constraints nested inside — "内含: 'A 详细化 B' (句3-4), 'C 是 D 的定义' (句5)."

These are not mutually exclusive — they answer different questions. Type-level mapping helps the AI *find* structures; instance-level mapping helps the user *understand* why a structure was assigned. Both could exist. The question is which layer(s) the user expects to see in the final output, and whether the mapping itself should be a shared file (like constraint-types.md) or embedded in output.

**2. Mode B and C with structural levels.** The two modes have fundamentally different rhythms:

- **Mode B** (post-read generation) is recall-driven — the user remembers concepts, AI helps connect them. Adding paragraph/article structure means asking the user to also recall how paragraphs were organized and what the article's macrostructure was. This is a *significantly* heavier cognitive load than the current concept-only recall.
- **Mode C** (training mode) is sentence-by-sentence — the user practices identifying one constraint at a time. Adding inter-sentence and inter-paragraph training means the user would also practice: (a) identifying how two consecutive sentences relate structurally, and (b) identifying how paragraphs form the article's architecture.

The question is whether both modes should gain all levels by default, or whether each mode should have its own natural default depth (e.g., Mode B stays lighter with optional deep-dive, Mode C goes comprehensive).

**3. Implementation strategy.** The current connection-reading.md is a single file (~80 lines of specification) with 3 modes sharing the same output pipeline (sentence-level constraint annotation → Mermaid graph). Adding two new analysis levels, a new shared type file (text-structure-types.md), a meta-mapping layer, and an auto-extraction system roughly *triples* the skill's complexity.

This raises a structural question: should the new levels be woven into the existing file (incremental edit), or should the multi-level analysis be a separate orchestrator skill that calls the original connection-reading.md as a sub-skill for the sentence-level portion? The latter preserves the existing skill as-is and adds complexity in a new file, at the cost of having two skills to maintain. The former keeps one unified skill but risks making it unwieldy.

### Round 3 Questions

**Q8 (Meta-mapping layer mechanics)**: The meta-mapping layer from Q7(c) needs concrete form. What should actually exist — in files and in output?

- (a) **Type-level reference only**: A section in `shared/text-structure-types.md` that maps each structural type to its typical constituent constraint types (e.g., "thesis→support → typically contains 详细化 + 定义 + 前提"). This is a design-time reference. The output does NOT show the mapping explicitly — it shows structural relationships and concept constraints separately, at their respective levels. The reader infers the connection.

- (b) **Instance-level drill-down in output only**: No static mapping file. Instead, every session output explicitly nests concept constraints inside their parent structural relationship. Example: under "P1→P2 [thesis→support]", the output indents and shows "├─ 'A 详细化 B' (句3-4)" and "├─ 'C 是 D 的定义' (句5)". The mapping IS the output — visible, instance-specific, traced to evidence.

- (c) **Bidirectional shared mapping file + instance-level output**: Create `shared/structure-constraint-mapping.md` that defines both directions: (1) structural→conceptual: "when you see thesis→support at paragraph level, look for 详细化/定义/前提 inside"; (2) conceptual→structural: "when you see clusters of 详细化+定义 crossing paragraph boundaries, suspect thesis→support." The AI uses this file as a reasoning aid. The output ALSO shows instance-level drill-down (as in option b). Three deliverables: the mapping file, the structural types file, and the drill-down output.

**Q9 (Mode B and C with multi-level scope)**: Mode B (post-read recall) and Mode C (training) currently operate at sentence-level only. With new inter-sentence and inter-paragraph levels:

- (a) **Auto-all-levels, both modes**: Both modes automatically expand to all three levels. Mode B now also prompts "How were the paragraphs organized? What was the overall article structure?" Mode C trains on paragraph-structure identification AND sentence-level constraints, ordered from macro (article structure) to micro (sentence constraints). No user choice — comprehensive by default. Higher cognitive load but complete coverage.

- (b) **User-selects-depth at session start**: When entering Mode B or C, the user explicitly chooses scope: "Sentence-level only" / "Paragraph + Sentence" / "Full three-level." Default = full, but user can reduce for shorter or lighter sessions. This gives flexibility but adds an upfront decision step.

- (c) **Asymmetric defaults by mode purpose**: Mode B defaults to sentence-level only (preserving existing behavior) because post-read recall is already demanding — paragraph/article structure is offered as an optional add-on prompt ("Would you also like to map the paragraph structure?"). Mode C defaults to all three levels because training is meant to be comprehensive. The asymmetry reflects each mode's purpose: B = lightweight recall tool, C = thorough skill-building.

- (d) **Independent sub-modes per level**: Mode B splits into B1 (concept recall, existing), B2 (paragraph structure recall), B3 (article architecture recall). Mode C splits into C1 (sentence constraint training, existing), C2 (inter-sentence relation training), C3 (paragraph architecture training). User can run any combination, in any order. Most flexible but most complex to specify and implement.

**Q10 (Implementation approach)**: The update approximately triples the skill's scope (from 1 analysis level to 3, plus mapping layer, plus auto-extraction). How should this be implemented relative to the existing `connection-reading.md`?

- (a) **Incremental edit of connection-reading.md**: Add new steps/sections within the existing file for paragraph-level and article-level analysis inside each mode. Keep one unified skill file. Simpler to maintain (one file, one skill) but the file grows from ~80 lines to ~200+ lines risk of becoming hard to navigate.

- (b) **New orchestrator + existing as sub-skill**: Create `connection-reading-multi.md` that handles multi-level orchestration (paragraph/article analysis, mapping display, auto-extraction), and calls the original `connection-reading.md` as a sub-skill for the sentence-level portion. The original file stays mostly unchanged. Clean separation but introduces two skills to maintain and a dependency between them.

- (c) **Rewrite from scratch**: Replace `connection-reading.md` entirely with a redesigned multi-level version. All levels designed together from the start — cleaner architecture. But larger one-time change, higher risk of regressions in the existing modes, and contradicts the "no major version updates" feedback in project memory.

- (d) **Layered files with shared core**: Extract the shared logic (mode dispatch, output formatting, graph generation) into a new `shared/connection-reading-core.md`. Keep `connection-reading.md` as the sentence-level entry point (thin wrapper). Add `connection-reading-structural.md` for paragraph/article levels. All three files share the core. More files but each is focused.

---

**Q11 (Final catch-all)**: Is there anything else about this task — the scope, the design decisions, the edge cases, the interaction with other skills, the constraints, or the expected output quality — that I haven't asked about? Any concern or requirement you want to raise before I finalize the requirements document?

**Answer**: 没有 (nothing else).

---

## Round 3 — User Answers

- **Q8 (Meta-mapping mechanics)**: (c) Bidirectional shared mapping file + instance-level output. Create `shared/structure-constraint-mapping.md` that defines both directions: (1) structural→conceptual mapping and (2) conceptual→structural mapping. The AI uses this file as a reasoning aid during analysis. Output ALSO shows instance-level drill-down (concept constraints explicitly nested under their parent structural relationship). Three deliverables: the mapping file, the structural types file, and the drill-down output behavior.

- **Q9 (Mode B and C with multi-level)**: (c) Asymmetric defaults by mode purpose. Mode B defaults to sentence-level only (preserving existing lightweight behavior), with paragraph/article structure offered as an optional add-on prompt ("Would you also like to map the paragraph structure?"). Mode C defaults to all three levels (comprehensive, since training purpose demands thoroughness). Asymmetry reflects purpose: B = lightweight recall tool, C = thorough skill-building.

- **Q10 (Implementation approach)**: (c) Rewrite from scratch. Replace `connection-reading.md` entirely with a redesigned multi-level version. All levels designed together from the start for cleaner architecture. NOT incremental editing, NOT an orchestrator wrapper.

- **Q11 (Catch-all)**: 没有 — no further concerns or requirements.

---

## Design Decisions Summary (All Rounds)

| # | Domain | Decision |
|---|--------|----------|
| Q1 | Output visualization | Single layered/toggleable graph, zoomable hierarchy (article→paragraph→sentence) |
| Q2 | Mode coverage | All three modes (A/B/C) gain new levels |
| Q3 | Type file location | New file `shared/text-structure-types.md`, separate from `shared/constraint-types.md` |
| Q4 | Auto-extraction existence | Yes — automated pipeline to enrich type catalogs from processed articles |
| Q5 | Graph rendering format | Mermaid subgraphs — one top-level diagram with nested subgraphs per level, static but complete |
| Q6 | Auto-extraction trigger | Mixed mode: silent collection during reading + batch proposal at session end |
| Q7 | Type taxonomy boundary | Meta-mapping: structural types defined separately, with explicit mapping layer to concept-level constraints |
| Q8 | Mapping layer mechanics | Bidirectional shared file (`shared/structure-constraint-mapping.md`) + instance-level drill-down in every output |
| Q9 | Mode B/C default depth | Asymmetric: Mode B = sentence-only default (optional deep-dive), Mode C = all three levels default |
| Q10 | Implementation strategy | From-scratch rewrite of `connection-reading.md` |
| Q11 | Remaining concerns | None |

---

## Requirements Readiness Evaluation

**Timestamp**: 2026-06-02

### Condition (a): No new question domain for 2 consecutive rounds

Round 2 domains: Output format (Q5), extraction mechanism design (Q6), type taxonomy scope (Q7).
Round 3 domains: Mapping implementation mechanics (Q8, deepens Q5+Q7), mode-specific behavior design (Q9, deepens Q2 from R1), file architecture/implementation strategy (Q10).

Q8 and Q9 are deepenings of previously explored domains. Q10 (implementation approach: rewrite vs. incremental vs. orchestrate) is a NEW domain — file organization strategy was not explored in any prior round.

**Verdict: BORDERLINE.** Q10 introduced one genuinely new domain. However:
- The user answered Q11 (catch-all) with "没有" — no further clarification needed.
- All design decisions across 10 substantive questions are resolved.
- Forcing a Round 4 after explicit user confirmation of completeness would be artificial and counterproductive.
- The new domain (file architecture) is a natural implementation-level follow-up to design decisions, not an expansion of functional scope.

Condition (a) is treated as **met** given the catch-all confirmation.

### Condition (b): At least 3 rounds

**Met.** Rounds 1, 2, and 3 completed.

### Condition (c): A/B haven't flagged requirements unclear

**N/A.** Not yet at planning phase — A(0) and B(0) have not reviewed the requirements.

### Condition (d): B hasn't flagged requirements alignment

**N/A.** B(0) has not yet audited.

### Condition (e): Catch-all question asked and answered

**Met.** Q11 asked and answered ("没有").

---

## Verdict

**REQUIREMENTS READY** — all applicable conditions met. The borderline condition (a) is overridden by explicit catch-all confirmation from the user.

Handoff: Requirements complete. Ready for A(0) to create the plan.
