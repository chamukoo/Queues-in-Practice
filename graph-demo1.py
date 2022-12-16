# Object Representation of the Cities and Roads


# DEMO 1
import networkx as nx

graph = nx.nx_agraph.read_dot("roadmap.dot")

# Print Statement
print("\n" + ("="*26) + " DEMO 1 " + ("="*26) + "\n")
print(nx.nx_agraph.read_dot("roadmap.dot"))
print(graph.nodes["london"])
print("\n" + ("="*60) + "\n")


# DEMO 2
from graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# Display graphs and nodes in London
print("\n" + ("="*26) + " DEMO 2 " + ("="*26) + "\n")
print(nodes["london"])
print(graph)
print("\n" + ("="*60) + "\n")

# DEMO 3
# Display neighbors in london through for loop
print("\n" + ("="*26) + " DEMO 3 " + ("="*26) + "\n")
for neighbor in graph.neighbors(nodes["london"]):
    print(neighbor.name)
print("\n" + ("="*60) + "\n")


# DEMO 4
# Display weights and neighbors in london through for loop
print("\n" + ("="*26) + " DEMO 4 " + ("="*26) + "\n")
for neighbhor, weights in graph[nodes["london"]].items():
    print(weights["distance"], neighbor.name)
print("\n" + ("="*60) + "\n")


# DEMO 5
def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

def by_distance(weights):
    return float(weights["distance"])

# Display distance and neighbors in london through for loop
print("\n" + ("="*26) + " DEMO 5 " + ("="*26) + "\n")
for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")
print("\n" + ("="*60) + "\n")
