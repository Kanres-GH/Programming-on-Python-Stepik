a, b = int(input()), int(input())
d = 1
while d%a!=0 or d%b!=0:
    d += 1
print(d)