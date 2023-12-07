class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

        for i in range(vertices):
            self.graph[i] = {}

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        self.graph[v][u] = 0  # Residual capacity for reverse edge

    def bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for v, capacity in self.graph[u].items():
                if visited[v] == False and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return visited[t]

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            v = sink

            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                v = parent[v]

            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


# Example Usage:
g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 6)
g.add_edge(1, 2, 5)
g.add_edge(1, 3, 3)
g.add_edge(2, 3, 2)
g.add_edge(2, 4, 3)
g.add_edge(3, 4, 6)
g.add_edge(3, 5, 4)
g.add_edge(4, 5, 5)

source = 0
sink = 5

max_flow = g.ford_fulkerson(source, sink)
print(f"Maximum flow possible from {source} to {sink} is: {max_flow}")
