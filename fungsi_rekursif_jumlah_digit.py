'''
          FUNGSI REKURSIF

Contoh fungsi rekursif (bukan python):

    (define (faktorial n)
        if (= n 0
            1
            (* n (faktorial (- n 1)))
        )
    )
    (display (faktorial (read)))
    (newline)

Buatlah program fungsional untuk menghitung jumlah dari setiap digit penyusun suatu bilangan bulat. Sebagai contoh, jumlah digit dari 234 adalah 9 (yaitu 2+3+4).
'''

def jumlah_digit(a):
    if len(a) == 0: return 0
    else:
        a_sliced = a[1:]
        return int(a[0]) + jumlah_digit(a_sliced)

n = input()
h = jumlah_digit(n)

print(h, end = '\n')
