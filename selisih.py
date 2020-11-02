'''
          SELISIH

Rancang sebuah program untuk mengitung selisih antara dua bilangan bulat.

> Format Masukan:
Masukan berupa satu baris yang terdiri atas dua bilangan bulat dengan rentang [-100, 100].

> Format Keluaran:
Keluaran berupa satu baris yang terdiri atas satu bilangan asli selisih. Akhiri keluaran dengan newline.
'''

a, b = map (int, input().split())

c = a - b
c = abs(c)
print(c, end = '\n')
