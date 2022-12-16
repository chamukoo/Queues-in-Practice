
from graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# Display nodes in London
nodes["london"]

# Display graph
print(graph)

# Display neighbors in london through for loop
for neighbor in graph.neighbors(nodes["london"]):
    print(neighbor.name)

# Display weights and neighbors in london through for loop
for neighbhor, weights in graph[nodes["london"]].items():
    print(weights["distance"], neighbor.name)


def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

def by_distance(weights):
    return float(weights["distance"])


# Display distance and neighbors in london through for loop
for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")
  