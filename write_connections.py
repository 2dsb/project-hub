"""Write connection suggestions back to .md files.

- High confidence (>= 0.60): write directly as regular connections
- Low confidence (0.50-0.60): write with a "review" flag for later manual check
- Skips connections that already exist (idempotent)
"""

import json
import os
import re
from pathlib import Path
from frontmatter_utils import parse_idea

IDEAS_DIR = Path("idea-lab/ideas")
SUGGESTIONS_PATH = Path("idea-lab/connection-suggestions.json")
HIGH_CONFIDENCE = 0.60


def write_connections(suggestions_path: Path, dry_run: bool = False) -> dict:
    """Write connection suggestions to .md files. Returns stats."""
    if not suggestions_path.exists():
        print(f"  WARN: {suggestions_path} not found -- run compute_connections.py first")
        return {"written_high": 0, "written_low": 0, "skipped_existing": 0, "files_touched": 0}

    data = json.loads(suggestions_path.read_text(encoding="utf-8"))

    stats = {"written_high": 0, "written_low": 0, "skipped_existing": 0, "files_touched": 0}

    for entry in data["suggestions"]:
        slug = entry["slug"]
        filepath = IDEAS_DIR / f"{slug}.md"
        if not filepath.exists():
            print(f"  WARN: {slug} not found, skipping")
            continue

        idea = parse_idea(filepath)
        if not idea:
            print(f"  WARN: {slug} parse error, skipping")
            continue

        # Existing connection slugs from shared parser
        existing_slugs = {conn["slug"] for conn in idea["connections"]}

        # Build new connection lines
        new_lines = []
        for sug in entry["suggestions"]:
            if sug["slug"] in existing_slugs:
                stats["skipped_existing"] += 1
                continue

            if sug["score"] >= HIGH_CONFIDENCE:
                new_lines.append(f'  - type: idea\n    slug: "{sug["slug"]}"  # auto')
                stats["written_high"] += 1
            else:
                new_lines.append(f'  - type: idea\n    slug: "{sug["slug"]}"  # auto, review: {sug["score"]:.3f}')
                stats["written_low"] += 1

        if not new_lines:
            continue

        # Find the connections section in raw frontmatter
        lines = idea["raw_frontmatter"].split("\n")
        conn_start = -1
        conn_end = -1
        in_conn = False
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped in ("connections:", "connections: []"):
                conn_start = i
                in_conn = True
                if stripped == "connections: []":
                    lines[i] = "connections:"  # replace empty inline list with block start
            elif in_conn and stripped.startswith("- type:"):
                conn_end = i
            elif in_conn and stripped.startswith("slug:"):
                conn_end = i
            elif in_conn and not stripped.startswith(("- ", "  ", "slug:")):
                in_conn = False

        if conn_start >= 0:
            # Insert new lines after last connection entry
            insert_at = max(conn_end, conn_start)
            for j, new_line in enumerate(new_lines):
                lines.insert(insert_at + 1 + j, new_line)
        else:
            # No connections section -- create one before the closing ---
            lines.append("connections:")
            for new_line in new_lines:
                lines.append(new_line)

        new_fm = "\n".join(lines)
        new_content = f"---\n{new_fm}\n---\n{idea['raw_body'].lstrip(chr(10))}"

        if not dry_run:
            tmp = filepath.with_suffix(".tmp")
            tmp.write_text(new_content, encoding="utf-8")
            os.replace(tmp, filepath)
        stats["files_touched"] += 1

    return stats


def main():
    import sys
    dry_run = "--dry-run" in sys.argv

    print(f"Reading suggestions from {SUGGESTIONS_PATH}...")
    print(f"High confidence threshold: >= {HIGH_CONFIDENCE}")
    print(f"Mode: {'DRY RUN' if dry_run else 'WRITE'}")
    print()

    stats = write_connections(SUGGESTIONS_PATH, dry_run=dry_run)

    print(f"---")
    print(f"Files touched: {stats['files_touched']}")
    print(f"High confidence (>= {HIGH_CONFIDENCE}): {stats['written_high']}")
    print(f"Low confidence (need review): {stats['written_low']}")
    print(f"Skipped (already exist): {stats['skipped_existing']}")
    print(f"Total new connections: {stats['written_high'] + stats['written_low']}")

    if dry_run:
        print("\n(Dry run -- no files modified. Remove --dry-run to write.)")


if __name__ == "__main__":
    main()
