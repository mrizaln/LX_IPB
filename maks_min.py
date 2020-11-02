'''
      MAKSIMUM DAN MINIMUM 3 BILANGAN (Menggunakan Function)

Diberikan tiga buah bilangan x,y, dan z yang masing-masing merupakan bilangan bulat. Cetaklah nilai terbesar dan terkecil dari ketiga bilangan tersebut dengan tidak diakhiri newline.
 
> Format Masukan:
Satu baris berisi 3 bilangan bulat yang dipisahkan oleh spasi

> Format Keluaran:
Satu baris keluaran yang berisi bilangan maksimal dan minimal yang dipisahkan spasi.

'''

x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

maks = max(x, y, z)
minn = min(x, y, z)

print("%d %d" % (maks, minn), end = "")
