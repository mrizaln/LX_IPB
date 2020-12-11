def factorial(a):
    if a == 1:
        return a
    else:
        return factorial(a-1) * a

s = input()
n = int(s[:(len(s)-1)])
h = factorial(n)

print(h, end = '\n')
