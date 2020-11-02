'''
          JUMLAH TIDAK LULUS

Rancang sebuah program untuk menghitung jumlah siswa yang tidak lulus karena nilainya di bawah batas kelulusan.

> Format Masukan:
Masukan terdiri atas tiga baris:

    Baris pertama adalah banyaknya siswa, berupa satu integer n.
    Baris kedua adalah nilai siswa, sejumlah n integer yang dipisahkan spasi.
    Baris ketiga adalah batas kelulusan, berupa satu bilangan real.

> Format Keluaran:
Keluaran berupa jumlah siswa yang tidak lulus dan rataan kelas berupa bilangan real dengan satu angka di belakang koma. Baris keluaran diakhiri newline. Format selengkapnya lihat pada contoh keluaran.

> Contoh Masukan:
5
63 51 34 75 81
49.5

> Contoh Keluaran:
1 dari 5 siswa tidak lulus, rataan kelas 60.8
'''

banyak_siswa = int(input())
nilai = list(map(int, input().split()))
batas_lulus = float(input())

jumlah = 0
banyak_tidak_lulus = 0
for i in nilai:
    if i < batas_lulus:
        banyak_tidak_lulus += 1
    jumlah += i

rataan = round(jumlah / banyak_siswa, 1)

print('{} dari {} siswa tidak lulus, rataan kelas {}'.format(banyak_tidak_lulus, banyak_siswa, rataan))
