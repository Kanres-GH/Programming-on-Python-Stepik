s1, s2, encrypt, decrypt = list(input()), list(input()), list(input()), list(input())
for i in encrypt:
    print(s2[s1.index(i)], end = '')
print()
for i in decrypt:
    print(s1[s2.index(i)], end = '')