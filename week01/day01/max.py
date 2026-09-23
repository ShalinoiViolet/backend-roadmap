a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))
if a > b and a > c:
    print('Наибольшее число:', a)
elif b > a and b > c:
    print('Наибольшее число:', b)
else:
    print('Наибольшее число:', c)
