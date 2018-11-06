import networkx as nx


def dijkstra(g: nx, s: int, t: int)->str:
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


graph_A = nx.MultiDiGraph()

with open("data.dat", "r") as file:
    for line in file:
        line = line.split()
        graph_A.add_edge(int(line[0]), int(line[1]), weight=float(line[2]))


print('My Dijkstra answer: {0}'.format(dijkstra(graph_A, 1, 3)))
print('Networkx Dijkstra path = {0}, length = {1}'.format(nx.dijkstra_path(graph_A, 1, 3, weight='weight'), nx.dijkstra_path_length(graph_A, 1, 3, weight='weight')))
