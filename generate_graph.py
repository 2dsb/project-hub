"""Generate an interactive relationship graph for all ideas.

Output: idea-lab/graph.html — open in browser.
Default view hides nodes with <= 1 connection (toggle to show all).
"""

import colorsys
from pathlib import Path
from collections import Counter

import networkx as nx
from networkx.algorithms import community
from pyvis.network import Network
from frontmatter_utils import parse_idea

IDEAS_DIR = Path("idea-lab/ideas")
OUTPUT_PATH = Path("idea-lab/graph.html")

# Layout tuning
SPRING_LENGTH = 250
MIN_CONN_FILTER = 2  # hide nodes with <= this many connections in default view


def build_graph_from_files() -> nx.Graph:
    """Build graph by reading .md files directly (connections use slugs not ids)."""
    G = nx.Graph()

    # Collect all valid slugs for edge validation
    all_slugs = {f.stem for f in IDEAS_DIR.glob("*.md")}

    for f in sorted(IDEAS_DIR.glob("*.md")):
        idea = parse_idea(f)
        if not idea:
            continue

        slug = idea["slug"]
        idea_conns = [c for c in idea["connections"] if c.get("type") == "idea" and c.get("slug") in all_slugs]

        G.add_node(
            slug,
            title=idea["title"],
            tags=idea["tags"],
            summary=idea["summary"][:120],
            importance=idea["importance"],
            conn_count=len(idea_conns),
        )

        # Add edges — undirected graph handles dedup automatically
        for conn in idea_conns:
            other = conn["slug"]
            G.add_edge(slug, other)

    return G


def detect_communities(G: nx.Graph) -> dict:
    """Assign each node to a community (color group). Returns {node_id: community_id}.

    Small communities (< 5 nodes) are merged into a single "misc" group (-1)
    so that only major clusters get distinct colors.
    """
    if G.number_of_edges() == 0:
        return {n: 0 for n in G.nodes}

    try:
        comms = community.louvain_communities(G, seed=42)
    except Exception:
        comms = list(nx.connected_components(G))

    # Sort communities by size (largest first)
    comms = sorted(comms, key=len, reverse=True)

    # Assign IDs: large communities get 0, 1, 2...; small ones get -1
    node_to_comm = {}
    for i, comm in enumerate(comms):
        cid = i if len(comm) >= 3 else -1
        for node in comm:
            node_to_comm[node] = cid

    return node_to_comm


