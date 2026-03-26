import networkx as nx
import matplotlib.pyplot as plt
from graph_data import graph

def draw_graph():
    G = nx.Graph()

    for node in graph:
        for neighbor, weight in graph[node]:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)

    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Road Network Graph")
    plt.show()