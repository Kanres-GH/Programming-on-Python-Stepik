n = int(input())
if n%10 == 0 or 5<=n%10<=9 or 11<=n%100<=14:
    print(n, 'программистов')
elif n%10==1:
    print(n, 'программист')
else:
    print(n, 'программиста')