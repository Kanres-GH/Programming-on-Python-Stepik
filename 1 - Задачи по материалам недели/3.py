a, b, s = float(input()), float(input()), input()
if s == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        print(int(a)%int(b))
if s == '/':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a/b)
if s == 'pow':
    print(a**b)
if s == '*':
    print(a*b)
if s == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a//b)
if s == '+':
    print(a+b)
if s == '-':
    print(a-b)