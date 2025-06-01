import pandas as pd
import networkx as nx
from itertools import combinations


df = pd.read_csv("data/preprocessed_coordination.csv")


coord_groups = {}

for _, row in df.iterrows():
    key = f"{row['manual_keywords']}__{row['target']}"
    if key not in coord_groups:
        coord_groups[key] = set()
    coord_groups[key].add(row['author'])


G = nx.Graph()


for authors in coord_groups.values():
    for u, v in combinations(authors, 2):
        if G.has_edge(u, v):
            G[u][v]["weight"] += 1
        else:
            G.add_edge(u, v, weight=1)


nx.write_gexf(G, "data/coordination_graph.gexf")
print(f" Coordination graph saved with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
