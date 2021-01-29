'''
          SEARCHING (Binary Search)

Buatlah sebuah fungsi pada python yang dapat mencari suatu item pada list.

> Format Masukan:
Masukan terdiri dari tiga baris. Baris pertama adalah n jumlah item yang ada pada list. Baris kedua adalah daftar item yang ada pada list. Baris ketiga adalah item yang akan dicari di dalam list.

> Format Keluaran:
Keluaran terdiri dari dua baris. Baris pertama akan menampilkan kata "Ada", jika item terdapat pada list. Namun jika tidak ada, maka akan menampilkan kata "Tidak Ada". Baris kedua akan menampilkan posisi item tersebut pada list. Jika item tidak terdapat pada list, maka posisi item tersebut = -1

> Contoh Masukan 1:
5
10 20 30 40 50
60

> Contoh Keluaran 1:
Tidak Ada
-1

> Contoh Masukan 2:
5
10 20 30 40 50
50

> Contoh Keluaran 2:
Ada
4

'''

#Kode hanya bekerja jika item yang dicari berada pada list yang terurut (karena binary search)

def binary_search(lst, X):
    ind = list(range(len(lst)))
    lst.sort() #redundant inii (list yang masuk sudah terurut, tapi tak apalah)

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

if posisi == -1: print('Tidak Ada')
else: print('Ada')
print (posisi)
