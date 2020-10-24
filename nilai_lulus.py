uts, uas, prak, tugas = map(float, input().split())


nilai = 0.35 * uts + 0.35 * uas + 0.25 * prak + 0.05 * tugas

if nilai < 40:
    print("TIDAK LULUS", end = '\n')
else:
    print("LULUS", end = '\n')
