"""Idea-lab maintenance — run all four steps in order.

Usage:
    python maintain.py              # run all steps
    python maintain.py --skip-summaries  # skip API calls (new ideas only)
"""

import subprocess
import sys
import time


STEPS = [
    ("generate_summaries.py", "Generate LLM summaries"),
    ("compute_connections.py", "Compute connection suggestions"),
    ("write_connections.py", "Write connections to .md files"),
    ("compute_importance.py", "Compute idea importance (PageRank)"),
    ("rebuild_index.py", "Rebuild ideas-index.json"),
    ("generate_graph.py", "Generate relationship graph"),
]


def main():
    skip_summaries = "--skip-summaries" in sys.argv

    print("=" * 50)
    print("idea-lab maintenance")
    print("=" * 50)
    print()

    start = time.time()
    failed = []

    total_steps = len(STEPS) - (1 if skip_summaries else 0)
    step_num = 0

    for script, desc in STEPS:
        if skip_summaries and script == "generate_summaries.py":
            print(f"[SKIP] {desc}\n")
            continue

        step_num += 1
        print(f"[{step_num}/{total_steps}] {desc}...")
        step_start = time.time()

        result = subprocess.run(
            [sys.executable, script],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            # Print last line of output (summary line)
            lines = result.stdout.strip().split("\n")
            summary = lines[-1] if lines else "OK"
            elapsed = time.time() - step_start
            print(f"  ✓ {summary} ({elapsed:.1f}s)")
        else:
            elapsed = time.time() - step_start
            print(f"  ✗ FAILED ({elapsed:.1f}s)")
            print(result.stderr.strip()[-300:])
            failed.append(script)

        print()

    total = time.time() - start
    print(f"---")
    print(f"Total: {total:.1f}s, Failed: {len(failed)}")
    if failed:
        print(f"Failed steps: {', '.join(failed)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
