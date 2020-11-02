'''
          KONVERSI USIA

Dapatkanlah nilai satuan tahun dan bulan dari usia yang diketahui dalam satuan bulan. Sebagai contoh, usia 14 bulan akan dikonversi menjadi 1 tahun dan 2 bulan (nilai tahun = 1 dan nilai bulan = 2).

> Format Masukan:
Masukan terdiri atas sebuah bilangan bulat yang merupakan usia dalam satuan bulan. Nilai ini berada pada rentang (0, 1200].

> Format Keluaran:
Keluaran berupa dua buah bilangan bulat yang dipisahkan oleh karakter spasi. Bilangan bulat pertama merupakan nilai tahun dan bilangan kedua merupakan nilai bulan. Akhiri keluaran dengan karakter newline ('\n'). 
'''

a = int(input())

thn = a // 12
bln = a - 12 * thn

print(thn, bln, end="\n")
