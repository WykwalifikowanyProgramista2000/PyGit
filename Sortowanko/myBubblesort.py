def bubblesort(I: list):
    n = len(I)
    j = 0
    is_sorted = False
    passes = 0
    while j < n and is_sorted == False:
        is_sorted = True
        for i in range(1, n):
            #passes += 1
            if I[i - 1] > I[i]:
                I[i - 1], I[i] = I[i], I[i - 1]
                is_sorted = False
        j += 1
    #print("passes = ", passes)

'''
aList = [9, 8, 1, 2, 3, 4, 5, 6, 100, 7, 1, 1, 1, 1, 1, 5, 8, 0]
print(aList)

myBubblesort(aList)
print(aList)
'''
