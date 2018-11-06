import networkx as nx

graph_A = nx.MultiDiGraph()

with open("data.dat", "r") as file:
    for line in file:
        line = line.split()
        graph_A.add_edge(int(line[0]), int(line[1]), weight=float(line[2]))

xd = graph_A.size('weight')
print('xd', xd)


Q = [n for n in graph_A.nodes]  # [1, 2, 3]
d = [12, 1, 100]
u = d.index(min(d))
Q.remove(u+1)
print('XDDD', u, Q)
#X = [n for n in graph_A.edges[2][3]]
#X = graph_A.edges[2,3,0]['weight']

for u, v, key, weight in graph_A.edges(1, data='weight', keys=True):
    if weight is not None:
        print(weight)

print('1', [list([keys, weight]) for u, v, keys, weight in graph_A.edges(1, data='weight', keys=True)])
print(graph_A.edges(1, data='weight'))
d = [[v, keys, weight] for u, v, keys, weight in graph_A.edges(2, data='weight', keys=True)]
print(d)

#print(X)

lst = []
for n in range(3):
    lst.append(None)
print('test', graph_A[1][2][0])


