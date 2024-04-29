# Корректный email
# Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки (.).
# Напишите программу, проверяющую корректность email адреса.

mail = input()
DOT = '.'
AT = '@'
if DOT in mail and AT in mail:
    print('YES')
else:
    print('NO')
