from math import sqrt

a, b, c = map(int, input().split())

d = b**2 - 4*a*c

if d < 0:
    print("Tidak memiliki akar real.", end = "\n")
else:
    x1 = (-b + sqrt(d)) / (2*a)
    x2 = (-b - sqrt(d)) / (2*a)
    print("%g %g" % (x1, x2), end = "\n")
