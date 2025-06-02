import networkx as nx
import matplotlib.pyplot as plt


G = nx.read_gexf("data/propnet_graph.gexf")


if not nx.is_empty(G):
    largest_cc = max(nx.weakly_connected_components(G), key=len)
    G = G.subgraph(largest_cc).copy()


pos = nx.spring_layout(G, seed=42)


plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_size=60, node_color='skyblue')
nx.draw_networkx_edges(G, pos, alpha=0.2)
nx.draw_networkx_labels(G, pos, font_size=6)


plt.title("PropNet Mention Graph", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.savefig("data/propnet_graph_visual.png", dpi=300)
print(" Graph saved as 'data/propnet_graph_visual.png'")
