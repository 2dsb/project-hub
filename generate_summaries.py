"""Generate LLM summaries for all idea files, write to YAML frontmatter, regenerate index.

Skips files that already have a summary field (safe to re-run).
"""

import json
import os
import re
import time
from pathlib import Path
from openai import OpenAI

# --- Config ---
API_KEY = "sk-3578289a53ca446fafde6850cc895e68"
BASE_URL = "https://api.deepseek.com"
MODEL = "deepseek-v4-pro"

IDEAS_DIR = Path("idea-lab/ideas")
INDEX_PATH = Path("idea-lab/ideas-index.json")
SUMMARY_MAX_WORDS = 100

# --- Init ---
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

SYSTEM_PROMPT = (
    "You are a precise summarization engine for a personal knowledge base. "
    "Each input is a note with a title, tags, and body text.\n\n"
    "Produce a summary in plain English (no markdown, no bullet points, no preamble). "
    "Output ONLY the summary — never add quotes, labels, or meta-commentary.\n\n"
    "Summary rules:\n"
    "- State the core claim or central question directly.\n"
    "- If the idea argues a position, compress the reasoning into a single connected "
    "sentence (X because Y, therefore Z).\n"
    "- Include specific terminology from the text (technical terms, proper names, "
    "coined phrases) — these anchor the embedding vector.\n"
    "- If the body is very short, restate it faithfully — don't invent content from tags.\n"
    "- Target length: the idea expressed fully, never padded. Short ideas get short "
    "summaries. Aim for 3–6 sentences, up to 100 words."
)


def read_idea(filepath: Path) -> dict | None:
    """Parse an idea .md file. Returns dict with slug, title, tags, body, raw_frontmatter, raw_body."""
    content = filepath.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", content, re.DOTALL)
    if not m:
        return None

    frontmatter = m.group(1)
    body = m.group(2).strip()
    slug = filepath.stem

    title = ""
    tags = []
    in_tags = False

    for line in frontmatter.split("\n"):
        stripped = line.strip()
        if stripped.startswith("title:"):
            title = stripped.removeprefix("title:").strip().strip('"').strip("'")
        elif stripped == "tags:":
            in_tags = True
        elif stripped.startswith("- ") and in_tags:
            tags.append(stripped.removeprefix("- ").strip())
        elif in_tags and not stripped.startswith("- "):
            in_tags = False

    return {
        "slug": slug,
        "title": title,
        "tags": tags,
        "body": body,
        "raw_frontmatter": frontmatter,
        "raw_body": m.group(2),  # including leading newline
    }


def has_summary(frontmatter: str) -> bool:
    """Check if frontmatter already has a non-empty summary field."""
    m = re.search(r'^summary:\s*"?([^"]*)"?', frontmatter, re.MULTILINE)
    if m:
        return len(m.group(1).strip()) > 0
    return False


def generate_summary(title: str, tags: list[str], body: str) -> str:
    """Call DeepSeek API to generate a summary. Retries with higher max_tokens if empty."""
    tag_str = ", ".join(tags) if tags else "none"
    user_prompt = f"Title: {title}\nTags: {tag_str}\nBody:\n{body}"

    for attempt, max_tok in enumerate([600, 1200, 2000]):
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3,
            max_tokens=max_tok,
        )

        msg = resp.choices[0].message
        summary = (msg.content or "").strip()
        summary = summary.strip('"').strip("'")
        finish = resp.choices[0].finish_reason

        if len(summary.split()) >= 5:
            return summary

        # Log why it was empty/short
        print(f"    [attempt {attempt+1}] max_tokens={max_tok}, finish={finish}, "
              f"content_len={len(msg.content or '')}, summary_words={len(summary.split())}")

        if finish == "stop" and len(summary.split()) < 5:
            # Model stopped but gave too little — body might be too short
            if len(body.strip()) < 30:
                # Very short body — just use body as summary directly
                return body.strip()
            # Otherwise retry with higher max_tokens
        elif finish == "length":
            # Hit token limit — definitely need more tokens
            continue
        else:
            # Unknown issue — retry
            continue

    # Last resort: use body[:200] as summary
    fallback = body.strip()[:200]
    print(f"    [fallback] using body snippet as summary ({len(fallback.split())} words)")
    return fallback


def insert_summary_into_frontmatter(frontmatter: str, summary: str) -> str:
    """Insert summary field after the title line (or after tags block). Cleans old summary lines first."""
    lines = frontmatter.split("\n")

    # Remove any existing summary lines (empty or not)
    lines = [l for l in lines if not l.strip().startswith("summary:")]

    # Find where to insert: after the last tag line, or after title line
    insert_idx = 0
    in_tags = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "tags:":
            in_tags = True
            insert_idx = i
        elif in_tags and stripped.startswith("- "):
            insert_idx = i
        elif in_tags and not stripped.startswith("- "):
            in_tags = False

    # insert_idx is now the last tag line (or title line). Insert summary after it.
    summary_line = f'summary: "{summary}"'
    lines.insert(insert_idx + 1, summary_line)
    return "\n".join(lines)


def rebuild_index():
    """Regenerate ideas-index.json from all .md files."""
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
            elif s.startswith("importance:"):
                try:
                    entry["importance"] = float(s.removeprefix("importance:").strip())
                except ValueError:
                    pass
            elif s == "tags:":
                in_tags, in_conn = True, False
            elif s == "connections:":
                in_conn, in_tags = True, False
            elif s.startswith("- type:") and in_conn:
                cur = {"type": s.removeprefix("- type:").strip()}
            elif s.startswith("slug:") and in_conn:
                cur["slug"] = s.removeprefix("slug:").strip().strip('"')
                entry["connections"].append(cur)
                cur = {}
            elif s.startswith("- ") and in_tags:
                entry["tags"].append(s.removeprefix("- ").strip())

        ideas.append(entry)

    index = {"generated": time.strftime("%Y-%m-%d"), "total": len(ideas), "ideas": ideas}
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    return len(ideas)


def main():
    md_files = sorted(IDEAS_DIR.glob("*.md"))
    total = len(md_files)
    done = 0
    skipped = 0
    failed = 0

    print(f"Processing {total} files...\n")

    for i, filepath in enumerate(md_files, 1):
        idea = read_idea(filepath)
        if not idea:
            print(f"  [{i}/{total}] {filepath.stem} — SKIP (parse error)")
            skipped += 1
            continue

        # Check if already has summary
        if has_summary(idea["raw_frontmatter"]):
            print(f"  [{i}/{total}] {idea['slug']} — SKIP (already has summary)")
            skipped += 1
            continue

        # Generate summary
        try:
            summary = generate_summary(idea["title"], idea["tags"], idea["body"])
        except Exception as e:
            print(f"  [{i}/{total}] {idea['slug']} — FAIL ({e})")
            failed += 1
            continue

        # Insert into frontmatter
        new_fm = insert_summary_into_frontmatter(idea["raw_frontmatter"], summary)
        new_content = f"---\n{new_fm}\n---\n{idea['raw_body'].lstrip('\n')}"

        # Write back
        filepath.write_text(new_content, encoding="utf-8")
        done += 1
        print(f"  [{i}/{total}] {idea['slug']} — OK ({len(summary.split())} words)")

        # Brief pause to avoid rate limits
        time.sleep(0.3)

    print(f"\n---")
    print(f"Done: {done}, Skipped: {skipped}, Failed: {failed}")

    # Regenerate index
    if done > 0 or failed > 0:
        count = rebuild_index()
        print(f"ideas-index.json regenerated: {count} ideas")


if __name__ == "__main__":
    main()
