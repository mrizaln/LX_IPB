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
