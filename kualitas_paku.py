def roundup(k):
    if k != int(k): k = k // 1 + 1
    return int(k)

n     = int(input())
pakls = [float(inp) for inp in input().split()[:n]]
bound = [float(inp) for inp in input().split()]
cost  = int(input())

unf = len(pakls)
loss = 0
for pak in pakls:
    if not (bound[0] <= pak <= bound[1]):
        unf  -= 1
        loss += cost * roundup(pak)

if unf == len(pakls): print ('100% paku memenuhi standar')
else:
    perc = round(100 * unf / len(pakls))
    print('{}% paku memenuhi standar, kerugian {} rupiah'.format(perc, loss))
