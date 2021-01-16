N = int(input())
inp = input()
outp = []

n = 1
k = 0

while k < len(inp):
    outp.append(inp[k])
    k = n * (N + 1)
    n += 1

st = ''.join(i for i in outp)
print(st)
