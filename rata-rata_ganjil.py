'''
          MENGHITUNG RATA-RATA GANJIL

Buatlah program untuk menentukan rata-rata dari bilangan ganjil yang muncul pada suatu selang yang diberikan.

> Format Masukan:
Masukan berupa dua buah bilangan bulat dipisahkan oleh spasi yang menunjukkan batas awal dan akhir selang. Batas akhir harus lebih besar dari batas awal.

> Format Keluaran:
Keluaran berupa bilangan bulat yang menunjukkan  rata-rata dari bilangan ganjil yang ada pada selang tersebut. Keluaran diakhiri newline.
'''

a, b = map(int, input().split())

ganjil = []
for i in range(a, b+1):
    if i % 2 == 1:
        ganjil.append(i)

print(ganjil)
rataan = sum(ganjil) / len(ganjil)
print(rataan, end = '\n')
