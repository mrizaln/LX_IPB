'''
          TARIF KRL FLEKSIBEL

Seorang manajer perusahaan kereta api ingin merancang skema tarif KRL yang fleksibel agar mudah disesuaikan dari waktu ke waktu. Skema tersebut melibatkan:

    MIN: tarif minimum
    K: jumlah stasiun yang tercakup dalam M
    S: tarif per stasiun setelah K
    MAKS: tarif maksimum

Buatlah program yang menghitung besaran tarif untuk perjalanan N stasiun dengan skema tertentu.

Besaran tarif didapat dengan cara mengalikan tarif per stasiun dengan jumlah stasiun yang dilewati yang dikurangi dengan jumlah stasiun yang tercakup dalam tarif minimum. Jika jumlah stasiun yang dilewati masih tercakup dalam M, maka tarif yang dibayarkan adalah tarif minimum. Sementara, jika tarif yang dibayarkan telah melewati tarif maksimum, maka tarif yang dibayarkan adalah tarif maksimum tersebut.

> Format Masukan:
Baris pertama berisikan MIN, K, S, dan MAKS yang dipisahkan spasi.

Baris kedua berisikan N.

> Format Keluaran:
Tarif yang dikenakan. Keluaran diakhiri newline.
'''

MIN, K, S, MAKS = map(int, input().split())
N = int(input())

if N <= K:
    print(MIN, end = '\n')
else:
    tarif = MIN + (N - K) * S
    if tarif > MAKS:
        print(MAKS, end = '\n')
    else:
        print(tarif, end = '\n')
