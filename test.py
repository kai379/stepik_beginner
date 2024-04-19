# Римские цифры
# Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру.
# Если число находится вне диапазона 1−10, то программа должна вывести текст «ошибка».
# В таблице приведены римские цифры для чисел от 1 до 10.

n = int(input())
if n == 1:
    print('I')
elif n == 2:
    print('II')
elif n == 3:
    print('III')
elif n == 4:
    print('IV')
elif n == 5:
    print('V')
elif n == 6:
    print('VI')
elif n == 7:
    print('VII')
elif n == 8:
    print('VIII')
elif n == 9:
    print('IX')
elif n == 10:
    print('X')
else:
    print('ошибка')


# n = int(input())
# if not 0 < n < 11:
#     print('ошибка')
# elif n < 4:
#     print(n*'I')
# elif n == 4:
#     print('IV')
# elif n < 9:
#     print('V' + (n-5)*'I')
# elif n < 11:
#     print((10-n)*'I' + 'X')
