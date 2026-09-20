---
id: idea-20260915-ai-task-cost-bounds
title: "What Bounds an AI Task's Cost — Detectable and Convergent Errors"
tags:
  - ai-limits
  - task-estimation
  - error-convergence
  - verifiability
  - tool-selection
  - native-form
  - cost-estimation
summary: "A task's cost is bounded only when its errors are both detectable and convergent, and AI image work fails both, which is why it has no reliable estimate. The estimate failed because it was priced off the happy path, whereas in AI work the retry loop is the cost and has no natural ceiling. Errors are detectable when you can tell an output is wrong without redoing the work, and convergent when retrying moves toward correct; if either property is missing, cost has no upper bound. Image work sits in the unbounded region because the model's native form is text, so coercing images in and out degrades detectability and produces non-deterministic re-renderings that prevent convergence. For such tasks, bound the work externally by timeboxing and sending what is verified rather than what is complete."
body_hash: "69274700"
importance: 0.0  # auto
---
# What Bounds an AI Task's Cost — Detectable and Convergent Errors

**One sentence**: A task's cost is bounded only when its errors are both *detectable* and *convergent* — and AI image work fails both, which is why it has no reliable estimate.

## The Event

After a lecture, the job was to clean up images and send the organized result the same day. The estimate assumed the AI would handle the images with maybe a retry or two. Instead the AI kept erring, and the work ran to 2am.

The estimate wasn't careless. It was **priced off the happy path** — and the happy path is exactly what AI tasks don't reliably have.

## Why the Estimate Failed

The natural estimate for a task is "how long does it take when it works?" For most work that's fine, because failures are cheap and rare. For AI work it's systematically wrong, because the retry loop *is* the cost — and the retry loop has no natural ceiling.

So the question isn't "how long does this take?" It's "how long until it's *done*?" — and whether that's bounded depends on two properties of the task that have nothing to do with how hard it looks.

## The Two Conditions

A task's cost is bounded when errors are both:

**1. Detectable — can you tell the output is wrong without redoing the work?**

If checking the answer costs as much as producing it, you have no cheap verification. You either redo the work yourself or ship something you can't vouch for.

**2. Convergent — does retrying move toward correct?**

If each attempt is an independent draw, retrying doesn't converge. You get a *different* error, not a better one. There is no sequence of attempts that reliably terminates at correct.

When either property is missing, cost has no ceiling. When both are missing, the task is a trap.

| Task | Errors detectable? | Errors convergent? | Cost bounded? |
|---|---|---|---|
| Writing code | Yes — it runs or it doesn't | Yes — fixing the bug fixes it | Yes |
| Text summarization | Roughly — you can skim it | Mostly | Usually |
| Image → text transcription | No — you'd have to read the image yourself | No — a retry yields a different error | **No** |
| Image editing / generation | Partly — it looks right? | No | **No** |

Code is the well-behaved case on both axes, which is why AI-assisted coding feels tractable: a failing test is a *detectable* error, and fixing it is *convergent*. Neither is true of a transcription error in an image.

## Why Images Specifically

The model's native form is text. An image has to be coerced in, and the result coerced back out — and coercion is where the loss happens. This is the general principle that tools should be chosen by **native form**: where the tool's natural material and the data's form mismatch, you pay a conversion price, and here that price is paid in exactly the two properties above. The image is degraded on the way in (so errors aren't reliably detectable) and the output is a non-deterministic re-rendering (so errors aren't convergent).

The practical read is not "AI is bad at images" as a permanent verdict — capability will shift. It's that **image work sits in the region where AI cost is unbounded**, and that region is identified by the two conditions rather than by the modality.

## Implications

- **Estimate the tail, not the mean.** For any AI task, the honest estimate is "how long if it takes N attempts?" — and N has no reliable upper bound when the conditions fail. If you can't answer that, you don't have an estimate.
- **Run the two checks before committing.** Detectable and convergent are answerable in advance, and they predict cost behavior better than how easy the task appears.
- **Prefer tasks where errors are detectable and convergent.** Not because the work is easier, but because the cost is *knowable* — and knowability is what lets you plan, promise, or delegate.
- **When the conditions fail, bound the task externally.** Timebox it and prepare a fallback deliverable (send what's verified, not what's complete). The task won't bound itself.

## Open Questions

- **How do you estimate a non-convergent task at all?** "It might work on the first try, or not at all" isn't an estimate — but some decision still has to be made. A probabilistic framing (expected attempts × per-attempt cost) may be the only honest form.
- **Do the conditions change with model capability?** Detectability and convergence may improve independently as models get better — and the two would matter differently if only one did.
- **Is there a cheap way to make a task detectable?** Building verification for an image task might itself be cheaper than the unbounded retry loop — the tradeoff hasn't been explored.
- **Where else does this pattern live?** Any task whose verification cost approaches its production cost, or whose failures are independent draws rather than corrections, should behave the same way.
