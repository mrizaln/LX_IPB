str = input()

mid = len(str) // 2
str_rev = ''.join(reversed(str[:mid]))

if str[-mid:] == str_rev[:mid]: print('SAMA', end = '\n')
else: print('TIDAK SAMA', end = '\n')
