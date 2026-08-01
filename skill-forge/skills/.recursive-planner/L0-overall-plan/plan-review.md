# Plan Review — connection-reading 多层级优化

**Reviewer**: B(0) | **Date**: 2026-06-02 | **Verdict**: PASS

---

## 9-Point Audit Results

### #1: Completeness — PASS

The plan covers all 10 design decisions from the 3-round requirements process:

| Decision | Plan Step | Status |
|----------|-----------|--------|
| Q1: Layered/toggleable graph | Step 3 (Mermaid nested subgraphs) | Covered |
| Q2: All three modes gain levels | Step 4 sub-steps 2A, 2B, 2C | Covered |
| Q3: New text-structure-types.md | Step 1 | Covered |
| Q4: Auto-extraction pipeline | Step 4 sub-step 2D | Covered |
| Q5: Mermaid subgraphs (static, complete) | Step 3 | Covered |
| Q6: Mixed mode (silent + batch) | Step 4 sub-step 2D | Covered |
| Q7: Meta-mapping (separate + mapping) | Step 2 | Covered |
| Q8: Bidirectional file + instance-level drill-down | Step 2 (mapping file) + Step 3 (output format) | Covered |
| Q9: Asymmetric defaults (B=sentence, C=all) | Step 4 sub-steps 2B, 2C | Covered |
| Q10: Rewrite from scratch | Step 4 | Covered |

The plan also covers: shared data layer structure, offline/online separation, supplementary rules, Mermaid limitation workarounds, large-article handling, edge cases, and pairing compatibility verification. No gaps identified.

### #2: Feasibility — PASS

Every step is within AI capabilities:
- Steps 1-3: Writing structured markdown files with tables, taxonomies, and format specifications — trivially feasible.
- Step 3: Designing Mermaid `flowchart TB` syntax with nested subgraphs — well-documented, stable syntax. No custom rendering required.
- Step 4: Rewriting a markdown skill file (~300 lines) following established conventions — feasible, albeit the most complex step (flagged as HIGH risk with mitigations).
- Step 5: Cross-reference verification — read-only check against existing files.

No step requires capabilities beyond AI's current abilities (no code execution, no external API calls, no binary processing). All steps operate exclusively on markdown files.

### #3: Methodology Correctness — PASS

The step order follows professional practice for designing a structured analysis system:

1. **Define types** (Step 1) — foundation layer, establishes taxonomy before anything references it
2. **Map between type systems** (Step 2) — bridge layer, connects the new structural taxonomy to the existing conceptual taxonomy
3. **Design output format** (Step 3) — presentation layer, defines how analysis results are rendered
4. **Implement skill** (Step 4) — integration layer, weaves types + mapping + format into a coherent operational procedure
5. **Verify** (Step 5) — quality gate, ensures all artifacts are consistent and conformant

This mirrors standard software design methodology (data model → mapping/API → UI → implementation → testing) and linguistic annotation pipeline design (taxonomy → inter-annotator framework → output specification → pipeline → validation).

