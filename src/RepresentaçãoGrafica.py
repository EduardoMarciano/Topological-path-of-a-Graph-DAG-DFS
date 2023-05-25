#Função para imprimir a representação gráfica
import networkx 
import matplotlib.pyplot

def print_graficamente(grafo):
    # Cria um objeto do tipo DiGraph (grafo direcionado)
    G = networkx.DiGraph()

    # Adicionando as arestas ao objeto do tipo DiGraph
    for vertex in grafo.getVertices():
        for edge in vertex.getSaida():
            G.add_edge(vertex.id, edge[0], weight=edge[1])

    # Plotando o grafo
    pos = networkx.spring_layout(G, seed = 450)
    networkx.draw_networkx(G, pos)
    edge_labels = networkx.get_edge_attributes(G, 'weight')
    networkx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    matplotlib.pyplot.show()