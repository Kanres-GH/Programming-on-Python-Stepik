d = int(input())
p1 = []
for i in range(d):
    s1 = input().lower()
    p1.append(s1)
l = int(input())
for i in range(l):
    s2 = input().lower().split()
    for j in s2:
        if j not in p1:
            print(j)
            p1.append(j)