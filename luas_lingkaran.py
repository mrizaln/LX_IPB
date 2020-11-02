'''
          MENGHITUNG LUAS LINGKARAN

Di pekan ini, Anda akan berlatih menggunakan operator matematika dan tipe data. Pada soal ini, tugas Anda ialah merancang sebuah program untuk menghitung luas sebuah lingkaran jika diketahui panjang jari-jari lingkaran tersebut. Gunakanlah nilai pi sebesar 3.14. Input berupa jari-jari lingkaran yang dimasukkan oleh pengguna (gunakanlah fungsi scanf).

> Format Masukan:
Masukan berupa satu baris yang terdiri atas satu bilangan asli r (1 ≤ r ≤ 100).

> Format Keluaran:
Keluaran berupa sebuah bilangan real dengan dua angka di belakang koma yang merupakan luas lingkaran. Akhiri baris dengan karakter newline.
'''

r = int(input())

A = 3.14 * r ** 2

print('%.2f' % A, end = '\n')
