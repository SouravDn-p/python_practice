WHITE = 0
GRAY = 1
BLACK = 2

def DFS(graph):
    n = len(graph)
    color = [WHITE] * n
    prev = [None] * n
    d = [float('inf')] * n
    f = [float('inf')] * n
    time = [0]  # Using list to make it mutable inside nested function

    def DFS_Visit(u):
        color[u] = GRAY
        time[0] += 1
        d[u] = time[0]

        for v in graph[u]:
            if color[v] == WHITE:
                prev[v] = u
                DFS_Visit(v)

        color[u] = BLACK
        time[0] += 1
        f[u] = time[0]

    for u in range(n):
        if color[u] == WHITE:
            DFS_Visit(u)

    return d, f, prev  # You can return whatever data you need
