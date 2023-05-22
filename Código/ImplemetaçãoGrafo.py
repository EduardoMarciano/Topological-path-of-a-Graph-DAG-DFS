#  adjGraph
#  Created by Brad Miller on 2005-02-24.
#  Copyright (c) 2005 Brad Miller, David Ranum, Luther College. All rights reserved.

class Graph:
    def __init__(self):
        self.vertices = []
        self.vertices_id = []
        
    def addVertex(self, v):

        newVertex = Vertex(v)
        self.vertices.append(newVertex)
        self.vertices_id.append(newVertex.id)
    
    def getVertex(self,n):
        for v in self.vertices:
            if v.id == n:
                return v


    def getVertices(self):
        return self.vertices
        
class Vertex:
    def __init__(self,num):
        self.id = num
        self.saida = []
        self.incidencia = []
        #Numero de matérias com pré-requisitos diretos
        self.dependencia = 0

        #Atributos para implementação do Dikstra
        self.d=float('inf')
        self.parent=None
        self.finished=False

    
    def addSaida(self,nbr, peso):
        self.saida.append((nbr, peso))

    def getSaida(self):
        return self.saida
    
    def addIncidencia(self,nbr):
        self.incidencia.append(nbr)
        self.dependencia+= 1          
    
    def getIncidencia(self):
        return self.incidencia
    
    def getSaida(self):
        return self.saida
    
