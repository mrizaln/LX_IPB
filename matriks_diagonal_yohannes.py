n = int(input())
matriks = str(input())
matriks = matriks.split()

indeks = 0
for i in range(n):
    for j in range(n):
        if j == indeks and j == n - 1:
            print(matriks[indeks], end = '\n')
        elif j == indeks and j != n - 1:
            print(matriks[indeks], end = ' ')
        elif j != indeks and j == n - 1:
            print('0', end = '\n')
        else:
            print('0', end = ' ')
    indeks += 1

