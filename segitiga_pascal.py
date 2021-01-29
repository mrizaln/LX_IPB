'''
          SEGITIGA PASCAL REKURSIF

Rancanglah sebuah program untuk mencetak segitiga pascal secanyak n baris. Segitiga pascal tersusun atas koefisien binomial. Berikut adalah protoripe dan definisi fungsi rekursif untuk menghitung koefisien binomial:

           | 1				jika k = 0 atau k = n
(n, k)^T = |
           | (n-1, k-1)^T + (n-1, k)^T	jika 0 < k < n

							  | a |
Note: ^T menunjukkan transpose matriks, misal (a,b,c)^T	= | b |
 							  | c |
> Format Masukan:
Masukan berupa satu baris yang terdiri atas satu bilangan asli n, dnegan selang [1, 12]

> Format Keluaran:
Keluaran berupa segitiga Pascal sebanyak n baris yang terdiri atas bilangan asli koefisien binomial yang dicetak dengan lebar 4 karakter (gunakan "4u" pada print). Akhiri keluaran dengan newline.

> Contoh Masukan:
5

> Contoh Keluaran:
           1
         1   1
       1   2   1
     1   3   3   1
   1   4   6   4   1 

'''

def binom(row, col):
    if row >= 0 and (col == 0 or col == row): return 1
    else: return binom(row - 1, col - 1) + binom (row - 1, col)

baris = int(input())
for i in range(baris):
    spasi = baris - i - 1
    while spasi > 0:
        print("  ", end = '')
        spasi -= 1
    for j in range(0, i + 1):
        print('%4u' % (binom(i, j)), end = '')
    print()
