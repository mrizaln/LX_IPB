'''
          FUNGSI FAKTORIAL REKURSIF

     | 1 		jika n=0
n! = | 
     | n x (n-1)!	jika n>0

Lengkapi kode program di bawah ini pada bagian fungsi untuk menghitung nilai faktorial secara rekursif.
     
     def faktorial(n):
         #...
         
     x = int(input())
     print(faktorial(x)

> Format Masukan:
Masukan berupa satu baris yang terdiri atas satu bilangan asli [0, 25] diikuti dengan karakter '!'.

> Format Keluaran:
Keluaran berupa satu baris yang terdiri dari satu bilangan ral (long double) tanpa angka di belakang koma. Akhiri keluaran dengan newline.

> Contoh Masukan:
25!

>Contoh Keluaran:
15511210043330985984000000 
'''

def factorial(n):
    n = int(n[:-1])
    if n == 1:
        return n
    else:
        return factorial(n - 1) * n

x = input()
print(factorial(x), end = '\n')
