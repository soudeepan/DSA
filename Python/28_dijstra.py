import sys

class Graph():
    def __init__(self, no_of_vertices):
        self.V = no_of_vertices
        self.graph = [[0]*self.V for _ in range(self.V)]

    def minDistance(self, distance, visited):
        min_val = sys.maxsize
        min_index = -1
        for i in range(self.V):
            if distance[i][0] < min_val and not visited[i]:
                min_val = distance[i][0]
                min_index = i
        return min_index

    def dijkstra(self, start):
        visited = [False]*self.V
        distance = [[sys.maxsize, None] for _ in range(self.V)]

        distance[start] = [0, None]

        v = start

        while not all(visited):               
            for j in range(self.V):
                if self.graph[v][j] > 0 and not visited[j]:
                    d = distance[v][0] + self.graph[v][j]
                    if d < distance[j][0]:
                        distance[j][0] = d
                        distance[j][1] = v

            v = self.minDistance(distance, visited)
            visited[v] = True

        for i in range(self.V):
            print("\n\nDistance of",i,":",distance[i][0])
            self.path(i,distance)


    def path(self,node,distance):
        if node is None:
            return
        else:
            
            self.path(distance[node][1],distance)
            print(" ->",node,end="")
            return


    

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

g.dijkstra(0)
