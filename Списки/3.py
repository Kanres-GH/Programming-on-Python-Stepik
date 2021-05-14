n = sorted([int(i) for i in input().split()])
l = []
for i in range(1, len(n)):
    if n[i] == n[i - 1]:
        if n[i] not in l:
            l.append(n[i])
            
print(*l)