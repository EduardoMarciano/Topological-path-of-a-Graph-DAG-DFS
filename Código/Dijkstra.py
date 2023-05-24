# Implementação do algorítimo de Dijktra com a utilização de fila de prioridade.

import heapq

def dijkstra(graph,root):
  nodes={}

  for v in graph.vertices:
      nodes[v.id]= v

  nodes[root.id].d=0

  queue=[(0,root.id)] #priority queue

  while queue:
      
      d,v = heapq._heappop_max(queue)
      v = graph.getVertex(v)
      
      if nodes[v.id].finished:
          continue
      
      nodes[v.id].finished=True

      for neighbor in v.getSaida():
          nbr = graph.getVertex(neighbor[0])
          new_d = d+ neighbor[1]

          if nbr.finished:
              continue
          
          if new_d < nodes[nbr.id].d:
              nodes[nbr.id].d=new_d
              nodes[nbr.id].parent=v

              heapq.heappush(queue,(new_d,neighbor[0]))

  return nodes