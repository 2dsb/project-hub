---
id: idea-20260608-mr01
title: Mindustry Resource Routing: Optimizing N Conveyor Lines Merging into the Core
tags:
  - mindustry
  - logistics
  - routing
  - optimization
  - game-design
summary: "The note rejects a split-distribution approach (Plan A) for Mindustry core routing because splitting each conveyor belt into 12 equal shares scales poorly and is complex to deploy. Instead, Plan B merges N belts into 12 groups via routers, directing each group to a dedicated core port, and uses overflow gates to reroute excess when per-port throughput exceeds 4/s. This adopted Plan B achieves O(N) linear complexity, scaling directly with the core’s port count."
body_hash: "b0286b87"
importance: 1.3  # auto
connections:
  - type: idea
    slug: flow-based-thinking
  - type: idea
    slug: mindustry-overflow-priority-routing
---
# Mindustry Resource Routing: Optimizing N Conveyor Lines Merging into the Core

## Problem Model
N resource blocks → individual conveyor belts (0–4/s each) → must merge into the initial core (12 ports, 48/s cap)

Available nodes: Router (≤4 ports, splits evenly), Distributor (≤8 ports, splits evenly)

## Plan A (Rejected)
Split each belt into 12 equal shares → 12 trunk lines → core. Problem: complex to deploy, not scalable when port count exceeds 12.

## Plan B (Adopted)
Don't split, merge instead — group N belts into 12 groups (each ≤4/s), merge each group with a router → direct to core port. When throughput exceeds 4/s, overflow gate redirects to adjacent port. Complexity O(N), scales linearly with core port count.
