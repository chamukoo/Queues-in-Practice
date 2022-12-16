# Dijkstra’s Algorithm Using a Priority Queue

print("\n" + ("="*60) + "\n\n\tDijkstra’s Algorithm Using a Priority Queue\n\n" + ("="*60))


import networkx as nx
from graph import City, load_graph, dijkstra_shortest_path

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# Setting the two nodes to london and edinburgh
city1 = nodes["london"]
city2 = nodes["edinburgh"]


# --------- DEMO 1
def distance(weights):
    return float(weights["distance"])

print("\n\n\tDEMO 1 - Shortest Path by Distance\n" + ("-"*60) + "\n")
for city in dijkstra_shortest_path(graph, city1, city2,distance):
    print("\t" + city.name)


# --------- DEMO 2
def weight(node1, node2, weights):
    return distance(weights)

print("\n\n\n\tDEMO 2 - Shortest Path by Weight\n" + ("-"*60) + "\n")
for city in nx.dijkstra_path(graph, city1, city2, weight):
    print("\t" + city.name)

print("\n" + ("="*60))
 