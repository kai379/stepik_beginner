# Квадратное уравнение
# Даны три вещественных числа
# Напишите программу, которая находит вещественные корни квадратного уравнения:
# ax2+bx+c=0.
# Если уравнение имеет два корня, то следует вывести их в порядке возрастания.

from math import sqrt

a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = ((b * -1) - sqrt(d)) / (2 * a)
    x2 = ((b * -1) + sqrt(d)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
elif d == 0:
    print(-b / (a * 2))
else:
    print('Нет корней')
