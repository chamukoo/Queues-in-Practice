# Depth-First Search Using a LIFO Queue

import networkx as nx
from graph import City, load_graph

def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# For statement (Traversal order with nx.dfs_tre())
for node in nx.dfs_tree(graph, nodes["edinburgh"]):
    print("📍", node.name)

    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
else:
    print("Not Found")


