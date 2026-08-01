---
id: idea-20260717-teach-coverage-check
title: "Teach Coverage Check — Cross-Reference Teach Output Against Course Content"
tags:
  - teach
  - learning-method
  - quality-assurance
  - cs61a
importance: 3
connections:
  - type: project
    slug: cs61a
  - type: project
    slug: runoob-python
---

# Teach Coverage Check

**Simple practice**: After finishing a CS61A lecture (or any course section), have teach generate lecture notes based on the content. Then cross-check: does the teach output cover all the important points from the original lecture? If something is missing, flag it and fill the gap.

## Why

Teach is extremely efficient for learning, but it may miss important content. The course lecture serves as a coverage baseline — it defines what "should" be covered. A quick cross-check after each section catches omissions before they compound.

## Workflow

1. Watch the CS61A lecture
2. Have teach generate notes/lecture materials for the same topic
3. Scan for gaps — anything the lecture covered that teach didn't
4. Fill gaps manually or ask teach to cover them in a follow-up

## Scope

Applies to any course where teach is the primary learning tool and there's an external reference (lecture, textbook, syllabus) to check against. Currently: CS61A, Runoob Python.
