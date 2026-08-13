# Skill Report — All 23 teach-* Learning Projects

**Generated:** 2026-08-13
**Scope:** `C:\Users\61602\teach-*` (23 projects)
**Methodology:** Exhaustive file reading of MISSION.md, NOTES.md, learning records, code files, HTML lessons, and reference materials from every project. Proficiency assessments are evidence-based — citations drawn directly from artifacts produced.

---

## 1. Skill Inventory — Per Project

### teach-Agent (AI Agents)
| Field | Detail |
|---|---|
| **Domain** | AI Agents — ReAct agent loop, function/tool calling protocol, tool schema design, guardrails, prompt engineering |
| **Skill level** | Intermediate — reads/traces a Python agent loop end-to-end, diagnoses which of 4 layers (prompt / tool schema / loop / data structure) a bug lives in, and designs agent system prompts; reading fluency > writing (exercises scaffolded) |
| **Concrete skills** | Traces a Python agent loop (Thought → Action → Observation) through prompt, tools, messages, and guardrails; diagnoses which layer a bug lives in; understands tool/function-calling protocol and schemas; designs system prompts (5 questions, stopping cues, negative guidance); maps guardrails to failure modes; bug-hunts course materials — found and fixed 3 structural bugs |
| **Hours invested** | ~8 hours (one-day sprint, 2026-07-19) |
| **Completion** | 100% (5/5 lessons + deep-dive + coding practice; track-complete marker; all MISSION.md success criteria met) |
| **Key evidence** | `learning-records/0006-track-complete.md`; `learning-records/0004-robust-agent-loop.md`; `lessons/0005-coding-practice.html` |

### teach-andrej-karpathy-zero-to-hero (Deep Learning)
| Field | Detail |
|---|---|
| **Domain** | Deep Learning / neural networks — Karpathy's Zero to Hero (micrograd → makemore → GPT), PyTorch |
| **Skill level** | Beginner — read and understood micrograd `engine.py` (autograd Value class, backward pass, topological sort); no independent implementation written from scratch |
| **Concrete skills** | Understands micrograd autograd engine (Value class, `_backward` closures, topological-sort backward pass); explains backpropagation / chain-rule gradient flow on computation graphs; familiar with deep learning fundamentals |
| **Hours invested** | ~3 hours |
| **Completion** | 13% (1 of 8 checklist milestones — micrograd only; makemore P1–P5, GPT tokenizer, GPT from scratch all pending; README frontmatter `status: paused`) |
| **Key evidence** | `README.md`; `resources/micrograd.md` |

### teach-CPA-JJF (CPA Economic Law)
| Field | Detail |
|---|---|
| **Domain** | CPA 经济法 (Chinese Economic Law) — understanding-oriented legal study, not exam prep |
| **Skill level** | Advanced beginner — decomposes legal scenarios via a 6-step analysis template and re-expresses law as Python OOP models (law = class, legal act = `__init__`, 位阶 = MRO); co-authored lesson content and caught genuine errors in teaching material |
| **Concrete skills** | 6-step legal scenario decomposition (is-it-law → rank → subjects → object → rights/obligations → trigger); classifies civil legal acts by validity tier (无效/可撤销/效力待定) with underlying rationale; two-way memorization-understanding pedagogical framework |
| **Hours invested** | ~10 hours |
| **Completion** | 15% (5 of 28 lessons + 0 of 5 exams; Cycle 1 法律基础 is 5/7 through; last session 2026-08-02) |
| **Key evidence** | `learning-records/0008-lesson-0005-passed.md`; `learning-records/0007-lesson-0004-passed.md`; `NOTES.md`; `lessons/0005-civil-legal-acts.html` |

### teach-cs61a (CS Fundamentals)
| Field | Detail |
|---|---|
| **Domain** | UC Berkeley CS61A — Python programming fundamentals (functions, recursion, sequences, objects, interpreters, SQL) |
| **Skill level** | Intermediate — implemented both full CS61A projects (Hog dice game, Cats typing game) passing all ok-autograder questions; fluent in higher-order functions, closures, recursion; authored an original "portal model" of frame-tree program execution |
| **Concrete skills** | HOFs / closures / function factories; recursion and tree/mutual recursion; memoization; string/list processing; TDD via ok-autograder + pytest with coverage; debugging and algorithm design; abstract model-building of program execution |
| **Hours invested** | ~30 hours |
| **Completion** | 30% (Weeks 1–3 of 10 complete: Hog + HW01-03 + labs; Week 4 next; README frontmatter `status: active`) |
| **Key evidence** | `README.md`; `resources/hog/hog.py`; `resources/cats/cats.py`; `resources/comprehension-view-portal-model.md` |

