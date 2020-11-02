'''
          CETAK MATRIKS

Buat sebuah program untuk mencetak matriks sesuai dengan jumlah baris dan kolomnya.

> Format Masukan:
Baris pertama adalah dimensi matriks, yaitu jumlah baris dan kolom (maksimal 20). Baris kedua adalah elemen-elemen matriks.

> Format Keluaran:
Sebuah matriks, tiap elemen dipisahkan dengan spasi, tiap baris diakhiri newline (tidak ada spasi sebelum newline).
'''

baris, kolom = map(int, input().split())
elemen = list(map(int, input().split()))

a = 0
for i in range(baris):
    for j in range(kolom):
        print(elemen[a], end = '')
        a += 1
        if (j + 1) % kolom == 0: 
            print('\n', end = '')
        else:
            print(' ', end = '')
