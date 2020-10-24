N = int(input())
elemen = list(map(int, input().split()))

a = 0
for i in range(N):
    for j in range(N):
        if i == j:           print(elemen[a], end = '')
        else:                print('0', end = '')

        if (j + 1) % N == 0: print()
        else:                print(' ', end = '')
    a += 1
