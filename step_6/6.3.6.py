# Пол и потолок
# Напишите программу, которая принимает на вход действительное число
# x и вычисляет по нему значение: ⌊x⌋+⌈x⌉

from math import floor, ceil

x = float(input())
print(floor(x) + ceil(x))
