import networkx as nx
from graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# Node 1 is set in Aberdeen
city1 = nodes["aberdeen"]

# Node 2 is set in Perth
city2 = nodes["perth"]

# Display the shortest path in city1 and city2
for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
    print(f"{i}.", " → ".join(city.name for city in path))


