a, b = map(int, input().split())

ganjil = []
for i in range(a, b+1):
    if i % 2 == 1:
        ganjil.append(i)

print(ganjil)
rataan = sum(ganjil) / len(ganjil)
print(rataan)
