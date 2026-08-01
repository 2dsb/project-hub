---
id: idea-20260608-mr01
title: Mindustry Resource Routing: Optimizing N Conveyor Lines Merging into the Core
tags:
  - mindustry
  - logistics
  - routing
  - optimization
  - game-design
summary: "In Mindustry logistics, the optimal way to route N conveyor belts into the core is to avoid splitting each belt into 12 shares and instead merge belts into groups capped at 4 items per second, then feed each group into a core port via a Router. If a group's throughput exceeds the 4/s port limit, an overflow gate redirects surplus items to an adjacent port, scaling linearly with core port count. This merge-based approach (Plan B) keeps deployment complexity O(N), whereas the split-based alternative (Plan A) becomes unwieldy and fails to scale when the number of belts or core ports increases."
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