### teach-database (SQL/SQLite)
| Field | Detail |
|---|---|
| **Domain** | SQLite / SQL — read and query a production `.db`, indexes, FTS5 |
| **Skill level** | Intermediate — from absolute zero on 07-22 to independently querying a 21-table production schema (Hermes state.db) from memory by 07-24; understands execution plans and FTS5 virtual tables |
| **Concrete skills** | SQLite CLI fluency (`.tables`, `.schema`, dot-commands); SELECT/WHERE/ORDER BY/LIMIT/JOIN/GROUP BY/aggregates from memory; reading CREATE TABLE schema; regular index vs FTS5 abstraction; querying a real production database without reference; self-derived truth table (no-GROUP-BY two modes) |
| **Hours invested** | ~5 hours (2 days: 07-22, 07-24) |
| **Completion** | 100% (5/5 lessons; all 5 MISSION goals met; course-complete marker `0008`) |
| **Key evidence** | `learning-records/0008-course-complete.md`; `learning-records/0007-virtual-table-mental-model.md`; `learning-records/0006-no-group-by-two-modes.md`; `lessons/0005-indexes-fts5.html` |

### teach-deep-learning-book (DL Theory)
| Field | Detail |
|---|---|
| **Domain** | Reading Goodfellow's "Deep Learning" textbook sequentially with per-chapter notes |
| **Skill level** | Intermediate — synthesizes dense math-textbook chapters into original multi-layer mental models with rigorous notation (MLE ≡ NLL ≡ KL ≡ cross-entropy ≡ ERM, Bayes error, Cramér–Rao, conjugate priors) and concept dependency graphs |
| **Concrete skills** | Linear algebra / matrix-calculus reasoning (eigendecomposition, SVD, PCA); probability & information theory (Bayes, KL, MLE equivalence chain); numerical computation & gradient-based optimization; ML fundamentals (capacity/bias-variance/estimators/SGD); knowledge synthesis into layered mental-model architectures |
| **Hours invested** | ~16 hours |
| **Completion** | 17% (4 of 20 chapters: Ch2 linear algebra, Ch3 probability, Ch4 numerical computation, Ch5 ML basics; Parts II–III untouched; README frontmatter `status: active`) |
| **Key evidence** | `README.md`; `resources/ch5-machine-learning-basics.md` (590 lines); `resources/ch2-linear-algebra.md` |

### teach-english-learning (English)
| Field | Detail |
|---|---|
| **Domain** | English conversational fluency (target MIT, IELTS 7.5+) — SLA-grounded conversation training, concept-first in Chinese |
| **Skill level** | A2–B1 baseline (per MISSION.md) — solid conceptual mastery of the collaborative conversation model; can explain, self-diagnose, analyze real dialogues, and teach it; no confirmed speaking practice yet (practice lesson pending) |
| **Concrete skills** | Explains performance-vs-collaborative model of conversation; identifies own performance-mindset patterns in past conversations; analyzes a real conversation for communication strategies; teaches a newly learned concept (learn-by-teaching) |
| **Hours invested** | ~4 hours |
| **Completion** | 20% (Cycle 1 step 1 of 5 complete; Lesson 0002 built with passing criteria, Lesson 0003 announced; Practice and Exam lessons pending) |
| **Key evidence** | `learning-records/0001-performance-vs-collaborative-model.md`; `lessons/0001-conversation-is-not-performance.html`; `lessons/0002-communication-strategies.html` |

