bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

a = int(input())

if 1 <= a <= 12:
    print(bulan[a-1], end = '\n')
else:
    print('Input tidak valid', end = '\n')
