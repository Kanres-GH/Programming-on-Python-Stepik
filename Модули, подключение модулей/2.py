import sys
s = ''
s2 = ''
for i in range(1,len(sys.argv)):
    s += sys.argv[i]+' '
s2 = s
print(s2,end=' ')