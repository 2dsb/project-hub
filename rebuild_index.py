"""Rebuild ideas-index.json from all .md files in idea-lab/ideas/."""
import json
import time
from pathlib import Path
from frontmatter_utils import parse_idea

IDEAS_DIR = Path("idea-lab/ideas")
INDEX_PATH = Path("idea-lab/ideas-index.json")


def rebuild_index():
    ideas = []
    for f in sorted(IDEAS_DIR.glob("*.md")):
        idea = parse_idea(f)
        if not idea:
            continue

        entry = {
            "id": idea["id"],
            "title": idea["title"],
            "tags": idea["tags"],
            "summary": idea["summary"],
            "importance": idea["importance"],
            "connections": idea["connections"],
        }
        ideas.append(entry)

    index = {"generated": time.strftime("%Y-%m-%d"), "total": len(ideas), "ideas": ideas}
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    return len(ideas)


if __name__ == "__main__":
    count = rebuild_index()
    print(f"ideas-index.json regenerated: {count} ideas")
