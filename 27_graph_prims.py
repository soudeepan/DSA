import sys

class Graph():
    def __init__(self,no_of_vertices):
        self.V = no_of_vertices
        self.graph = []

    def addEdge(self,x):
        self.graph.append()

    def minKey(self,key,mst):
        min = sys.maxsize

        for v in range(self.V):
            if key[v]<min and mst[v] is False:
                min = key[v]
                m_index = v
        
        return m_index

    def primsMST(self):

        parent = [None]*self.V
        key = [sys.maxsize]*self.V
        mst = [False]*self.V
        
        parent[0] = -1
        key[0] = 0

        for vv in range(self.V):

            s = self.minKey(key,mst)

            mst[s] = True

            for v in range(self.V):

                if self.graph[s][v] > 0 and mst[v] is False and key[v] > self.graph[s][v]:
                    key[v] = self.graph[s][v]
                    parent[v] = s


        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]

g.primsMST()