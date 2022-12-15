# Depth-First Search Using a LIFO Queue

import networkx as nx
from queues_demo.graph import City, load_graph

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


# Now, breadth_first_search() and depth_first_search() functions 
# call search() with the corresponding traversal strategy.
from queues_demo.graph import (
    City,
    load_graph,
    depth_first_traverse,
    depth_first_search as dfs,
)

city = dfs(graph, nodes["edinburgh"], is_twentieth_century)
print(city.name)

for city in depth_first_traverse(graph, nodes["edinburgh"]):
    print(city.name)
