a = int(input())

b = a // 60
bayar = 0
dasar = 2000
if b  < 1:
    bayar = dasar
if 1 <= b <= 6:
    bayar = dasar + b * 1000
if b > 6:
    bayar = 8000

print(bayar, end = '\n')