### teach-github-learning (Git/GitHub)
| Field | Detail |
|---|---|
| **Domain** | Git & GitHub via a sequential 42-task checklist (T1–T42), Pro Git + GitHub Docs based |
| **Skill level** | Beginner-to-intermediate — full local + remote workflow fluent (init/commit/branch/merge/push/PR); wrote a deep conceptual mental-model doc; Phases 3–4 (conflicts, stash, rebase, Issues) not yet done |
| **Concrete skills** | Full local workflow; branching & merging (fast-forward vs 3-way); GitHub remotes (SSH, push/pull/fetch, clone); PR lifecycle; branch cleanup & sync; history fixes (amend, restore); conceived a formal git mental model (two areas, one graph, three pointer sets, remote-tracking staleness) |
| **Hours invested** | ~15 hours |
| **Completion** | 51% (24/42 tasks checked, T1–T25; Phases 1–2 complete; README frontmatter `status: active`) |
| **Key evidence** | `README.md`; `resources/git-commands-T1-T25.md`; `resources/git-mental-model.md` |

### teach-hello-world (World Systems)
| Field | Detail |
|---|---|
| **Domain** | Understanding how world systems work — markets, finance, geopolitics, governance (世界运行规律) |
| **Skill level** | Intermediate — independently builds and applies a unified market model (six-dimension framework + Five Filters compression) and an A/B/C static→strategy→dynamic protocol to real industrial cases (polysilicon/wafer markets), reasoning under limited public data |
| **Concrete skills** | Unified multi-layer market model; A/B/C three-stage analysis protocol on real market cases; entity-first analysis under limited public data (financial-signal, structural, boundary-framing, conditional reasoning); cross-subsystem causal-trace reasoning; first-principles critique of taxonomy-vs-derivation gaps; falsifiable counterfactual prediction design |
| **Hours invested** | ~12 hours (intense first week: sessions 08-08, 08-09, 08-11, 08-12) |
| **Completion** | 45% (explicitly open-ended course — hermeneutic circle; Cycle 1 market subsystem ~90% complete: lessons 0001–0004 done, unified model built) |
| **Key evidence** | `reference/polysilicon-market-data.html`; `reference/entity-first-analysis-protocol.html`; `learning-records/0009-abc-analysis-method.md`; `learning-records/0010-market-as-perspective-superposition.md` |

### teach-hermes-agent (Agent Framework)
| Field | Detail |
|---|---|
| **Domain** | Hermes Agent source code — cron scheduling, tool calling, 4-layer memory architecture, FTS5 database design; plus a from-scratch Python mini agent |
| **Skill level** | Intermediate — wrote a working tool-calling agent loop + cron scheduler (~100-line Python, `agent.py` + `cron.py`) from memory with zero Hermes deps; reads production framework source (4-layer memory, FTS5 composite-column pattern) with correct mental models |
| **Concrete skills** | From-scratch autonomous agent (3-branch loop + OpenAI-compatible tool calling + JSON persistence); cron scheduler from memory (parse/load/save/cron_loop); Python file-I/O fluency via 7 progressive drills; operated Hermes from source (0.18.2, DeepSeek API); traces FTS5 composite columns, MATCH/snippet()/rank, triggers; debugged real API issues |
| **Hours invested** | ~20 hours (9 lessons + drill practice) |
| **Completion** | 75% (lessons 0001–0007 complete; track paused 2026-07-24 when manager redirected to LangGraph → teach-langgraph-agent) |
| **Key evidence** | `mini-agent/agent.py` (143 lines); `mini-agent/cron.py` (99 lines); `learning-records/0014-layer-2-synthesis.md`; `NOTES.md` |

### teach-HTML (Frontend/HTML)
| Field | Detail |
|---|---|
| **Domain** | HTML as the first step of the frontend stack (HTML → CSS → JavaScript → Vue), required for an internship |
| **Skill level** | Intermediate — writes a complete, semantically correct multi-page HTML site from memory (skeleton, semantic HTML5, tables with colspan/rowspan, forms); maps form submission to an HTTP request; understands SVG (retained-mode) vs Canvas (immediate-mode); zero frontend experience → 15/15 lessons in ~3 days |
| **Concrete skills** | Semantic HTML5 documents from memory; complex tables (one-slot-one-owner grid model); forms (20+ input types, validation, GET vs POST, enctype) mapped to HTTP; multi-page site structure (relative links, iframes, head glue); HTML5 APIs (Canvas/SVG/DnD awareness); self-editing — catches structural tag mismatches and stale runoob "fossils" |
| **Hours invested** | ~12 hours (3 sessions, Aug 10–12) |
| **Completion** | 100% (15/15 lessons + three-tier exam passed Aug 10–12: Easy 6/6, Medium 2/2, Hard 1/1; MISSION success criteria 1–4 met; hands off to teach-CSS) |
| **Key evidence** | `learning-records/0015-exam-passed.md`; `NOTES.md`; `practice/semantic-blog.html`; `practice/forms-demo.html` |

