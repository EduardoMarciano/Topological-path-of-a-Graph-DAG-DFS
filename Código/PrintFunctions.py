# Funções para imprir o resultado Obitido
def print_caminho_topologico(caminho):
    print(f"Caminho Topológico:")

    for mateira in caminho[:len(caminho)-1]:
        print(f" {mateira} -> ", end = " ")
         
    print(f"{caminho[len(caminho)-1]}.")

def print_grafo(graph):
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

def print_sequencia(lista):
    for m in lista[:len(lista)-1]:
        print(f"{m} -> ", end = "")

    print(f"{lista[-1]}.", end = "")