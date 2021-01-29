'''
          PERSENTASE UMUR

Anda diminta untuk membuat sebuah program yang menghitung persentase umur dari N orang pegawai. Pegawai paling banyak berjumlah 1000 orang.

> Format Masukan:
Baris pertama adalah sebuah bilangan bulat N yang merupakan banyaknya pegawai. Baris kedua terdiri atas N buah bilangan bulat positif yang dipisahkan oleh spasi yang merupakan usia dari setiap pegawai.

> Format Keluaran:
Keluaran terdiri atas bbeberapa baris bilangan yang setiap barisnya terdiri atas sebuah bilangan bulat X dan bilangan real Y yang dipisahakan oleh spasi. X adalah usia dan Y adalah persentase pegawai yang memiliki usia tersebut, dibulatkan 2 angka di belakang koma.

> Contoh Masukan:
10
28 28 28 29 30 24 24 25 27

> Contoh Keluaran:
24 0.20
25 0.20
27 0.10
28 0.30
29 0.10
30 0.10

'''

def counter(v, x):
    count = 0
    for i in v:
        if i == x: count += 1
    return count

n = int(input())
val = [int(i) for i in input().strip().split()[:n]]
idx = sorted(list(dict.fromkeys(val)))

for i in idx:
    h = counter(val, i)
    res = round((h / n), 2)
    if res != 0: print('{:d} {:.2f}'.format(i, res))
