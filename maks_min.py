x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

maks = max(x, y, z)
minn = min(x, y, z)

print("%d %d" % (maks, minn), end = "")
