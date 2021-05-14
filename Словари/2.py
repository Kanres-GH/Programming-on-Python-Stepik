s = [i.lower() for i in input().split()]
d = dict()
for i in s:
    d[i] = 0
for i in s:
    d[i] += 1
for i in d:
    print(i, d[i])