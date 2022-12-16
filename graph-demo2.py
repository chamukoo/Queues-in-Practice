# Breadth-First Search Using a FIFO Queue

import networkx as nx
from mod.graph import City, load_graph

print("\n\n\n" + ("="*60) + "\n\n\tBreadth-First Search Using a FIFO Queue\n\n" + ("="*60))

def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

def order(neighbors):
    def by_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key=by_latitude, reverse=True))

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# ---------- DEMO 1
print("\n\n\t⭐ DEMO 1\n" + ("-"*60) + "\n")
for node in nx.bfs_tree(graph, nodes["edinburgh"]):
    print("\t📍", node.name)
    if is_twentieth_century(node.year):
        print("\n\tFound:", node.name, node.year)
        break
else:
    print("\nNot Found")
print("\n" + ("-"*60))


# ---------- DEMO 2
print("\n\n\n\t⭐ DEMO 2\n" + ("-"*60) + "\n")
for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
    print("\t📍", node.name)
    if is_twentieth_century(node.year):
        print("\n\tFound:", node.name, node.year)
        break
else:
    print("\nNot Found")
print("\n" + ("-"*60))


from mod.graph import (
    City, 
    load_graph,
    breadth_first_traverse,
    breadth_first_search as bfs,
)

def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)


# ---------- DEMO 3
# Display city names at Edinburgh in traversal order
print("\n\n\n\t⭐ DEMO 3\n" + ("-"*60) + "\n")
city = bfs(graph, nodes["edinburgh"], is_twentieth_century)
print("\t" + city.name)
print("\n" + ("-"*60))


# ---------- DEMO 4
print("\n\n\n\t⭐ DEMO 4\n" + ("-"*60) + "\n")
for city in breadth_first_traverse(graph, nodes["edinburgh"]):
    print("\t" + city.name)


print("\n" + ("="*60) + "\n\n\n")
