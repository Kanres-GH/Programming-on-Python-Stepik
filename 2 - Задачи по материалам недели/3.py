n = [int(i) for i in input().split()]
l = []
x = int(input())
for i in range(len(n)):
    if n[i] == x:
        l.append(i)
if len(l) == 0:
    print('Отсутствует')
else:
    print(*l)