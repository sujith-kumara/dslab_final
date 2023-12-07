class BipartiteGraph:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.graph = {u: [] for u in range(left)}  # Adjacency list representation
        self.pair_u = [-1] * left  # Keeps track of pair for vertices in set U
        self.pair_v = [-1] * right  # Keeps track of pair for vertices in set V

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self):
        dist = [-1] * self.left
        queue = []
        for u in range(self.left):
            if self.pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)

        max_matching = 0

        while queue:
            u = queue.pop(0)
            for v in self.graph[u]:
                if self.pair_v[v] == -1:
                    self.pair_v[v] = u
                    self.pair_u[u] = v
                    max_matching += 1
                    return max_matching

                if dist[self.pair_v[v]] == -1:
                    dist[self.pair_v[v]] = dist[u] + 1
                    queue.append(self.pair_v[v])

        return max_matching

    def hopcroft_karp(self):
        max_matching = 0
        while True:
            matching = self.bfs()
            if matching == 0:
                break
            max_matching += matching
        return max_matching


# Example Usage:
g = BipartiteGraph(4, 4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

max_matching = g.hopcroft_karp()
print(f"Maximum matching in the bipartite graph is: {max_matching}")
