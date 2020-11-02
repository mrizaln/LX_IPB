'''
          TARIF PARKIR

Rancang sebuah program untuk menghitung besarnya tarif parkir.
Tarif dasar parkir (kurang dari satu jam) adalah 2000.
Untuk setiap jam berikutnya, tarif parkir bertambah 1000.
Tarif parkir maksimal adalah 8000.

> Format Masukan:
Masukan berupa satu baris yang terdiri atas satu bilangan asli lama parkir dalam menit.

> Format Keluaran:
Keluaran berupa satu baris yang terdiri atas satu bilangan asli tarif parkir. Akhiri keluaran dengan newline.
'''

a = int(input())

b = a // 60
bayar = 0
dasar = 2000
if b  < 1:
    bayar = dasar
if 1 <= b <= 6:
    bayar = dasar + b * 1000
if b > 6:
    bayar = 8000

print(bayar, end = '\n')
