import networkx as nx


G = nx.read_gexf("data/propnet_graph.gexf")


G.remove_nodes_from(list(nx.isolates(G)))


nx.write_gml(G, "data/coordination_graph.gml")
print("✅ Coordination graph exported to 'data/coordination_graph.gml'")
