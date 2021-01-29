'''
          PANGKAT REKURSIF

Rancanglah sebuah program untuk menghitung n pangkat p dengan fungsi rekursif:

               |   1			jika p = 0
pangkat(n,p) = |   n * pangkat(n,p-1)	jika p > 0
               | 1/n * pangkat(n,p+1)	jika p < 0 

> Format Masukan:
Masukan berupa satu baris yang terdiri atas dua bilangan bulat n dan p yang dipisahkan oleh spasi, dengan selang [-100,100].

> Format Keluaran:
Keluaran berupa satu baris yang terdiri atas satu bilangan real dalam notasi ilmiah (gunakan format cetak %E) dengan enam angka di belakang koma. Akhiri dengan newline.

> Contoh Masukan:
10 100

> Contoh Keluaran:
1.000000E+100
'''

def pangkat(n, p):
    if p == 0: return 1
    elif p > 0:
        return n * pangkat(n, p - 1)
    elif p < 0:
        return 1/n * pangkat(n, p + 1)

a, b = map(int, input().split())
h = pangkat(a, b)

print('%.6E' % h, end = '\n')
