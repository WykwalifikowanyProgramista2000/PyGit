import networkx as nx
import matplotlib.pyplot as plt


graph_A = nx.MultiDiGraph()

with open("data.dat", "r") as file:
    for line in file:
        line = line.split()
        graph_A.add_weighted_edges_from(int(line[0]), int(line[1]), float(line[2]))

