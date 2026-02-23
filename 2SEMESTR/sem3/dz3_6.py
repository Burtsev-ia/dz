'''3
0 1
1 2
2 0
'''

from collections import defaultdict


class Graph:
    def __init__(self):
        # Initialize the graph using defaultdict to store adjacency lists
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v):
        """Add a directed edge from vertex u to vertex v"""
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def transpose(self):
        """Create a transpose graph by reversing all edges"""
        g_transpose = Graph()
        for u in self.graph:
            # For each edge u->v, add edge v->u in transposed graph
            for v in self.graph[u]:
                g_transpose.add_edge(v, u)
        return g_transpose

    def dfs_first_pass(self, vertex, visited, finishing_times):
        """First DFS pass to compute finishing times"""
        visited[vertex] = True
        # Recursively visit all adjacent vertices
        for adj_vertex in self.graph[vertex]:
            if not visited[adj_vertex]:
                self.dfs_first_pass(adj_vertex, visited, finishing_times)
        # Add vertex to finishing_times after exploring all its neighbors
        finishing_times.append(vertex)

    def dfs_second_pass(self, vertex, visited, scc):
        """Second DFS pass to find SCCs"""
        visited[vertex] = True
        scc.append(vertex)
        # Recursively visit all adjacent vertices
        for adj_vertex in self.graph[vertex]:
            if not visited[adj_vertex]:
                self.dfs_second_pass(adj_vertex, visited, scc)

    def find_sccs(self):
        """Main function to find strongly connected components"""
        # Step 1: First DFS pass on original graph
        visited = {vertex: False for vertex in self.vertices}
        finishing_times = []
        # Process all vertices in first DFS pass
        for vertex in self.vertices:
            if not visited[vertex]:
                self.dfs_first_pass(vertex, visited, finishing_times)
        # Step 2: Create transpose graph
        transposed_graph = self.transpose()
        # Step 3: Second DFS pass on transposed graph
        visited = {vertex: False for vertex in self.vertices}
        sccs = []
        # Process vertices in order of decreasing finishing time
        for vertex in reversed(finishing_times):
            if not visited[vertex]:
                current_scc = []
                transposed_graph.dfs_second_pass(vertex, visited, current_scc)
                sccs.append(current_scc)
        return sccs


def usage(edges):
    g = Graph()
    for u, v in edges:
        g.add_edge(u, v)
    sccs = sorted(g.find_sccs())
    for i in range(len(sccs)):
        sccs[i] = sorted(sccs[i])
    print(sccs)
    print(len(sccs))


n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
usage(a)
