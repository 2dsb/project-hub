---
id: "idea-20260719-information-exchange-as-package-cycle"
title: "Information Exchange as Package-Unpack-Repeat Cycle"
tags:
  - information-exchange
  - agent-loop
  - communication
  - llm
  - abstraction
summary: "Seeing `response = llm_chat(messages, tools=tool_schemas)` crystallizes information exchange as a mechanical cycle of packaging state into a serialized format, sending, receiving, unpacking, acting, and repackaging. The crucial insight is that the package format itself constitutes the interface: the `list[dict]` message structure isn't an implementation detail but the protocol. This pattern recurs in HTTP requests, function calls, database queries, human conversation, and event systems. The agent loop is distinct because the `list[dict]` accumulates history with each cycle, making it a conversation rather than a transaction."
importance: 0.93  # auto
connections:
  - type: idea
    slug: interaction-as-essence-heuristic
  - type: idea
    slug: interaction-as-dictionary
---
# Information Exchange as Package-Unpack-Repeat Cycle

## The trigger

One line of code made the abstraction click:

```python
response = llm_chat(messages, tools=tool_schemas)
```

What's happening: you take a `list[dict]` — a structured package of data — and throw it at the LLM (an invisible interlocutor on the other side). The LLM throws back a package of type `object`. On your side, you unpack it, inspect what's inside, execute actions, pack the right data back into the message list, and repeat.

This is the first visceral understanding of what "information exchange" actually is — not as an abstract concept, but as a concrete mechanical cycle.

## The general pattern

1. **Package** — serialize your state/request into a structured format the receiver understands
2. **Send** — hand the package across a boundary (function call, API, network, conversation turn)
3. **Receive** — get a structured package back
4. **Unpack** — inspect the contents, extract what's actionable
5. **Act** — perform local operations based on what you received
6. **Re-package** — fold the results back into the package format
7. **Repeat**

## Why this is non-obvious

The insight isn't the steps — they're trivial. The insight is that **the package format IS the interface**. The `list[dict]` message format isn't an implementation detail; it IS the protocol. Understanding an information exchange system means understanding:

- What shape does the package have? (the data structures — see [[data-structure-first-code-reading]])
- What does each field mean to the receiver? (the semantics)
- What shapes can the response package take? (the contract)

Once you know the package format, the exchange becomes mechanical. The LLM's "intelligence" is a black box, but the *exchange* is fully transparent — and you can reason about everything on your side of the boundary.

## Where else does this pattern show up?

- **HTTP**: request package (method + headers + body) → response package (status + headers + body)
- **Function calls**: argument package → return value package
- **Database queries**: SQL string → result set
- **Human conversation**: utterance package → response utterance (the package format is natural language + social context)
- **Event systems**: event payload → handler side effects

The agent loop is special because the package format (`list[dict]`) is explicitly designed to accumulate history — each cycle appends to the package rather than replacing it. This makes the agent loop a *conversation* rather than a *transaction*.
