import networkx as nx


def dijkstra(g: nx.MultiDiGraph, s: int, t: int)->str:
    d = []
    prev = []
    Q = []
    for n in g.nodes:
        d.append(g.size('weight') + 1)
        prev.append(None)
        Q.append(n)
    d[s-1] = 0

    while Q:
        u = d.index(min(list([d[n-1] for n in Q])))
        Q.remove(u+1)

        for z, v, keys, weight in g.edges(u + 1, data='weight', keys=True):
            if d[v-1] > d[u] + weight:
                d[v-1] = d[u] + weight
                prev[v-1] = [u+1, keys]

    ans = ['{0} (total: {1})'.format(t, d[t-1])]
    while t != s:
        ans = ['{0} -[{1}: {2}]-> {3}'.format(prev[t-1][0], prev[t-1][1], g[prev[t - 1][0]][t][prev[t - 1][1]]['weight'], ans[0])]
        t = prev[t-1][0]
    return ans[0]


def newDijkstra(Graph: nx.MultiDiGraph, start_node: int, target_node: int)->list:
    total_path_length = nx.dijkstra_path_length(Graph, start_node, target_node)
    nodes = nx.dijkstra_path(Graph, start_node, target_node)
    key_weights = []

    for n in range(len(nodes)):
        key_weights.append([None, None, None, total_path_length])
        for u, v, key, weight in Graph.edges(nodes[n], data='weight', keys=True):
            if n < len(nodes) and v == nodes[n + 1]:
                if weight < key_weights[n][3]:
                    key_weights[n] = [u, v, key, weight]

    ans = [start_node]
    for i in range(len(nodes)-1):
        ans = ['{0} -[{1}: {2}]-> {3}'.format(ans[0], key_weights[i][2], key_weights[i][3], key_weights[i][1])]

    return ['{0} (total: {1})'.format(ans[0], total_path_length)]

graph_A = nx.MultiDiGraph()

with open("data.dat", "r") as file:
    for line in file:
        line = line.split()
        graph_A.add_edge(int(line[0]), int(line[1]), weight=float(line[2]))


print('My Dijkstra answer: {0}'.format(dijkstra(graph_A, 1, 3)))
print('Networkx Dijkstra path = {0}, length = {1}'.format(nx.dijkstra_path(graph_A, 1, 3, weight='weight'), nx.dijkstra_path_length(graph_A, 1, 3, weight='weight')))
print('newDijkstra: {0}'.format(newDijkstra(graph_A, 1, 3)[0]))
