n = int(input())
if n%4==0 and n%100!=0:
    print('Високосный')
elif n%400==0:
    print('Високосный')
else:
    print('Обычный')