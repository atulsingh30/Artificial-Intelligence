import networkx as nx
import matplotlib.pyplot as plt

def graph_coloring():
    v, e = map(int, input().split())
    g = [[] for _ in range(v)]
    for i in range(e):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)

    res = [-1] * v
    available = [False] * v
    res[0] = 0

    cn = 0
    for i in range(1, v):
        for x in g[i]:
            if res[x] != -1:
                available[res[x]] = True

        cr = 0
        while available[cr] or cr in [res[x] for x in g[i] if res[x]!=-1]:
            cr += 1

        res[i] = cr
        cn = max(cn, cr + 1)

        for x in g[i]:
            if res[x] != -1:
                available[res[x]] = False

    print("Minimum number of colors required:", cn)
    print("Colors assigned to vertices:", res)

    # Visualization of the graph
    G = nx.Graph()
    for i in range(v):
        G.add_node(i, color=res[i])

    for i in range(v):
        for j in g[i]:
            G.add_edge(i, j)