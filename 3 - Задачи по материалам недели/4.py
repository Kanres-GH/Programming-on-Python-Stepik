x = y = 0
n = int(input())
for i in range(n):
    s = input().split()
    s[1] = int(s[1])
    if s[0] == 'север':
        y += s[1]
    if s[0] == 'запад':
        x -= s[1]
    if s[0] == 'юг':
        y -= s[1]
    if s[0] == 'восток':
        x += s[1]
print(x, y)