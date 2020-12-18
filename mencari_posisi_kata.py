paragraph = input().lower()
word = input().lower()

pos = paragraph.find(word) + 1

if pos: print(pos, end = '\n')
else: print('KATA TIDAK DITEMUKAN', end = '\n')
