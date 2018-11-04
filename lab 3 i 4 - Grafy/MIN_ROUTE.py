import networkx as nx


graph_A = nx.MultiDiGraph()

with open("data.dat", "r") as file:
    for line in file:
        line = line.split()
        graph_A.add_edge(int(line[0]), int(line[1]), weight=float(line[2]))


alist = []

print(list(graph_A.nodes(data=True)))
print(graph_A.size(weight='weight'))
