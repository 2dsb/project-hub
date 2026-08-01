---
id: "idea-20260719-core-capability-supporting-infrastructure"
title: "Core Capability → Supporting Infrastructure as Technology Evolution Pattern"
importance: 3
tags:
  - technology-evolution
  - llm
  - infrastructure
  - rag
  - agents
  - patterns
connections: []
---

# Core Capability → Supporting Infrastructure as Technology Evolution Pattern

## The observation

RAG and Agents are both supporting infrastructure built around a single core capability: the LLM's "sentence in, sentence out" transform. Neither RAG nor Agents changes what the LLM fundamentally does — they wrap the input side (RAG: inject relevant context before the prompt) and the output side (Agents: parse the response, route to tools, feed results back). They exist to bridge the gap between raw text-to-text and practical, grounded applications.

## The pattern

A technology evolution pattern: **core capability emerges → supporting infrastructure grows around it to make the core practically useful.**

The core capability is narrow and pure. The supporting infrastructure is messy and broad. The core is algorithmic; the infrastructure is plumbing. But without the infrastructure, the core is a demo, not a product.

| Core Capability | Supporting Infrastructure |
|---|---|
| LLM: text → text | RAG (knowledge grounding), Agents (action routing), Guardrails (safety), Orchestration (multi-step), Memory (state management) |
| Database: store → query | ORMs (object mapping), Connection pools (resource management), Replication (availability), Migration tools (schema evolution) |
| CPU: instruction → execution | OS (resource abstraction), Compilers (language → instructions), Schedulers (multi-tasking) |
| HTTP: request → response | Caching layers, Load balancers, Auth middleware, CDNs, API gateways |

## Implication for spotting the next thing

When a new "sentence in, sentence out" level core capability appears, the supporting infrastructure playbook is predictable:

1. **Input enrichment** — give the core access to more/better context (RAG pattern)
2. **Output routing** — parse output, take action, feed back (Agent pattern)
3. **Safety wrapping** — validate inputs, sanitize outputs (Guardrails pattern)
4. **State management** — give the stateless core a memory (conversation history, vector DBs)
5. **Composition** — chain multiple core calls into workflows (orchestration)

Each of these is a category of infrastructure waiting to be built around any new core capability. The infrastructure isn't glamorous, but it's where most of the practical value lives.

## Status

The pattern feels right but needs more historical examples to test whether it's genuinely universal or just fits the LLM case well. Possible counterexample: the internet (TCP/IP) — the core capability WAS the infrastructure; applications came after. Does that invert the pattern, or is it a different category?