Step 1 correctly references established academic frameworks (RST by Mann & Thompson, FARS by Golebiowski, PEEL/TEEL, Hyland's metadiscourse) as its intellectual foundation. The taxonomy boundaries (sentence-level concepts vs. paragraph/article-level structure) are cleanly separated, avoiding category confusion.

### #4: Dependency Clarity — PASS

All inter-step dependencies are explicit and correctly reasoned:

```
Step 1 (no dependencies)
  ├──→ Step 2 (needs Step 1 structural type names)
  └──→ Step 3 (needs Step 1 structural type labels)
         │
         └──→ Step 4 (needs Steps 1+2+3 outputs)
                └──→ Step 5 (needs Step 4 output)
```

Verification of parallelism claim: Steps 2 and 3 both depend only on Step 1. Step 2 defines conceptual-to-structural mappings (text-based); Step 3 defines visual output format (Mermaid-based). They share no outputs and neither depends on the other. The parallelism claim is valid — these can execute concurrently after Step 1 completes.

Step 4's dependency on all three prior steps is correct: the skill rewrite must reference type names (Step 1), use mapping guidance (Step 2), and follow output format (Step 3). No hidden circular dependencies.

### #5: Quantifiable Acceptance Criteria — PASS

All steps have specific, measurable "done" criteria:

- **Step 1**: 24 types minimum (12 per level), each with 4 required fields, extension mechanism present, >=3 quality metrics — all numeric or binary checks.
- **Step 2**: All 24 types mapped with >=2 constraint types each, >=6 inference rules, confidence levels present, unambiguous format spec — all verifiable.
- **Step 3**: Valid Mermaid syntax, 3 distinguishable levels, complete conventions table, per-mode conventions, large-article rule, limitation workarounds — all operationalizable.
- **Step 4**: 12 specific criteria covering format validity, structural completeness, mode specification, extraction procedure, defaults correctness, convention compliance — all binary or checklist verifiable.
- **Step 5**: 5 criteria covering cross-references, pairing, conventions, edge cases, and report output — all verifiable.

Observation (non-blocking): Step 3 criterion "Three levels are visually distinguishable" is somewhat subjective. Consider adding a concrete sub-criterion: "Each level uses a distinct border color (blue/green/orange as specified) and distinct node shape, such that a reader can identify which level a node belongs to without reading labels." Not required for PASS — the visual conventions table already provides this specificity.

### #6: Risk Identification — PASS

9 risks identified across all severity levels, each with specific mitigation:

- 3 MEDIUM risks (taxonomy incompleteness, diagram readability, file bloat, regression) — all have concrete mitigations (extension mechanism, >8-paragraph collapse rule, externalization to shared files, preserved sentence-only default).
- 4 LOW-MED risks (mapping opinionation, context overload for A(0), auto-extraction false positives) — mitigated by confidence indicators and user-approval gates.
- 2 LOW risks (intrusive prompt, overwhelming training) — mitigated by one-time prompt and progressive reveal.

The HIGH risk on Step 4 (file complexity) is well-analyzed with three sub-risks and corresponding mitigations. The risk table is thorough and actionable.

### #7: User Requirements Alignment — PASS

All Q1-Q10 decisions are directly addressed (see #1 completeness table above). Additionally:

- The "no major version updates" feedback in project memory is acknowledged in Step 4 — but correctly overridden per the user's explicit Q10(c) choice (rewrite from scratch). The user's explicit instruction takes precedence over memory feedback.
- The meta-mapping implementation (Q8(c)) is fully specified: bidirectional static file (Step 2) + instance-level drill-down in output (Step 3 format conventions + Step 4 sub-step 2A item 6).
- Asymmetric defaults (Q9(c)) are correctly implemented: Mode B preserves existing sentence-only behavior with opt-in deep-dive; Mode C defaults to all three levels with progressive reveal.
- Auto-extraction (Q6(d)) is correctly specified as silent collection with >=3 item threshold and end-of-session batch proposal.

### #8: Context Safety — PASS

Dedicated context safety analysis (plan Section 4):

- Per-step context budgets estimated: 4K-12K tokens per sub-agent — all well within current AI context limits (200K+ tokens).
- Total plan-level context: ~28K tokens across all agents — safe.
- Cross-contamination prevention: Steps 1-3 each write a different new file; Step 4 reads but does not modify Steps 1-3 outputs; Step 5 is read-only verification. No two steps write to the same file.
- File ownership is clear: Step 1 owns text-structure-types.md, Step 2 owns structure-constraint-mapping.md, Step 3 produces a format specification (template reference), Step 4 owns connection-reading.md.

Observation (non-blocking): The Step 4 context estimate of ~12K tokens may be optimistic. When the sub-agent loads all three shared files + existing connection-reading.md + inquiry-essay.md + .ai-conventions.md + the plan itself, the context could reach ~18K-22K tokens. This is still well within limits (>200K). No action required.

### #9: Skill Utilization — PASS (pending B(0) independent verification)

A(0) conducted a skill search (documented in state.json) and found:
- **skill-creator:skill-creator** (installed) — applicable, referenced in Steps 1-4's "Required resources/tools."
- **knowledge-graph** (726 installs) — rejected, reasonable judgment (indirect benefit; task is writing spec files, not implementing graph engines).
- **argument-audit** (27 installs) — rejected, reasonable judgment (low install count, insufficiently battle-tested).

A(0)'s search and rejection rationales are reasonable. The skill-creator is appropriately used for post-write optimization in Steps 1-4.

B(0) will independently run find_skills after this review to confirm no applicable skills were missed.

---

## Verdict: PASS

All 9 audit standards pass. The plan is comprehensive, well-structured, methodologically sound, and directly addresses all design decisions from the 3-round requirements process. Dependencies are explicit, risks are identified with mitigations, acceptance criteria are measurable, and context safety is analyzed.

The plan is ready for execution. Handoff to C(0) for scheduling.

---

## Observations for Execution (Non-Blocking)

These are notes for A(0) and sub-agents during execution — not defects, but awareness items:

1. **Step 3 Mermaid validity verification**: Criterion #1 requires the template to parse correctly. The executing agent should copy-paste the generated Mermaid into a live renderer (mermaid.live or equivalent) to confirm validity, not just visually inspect the syntax.

2. **Step 4 mode interaction clarity**: When Mode B's optional deep-dive path and Mode C's macro→micro training are both specified in one file, use clear visual separators (horizontal rules, subsection headers) to prevent the reader from confusing the two flows. The plan mentions this as a mitigation but does not prescribe a specific formatting convention.

3. **Step 1 type count flexibility**: The plan specifies "24 types minimum." If research during execution reveals additional well-motivated types beyond the 24 listed, adding them is within scope — the extension mechanism is designed for this. But the agent should not add types merely to inflate the count; each addition must be traceable to a genuine structural pattern in academic/argumentative writing.

4. **Old connection-reading.md backup**: The rewrite in Step 4 completely replaces the existing file. Git will preserve history, but the executing agent should note that the old version's metadata header (id, slug, created date) should be preserved in the new file to maintain skill continuity.