### teach-langgraph-agent (LangGraph)
| Field | Detail |
|---|---|
| **Domain** | LangGraph (StateGraph, ToolNode, checkpointing, streaming) — graph-based agent framework |
| **Skill level** | Intermediate — writes a full 3-file LangGraph agent (state.py / agent.py / main.py) from memory, including a 3-branch router and custom reducer; built an independent 5-node linear-pipeline app (LGA) with real API integration |
| **Concrete skills** | StateGraph from scratch (add_node/add_edge/add_conditional_edges/compile); TypedDict + Annotated reducers (add_messages, custom add_tool_log); 3-branch conditional routers with hand-written tool execution; debugs to zero errors unaided (Exam 0001: 12→3→0 over 3 passes); real-world app with API discovery, pagination, timezone, .env secrets, Chinese JSON; iterates pragmatically (5 region-classification approaches) |
| **Hours invested** | ~12 hours |
| **Completion** | 80% (4/4 lessons + Exam 0001 + real-world capstone; all 4 MISSION criteria met; streaming/checkpointing lessons planned) |
| **Key evidence** | `lessons/0004-tools-and-routing.html`; `hands-on/agent.py` (127 lines); `learning-records/0003-exam-0001-complete.md`; `learning-records/0004-first-real-world-project-lga.md` |

### teach-mit-6s184 (Diffusion Models)
| Field | Detail |
|---|---|
| **Domain** | MIT 6.S184 — Flow Matching & Diffusion Models (generative AI / deep learning) |
| **Skill level** | Beginner — read pp.1–18 of the lecture notes and drafted an analogy-based explanation of generative modeling as sampling (mountain story); no labs, no code written |
| **Concrete skills** | Read and summarized technical ML lecture notes; explained generative-modeling-as-sampling via an original analogy (4-section Chinese story); maintained structured project docs (frontmatter status, syllabus checklist) |
| **Hours invested** | ~4 hours |
| **Completion** | 2% (0/7 chapters, 0/3 labs; only pp.1–18 read; README frontmatter `status: paused` — prerequisite gap identified) |
| **Key evidence** | `README.md`; `resources/lecture_notes.pdf` |

### teach-naked-economics (Economics)
| Field | Detail |
|---|---|
| **Domain** | Reading Charles Wheelan's "Naked Economics" via connection-based reading — per-chapter bilingual sentence annotation + concept-constraint graphs |
| **Skill level** | Advanced (analytical depth) / Beginner (breadth — only 1 of 14 chapters) — produced sentence-level 3-layer structural analysis of a full English chapter (157 sentences, 18 sections) with constraint-typed Mermaid concept-constraint graphs |
| **Concrete skills** | 3-layer text-structure analysis (sentence → paragraph → article) with structural-role tagging; bilingual EN–CN sentence-by-sentence annotation (157 sentences); Mermaid concept-constraint graph + interactive zoomable HTML graph; systematic connection-reading methodology; economics concept mapping (adverse selection, asymmetric information, signaling, lemon markets, death spiral) |
| **Hours invested** | ~15 hours (on a single chapter) |
| **Completion** | 7% (Ch5 Economics of Information complete; 13 chapters + epilogue unchecked; README frontmatter `status: paused`) |
| **Key evidence** | `resources/ch05-structural-analysis.md` (53 KB); `resources/ch05-section1-full-structure.md` (19 KB); `resources/ch05-graph.html` |

