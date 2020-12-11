inp = input().lower()

lst = list(dict.fromkeys(inp))
key = []
for i in lst:
    if i.isalpha(): key.append(i)

key.sort()

for i in key:
    cnt = 0
    for j in inp:
        if j == i: cnt += 1
    print('{}: {}'.format(i, cnt), end = '\n')
