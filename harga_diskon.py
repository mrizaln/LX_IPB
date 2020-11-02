'''
          HARGA DISKON

Rancang sebuah program untuk menghitung total harga yang harus dibayar seorang pembeli jika terdapat ketentuan diskon. Jika total harga barang yang dibeli lebih besar dari 1 juta, pembeli mendapatkan diskon 30%, jika totalnya antara 500 ribu dan 1 juta (500.000 <= total <= 1.000.000), maka berhak mendapatkan 20%, jika lebih kecil dari 500 ribu, maka tidak mendapatkan diskon.

> Format Masukan:
Masukan berupa satu baris yang terdiri atas satu bilangan asli harga total. Rentang harga total ialah [0, 2000000]. Harga total selalu kelipatan 50, misalnya 12750.

> Format Keluaran:
Keluaran berupa sebuah bilangan asli yang merupakan harga total setelah didiskon. Akhiri baris dengan karakter newline.
'''

a = int(input())

if 500000 <= a <= 1000000:
    a = a - a * 0.2
elif a > 1000000:
    a = a - a * 0.3

a = int(a)
print(a)
