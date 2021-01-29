'''
          BINARY SEARCH

Diberikan N (1 <= N <= 1 juta) integer terurut, tugas anda adalah menemukan indeks tempat bilangan bulat X berada. Setiap bilangan hanya muncul tepat satu kali. Sesuai judul, jangan pakai sekuensial search (Buka catatan kuliah dan atau Google untuk mencari tahu tentang binary search).

> Format Masukan:
Bilangan bulat N. Diikuti N bilangan bulat diikuti dengan bilangan bulat X

> Format Keluaran:
Sebuah bilangan bulat yang merupakan indeks tempat X berada. Keluarkan -1 jika tidak ada. Akhiri baris dengan newline.

> Contoh Masukan:
12
0 1 1 2 3 4 5 6 7 8 9 10
6

> Contoh Keluaran:
7

'''


def binary_search(lst, X):
    ind = list(range(len(lst)))
    lst.sort()	#redundant sebenarnya line ini, karena input sudah terurut

    start = 0
    end = len(lst) - 1
    found = False

    while start <= end and not found:
        mid = (start + end) // 2
        if lst[mid] == X: found = True
        else:
            if X < lst[mid]: end = mid - 1
            else: start = mid + 1

    if found == False: ind[mid] = -1
    return ind[mid]

N = int(input())
daftar = list(map(int, input().split()))
item = int(input())

posisi = binary_search(daftar, item)
print (posisi, end = '\n')
