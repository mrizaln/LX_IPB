'''
        MENGHITUNG LUAS KUBUS
        
Rancang sebuah program untuk menghitung luas sebuah kubus, jika diketahui panjang sisi kubus tersebut. Input berupa sisi kubus yang dimasukkan oleh pengguna.

> Format Masukan:
Masukan berupa satu baris yang terdiri atas satu bilangan asli s (1 ≤ s ≤ 100).

> Format Keluaran:
Keluaran berupa satu baris yang terdiri atas sebuah bilangan asli yang merupakan hasil perhitungan luas kubus 6*s*s dan diakhiri dengan newline.
'''

s = int(input())
luas = 6*s*s

print(luas, end="\n")
