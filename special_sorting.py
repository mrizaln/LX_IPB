def special_sorter(ls):
    even = []
    odd = []
    for i in ls:
        if i % 2 == 0: even.append(i)
        else: odd.append(i)
    even = even[::-1]
    odd = odd[::-1]
    num = even + odd
    return num

N = int(input())
item = [int(i) for i in input().split()]
if len(item) != N: print('Data tidak sesuai')
else:
    resl = special_sorter(item)
    for i in resl: print(str(i), end = ' ')
    print()

