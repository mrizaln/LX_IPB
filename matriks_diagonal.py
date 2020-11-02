'''
          MATRIKS DIAGONAL

Buatlah program yang dapat menghasilkan matriks persegi diagonal berukuran n x n. Diagonal dari matriks diisi dengan angka-angka yang diberikan sebagai input, sedangkan sisanya diisi nol.

> Format Masukan:
Masukan terdiri atas dua baris. Baris pertama adalah n, yaitu ukuran baris dan kolom matriks (1 <= n <= 100). Baris kedua adalah angka-angka sebanyak n, dengan masing-masing angka dalam rentang 0 <= x <= 9.

> Format Keluaran:
Keluaran adalah matriks berukuran n x n sesuai ketentuan. Setiap elemen matriks dipisahkan dengan satu spasi, kecuali kolom terakhir yang langsung berupa newline tanpa spasi.
'''

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
