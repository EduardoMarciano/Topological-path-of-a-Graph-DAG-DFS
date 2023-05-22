import random
import heapq
import copy
from ImplemetaçãoGrafo import Graph, Vertex
from ImplementaçãoDijkstra import dijkstra
from ImprimeFun import imprimi_caminho_topologico, imprimi_grafo
from RepresentaçãoGrafica import imprime_graficamente

#Calcula o número de pré-requisitos
def calculaDependencia(grafo, v):
    
    for adj in v.incidencia:
        if adj not in grafo.vertices_id:
            v.incidencia.remove(adj)

    v.dependencia = len(v.incidencia)
def limpa_grafo(g):
    for v in g.getVertices():
        v.d = float('inf')


#Lê o arquivo com todas as diciplinas e seus pré-requisitos
arquivo_diciplinas = open("DiciplinasCIC.txt")
materias = arquivo_diciplinas.read().split("\n")

#Embaralha as matérias para simular um ambiente mais realista
random.shuffle(materias)

#Começo efeitvo do código
grafo = Graph()

caminho_topoligco = []
#Define os Vêrtices do Grafo e os Vêrtices de incidência
for materia in materias:
    
    materia = materia.split(":")
    texto = materia[0]
    nome_materia = texto.split(" ")[0]
    
    grafo.addVertex(nome_materia)

    requisitos = materia[1].split(",")
    
    for adj in requisitos:
        if adj !=  " ??":
            v = grafo.getVertex(nome_materia)
            v.addIncidencia(adj[1:])

#Define os Vêrtices de Saida
n = 0
for v in grafo.getVertices():
    for adj in v.getIncidencia():

        x = grafo.getVertex(adj)
        x.addSaida(v.id, 1)

#Ordena a lista de Vêrtices pelo grau 
grafo.vertices = sorted(grafo.getVertices(), key=lambda Vertex: Vertex.dependencia)
grafo0 = copy.deepcopy(grafo)

#Define um possível caminho crítico
n_m_apc = 0
apc = (dijkstra(grafo, grafo.getVertex("CIC0004")))
for m in apc:
    if n_m_apc <= apc[m].d and apc[m].d != float('inf'):
        n_m_apc = apc[m].d

limpa_grafo(grafo)

c1  = (dijkstra(grafo, grafo.getVertex("MAT0025")))

n_m_c1 = 0
for m in c1:
    if (n_m_c1<= c1[m].d) and c1[m].d != float('inf'):
        n_m_c1 = c1[m].d


limpa_grafo(grafo)

#Define um possível caminho topológico
while grafo.vertices_id != []:
    v = grafo.vertices.pop(0)

    calculaDependencia(grafo, v)

    if v.dependencia == 0:
        grafo.vertices_id.remove(v.id)
        caminho_topoligco.append(v.id)

    else:
        grafo.vertices.append(v)

#Nome do curso
print("Bacharelado em Ciência da Computação:")
print()
print(f"Grafo das matérias do curso:")
print()

#Grafo das Matérias do Curso
imprimi_grafo(grafo0)

#Caminho Cŕtico
print(f"O caminho crítico começando por apc tem {n_m_apc+1} matérias")
print(f"Com sequência: ")

#imprime_sequencia("CIC0004")
print()

print(f"O caminho crítico começando por cáclculo 1 tem {n_m_c1+1} matérias")
print(f"COm sequência: ")
#imprime_sequencia("MAT0025")
print()
#Imprime o caminho topológico encontrado
imprimi_caminho_topologico(caminho_topoligco)

#Imprimindo o grafo com o auxílio das bibliotecas networkx e matplotlib
imprime_graficamente(grafo0)