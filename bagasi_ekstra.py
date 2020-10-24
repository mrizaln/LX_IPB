from math import ceil

banyak = int(input())
berat = list(map(float, input().split()))
batas_berat = int(input())
biaya_ekstra = int(input())

berat_total = sum(berat)

if berat_total > batas_berat:
    berat_ekstra = round(berat_total - batas_berat, 1)
    total_biaya_ekstra = ceil(berat_ekstra) * biaya_ekstra
    print('bagasi ekstra {a} kg, biaya ekstra {b} rupiah'.format(a = berat_ekstra, b = total_biaya_ekstra))
else:
    print('tidak ada bagasi ekstra')
