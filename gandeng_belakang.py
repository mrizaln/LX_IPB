n = int(input())

kata = []
for i in range(n):
    kata.append(input())

l = min(len(ele) for ele in kata)

kat = [k[-l:] for k in kata]

print(''.join(k for k in kat), end = '\n')
