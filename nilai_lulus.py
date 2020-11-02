'''
          NILAI LULUS

Rancang sebuah program untuk menentukan status kelulusan dari nilai uts, uas, ujian praktikum dan nilai tugas seorang mahasiswa. Bobot nilai uts 35%, uas 35%, ujian praktikum 25% dan tugas 5%. Jika nilai akhir kurang dari 40, maka mahasiswa tidak lulus.

> Format Masukan:
Masukan berupa satu baris yang terdiri atas bilangan real uts, uas, ujian praktikum, dan tugas yang dipisahkan oleh satu spasi. Rentang nilai ialah [0, 100].

> Format Keluaran:
Keluaran berupa kata "LULUS" atau "TIDAK LULUS" yang dicetak pada layar sesuai dengan nilai akhir mahasiswa. Akhiri baris dengan karakter newline.
'''

uts, uas, prak, tugas = map(float, input().split())


nilai = 0.35 * uts + 0.35 * uas + 0.25 * prak + 0.05 * tugas

if nilai < 40:
    print("TIDAK LULUS", end = '\n')
else:
    print("LULUS", end = '\n')
