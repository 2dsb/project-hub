"""Compute connection suggestions using embedding similarity.

For each idea, find semantically similar ideas that aren't already connected.
Uses Top-N + Gap Detection to avoid forcing low-quality suggestions.
"""

import json
from pathlib import Path
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from frontmatter_utils import parse_idea

IDEAS_DIR = Path("idea-lab/ideas")
OUTPUT_PATH = Path("idea-lab/connection-suggestions.json")
MAX_CANDIDATES = 20  # pool size for gap detection
MIN_SCORE = 0.50     # absolute floor — below this, never suggest
MIN_GAP = 0.06       # minimum gap to trigger a cut — smaller gaps mean scores are all close
MAX_SUGGESTIONS = 15 # hard cap per idea
BODY_MAX_CHARS = 300


def apply_gap_detection(candidates: list) -> list:
    """Filter candidates by finding the natural gap in similarity scores.

    Candidates are [(slug, title, score), ...] sorted descending.
    Finds the biggest score drop and cuts off everything after it.
    Then applies MIN_SCORE floor.
    """
    if not candidates:
        return []

    scores = [c[2] for c in candidates]

    # Find the index of the largest drop between consecutive scores
    max_gap = 0
    gap_idx = len(scores)  # default: keep all
    for i in range(1, len(scores)):
        gap = scores[i - 1] - scores[i]
        if gap > max_gap:
            max_gap = gap
            gap_idx = i

    # Only cut if the gap is meaningful — scores that are all close together
    # don't have a real semantic cliff, so keep all candidates
    if max_gap < MIN_GAP:
        gap_idx = len(scores)

    # Keep everything BEFORE the biggest gap (or all if no real gap)
    kept = candidates[:gap_idx]

    # Apply minimum score floor
    kept = [c for c in kept if c[2] >= MIN_SCORE]

    # Hard cap
    kept = kept[:MAX_SUGGESTIONS]

    return kept


def main():
    print("Loading model...")
    model = SentenceTransformer("all-mpnet-base-v2")

    print(f"Reading ideas from {IDEAS_DIR}...")
    ideas = []
    for md_file in sorted(IDEAS_DIR.glob("*.md")):
        idea = parse_idea(md_file)
        if not idea:
            continue

        tag_str = " ".join(f"#{t}" for t in idea["tags"])
        # Use summary if available, fall back to body[:300] for backwards compatibility
        text_source = idea["summary"] if idea["summary"] else idea["body"][:BODY_MAX_CHARS]
        text_for_embedding = f"{idea['title']}. {tag_str}. {text_source}"

        existing_slugs = {conn["slug"] for conn in idea["connections"]}

        ideas.append({
            "slug": idea["slug"],
            "title": idea["title"],
            "text": text_for_embedding,
            "existing_connections": existing_slugs,
        })

    texts = [i["text"] for i in ideas]
    slugs = [i["slug"] for i in ideas]

    print(f"Embedding {len(ideas)} ideas...")
    embeddings = model.encode(texts, show_progress_bar=True)

    print("Computing similarity matrix...")
    sim_matrix = cosine_similarity(embeddings)

    print(f"Generating suggestions (gap detection, min={MIN_SCORE}, max_candidates={MAX_CANDIDATES})...")
    suggestions = []
    stats = {"counts": {}, "scores": []}

    for i, idea in enumerate(ideas):
        scores = sim_matrix[i]
        ranked = sorted(
            [(j, scores[j]) for j in range(len(scores)) if j != i],
            key=lambda x: x[1],
            reverse=True,
        )

        # Pool top candidates not already connected
        pool = []
        for j, score in ranked:
            other_slug = slugs[j]
            if other_slug not in idea["existing_connections"]:
                pool.append((other_slug, ideas[j]["title"], round(float(score), 4)))
            if len(pool) >= MAX_CANDIDATES:
                break

        # Apply gap detection
        filtered = apply_gap_detection(pool)

        if filtered:
            suggestions.append({
                "slug": idea["slug"],
                "title": idea["title"],
                "suggestions": [
                    {"slug": s[0], "title": s[1], "score": s[2]}
                    for s in filtered
                ],
            })
            n = len(filtered)
            stats["counts"][str(n)] = stats["counts"].get(str(n), 0) + 1
            for s in filtered:
                stats["scores"].append(s[2])
        else:
            stats["counts"]["0"] = stats["counts"].get("0", 0) + 1

    # Write output
    output = {
        "model": "all-mpnet-base-v2",
        "method": "top-N + gap detection",
        "min_score": MIN_SCORE,
        "max_candidates": MAX_CANDIDATES,
        "generated": "2026-08-01",
        "total_ideas": len(ideas),
        "ideas_with_suggestions": len(suggestions),
        "total_suggestions": sum(len(s["suggestions"]) for s in suggestions),
        "stats": {
            "suggestion_count_distribution": dict(sorted(stats["counts"].items(), key=lambda x: int(x[0]))),
            "score_range": {
                "min": round(min(stats["scores"]), 4) if stats["scores"] else None,
                "max": round(max(stats["scores"]), 4) if stats["scores"] else None,
                "avg": round(sum(stats["scores"]) / len(stats["scores"]), 4) if stats["scores"] else None,
            },
        },
        "suggestions": suggestions,
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nDone!")
    print(f"  Ideas with suggestions: {output['ideas_with_suggestions']}/{output['total_ideas']}")
    print(f"  Total suggestions: {output['total_suggestions']}")
    print(f"  Distribution: {output['stats']['suggestion_count_distribution']}")
    print(f"  Score range: {output['stats']['score_range']}")
    print(f"  Output: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
