x, y, z = map(int, input().split())

if x > y and x > z:
    besar = x
    if y > z:
        kecil = z
    else:
        kecil = y

elif y > x and y > z:
    besar = y
    if x > z:
        kecil = z
    else:
        kecil = x

elif z > x and z > y:
    besar = z
    if x > y:
        kecil = y
    else:
        kecil = x

else:
    if x == y:
        if x > z:
            besar = x
            kecil = z
        else:
            besar = z
            kecil = x
    elif y == z:
        if z > x:
            besar = z
            kecil = x
        else:
            besar = x
            kecil = z
    elif x == z:
        if z > y:
            besar = z
            kecil = y
        else:
            besar = y
            kecil = z
    else:
        besar = x
        kecil = x

print(besar, kecil, sep = ' ', end = ' ')
