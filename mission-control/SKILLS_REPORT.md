# Skill Report — All 25 teach-* Learning Projects

**Generated:** 2026-09-06
**Scope:** `C:\Users\61602\teach-*` (25 projects — 2 added since the 2026-08-13 report: `teach-Introduction-to-Computing-B`, `teach-linear-algebra`. The `teach-regex` directory exists but is an empty scaffold created 2026-09-02 with no content, so it is excluded.)
**Methodology:** Exhaustive file reading of MISSION.md, NOTES.md, learning records, code files, HTML lessons, and reference materials from every project (25 parallel project audits, 2026-09-06). Proficiency assessments are evidence-based — citations drawn directly from artifacts produced. Where a project records no hours on disk, figures are estimates carried from session history and flagged accordingly.

---

## 1. Skill Inventory — Per Project

### teach-Agent (AI Agents)
| Field | Detail |
|---|---|
| **Domain** | AI Agents — ReAct agent loop, function/tool-calling protocol, tool schema design, guardrails, agent system-prompt design |
| **Skill level** | Intermediate — reads/traces a Python agent loop end-to-end, diagnoses which of 4 layers (prompt / tool schema / loop+guardrails / data structure) a bug lives in, and designs agent system prompts; reading fluency > writing (coding exercises scaffolded). Track complete. |
| **Concrete skills** | Traces a ReAct loop (Thought→Action→Observation) through response, messages, tools, and guardrails; diagnoses bugs across 4 layers and proposes correct fixes; maps each guardrail (timeout, max_steps, context threshold, malformed JSON, duplicate calls, tool exceptions, force_final_answer) to the failure it prevents; designs system prompts over the five questions (identity / tools / thinking style / stopping cues / negative guidance); understands tool-calling protocol and schema design incl. `.` vs `[]` data-access tracing; applies a "draw the data structure before reading code" debug technique — found and fixed 3 structural bugs in course materials |
| **Hours invested** | ~8 hours (one-day sprint, 2026-07-19) |
| **Completion** | 100% — completed. All 5 lessons + data-structure deep-dive + coding practice finished before the 2026-07-20 internship start; every MISSION success criterion met. Unchanged since the 08-13 report; a planned follow-on track (record 0007) was never written. |
| **Key evidence** | `learning-records/0006-track-complete.md`; `learning-records/0004-robust-agent-loop.md`; `learning-records/0005-prompting-strategies.md`; `lessons/0005-coding-practice.html` |

### teach-andrej-karpathy-zero-to-hero (Deep Learning)
| Field | Detail |
|---|---|
| **Domain** | Deep Learning / neural networks — Karpathy's Zero to Hero (micrograd → makemore → GPT), PyTorch |
| **Skill level** | Beginner — read and understood micrograd `engine.py` (autograd Value class, backward pass, topological sort); no independent implementation written from scratch |
| **Concrete skills** | Understands the micrograd autograd engine (Value class, gradient accumulation, `_backward` closures, topological-sort backward pass); explains backpropagation / chain-rule gradient flow on computation graphs; working familiarity with deep-learning fundamentals from the Zero to Hero framing |
| **Hours invested** | ~3 hours |
| **Completion** | 13% (paused) — only milestone 1 of 8 (micrograd) complete; makemore P1–P5, GPT tokenizer, GPT from scratch all pending; README frontmatter `status: paused` |
| **Key evidence** | `README.md`; `resources/micrograd.md` |

### teach-CPA-JJF (CPA Economic Law)
| Field | Detail |
|---|---|
| **Domain** | CPA 经济法 (Chinese Economic Law) — understanding-oriented legal study, not exam prep |
| **Skill level** | Advanced beginner — decomposes legal scenarios via a 6-step analysis template and re-expresses law as Python OOP models (law = class, legal act = `__init__`, 位阶 = MRO); co-authored lesson content and caught genuine errors in teaching material |
| **Concrete skills** | 6-step legal scenario decomposition (is-it-law → rank → subjects → object → rights/obligations → trigger); classifies civil legal acts by validity tier (无效/无效但可撤销/可撤销/效力待定) with underlying rationale (e.g., 公序良俗 ≠ 违法; why the fraudster cannot rescind); re-expresses legal structure as precise Python OOP validity models (`is_active()` branches); explains the 法人 limited-liability "wall" and why 非法人组织 exists; distinguishes 法律事实 event-vs-act by the actor's will and 民事法律行为 vs 事实行为 by actor intent; two-way memorization-understanding pedagogy |
| **Hours invested** | ~10 hours |
| **Completion** | 15% (active) — Cycle 1 法律基础 is 5 of 7 lessons through (0001–0005 passed incl. civil legal acts); lessons 0006 代理 and 0007 诉讼时效, the Cycle-1 case exam, then Cycles 2–5 (23 lessons + 4 exams) remain. No session recorded since 2026-08-02. |
| **Key evidence** | `learning-records/0008-lesson-0005-passed.md`; `learning-records/0007-lesson-0004-passed.md`; `lessons/0005-civil-legal-acts.html`; `NOTES.md` |

### teach-cs61a (CS Fundamentals)
| Field | Detail |
|---|---|
| **Domain** | UC Berkeley CS61A — Python programming fundamentals (functions, recursion, sequences, objects, interpreters, SQL) |
| **Skill level** | Intermediate — implemented both full CS61A projects (Hog dice game, Cats typing game) passing all ok-autograder questions; fluent in higher-order functions, closures, recursion; authored an original "portal model" of frame-tree program execution |
| **Concrete skills** | HOFs / closures / function factories (Weeks 1–2, HW01–02, lab02); recursion incl. mutual/tree recursion and memoization (Week 3, HW03, lab03); Hog (390-line `hog.py`) and Cats (508-line `cats.py`) passing all ok-autograder tests; TDD via ok-autograder + pytest with coverage; original abstract model-building of program execution (Portal Model, 231-line doc); string/list processing and algorithm design |
| **Hours invested** | ~30 hours |
| **Completion** | 30% (active) — Weeks 1–3 of 10 complete (Hog + HW01–03 + labs); Week 4 (Sequences) next. Progress is tracked only in README.md; on-disk lab04/lab05 dirs are not yet reflected in the checklist. No recorded activity since ~mid-August. |
| **Key evidence** | `README.md`; `resources/hog/hog.py`; `resources/cats/cats.py`; `resources/comprehension-view-portal-model.md` |

