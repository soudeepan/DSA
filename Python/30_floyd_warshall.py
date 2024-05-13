import sys

class Graph():
    def __init__(self,vertices) -> None:
        self.V = vertices
        self.graph = [[sys.maxsize]*self.V for _ in range(self.V)]

    def addGraph(self,g):
        for i in range(self.V):
            for j in range(self.V):
                if g[i][j] != 0:
                    self.graph[i][j] = g[i][j]

    def showGraph(self):
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] == sys.maxsize:
                    self.graph[i][j] = 0

        print(self.graph)
    
    def floyd_warshall(self):

        for i in range(self.V):
            for j in range(self.V):
                for k in range(self.V):

                    if self.graph[i][j] > self.graph[i][k] + self.graph[k][j]:
                        self.graph[i][j] = self.graph[i][k] + self.graph[k][j]

        self.showGraph()

g= Graph(4)
 
graph = [[1, 1, 0, 1],
         [0, 1, 1, 0],
         [0, 0, 1, 1],
         [0, 0, 0, 1]]
 
g.addGraph(graph)

g.floyd_warshall()