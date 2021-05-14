n = int(input())
l = []
for i in range(1, n + 1):
    for j in range(i):
        l.append(i)
for i in range(n):
    print(l[i], end = ' ')