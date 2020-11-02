'''
BAGASI EKSTRA

Rancang sebuah program untuk menghitung biaya bagasi ekstra jika berat bagasi melebihi batas yang ditentukan.

> Format Masukan:
Masukan terdiri atas empat baris:

    Baris pertama adalah banyaknya koper, berupa satu integer n.
    Baris kedua adalah berat tiap koper dalam kg, sejumlah n bilangan real yang dipisahkan spasi.
    Baris ketiga adalah batas berat bagasi, berupa satu integer.
    Baris keempat biaya ekstra bagasi per kg, berupa satu integer.

> Format Keluaran:
Keluaran berupa berat total bagasi berupa bilangan real dengan satu angka di belakang koma dan biaya ekstra bagasi jika ada. Biaya ekstra dihitung dari berat bagasi ekstra dengan pembulatan ke atas. Jika tidak ada bagasi ekstra, ikuti format selengkapnya pada contoh keluaran.

> Contoh Masukan:
4
3.2 5.0 6.0 3.0
15
15000

> Contoh Keluaran:
bagasi ekstra 2.2 kg, biaya ekstra 45000 rupiah

> Contoh Masukan 2:
4
3.2 5.0 6.0 3.0
20
15000

> Contoh Keluaran 2:
tidak ada bagasi ekstra
'''

from math import ceil

banyak = int(input())
berat = list(map(float, input().split()))
batas_berat = int(input())
biaya_ekstra = int(input())

berat_total = sum(berat)

if berat_total > batas_berat:
    berat_ekstra = round(berat_total - batas_berat, 1)
    total_biaya_ekstra = ceil(berat_ekstra) * biaya_ekstra
    print('bagasi ekstra {a} kg, biaya ekstra {b} rupiah'.format(a = berat_ekstra, b = total_biaya_ekstra))
else:
    print('tidak ada bagasi ekstra')
