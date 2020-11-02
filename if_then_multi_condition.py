'''
          IF THEN, MULTI CONDITON

Pak Dengklek memberikan Anda sebuah bilangan bulat N (-100.000 ≤ N ≤ 100.000). Jika N adalah bilangan genap positif, maka cetak kembali bilangan tersebut. Jika tidak, jangan cetak apa-apa.

> Format Masukan:
Baris pertama berisi sebuah bilangan bulat N.

> Format Keluaran:
Sebuah baris berisi keluaran sesuai permintaan soal.
'''

a = int(input())
 
if ((a % 2) == 0) and (a > 0):
    print(a)
