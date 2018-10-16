from math import fabs


def quicksort(lst: list, start: int, stop: int) -> list:
    i = int(start)
    j = int(stop)
    pivot = int(lst[i + int(fabs(i-j)//2)])
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


'''
aList = [10, 20, 100, 40, 30, 60, 70, 80, 90, 1, 6, 9, 5, 2,2,2,2,2]
print(aList)

quicksort(aList, 0, len(aList)-1)
print(aList)
'''