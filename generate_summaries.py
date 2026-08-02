"""Generate LLM summaries for all idea files, write to YAML frontmatter, regenerate index.

Skips files that already have a summary field (safe to re-run).
"""

import hashlib
import json
import os
import re
import time
from pathlib import Path
from openai import OpenAI
from rebuild_index import rebuild_index
from frontmatter_utils import parse_idea

# --- Config ---
API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
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


def body_hash(body: str) -> str:
    """Short hash of body text for change detection."""
    return hashlib.md5(body.strip().encode()).hexdigest()[:8]


def has_summary(frontmatter: str, body: str) -> bool:
    """Check if frontmatter has a non-empty summary and body hasn't changed."""
    m = re.search(r'^summary:\s*(.*)', frontmatter, re.MULTILINE)
    if not m:
        return False
    summary_val = m.group(1).strip().strip('"').strip("'")
    if len(summary_val) == 0:
        return False
    hm = re.search(r'^body_hash:\s*"?(\w+)"?', frontmatter, re.MULTILINE)
    if hm:
        stored_hash = hm.group(1)
        return stored_hash == body_hash(body)
    # No hash stored — summary exists but hash unknown, regenerate to be safe
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

        if len(summary.split()) >= 5 and finish == "stop":
            return summary

        # Log why it was empty/short
        print(f"    [attempt {attempt+1}] max_tokens={max_tok}, finish={finish}, "
              f"content_len={len(msg.content or '')}, summary_words={len(summary.split())}")

        if finish == "stop" and len(summary.split()) < 5:
            # Model stopped but gave too little — body might be too short
            if len(body.strip()) < 30:
                text = body.strip()
                if not text:
                    return title
                return text
        elif finish == "length":
            continue
        else:
            continue

    # Last resort: use body as summary, flattening newlines
    fallback = body.strip().replace("\n", " ")[:200]
    print(f"    [fallback] using body snippet as summary ({len(fallback.split())} words)")
    return fallback


def insert_summary_and_hash(frontmatter: str, summary: str, body: str) -> str:
    """Insert summary and body_hash fields. Cleans old summary/hash lines first."""
    lines = frontmatter.split("\n")

    # Remove any existing summary and body_hash lines
    lines = [l for l in lines if not l.strip().startswith(("summary:", "body_hash:"))]

    # Find where to insert: after the last tag line, or after title line
    insert_idx = 0
    in_tags = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("title:"):
            insert_idx = i
        elif stripped == "tags:":
            in_tags = True
            insert_idx = i
        elif in_tags and stripped.startswith("- "):
            insert_idx = i
        elif in_tags and not stripped.startswith("- "):
            in_tags = False
        elif stripped.startswith("tags: [") or stripped.startswith('tags: ["'):
            insert_idx = i
            in_tags = False

    # Escape backslashes and double quotes for YAML double-quoted string
    escaped = summary.replace("\\", "\\\\").replace('"', '\\"')
    summary_line = f'summary: "{escaped}"'
    hash_line = f'body_hash: "{body_hash(body)}"'
    lines.insert(insert_idx + 1, summary_line)
    lines.insert(insert_idx + 2, hash_line)
    return "\n".join(lines)


def main():
    md_files = sorted(IDEAS_DIR.glob("*.md"))
    total = len(md_files)
    done = 0
    skipped = 0
    failed = 0

    print(f"Processing {total} files...\n")

    for i, filepath in enumerate(md_files, 1):
        idea = parse_idea(filepath)
        if not idea:
            print(f"  [{i}/{total}] {filepath.stem} — SKIP (parse error)")
            skipped += 1
            continue

        # Check if already has summary and body hasn't changed
        if has_summary(idea["raw_frontmatter"], idea["body"]):
            print(f"  [{i}/{total}] {idea['slug']} — SKIP (unchanged)")
            skipped += 1
            continue

        # Generate summary
        try:
            summary = generate_summary(idea["title"], idea["tags"], idea["body"])
        except Exception as e:
            print(f"  [{i}/{total}] {idea['slug']} — FAIL ({e})")
            failed += 1
            continue

        # Insert into frontmatter (with body hash for change detection)
        new_fm = insert_summary_and_hash(idea["raw_frontmatter"], summary, idea["body"])
        new_content = f"---\n{new_fm}\n---\n{idea['raw_body'].lstrip(chr(10))}"

        # Atomic write: temp file then rename (safe against crashes)
        tmp = filepath.with_suffix(".tmp")
        tmp.write_text(new_content, encoding="utf-8")
        os.replace(tmp, filepath)
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
