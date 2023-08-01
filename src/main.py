import copy
import random
from Grafo import Graph
from DefineVertex import define_vertex
from Topologia import define_caminho_topologico
from RepresentaçãoGrafica import print_graficamente

def print_caminho_topologico(caminho):
    print(f"Caminho Topológico:")

    for mateira in caminho[:len(caminho)-1]:
        print(f" {mateira} -> ", end = " ")
         
    print(f"{caminho[len(caminho)-1]}.")

#Lê o arquivo com todas as diciplinas e seus pré-requisitos
arquivo_diciplinas = open("src/DATA/DiciplinasCIC.txt")
materias = arquivo_diciplinas.read().split("\n")

#Embaralha as matérias para simular um ambiente mais realista
random.shuffle(materias)

#Começo efeitvo do código
grafo = Graph()
caminho_topoligco = []

#Define os Vêrtices do Grafo, sua incidência e sua saida
define_vertex(grafo, materias)

#Define um possível caminho topológico
caminho_topoligco = define_caminho_topologico(copy.deepcopy(grafo))

#Impressão dos resultados
print("--------------------------------------")
print("Bacharelado em Ciência da Computação:")
print("--------------------------------------")
print_caminho_topologico(caminho_topoligco)
print("--------------------------------------")
print_graficamente(copy.deepcopy(grafo))
