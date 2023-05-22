def imprimi_caminho_topologico(caminho):

    print(f"Caminho Topológico:")

    for mateira in caminho[:len(caminho)-1]:
        print(f" {mateira} -> ", end = " ")  
    print(f"{caminho[len(caminho)-1]}.")

def imprimi_grafo(graph):
    for v in graph.getVertices():
        print("Vertex:", v.id)

        print("Outgoing Edges:")
        for neighbor in v.getSaida():
            print("-> Neighbor:", neighbor[0])
        print()
        print("Incoming Edges:")
        for nbr in v.getIncidencia():
            print("<- Neighbor:", nbr)
        print()
        print("------------------------")
        