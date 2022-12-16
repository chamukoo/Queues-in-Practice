# Shortest Path Using Breadth-First Traversal

print("\n\n\n" + ("="*60) + "\n\n\tShortest Path Using Breadth-First Traversal\n\n" + ("="*60))


# ----------- DEMO 1
import networkx as nx
from mod.graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)
city1 = nodes["aberdeen"]   # Node 1 is set in Aberdeen
city2 = nodes["perth"]      # Node 2 is set in Perth

# Display the shortest path in city1 and city2
print("\n\n\t⭐ DEMO 1\n" + ("-"*60) + "\n")
for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
    print("\t" + f"{i}.", " → ".join(city.name for city in path))
print("\n" + ("-"*60))


# ----------- DEMO 2
from mod.graph import shortest_path

# The first path follows the natural order of neighbors from the DOT file
print("\n\n\n\t⭐ DEMO 2 - Shortest Path by Natural Order\n" + ("-"*60) + "\n")
print("\t" + " → ".join(
    city.name 
    for city in shortest_path(graph, city1, city2)))
print("\n" + ("-"*60))


# ----------- DEMO 3
def by_latitude(city):
    return -city.latitude

# The second one prefers neighbors with a higher latitude
print("\n\n\n\t⭐ DEMO 3 - Shortest path by Latitude\n" + ("-"*60) + "\n")
print("\t" + " → ".join(
    city.name
    for city in shortest_path(graph, city1, city2, by_latitude)
))
print("\n" + ("-"*60))


# ----------- DEMO 4
from mod.graph import connected

# Dsiplay whether the two nodes are connected
print("\n\n\n\t⭐ DEMO 4 - Determine the Connection\n" + ("-"*60) + "\n")
print("\t", f"{'Belfast → Glasgow:':<20s}", connected(graph, nodes["belfast"], nodes["glasgow"]))
print("\t", f"{'Belfast → Derry:':<20s}", connected(graph, nodes["belfast"], nodes["derry"]))

print("\n" + ("="*60) + "\n\n\n")
