
class Graph():
    def __init__(self,no_of_vertices):
        self.V = no_of_vertices
        self.graph = []

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def find(self,parent,i):
        if parent[i] != i:
            self.find(parent,parent[i])
        return parent[i]
    
    def union(self,parent,rank,x,y):

        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x

        else:
            parent[x] = y
            rank[y] += 1

    def KruskalMST(self):

        result = []

        self.graph = sorted(self.graph,key=lambda item:item[2])

        parent = []
        rank = []

        for i in range(self.V):
            parent.append(i)
            rank.append(0)

        i = 0
        e = 0

        while e < self.V - 1:

            u,v,w = self.graph[i]
            i += 1
            x = self.find(parent,u)
            y = self.find(parent,v)

            if x != y:
                e += 1
                result.append([u,v,w])
                self.union(parent,rank,x,y)

        print(result)

g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 

g.KruskalMST()
