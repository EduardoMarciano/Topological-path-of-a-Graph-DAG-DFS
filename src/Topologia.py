# Funções para definir o caminho topológico de um grafo.
#Calcula o número de pré-requisitos diretos em cada matéria.
def calculaDependencia(grafo, v):
    
    for adj in v.incidencia:

        if adj not in grafo.vertices_id:
            v.incidencia.remove(adj)
    
    v.dependencia = len(v.incidencia)


def define_caminho_topologico(grafo):
    caminho_topoligco = []

    while grafo.vertices_id != []:
        v = grafo.vertices.pop(0)

        calculaDependencia(grafo, v)

        if v.dependencia == 0:
            grafo.vertices_id.remove(v.id)
            caminho_topoligco.append(v.id)

        else:
            grafo.vertices.append(v)
    
    return caminho_topoligco