### teach-openclaw-companion (Backend Development)
| Field | Detail |
|---|---|
| **Domain** | Backend for OpenClaw Companion, a Windows desktop AI assistant — FastAPI + async SQLAlchemy + LangGraph + MCP + SSE (RAG/scheduler planned) |
| **Skill level** | Intermediate — writes and debugs a real FastAPI + LangGraph + MCP backend by hand (async SSE streaming pipeline, MCP subprocess lifecycle, async SQLAlchemy); self-diagnoses recall errors clustering in SQLAlchemy type names and HTTP method mapping |
| **Concrete skills** | FastAPI + async SQLAlchemy (REST CRUD, Pydantic schemas, DI, lifespan, async engine); async Python deep dive (event loop, asyncio.Queue, backpressure); SSE streaming (POST+SSE, async generator, is_disconnected); LangGraph orchestration (astream_events, MemorySaver, ToolNode); MCP protocol + SDK (subprocess spawn/health-check/shutdown, stdio transport); deliberate retrieval practice |
| **Hours invested** | ~30 hours (largest single project, internship deliverable) |
| **Completion** | 50% (4 of ~8 phases: Skeleton, Model Provider, Agent Host, MCP Integration; Phases 1–3 fully tested; RAG, scheduling, multi-agent, frontend pending) |
| **Key evidence** | `NOTES.md`; `backend/src/mcp_servers/manager.py` (204 lines); `reference/learning-roadmap.html`; `learning-records/0007-retrieval-practice-error-patterns.md` |

### teach-physics (Physics)
| Field | Detail |
|---|---|
| **Domain** | University physics (mechanics → EM → thermo → waves/optics → modern), AI-navigated derivation-first self-study from zero |
| **Skill level** | Beginner — physics not started (progress 0%); strong math background, but only method + resource library imported |
| **Concrete skills** | Curriculum scoping (5-branch university physics coverage with ordered sequence); learning-system design (AI-navigator loop, single-smallest-step, state-file discipline); resource curation (Landau, Morin, Susskind, Feynman, Goldstein, Tong, MIT 8.223) |
| **Hours invested** | ~2 hours |
| **Completion** | 0% (progress per README frontmatter; `status: paused`; only method & resource library imported 06-22) |
| **Key evidence** | `README.md`; `resources/AI Tutor Instructions.md`; `resources/Physics Learning State.md` (both friend's artifacts, not user's own progress) |

### teach-pku-freshman-prep (University Prep)
| Field | Detail |
|---|---|
| **Domain** | Transition to Peking University — practical, academic, and mental prep for an incoming freshman (Class of 2030) |
| **Skill level** | Advanced — independently built a structurally complete ~46-object / ~200-interaction unified model of university life from raw OCR'd official documents; discovered structural properties (emotion as modulation layer, senior as dual-property node) and made methodology-level decisions |
| **Concrete skills** | Systems modeling (objects + interactions); knowledge extraction from raw OCR documents; applied own epistemological frameworks to a high-stakes domain; structural property discovery (signal decay law, activation-energy gradient); self-contained technical document authoring (HTML + Mermaid, dual English/Chinese); dual-language product creation (初入燕园 desktop series); meta-learning methodology (batch-size convergence) |
| **Hours invested** | ~30 hours |
| **Completion** | 80% (model phase 100% — 26/26 learning records "accepted", structurally complete; the strategy/action layer is pending) |
| **Key evidence** | `reference/unified-model.html`; `learning-records/0026-emotion-as-modulation-layer.md`; `NOTES.md`; `reference/subsystems/01-core-campus.html` |

### teach-pytorch (PyTorch)
| Field | Detail |
|---|---|
| **Domain** | PyTorch / deep-learning framework fundamentals (tensor ops, autograd, torch.nn) |
| **Skill level** | Beginner — tensor construction and ops fluent; first half of autograd tutorial complete; second half blocked at L2 (missing prerequisite knowledge) |
| **Concrete skills** | Tensor construction and elementwise/matrix operations (rand, zeros, cat, @, broadcast); autograd gradient tracking (first half); read and understood micrograd engine.py (transfer foundation) |
| **Hours invested** | ~4 hours |
| **Completion** | 11% (1/9 learning-path items checked; autograd half-done; README frontmatter `status: paused`) |
| **Key evidence** | `README.md` |

### teach-RAG (Retrieval-Augmented Generation)
| Field | Detail |
|---|---|
| **Domain** | RAG — embeddings, vector search, chunking, retrieval-augmented generation, failure modes |
| **Skill level** | Beginner-to-Intermediate — builds and runs a minimal end-to-end RAG pipeline (Chroma + sentence-transformers, all-MiniLM-L6-v2); explains embeddings, vector search, chunking, and standard failure-mode fixes (re-ranking, hybrid search/BM25, HyDE); from-memory Python still error-prone |
| **Concrete skills** | End-to-end RAG pipeline (load → chunk → embed → store → retrieve → generate); vector search with sentence-transformers + Chroma PersistentClient; explains naive-RAG failure modes and fixes; systematic retrieval debugging; manual vector similarity with numpy (cosine scaffolding) |
| **Hours invested** | ~8 hours (one-day sprint, 2026-07-18) |
| **Completion** | 100% (5/5 core lessons; all 4 MISSION success criteria met; track complete — record 0006 confirms) |
| **Key evidence** | `demo/rag_pipeline.py` (299 lines); `learning-records/0006-lesson-0005-complete.md`; `lessons/0006-coding-practice.html` |

