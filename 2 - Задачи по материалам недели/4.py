a =[list(map(int, s.split())) for s in iter(input, 'end')]
for row in [[a[i-1][j]+a[(i+1) % len(a)][j]+a[i][j-1]+a[i][(j+1) % len(a[i])] for j in range(len(a[i]))] for i in range(len(a))]:
    print(*row)