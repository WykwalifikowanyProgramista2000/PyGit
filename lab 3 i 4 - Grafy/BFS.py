

'''
    0 = biały
    1 = szary
    2 = czarny
'''



def BFS(g: list, s: int):
    color, q = [0]*len(g), [s]
    color[s] = 1
    while q:
        u = q.pop(0)
        for v in g[u]:
            if color[v] is 0:
                color[v] = 1
                q.append(v)
        color[u] = 2


def dist(start, stop)->int:
    return stop - start


def BFS_neighbours(g: list, s: int, d: int):
    color, q, nlist = [0]*len(g), [[s, 0]], []
    while q:
        u = q.pop(0)
        for v in g[u[0]]:
            if color[v] is 0:
                color[v] = 1
                q.append([v, u[1]+1])
                if (u[1]+1) <= d:
                    nlist.append(v)
        color[u[0]] = 2
    return nlist


graph_A = [
    [1, 2, 4],
    [0, 3, 5],
    [0, 6],
    [1],
    [0, 5],
    [1, 4],
    [2]
]

graph_B = [
    [1, 3],
    [2],
    [],
    [4],
    [1, 5],
    [],
    [0]
]

BFS(graph_A, 0)
x = BFS_neighbours(graph_B, 6, 3)
y = BFS_neighbours(graph_A, 6, 3)
print(x)
print(y)
