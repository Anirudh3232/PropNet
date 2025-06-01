import networkx as nx
import matplotlib.pyplot as plt
import community as community_louvain
import matplotlib.cm as cm


G = nx.read_gexf("data/coordination_graph.gexf")


partition = community_louvain.best_partition(G)


degrees = dict(G.degree())
node_sizes = [degrees[n] * 800 for n in G.nodes]


num_comms = len(set(partition.values()))
cmap = cm.get_cmap('Set2', num_comms)
node_colors = [cmap(partition[n]) for n in G.nodes]


pos = nx.spring_layout(G, seed=42)


plt.figure(figsize=(10, 6))
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes)
nx.draw_networkx_edges(G, pos, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=9, font_weight="bold")

plt.title("PropNet: Coordination Graph with Clusters")
plt.axis("off")
plt.tight_layout()
plt.savefig("data/coordination_graph_clustered.png", dpi=300)
print(" Saved: data/coordination_graph_clustered.png")
