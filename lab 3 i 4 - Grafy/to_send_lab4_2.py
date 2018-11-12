import networkx as nx


def newDijkstra(Graph: nx.MultiDiGraph, start_node: int, target_node: int)->list:
    total_path_length = nx.dijkstra_path_length(Graph, start_node, target_node)
    nodes = nx.dijkstra_path(Graph, start_node, target_node)
    key_weights = []
    ans = [start_node]

    for n in range(len(nodes)-1):
        key_weights.append([None, None, None, total_path_length])
        for u, v, key, weight in Graph.edges(nodes[n], data='weight', keys=True):
            if n < len(nodes) and v == nodes[n + 1]:
                if weight <= key_weights[n][3]:
                    key_weights[n] = [u, v, key, weight]

    for i in range(len(nodes)-1):
        ans = ['{0} -[{1}: {2}]-> {3}'.format(ans[0], key_weights[i][2], key_weights[i][3], key_weights[i][1])]
    return ['{0} (total: {1})'.format(ans[0], total_path_length)]


graph_A = nx.MultiDiGraph()
with open("data.dat", "r") as file:
    for line in file:
        line = line.split()
        graph_A.add_edge(int(line[0]), int(line[1]), weight=float(line[2]))

print('newDijkstra: {0}'.format(newDijkstra(graph_A, 1, 3)[0]))


# ==========================================================================


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


def BFS_neighbours(g: list, s: int, d: int)->set:
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
