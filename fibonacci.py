'''
          FIBONACCI (KASUS KECIL)

Setiap suku pada deret Fibonacci diperoleh dengan menambahkan dua suku sebelumnya. Dengan asumsi suku pertama (F1) dan suku kedua (F2) bernilai 1, 10 suku pertama dari deret tersebut adalah:
      1, 1, 2,3, 5, 8, 13, 21, 34, 55, ...

Sekarang, buatlah program yang dapat mencetak suku Fibonaci ke-N. Pada kasus kecil ini, nilai N maksimum ialah 40.

Note:
Pada soal ini, anda masih dapat menggunakan fungsi rekursif yang memakan waktu eksponensial. Pada soal berikutnya, kasus besar akan digunakan sehingga anda harus menggunakan teknik yang lain yang lenih efisien.

> Format Masukan:
Masukan diawali oleh bilangan sebuah bilangan bulat M (1 <= M <= 40) yang merupakan banyaknya nilai Fibonacci yang dicari. M baris berikutnya menyatakan posisi bilangan Fibonacci (suku ke-N) merupakan bilangan bulat (1 <= N <= 40)

> Format Keluaran:
Keluaran terdiri atas M baris. Setiap baris terdiri atas satu bilangan bulat yang merupakan suku Fibonacci ke-N yang diminta pada setiap baris masukan. Keluaran diakhiri newline

> Contoh Masukan:
10
1
2
3
4
5
6
7
8
9
10

> Contoh Keluaran:
1
1
2
3
5
8
13
21
34
55

'''

def fibonacci(n):
    F1 = 1
    F2 = 1
    if n == 1: return 1
    else:
        for i in range (2, n):
            F3 = F1 + F2
            F1, F2 = F2, F3
        return F2

N = int(input())

pos = []
for i in range (N): pos.append(int(input()))

ls = [fibonacci(j) for j in pos]

for i in ls: print(i, end = '\n')
