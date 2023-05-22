import networkx as nx
import matplotlib.pyplot as plt
from ImplemetaçãoGrafo import Graph, Vertex

def imprime_graficamente(grafo):
    # Criando um objeto do tipo DiGraph (grafo direcionado)
    G = nx.DiGraph()

    # Adicionando as arestas ao objeto do tipo DiGraph
    for vertex in grafo.getVertices():
        for edge in vertex.getSaida():
            G.add_edge(vertex.id, edge[0], weight=edge[1])

    # Plotando o grafo
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()


    
