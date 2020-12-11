def binary_search(lst, X):
    ind = list(range(len(lst)))
    lst.sort()

    start = 0
    end = len(lst) - 1
    found = False

    while start <= end and not found:
        mid = (start + end) // 2
        if lst[mid] == X: found = True
        else:
            if X < lst[mid]: end = mid - 1
            else: start = mid + 1

    if found == False: ind[mid] = -1
    return ind[mid]

N = int(input())
daftar = list(map(int, input().split()))
item = int(input())

posisi = binary_search(daftar, item)
print (posisi, end = '\n')
