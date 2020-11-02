'''
          MENGHITUNG DERET BILANGAN

Buatlah program untuk menghitung jumlah satu baris bilangan.

> Format Masukan:
Masukan terdiri dari dua baris.
Baris pertama berupa banyaknya N bilangan (1<N<100),
baris kedua berupa bilangan yang akan dijumlahkan, dipisahkan oleh karakter spasi

> Format Keluaran:
Keluaran berupa hasil penjumlahan semua bilangan dan diakhiri newline
'''

N = int(input())
a = list(map(int, input().split()))

b = 0
for i in range(N):
    b = b + a[i]

print(b, end = '\n')
