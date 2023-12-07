class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))

    def bellman_ford(self, src):
        distances = [float('inf')] * self.V
        distances[src] = 0

        for _ in range(self.V - 1):
            for u, v, weight in self.graph:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        self.print_solution(distances)

    def print_solution(self, dist):
        print("Vertex   Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")


# Example Usage:
g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 2)
g.add_edge(1, 2, 5)
g.add_edge(1, 3, 10)
g.add_edge(2, 3, 3)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 4)

g.bellman_ford(0)  # Calculate shortest paths from source vertex 0
