#Define o caminho cŕitco de uma vêrtice sem incideência, a sequência desse caminho e seu tamanho.
from Dijkstra import dijkstra

#Zera as distância de cada vêrtice
def limpa_grafo(g):

    for v in g.getVertices():

        v.d = float('inf')
        v.parent=None
        v.finished=False

def calcula_tamanho_caminho_critico(grafo, name_root):
    n_m_root = 0
    name_max_root = ""

    dic_root = (dijkstra(grafo, grafo.getVertex(name_root)))

    for m in dic_root:
        if n_m_root <= dic_root[m].d and dic_root[m].d != float('inf'):
            n_m_root = dic_root[m].d
            name_max_root = dic_root[m].id

    return name_max_root, n_m_root

def CalculaSequenciaCritica(grafo,root):

    final, best = calcula_tamanho_caminho_critico(grafo, root.id)
    limpa_grafo(grafo)

    best1 = 5
    final = grafo.getVertex(final)

    fila = [root]
    sequencia = []  
  
    while len(fila) != 0:
        v = fila.pop(0)

        limpa_grafo(grafo)
        dic = dijkstra(grafo, v)

        if dic[final.id].d != float('inf') and dic[final.id].d == best:
                best -= 1
                sequencia.append(v.id)
                
                fila = []
                for nbr in v.getSaida():
                    nbr = grafo.getVertex(nbr[0])
                    fila.append(nbr)

                    if nbr.id == final.id:
                        sequencia.append(nbr.id)
                        return sequencia, final
                       
    return sequencia, final