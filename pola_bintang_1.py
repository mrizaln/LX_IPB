'''
          POLA BINTANG 1

Diberikan sebuah bilangan bulat N yang berada pada rentang [1, 100], buatlah pola segitiga yang memiliki N baris dan N kolom. Sebagai contoh, jika N = 3, segitiga yang dihasilkan berbentuk:

*
**
***

> Format Masukan:
Sebuah bilangan bulat N.

> Format Keluaran:
Segitiga berukuran N yang sesuai dengan pola. Jangan mencetak spasi setelah tanda * terakhir pada setiap baris. Akhiri dengan mencetak karakter newline.
'''

N = int(input())

for i in range(N):
    for j in range(N):
        if i >= j:
            print('*', end = '')
    print()
