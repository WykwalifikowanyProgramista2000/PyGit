

def dfs(g: list, v: int, visited: list):
    visited.append(v)
    for u in g[v-1]:
        if u not in visited:
            dfs(g, u, visited)


def is_acyclic(g: list, v: int, visited: list):
    flag = True
    visited.append(v)
    for c in g[v-1]:
        if c in visited:
            flag = False
    if flag is True:
        for u in g[v-1]:
            if u not in visited:
                return is_acyclic(g, u, visited)
        return True
    else:
        return False


graph_0 = [
    [2, 3, 4],
    [1, 4, 6],
    [1, 7],
    [2],
    [1, 6],
    [2, 5],
    [3]
]

graph_A = [
    [2, 3],
    [],
    [4],
    []
]

graph_B = [
    [2],
    [3],
    [1]
]

graph_C = [
    
]

wis = []
for i in range(10):
    wis.append([])

#dfs(graph_0, 1, wis[0])
#print(wis[0])

print("Graph 0:", is_acyclic(graph_0, 1, wis[0]))
print("Graph A:", is_acyclic(graph_A, 1, wis[1]))
print("Graph B:", is_acyclic(graph_B, 1, wis[2]))
#print("Graph C:", is_acyclic(graph_C, 1, wis[3]))
#print("Graph D:", is_acyclic(graph_D, 1, wis[4]))
#print("Graph E:", is_acyclic(graph_E, 1, wis[5]))

