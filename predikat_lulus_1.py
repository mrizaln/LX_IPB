IPK         = float(input())
LamaStudi   = int(input())
NilaiC      = int(input())
NilaiD      = int(input())
KuliahUlang = input()
Sanksi      = input()

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
