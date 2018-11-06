from enum import Enum


class Col(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2


def BFS(g: list, s: int):
    color, q = [Col.WHITE]*len(g), [s]
    color[s] = Col.GREY
    while q:
        u = q.pop(0)
        for v in g[u]:
            if color[v] is Col.WHITE:
                color[v] = Col.GREY
                q.append(v)
        color[u] = Col.BLACK


def BFS_neighbours(g: list, s: int, d: int):
    color, q, nlist = [Col.WHITE]*len(g), [[s, 0]], []
    while q:
        u = q.pop(0)
        for v in g[u[0]]:
            if color[v] is Col.WHITE:
                color[v] = Col.GREY
                q.append([v, u[1]+1])
                if (u[1]+1) <= d:
                    nlist.append(v)
        color[u[0]] = Col.BLACK
    return nlist


#  Wierzchołki numerowane są od 0
graph_B = [
    [1, 3],
    [2],
    [],
    [4],
    [1, 5],
    [],
    [0]
]

print('s = 0, d = 1: {0}\ns = 0, d = 2: {1}'.format(BFS_neighbours(graph_B, 0, 1), BFS_neighbours(graph_B, 0, 2)))
