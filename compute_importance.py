"""Compute idea importance using undirected PageRank on the connection graph.

- Undirected: connections are treated as mutual links (no hub/authority split)
- Existing importance values != 1 are preserved (manually set)
- Output scaled to 0-10 with one decimal place
"""

import json
import re
from pathlib import Path

import networkx as nx

IDEAS_DIR = Path("idea-lab/ideas")
INDEX_PATH = Path("idea-lab/ideas-index.json")


def build_graph() -> nx.Graph:
    """Build an undirected graph from idea connections."""
    G = nx.Graph()

    for f in sorted(IDEAS_DIR.glob("*.md")):
        content = f.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not m:
            continue
        fm = m.group(1)
        slug = f.stem

        # Extract title and existing importance
        title = ""
        importance = 1
        is_auto = False  # was it auto-generated?
        connections = []
        in_tags = False
        in_conn = False
        cur = {}

        for line in fm.split("\n"):
            s = line.strip()
            if s.startswith("title:"):
                title = s.removeprefix("title:").strip().strip('"').strip("'")
            elif s.startswith("importance:"):
                raw = s.removeprefix("importance:").strip()
                # Strip comment and parse
                raw = raw.split("#")[0].strip()
                try:
                    importance = float(raw)
                except ValueError:
                    pass
            elif s == "tags:":
                in_tags = True
                in_conn = False
            elif s == "connections:":
                in_conn = True
                in_tags = False
            elif in_conn and s.startswith("- type:"):
                cur = {"type": s.removeprefix("- type:").strip()}
            elif in_conn and s.startswith("slug:"):
                raw = s.removeprefix("slug:").strip().strip('"')
                cur["slug"] = raw.split("#")[0].strip().strip('"')
                connections.append(cur)
                cur = {}
            elif in_conn and not s.startswith(("- ", "slug:")):
                in_conn = False

        # Only idea-to-idea connections where the target file exists
        idea_conns = [
            c for c in connections
            if c.get("type") == "idea" and (IDEAS_DIR / f"{c['slug']}.md").exists()
        ]

        # -1  → manual "very important" tag, never overwrite
        # everything else → auto (PageRank overwrites each run)
        manual = importance == -1

        G.add_node(slug, title=title, importance=importance, manual=manual)

        for conn in idea_conns:
            other = conn["slug"]
            G.add_edge(slug, other)

    return G


def compute_pagerank(G: nx.Graph) -> dict:
    """Run undirected PageRank on the graph."""
    # networkx pagerank on undirected graph treats edges as bidirectional
    pr = nx.pagerank(G, alpha=0.85, max_iter=100, tol=1e-6)
    return pr


def scale_scores(pr: dict) -> dict:
    """Scale PageRank values to 0–10, preserving relative differences."""
    values = list(pr.values())
    if not values:
        return {}

    min_val = min(values)
    max_val = max(values)

    if max_val == min_val:
        return {k: 5.0 for k in pr}

    scaled = {}
    for k, v in pr.items():
        # Linear scale to 0–10
        scaled[k] = round((v - min_val) / (max_val - min_val) * 10, 2)

    return scaled


def write_importance(G: nx.Graph, scores: dict, dry_run: bool = False) -> dict:
    """Write importance scores back to .md files. Preserve manual values."""
    stats = {"updated": 0, "preserved": 0, "total": 0}

    for slug in G.nodes:
        data = G.nodes[slug]
        stats["total"] += 1

        if data.get("manual"):
            stats["preserved"] += 1
            continue

        new_score = scores.get(slug, 1.0)
        filepath = IDEAS_DIR / f"{slug}.md"

        if not filepath.exists():
            continue

        content = filepath.read_text(encoding="utf-8")

        # Only modify the frontmatter, not the body
        m = re.match(r"^(---\s*\n)(.*?)(\n---\s*\n.*)", content, re.DOTALL)
        if not m:
            continue
        before, fm, after = m.group(1), m.group(2), m.group(3)

        new_fm = re.sub(
            r"^importance:\s*[\d.]+.*$",
            f"importance: {new_score}  # auto",
            fm,
            flags=re.MULTILINE,
        )

        if not dry_run:
            tmp = filepath.with_suffix(".tmp")
            tmp.write_text(f"{before}{new_fm}{after}", encoding="utf-8")
            os.replace(tmp, filepath)
        stats["updated"] += 1

    return stats


def main():
    import sys
    dry_run = "--dry-run" in sys.argv

    print("Building undirected connection graph...")
    G = build_graph()
    print(f"  Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")

    manual_count = sum(1 for n in G.nodes if G.nodes[n].get("manual"))
    print(f"  Manual importance (preserved): {manual_count}")

    print("Computing undirected PageRank...")
    pr = compute_pagerank(G)

    # Show top/bottom
    sorted_pr = sorted(pr.items(), key=lambda x: x[1], reverse=True)
    print(f"\n  Top 5:")
    for slug, score in sorted_pr[:5]:
        title = G.nodes[slug].get("title", slug)
        print(f"    {score:.6f}  {title}")
    print(f"\n  Bottom 5:")
    for slug, score in sorted_pr[-5:]:
        title = G.nodes[slug].get("title", slug)
        print(f"    {score:.6f}  {title}")

    print("\nScaling to 0–10...")
    scores = scale_scores(pr)

    print(f"  Range: {min(scores.values())} – {max(scores.values())}")

    print(f"\nWriting importance scores ({'DRY RUN' if dry_run else 'LIVE'})...")
    stats = write_importance(G, scores, dry_run=dry_run)

    print(f"  Updated: {stats['updated']}")
    print(f"  Preserved (manual): {stats['preserved']}")
    print(f"  Total: {stats['total']}")

    if dry_run:
        print("\n(Dry run — no files modified. Remove --dry-run to write.)")


if __name__ == "__main__":
    main()
