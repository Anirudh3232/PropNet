import pandas as pd
import re
import networkx as nx
import os

# Step 1: Ensure 'data/' folder exists
os.makedirs("data", exist_ok=True)

# Step 2: Load the dataset
df = pd.read_csv("../data/Truth_Seeker_Model_Dataset.csv")


df = df[["author", "tweet"]].dropna()


def extract_mentions(text):
    return re.findall(r"@\w+", text)


edges = []

for _, row in df.iterrows():
    author = row["author"]
    mentions = extract_mentions(str(row["tweet"]))
    for mention in mentions:
        edges.append((author, mention))


G = nx.DiGraph()
G.add_edges_from(edges)


print("\n Graph Summary:")
print(f"Total nodes: {G.number_of_nodes()}")
print(f"Total edges: {G.number_of_edges()}")


nx.write_gexf(G, "data/propnet_graph.gexf")
print(" Graph saved to 'data/propnet_graph.gexf'")
