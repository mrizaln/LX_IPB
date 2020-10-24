a, b, c = map(int, input().split())

d = 'Segitiga'
if a == b == c:
    d = d + ' sama-sisi'

else:
    if a == 90 or b == 90 or c == 90:
        d = d + ' siku-siku'
    elif a < 90 and b < 90 and c < 90:
        d = d + ' lancip'
    elif a > 90 or b > 90 or c > 90:
        d = d + ' tumpul'

if (a == b or a == c or b == c) and not (a == b == c):
   d = d + ' sama-kaki'

print(d)
