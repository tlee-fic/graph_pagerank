# Thomas Lee
# FI Consulting
# Graph PageRank for Predictive Analytics
# pagerank_2.py


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from pyvis.network import Network
from functions import normalize, prGetColor

# GRAPH NETWORK CONSTRUCTION ======================================================================
# Instantiate NetworkX Graph
N = nx.DiGraph()
# Declare output file name
outputFile = "graph_2.html"
# Declare nodes and edges of graph
nodes, edges = [], []
nodes = [
    1, 2, 3, 4, 5, 6
]
edges = [
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 1],
    [6, 1]
]
# Insert nodes and edges into NetworkX Graph
for node in nodes:
    N.add_node(node)
for edge in edges:
    N.add_edge(edge[0], edge[1])

# PAGERANK EVALUATION =============================================================================
# Compute PageRank of graph nodes
pr = nx.pagerank(N, alpha=0.85)
prSorted = dict(sorted(pr.items(), key=lambda item: item[1]))
# Build PageRank HTML
prData = ""
for key in prSorted:
    prData = "<li>" + str(key) + ": " + str(prSorted[key]) + "</li>" + prData

# EIGENVECTOR CENTRALITY ==========================================================================
ec = nx.eigenvector_centrality(N, max_iter=1000, tol=1e-06)
ecSorted = dict(sorted(ec.items(), key=lambda item: item[1]))
# Build Eigenvector Centrality HTML
ecData = ""
for key in ecSorted:
    ecData = "<li>" + str(key) + ": " + str(ecSorted[key]) + "</li>" + ecData

# OUTPUT VISUALIZATION ============================================================================
# Build Results HTML
resultsHTML = f"""
    <div style="display: flex; gap: 40px;">
        <div>
            <h2>PageRank:</h2>
            <ul>{prData}</ul>
        </div>
        <div>
            <h2>Eigenvector Centrality:</h2>
            <ul>{ecData}</ul>
        </div>
    </div>
"""
# Instantiate Pyvis Network Graph
net = Network(height="600px", width="800px", bgcolor="#222222", font_color="white")
# Insert nodes and edges into Pyvis graph
minPR = min(prSorted.values())
maxPR = max(prSorted.values())
for node in nodes:
    normScore = normalize(minPR, maxPR, prSorted[node])
    color = prGetColor(normScore)
    net.add_node(node, label=str(node), color=color)
for edge in edges:
    net.add_edge(*edge, arrows='to')

# Write Pyvis Graph visualization to HTML output file
net.write_html(outputFile)

# Write PageRank to HTML output file
with open(outputFile, "a") as f:
    f.write(resultsHTML)