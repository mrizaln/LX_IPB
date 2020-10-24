baris, kolom = map(int, input().split())
elemen = list(map(int, input().split()))

a = 0
for i in range(baris):
    for j in range(kolom):
        print(elemen[a], end = '')
        a += 1
        if (j + 1) % kolom == 0: 
            print('\n', end = '')
        else:
            print(' ', end = '')
