print('Введите координаты и радиус круга')
x = float(input('x: '))
y = float(input('y: '))
r = float(input('r: '))


import math


# c = sqrt(x**2 + y**2)
hypot = math.sqrt(x**2 + y**2)
print(hypot)

if hypot <= r:
    print('Точка принадлежит кругу')
else:
    print('Точка вне круга')
