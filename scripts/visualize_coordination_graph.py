import networkx as nx
import matplotlib.pyplot as plt


G = nx.read_gexf("data/coordination_graph.gexf")


pos = nx.spring_layout(G, seed=42)


plt.figure(figsize=(8, 5))
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color="skyblue")
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6)
nx.draw_networkx_labels(G, pos, font_size=9, font_weight="bold")


plt.title("PropNet Coordination Graph")
plt.axis("off")
plt.tight_layout()


plt.savefig("data/coordination_graph_visual.png", dpi=300)
print("📷 Saved: data/coordination_graph_visual.png")
