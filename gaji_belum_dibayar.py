voc = ['a', 'i', 'u', 'e', 'o']

inp = input()
inp = inp[::-1]
ls_inp = list(inp)

for i in voc:
    for j in range(len(inp)):
        if i == inp[j]: ls_inp[j] = '%'
    print(ls_inp)

for k in ls_inp: print(k, end = '')
print()
