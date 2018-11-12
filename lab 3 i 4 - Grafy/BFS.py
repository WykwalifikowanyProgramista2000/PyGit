from enum import Enum


class Col(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2


def BFS(g: list, s: int):
    color, queue = [Col.WHITE]*len(g), [s]
    color[s] = Col.GREY
    while queue:
        u = queue.pop(0)
        for v in g[u]:
            if color[v] is Col.WHITE:
                color[v] = Col.GREY
                queue.append(v)
        color[u] = Col.BLACK


def BFS_neighbours(g: list, s: int, d: int):
    color, queue, neighbours_set = [Col.WHITE]*len(g), [[s, 0]], set()
    while queue:
        u = queue.pop(0)
        for v in g[u[0]-1]:
            if color[v] is Col.WHITE:
                color[v] = Col.GREY
                queue.append([v, u[1]+1])
                if (u[1]+1) <= d:
                    neighbours_set.add(v)
        color[u[0]] = Col.BLACK
    return neighbours_set


graph_B = [
    [2, 4],
    [3],
    [],
    [5],
    [2, 6],
    [],
    [1]
]

print('s = 0, d = 1: {0}\ns = 0, d = 2: {1}'.format(BFS_neighbours(graph_B, 1, 1), BFS_neighbours(graph_B, 1, 2)))
