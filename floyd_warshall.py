class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[float('inf')] * vertices for _ in range(vertices)]
        for i in range(vertices):
            self.graph[i][i] = 0

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight

    def floyd_warshall(self):
        dist = [row[:] for row in self.graph]

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        self.print_solution(dist)

    def print_solution(self, dist):
        print("Shortest distances between all pairs of vertices:")
        for i in range(self.V):
            for j in range(self.V):
                if dist[i][j] == float('inf'):
                    print("INF", end=" ")
                else:
                    print(dist[i][j], end=" ")
            print()


# Example Usage:
g = Graph(4)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 9)
g.add_edge(0, 3, 4)
g.add_edge(1, 0, 5)
g.add_edge(1, 2, 2)
g.add_edge(2, 3, 3)
g.add_edge(3, 0, 4)
g.add_edge(3, 2, 3)

g.floyd_warshall()  # Calculate shortest paths between all pairs of vertices