### teach-runoob-python (Python)
| Field | Detail |
|---|---|
| **Domain** | Practical Python for an AI internship (runoob.com/python3 curriculum) — reading/writing real AI-codebase Python |
| **Skill level** | Intermediate — reads AI-codebase Python fluently (classes, type hints, requests, async) and writes real scripts/packages from scratch (textutils package); models async/await from first principles (six-operation event loop); known gap: authoring decorators from scratch |
| **Concrete skills** | HTTP/JSON API scripting with requests (3-layer error handling); OOP; modules/packages/import system (built textutils package); venv/pip; file I/O + exceptions; type annotations; async/await from first principles (generators → coroutines, event-loop scheduling simulation, gather); dict/list comprehensions |
| **Hours invested** | ~14 hours |
| **Completion** | 95% (all 5 MISSION criteria met; 10/11 lessons + async/await mastered; decorators writing deliberately deferred) |
| **Key evidence** | `learning-records/0011-async-mastered.md`; `NOTES.md`; `reference/async-first-principles.html`; `textutils/cleaning.py` |

### teach-social-resources (Social Resources)
| Field | Detail |
|---|---|
| **Domain** | Theory-layer conceptual model of social resources (connections, channels, platforms, endorsements, information) as a system, to be deployed strategically at PKU from Sep 2026 |
| **Skill level** | Beginner-intermediate — recalls a 5-subsystem taxonomy from memory; independently formalizes node/edge (connection/channel) models beyond the lesson-1 passing bar; applying the theory to own 36 contacts still pending |
| **Concrete skills** | Recalls structured 5-subsystem taxonomy from memory; models social structure as a graph (node = connection, edge = channel); decomposes connection value into position × willingness-to-activate; independently derives unifying formalizations (directed connection graph; channel as state→state transform); reasons about when to formalize vs. stay enumerative |
| **Hours invested** | ~6 hours (created 2026-08-12, two sessions) |
| **Completion** | 20% (1 of 6 cycle-1 steps complete; Lesson 0002 written but passing criteria pending; Practice 0005 and Exam 0006 to come) |
| **Key evidence** | `lessons/0001-social-resources-full-map.html`; `learning-records/0001-five-subsystem-map-internalized.md`; `reference/glossary.html` |

### teach-technical-terms (Technical Vocabulary)
| Field | Detail |
|---|---|
| **Domain** | Workplace technical vocabulary for an intern — glossary bank + semantic-proximity learning of tech terms |
| **Skill level** | Beginner-to-Intermediate — explains MCP Host/Client/Server split, REST vs JSON-RPC, and SPA/SSR vs full-stack from memory; built on 6 prior self-study courses (Agent, RAG, Python, DB, Hermes, LangGraph) |
| **Concrete skills** | MCP architecture from memory (Host/Client/Server, JSON-RPC, Tools/Resources/Prompts); REST vs JSON-RPC paradigms and HTTP status categories; frontend/backend split, SPA vs SSR; MCP tool granularity (processing boundary + context-budget reasoning); extracted ~235-term glossary into 9 semantic clusters |
| **Hours invested** | ~4 hours (one intensive session 2026-07-28) |
| **Completion** | 20% (glossary criterion met — ~235 terms, 9 clusters; 4 lessons delivered: MCP → API Design frontier; 8 more frontier directions identified) |
| **Key evidence** | `lessons/0001-mcp-protocol.html`; `lessons/0004-tool-design.html`; `reference/glossary.html` (68 KB); `learning-records/0005-lesson-0001-completed.md` |

