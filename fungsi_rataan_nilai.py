def rataan():
    uts, uas, tugas = map(int, input().split())
    nilai = 0.4 * uts + 0.4 * uas + 0.2 * tugas
    return nilai

b = rataan()

print(b)

