'''
          ingly

Dalam seuah bahasa di planet Namec, terdapat kata yang berakhiran -ing dan juga -ly. Buatlah sebuah program yang menambahkan akhiran -ing jika kata yang dimasukkan lebih dari 2 karakter. Jika masukan kata tersebut sudah berakhiran -ing, tambahkan dengan akhiran -ly. Jika kata kurang dari 3 karakter, cetak kata tersebut tanpa diubah sedikitpun.

> Format Masukan:
1 buah kata

> Format Keluaran:
1 buah kata berakhiran -ing atau ly atau kata itu sendiri (sesuai ketentuan soal). Keluaran diakhiri newline.

> Contoh Masukan 1:
burn

> Contoh Keluaran 1:
burning

> Contoh Masukan 2:
runcing

> Contoh Keluaran 2:
runcingly

> Contoh Masukan 3:
itu

> Contoh Keluaran 3:
ituing

> Contoh Masukan 4:
oi

> Contoh Keluaran 4:
oi

'''


str = input()

if len(str) > 2:
    if str[-3:] == 'ing': str += 'ly'
    else: str += 'ing'

print(str, end = '\n')