### teach-database (SQL/SQLite)
| Field | Detail |
|---|---|
| **Domain** | SQLite / SQL — read and query a production `.db`, indexes, FTS5 |
| **Skill level** | Intermediate — from absolute zero on 07-22 to independently querying a 21-table production schema (Hermes state.db) from memory by 07-24; understands execution plans and FTS5 virtual tables. Course complete. |
| **Concrete skills** | SQLite CLI fluency (`.tables`, `.schema`, dot-commands); SELECT/WHERE/ORDER BY/LIMIT/JOIN/GROUP BY/aggregates and LIKE/GLOB from memory; reading CREATE TABLE schema (PK, FK, types); regular index vs FTS5 virtual table (interface vs engine) with MATCH and EXPLAIN QUERY PLAN; querying a real production database without reference; self-derived mental models (no-GROUP-BY two modes; virtual tables as encapsulated storage backends) |
| **Hours invested** | ~5 hours (2 days: 07-22, 07-24) |
| **Completion** | 100% (completed) — 5/5 lessons; all 5 MISSION goals met; user declared ready to return to the Hermes memory-architecture track. Unchanged since 08-13. |
| **Key evidence** | `learning-records/0008-course-complete.md`; `learning-records/0007-virtual-table-mental-model.md`; `learning-records/0006-no-group-by-two-modes.md`; `lessons/0005-indexes-fts5.html` |

### teach-deep-learning-book (DL Theory)
| Field | Detail |
|---|---|
| **Domain** | Reading Goodfellow's "Deep Learning" sequentially with per-chapter original mental-model synthesis notes |
| **Skill level** | Intermediate — synthesizes dense math-textbook chapters into original multi-layer mental-model architectures with rigorous notation (MLE ≡ NLL ≡ KL ≡ cross-entropy ≡ ERM, Bayes error, Cramér–Rao, conjugate priors) and concept dependency graphs |
| **Concrete skills** | Linear algebra / matrix-calculus reasoning (eigendecomposition, SVD, PCA); probability & information theory (Bayes, entropy, KL, MLE equivalence chain); numerical computation & gradient-based optimization; ML fundamentals (capacity/bias-variance/estimators, Bayes error, curse of dimensionality, NFL); knowledge synthesis into layered mental-model architectures (ch5 three-layer scaffold covering all 116 concepts); concept-dependency maps and transferable-methodology extraction |
| **Hours invested** | ~16 hours |
| **Completion** | 17% (active) — 4 of 20 chapters: Ch2 linear algebra, Ch3 probability, Ch4 numerical computation, Ch5 ML basics (all distilled into 342–800-line notes); Ch6 deep feedforward networks next; Parts II–III untouched. No recorded activity since 2026-07-02. |
| **Key evidence** | `README.md`; `resources/ch5-machine-learning-basics.md`; `resources/ch4-numerical-computation.md`; `resources/ch3-probability.md`; `resources/ch2-linear-algebra.md` |

### teach-english-learning (English)
| Field | Detail |
|---|---|
| **Domain** | English conversational fluency (target MIT / IELTS 7.5+) — SLA-grounded conversation training, concept-first taught in Chinese |
| **Skill level** | A2–B1 baseline (per MISSION.md) — solid conceptual mastery of the collaborative conversation model; can explain, self-diagnose, analyze real dialogues, and teach it; no confirmed speaking practice yet (practice lesson pending) |
| **Concrete skills** | Explains performance-vs-collaborative model of conversation (being understood, not impressing); identifies own performance-mindset patterns in past conversations (self-diagnosis); analyzes a real conversation for communication strategies (circumlocution, clarification requests, comprehension checks); teaches a newly learned concept (learn-by-teaching / Feynman recall); designs and follows a structured SLA learning system (dependency-graph curriculum, concept lessons in Chinese vs practice in English, per-lesson passing criteria) |
| **Hours invested** | ~4 hours |
| **Completion** | 20% (active) — Cycle 1 step 1 of 5 (Concept) complete: Lesson 0001 passing record exists; Lesson 0002 built but no completion record; Lesson 0003 never created; Practice "First Contact" and the three-tier Exam pending. No activity since 2026-08-09. |
| **Key evidence** | `learning-records/0001-performance-vs-collaborative-model.md`; `lessons/0001-conversation-is-not-performance.html`; `lessons/0002-communication-strategies.html`; `MISSION.md`; `NOTES.md` |

