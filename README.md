PropNet: Coordinated Propaganda Detection on Twitter

PropNet is a system designed to identify and visualize coordinated propaganda campaigns on Twitter using clustering, user interaction graphs, and coordination detection based on shared narratives. This project leverages machine learning, NLP, and network analysis to analyze user tweets, detect propaganda narratives, and uncover coordinated behavior.

 Project Overview

PropNet consists of two primary pipelines:

Narrative Clustering: Groups similar tweets using sentence embeddings and clustering algorithms.

Coordination Detection: Builds graphs based on shared narratives and user behavior to uncover coordination.


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

Developed by Anirudh Balmuri as a social media analysis project.

->Due to size restrictions and terms of use, the original dataset is not included in this repo.
 Place `Twitter Analysis.csv` in the `data/` folder before running the notebooks.


