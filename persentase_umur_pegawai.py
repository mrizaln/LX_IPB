def counter(v, x):
    count = 0
    for i in v:
        if i == x: count += 1
    return count

n = int(input())
val = [int(i) for i in input().strip().split()[:n]]
idx = sorted(list(dict.fromkeys(val)))

for i in idx:
    h = counter(val, i)
    res = round((h / n), 2)
    if res != 0: print('{:d} {:.2f}'.format(i, res))
