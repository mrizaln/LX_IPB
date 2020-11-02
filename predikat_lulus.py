'''
          PREDIKAT LULUS

Rancang sebuah program untuk menentukan predikat kelulusan mahasiswa S1 yang ditentukan berdasarkan (1) IPK, (2) lama masa studi, (3) jumlah nilai C, (4) jumlah nilai D, (5) perkuliahan ulang, dan (6) sanksi akademik tertulis. Asumsi: semua mahasiswa telah memenuhi beban kurikulum tanpa nilai E dengan IPK >= 2.00.

    Cum Laude
        IPK > 3.5
            Lama masa studi <= 5 tahun
            Maksimum satu nilai C
            Tidak ada nilai D
            Tidak pernah mengikuti perkuliahan ulang
            Tidak pernah terkena sanksi akademik tertulis

    Sangat Memuaskan
        IPK > 3.5
            Tidak memenuhi syarat "Cum Laude"
            Tidak ada nilai D
            Tidak pernah terkena sanksi akademik tertulis
        2.75 < IPK <= 3.5
            Lama masa studi <= 5 tahun
            Tidak ada nilai D
            Tidak pernah terkena sanksi akademik tertulis

    Memuaskan
        IPK > 3.5
            Tidak memenuhi syarat "Sangat Memuaskan"
        2.75 < IPK <= 3.5
            Tidak memenuhi syarat "Sangat Memuaskan"
        2.00 <= IPK <= 2.75

> Format Masukan:
Masukan berupa satu baris yang terdiri atas IPK, LamaStudi (dalam bulan), NilaiC, NilaiD, KuliahUlang (Y/N), dan Sanksi (Y/N). Rentang IPK ialah [2.00, 4.00], rentang LamaStudi ialah [36, 84], rentang jumlah NilaiC dan NilaiD ialah [0, 48].

> Format Keluaran:
Keluaran berupa predikat lulus "Cum Laude", "Sangat Memuaskan", atau "Memuaskan". Akhiri keluaran dengan karakter newline.
'''

IPK         = float(input('IPK: '))
LamaStudi   = int(input('lama studi (36 - 84): '))
NilaiC      = int(input('banyak nilai C: '))
NilaiD      = int(input('banyak nilai D: '))
KuliahUlang = input('pernah kuliah ulang? (Y/N): ')
Sanksi      = input('pernah terkena sanksi? (Y/N): ')

if IPK > 3.5:
    if LamaStudi <= 5*12 and NilaiC <= 1 and NilaiD == 0 and KuliahUlang == 'N' and Sanksi == 'N':
        print('Cum Laude')
    elif (LamaStudi > 5*12 or NilaiC > 1  or KuliahUlang == 'Y') and NilaiD == 0 and Sanksi == 'N':
        print('Sangat Memuaskan')
    else:
        print('Memuaskan')

elif 2.75 < IPK <= 3.5:
    if LamaStudi <= 5*12 and NilaiD == 0 and Sanksi == 'N':
        print('Sangat Memuaskan')
    else:
        print('Memuaskan')

else:
    print('Memuaskan')

print()
