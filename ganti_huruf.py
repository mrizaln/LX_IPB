'''
          GANTI HURUF

Buatlah sebuah program python untuk mengganti setiap huruf yang sama dengan huruf pertama dari sebuah kata tetapi tidak mengganti huruf pertama itu sendiri, dengan karakter underscore (_).

> Format Masukan:
Sebuah kata

> Format Keluaran:
Kata yang telah berganti huruf yang sama dengan huruf awal string tersebut dengan karakter underscore (_). Baris keluaran diakhiri dengan newline.

> Contoh Masukan:
ubuntu

> Contoh Keluaran:
ub_nt_

'''

kata = input()
hurf = list(kata)

for i in range(len(kata) - 1):
    if kata[i + 1] == kata[0]: hurf[i + 1] = '_'

lett = ''
for i in hurf: lett += i
print(lett)
