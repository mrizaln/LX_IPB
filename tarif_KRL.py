MIN, K, S, MAKS = map(int, input().split())
N = int(input())

if N <= K:
    print(MIN, end = '\n')
else:
    tarif = MIN + (N - K) * S
    if tarif > MAKS:
        print(MAKS, end = '\n')
    else:
        print(tarif, end = '\n')
