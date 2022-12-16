# Shortest Path Using Breadth-First Traversal

import networkx as nx
from graph import City, load_graph
from graph import connected

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# Node 1 is set in Aberdeen
city1 = nodes["aberdeen"]

# Node 2 is set in Perth
city2 = nodes["perth"]

# Display the shortest path in city1 and city2
for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
    print(f"{i}.", " → ".join(city.name for city in path))


from graph import shortest_path

# The first path follows the natural order of neighbors from the DOT file
print(" → ".join(
    city.name 
    for city in shortest_path(graph, city1, city2)))


def by_latitude(city):
    return -city.latitude

# The second one prefers neighbors with a higher latitude
print(" → ".join(
    city.name
    for city in shortest_path(graph, city1, city2, by_latitude)
))

# Dsiplay whether the two nodes are connected
print(connected(graph, nodes["belfast"], nodes["glasgow"]))
print(connected(graph, nodes["belfast"], nodes["derry"]))
