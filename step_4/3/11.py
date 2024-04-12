# Пересечение отрезков
# Найти пересечение двух отрезков на прямой:
# отрезок, тока или пустое множество.
# ---Входные данные
# a1, b1, a2, b2
# ---Выходные данные

a1, b1, a2, b2 = 5, 6, 6, 8
if a1 <= a2 < b1 and b2 > b1:
    print(a2, b1)
elif a2 <= a1 < b2 and b1 > b2:
    print(a1, b2)
elif a1 <= a2 and b2 <= b1:
    print(a2, b2)
elif a2 <= a1 and b1 <= b2:
    print(a1, b1)
elif a2 == b1:
    print(a2)
elif a1 == b2:
    print(a1)
else:
    print('пустое множество')


