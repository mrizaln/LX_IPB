'''
          SPECIAL SORTING

Buatlah sebuah fungsi yang dapat mengurutkan item pada list yang mana semua bilangan genap terurut berada di awal list, kemudian diikuti dengan semua bilangan ganjil terurut. Item diurutkan dari yang terbesar hingga yang terkecil.

> Format Masukan:
Terdapat dua baris masukan. Baris pertama adalah n jumlah item yang ada dalam list. Baris kedua adalah dagtar item yang ada pada list.

> Format Keluaran:
Menampilkan list yang mana bagian awal list merupakan bilangan genap terurut, kemudian diikuti dengan bilangan ganjil terurut. Semua bagian diurutkan dari bilangan terbesar hingga yang terkecil. Setiap item list dipisahkan oleh sebuah spasi.

Note: pastikan jumlah daftar item yang anda masukkan sama dengan jumlah item yang anda definisikan. Jika tidak sesuai maka program akan menampilkan "Data tidak sesuai".

> Contoh Masukan:
10
1 2 3 4 5 6 7 8 9 10

> Contoh Keluaran:
10 8 6 4 2 9 7 5 3 1

'''

def special_sorter(ls):
    even = []
    odd = []
    for i in ls:
        if i % 2 == 0: even.append(i)
        else: odd.append(i)
    even = even[::-1]
    odd = odd[::-1]
    num = even + odd
    return num

N = int(input())
item = [int(i) for i in input().split()]
if len(item) != N: print('Data tidak sesuai')
else:
    resl = special_sorter(item)
    for i in resl: print(str(i), end = ' ')
    print()

