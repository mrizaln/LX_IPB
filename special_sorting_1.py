

n = int(input())
item = [int(i) for i in input().split()]
item.sort()

even = []
odd = []

if len(item) != n:
    print('Data tidak sesuai')
else:
    for i in item:
        if i % 2 == 0: even.append(i)
        else: odd.append(i)
    even = even[::-1]
    odd = odd[::-1]
    even.extend(odd)
    print(*even, end = ' ')

