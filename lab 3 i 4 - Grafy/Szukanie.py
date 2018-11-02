

def dfs(g: list, v: int, visited: list):
    visited.append(v)
    for u in g[v-1]:
        if u not in visited:
            dfs(g, u, visited)


'''
def dfs_iterative(g: list, v)->list:
    s = [v]
    while s is not None:
        s.pop()
        if v not in s:
            s.append(v)
            for u in g[v-1]:
                s.append(u)
    return s
'''

def is_acyclic(g: list, v: int, visited: list):
    flag = True
    visited.append(v)
    print(visited)
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
]# 7 wierzchołków

graph_A = [
    [2, 3],
    [],
    [4],
    []
]# 4 wierzchołki

graph_B = [
    [2],
    [3],
    [1]
]

graph_C = [
    
]# 3 wierzchołki

wis = []
for i in range(10):
    wis.append([])

dfs(graph_0, 1, wis[0])
print("dfs_recursive:", wis[0])
#print("dfs_iterative:", dfs_iterative(graph_0, 1))

print("Graph 0:", is_acyclic(graph_0, 7, wis[0]))
print("Graph A:", is_acyclic(graph_A, 4, wis[1]))
print("Graph B:", is_acyclic(graph_B, 3, wis[2]))
#print("Graph C:", is_acyclic(graph_C, 1, wis[3]))
#print("Graph D:", is_acyclic(graph_D, 1, wis[4]))
#print("Graph E:", is_acyclic(graph_E, 1, wis[5]))

