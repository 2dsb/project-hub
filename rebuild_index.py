"""Rebuild ideas-index.json from all .md files in idea-lab/ideas/."""
import json
import re
import time
from pathlib import Path

IDEAS_DIR = Path("idea-lab/ideas")
INDEX_PATH = Path("idea-lab/ideas-index.json")


def rebuild_index():
    ideas = []
    for f in sorted(IDEAS_DIR.glob("*.md")):
        content = f.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not m:
            continue
        fm = m.group(1)

        entry = {
            "id": "", "title": "", "tags": [],
            "importance": 1, "connections": [], "summary": "",
        }
        in_tags, in_conn = False, False
        cur = {}

        for line in fm.split("\n"):
            s = line.strip()
            if s.startswith("id:"):
                entry["id"] = s.removeprefix("id:").strip().strip('"')
            elif s.startswith("title:"):
                entry["title"] = s.removeprefix("title:").strip().strip('"').strip("'")
            elif s.startswith("summary:"):
                entry["summary"] = s.removeprefix("summary:").strip().strip('"').strip("'")
            elif s == "tags:":
                in_tags, in_conn = True, False
            elif s == "connections:":
                in_conn, in_tags = True, False
            elif s.startswith("- type:") and in_conn:
                cur = {"type": s.removeprefix("- type:").strip()}
            elif s.startswith("slug:") and in_conn:
                raw = s.removeprefix("slug:").strip().strip('"')
                cur["slug"] = raw.split("#")[0].strip().strip('"')  # strip inline comments
                entry["connections"].append(cur)
                cur = {}
            elif s.startswith("- ") and in_tags:
                entry["tags"].append(s.removeprefix("- ").strip())

        ideas.append(entry)

    index = {"generated": time.strftime("%Y-%m-%d"), "total": len(ideas), "ideas": ideas}
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    return len(ideas)


if __name__ == "__main__":
    count = rebuild_index()
    print(f"ideas-index.json regenerated: {count} ideas")
