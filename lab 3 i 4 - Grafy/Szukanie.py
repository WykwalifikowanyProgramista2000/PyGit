

def dfs(g: list, v: int, visited: list):
    visited.append(v)
    print(visited)
    for u in g[v-1]:
        print("u:", u, "g[v]:", v)
        if u not in visited:
            dfs(g, u, visited)


def is_acyclic(g: list, v: int, visited: list)->bool:
    visited.append(v)
    print("\n", visited)
    for c in g[v-1]:
        if c in visited[:-1]:
            return False
    for u in g[v-1]:
        print("u:", u, "g[v]:", v)
        if u not in visited:
            is_acyclic(g, u, visited)
    return True


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

wis = [[], [], []]
#dfs(graph_0, 1, wis[0])
#print(wis[0])

print("Graph A:", is_acyclic(graph_A, 1, wis[1]))
print("Graph B:", is_acyclic(graph_B, 1, wis[2]))

