"""Shared frontmatter parsing for all idea-lab scripts.

Single source of truth for reading .md idea files. Every script imports
parse_idea() from here instead of writing its own inline parser.

Handles both list-format and bracket-format tags, inline comments on
connection slugs, and the empty-block variants (tags: [], connections: []).
"""

import re
from pathlib import Path


def parse_idea(filepath: Path) -> dict | None:
    """Parse an idea .md file and return all frontmatter fields plus body.

    Returns None if the file has no valid YAML frontmatter delimited by ---.
    """
    content = filepath.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", content, re.DOTALL)
    if not m:
        return None

    fm = m.group(1)
    body = m.group(2)
    slug = filepath.stem

    idea_id = ""
    title = ""
    tags = []
    summary = ""
    importance = 1.0
    connections = []

    in_tags = False
    in_conn = False
    cur = {}

    for line in fm.split("\n"):
        s = line.strip()
        if s.startswith("id:"):
            idea_id = s.removeprefix("id:").strip().strip('"')
        elif s.startswith("title:"):
            title = s.removeprefix("title:").strip().strip('"').strip("'")
        elif s.startswith("summary:"):
            # Unescape \" → " and \\ → \ for display
            raw = s.removeprefix("summary:").strip().strip('"').strip("'")
            summary = raw.replace('\\"', '"').replace("\\\\", "\\")
        elif s.startswith("importance:"):
            raw = s.removeprefix("importance:").strip().split("#")[0].strip()
            try:
                importance = float(raw)
            except ValueError:
                pass
        elif s in ("tags:", "tags: []"):
            in_tags = True
            in_conn = False
        elif s in ("connections:", "connections: []"):
            in_conn = True
            in_tags = False
        elif in_conn and s.startswith("- type:"):
            cur = {"type": s.removeprefix("- type:").strip()}
        elif in_conn and s.startswith("slug:"):
            raw = s.removeprefix("slug:").strip().strip('"')
            cur["slug"] = raw.split("#")[0].strip().strip('"')  # strip inline comments
            connections.append(cur)
            cur = {}
        elif in_conn and not s.startswith(("- ", "slug:")):
            in_conn = False
        elif in_tags and s.startswith("- "):
            tags.append(s.removeprefix("- ").strip())
        elif in_tags and not s.startswith("- "):
            in_tags = False
        elif s.startswith("tags: [") or s.startswith('tags: ["'):
            # Bracket format: tags: [a, b, c] or tags: ["a", "b"]
            raw = s.removeprefix("tags:").strip().strip("[]")
            tags = [t.strip().strip('"').strip("'") for t in raw.split(",") if t.strip()]
            in_tags = False

    return {
        "id": idea_id,
        "slug": slug,
        "title": title,
        "tags": tags,
        "summary": summary,
        "importance": importance,
        "connections": connections,
        "body": body.strip(),
        "raw_frontmatter": fm,
        "raw_body": body,
    }