### teach-github-learning (Git/GitHub)
| Field | Detail |
|---|---|
| **Domain** | Git & GitHub via a sequential 42-task checklist (T1–T42), Pro Git + GitHub Docs based |
| **Skill level** | Beginner-to-intermediate — full local + remote workflow fluent (init/commit/branch/merge/push/PR); wrote a deep conceptual mental-model doc; Phases 3–4 (conflicts, stash, rebase, Issues) not yet done |
| **Concrete skills** | Full local git workflow — init/config/add/commit, log flag variants, staged-vs-unstaged diff, amend, restore, .gitignore (T1–T11); branching & merging — create/switch/rename, fast-forward vs 3-way, cleanup via -d/--merged/--no-merged (T17–T22, T25); GitHub remotes + SSH auth — keygen/add, push/pull/fetch/clone, origin/* tracking (T13–T16, T19–T20); full PR lifecycle — push, open, review, merge, delete remote branch, sync (T24); formal git mental model (two areas, one isomorphic graph, three pointer sets, remote-tracking staleness); confusable-command cheat sheet (T1–T25) |
| **Hours invested** | ~15 hours |
| **Completion** | 51% (active) — Phases 1–2 complete: 24 of 42 tasks (T1–T25); next is T26 (merge conflicts) opening Phase 3, then Issues/Projects and the Phase 4 sandbox journal + 15-minute self-test. No work recorded since 2026-07-30. |
| **Key evidence** | `README.md`; `resources/git-mental-model.md`; `resources/git-commands-T1-T25.md` |

### teach-hello-world (World Systems)
| Field | Detail |
|---|---|
| **Domain** | Understanding how world systems work — markets, finance, geopolitics, governance — via a self-built unified interaction model (世界运行规律) |
| **Skill level** | Intermediate — independently builds and applies a unified market model (six-dimension framework + Five Filters compression) and an A/B/C static→strategy→dynamic protocol to real industrial cases (polysilicon/wafer markets), reasoning under limited public data |
| **Concrete skills** | Unified market interaction model — six-dimension (Price/Good/Information/Volume/Rules/Externalities) framework + Five Filters, applied to the 2017 polysilicon market; A/B/C three-stage case protocol (static baseline → quasi-static strategy → dynamic increment + industry-chain tracing); entity-first analysis under limited public data via four reasoning tools (financial-signal, structural, boundary-framing, conditional); falsifiable prediction design under a "stand at the historical scene" anti-hindsight rule; perspective-superposition ontology (market dimensions as emergent across viewpoints, not objective properties); hermeneutic-circle curriculum design with first-principles critique of taxonomy-vs-derivation gaps |
| **Hours invested** | ~12 hours (intense first week: 08-08, 08-09, 08-11, 08-12) |
| **Completion** | 45% (active, open-ended course — hermeneutic circle) — Cycle 1 market subsystem substantially built: lessons 0001–0004 + unified model + A/B/C protocol applied. Next per NOTES.md: Cycle-1 Criterion 2 (re-analysis with the correct policy-segmentation subgraph). No recorded activity since ~08-12/13. |
| **Key evidence** | `reference/polysilicon-market-data.html`; `reference/entity-first-analysis-protocol.html`; `learning-records/0010-market-as-perspective-superposition.md`; `learning-records/0009-abc-analysis-method.md`; `NOTES.md` |

### teach-hermes-agent (Agent Framework)
| Field | Detail |
|---|---|
| **Domain** | Hermes Agent source code — cron scheduling, tool calling, 4-layer memory architecture, FTS5 database design; plus a from-scratch Python mini agent |
| **Skill level** | Intermediate — wrote a working tool-calling agent loop + cron scheduler from memory with zero Hermes deps; reads production framework source (4-layer memory, FTS5 composite-column pattern) with correct mental models |
| **Concrete skills** | From-scratch autonomous agent (3-branch loop + OpenAI-compatible tool calling + JSON persistence; `mini-agent/agent.py`, 142 lines); cron scheduler from memory (parse/load/save/cron_loop; `mini-agent/cron.py`, 98 lines); Python file-I/O fluency via 7 progressive drills; operated Hermes 0.18.2 from source (DeepSeek API); traces the 4-layer memory architecture and FTS5 state.db (composite content column, dual tokenizers, 6 sync triggers); explains session_search's 4 calling modes and the DISCOVERY 3-table JOIN-chain with MATCH/snippet()/rank + input sanitization |
| **Hours invested** | ~20 hours (9 lessons authored + drill practice) |
| **Completion** | 80% (paused) — lessons 0001–0009 on disk, records through 0014 (Layer-2 synthesis: one storage SQLite+FTS5, one tool session_search, one lineage-dedup rule). Track paused 2026-07-24 when the manager redirected to LangGraph (→ teach-langgraph-agent). Completion corrected up from 75% in the 08-13 report to reflect the full authored lesson set. |
| **Key evidence** | `mini-agent/agent.py`; `mini-agent/cron.py`; `learning-records/0014-layer-2-synthesis.md`; `reference/state-db-schema.html`; `NOTES.md` |

### teach-HTML (Frontend/HTML)
| Field | Detail |
|---|---|
| **Domain** | HTML as the first step of the frontend stack (HTML → CSS → JavaScript → Vue), required for an internship |
| **Skill level** | Intermediate — writes a complete, semantically correct multi-page HTML site from memory (skeleton, semantic HTML5, tables with colspan/rowspan, forms); maps form submission to an HTTP request; distinguishes SVG (retained-mode) vs Canvas (immediate-mode). 15/15 lessons + exam complete. |
| **Concrete skills** | Semantic HTML5 documents from memory; complex tables via a strict one-slot-one-owner colspan/rowspan grid model; forms (20+ input types, validation, GET vs POST, enctype) mapped to the browser-composes-an-HTTP-request model; multi-page site structure (relative links, iframes, head glue); HTML5 APIs (Canvas vs SVG, DnD/Geolocation awareness); self-editing — catches structural tag mismatches and stale runoob "fossils" |
| **Hours invested** | ~12 hours (3 sessions, Aug 10–13) |
| **Completion** | 100% (completed) — 15/15 lessons + three-tier exam passed Aug 10–13 (Easy 6/6, Medium 2/2, Hard 1/1); MISSION success criteria 1–4 met; hands off to teach-CSS. A non-blocking forms reference remains a nice-to-have. |
| **Key evidence** | `learning-records/0015-exam-passed.md`; `NOTES.md`; `practice/semantic-blog.html`; `practice/forms-demo.html` |

### teach-Introduction-to-Computing-B (Intro to Computing — Exemption Exam)
| Field | Detail |
|---|---|
| **Domain** | PKU 计算概论B (Intro to Computing, Python) exemption-exam prep — computer-systems fundamentals + exam technique. **New to this report (created ~2026-08-21).** |
| **Skill level** | Advanced — experienced Python/Agent developer (CMO-level math) preparing to exempt an intro course via authentic closed-book past papers; runs full-coverage audits of official courseware and builds exam-specific gap-fill lessons |
| **Concrete skills** | Translated the official PKU syllabus into a milestone-tracked exemption-exam plan (12 numbered learning records); reverse-engineered three years of authentic closed-book Python papers (2021/22/23) into a question-type/weighting map and a 200→170 (85%) pass-line strategy; ran a full-coverage audit extracting all 356 concepts from 12 lectures / 735 pages of official courseware, flagging 102 untaught points triaged 16-high/77-mid/9-low; built and delivered 10 interactive HTML lessons (binary/encoding/CPU/OS/network, flowchart programming, AI/LLM concepts) each with self-verified pass records; reconstructed and ran past-exam Python programs (sliding window, max subarray, myAtoi, prime sieve) against official grading rubrics; built flowchart skill from zero incl. "in-head dry-run" closed-book technique; codified a reusable exam-prep doctrine (exhaustive authoritative-source extraction before any coverage filtering) |
| **Hours invested** | ~25 hours (estimated; not recorded on disk) |
| **Completion** | 70% (paused) — the exemption exam was sat in September 2026 but **not passed**, so the project is now paused (计算概论B itself will be taken for credit this term). Prep work stands as delivered: 7 of 10 lessons verified passed via records, the 356-concept courseware audit + two gap-fill lessons (0009/0010) and AI/LLM lesson (0008), a revised glossary, and a tick-off checklist. All prep assets are retained as reference. |
| **Key evidence** | `MISSION.md`; `learning-records/0012-exam-prep-methodology-overhaul.md`; `learning-records/0011-lesson-0007-passed.md`; `reference/coverage-gap-checklist.md`; `reference/courseware-2021-full-points.md` |

### teach-langgraph-agent (LangGraph)
| Field | Detail |
|---|---|
| **Domain** | LangGraph (StateGraph, ToolNode, checkpointing, streaming) — graph-based agent framework |
| **Skill level** | Intermediate — writes a full 3-file LangGraph agent (state.py / agent.py / main.py) from memory, including a 3-branch router and custom reducer; built an independent 5-node linear-pipeline app (LGA) with real API integration |
| **Concrete skills** | StateGraph from scratch (add_node/add_edge/add_conditional_edges/compile); TypedDict + Annotated reducers (add_messages, custom add_tool_log); 3-branch conditional routers (tools/retry/end) with hand-written tool execution and try/except recovery; self-debugs to zero errors unaided (Exam 0001: 12→3→0 over 3 passes, all 7 self-check cases passed); real-world capstone — 5-node linear-pipeline news-to-daily-report app with API discovery, pagination/cursor, timezone, .env secrets, Chinese JSON (5 region-classification approaches iterated); explains the declarative graph model vs the imperative agent loop and when each fits |
| **Hours invested** | ~12 hours |
| **Completion** | 80% (active) — all 4 MISSION criteria met; lessons 0001–0004 + Exam 0001 + LGA capstone (2026-07-27) complete. Next planned, not started: lessons 0005 Streaming, 0006 Checkpointing, 0007 Parallelism. |
| **Key evidence** | `lessons/0004-tools-and-routing.html`; `hands-on/agent.py`; `learning-records/0003-exam-0001-complete.md`; `learning-records/0004-first-real-world-project-lga.md`; `NOTES.md` |

### teach-linear-algebra (Linear Algebra / 高等代数)
| Field | Detail |
|---|---|
| **Domain** | Linear algebra / 高等代数 — rigorous theory spine for PKU 数院 英才班 with conceptual deep-learning binding. **New to this report (created ~2026-08-27).** |
| **Skill level** | Advanced (theory, freshly acquired, not yet exam-tested) — states and proves core results closed-book, and binds DL artifacts to the spine conceptually (PCA=SVD, backprop=adjoint, least squares=regression loss, conditioning=training stability) |
| **Concrete skills** | States and proves core results — rank-nullity, invertible-matrix theorem, spectral theorem, SVD, diagonalization, determinant theory, Rayleigh quotient, conditioning — each passed via a 6-act passbar (compute by hand, prove, DL-bind, closed-book map-patch); operates an "interaction-as-dictionary" modeling framework — authored the adopted final 9-dimension dictionary (199 canonical terms + 370 interaction edges) as course-root HTML; derives DL artifacts conceptually from the spine rather than recalling them (affine layers, embeddings/inner-product similarity, PCA=SVD, least squares=regression loss, backprop=adjoint/transpose, low-rank, conditioning=training stability); numerical-linear-algebra reasoning (forward error ≤ κ·backward error, never form AᵀA, distance-to-singularity = σ_min = 1/κ, fp16/bf16 precision budgets); self-directed retrieval discipline (closed-book after every dive, self-pass on own word, interleaved anti-massing design with 15-min-flag cap); navigates authoritative Chinese 高等代数 sources (谢启鸿 白皮书, OCR'd) tagging every problem to the 9-dimension map; numpy computation fluency (row reduction, inverse, least squares, eigenvalues, diagonalization) |
| **Hours invested** | ~50 hours (estimated; not recorded on disk) |
| **Completion** | 40% (active) — Phase 1 (concept acquisition) complete: 25 HTML lessons covering all 33 content nodes, both "master questions" crowned (least-squares 0008, SVD 0017), through conditioning (lesson 0026 / pass record 0027, 2026-09-06); learner-map v3.0 (9-dimension dictionary) adopted FINAL same day (record 0028). Phase 2 (daily interleaved problem bank riding the PKU course, started ~09-05) launched 2026-09-06: operating rules + week-01 menu authored, no problems logged yet. |
| **Key evidence** | `learning-records/0028-map-v3-final-9dimension-dictionary.md`; `NOTES.md`; `reference/learner-map.md`; `terms-by-dimension.html`; `phase2/README.md` |

### teach-mit-6s184 (Diffusion Models)
| Field | Detail |
|---|---|
| **Domain** | MIT 6.S184 — Flow Matching & Diffusion Models (generative AI / deep learning) |
| **Skill level** | Beginner — read pp.1–18 of the lecture notes and drafted an analogy-based explanation of generative modeling as sampling (mountain story); no labs, no code written |
| **Concrete skills** | Read and summarized a technical ML lecture-notes PDF (generative modeling via SDEs / flow matching); explained generative-modeling-as-sampling through an original 4-section Chinese mountain-analogy story; structured a self-study course project with frontmatter + 7-chapter/3-lab syllabus checklist; scoped the course and self-identified prerequisite gaps, pausing rather than proceeding unprepared |
| **Hours invested** | ~4 hours |
| **Completion** | 2% (paused) — 0/7 chapters, 0/3 labs; only pp.1–18 read (2026-07-30); README frontmatter `status: paused` — prerequisite gap (deep-learning basics) identified |
| **Key evidence** | `README.md`; `resources/lecture_notes.pdf` |

### teach-naked-economics (Economics)
| Field | Detail |
|---|---|
| **Domain** | Reading Charles Wheelan's "Naked Economics" via connection-based reading — per-chapter bilingual sentence annotation + concept-constraint graphs |
| **Skill level** | Advanced (analytical depth) / Beginner (breadth — only 1 of 14 chapters) — produced sentence-level 3-layer structural analysis of a full English chapter (157 sentences, 18 sections) with constraint-typed Mermaid concept-constraint graphs |
| **Concrete skills** | 3-layer text-structure analysis (sentence → paragraph → article) with constraint-typed relation tagging; bilingual EN–CN sentence-by-sentence annotation of a full chapter (157 sentences, 18 sections); Mermaid concept-constraint graphs of economics concepts (adverse selection, asymmetric information, signaling, lemon markets, death spiral); interactive zoomable HTML concept graph; systematic connection-reading methodology (read → redraw the concept-constraint graph from memory) |
| **Hours invested** | ~15 hours (on a single chapter) |
| **Completion** | 7% (paused) — Ch5 Economics of Information complete; 13 chapters + epilogue unchecked; paused since 2026-06-21 per frontmatter |
| **Key evidence** | `README.md`; `resources/ch05-structural-analysis.md`; `resources/ch05-section1-full-structure.md`; `resources/ch05-graph.html` |

### teach-openclaw-companion (Backend Development)
| Field | Detail |
|---|---|
| **Domain** | Backend for OpenClaw Companion, a Windows desktop AI assistant — FastAPI + async SQLAlchemy + LangGraph + MCP + SSE (RAG/scheduler/multi-agent/frontend pending) |
| **Skill level** | Intermediate — writes and debugs a real FastAPI + LangGraph + MCP backend by hand (async SSE streaming pipeline, MCP subprocess lifecycle, async SQLAlchemy); self-diagnoses recall errors clustering in SQLAlchemy type names and HTTP method mapping |
| **Concrete skills** | FastAPI + Pydantic + async SQLAlchemy REST backend (CRUD routers, schemas, DI, lifespan, async engine) verified via from-memory retrieval rewrite; SSE streaming agent-response pipeline (POST+SSE split, asyncio.Queue producer/consumer, async generator, `is_disconnected`) in `chat.py`; LangGraph orchestration (StateGraph, MemorySaver, ToolNode, astream_events token streaming) in `graph.py`; MCP protocol + Python SDK subprocess lifecycle (JSON-RPC 2.0 stdio spawn, health-check, tool discovery, clean shutdown) in `manager.py` (203 lines); async Python from first principles (event loop, asyncio.Queue internals, backpressure chain); httpx async client authoring; deliberate retrieval practice / meta-learning (recall-error cluster self-diagnosis, spaced-retrieval policy) |
| **Hours invested** | ~30 hours (largest single project, internship deliverable) |
| **Completion** | 50% (active) — Phases 1–3 fully tested (skeleton, model provider, agent host with full POST-to-SSE token-streaming verified 08-06); Phase 4 MCP Integration code written + sub-agent reviewed 08-07 (3 crash + 2 wrong-result bugs fixed) but end-to-end uvicorn test never logged. 21 lessons through 0021; records through 0008 (no-cycle-exams policy). No session since 08-07/08-13; RAG, scheduling, multi-agent, frontend pending. |
| **Key evidence** | `NOTES.md`; `backend/src/mcp_servers/manager.py`; `backend/src/api/routers/chat.py`; `learning-records/0008-no-cycle-exams-policy.md`; `reference/learning-roadmap.html` |

### teach-physics (Physics)
| Field | Detail |
|---|---|
| **Domain** | University physics (mechanics → EM → thermo/stat mech → waves/optics → modern), AI-navigated derivation-first self-study from zero |
| **Skill level** | Beginner — physics not started (progress 0%); strong math background, but only method + resource library imported |
| **Concrete skills** | Curriculum scoping (5-branch university physics coverage with ordered sequence); AI-navigator learning-system design (single-smallest-step cycle, state-file feedback loop 懂了/太难/卡住); resource curation (Landau, Morin, Susskind, Feynman, Goldstein, Tong, MIT 8.223); method-entry analysis (Newtonian-first vs Lagrangian-first — open, undecided) |
| **Hours invested** | ~2 hours |
| **Completion** | 0% (paused) — content not begun; only method & resource library imported 06-22; README frontmatter `status: paused` |
| **Key evidence** | `README.md`; `resources/AI Tutor Instructions.md`; `resources/Physics Learning State.md` (friend's artifacts, not user's own progress) |

### teach-pku-freshman-prep (University Prep)
| Field | Detail |
|---|---|
| **Domain** | Transition to Peking University — practical, academic, and mental prep for an incoming freshman (Class of 2030) |
| **Skill level** | Advanced — independently built a structurally complete ~46-object / ~200-interaction unified model of university life from raw OCR'd official documents; discovered structural properties (emotion as modulation layer, senior as dual-property node) and made methodology-level decisions |
| **Concrete skills** | Systems modeling (objects + interactions, Mermaid) in Chinese reference/unified-model.html; knowledge extraction from raw OCR'd Chinese official documents; structural property discovery (emotion as modulation layer not dimension; dimension-slice vs constraint-layer distinctions); self-contained technical document authoring (HTML + Mermaid, dual English/Chinese incl. the 初入燕园 desktop series); dimension-slice analysis (traversing the model through information/financial/health filters); meta-learning methodology (batch-size convergence, speed-first model-second, model-vs-technique distinction); falsifiable lesson design separating understand-now vs execute-later |
| **Hours invested** | ~30 hours |
| **Completion** | 80% (active) — model phase 100% (26/26 learning records "accepted", newest 0026 emotion-as-modulation-layer; unified model structurally complete 07-25). Declared next: the strategy/action layer turning model knowledge into "what to do when" — still pending. |
| **Key evidence** | `reference/unified-model.html`; `learning-records/0026-emotion-as-modulation-layer.md`; `NOTES.md`; `reference/subsystems/01-core-campus.html` |

### teach-pytorch (PyTorch)
| Field | Detail |
|---|---|
| **Domain** | PyTorch / deep-learning framework fundamentals (tensor ops, autograd, torch.nn) |
| **Skill level** | Beginner — tensor construction and ops fluent; first half of autograd tutorial complete; second half blocked at L2 (missing prerequisite knowledge) |
| **Concrete skills** | Tensor construction and elementwise/matrix operations (rand, zeros, cat, @, broadcast); autograd gradient tracking (first half); transfers prior micrograd engine.py understanding as a conceptual foundation for autograd |
| **Hours invested** | ~4 hours |
| **Completion** | 11% (paused) — 1/9 learning-path items checked; autograd half-done and blocked; rest (torch.nn/optim/DataLoader/training loops/GPU/save-load/compile) untouched; README frontmatter `status: paused` |
| **Key evidence** | `README.md` |

### teach-RAG (Retrieval-Augmented Generation)
| Field | Detail |
|---|---|
| **Domain** | RAG — embeddings, vector search, chunking, retrieval-augmented generation, failure modes |
| **Skill level** | Beginner-to-Intermediate — builds and runs a minimal end-to-end RAG pipeline (Chroma + sentence-transformers, all-MiniLM-L6-v2); explains embeddings, vector search, chunking, and standard failure-mode fixes (re-ranking, hybrid search/BM25, HyDE); from-memory Python still error-prone. Track complete. |
| **Concrete skills** | End-to-end RAG pipeline (load → chunk → embed → store → retrieve → generate; `demo/rag_pipeline.py`, 298 lines); vector search with sentence-transformers + Chroma PersistentClient incl. manual numpy cosine scaffolding; naive-RAG failure modes and fixes; systematic retrieval debugging decision tree; coding-practice exercises (chunk explorer + reranker with solutions); recall of RAG concepts from memory for internship day-1 use |
| **Hours invested** | ~8 hours (one-day sprint, 2026-07-18) |
| **Completion** | 100% (completed) — 5/5 core lessons + coding-practice lesson; all 4 MISSION success criteria met; user declared internship-ready, workspace kept as reference. Unchanged since 08-13. |
| **Key evidence** | `learning-records/0006-lesson-0005-complete.md`; `demo/rag_pipeline.py`; `lessons/0006-coding-practice.html`; `reference/rag-pipeline-cheatsheet.html` |

### teach-runoob-python (Python)
| Field | Detail |
|---|---|
| **Domain** | Practical Python for an AI internship (runoob.com/python3 curriculum) — reading/writing real AI-codebase Python |
| **Skill level** | Intermediate — reads AI-codebase Python fluently (classes, type hints, requests, async) and writes real scripts/packages from scratch (textutils package); models async/await from first principles (six-operation event loop); known gap: authoring decorators from scratch |
| **Concrete skills** | HTTP/JSON API scripting with requests (layered error handling); OOP; modules/packages/import system (authored a real textutils package); venv/pip; file I/O + exceptions; type annotations; async/await from first principles (generator-based toy event loop, six-op + three-zone scheduler model, paper-simulating complex gather scenarios); dict/list comprehensions; decorators recognized via closures/@-sugar/@wraps but not yet authored from scratch |
| **Hours invested** | ~14 hours |
| **Completion** | 95% (completed) — all 5 MISSION criteria met; 10/11 lessons + async/await mastered (2026-07-28); authoring decorators from scratch deliberately deferred until the internship requires it. |
| **Key evidence** | `learning-records/0011-async-mastered.md`; `NOTES.md`; `reference/async-first-principles.html`; `textutils/cleaning.py` |

### teach-social-resources (Social Resources)
| Field | Detail |
|---|---|
| **Domain** | Conceptual theory of social capital / social resources: a 3-cycle model (five-subsystem taxonomy → social-capital unified theory of Bourdieu/Coleman/Putnam/kinship → SNA structure), driving toward a formal "generative core", for strategic deployment at PKU from Sep 2026 |
| **Skill level** | Advanced (theory-building & formal modeling) — recalls the five-subsystem map from memory, integrates classical social-capital theory with exact source attribution, and independently derives original formalizations beyond what lessons gesture at. **Major progress since the 08-13 report.** |
| **Concrete skills** | Recalls the five-subsystem map and four now-separated axes (tie strength / density-closure / composition / ascribed-achieved) entirely from memory; integrates classical social-capital theory (Bourdieu 1986, Coleman 1988, Putnam 2000, Curry 2013, Linton 1936) with exact source attribution, separating literature from course gloss; independently derives original formalizations (node-level vs tie-level ascription split; composition as a vector f(tie, cleavage)); builds original generative models (cost-based signal model, two-network substrate-vs-capital-flow model, framework-as-community-core strategy); formalizes the end goal as a self-referential A/B-manifold theory (theory = filter; stable core = fixed point T = Φ(T)) in GENERATIVE-CORE-FOUNDATIONS.md; directs multi-agent source-verification workflows (4–6 parallel research agents, ~293k tokens) with a misattribution ledger |
| **Hours invested** | ~15 hours (estimated — grew from 2 to ~11 lessons since 08-13; hours not recorded on disk) |
| **Completion** | 50% (active) — Cycle 1 (five-subsystem taxonomy + inventory audit) complete through its exam (LR-0006). Cycle 2 (unified theory: Bourdieu 0007, Coleman 0008, Putnam 0009, kinship axis 0010) all four lessons internalized incl. two original syntheses; lesson 0011 (conversion/compounding) written and mid-way through four rounds of deep Q&A (pass criteria + LR-0011 pending). Two 2026-08-16 adversarial audits repositioned Cycle 2 as "generative-materials" and produced the generative-core documents; Cycle 3 (SNA/Burt/North, lessons 0014–0020) scoped. Next: close 0011 and Cycle 2 (lessons 0012–0013), then deploy at PKU (Sep 2026). |
| **Key evidence** | `learning-records/0010-kinship-axis-internalized.md`; `lessons/0011-conversion-compounding.html`; `GENERATIVE-CORE-FOUNDATIONS.md`; `learning-records/0006-cycle-1-complete.md`; `reference/signal-model.html` |

### teach-technical-terms (Technical Vocabulary)
| Field | Detail |
|---|---|
| **Domain** | Workplace technical vocabulary for an intern — glossary bank + semantic-proximity learning of tech terms |
| **Skill level** | Beginner-to-Intermediate — explains MCP Host/Client/Server split, REST vs JSON-RPC, and SPA/SSR vs full-stack from memory; built on 6 prior self-study courses (Agent, RAG, Python, DB, Hermes, LangGraph) |
| **Concrete skills** | MCP protocol architecture from memory (Host/Client/Server, JSON-RPC, Tools/Resources/Prompts); REST vs JSON-RPC paradigms (closed CRUD verb set + 2xx–5xx status categories vs open arbitrary tool-method set); frontend/backend split, SPA vs SSR (incl. SSR's dual modern meaning), full-stack as role scope; MCP tool design reasoning (Server vs Host processing split, tool granularity, schema quality, context-budget tradeoffs); ~235-term glossary extracted into 9 semantic clusters + 8 expansion frontiers by proximity; API-as-contract mental model tying frontend/backend, HTTP, and REST together |
| **Hours invested** | ~4 hours (one intensive session 2026-07-28) |
| **Completion** | 20% (active) — glossary criterion met (~235 terms, 9 clusters); 4 lessons delivered on the MCP → API Design path (records 0001–0009); GraphQL or internship-encountered terms next; DevOps/Infra, System Design, Networking, Security frontiers open. No content activity since the single 07-28 session. |
| **Key evidence** | `lessons/0001-mcp-protocol.html`; `lessons/0004-tool-design.html`; `reference/glossary.html`; `learning-records/0003-semantic-frontiers-identified.md`; `learning-records/0009-lesson-0004-tool-design-chosen.md` |

### teach-x1 (AI Industry Value Chain)
| Field | Detail |
|---|---|
| **Domain** | AI industry value chain (upstream/midstream/downstream) analysis to identify a defensible startup niche — the declared core freshman-year task |
| **Skill level** | Advanced (analytical) — independently derived a dual-graph duality (company-consumer vs material-service) and a unified mixed-graph abstraction for industry-chain analysis; PKU math-department background |
| **Concrete skills** | Formal graph-theoretic modeling of a value chain (topology-defined layers — a node's layer set by graph position, not pre-assigned category); dual-graph analysis to locate bottleneck/pricing-power nodes (incl. why capacity constraints live in the material graph); unified mixed-graph model (2 node types, 2 edge types, projections recover each earlier graph); four-direction defensibility judgment (upstream / same-layer / downstream / time + bottleneck-migration) with an is/conditional/no verdict; real-company chain mapping (Cursor as a worked full-chain demo); quantifying an industry chain into cheat-sheet references and interactive HTML/SVG visualizations |
| **Hours invested** | ~7 hours (sessions 2026-08-05 and 2026-08-20) |
| **Completion** | 55% (active) — Cycle 1: four concept lessons (0001–0004) + practice lesson 0005 (Cursor full-chain mapping, 2026-08-20) + record 0004 (user found the simplified defensibility framing flawed and re-derived the complete four-direction-plus-time definition). Pending: user's own company-mapping exercise (0005 pass criteria), the Cycle-1 three-tier exam (0006, not yet created), then a Cycle-2 direction toward the entrepreneurial entry-point analysis. |
| **Key evidence** | `lessons/0005-practice-company-mapping.html`; `learning-records/0004-defensibility-three-fronts-plus-time.md`; `learning-records/0003-mixed-graph-unified-model.md`; `reference/value-chain-map.md`; `reference/company-analysis-worksheet.md` |

---

## 2. Skill Map — By Domain

### Programming & CS

| Sub-domain | Level | Source Projects | Evidence Summary |
|---|---|---|---|
| **Python** | Intermediate | cs61a, runoob-python, hermes-agent, langgraph-agent, openclaw-companion, RAG, IntroB, linear-algebra | Writes complete agents from scratch; async/await from first principles; FastAPI CRUD, async SQLAlchemy, Pydantic v2, MCP protocol implementation. New: past-exam Python (sliding window, myAtoi, prime sieve) and numpy numerical scripting. |
| **Git/GitHub** | Late beginner | github-learning | ~40 commands fluent; layered-architecture mental model (two areas, one graph, three pointer sets). |
| **Databases/SQL** | Intermediate | database, hermes-agent, openclaw-companion | SELECT/JOIN/GROUP BY from memory; FTS5 virtual tables; EXPLAIN QUERY PLAN; async SQLAlchemy ORM. |
| **CS Fundamentals** | Intermediate | cs61a, IntroB | cs61a recursion/HOFs/trees; **new:** IntroB computer-systems fundamentals — binary/encoding, CPU, OS/filesystem, network, flowchart programming — built for an exemption exam. |
| **Backend Development** | Intermediate | openclaw-companion, langgraph-agent | FastAPI, async SQLAlchemy, SSE streaming, MCP JSON-RPC, asyncio subprocess management. |
| **Frontend/HTML** | Intermediate | HTML, technical-terms | Semantic HTML5 multi-page sites from memory; forms mapped to HTTP; SVG vs Canvas; SPA/SSR concepts. |
| **CS Theory** | Beginner | hermes-agent | Regex, state machines, threads identified as prerequisite gaps; event loop internals. |

### AI/ML

| Sub-domain | Level | Source Projects | Evidence Summary |
|---|---|---|---|
| **AI Agents** | Intermediate-Advanced | Agent, hermes-agent, langgraph-agent, RAG | ReAct loop, tool-calling protocol, 4-layer debugging; Hermes 40K-line codebase traced; LangGraph StateGraph from memory; cron scheduler from scratch. |
| **RAG** | Intermediate | RAG | Full pipeline implementation; embeddings/vector search/chunking; 4 failure modes with fixes. |
| **Deep Learning Theory** | Advanced (analytical) | deep-learning-book, andrej-karpathy | Linear algebra, probability, optimization, ML basics — restructured into novel architectures; MLE equivalence chain; autograd/backprop from first principles. |
| **Deep Learning Practice** | Beginner | pytorch, andrej-karpathy, mit-6s184 | Tensor basics only; autograd blocked; no training loops, no GPU usage, no model architectures built. |
| **Diffusion Models** | Pre-beginner | mit-6s184 | Prerequisite gap (probability) identified; no content attempted. |
| **AI Industry Analysis** | Advanced (analytical) | x1 | Full value chain modeled; dual-graph theory; mixed-graph abstraction; bottleneck dynamics; defensibility four-direction-plus-time framework; 58+ company inventory. |

### Mathematics

| Sub-domain | Level | Source Projects | Evidence Summary |
|---|---|---|---|
| **Linear Algebra / 高等代数** | Advanced (theory) | linear-algebra | **New.** Full Phase-1 course: rank-nullity → spectral theorem → SVD → determinant theory → conditioning, each passed closed-book via a 6-act passbar; 9-dimension learner map (199 terms, 370 interaction edges); DL concepts bound to the spine (PCA=SVD, backprop=adjoint, conditioning=training stability). |

### Academic

| Sub-domain | Level | Source Projects | Evidence Summary |
|---|---|---|---|
| **Economics** | Intermediate | naked-economics | Deep analysis of information economics (Ch5); bilingual 3-layer structural analysis of 157 sentences. |
| **World Systems / Markets** | Intermediate | hello-world | Unified six-dimension market model; A/B/C analysis protocol on polysilicon/wafer cases; counterfactual prediction design. |
| **CPA Law (Chinese)** | Advanced beginner | CPA-JJF | 6-step legal scenario decomposition; law-as-OOP-model; 5 lessons of a redesigned 28-lesson curriculum. |
| **Physics** | Pre-beginner | physics | Methodology research only; no content executed. |
| **Computer Systems (exemption exam)** | Advanced | IntroB | **New.** Deep prep of PKU intro-computing content via exhaustive courseware audit + authentic past papers; exemption exam attempted Sept 2026 but not passed — project paused, materials retained as reference. |
| **University Strategy** | Exceptional | pku-freshman-prep | Graduate-level systems thinking; ~46-object unified model; Bayesian optimization, POMDP, control theory applied in practice. |

### Meta-learning & Communication

| Sub-domain | Level | Source Projects | Evidence Summary |
|---|---|---|---|
| **English (L2)** | Early intermediate | english-learning | CEFR A2-B1; collaborative conversation model; SLA methodology knowledge. |
| **Technical Vocabulary** | Intermediate | technical-terms | ~235 terms in 9 clusters; MCP, REST, frontend/backend, tool design concepts. |
| **Social Capital Modeling** | Advanced (theory-building) | social-resources | **Upgraded since 08-13.** Five-subsystem taxonomy; Bourdieu/Coleman/Putnam/kinship integrated with source attribution; original generative models; formal A/B-manifold / fixed-point framing of the field's end goal. |
| **Knowledge Modeling** | Advanced | pku-freshman-prep, deep-learning-book, naked-economics, x1, hello-world, social-resources, linear-algebra | Reusable pattern: extract invariant model structure from any domain. New: interaction-dictionary modeling (199-term/370-edge linear-algebra map). |
| **Instructional Design** | Strong | Agent, RAG, database, runoob-python, hermes-agent, langgraph-agent, HTML, technical-terms, x1, hello-world, IntroB, linear-algebra | 12+ curricula designed (for AI teacher persona); consistent methodology: progressive disclosure, criterion-referenced assessment, hands-on practice, learning record journaling. New: bounded-hermeneutic-circle course with 6-act passbars (linear-algebra); exhaustive-audit-first exam-prep doctrine (IntroB). |

---

## 3. Proficiency Matrix

Rows = skill areas. Columns = contributing projects. Values = contribution level (1 = foundational exposure, 2 = developing, 3 = proficient, 4 = advanced, 5 = exceptional).

| Skill Area | cs61a | runoob | database | github | Agent | RAG | hermes | langgraph | openclaw | HTML | dl-book | karpathy | pytorch | CPA | econ | hello-world | english | physics | mit-6s184 | pku | terms | social-resources | x1 | IntroB | LA | **Composite** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Python | 3 | 4 | 1 | — | 2 | 3 | 3 | 3 | 4 | — | — | 1 | 1 | — | — | — | — | — | — | — | — | — | — | 3 | 2 | **4 (Intermediate)** |
| Git | — | — | — | 3 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | **3** |
| SQL/Databases | — | — | 4 | — | — | — | 3 | — | 3 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | **4 (Intermediate)** |
| CS Fundamentals | 4 | 2 | — | — | — | — | 1 | 1 | 2 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | 4 | — | **4 (Intermediate)** |
| Backend Dev | — | 1 | — | — | — | 1 | 1 | 2 | 4 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | **4 (Intermediate)** |
| Frontend/HTML | — | — | — | — | — | — | — | — | — | 3 | — | — | — | — | — | — | — | — | — | — | 2 | — | — | — | — | **3 (Intermediate)** |
| AI Agents | — | — | — | — | 4 | — | 4 | 4 | 3 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | **4 (Advanced)** |
| RAG | — | — | — | — | — | 4 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | **4** |
| DL Theory | — | — | — | — | — | — | — | — | — | — | 5 | 2 | — | — | — | — | — | — | — | — | — | — | — | — | — | **5 (Exceptional)** |
| DL Practice | — | — | — | — | — | — | — | — | — | — | — | 1 | 1 | — | — | — | — | — | 1 | — | — | — | — | — | — | **1 (Beginner)** |
| Linear Algebra / Math | — | — | — | — | — | — | — | — | — | — | 2 | — | — | — | — | — | — | — | — | — | — | — | — | — | 4 | **4 (Advanced)** |
| AI Industry | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | 4 | — | — | **4 (Advanced)** |
| Economics | — | — | — | — | — | — | — | — | — | — | — | — | — | — | 4 | — | — | — | — | — | — | — | — | — | — | **4 (Intermediate)** |
| Markets & World Systems | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | 3 | — | — | — | — | — | — | — | — | — | **3 (Intermediate)** |
| CPA Law | — | — | — | — | — | — | — | — | — | — | — | — | — | 3 | — | — | — | — | — | — | — | — | — | — | — | **3** |
| English | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | 3 | — | — | — | — | — | — | — | — | **3** |
| Technical Vocab | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | 4 | — | — | — | — | **4** |
| Social Capital Modeling | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | 4 | — | — | — | **4 (Advanced)** |
| Systems Thinking | — | — | — | — | — | — | — | — | — | — | 4 | — | — | — | 3 | 4 | — | — | — | 5 | — | 4 | 5 | 3 | 4 | **5 (Exceptional)** |
| Meta-learning | 2 | 3 | 3 | 2 | 3 | 3 | 4 | 4 | 4 | 2 | 5 | 2 | 2 | 3 | 3 | 3 | 4 | 2 | 2 | 5 | 3 | 4 | 4 | 4 | 4 | **5 (Exceptional)** |
| Instructional Design | — | 3 | 4 | — | 4 | 4 | 4 | 4 | — | 4 | — | — | — | — | — | 4 | — | — | — | 5 | 4 | 4 | 4 | 4 | 4 | **5 (Exceptional)** |

**Columns added since the 2026-08-13 report:** `IntroB` = teach-Introduction-to-Computing-B, `LA` = teach-linear-algebra (rightmost two). `social-resources` and `x1` values were raised to reflect post-08-13 progress.

**"Exceptional" defined as:** Producing original theoretical insights, novel frameworks, or graduate-level analysis beyond what the learning materials themselves contain. Meta-cognitive sophistication that distinguishes expert learners.

---

## 4. Project Status Summary

```
COMPLETE (5):   Agent (100%), database (100%), HTML (100%),
                RAG (100%), runoob-python (95%)
ACTIVE (13):    langgraph-agent (80%), pku-freshman-prep (80%),
                x1 (55%), github-learning (51%),
                openclaw-companion (50%), social-resources (50%),
                hello-world (45%), linear-algebra (40%),
                cs61a (30%), english-learning (20%),
                technical-terms (20%), deep-learning-book (17%),
                CPA-JJF (15%)
PAUSED (7):     hermes-agent (80%), IntroB (70%),
                andrej-karpathy (13%), pytorch (11%),
                naked-economics (7%), mit-6s184 (2%), physics (0%)
```

**Total estimated hours:** ~355
**Projects complete:** 5 of 25 (20%)
**Projects with active progress:** 13 of 25 (52%)
**Most hours in:** linear-algebra (~50h), openclaw-companion (~30h), cs61a (~30h), pku-freshman-prep (~30h), IntroB (~25h), hermes-agent (~20h), deep-learning-book (~16h), github-learning (~15h), naked-economics (~15h), social-resources (~15h)

> **Hours caveat:** Only teach-Agent records a confirmed figure; the remaining hour totals are estimates (most projects keep no time log on disk) — largest growth this cycle is teach-linear-algebra and teach-Introduction-to-Computing-B, both new.

---

## 5. Notable Changes Since the 2026-08-13 Report

- **New projects (2):** `teach-linear-algebra` (created ~08-27) and `teach-Introduction-to-Computing-B` (created ~08-21) — report scope grew 23 → 25. Both registered in `_PROJECTS.md` on 2026-09-06.
- **teach-Introduction-to-Computing-B:** status set to `paused` on 2026-09-06 — the exemption exam was sat in September but not passed; prep materials retained as reference and the course will be taken for credit this term.
- **teach-social-resources:** 20% → 50%. Cycle 1 now complete through its exam (LR-0006); Cycle 2 (Bourdieu/Coleman/Putnam/kinship-axis unified theory) internalized through LR-0010; lesson 0011 written and mid-way; two 08-16 adversarial audits produced the generative-core documents; Cycle 3 (SNA) scoped. Skill level reassessed to Advanced (formal modeling).
- **teach-x1:** 40% → 55%. The 08-20 session added practice lesson 0005 (Cursor full-chain mapping), record 0004 (corrected four-direction-plus-time defensibility), and the company-analysis worksheet.
- **teach-hermes-agent:** completion corrected 75% → 80% — the project holds 9 authored lessons (0001–0009) and records through 0014; the pause was a manager redirect, not a lack of material.
- **teach-technical-terms:** no content change, but the agent audit re-graded it as effectively dormant (single 07-28 session); it is retained as `active` to match the registry.

> **Registry drift:** the two new projects were added to `_PROJECTS.md` on 2026-09-06. Separately, several registry-`active` tracks show no content written in 2–6 weeks — CPA-JJF (since 08-02), english-learning (08-09), hello-world (~08-12), openclaw-companion (08-13), cs61a (~mid-Aug), deep-learning-book (07-02), github-learning (07-30), technical-terms (07-28), pku-freshman-prep (07-25). Statuses here mirror the registry (source of truth); a future registry reconciliation may move some to paused.
