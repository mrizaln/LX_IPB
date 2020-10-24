N = int(input())
a = list(map(int, input().split()))

b = 0
for i in range(N):
    b = b + a[i]

print(b, end = '\n')
