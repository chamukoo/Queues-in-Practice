from graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# Display nodes in London
print(nodes["london"])

# Display graph
print(graph)

# Display neighbors in london through for loop
for neighbor in graph.neighbors(nodes["london"]):
    print(neighbor.name)

# Display weights and neighbors in london through for loop
for neighbhor, weights in graph[nodes["london"]].items():
    print(weights["distance"], neighbor.name)

    