### teach-x1 (AI Industry Value Chain)
| Field | Detail |
|---|---|
| **Domain** | AI industry value chain (upstream/midstream/downstream) analysis to identify a defensible startup niche — the declared core freshman-year task |
| **Skill level** | Advanced (analytical) — independently derived a dual-graph duality (company-consumer vs material-service) and a unified mixed-graph abstraction for industry-chain analysis; PKU math-department background |
| **Concrete skills** | Formal graph-theoretic modeling of a value chain (topology-defined layers); dual-graph analysis to locate bottleneck/pricing-power nodes; bottleneck analysis via edge capacity, path-equivalence, supply-demand growth-rate differentials; unified mixed-graph model (2 node types, layer projection); deep mapping of the AI chain (58+ companies, 6 consumer types, 24 materials, 31 services); synthesizing primary research into quantified cheat-sheets; interactive HTML visualizations |
| **Hours invested** | ~5 hours (single substantive session 2026-08-05) |
| **Completion** | 40% (4/4 concept lessons + 3 learning records; practice lesson 0005, three-tier exam, and entrepreneurial-entry analysis pending) |
| **Key evidence** | `learning-records/0002-dual-graphs-companies-vs-materials.md`; `learning-records/0003-mixed-graph-unified-model.md`; `reference/company-transformation-table.md`; `reference/value-chain-map.md` |

---

## 2. Skill Map — By Domain

### Programming & CS

| Sub-domain | Level | Source Projects | Evidence Summary |
|---|---|---|---|
| **Python** | Intermediate | cs61a, runoob-python, hermes-agent, langgraph-agent, openclaw-companion, RAG | Writes complete agents from scratch; async/await from first principles; FastAPI CRUD, async SQLAlchemy, Pydantic v2, MCP protocol implementation. |
| **Git/GitHub** | Late beginner | github-learning | ~40 commands fluent; layered-architecture mental model (two areas, one graph, three pointer sets). |
| **Databases/SQL** | Intermediate | database, hermes-agent, openclaw-companion | SELECT/JOIN/GROUP BY from memory; FTS5 virtual tables; EXPLAIN QUERY PLAN; async SQLAlchemy ORM. |
| **CS Fundamentals** | Intermediate | cs61a | Recursion, HOFs, closures, trees, OOP, iterators/generators, environment diagrams; created original Portal Model. |
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
| **AI Industry Analysis** | Advanced (analytical) | x1 | Full value chain modeled; dual-graph theory; bottleneck dynamics; 58+ company inventory with financial data. |

### Academic

| Sub-domain | Level | Source Projects | Evidence Summary |
|---|---|---|---|
| **Economics** | Intermediate | naked-economics | Deep analysis of information economics (Ch5); bilingual 3-layer structural analysis of 157 sentences. |
| **World Systems / Markets** | Intermediate | hello-world | Unified six-dimension market model; A/B/C analysis protocol on polysilicon/wafer cases; counterfactual prediction design. |
| **CPA Law (Chinese)** | Advanced beginner | CPA-JJF | 6-step legal scenario decomposition; law-as-OOP-model; 5 chapters of a redesigned 28-lesson curriculum. |
| **Physics** | Pre-beginner | physics | Methodology research only; no content executed. |
| **University Strategy** | Exceptional | pku-freshman-prep | Graduate-level systems thinking; ~46-object unified model; Bayesian optimization, POMDP, control theory applied in practice. |

### Meta-learning & Communication

| Sub-domain | Level | Source Projects | Evidence Summary |
|---|---|---|---|
| **English (L2)** | Early intermediate | english-learning | CEFR A2-B1; collaborative conversation model; SLA methodology knowledge. |
| **Technical Vocabulary** | Intermediate | technical-terms | ~235 terms in 9 clusters; MCP, REST, frontend/backend, tool design concepts. |
| **Social Resource Modeling** | Beginner-intermediate | social-resources | 5-subsystem taxonomy from memory; node/edge (connection/channel) formalization. |
| **Knowledge Modeling** | Advanced | pku-freshman-prep, deep-learning-book, naked-economics, x1, hello-world, social-resources | Reusable pattern: extract invariant model structure from any domain. 5-step lesson extraction pipeline. |
| **Instructional Design** | Strong | Agent, RAG, database, runoob-python, hermes-agent, langgraph-agent, HTML, technical-terms, x1, hello-world | 10+ curricula designed (for AI teacher persona); consistent methodology: progressive disclosure, criterion-referenced assessment, hands-on practice, learning record journaling. |

---

## 3. Proficiency Matrix

