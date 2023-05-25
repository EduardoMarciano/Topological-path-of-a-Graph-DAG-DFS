import random
import copy
from Grafo import Graph
from PrintFunctions import print_grafo, print_sequencia, print_caminho_topologico
from RepresentaçãoGrafica import print_graficamente
from DefineVertex import define_vertex
from CaminhoCritico import CalculaSequenciaCritica
from Topologia import define_caminho_topologico


#Lê o arquivo com todas as diciplinas e seus pré-requisitos
arquivo_diciplinas = open("DiciplinasCIC.txt")
materias = arquivo_diciplinas.read().split("\n")

#Embaralha as matérias para simular um ambiente mais realist
random.shuffle(materias)

#Começo efeitvo do código
grafo = Graph()
caminho_topoligco = []

#Define os Vêrtices do Grafo, sua incidência e sua saida
define_vertex(grafo, materias)

#Define dois possíveis caminhos críticos com seu número de matérias
sequencia_apc, name_max_apc = CalculaSequenciaCritica(copy.deepcopy(grafo), grafo.getVertex("CIC0004"))

sequencia_c1, name_max_c1 = CalculaSequenciaCritica(copy.deepcopy(grafo), grafo.getVertex("MAT0025"))

#Define um possível caminho topológico
caminho_topoligco = define_caminho_topologico(copy.deepcopy(grafo))


#Impressão dos resultados
print("--------------------------------------")
print("Bacharelado em Ciência da Computação:")
print()
print(f"Grafo das matérias do curso:")
print()


print_grafo(copy.deepcopy(grafo))


print(f"O caminho crítico começando por apc tem {len(sequencia_apc)} matérias.")
print(f"Com sequência: ", end = "")

print_sequencia(sequencia_apc)

print()
print()

print(f"O caminho crítico começando por cáclculo 1 tem {len(sequencia_c1)} matérias")
print(f"Com sequência: ")

print_sequencia(sequencia_c1)

print()
print()

print_caminho_topologico(caminho_topoligco)

print_graficamente(copy.deepcopy(grafo))