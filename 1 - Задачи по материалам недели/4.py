s = input()
pi = 3.14
if s == 'треугольник':
    a, b, c = int(input()), int(input()), int(input())
    p = (a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**0.5)
if s == 'прямоугольник':
    a, b = int(input()), int(input())
    print(a*b)
if s == 'круг':
    r = int(input())
    print(pi*r**2)