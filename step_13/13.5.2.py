# Is Valid Triangle?
# a+b>c
# a+c>b
# b+c>a

# объявление функции
def is_valid_triangle(side1, side2, side3):
    flag = False
    if (side1 + side2) > side3 and (side1 + side3) > side2 and (side2 + side3) > side1:
        flag = True
    return flag


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))