def render_graph(G: nx.Graph, communities: dict, output_path: Path):
    """Render the graph to an interactive HTML file using pyvis."""
    # Curated palette of 20 visually distinct colors (hand-picked for contrast)
    palette_20 = [
        "#4e79a7", "#f28e2b", "#e15759", "#76b7b2", "#59a14f",
        "#edc948", "#b07aa1", "#ff9da7", "#9c755f", "#bab0ac",
        "#6a3d9a", "#b15928", "#33a02c", "#1f78b4", "#fb9a99",
        "#e31a1c", "#fdbf6f", "#cab2d6", "#a6cee3", "#b2df8a",
    ]
    n_large = max(1, sum(1 for c in set(communities.values()) if c >= 0))
    palette = palette_20[:n_large]
    # If more communities than palette entries, generate extras
    if n_large > len(palette_20):
        for i in range(len(palette_20), n_large):
            hue = (i * 137.5) % 360  # golden angle for good separation
            r, g, b = colorsys.hls_to_rgb(hue / 360, 0.50, 0.65)
            palette.append(f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}")

    net = Network(
        height="100vh",
        width="100%",
        bgcolor="#1a1a2e",
        font_color="#e0e0e0",
        directed=False,
    )

    # Physics tuning
    net.force_atlas_2based(
        gravity=-50,
        central_gravity=0.01,
        spring_length=SPRING_LENGTH,
        spring_strength=0.08,
        damping=0.4,
    )

    # Find min/max for scaling
    conn_values = [G.nodes[n].get("conn_count", 0) for n in G.nodes]
    max_conn = max(conn_values) if conn_values else 1
    min_conn = min(conn_values) if conn_values else 0

    for node in G.nodes:
        data = G.nodes[node]
        conn = data.get("conn_count", 0)
        comm = communities.get(node, 0)
        if comm < 0:
            color = "#555566"  # gray for small communities
        else:
            color = palette[comm % len(palette)]

        # Node size: scale between 8 and 40 based on connections
        if max_conn > min_conn:
            size = 8 + (conn - min_conn) / (max_conn - min_conn) * 32
        else:
            size = 20

        # Is this a "core" node?
        is_core = conn >= MIN_CONN_FILTER

        # Build tooltip
        summary = data.get("summary", "")
        tags_str = ", ".join(data.get("tags", [])[:5])
        tooltip = f"<b>{data['title']}</b><br>"
        tooltip += f"<i>{tags_str}</i><br>"
        tooltip += f"Connections: {conn}<br>"
        if summary:
            tooltip += f"<br>{summary}"

        # Store core/peripheral in a custom field (NOT 'group' — pyvis drops color when group is set)
        node_group = "core" if is_core else "peripheral"

        net.add_node(
            node,
            label=data["title"][:30] + ("..." if len(data["title"]) > 30 else ""),
            title=tooltip,
            size=size,
            color=color,
            borderWidth=1,
            borderWidthSelected=3,
            nodeGroup=node_group,  # custom attr, vis.js passes it through
        )

    for a, b in G.edges:
        net.add_edge(a, b, color="#555577", width=0.5, hoverWidth=2)

    # Add controls: toggle button, search box, node count
    controls_html = """
    <div id="controls" style="position:fixed;top:10px;left:10px;z-index:1000;display:flex;gap:8px;align-items:center;flex-wrap:wrap;">
      <button id="toggleBtn" onclick="togglePeripheral()" style="
        padding:8px 16px;background:#4e79a7;color:#fff;border:none;border-radius:4px;
        cursor:pointer;font-size:14px;">
        Show All (190)
      </button>
      <input id="searchBox" type="text" placeholder="Search ideas..." oninput="doSearch()" onkeydown="if(event.key==='Enter')selectFirst()" style="
        padding:6px 12px;background:#2a2a3e;color:#e0e0e0;border:1px solid #555;border-radius:4px;
        font-size:13px;width:200px;outline:none;">
      </input>
      <div id="searchResults" style="display:none;position:absolute;top:42px;left:110px;background:#2a2a3e;
        border:1px solid #555;border-radius:4px;max-height:300px;overflow-y:auto;min-width:300px;z-index:1001;"></div>
      <span id="nodeCount" style="color:#aaa;font-size:13px;"></span>
    </div>
    <script>
      var showingAll = false;
      var totalNodes = """ + str(G.number_of_nodes()) + """;
      var coreCount = """ + str(sum(1 for n in G.nodes if G.nodes[n].get("conn_count", 0) >= MIN_CONN_FILTER)) + """;

      function updateUI() {
        var btn = document.getElementById("toggleBtn");
        var count = document.getElementById("nodeCount");
        if (showingAll) {
          btn.textContent = "Core Only (" + coreCount + ")";
          count.textContent = "Showing all " + totalNodes + " nodes";
        } else {
          btn.textContent = "Show All (" + totalNodes + ")";
          count.textContent = "Showing " + coreCount + " core nodes (>=""" + str(MIN_CONN_FILTER) + """ connections)";
        }
      }

      function togglePeripheral() {
        showingAll = !showingAll;
        var items = network.body.data.nodes.get();
        items.forEach(function(n) {
          var isCore = n.nodeGroup === "core";
          n.hidden = showingAll ? false : !isCore;
        });
        network.body.data.nodes.update(items);
        updateUI();
      }

      // --- Search ---
      function doSearch() {
        var q = document.getElementById("searchBox").value.toLowerCase().trim();
        var results = document.getElementById("searchResults");
        if (!q) { results.style.display = "none"; return; }

        var allNodes = network.body.data.nodes.get();
        var matches = allNodes.filter(function(n) {
          var label = (n.label || "").toLowerCase();
          var title = (n.title || "").toLowerCase();
          return label.indexOf(q) >= 0 || title.indexOf(q) >= 0;
        });

        if (matches.length === 0) {
          results.innerHTML = '<div style="padding:8px 12px;color:#888;">No matches</div>';
          results.style.display = "block";
        } else if (matches.length === 1) {
          // Single match: focus and select it
          focusNode(matches[0].id);
          results.style.display = "none";
        } else {
          var html = "";
          matches.slice(0, 15).forEach(function(n, i) {
            html += '<div data-nid="' + n.id + '" onmousedown="focusNode(this.dataset.nid)" style="padding:6px 12px;cursor:pointer;color:#e0e0e0;'
              + (i === 0 ? 'background:#4e79a7;' : '')
              + '" onmouseenter="this.style.background=\\'#4e79a7\\'" onmouseleave="this.style.background=\\'\\'">'
              + (n.label || n.id) + '</div>';
          });
          if (matches.length > 15) html += '<div style="padding:6px 12px;color:#888;">... and ' + (matches.length - 15) + ' more</div>';
          results.innerHTML = html;
          results.style.display = "block";
        }
      }

      function selectFirst() {
        var results = document.getElementById("searchResults");
        var first = results.querySelector("div");
        if (first && first.onmousedown) first.onmousedown();
      }

      function focusNode(nodeId) {
        // Unhide the node if hidden
        var items = network.body.data.nodes.get();
        items.forEach(function(n) {
          if (n.id === nodeId) n.hidden = false;
        });
        network.body.data.nodes.update(items);
        // Select and focus
        network.selectNodes([nodeId]);
        network.focus(nodeId, {scale: 1.5, animation: true});
        document.getElementById("searchResults").style.display = "none";
        document.getElementById("searchBox").value = "";
      }

      // Click outside to close search results
      document.addEventListener("click", function(e) {
        if (!e.target.closest("#searchBox") && !e.target.closest("#searchResults")) {
          document.getElementById("searchResults").style.display = "none";
        }
      });

      // Hide peripheral nodes on load
      setTimeout(function() {
        var items = network.body.data.nodes.get();
        items.forEach(function(n) {
          if (n.nodeGroup !== "core") n.hidden = true;
        });
        network.body.data.nodes.update(items);
        updateUI();
      }, 500);
    </script>
    """

    html = net.generate_html()
    # Inject controls before </body>
    html = html.replace("</body>", controls_html + "\n</body>")

    # Add title
    title_html = """
    <div style="position:fixed;top:10px;right:20px;z-index:1000;color:#aaa;font-size:13px;text-align:right;">
      <b style="color:#e0e0e0;font-size:16px;">idea-lab relationship graph</b><br>
      nodes sized by connection count · colored by community · drag to explore
    </div>
    """
    html = html.replace("</body>", title_html + "\n</body>")

    output_path.write_text(html, encoding="utf-8")
    return net


def main():
    print("Building graph from idea files...")
    G = build_graph_from_files()

    print(f"  Nodes: {G.number_of_nodes()}")
    print(f"  Edges: {G.number_of_edges()}")

    # Connection stats
    conn_values = [G.nodes[n].get("conn_count", 0) for n in G.nodes]
    core = sum(1 for c in conn_values if c >= MIN_CONN_FILTER)
    peripheral = sum(1 for c in conn_values if c < MIN_CONN_FILTER)
    print(f"  Core (>={MIN_CONN_FILTER} conns): {core}")
    print(f"  Peripheral (<{MIN_CONN_FILTER} conns): {peripheral}")

    print("Detecting communities...")
    communities = detect_communities(G)
    n_large = sum(1 for c in set(communities.values()) if c >= 0)
    n_misc = sum(1 for c in communities.values() if c < 0)
    print(f"  Large communities: {n_large}, Misc (small): {n_misc}")

    print(f"Rendering graph to {OUTPUT_PATH}...")
    render_graph(G, communities, OUTPUT_PATH)
    print(f"  Done! Open {OUTPUT_PATH} in browser.")


if __name__ == "__main__":
    main()
