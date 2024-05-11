from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def generate_edge(self):
        edge = []

        for node in self.graph:
            for neighbour in self.graph[node]:
                edge.append((node,neighbour))
        print(edge)

    def BFS(self,s):
        print("\nBFS: ")

        visited = [False] * (max(self.graph)+1)
        
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            s = queue.pop(0)
            print(s,end=" ")
            for neighbour in self.graph[s]:
                if not visited[neighbour]: 
                    queue.append(neighbour)
                    visited[neighbour] = True
    
    def DFS(self,s):
        print("\nDFS: ")

        visited = [False] * (max(self.graph)+1)

        stack = []

        stack.append(s)
        visited[s] = True

        while stack:

            s = stack.pop()
            print(s,end=" ")

            for neighbour in self.graph[s]:
                if not visited[neighbour]:
                    stack.append(neighbour)
                    visited[neighbour] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS(0)
g.DFS(0)