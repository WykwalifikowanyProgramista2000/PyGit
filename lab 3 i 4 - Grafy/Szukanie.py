

def dfs(g: list, v: int, visited: list):
    visited.append(v)
    for u in g[v-1]:
        if u not in visited:
            dfs(g, u, visited)


def acc(g: list, v: int, visited: list):  # funkcja sprawdzająca acykliczność względem danego wierzchołka
    flag = True
    visited.append(v)
    #print(visited)
    for c in g[v-1]:
        if c in visited:
            flag = False
    if flag is True:
        for u in g[v-1]:
            if u not in visited:
                return acc(g, u, visited)
        return True
    else:
        return False

# funkcja sprawdzająca acykliczność wszystkich wierzchołków grafu, do momentu znalezienia 'pętli'
def is_acyclic(g: list):
    flag = True
    for v in range(1, len(g)+1):
        tab = []
        if acc(g, v, tab) is False:
            flag = False
    return flag


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


a = [[2, 3], [], [4], []]
b = [[2], [3], [1]]
c = [[], [1, 3], [2]]
d = [[2], [], [2, 4], [3]]
e = [[2, 3], [4], [4], []]
f = [[2, 3], [3], []]

print('0', is_acyclic(graph_0))
print('A', is_acyclic(graph_A))
print('B', is_acyclic(graph_B))
print('a', is_acyclic(a))
print('b', is_acyclic(b))
print('c', is_acyclic(c))
print('d', is_acyclic(d))
print('e', is_acyclic(e))
print('f', is_acyclic(f))

