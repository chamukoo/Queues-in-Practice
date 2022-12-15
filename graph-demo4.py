import networkx as nx
from graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# Node 1 is set in Aberdeen
city1 = nodes["aberdeen"]

# Node 2 is set in Perth
city2 = nodes["perth"]
