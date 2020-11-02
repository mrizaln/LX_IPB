'''
          AKAR PERSAMAAN KUADRAT

Rancang sebuah program untuk mencari akar persamaan kuadrat ax2 + bx + c = 0 dengan rumus x = (- b ± √d) / 2a, dengan determinan d = (b2 - 4ac). Gunakan fungsi sqrt() untuk menghitung akar kuadrat, yang terdapat pada pustaka math.

> Format Masukan:
Masukan berupa satu baris yang terdiri atas tiga bilangan bulat a, b, dan c yang membentuk persamaan kuadratik ax2 + bx + c = 0, dengan a ≠ 0.

> Format Keluaran:
Keluaran berupa akar persamaan kuadrat yang terdiri atas dua bilangan real x1 dan x2, dengan x1 ≥ x2. Jika d < 0, maka keluaran berupa kalimat Tidak memiliki akar real.. Gunakan "%g" untuk mencetak digit yang signifikan saja, akhiri keluaran dengan newline.
'''

from math import sqrt

a, b, c = map(int, input().split())

d = b**2 - 4*a*c

if d < 0:
    print("Tidak memiliki akar real.", end = "\n")
else:
    x1 = (-b + sqrt(d)) / (2*a)
    x2 = (-b - sqrt(d)) / (2*a)
    print("%g %g" % (x1, x2), end = "\n")
