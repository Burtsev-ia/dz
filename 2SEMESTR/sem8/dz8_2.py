import networkx as nx


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        g = nx.Graph()
        a = list()
        n = int(input())
        g.add_nodes_from(range(1, n+1))

        for _ in range(n):
            a.append(int(input()))
        e = int(input())
        for _ in range(e):
            s, t = list(map(int, input().split()))
            g.add_edge(s, t)
        
##НЕ РЕШАЕТСЯ  
        
        for _ in range(c):
            i = int(input())
