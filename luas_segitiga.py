'''
          MENGHITUNG LUAS SEGITIGA
          
Buatlah sebuah program untuk menghitung luas segitiga. Program menerima dua buah masukan, yaitu nilai alas dan tinggi segitiga.

> Format Masukan:
Masukan berupa satu baris yang terdiri atas bilangan real a dan t yang dipisahkan oleh satu spasi. 

> Format Keluaran:
Keluaran berupa satu baris yang terdiri atas sebuah bilangan real dengan dua angka di belakang koma yang merupakan hasil perhitungan luas segitiga a*t/2 dan diakhiri newline.
'''

a, t = input().split()
a = float(a)
t = float(t)

luas = a*t/2

print('%.2f' % luas, end="\n")
