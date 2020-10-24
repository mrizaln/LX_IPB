a = int(input())

if 500000 <= a <= 1000000:
    a = a - a * 0.2
elif a > 1000000:
    a = a - a * 0.3

a = int(a)
print(a)
