def jumlah_digit(a):
    if len(a) == 0: return 0
    else:
        a_sliced = a[1:len(a)]
        return int(a[0]) + jumlah_digit(a_sliced)

n = input()
h = jumlah_digit(n)

print(h, end = '\n')
