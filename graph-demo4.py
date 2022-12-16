# Depth-First Search Using a LIFO Queue

print("\n" + ("="*60) + "\n\n\tDepth-First Search Using a LIFO Queue\n\n" + ("="*60))

# ----------- DEMO 1
import networkx as nx
from graph import City, load_graph

def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# For statement (Traversal order with nx.dfs_tre())
print("\n\n\tDEMO 1\n" + ("-"*60) + "\n")
for node in nx.dfs_tree(graph, nodes["edinburgh"]):
    print("\t📍", node.name)
    if is_twentieth_century(node.year):
        print("\n\tFound:", node.name, node.year)
        break
else:
    print("\n\tNot Found")


# Now, breadth_first_search() and depth_first_search() functions 
# call search() with the corresponding traversal strategy.
from graph import (
    City,
    load_graph,
    depth_first_traverse,
    depth_first_search as dfs,
)

def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# ----------- DEMO 2
print("\n\n\n\tDEMO 2\n" + ("-"*60) + "\n")
city = dfs(graph, nodes["edinburgh"], is_twentieth_century)
print("\t" + city.name)

# ----------- DEMO 3
print("\n\n\n\tDEMO 3\n" + ("-"*60) + "\n")
for city in depth_first_traverse(graph, nodes["edinburgh"]):
    print("\t" + city.name)

print("\n" + ("="*60))
