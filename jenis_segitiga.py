'''
          JENIS SEGITIGA

Rancang sebuah program untuk menentukan jenis segitiga berdasarkan besar ketiga sudutnya.

> Format Masukan:
Masukan berupa satu baris yang terdiri atas bilangan asli sudut a, b, dan c (dalam derajat) yang dipisahkan oleh satu spasi. Rentang sudut ialah (0°, 180°) dan jumlah semua sudut dijamin selalu 180°.

> Format Keluaran:
Keluaran berupa jenis segitiga dengan ketentuan sebagai berikut:

    jika ketiga sudutnya sama besar, cetak "Segitiga sama-sisi"
    jika semua sudutnya kurang dari 90°, cetak "Segitiga lancip"
    jika salah satu sudutnya 90°, cetak "Segitiga siku-siku"
    jika salah satu sudutnya lebih dari 90°, cetak "Segitiga tumpul"
    jika dua sudut saja yang sama besar, tambahkan kata " sama-kaki"

Bantuan: ada 7 kemungkinan keluaran yang mungkin: Segitiga sama-sisi, Segitiga lancip, Segitiga siku-siku, Segitiga tumpul, Segitiga lancip sama-kaki, Segitiga siku-siku sama-kaki, Segitiga tumpul sama-kaki.

Akhiri keluaran dengan karakter newline.
'''

a, b, c = map(int, input().split())

d = 'Segitiga'
if a == b == c:
    d = d + ' sama-sisi'

else:
    if a == 90 or b == 90 or c == 90:
        d = d + ' siku-siku'
    elif a < 90 and b < 90 and c < 90:
        d = d + ' lancip'
    elif a > 90 or b > 90 or c > 90:
        d = d + ' tumpul'

if (a == b or a == c or b == c) and not (a == b == c):
   d = d + ' sama-kaki'

print(d)
