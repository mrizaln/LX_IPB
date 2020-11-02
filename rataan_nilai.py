'''
          MENGHITUNG RATAAN UJIAN

Buat program menghitung nilai rata-rata dari dua ujian (UTS dan UAS) dan satu tugas. Ujian UTS dan UAS masing-masing diberi bobot 40%, sedangkan tugas diberi bobot 20%.

> Format Masukan:
Input data berupa tiga nilai berturut-turut uts, uas, dan tugas yang semuanya bilangan bulat dengan selang -25 sampai dengan 100. Masing-masing nilai dipisahkan oleh satu spasi.

> Format Keluaran:
Sebuah bilangan pecahan (dua angka di belakang koma) hasil rata-rata dari nilai uts, uas, dan tugas dengan bobot sesuai ketentuan di atas. Output program selalu diakhiri dengan newline
'''

uts, uas, tugas = input().split()
uts = float(uts)
uas = float(uas)
tugas = float(tugas)

nilai = 0.4*uts + 0.4*uas + 0.2*tugas

print('%.2f' % nilai, end="\n")
