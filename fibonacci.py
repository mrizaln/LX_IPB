def fibonacci(n):
    F1 = 1
    F2 = 1
    if n == 1: return 1
    else:
        for i in range (2, n):
            F3 = F1 + F2
            F1, F2 = F2, F3
        return F2

N = int(input())

pos = []
for i in range (N): pos.append(int(input()))

ls = [fibonacci(j) for j in pos]

for i in ls: print(i, end = '\n')
