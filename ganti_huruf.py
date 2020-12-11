kata = input()
hurf = list(kata)

for i in range(len(kata) - 1):
    if kata[i + 1] == kata[0]: hurf[i + 1] = '_'

lett = ''
for i in hurf: lett += i
print(lett)
