import random
from timeit import timeit
from copy import deepcopy

def quicksort(lst: list, start: int, stop: int) -> list:
    i = start
    j = stop
    pivot = ((i+j)//2)
    while i < j:
        while lst[i] < pivot:
            i += 1
        while lst[j] > pivot:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
    if start < j:
        quicksort(lst, start, j)
    if i < stop:
        quicksort(lst, i, stop)
    return lst


def bubblesort(I: list):
    n = len(I)
    j = 0
    is_sorted = False
    while j < n and is_sorted == False:
        is_sorted = True
        for i in range(1, n):
            if I[i - 1] > I[i]:
                I[i - 1], I[i] = I[i], I[i - 1]
                is_sorted = False
        j += 1


tablesToSort = int(input("Enter number of tests to run: "))
aTimeTable = [["bubblesort", 0, 0, 0, 0],
              ["quicksort", 0, 0, 0, 0]]


# Sorted List
for i in range(0, tablesToSort):
    aListQ = random.sample(range(1000), 1000)
    quicksort(aListQ, 0, len(aListQ)-1)
    aListB = deepcopy(aListQ)
    aTimeTable[0][1] += timeit("bubblesort(aListQ)", number=1, globals=globals())
    aTimeTable[1][1] += timeit("quicksort(aListB, 0, len(aListQ)-1)", number=1, globals=globals())


# Sorted Backward
for i in range(0, tablesToSort):
    aListQ = random.sample(range(1000), 1000)
    quicksort(aListQ, 0, len(aListQ)-1)
    aListB = deepcopy(aListQ[::-1])
    aListQ = aListQ[::-1]
    aTimeTable[0][2] += timeit("bubblesort(aListQ)", number=1, globals=globals())
    aTimeTable[1][2] += timeit("quicksort(aListB, 0, len(aListQ)-1)", number=1, globals=globals())


# All Same
for i in range(0, tablesToSort):
    aListQ = [2]
    for j in range(1000):
        aListQ.append(2)
    aListB = deepcopy(aListQ)
    aTimeTable[0][3] += timeit("bubblesort(aListQ)", number=1, globals=globals())
    aTimeTable[1][3] += timeit("quicksort(aListB, 0, len(aListQ)-1)", number=1, globals=globals())


# All Random
for i in range(0, tablesToSort):
    aListQ = random.sample(range(1000), 1000)
    aListB = deepcopy(aListQ)
    aTimeTable[0][4] += timeit("bubblesort(aListQ)", number=1, globals=globals())
    aTimeTable[1][4] += timeit("quicksort(aListB, 0, len(aListQ)-1)", number=1, globals=globals())


for i in range(0, 2):
    print(aTimeTable[i][0])
    for j in range(1, 5):
        print(aTimeTable[i][j]/tablesToSort)
    print("\n")

for i in range(1, 5):
    if aTimeTable[0][i] < aTimeTable[1][i]:
        print(i, ". bubble better")
    else:
        print(i, ". quicksort better")