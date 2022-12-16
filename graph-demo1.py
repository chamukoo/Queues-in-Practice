# Object Representation of the Cities and Roads

print("\n" + ("="*60) + "\n\n\tObject Representation of the Cities and Roads\n\n" + ("="*60))

# -------- DEMO 1
import networkx as nx

graph = nx.nx_agraph.read_dot("roadmap.dot")

# Print Statement
print("\n\n\tDEMO 1\n" + ("-"*60) + "\n")
print(nx.nx_agraph.read_dot("roadmap.dot"))
print(graph.nodes["london"])


# -------- DEMO 2
from graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# Display graphs and nodes in London
print("\n\n\n\tDEMO 2\n" + ("-"*60) + "\n")
print(nodes["london"])
print(graph)


# -------- DEMO 3
# Display neighbors in london through for loop
print("\n\n\n\tDEMO 3\n" + ("-"*60) + "\n")
for neighbor in graph.neighbors(nodes["london"]):
    print("\t", neighbor.name)


# --------- DEMO 4
# Display weights and neighbors in london through for loop
print("\n\n\n\tDEMO 4\n" + ("-"*60) + "\n")
for neighbhor, weights in graph[nodes["london"]].items():
    print("\t", weights["distance"], neighbor.name)


# -------- DEMO 5
def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

def by_distance(weights):
    return float(weights["distance"])

# Display distance and neighbors in london through for loop
print("\n\n\n\tDEMO 5\n" + ("-"*60) + "\n")
for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    print("\t", f"{weights['distance']:>3} miles, {neighbor.name}")

print("\n" + ("="*60) + "\n")
