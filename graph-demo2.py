# Breadth-First Search Using a FIFO Queue

import networkx as nx
from graph import City, load_graph

print("\n" + ("="*60) + "\n\n\tBreadth-First Search Using a FIFO Queue\n\n" + ("="*60))

def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

def order(neighbors):
    def by_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key=by_latitude, reverse=True))

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# ---------- DEMO 1
print("\n\n\tDEMO 1\n" + ("-"*60) + "\n")
for node in nx.bfs_tree(graph, nodes["edinburgh"]):
    print("\t📍", node.name)
    if is_twentieth_century(node.year):
        print("\n\tFound:", node.name, node.year)
        break
else:
    print("\nNot Found")

# ---------- DEMO 2
print("\n\n\tDEMO 2\n" + ("-"*60) + "\n")
for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
    print("\t📍", node.name)
    if is_twentieth_century(node.year):
        print("\n\tFound:", node.name, node.year)
        break
else:
    print("\nNot Found")
print("\n" + ("="*60))
