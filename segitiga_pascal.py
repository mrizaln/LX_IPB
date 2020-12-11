def binom(row, col):
    if row >= 0 and (col == 0 or col == row): return 1
    else: return binom(row - 1, col - 1) + binom (row - 1, col)

baris = int(input())
for i in range(baris):
    spasi = baris - i - 1
    while spasi > 0:
        print("  ", end = '')
        spasi -= 1
    for j in range(0, i + 1):
        print('%4u' % (binom(i, j)), end = '')
    print()
