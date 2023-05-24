#Define os Vêrtices, sua incidência e saída a partir do arquivo .txt DiciplinasCIC

def define_vertex(grafo, materias):

    for materia in materias:
    
        materia = materia.split(":")
        texto = materia[0]
        nome_materia = texto.split(" ")[0]
    
        grafo.addVertex(nome_materia)

        define_incidencia(grafo, materia, nome_materia)
    
    define_saida(grafo)

def define_incidencia(grafo, materia, nome_materia):

    requisitos = materia[1].split(",")

    for adj in requisitos:
        if adj !=  " ??":
            v = grafo.getVertex(nome_materia)
            v.addIncidencia(adj[1:])

def define_saida(grafo):
    for v in grafo.getVertices():
        for adj in v.getIncidencia():

            x = grafo.getVertex(adj)
            x.addSaida(v.id, 1)