import sys

class Graph():
    def __init__(self,v):
        self.V = v
        self.edge = []

    def addEdge(self,u,v,w):
        self.edge.append([u,v,w])

    
    def bellman_ford(self,s):

        distance = [float("Inf")] * self.V
        distance[s] = 0

        for i in range(self.V-1):      
            for u,v,w in self.edge:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        for i in range(self.V-1):
            for u,v,w in self.edge:
                if distance[u] < distance[v]:
                    distance[v] = -float("Inf") 

        print(distance)

g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

g.bellman_ford(0)