

def adjmat_to_adjlist(m: list)->list:
    temp = []
    print(temp)
    for j in range(len(m)):
        temp.append([])
        for i in range(len(m)):
            if m[j][i] is not 0:
                for c in range(m[j][i]):
                    temp[j].append(i+1)
                    print("j:", j, "i:", i, "c:", c, " ", temp)
    return temp


matrix = [[0, 1, 0], [0, 0, 1], [1, 2, 0]]
ans = adjmat_to_adjlist(matrix)
print(ans)
