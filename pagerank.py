# Thomas Lee
# FI Consulting
# Graph PageRank for Predictive Analytics
# pagerank.py


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from pyvis.network import Network
from functions import normalize, prGetColor

# GRAPH NETWORK CONSTRUCTION ======================================================================
# Instantiate NetworkX Graph
N = nx.DiGraph()
# Declare output file name
outputFile = "graph.html"
# Declare nodes and edges of graph
nodes, edges = [], []
nodes = [
    19, 110, 111, 112, 113, 25, 37, 56, 73, 47, 26, 27, 95, 38, 39, 310, 66, 58
]
edges = [
    [19, 110],
    [19, 111],
    [19, 112],
    [112, 113],
    [19, 25],
    [19, 37],
    [19, 56],
    [19, 73],
    [19, 95],
    [112, 26],
    [113, 26],
    [112, 47],
    [113, 47],
    [112, 38],
    [113, 39],
    [112, 66],
    [110, 27],
    [113, 310],
    [110, 58],
    [110, 66]
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
prHTML = f"""
    <div>
        <h2> PageRank: </h2>
        <p> {prData} </p>
    </div>
"""

# OUTPUT VISUALIZATION ============================================================================
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
    f.write(prHTML)