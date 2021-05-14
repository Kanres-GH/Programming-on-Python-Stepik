n = [int(i) for i in input().split()]
sum = []
if len(n) == 1:
    print(n[0])
else:
    for i in range(len(n)):
        if i == len(n) - 1:
            sum += [n[-2] + n[0]]
        else:
            sum += [n[i - 1] + n[i + 1]]
print(*sum)