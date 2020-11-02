'''
          NAMA BULAN

Rancang sebuah program untuk mengkonversi dari nomor bulan menjadi nama bulan. Berikut adalah urutan nama bulan yang diinginkan.

Januari, Februari, Maret, April, Mei, Juni, Juli, Agustus, September, Oktober, November, Desember

> Format Masukan:
Masukan berupa satu baris yang terdiri atas bilangan asli nomor bulan.

> Format Keluaran:
Keluaran berupa nama bulan. Jika input selain [1, 12], keluaran berupa kalimat "Input tidak valid". Akhiri keluaran dengan karakter newline.
'''

bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

a = int(input())

if 1 <= a <= 12:
    print(bulan[a-1], end = '\n')
else:
    print('Input tidak valid', end = '\n')
