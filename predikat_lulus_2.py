IPK         = float(input('IPK: '))
LamaStudi   = int(input('lama studi (36 - 84): '))
NilaiC      = int(input('banyak nilai C: '))
NilaiD      = int(input('banyak nilai D: '))
KuliahUlang = input('pernah kuliah ulang? (Y/N): ')
Sanksi      = input('pernah terkena sanksi? (Y/N): ')

a = [IPK, LamaStudi, NilaiC, NilaiD, KuliahUlang, Sanksi]

if a[0] > 3.5      : a[0] = 1
else               : a[0] = 0
if a[1] <= 5*12    : a[1] = 1
else               : a[1] = 0
if a[2] <= 1       : a[2] = 1
else               : a[2] = 0
if a[3] == 0       : a[3] = 1
else               : a[3] = 0
if a[4] == 'N'     : a[4] = 1
else               : a[4] = 0
if a[5] == 'N'     : a[5] = 1
else               : a[5] = 0

print(a)
if a == [1, 1, 1, 1, 1, 1]:
    print('Cum Laude')

elif a == [1, 1 ,1 ,1 ,1 ,0] or a == [1, 1, 1, 1, 0, 1]:
   print('Memuaskan')