Rows = skill areas. Columns = contributing projects. Values = contribution level (1 = foundational exposure, 2 = developing, 3 = proficient, 4 = advanced, 5 = exceptional).

| Skill Area | cs61a | runoob | database | github | Agent | RAG | hermes | langgraph | openclaw | HTML | dl-book | karpathy | pytorch | CPA | econ | hello-world | english | physics | mit-6s184 | pku | terms | social-resources | x1 | **Composite** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Python | 3 | 4 | 1 | — | 2 | 3 | 3 | 3 | 4 | — | — | 1 | 1 | — | — | — | — | — | — | — | — | — | — | **4 (Intermediate)** |
| Git | — | — | — | 3 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | **3** |
| SQL/Databases | — | — | 4 | — | — | — | 3 | — | 3 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | **4 (Intermediate)** |
| CS Fundamentals | 4 | 2 | — | — | — | — | 1 | 1 | 2 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | **4 (Intermediate)** |
| Backend Dev | — | 1 | — | — | — | 1 | 1 | 2 | 4 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | **4 (Intermediate)** |
| Frontend/HTML | — | — | — | — | — | — | — | — | — | 3 | — | — | — | — | — | — | — | — | — | — | 2 | — | — | **3 (Intermediate)** |
| AI Agents | — | — | — | — | 4 | — | 4 | 4 | 3 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | **4 (Advanced)** |
| RAG | — | — | — | — | — | 4 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | **4** |
| DL Theory | — | — | — | — | — | — | — | — | — | — | 5 | 2 | — | — | — | — | — | — | — | — | — | — | — | **5 (Exceptional)** |
| DL Practice | — | — | — | — | — | — | — | — | — | — | — | 1 | 1 | — | — | — | — | — | 1 | — | — | — | — | **1 (Beginner)** |
| AI Industry | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | 4 | **4 (Advanced)** |
| Economics | — | — | — | — | — | — | — | — | — | — | — | — | — | — | 4 | — | — | — | — | — | — | — | — | **4 (Intermediate)** |
| Markets & World Systems | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | 3 | — | — | — | — | — | — | — | **3 (Intermediate)** |
| CPA Law | — | — | — | — | — | — | — | — | — | — | — | — | — | 3 | — | — | — | — | — | — | — | — | — | **3** |
| English | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | 3 | — | — | — | — | — | — | **3** |
| Technical Vocab | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | 4 | — | — | **4** |
| Systems Thinking | — | — | — | — | — | — | — | — | — | — | 4 | — | — | — | 3 | 4 | — | — | — | 5 | — | 3 | 5 | **5 (Exceptional)** |
| Meta-learning | 2 | 3 | 3 | 2 | 3 | 3 | 4 | 4 | 4 | 2 | 5 | 2 | 2 | 3 | 3 | 3 | 4 | 2 | 2 | 5 | 3 | 3 | 4 | **5 (Exceptional)** |
| Instructional Design | — | 3 | 4 | — | 4 | 4 | 4 | 4 | — | 4 | — | — | — | — | — | 4 | — | — | — | 5 | 4 | 3 | 4 | **5 (Exceptional)** |

**"Exceptional" defined as:** Producing original theoretical insights, novel frameworks, or graduate-level analysis beyond what the learning materials themselves contain. Meta-cognitive sophistication that distinguishes expert learners.

---

## Project Status Summary

```
COMPLETE (5):   Agent (100%), database (100%), HTML (100%),
                RAG (100%), runoob-python (95%)
ACTIVE (12):    langgraph-agent (80%), pku-freshman-prep (80%),
                github-learning (51%), openclaw-companion (50%),
                hello-world (45%), x1 (40%), cs61a (30%),
                english-learning (20%), social-resources (20%),
                technical-terms (20%), deep-learning-book (17%),
                CPA-JJF (15%)
PAUSED (6):     hermes-agent (75%), andrej-karpathy (13%),
                pytorch (11%), naked-economics (7%),
                mit-6s184 (2%), physics (0%)
```

**Total estimated hours:** ~269
**Projects complete:** 5 of 23 (22%)
**Projects with active progress:** 12 of 23 (52%)
**Most hours in:** cs61a (~30h), openclaw-companion (~30h), pku-freshman-prep (~30h), hermes-agent (~20h), deep-learning-book (~16h), github-learning (~15h), naked-economics (~15h), runoob-python (~14h)
