'''
          BELAJAR PENGURANGAN

Pada soal ini, anda akan berlatih membaca masukan dari pengguna dan melakukan operasi pengurangan sederhana.

> Format Masukan:
Masukan berupa satu baris yang terdiri atas bilangan bulat a dan b yang dipisahkan oleh satu spasi. Gunakanlah tipe data int untuk kedua variabel tersebut.

> Format Keluaran:
Keluaran berupa sebuah bilangan bulat yang merupakan hasil pengurangan a - b. Akhiri baris dengan karakter newline.
'''

a, b = input().split()
a = int(a)
b = int(b)

c = a - b

print(c, end = '\n')
