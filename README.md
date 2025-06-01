PropNet: Coordinated Propaganda Detection on Twitter

PropNet is a system designed to identify and visualize coordinated propaganda campaigns on Twitter using clustering, user interaction graphs, and coordination detection based on shared narratives. This project leverages machine learning, NLP, and network analysis to analyze user tweets, detect propaganda narratives, and uncover coordinated behavior.

 Project Overview

PropNet consists of two primary pipelines:

Narrative Clustering: Groups similar tweets using sentence embeddings and clustering algorithms.

Coordination Detection: Builds graphs based on shared narratives and user behavior to uncover coordination.

 Folder Structure

PropNet/
│
├── data/                            # Project datasets and outputs
│   ├── Truth_Seeker_Model_Dataset.csv     # Original dataset for coordination detection
│   ├── Twitter Analysis.csv               # Dataset for narrative clustering
│   ├── preprocessed_coordination.csv      # Cleaned dataset used for building coordination graph
│   ├── coordination_graph.gexf            # GEXF graph of coordinated user connections
│   ├── coordination_graph_clustered.png   # Visualized graph with coordination clusters
│   ├── coordination_graph_visual.png      # Visual representation of raw coordination network
│   ├── propnet_graph.gexf                 # Mention graph based on @mentions
│   ├── propnet_graph_visual.png           # Visual of the mention graph
│   ├── tweet_embeddings.npy               # Encoded tweet vectors using MiniLM
│   ├── label_distribution.png             # Label breakdown of clusters
│
├── notebooks/                      # Jupyter Notebooks
│   ├── topic_clustering.ipynb            # Main notebook for clustering tweets using embeddings
│   └── data/
│       ├── tweet_clusters.png             # Visualization of PCA tweet clusters
│       ├── tweet_embeddings.npy           # Embeddings used for clustering
│       └── tweets_with_clusters.csv       # Final output of cluster-labeled tweets
│
├── scripts/                        # Python scripts for modular processing
│   ├── build_user_graph.py              # Generates mention graph (propnet_graph)
│   ├── build_coordination_graph.py      # Builds coordination graph from shared narratives
│   ├── export_coordination_graph.py     # Exports coordination GEXF as GML for further use
│   ├── analyze_coordination_graph.py    # Loads and analyzes coordination graph structure
│   ├── visualize_coordination_graph.py  # Plots coordination graphs
│   ├── visualize_graph.py               # Plots mention graph
│   ├── load_truthseeker_data.py         # Handles dataset preprocessing
│   └── preprocess_for_coordination.py   # Extracts narrative-target pairs for coordination
│
└── README.md                      # Project documentation

How to Run:-

Clone the repository and install dependencies in a virtual environment.

Run the scripts from the scripts/ folder step by step.

Explore results via visualizations in the data/ folder and notebooks.

python scripts/build_user_graph.py
python scripts/preprocess_for_coordination.py
python scripts/build_coordination_graph.py

Requirements:-

The following packages are required
pandas
numpy
matplotlib
networkx
sentence-transformers
scikit-learn
python-louvain

 Technologies Used:-

Python 3.11

NetworkX

Pandas, NumPy

Sentence-Transformers (MiniLM)

Matplotlib / Seaborn

Jupyter Notebooks

Files to Ignore in GitHub:-

These are large or unnecessary for  release:

venv/                    # Python virtual environment
__pycache__/             # Compiled files
*.npy                    # Raw embeddings
*.gexf, *.gml            # Optional if not visualizing
*.png                    # Optional if regenerating visuals
notebooks/data/          # Only needed if not running notebook again

 Outputs:-

Narrative clusters based on tweet content

Coordination graphs (users sharing similar narratives)

Mention graphs showing interaction patterns

Final CSV with cluster labels for narrative inspection

 Author:-

Developed by Anirudh Balmuri as part of a research-driven social media analysis project.

