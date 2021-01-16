rc = [int(i) for i in input().split()]

matrix = []
for i in range(rc[0]):
    row =[int(n) for n in input().split()[:rc[1]]]
    matrix.append(row)

k = [int(i) for i in input().split()]

for i in range(k[0], k[1]+1):
    for j in range(k[2], k[3]+1):
        print(matrix[i][j], end = ' ')
    print()
