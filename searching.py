def searching(ls, item):
    try:
        idx = ls.index(item)
        return idx
    except:
        return -1

N = int(input())
daft = [int(i) for i in input().split()[:N]]
itm = int(input())

h = searching(daft, itm)
if h >= 0: print('Ada')
else: print('Tidak Ada')
print(h)

