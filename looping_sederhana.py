'''
          LOOPING SEDERHANA

Agri dihukum karena tidak membuat PR Algoritme Pemrograman, dia dihukum untuk menulis kalimat secara berulang-ulang.

Karena Agri butuh bantuan, buatlah program untuk membantu Andi untuk memudahkan menulis kalimat tersebut dengan cepat.

> Format Masukan:
Masukan berupa N bilangan (1<N<1000)

> Format Keluaran:
Berupa kalimat yang dicetak sebanyak N, "Saya tidak akan mengulangi kesalahan saya lagi" dan diakhiri dengan newline (tanpa tanda petik)
'''

N = int(input())

for i in range(N):
    print('Saya tidak akan mengulangi kesalahan saya lagi', end = '\n')
